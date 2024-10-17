
--- 
title:  Mongodb基础操作 
tags: []
categories: [] 

---
### 一、简介

        MongoDB是一个NoSQL型的数据库，基于分布式文档型储存数据库，由C++语言编写，它的特点是开源、高性能、高可用、高扩展、易部署。支持 Golang、RUBY、PYTHON、JAVA、C++、PHP等多种开发语言。

### 二、应用场景

        MongoDB适用于高并发读写、数据量大、高可扩展性和高可用性且对事务要求不高的场景，常用的应用场景有以下：

        1. 社交应用：可以使用MongoDB来存储用户信息和朋友圈动态，实现附近的人等功能。

        2. 游戏：使用MongoDB来存储用户基础信息，以及游戏中的积分、等级以及装备等用户关联信息。

        3. 物流：使用MongoDB存储订单信息，以及物流轨迹信息。

        4. 物联网：使用MongoDB存储各设备信息，以及个设备的产生的日志信息，以便于对设备进行分析、维护和预警。

        5. 视频直播：使用MongoDB来吃存储用户信息，以及用户操作日志、点赞、收藏和评价。

### 三、基础操作

#### 1、创建集合

集合的创建分为隐式创建和显式创建。

显式创建：db.createCollection(name)。

隐式创建：当向一个集合插入一个文档时，如果集合不存在则会自动创建集合。

#### 2、插入操作：

**insert插入**：插入单个数据。

>  
 db.user.insert({name:"张三",age:19,sex:1})  


 <img alt="" height="39" src="https://img-blog.csdnimg.cn/e98876eedb074d9cb6764cefc14d7214.png" width="679">         ** insertMany插入**：插入多条数据。

>  
  db.user.insertMany([{name:"李四",age:24,sex:1},{name:"王五",age:20,sex:0}]) 


<img alt="" height="148" src="https://img-blog.csdnimg.cn/a5b28c65032547dc8983fa95c077d2fa.png" width="810">

#### 3、查询操作：

查询操作使用find()或findOne()进行查询，其中findOne()只查询出一条数据。

##### **find查询**

>  
          db.user.find({age:20},{_id:0,age:1,name:1}); 
          // 等同于：select age,name from user where age=20; 


    <img alt="" height="59" src="https://img-blog.csdnimg.cn/f6904e3dbe4d4d9dbce97182b3b36a5d.png" width="569">               

##### 比较查询 
<td style="width:97px;">操作</td><td style="width:136px;">操作符</td><td style="width:347px;">查询格式</td>
<td style="width:97px;">小于</td><td style="width:136px;">$lt</td><td style="width:347px;">{age:{$lt:18}}   // where age&lt;18</td>
<td style="width:97px;">小于等于</td><td style="width:136px;">$lte</td><td style="width:347px;">{age:{$lte:18}}   // where age&lt;=18</td>
<td style="width:97px;">大于</td><td style="width:136px;">$gt</td><td style="width:347px;">{age:{$gt:18}}   // where age&gt;18</td>
<td style="width:97px;">大于等于</td><td style="width:136px;">$gte</td><td style="width:347px;">{age:{$gte:18}}   // where age&gt;=18</td>
<td style="width:97px;">不等于</td><td style="width:136px;">$ne</td><td style="width:347px;">{age:{$ne:18}}   // where age&lt;&gt;18</td>

>  
 db.user.find({age:{$lt:30}}) 
 //等同于 select * from user where age&lt;30;  


<img alt="" height="79" src="https://img-blog.csdnimg.cn/77034d61ae7b47429a10aba12894ba43.png" width="924">

##### 逻辑查询

and查询

>  
 db.user.find({$and:[{age:20},{sex:0}]}); 
 // 等同于 select * from user where age=20 and sex=0 


<img alt="" height="75" src="https://img-blog.csdnimg.cn/b983bdfd550c4bef8681083d535a3fbf.png" width="775">

或者缺省$and

>  
 db.user.find({age:20,sex:0})       


or查询

>  
  db.user.find({$or:[{age:{$lt:24}},{sex:1}]}); 
 //等同于 select * from user where age&lt;24 or sex=1 


<img alt="" height="115" src="https://img-blog.csdnimg.cn/c9d2405e99484c95838f0bf0c712c259.png" width="877">

混合查询  

>  
 db.user.find({$or: 
         [{sex:1}, 
          {$and: 
                 [{age:20},{sex:0}] 
          }]}); 
 //等同于 select * from user where sex=1 or（age=20 and sex=0） 


