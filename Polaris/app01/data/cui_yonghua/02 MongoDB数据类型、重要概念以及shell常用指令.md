
--- 
title:  02 MongoDB数据类型、重要概念以及shell常用指令 
tags: []
categories: [] 

---
基础篇（能解决工作中80%的问题）:
1.   1.   1.   1.   1.   1.   
进阶篇:
1.   1.   1.   1.   1.   1.   1.   
其它:
1.   1.   
#### 一. mongo 数据类型

|数据类型|描述
|------
|String|字符串。存储数据常用的数据类型。在 MongoDB 中，UTF-8 编码的字符串才是合法的。
|Integer|整型数值。用于存储数值。根据你所采用的服务器，可分为 32 位或 64 位。
|Boolean|布尔值。用于存储布尔值（真/假）。
|Double|双精度浮点值。用于存储浮点值。
|Min/Max keys|将一个值与 BSON（二进制的 JSON）元素的最低值和最高值相对比。
|Array|用于将数组或列表或多个值存储为一个键。
|Timestamp|时间戳。记录文档修改或添加的具体时间。
|Object|用于内嵌文档。
|Null|用于创建空值。
|Symbol|符号。该数据类型基本上等同于字符串类型，但不同的是，它一般用于采用特殊符号类型的语言。
|Date|日期时间。用 UNIX 时间格式来存储当前日期或时间。你可以指定自己的日期时间：创建 Date 对象，传入年月日信息。
|Object ID|对象 ID。用于创建文档的 ID。
|Binary Data|二进制数据。用于存储二进制数据。
|Code|代码类型。用于在文档中存储 JavaScript 代码。
|Regular expression|正则表达式类型。用于存储正则表达式。

##### 1.1 几种重要的数据类型:

`ObjectId`: 类似唯一主键，可以很快的去生成和排序，包含 12 bytes，含义是：
- 前4个字节表示创建unix时间戳,格林尼治时间UTC时间，比北京时间晚了8小时- 接下来的 3 个字节是机器标识码- 紧接的两个字节由进程 id 组成 PID- 最后三个字节是随机数 <img src="https://img-blog.csdnimg.cn/cb3e9e5732164272913060c9eedba134.png" alt="">
`字符串`: BSON 字符串都是 UTF-8 编码。

`时间戳`: BSON 时间戳类型主要用于 MongoDB 内部使用。在大多数情况下的应用开发中，可以使用 BSON 日期类型。

`日期类型`: 表示当前距离 Unix新纪元（1970年1月1日）的毫秒数。日期类型是有符号的, 负数表示 1970 年之前的日期。

#### 二. 重要概念

##### 2.1 mongo与sql术语的对比

|SQL术语/概念|MongoDB术语/概念|解释/说明
|------
|database|database|数据库
|table|collection|数据库表/集合
|row|document|数据记录行/文档
|column|field|数据字段/域
|index|index|索引
|table joins||表连接,MongoDB不支持
|primary key|primary key|主键,MongoDB自动将_id字段设置为主键

##### 2.2 MongoDB保留的数据库

有一些数据库名是保留的，可以直接访问这些有特殊作用的数据库。

>  
 **`admin`**： 从权限的角度来看，这是"root"数据库。要是将一个用户添加到这个数据库，这个用户自动继承所有数据库的权限。一些特定的服务器端命令也只能从这个数据库运行，比如列出所有的数据库或者关闭服务器。 **`local`**: 这个数据永远不会被复制，可以用来存储限于本地单台服务器的任意集合 **`config`**: 当Mongo用于分片设置时，config数据库在内部使用，用于保存分片的相关信息。 


##### 2.3 文档(document)

文档是一组键值(key-value)对(即 BSON)。MongoDB 的文档不需要设置相同的字段，并且相同的字段不需要相同的数据类型，这与关系型数据库有很大的区别，也是 MongoDB 非常突出的特点。

注意： 文档的数据结构和 JSON 基本一样。 所有存储在集合中的数据都是 BSON 格式。 BSON 是一种类似 JSON 的二进制形式的存储格式，是 Binary JSON 的简称。

##### 2.4 集合（collection）

集合就是 MongoDB 文档组，类似于 RDBMS （关系数据库管理系统：Relational Database Management System)中的表格。

集合存在于数据库中，集合没有固定的结构，这意味着你在对集合可以插入不同格式和类型的数据，但通常情况下我们插入集合的数据都会有一定的关联性。

合法的集合名
- 集合名不能是空字符串""。- 集合名不能含有\0字符（空字符)，这个字符表示集合名的结尾。- 集合名不能以"system."开头，这是为系统集合保留的前缀。- 用户创建的集合名字不能含有保留字符。有些驱动程序的确支持在集合名里面包含，这是因为某些系统生成的集合中包含该字符。除非你要访问这种系统创建的集合，否则千万不要在名字里出现$。
##### 2.5 几个重要的可执行文件

**`mongod`**：启动数据库实例的可执行文件，是整个MongoDB中最核心的文件，负责数据库的创建、删除等各项管理工作，运行在服务器端，监听客户端的连接请求。

**`mongo进程`**：是一个与mongod进程进行交互的`JavaScript Shell`进程，它提供了一些交互的接口函数为系统管理员对数据库进行管理。

**`mongodump`**：将数据导为BSON格式的文件，备份数据库，同时可以利用这些dump文件重建数据库。使用`mongodump -help`可以查看支持的指令。

**`mongorestore`**：恢复备份文件。

**`mongoexport`**：将数据导出成json或csv格式的文件。

**`mongoimport`**：将json或csv格式的文件导入到mongo。

**`mongos`**：在分片中用到的进程文件，所有应用程序端的查询操作都会先用它分析，然后将查询定位到某一个分片上，它的监听作用与mongod的监听作用类似。

**`mongofiles`**：mongofiles提供了一个操作MongoDB分布式文件存储GridFS系统的命令行接口。

**`mongostat`**：展示当前正在运行的mongod或mongos实例的状态工具，相当于unix/linux的 vmstat, 但是它提供的数据只与运行的mongod或mongos的实例相关。

**`mongotop`**：提供了一个分析MongoDB实例在读写数据上的时间跟踪方法。

#### 三. 常用shell指令

`mongo` 进入mongo环境;

`db.help()`: 显示指令方法及含义; `show dbs` : 显示所有数据的列表。(或者`show databases`指令); `use 数据库名` : 数据库不存在，则创建数据库，否则切换到指定数据库; `db.dropDatabase()` : 删除数据库（先`use 数据库名`进入数据库才能删除）; `show collections` : 显示集合名（或者使用`show tables`命令） `db.createCollection("user_demo")` : 创建集合user_demo; `db.user_demo.drop()` : 删除集合user_demo。

**注意**: 创建集合: `db.createCollection(name, options)`, name是要创建的集合名称; options是可选参数, 指定有关内存大小及索引的选项，参数如下:

>  
 `capped`：布尔类型，可选）如果为 true，则创建固定集合。固定集合是指有着固定大小的集合，当达到最大值时，它会自动覆盖最早的文档。 当该值为 true 时，必须指定 size 参数。 `autoIndexId`：3.2 之后不再支持该参数。（可选）如为 true，自动在 **_id** 字段创建索引。默认为 false。 `size`：（可选）为固定集合指定一个最大值，即字节数。 如果 capped 为 true，也需要指定该字段。 `max`：（可选）指定固定集合中包含文档的最大数量。 

