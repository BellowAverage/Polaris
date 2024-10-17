
--- 
title:  MySQL—SQL优化详解（上） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**努力不一定有回报，但一定会有收获加油！一起努力，共赴美好人生！** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 **♥️小刘私信可以随便问，只要会绝不吝啬，感谢CSDN让你我相遇！** 


**前言**

**本章讲解SQL语言中的优化**



**目录**







































### **SQL****优化 **

#### **1 ****插入数据 **

#### **1.1 insert**

如果我们需要一次性往数据库表中插入多条记录，可以从以下三个方面进行优化。

```
insert into tb_test values(1,'tom');
insert into tb_test values(2,'cat');
insert into tb_test values(3,'jerry');
```

#### 1). 优化方案一

批量插入数据

```
Insert into tb_test values(1,'Tom'),(2,'Cat'),(3,'Jerry');
```

#### 2). 优化方案二 

手动控制事务

```
start transaction;
insert into tb_test values(1,'Tom'),(2,'Cat'),(3,'Jerry');
insert into tb_test values(4,'Tom'),(5,'Cat'),(6,'Jerry');
insert into tb_test values(7,'Tom'),(8,'Cat'),(9,'Jerry');
commit;
```

#### 3). 优化方案三

主键顺序插入，性能要高于乱序插入。

```
主键乱序插入 : 8 1 9 21 88 2 4 15 89 5 7 3
主键顺序插入 : 1 2 3 4 5 7 8 9 15 21 88 89
```

### **1.2 ****大批量插入数据**

如果一次性需要插入大批量数据(比如: 几百万的记录)，使用insert语句插入性能较低，此时可以使

用MySQL数据库提供的load指令进行插入。操作如下：

<img alt="" height="174" src="https://img-blog.csdnimg.cn/db834ac8c1024ea98c85fdd4a2bafa12.png" width="759">

 可以执行如下指令，将数据脚本文件中的数据加载到表结构中：

```
-- 客户端连接服务端时，加上参数 -–local-infile
mysql –-local-infile -u root -p
-- 设置全局参数local_infile为1，开启从本地加载文件导入数据的开关
set global local_infile = 1;
-- 执行load指令将准备好的数据，加载到表结构中
load data local infile '/root/sql1.log' into table tb_user fields
terminated by ',' lines terminated by '\n' ;
```

>  
 主键顺序插入性能高于乱序插入 


#### 示例演示:

#### A. 创建表结构

```
CREATE TABLE `tb_user` (
`id` INT(11) NOT NULL AUTO_INCREMENT,
`username` VARCHAR(50) NOT NULL,
`password` VARCHAR(50) NOT NULL,
`name` VARCHAR(20) NOT NULL,
`birthday` DATE DEFAULT NULL,
`sex` CHAR(1) DEFAULT NULL,
PRIMARY KEY (`id`),
UNIQUE KEY `unique_user_username` (`username`)
) ENGINE=INNODB DEFAULT CHARSET=utf8 ;
```

#### B. 设置参数

```
-- 客户端连接服务端时，加上参数 -–local-infile
mysql –-local-infile -u root -p
-- 设置全局参数local_infile为1，开启从本地加载文件导入数据的开关
set global local_infile = 1;
```

#### C. load加载数据

```
load data local infile '/root/load_user_100w_sort.sql' into table tb_user
fields terminated by ',' lines terminated by '\n' ;
```

<img alt="" height="165" src="https://img-blog.csdnimg.cn/4249cc0dff364692b91afc1d51b7ccee.png" width="771">

 我们看到，插入100w的记录，17s就完成了，性能很好。

>  
 我们看到，插入100w的记录，17s就完成了，性能很好。 


### **2 ****主键优化**

在上一小节，我们提到，主键顺序插入的性能是要高于乱序插入的。 这一小节，就来介绍一下具体的原因，然后再分析一下主键又该如何设计。

### 1). 数据组织方式

在InnoDB存储引擎中，表数据都是根据主键顺序组织存放的，这种存储方式的表称为索引组织表

(index organized table IOT)。

<img alt="" height="289" src="https://img-blog.csdnimg.cn/fd37f02db1e44de9ab1c0a32b46b2aa6.png" width="746">

 行数据，都是存储在聚集索引的叶子节点上的。而我们之前也讲解过InnoDB的逻辑结构图：

<img alt="" height="280" src="https://img-blog.csdnimg.cn/c3621f49a6c94da1bc8c70b51f6a96ec.png" width="665">



在InnoDB引擎中，数据行是记录在逻辑结构 page 页中的，而每一个页的大小是固定的，默认16K。那也就意味着， 一个页中所存储的行也是有限的，如果插入的数据行row在该页存储不小，将会存储 到下一个页中，页与页之间会通过指针连接。

#### 2). 页分裂

页可以为空，也可以填充一半，也可以填充100%。每个页包含了2-N行数据(如果一行数据过大，会行溢出)，根据主键排列。

