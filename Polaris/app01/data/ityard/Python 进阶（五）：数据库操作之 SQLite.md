
--- 
title:  Python 进阶（五）：数据库操作之 SQLite 
tags: []
categories: [] 

---


#### 目录
- - - <ul><li>- - - - - - - - - - 


## 1. 简介

SQLite 是一种嵌入式关系型数据库，其本质就是一个文件，它占用资源低、处理速度快、跨平台、可与 Python、Java 等多种编程语言结合使用。

SQLite 是一个进程内的库，可以自给自足、无服务器、无需配置、支持事务，Python 可以通过 sqlite3 模块与 SQLite3 集成（3 是版本号），Python 2.5.x 以上版本内置了 sqlite3 模块，我们可以直接使用。

## 2. 数据类型

### 2.1 存储类型

存储类型是数据保存成文件后的表现形式，主要包括如下几种：

|类型<th align="left">描述</th>
|------
|NULL<td align="left">空值</td>
|REAL<td align="left">浮点数类型</td>
|TEXT<td align="left">字符串，使用数据库编码（UTF-8、UTF-16BE 或 UTF-16LE）存储</td>
|BLOB<td align="left">二进制表示</td>
|INTEGER<td align="left">有符号的整数类型</td>

### 2.2 亲和类型

亲和类型是数据库表中列数据对应存储类型的倾向性，当数据插入时，字段的数据将会优先采用亲缘类型作为值的存储方式，主要包括如下几种：

|类型<th align="left">描述</th>
|------
|NONE<td align="left">不做任何转换，直接以该数据所属的数据类型进行存储</td>
|TEXT<td align="left">该列使用存储类型 NULL、TEXT 或 BLOB 存储数据</td>
|NUMERIC<td align="left">该列可以包含使用所有五个存储类型的值</td>
|REAL<td align="left">类似于 NUMERIC，区别是它会强制把整数值转换为浮点类型</td>
|INTEGER<td align="left">类似于 NUMERIC，区别是在执行 CAST 表达式时</td>

### 2.3 声明类型

声明类型是我们写 SQL 时字段定义的类型，常用的声明类型与亲和类型具有如下对应关系：

<th align="left">声明类型</th>|亲和类型
|------
<td align="left">BLOB</td>|NONE
<td align="left">DOUBLE、FLOAT</td>|REAL
<td align="left">VARCHAR、TEXT、CLOB</td>|TEXT
<td align="left">INT、INTEGER、TINYINT、BIGINT</td>|INTEGER
<td align="left">DECIMAL、BOOLEAN、DATE、DATETIME</td>|NUMERIC

## 3. 基本使用

### 3.1 连接数据库

```
# 导入模块
import sqlite3
# 连接数据库
conn = sqlite3.connect('test.db')

```

数据库不存在会被自动创建。

### 3.2 游标

连接数据库后，需要通过游标进行相应 SQL 操作，所以要先创建游标。

```
# 创建游标
cs = conn.cursor()

```

### 3.3 建表

我们在 test.db 库中新建一张表 person。

```
# 创建表
cs.execute('''CREATE TABLE person
       (id varchar(20) PRIMARY KEY,
        name varchar(20));''')
# 关闭 cursor
cs.close()
# 提交当前事务
conn.commit()
# 关闭连接
conn.close()

```

### 3.4 新增

向表 person 中插入几条数据。

```
# 导入模块
import sqlite3
# 连接数据库
conn = sqlite3.connect('test.db')
# 创建游标
cs = conn.cursor()
# 新增
cs.execute("INSERT INTO person (id, name) VALUES ('1', '张三')")
cs.execute("INSERT INTO person (id, name) VALUES ('2', '李四')")
cs.execute("INSERT INTO person (id, name) VALUES ('3', '王五')")
cs.execute("INSERT INTO person (id, name) VALUES ('4', '赵六')")
cs.execute("INSERT INTO person (id, name) VALUES ('5', '朱七')")
cs.close()
conn.commit()
conn.close()

```

### 3.5 删除

删除 person 表中 id 为 3 这条数据。

```
# 导入模块
import sqlite3
# 连接数据库
conn = sqlite3.connect('test.db')
# 创建游标
cs = conn.cursor()
# 删除
cs.execute("DELETE FROM person WHERE id = '3'")
conn.commit()
cs.close()
conn.close()

```

### 3.6 修改

修改一下 person 表中 id 为 1 这条数据的 name 属性值。

```
# 导入模块
import sqlite3
# 连接数据库
conn = sqlite3.connect('test.db')
# 创建游标
cs = conn.cursor()
# 修改
cs.execute("UPDATE person set name = '张四' WHERE id = '1'")
conn.commit()
cs.close()
conn.close()

```

### 3.7 查询

看一下查询操作。

```
# 导入模块
import sqlite3
# 连接数据库
conn = sqlite3.connect('test.db')
# 创建游标
cs = conn.cursor()
# 查询
cs.execute("SELECT id, name FROM person")
# 获取查询结果集中的下一行
print(cs.fetchone())
# 获取查询结果集中的下几行
print(cs.fetchmany(2))
# 获取查询结果集中剩下的所有行
print(cs.fetchall())
cs.close()
conn.close()

```

### 3.8 图形化工具

我们可以通过 SQLite 图形化工具 SQLiteStudio 更加直观的查看其表结构、数据等，下载地址为：，进到下载页面后根据自己的系统选择下载版本，以 Windows 为例：选择免安装版 `SQLiteStudio-3.2.1.zip`，下载完毕后解压，再点击 SQLiteStudio.exe 启动。

启动后依次点击：Database、Add a database，弹出如下窗口： <img src="https://img-blog.csdnimg.cn/20200222094114518.PNG#pic" alt="" width="300"> 我们点击`文件`下方右侧的`绿色加号或文件夹`按钮，接着选择 `test.db` 文件，选完后点击`测试连接`按钮，如果连接正常，再点击 OK 按钮，最后我们就可以通过 SQLiteStudio 对 test.db 进行直观的查看了。 <img src="https://img-blog.csdnimg.cn/20200222094752269.PNG#pic" alt="" width="600">

<img src="https://img-blog.csdnimg.cn/20200215093746977.png#pic_center" alt="" width="500">
