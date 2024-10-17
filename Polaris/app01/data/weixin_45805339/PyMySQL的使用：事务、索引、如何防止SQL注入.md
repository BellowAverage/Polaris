
--- 
title:  PyMySQL的使用：事务、索引、如何防止SQL注入 
tags: []
categories: [] 

---
## PyMySQL的使用

### 事务

#### 介绍
- 事务就是用户定义的一系列执行SQL语句的操作, 这些操作要么完全地执行，要么完全地都不执行， 它是一个不可分割的工作执行单元。
#### 事务的使用场景:
- 在日常生活中，有时我们需要进行银行转账，这个银行转账操作背后就是需要执行多个SQL语句，假如这些SQL执行到一半突然停电了，那么就会导致这个功能只完成了一半，这种情况是不允许出现，要想解决这个问题就需要通过事务来完成。
#### 事务的四大特性
<li>原子性(Atomicity) 
  <ul>- 一个事务必须被视为一个不可分割的最小工作单元，整个事务中的所有操作要么全部提交成功，要么全部失败回滚，对于一个事务来说，不可能只执行其中的一部分操作，这就是事务的原子性- 数据库总是从一个一致性的状态转换到另一个一致性的状态。（在前面的例子中，一致性确保了，即使在转账过程中系统崩溃，支票账户中也不会损失200美元，因为事务最终没有提交，所以事务中所做的修改也不会保存到数据库中。）- 通常来说，一个事务所做的修改操作在提交事务之前，对于其他事务来说是不可见的。（在前面的例子中，当执行完第三条语句、第四条语句还未开始时，此时有另外的一个账户汇总程序开始运行，则其看到支票帐户的余额并没有被减去200美元。）- 一旦事务提交，则其所做的修改会永久保存到数据库。
#### 说明:
- 事务能够保证数据的完整性和一致性，让用户的操作更加安全。
#### 事务的使用
- 在使用事务之前，先要确保表的存储引擎是 InnoDB 类型, 只有这个类型才可以使用事务，MySQL数据库中表的存储引擎默认是 InnoDB 类型。<li>– 查看MySQL数据库支持的表的存储引擎 
  <ul>- show engines;- 常用的表的存储引擎是 InnoDB 和 MyISAM- InnoDB 是支持事务的- MyISAM 不支持事务，优势是访问速度快，对事务没有要求或者以select、insert为主的都可以使用该存储引擎来创建表- 通过创表语句可以得知，goods表的存储引擎是InnoDB。<li>修改表的存储引擎使用: alter table 表名 engine = 引擎类型; 
    <ul>- 比如: alter table students engine = ‘MyISAM’;
#### 开启事务:
- begin;- 或者start transaction;<li>说明: 
  <ul>- 开启事务后执行修改命令，变更数据会保存到MySQL服务端的缓存文件中，而不维护到物理表中- MySQL数据库默认采用自动提交(autocommit)模式，如果没有显示的开启一个事务,那么每条sql语句都会被当作一个事务执行提交的操作- 当设置autocommit=0就是取消了自动提交事务模式，直到显示的执行commit和rollback表示该事务结束。
#### 提交事务:
<li>将本地缓存文件中的数据提交到物理表中，完成数据的更新。 
  <ul>- commit;
#### 回滚事务:
<li>放弃本地缓存文件中的缓存数据, 表示回到开始事务前的状态 
  <ul>- rollback;
#### 事务演练的SQL语句:

begin; insert into students(name) values(‘李白’); – 查询数据，此时有新增的数据, 注意: 如果这里后续没有执行提交事务操作，那么数据是没有真正的更新到物理表中 select * from students; – 只有这里提交事务，才把数据真正插入到物理表中 commit;

– 新打开一个终端，重新连接MySQL数据库，查询students表,这时没有显示新增的数据，说明之前的事务没有提交，这就是事务的隔离性 – 一个事务所做的修改操作在提交事务之前，对于其他事务来说是不可见的 select * from students;

### 索引

#### 介绍
- 索引在MySQL中也叫做“键”，它是一个特殊的文件，它保存着数据表里所有记录的位置信息，更通俗的来说，数据库索引好比是一本书前面的目录，能加快数据库的查询速度。<li>应用场景: 
  <ul>- 当数据库中数据量很大时，查找数据会变得很慢，我们就可以通过索引来提高数据库的查询效率。
#### 索引的使用
<li>查看表中已有索引: 
  <ul>- show index from 表名;- 主键列会自动创建索引
#### 索引的创建:
<li>– 创建索引的语法格式 
  <ul>- – alter table 表名 add index 索引名[可选](列名, …)- alter table classes add index my_name (name);- 索引名不指定，默认使用字段名
#### 索引的删除:
<li>– 删除索引的语法格式 
  <ul>- – alter table 表名 drop index 索引名- show create table classes;- alter table classes drop index my_name;
#### 案例-验证索引查询性能
<li>创建测试表testindex: 
  <ul>- create table test_index(title varchar(10));
#### 联合索引
<li> 介绍 – 创建teacher表 create table teacher ( id int not null primary key auto_increment, name varchar(10), age int ); – 创建联合索引 alter table teacher add index (name,age); 
  <ul>- 联合索引又叫复合索引，即一个索引覆盖表中两个或者多个字段，一般用在多个字段一起查询的时候。
