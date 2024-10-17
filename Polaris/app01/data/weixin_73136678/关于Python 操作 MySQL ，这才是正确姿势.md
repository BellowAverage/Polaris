
--- 
title:  关于Python 操作 MySQL ，这才是正确姿势 
tags: []
categories: [] 

---
使用Python进行MySQL的库主要有三个，Python-MySQL（更熟悉的名字可能是MySQLdb），PyMySQL和SQLAlchemy。

Python-MySQL资格最老，核心由C语言打造，接口精炼，性能最棒，缺点是环境依赖较多，安装复杂，近两年已停止更新，只支持Python2，不支持Python3。

PyMySQL为替代Python-MySQL而生，纯python打造，接口与Python-MySQL兼容，安装方便，支持Python3。

SQLAlchemy是一个ORM框架，它并不提供底层的数据库操作，而是要借助于MySQLdb、PyMySQL等第三方库来完成，目前SQLAlchemy在Web编程领域应用广泛。

本文主要介绍PyMySQL的正确使用方法，示例代码都是选自实战项目。

### 安装

简单的方式：

```
pip install pymysql
复制代码
```

如果无法联网，需要进行离线安装，例如：

```
pip install pymysql-x.x.x.tar.gz
复制代码
```

### 导入

```
import pymysql
复制代码
```

### 连接

```
def connect_wxremit_db():
    return pymysql.connect(host='10.123.5.28',
                           port=3306,
                           user='root',
                           password='root1234',
                           database='db_name',
                           charset='latin1')
复制代码
```

### 查询

```
def query_country_name(cc2):
    sql_str = ("SELECT Fcountry_name_zh"
                + " FROM t_country_code"
                + " WHERE Fcountry_2code='%s'" % (cc2))
    logging.info(sql_str)

    con = mysql_api.connect_wxremit_db()
    cur = con.cursor()
    cur.execute(sql_str)
    rows = cur.fetchall()
    cur.close()
    con.close()

    assert len(rows) == 1, 'Fatal error: country_code does not exists!'
    return rows[0][0]
复制代码
```

### 简单插入

```
def insert_file_rec(self, file_name, file_md5):
        con = mysql_api.connect_wxremit_db()
        cur = con.cursor()
        try:
            sql_str = ("INSERT INTO t_forward_file (Ffile_name, Ffile_md5)", 
                       + " VALUES ('%s', '%s')" % (file_name, file_md5))
            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
            logging.exception('Insert operation error')
            raise
        finally:
            cur.close()
            con.close()
复制代码
```

### 批量插入

```
remit_ids = [('1234', 'CAD'), ('5678', 'HKD')]

con = mysql_api.connect_wxremit_db()
        cur = con.cursor()
        try:
                cur.executemany("INSERT INTO t_order (Fremit_id, Fcur_type, Fcreate_time"
                                                + " VALUES (%s, %s, now())", new_items)
                assert cur.rowcount == len(remit_ids), 'my error message'
                con.commit()
        except Exception as e:
                con.rollback()
                logging.exception('Insert operation error')
        finally:
                cur.close()
                con.close()
复制代码
```

### 更新

```
    def update_refund_trans(self, remit_id):
        con = mysql_api.connect_wxremit_db()
        cur = con.cursor()
        try:
            sql_str = ("SELECT Fremit_id"
                       + " FROM t_wxrefund_trans"
                       + " WHERE Fremit_id='%s'" % remit_id
                       + " FOR UPDATE")
            logging.info(sql_str)

            cur.execute(sql_str)
            assert cur.rowcount == 1, 'Fatal error: The wx-refund record be deleted!'

            sql_str = ("UPDATE t_wxrefund_trans"
                        + " SET Fcheck_amount_flag=1"
                        + ", Fmodify_time=now()"
                        + " WHERE Fremit_id='%s'" % remit_id
            logging.info(sql_str)
            cur.execute(sql_str)

            assert cur.rowcount == 1, 'The number of affected rows not equal to 1'
            con.commit()
        except:
            con.rollback()
            logging.exception('Update operation error')
            raise
        finally:
            cur.close()
            con.close()
复制代码
```

PyMySQL已经相当成熟，和Python-MySQL一样，它在很多Linux发行版本中都是可选的安装组件。
