
--- 
title:  Python 中 sqlite3 使用 executemany 批量插入数据 
tags: []
categories: [] 

---
千言万语，不如一个 demo 来得深沉。就目前我所知道的， Python 里边 MySQL 和 sqlite 都是可以使用 executemany 批量插入大量数据的，而且效率基本上是普通插入的数量级提升。

### 使用 executemany 的好处

#### 效率高

我自己测试过，同样的一万多条数据，普通插入用时 54.5 秒，使用 executemany 用时 0.22 秒。效率这玩意儿，我就不多赘述了。

**不过 sql 稍微有点区别的是，sqlite 是使用的 ? 作为占位符，而不是 %s，%d 之类的哟！正确方法的例子如下：**

```
sql = 'insert into filelist (pkgKey, dirname, filenames, filetypes) values (?, ?, ?, ?);'
```

```
import sqlite3

class DbOperate(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(DbOperate, cls).__new__(cls)
        return cls._instance

    def __init__(self, db_name):
        self.db_name = db_name
        self.connect = sqlite3.connect(self.db_name)
        self.cursor = self.connect.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.close()

    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()

    def executemany_sql(self, sql, data_list):
        # example:
        # sql = 'insert into filelist (pkgKey, dirname, filenames, filetypes) values (?, ?, ?, ?);'
        # data_list = [(1, '/etc/sysconfig', 'openshift_option', 'f'), (1, '/usr/share/doc', 'adb-utils-1.6', 'd')]
        try:
            self.cursor.executemany(sql, data_list)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            raise Exception("executemany failed")

sqlite_path = "***.sqlite"
with DbOperate(sqlite_path) as db:
    t1 = time.clock()
    sql = 'insert into filelist (pkgKey, dirname, filenames, filetypes) values (?, ?, ?, ?);'
    data_list = [(1, '/etc/sysconfig', 'openshift_option', 'f'), (1, '/usr/share/doc', 'adb-utils-1.6', 'd')]
    db.executemany_sql(sql, data_list)
    t2 = time.clock()
    print('insert data into filelist cost %s seconds' % (t2 - t1))
    print('success insert data into filelist with %s' % sqlite_path)
```

#### 不易受特殊字符影响

我之前单条插入的时候像下面这么搞过：

```
with DbOperate(sqlite_path) as db:
    t1 = time.clock()
    for item in packages:
        insert_data = f'insert into packages values {item};'
        insert_data = insert_data.replace('None', 'null')
        print(insert_data)
        db.execute_sql(insert_data)
    t2 = time.clock()
```

结果由于部分字段里边总是有很多特殊字符，像单引号，转义字符之类，直接拼接 sql 语句会由于各种原因导致 sql 语句不满足 sqlite 的语法，从而数据插入时总是会报各种错，搞得我很恼火。用 executemany 竟然没有这些报错了，我其实也是有点懵逼的，或许是 executemany 是将参数对应着传进去的缘故吧：

```
Traceback (most recent call last):
  File "C:/Users/lukaiyi/insight-tool/test.py", line 144, in &lt;module&gt;
    insert_data_sqlite(sqlite_list, filelist, packages)
  File "C:/Users/lukaiyi/insight-tool/test.py", line 42, in insert_data_sqlite
    db.execute_sql(insert_data)
  File "C:\Users\lukaiyi\insight-tool\src\tool\utils.py", line 92, in execute_sql
    self.cursor.execute(sql)
sqlite3.OperationalError: near "s": syntax error
```

 
