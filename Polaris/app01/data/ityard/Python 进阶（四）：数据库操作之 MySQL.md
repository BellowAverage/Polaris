
--- 
title:  Python 进阶（四）：数据库操作之 MySQL 
tags: []
categories: [] 

---


#### 目录
- - - <ul><li>- - - 


## 1. 简介

MySQL 是目前使用最广泛的数据库之一，它有着良好的性能，能够跨平台，支持分布式，能够承受高并发。如果还没有安装 MySQL，可以查看  | 。

Python 大致有如下 5 种方式操作 MySQL。
-  **MySQL-python** MySQL-python 也称 MySQLdb，基于 C 库开发，曾经是一个十分流行的 MySQL 驱动，具有出色的性能，但其早已停更，仅支持 Python2，不支持 Python3，现在基本不推荐使用了，取而代之的是它的衍生版。 -  **mysqlclient** MySQLdb 的 Fork 版本，完全兼容 MySQLdb，支持 Python3，它是 Django ORM 的依赖工具，如果你喜欢用原生 SQL 操作数据库，那么推荐使用它。 -  **PyMySQL** PyMySQL 采用纯 Python 开发，兼容 MySQLdb，性能不如 MySQLdb，安装方便，支持 Python3。 -  **peewee** peewee 是一个流行的 ORM 框架，实现了对象与数据库表的映射，兼容多种数据库，我们无需知道原生 SQL，只要了解面向对象的思想就可以简单、快速的操作相应数据库，支持 Python3。 -  **SQLAlchemy** SQLAlchemy 是一个 ORM 框架，同时也支持原生 SQL，支持 Python3，它类似于 Java 的 Hibernate 框架。 
## 2. 实际操作

因为 MySQLdb 不支持 Python3，这里我们只介绍其中后 4 中方式的使用，先使用如下建表语句创建一张简单的数据库表。

```
CREATE TABLE student (
  id int(10) AUTO_INCREMENT PRIMARY KEY,
  name varchar(255) NOT NULL,
  age int(10) NOT NULL
);

```

### 2.1 mysqlclient

执行 `pip install mysqlclient` 进行安装，看一下具体操作。

**新增**

```
import MySQLdb

connect = MySQLdb.connect(
     # 主机
     host='localhost',
     # 端口号
     port=3306,
     # 用户名
     user='root',
     # 密码
     passwd='root',
     # 数据库名称
     db='test',
     # 指定字符的编、解码格式
     use_unicode=True,
     charset='utf8')
# 先获取游标，再进行相应 SQL 操作
cursor = connect .cursor()
# 执行新增 SQL
sql = 'insert into student (name, age) values(%s,%s);'
data = [
    ('张三', '22'),
    ('李四', '23')
]
cursor.executemany(sql, data)
# 提交
connect.commit()
# 关闭
cursor.close()
connect.close()

```

**查询**

```
import MySQLdb

connect = MySQLdb.connect(
     host='localhost',
     port=3306,
     user='root',
     passwd='root',
     db='test',
     use_unicode=True,
     charset='utf8')
cursor = connect.cursor()
cursor.execute('SELECT * FROM student')
print(cursor.fetchall())
cursor.close()
connect.close()

```

cursor 查看方法
- fetchone() 获取结果集的下一行- fetchmany(size) 获取结果集的下几行务- fetchall() 获取结果集中剩下的所有行
**修改**

```
import MySQLdb

connect = MySQLdb.connect(
     host='localhost',
     port=3306,
     user='root',
     passwd='root',
     db='test',
     use_unicode=True,
     charset='utf8')
cursor = connect.cursor()
cursor.execute("UPDATE student SET name='张四' WHERE id = 1")
connect.commit()
cursor.close()
connect.close()

```

**删除**

```
import MySQLdb

connect = MySQLdb.connect(
     host='localhost',
     port=3306,
     user='root',
     passwd='root',
     db='test',
     use_unicode=True,
     charset='utf8')
cursor = connect.cursor()
cursor.execute("DELETE FROM student WHERE id = 1")
connect.commit()
cursor.close()
connect.close()

```

### 2.2 PyMySQL

执行 `pip install pymysql` 进行安装，使用方式与 mysqlclient 基本类似。

```
import pymysql

connect = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='test',
    charset='utf8'
)
cursor = connect.cursor()
sql = 'insert into student (name, age) values(%s,%s);'
data = [
    ('张三', '22'),
    ('李四', '23')
]
cursor.executemany(sql, data)
connect.commit()
cursor.execute('SELECT * FROM student')
print(cursor.fetchall())
cursor.close()
connect.close()

```

### 2.3 peewee

执行 `pip install peewee` 进行安装，看一下具体操作。

**定义映射类**

```
from peewee import *

# 连接数据库
db = MySQLDatabase('test',
                   host='localhost',
                   port=3306,
                   user='root',
                   passwd='root',
                   charset='utf8')
# 映射类
class Teacher(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    age =  IntegerField()
    class Meta:
        database = db
# 创建表
db.create_tables([Teacher])

```

**新增**

