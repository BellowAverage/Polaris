
--- 
title:  03 MongoDB文档的各种增加、更新、删除操作总结 
tags: []
categories: [] 

---
基础篇（能解决工作中80%的问题）:
1.   1.   1.   1.   1.   1.   
进阶篇:
1.   1.   1.   1.   1.   1.   1.   
其它:
1.   1.   
#### 一. 插入文档

注意: 在 MongoDB 中，直接插入内容会自动创建集合!

##### 1.1 使用insert()方法

**语法格式**: `db.COLLECTION_NAME.insert(document)`

**说明**: 若插入的数据主键已经存在，则会抛 org.springframework.dao.DuplicateKeyException 异常，提示主键重复，不保存当前数据。

**案例**: 如向集合user_demo中插入一条数据:

```
db.user_demo.insert({<!-- -->"name":"zhangsan", "age": 18})

# 相当于sql中的
insert into user_demo(name, age) values("zhangsan", 18);

```

##### 1.2 使用save()方法（新版本中已废弃）

**语法格式**: `db.COLLECTION_NAME.save(document)`

**说明**: 如果 **_id** 主键存在则更新数据，如果不存在就插入数据。该方法新版本中已废弃，可以使用 db.collection.insertOne() 或 db.collection.replaceOne() 来代替。

##### 1.3 使用insertOne()方法 (3.2版本新增)

**语法格式**: `db.collection.insertOne()`

**说明**: 向指定集合中插入一条文档数据, 可指定参数： writeConcern: 写入策略，默认为 1，即要求确认写操作，0 是不要求。

**案例**: 如向集合user_demo中插入一条数据:

```
db.user_demo.insertOne({<!-- -->"name":"zhangsan", "age": 18})

```

##### 1.4 insertMany()方法 (3.2版本新增)

**语法格式**: `db.collection.insertMany()`

**说明**: 向指定集合中插入多条文档数据, 可指定参数： writeConcern: 写入策略，默认为 1，即要求确认写操作，0 是不要求; ordered：指定是否按顺序写入，默认 true，按顺序写入。

**案例**: 如向集合user_demo中插入2条数据:

```
db.user_demo.insertMany([{<!-- -->"name":"zhangsan", "age": 18}, {<!-- -->"name":"lisi", "age": 20}])

```

#### 二. 更新文档

##### 2.1 使用 update() 方法

**语法格式**:

```
db.collection.update(
   &lt;query&gt;,
   &lt;update&gt;,
   {<!-- -->
     upsert: &lt;boolean&gt;,
     multi: &lt;boolean&gt;,
     writeConcern: &lt;document&gt;
   }
)

```

**说明**: 更新集合中的文档, 可指定参数：

>  
 <p>`query` : update的查询条件，类似sql update查询内where后面的; `update` : update的对象和一些更新的操作符（如 
      
       
        
        
          , 
         
        
       
         , 
        
       
     ,inc…）等，也可以理解为sql update查询内set后面的; `upsert` : 可选，这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入; `multi` : 可选，mongodb 默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新; `writeConcern` :可选，抛出异常的级别。</p> 


**案例**: 如向集合user_demo中名称为zhangsan的用户的age更新成21:

```
db.user_demo.update({<!-- -->'name':'zhangsan'},{<!-- -->$set:{<!-- -->'age': 21}})

# 相当于sql中的
update article set age = 21 where name &gt; 'zhangsan';

```

##### 2.2 使用 save() 方法

**语法格式**:

```
db.collection.save(
   &lt;document&gt;,
   {<!-- -->
     writeConcern: &lt;document&gt;
   }
)

```

**说明**: save() 方法通过传入的文档来替换已有文档，**_id** 主键存在就更新，不存在就插入, 可指定参数：

>  
 `document` : 文档数据; `writeConcern` :可选，抛出异常的级别。 


**案例**: 如向集合user_demo中替换 **_id** 为 56064f89ade2f21f36b03136的文档数据

```
db.user_demo.save({<!-- -->"_id" :          ObjectId("56064f89ade2f21f36b03136"),
    "name": "wangwu",
    "age": 23})

# 更新之后可查看结果
db.user_demo.find().pretty()

```