#### A. 主键顺序插入效果

①. 从磁盘中申请页， 主键顺序插入

<img alt="" height="193" src="https://img-blog.csdnimg.cn/54f4f477136a46c08c9dae6de46bdb8e.png" width="648">

 ②. 第一个页没有满，继续往第一页插入

<img alt="" height="196" src="https://img-blog.csdnimg.cn/5d137a5abfdd456c80ec91c49a4e1d18.png" width="635">

 ③. 当第一个也写满之后，再写入第二个页，页与页之间会通过指针连接

<img alt="" height="126" src="https://img-blog.csdnimg.cn/326d4ca7dd264cd2abe3eb2dff01997b.png" width="779">

 ④. 当第二页写满了，再往第三页写入

<img alt="" height="89" src="https://img-blog.csdnimg.cn/ce9881ecf15e4e6ea3cfe67b0d4cf31e.png" width="781">

####  B. 主键乱序插入效果

①. 加入1#,2#页都已经写满了，存放了如图所示的数据

<img alt="" height="121" src="https://img-blog.csdnimg.cn/0bdc1c2325da48d69314626beeee5723.png" width="751">

②. 此时再插入id为50的记录，我们来看看会发生什么现象

会再次开启一个页，写入新的页中吗？

<img alt="" height="199" src="https://img-blog.csdnimg.cn/c9101e2ba1584f26b0ade86a59f04aaa.png" width="776">

 不会。因为，索引结构的叶子节点是有顺序的。按照顺序，应该存储在47之后。

<img alt="" height="295" src="https://img-blog.csdnimg.cn/e9bb271ffee34b24a3becc02e77de054.png" width="771">

 但是47所在的1#页，已经写满了，存储不了50对应的数据了。 那么此时会开辟一个新的页 3#。

 <img alt="" height="78" src="https://img-blog.csdnimg.cn/6c1196d60ecd43cd8d07ea01f5802960.png" width="766">

 但是并不会直接将50存入3#页，而是会将1#页后一半的数据，移动到3#页，然后在3#页，插入50。

<img alt="" height="162" src="https://img-blog.csdnimg.cn/fde1937f40c44609bceef5b6c0302eaa.png" width="760">



移动数据，并插入id为50的数据之后，那么此时，这三个页之间的数据顺序是有问题的。 1#的下一个页，应该是3#， 3#的下一个页是2#。 所以，此时，需要重新设置链表指针。

<img alt="" height="88" src="https://img-blog.csdnimg.cn/d2604cafb02747b29cc291d8604810b0.png" width="775">

 上述的这种现象，称之为 "页分裂"，是比较耗费性能的操作。

#### 3). 页合并

目前表中已有数据的索引结构(叶子节点)如下：

<img alt="" height="113" src="https://img-blog.csdnimg.cn/82e5fec26d06439489ab5a6709f801d9.png" width="773">

 当我们对已有数据进行删除时，具体的效果如下:

当删除一行记录时，实际上记录并没有被物理删除，只是记录被标记（flaged）为删除并且它的空间变得允许被其他记录声明使用。

<img alt="" height="86" src="https://img-blog.csdnimg.cn/50be8c39564842c0856082e13807fab0.png" width="777">

 当我们继续删除2#的数据记录

<img alt="" height="105" src="https://img-blog.csdnimg.cn/638b10973dc74ccaa64cc1e4792e419d.png" width="762">

当页中删除的记录达到 MERGE_THRESHOLD（默认为页的50%），InnoDB会开始寻找最靠近的页（前或后）看看是否可以将两个页合并以优化空间使用。

<img alt="" height="214" src="https://img-blog.csdnimg.cn/2a0020080a154130a58fd61d9ecc8ea6.png" width="748">

 删除数据，并将页合并之后，再次插入新的数据21，则直接插入3#页

<img alt="" height="97" src="https://img-blog.csdnimg.cn/cc53381785cc4547a465effc36930cb1.png" width="758">

这个里面所发生的合并页的这个现象，就称之为 "页合并"。

>  
 补充： 
 MERGE_THRESHOLD：合并页的阈值，可以自己设置，在创建表或者创建索引时指定。 


#### 4). 索引设计原则

>  
 满足业务需求的情况下，尽量降低主键的长度。 
 插入数据时，尽量选择顺序插入，选择使用AUTO_INCREMENT自增主键。 
 尽量不要使用UUID做主键或者是其他自然主键，如身份证号。 
 业务操作时，避免对主键的修改。 


 <img alt="" height="476" src="https://img-blog.csdnimg.cn/d28fd4e374ce4cd99900e469c7648742.png" width="642">

>  
 ♥️关注，就是我创作的动力 
 ♥️点赞，就是对我最大的认可 
 ♥️这里是小刘，励志用心做好每一篇文章，谢谢大家 