<img alt="" height="118" src="https://img-blog.csdnimg.cn/ce415922c871487f899387ad244f80dd.png" width="862">

#####  in 和nin 查询

>  
 db.user.find({age:{$in:[18,19,20]}}) 
 //等同于 select * from user where age in (18,19,20) 


<img alt="" height="99" src="https://img-blog.csdnimg.cn/d7ad460804e64973bd0029cd76a5572d.png" width="824">

>  
 db.user.find({age:{$nin:[18,19,20]}}) 
 //等同于 select * from user where age not in (18,19,20) 


#####  为空查询

>  
 db.user.find({name:{$exists:1}}); 
 //等同于 select * from user where name is not null; 


<img alt="" height="111" src="https://img-blog.csdnimg.cn/97c96456499e4f1e94f71fd7b10fc35d.png" width="847">

#####  分页查询

>  
 db.user.find().skip(2).limit(2).sort({age:1}); 
 //等同于 select * from user order by age asc limit 2,2; 


<img alt="" height="86" src="https://img-blog.csdnimg.cn/7e4ce52d76db4f07940f57534065a764.png" width="817">

##### 分组查询

使用聚合方法aggregate()。

>  
 db.user.aggregate([{$group:{_id:"$sex",min_age:{$min:"$age"}}}])； 
 //等同于 select sex,min($age) from user group by sex; //获取男女中最小年龄 


<img alt="" height="74" src="https://img-blog.csdnimg.cn/bbae2fc633da4749816896a63f9a7176.png" width="726">

>  
  db.user.aggregate([{$group:{_id:"$sex",sex_total:{$sum:1}}}]); 
 //等同于 select sex,count(1) from user group by sex;// 统计男女的个数 


<img alt="" height="79" src="https://img-blog.csdnimg.cn/e8815d206c3a474598ec953197907e3d.png" width="716">

##### 其他聚合操作
<td style="width:124px;">操作 </td><td style="width:226px;">描述</td><td style="width:292px;">示例</td>
<td style="width:124px;">$avg</td><td style="width:226px;">计算平均值。</td><td style="width:292px;">db.user.aggregate([{$group:{_id:"$sex",avg_age:{$avg:"$age"}}}])</td>
<td style="width:124px;">$max</td><td style="width:226px;">求最大值。</td><td style="width:292px;">db.user.aggregate([{$group:{_id:"$sex",min_age:{$max:"$age"}}}])</td>
<td style="width:124px;">$push</td><td style="width:226px;">将值加入一个数组中，不判断重复。</td><td style="width:292px;">db.user.aggregate([{$group:{_id:"$sex",name:{$push:"$name"}}}])</td>
<td style="width:124px;">$addToSet</td><td style="width:226px;">将值加入一个数组中，会判断是重复，若重复则不加入。</td><td style="width:292px;">db.user.aggregate([{$group:{_id:"$sex",name:{$addToSet:"$name"}}}])</td>
<td style="width:124px;">$first</td><td style="width:226px;">获取第一个文档数据</td><td style="width:292px;">db.user.aggregate([{$group:{_id:"$sex",first_name:{$first:"$name"}}}])</td>
<td style="width:124px;">$last</td><td style="width:226px;">获取最后一个文档数据</td><td style="width:292px;">db.user.aggregate([{$group:{_id:"$sex",last_name:{$last:"$name"}}}])</td>

#### 4、更新操作

db.user.update({查询条件},{更新操作}，不存在时是否插入，是否多条，异常级别)。

>  
 db.user.update({name:"张三"},{$set:{age:40}}) // 将张三的年龄修改为40 
 db.user.update({name:"张三"},{$inc:{age:2}}) //将张三的年龄加2 


#### 5、删除操作

##### 删除集合（此操作慎用）

db.user.drop();

##### 删除文档

db.user.remove({查询条件})

### 四、索引

#### 1. 创建索引

db.user.createIndex({age:1}) // 创建index_age 按升序排序

#### 2. 查看索引

db.user.getIndexes()

#### 3. 查看索引大小

db.user.totalIndexSize()

#### 4. 删除索引

db.user.dropIndex(索引名)；

db.user.dropIndexes();//删除集合所有索引  

**总结：**

        本文主要介绍了MongoDB的常用的基础操作，操作方式主要使用的是json类型的条件语句，对json编写的要求较高，其操作和MySQL的操作基本相同，除了MongoDB没有join查询以外其他查询都支持，后续会给大家分享MongoDB的安装和主从复制等内容。