联合索引的好处:
- 减少磁盘空间开销，因为每创建一个索引，其实就是创建了一个索引文件，那么会增加磁盘空间的开销。
联合索引的最左原则
-  在使用联合索引的时候，我们要遵守一个最左原则,即index(name,age)支持 name 、name 和 age 组合查询,而不支持单独 age 查询，因为没有用到创建的联合索引。 -  最左原则示例: – 下面的查询使用到了联合索引 select * from stu where name=‘张三’ – 这里使用了联合索引的name部分 select * from stu where name=‘李四’ and age=10 – 这里完整的使用联合索引，包括 name 和 age 部分 – 下面的查询没有使用到联合索引 select * from stu where age=10 – 因为联合索引里面没有这个组合，只有 name | name age 这两种组合 <li> 说明: 
    <ul>- 在使用联合索引的查询数据时候一定要保证联合索引的最左侧字段出现在查询条件里面，否则联合索引失效
#### MySQL中索引的优点和缺点和使用原则
<li>优点： 
  <ul>- 加快数据的查询速度- 创建索引会耗费时间和占用磁盘空间，并且随着数据量的增加所耗费的时间也会增加- 通过优缺点对比，不是索引越多越好，而是需要自己合理的使用。- 对经常更新的表就避免对其进行过多索引的创建，对经常用于查询的字段应该创建索引，- 数据量小的表最好不要使用索引，因为由于数据较少，可能查询全部数据花费的时间比遍历索引的时间还要短，索引就可能不会产生优化效果。- 在一字段上相同值比较多不要建立索引，比如在学生表的"性别"字段上只有男，女两个不同值。相反的，在一个字段上不同值较多可是建立索引。
### pymysql

#### 使用
<li> 
  - 导包 
  <ul>- import pymysql1. 创建连接对象- pymysql.connect(参数列表)1. 获取游标对象- cursor =conn.cursor()1. 执行SQL语句- row_count = cursor.execute(sql)1. 获取查询结果集- result = cursor.fetchall()1. 将修改操作提交到数据库- conn.commit()1. 回滚数据- conn.rollback()1. 关闭游标- cursor.close()1. 关闭连接- conn.close()
#### pymysql完成数据的查询操作

```
import pymysql

# 创建连接对象

conn = pymysql.connect(host='localhost', port=3306, user='root', password='mysql',database='python', charset='utf8')

# 获取游标对象

cursor = conn.cursor()

# 查询 SQL 语句

sql = "select * from students;"

# 执行 SQL 语句 返回值就是 SQL 语句在执行过程中影响的行数

row_count = cursor.execute(sql)
print("SQL 语句执行影响的行数%d" % row_count)

# 取出结果集中一行数据,　例如:(1, '张三')

# print(cursor.fetchone())

# 取出结果集中的所有数据, 例如:((1, '张三'), (2, '李四'), (3, '王五'))

for line in cursor.fetchall():
    print(line)

# 关闭游标

cursor.close()

# 关闭连接

conn.close()

### pymysql完成对数据的增删改

import pymysql

# 创建连接对象

conn = pymysql.connect(host='localhost', port=3306, user='root', password='mysql',database='python', charset='utf8')

# 获取游标对象

cursor = conn.cursor()

try:
    # 添加 SQL 语句
    # sql = "insert into students(name) values('刘璐'), ('王美丽');"
    # 删除 SQ L语句
    # sql = "delete from students where id = 5;"
    # 修改 SQL 语句
    sql = "update students set name = '王铁蛋' where id = 6;"
    # 执行 SQL 语句
    row_count = cursor.execute(sql)
    print("SQL 语句执行影响的行数%d" % row_count)
    # 提交数据到数据库
    conn.commit()
except Exception as e:
    # 回滚数据， 即撤销刚刚的SQL语句操作
    conn.rollback()

# 关闭游标

cursor.close()

# 关闭连接

conn.close()

### 防止SQL注入

from pymysql import connect

def main():

find_name = input("请输入物品名称：")

# 创建Connection连接
conn = connect(host='localhost',port=3306,user='root',password='mysql',database='jing_dong',charset='utf8')
# 获得Cursor对象
cs1 = conn.cursor()

# 非安全的方式
# 输入 ' or 1 = 1 or '   (单引号也要输入)
# sql = "select * from goods where name='%s'" % find_name
# print("""sql===&gt;%s&lt;====""" % sql)
# # 执行select语句，并返回受影响的行数：查询所有数据
# count = cs1.execute(sql)

# 安全的方式
# 构造参数列表
params = [find_name]
# 执行select语句，并返回受影响的行数：查询所有数据
count = cs1.execute("select * from goods where name=%s", params)
# 注意：
# 如果要是有多个参数，需要进行参数化
# 那么params = [数值1, 数值2....]，此时sql语句中有多个%s即可
# %s 不需要带引号

# 打印受影响的行数
print(count)
# 获取查询的结果
# result = cs1.fetchone()
result = cs1.fetchall()
# 打印查询的结果
print(result)
# 关闭Cursor对象
cs1.close()
# 关闭Connection对象
conn.close()


if __name__ == '__main__':
    main()

```
<li>什么是SQL注入? 
  <ul>- 用户提交带有恶意的数据与SQL语句进行字符串方式的拼接，从而影响了SQL语句的语义，最终产生数据泄露的现象。<li>SQL语句参数化 
    <ul>- SQL语言中的参数使用%s来占位，此处不是python中的字符串格式化操作- 将SQL语句中%s占位所需要的参数存在一个列表中，把参数列表传递给execute方法中第二个参数