##### 3.3 MongoDB 3.2版本新增的方法

**更新一条**：`db.collection.updateOne()`， 参考：

**更新多条**：`db.collection.updateMany()`， 参考：

**替换1条**：`db.collection.replaceOne()`， 参考：

#### 三. 删除文档

注意：在删除文档前先执行 find() 命令来判断执行的条件是否正确，这是一个比较好的习惯。

##### 3.1 使用 remove() 方法删除文档

**语法格式**: 2.6版本以后

```
db.collection.remove(
   &lt;query&gt;,
   {<!-- -->
     justOne: &lt;boolean&gt;,
     writeConcern: &lt;document&gt;
   }
)

```

**说明**:用来移除集合中的数据,参数说明：

>  
 `query` :（可选）删除的文档的条件。 `justOne` : （可选）如果设为 true 或 1，则只删除一个文档，如果不设置该参数，或使用默认值 false，则删除所有匹配条件的文档。 `writeConcern` :（可选）抛出异常的级别。 


**案例**: 如在集合user_demo中移除名为zhangsan的数据:

```
db.user_demo.remove({<!-- -->"name":"zhangsan"})

db.user_demo.find()  # 发现没有名为zhangsan的数据了

# 相当于sql中的
delete from user_demo where name = "zhangsan"

```

注意：remove() 方法已经过时了，现在官方推荐使用 deleteOne() 和 deleteMany() 方法。

##### 3.2 使用 deleteOne() 方法删除文档

如删除user_demo集合下 status 等于 D 的一个文档：

`db.inventory.deleteOne({ status: "D"})`

##### 3.3 使用 deleteMany() 方法删除文档

如删除user_demo集合下全部文档：`db.user_demo.deleteMany({})`

如删除user_demo集合下 status 等于 A 的全部文档：`db.user_demo.deleteMany({status :"A"})`

#### 四. bulk-write 操作

MongoDB批量操作支持同时执行一批写操作，写操作包括：插入文档、更新文档、删除文档。

官网参考： 

bulkWrite 批量操作支持下面写操作自由组合。
- insertOne - 插入一个文档- updateOne - 更新一个文档- updateMany - 更新一批文档- replaceOne - 替换一个文档- deleteOne - 删除一个文档- deleteMany - 删除一批文档
语法格式：

```
# operation - 代表写操作配置
# bulkWrite接收一个写操作数组。
db.collection.bulkWrite(
   [ &lt;operation 1&gt;, &lt;operation 2&gt;, ... ],
)

```

mongo shell通过db.collection.bulkWrite()函数执行批量操作。

综合案例：

```
db.inventory.bulkWrite(
      [
         // 插入一个文档
         {<!-- --> insertOne :
            {<!-- -->
            // 文档内容
               "document" :
               {<!-- -->
                  "_id" : 4, "char" : "Dithras", "class" : "barbarian", "lvl" : 4
               }
            }
         },
         {<!-- --> insertOne :
            {<!-- -->
               "document" :
               {<!-- -->
                  "_id" : 5, "char" : "Taeln", "class" : "fighter", "lvl" : 3
               }
            }
         },
         // 更新一个文档，updateMany 更新一批文档类似
         {<!-- --> updateOne :
            {<!-- -->
               // 更新条件
               "filter" : {<!-- --> "char" : "Eldon" },
               // 更新内容
               "update" : {<!-- --> $set : {<!-- --> "status" : "Critical Injury" } }
            }
         },
         // 删除一个文档，deleteMany删除多个文档类似
         {<!-- --> deleteOne :
            // 删除条件
            {<!-- --> "filter" : {<!-- --> "char" : "Brisbane" } }
         },
         // 替换一个文档
         {<!-- --> replaceOne :
            {<!-- -->
                // 替换条件
               "filter" : {<!-- --> "char" : "Meldane" },
               // 替换内容
               "replacement" : {<!-- --> "char" : "Tanys", "class" : "oracle", "lvl" : 4 }
            }
         }
      ]
   );

```

附：官网crud操作：

❤️ 如果觉得有用，感谢一键三连哦 ！！！❤️