```
from peewee import *

db = MySQLDatabase('test',
                   host='localhost',
                   port=3306,
                   user='root',
                   passwd='root',
                   charset='utf8')
class Teacher(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    age =  IntegerField()
    class Meta:
        database = db
t1 = Teacher(name='张三', age=22)
t2 = Teacher(name='李四', age=33)
t3 = Teacher(name='王五', age=33)
t1.save()
t2.save()
t3.save()

```

**查询**

```
from peewee import *

db = MySQLDatabase('test',
                   host='localhost',
                   port=3306,
                   user='root',
                   passwd='root',
                   charset='utf8')
class Teacher(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    age =  IntegerField()
    class Meta:
        database = db
# 查询单条数据
t = Teacher.get(Teacher.id == 1)
print('name：', t.name)
# 查询多条
ts = Teacher.select().where(Teacher.age == 33)
for t in ts:
    print('name：', t.name)

```

**修改**

```
from peewee import *

db = MySQLDatabase('test',
                   host='localhost',
                   port=3306,
                   user='root',
                   passwd='root',
                   charset='utf8')
class Teacher(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    age =  IntegerField()
    class Meta:
        database = db
t = Teacher.update({<!-- -->Teacher.name: '张四'}).where(Teacher.id == 1)
t.execute()

```

**删除**

```
from peewee import *

db = MySQLDatabase('test',
                   host='localhost',
                   port=3306,
                   user='root',
                   passwd='root',
                   charset='utf8')
class Teacher(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    age =  IntegerField()
    class Meta:
        database = db
Teacher.delete().where(Teacher.id == 2).execute()

```

### 2.4 SQLAlchemy

执行 `pip install sqlalchemy` 进行安装，看一下具体操作。

**定义映射类**

```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/test?charset=utf8',
                       # 打印执行语句
                       echo=True,
                       # 连接池大小
                       pool_size=10,
                       # 指定时间内回收连接
                       pool_recycle=3600)
# 映射基类
Base = declarative_base()
# 具体映射类
class Teacher(Base):
    # 指定映射表名
    __tablename__ = 'teacher'
    # 映射字段
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    age = Column(Integer)
# 创建表
Base.metadata.create_all(engine)    

```

**新增**

```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/test?charset=utf8',
                       # 打印执行语句
                       echo=True,
                       # 连接池大小
                       pool_size=10,
                       # 指定时间内回收连接
                       pool_recycle=3600)
# 映射基类
Base = declarative_base()
# 具体映射类
class Teacher(Base):
    # 指定映射表名
    __tablename__ = 'teacher'
    # 映射字段
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    age = Column(Integer)
Session = sessionmaker(bind=engine)
# 创建 Session 类实例
session = Session()
ls = []
t1 = Teacher(name='张三', age=22)
t2 = Teacher(name='李四', age=33)
t3 = Teacher(name='王五', age=33)
ls.append(t1)
ls.append(t2)
ls.append(t3)
session.add_all(ls)
session.commit()
session.close()

```

**查询**

```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/test?charset=utf8',
                       # 打印执行语句
                       echo=True,
                       # 连接池大小
                       pool_size=10,
                       # 指定时间内回收连接
                       pool_recycle=3600)
# 映射基类
Base = declarative_base()
# 具体映射类
class Teacher(Base):
    # 指定映射表名
    __tablename__ = 'teacher'
    # 映射字段
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    age = Column(Integer)
Session = sessionmaker(bind=engine)
# 创建 Session 类实例
session = Session()
# 查询一条数据，filter 相当于 where 条件
t = session.query(Teacher).filter(Teacher.id==1).one()
print('---', t.name)
# 查询所有数据
ts = session.query(Teacher).filter(Teacher.age==33).all()
for t in ts:
    print('===', t.name)

```

**修改**

```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/test?charset=utf8',
                       # 打印执行语句
                       echo=True,
                       # 连接池大小
                       pool_size=10,
                       # 指定时间内回收连接
                       pool_recycle=3600)
# 映射基类
Base = declarative_base()
# 具体映射类
class Teacher(Base):
    # 指定映射表名
    __tablename__ = 'teacher'
    # 映射字段
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    age = Column(Integer)
Session = sessionmaker(bind=engine)
# 创建 Session 类实例
session = Session()
t = session.query(Teacher).filter(Teacher.id==1).one()
print('修改前名字--&gt;', t.name)
t.name = '张四'
session.commit()
print('修改后名字--&gt;', t.name)

```

**删除**

```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/test?charset=utf8',
                       # 打印执行语句
                       echo=True,
                       # 连接池大小
                       pool_size=10,
                       # 指定时间内回收连接
                       pool_recycle=3600)
# 映射基类
Base = declarative_base()
# 具体映射类
class Teacher(Base):
    # 指定映射表名
    __tablename__ = 'teacher'
    # 映射字段
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    age = Column(Integer)
Session = sessionmaker(bind=engine)
# 创建 Session 类实例
session = Session()
t = session.query(Teacher).filter(Teacher.id==1).one()
session.delete(t)
session.commit()

```

<img src="https://img-blog.csdnimg.cn/20200215093746977.png#pic_center" alt="" width="500">
