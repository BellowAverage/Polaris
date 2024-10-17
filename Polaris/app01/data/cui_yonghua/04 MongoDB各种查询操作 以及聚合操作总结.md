
--- 
title:  04 MongoDB各种查询操作 以及聚合操作总结 
tags: []
categories: [] 

---
基础篇（能解决工作中80%的问题）:
1.   1.   1.   1.   1.   1.   
进阶篇:
1.   1.   1.   1.   1.   1.   1.   
其它:
1.   1.   
#### 一. 使用 find() 方法查询文档

**语法格式**: `db.collection.find(query, projection)`

**说明**: find()方法以非结构化的方式来显示所有文档, 可指定参数：

>  
 `query` : 可选，使用查询操作符指定查询条件; `projection` : 可选，使用投影操作符指定返回的键。查询时返回文档中所有键值， 只需省略该参数即可（默认省略）。 


**案例1**: 如向集合user_demo中查询名字为zhangsan的用户:

```
db.user_demo.find({<!-- -->'name':'zhangsan'})

# 相当于sql中的
select * from user_demo where name = "zhangsan";

```

**案例2**： 指定返回哪些键

```
db.article.find({<!-- -->}, {<!-- -->"title": 1, "author": 1})

# 相当于sql中的
select title, author from article;

```

除了 find() 方法之外，还有一个 findOne() 方法，它只返回一个文档。

#### 二. AND查询和OR查询

##### 2.1 AND查询

**AND查询语法格式**: `db.col.find({key1:value1, key2:value2})`

**案例1**: 如向集合user_demo中查询名字为zhangsan的用户且age为20的数据:

```
db.user_demo.find({<!-- -->'name':'zhangsan', 'age': 20})

# 相当于sql中的
select * from user_demo where name = "zhangsan" and age = 20;

```

##### 2.2 OR查询

**OR查询语法格式**:

```
db.col.find(
   {<!-- -->
      $or: [
         {<!-- -->key1: value1}, {<!-- -->key2:value2}
      ]
   }
)

```

**案例2**: 如向集合user_demo中查询名字为zhangsan的用户或age为20的数据:

```
db.user_demo.find({<!-- -->$or:[{<!-- -->'name':'zhangsan', 'age': 20}]})

# 相当于sql中的
select * from article where name = "zhangsan" or age = 20;

```

**案例3**: AND和OR联合使用案例，类似常规SQL语句为：

```
db.col.find({<!-- -->"likes": {<!-- -->$gt:50}, $or: [{<!-- -->"by": "xx教程"},{<!-- -->"title": "MongoDB 教程"}]})

# 相当于sql中的
select * from col where likes&gt;50 AND (by = 'xx教程' OR title = 'MongoDB 教程');

```

#### 三. 条件操作符

##### 3.1 比较条件

MongoDB中条件操作符有：

>  
 (&gt;) 大于 - $gt (&lt;) 小于 - $lt (&gt;=) 大于等于 - $gte (&lt;= ) 小于等于 - $lte 


**案例1**: 获取 “col” 集合中 “likes” 大于 100 的数据：

```
db.col.find({<!-- -->likes : {<!-- -->$gt : 100}})

# 相当于sql中的
select * from col where likes &gt; 100;

```

**案例2**: 获取"col"集合中 “likes” 大于等于 100 的数据：

```
db.col.find({<!-- -->likes : {<!-- -->$gte : 100}})

# 相当于sql中的
select * from col where likes &gt;= 100;

```

**案例3**: 获取"col"集合中 “likes” 小于 150 的数据：

```
db.col.find({<!-- -->likes : {<!-- -->$lt : 150}})

# 相当于sql中的
select * from col where likes &lt; 150;

```

**案例4**: 获取"col"集合中 “likes” 小于等于 150 的数据：

```
db.col.find({<!-- -->likes : {<!-- -->$lte : 150}})

# 相当于sql中的
select * from col where likes &lt;= 150;

```

**案例5**: 获取"col"集合中 “likes” 大于100，小于 200 的数据：

```
db.col.find({<!-- -->likes : {<!-- -->$lt :200, $gt : 100}})

# 相当于sql中的
select * from col where likes &gt; 100 and likes &lt; 200;

```

**案例6**: 获取"col"集合中 “likes” 不等于100的数据：

```
db.col.find({<!-- -->likes : {<!-- -->"$ne": 100}})

# 相当于sql中的
select * from col where likes != 100;

```

##### 3.2 `in`条件

```
select * from article where author in ("a", "b", "c")

# 相当于sql中的
db.article.find({<!-- -->"author": {<!-- -->"$in": ["a", "b", "c"]}})

```

##### 3.3 `like`条件查询

```
db.article.find({<!-- -->"title": /mongodb/})

# 相当于sql中的
select * from article where title like "%mongodb%"

```

#### 四. limit() 方法与 skip() 方法

##### 4.1 控制返回数量 limit() 方法

**语法格式(limit)**：`db.COLLECTION_NAME.find().limit(NUMBER)`

如显示查询文档中的两条记录：

```
db.col.find({<!-- -->},{<!-- -->"title":1}).limit(2)

```

除了可以使用limit()方法来读取指定数量的数据外，还可以使用skip()方法来跳过指定数量的数据，skip方法同样接受一个数字参数作为跳过的记录条数。

##### 4.2 略过数量 skip() 方法

**语法格式**：`db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER)`

以下实例只会显示第二条文档数据:

```
db.col.find({<!-- -->},{<!-- -->"title":1).limit(1).skip(1)

# 下面是略过前5条数据，也就是从第6条开始返回。
db.article.find().skip(5)

```

注:skip()方法默认参数为 0 。

##### 4.3 limit和skip结合

可以结合limit()和skip()来达到分页效果：

```
db.article.find().skip(10).limit(20) 

# 相当于sql中的 
select * from article limit 10, 20;

```

#### 五. 排序 sort() 方法

在 MongoDB 中使用 sort() 方法对数据进行排序。

sort() 方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式，其中 1 为升序排列，而 -1 是用于降序排列。

**语法格式**：`db.COLLECTION_NAME.find().sort({KEY:1})`

如在 col 集合中的数据按字段 likes 的降序排列：

```
db.col.find({<!-- -->},{<!-- -->"title":1}).sort({<!-- -->"likes":-1})

# 相当于sql中的
select * from col where title = 1 order by likes desc;

```

注意：skip(), limilt(), sort()三个放在一起执行的时候，执行的顺序是先 sort(), 然后是 skip()，最后是显示的 limit()。

#### 六. **$type** 操作符

##### 6.1 MongoDB 中可以使用的类型如下表所示：
- Double 1- String 2- Object 3- Array 4- Binary data 5- Undefined 6 已废弃。- Object id 7- Boolean 8- Date 9- Null 10- Regular Expression 11- JavaScript 13- Symbol 14- JavaScript (with scope) 15- 32-bit integer 16- Timestamp 17- 64-bit integer 18- Min key 255 Query with -1.- Max key 127
案例: 获取 “col” 集合中 title 为 String 的数据: `db.col.find({"title" : {$type : 2}})` 或 `db.col.find({"title" : {$type : 'string'}})`

##### 6.2 多个元素的查询

案例: 只有type数组同时存在mongodb和javascript才会匹配。

```
db.article.find({<!-- -->"type": {<!-- -->"$all": ["mongodb", "javascript"]}})

```

##### 6.3 限制数组长度查询

案例: 只有数组的长度是2才会匹配, 注：type_list必须是数组

```
db.article.find({<!-- -->"type_list": {<!-- -->"$size": 2}})

```

##### 6.4 返回特定数量

当`$slice`的参数是一个时，表示返回的数量;当是一个数组时，第一个参数表示偏移量，第二个表示返回的数量：

案例：返回特定数量， 注：$slice针对的是数组

```
db.article.find({<!-- -->"type": {<!-- -->"$slice": 1}}) // 返回第1个

db.article.find({<!-- -->"type": {<!-- -->"$slice": -1}})  // 返回最后一个

db.article.find({<!-- -->"type": {<!-- -->"$slice": [20, 10]}})  // 从第21个开始，返回10个，也就是21～30

```

更多类型可以参考：

#### 七. MongoDB特有的语句

##### 7.1 元素匹配 ($elemMatch)

如果文档中有一个字段的值是数组，可以使用`$elemMatch`来匹配数组内的元素：

案例：只有a=1且b&gt;2才会匹配。

```
db.article.find({<!-- -->"kown": {<!-- --> "$elemMatch": {<!-- -->a: 1, b: {<!-- -->"$gt": 2}}}})

```

##### 7.2 取模（$mod）

比如我们要匹配 read % 5 == 1：

```
db.article.find({<!-- -->"read": {<!-- -->$mod: [5, 1]}})

```

##### 7.3 是否存在（$exists)

如果我们要判断love字段是否存在，可以这样：

```
# 如果存在字段love，就返回
db.article.find({<!-- -->"love": {<!-- -->"$exists": true}})

# 我们也可以判断不存在, 如果不存在字段love，就返回
db.article.find({<!-- -->"love": {<!-- -->"$exists": false}})

```

##### 7.4 正则表达式

mongodb支持正则表达式，使用方法与正则字面量一样：

```
# i是忽略大小写
db.article.find({<!-- -->"title": /mongodb/i})

```

##### 7.5 类型查询

我们可以根据字段类型来返回数据：

```
# 只有当comments的类型是数组才匹配
db.article.find({<!-- -->"comments": {<!-- -->"$type": 4}})

```

##### 7.6 内嵌文档

mongodb是允许内嵌文档的，而且要查询内嵌文档也很简单（使用点语法）：

```
{<!-- -->
  address: {<!-- --> name: "nanji" }
}

db.article.find({<!-- -->"address.name": "nanji"})

```

数组也可以采取点语法:

```
{<!-- -->
  comments: [{<!-- -->title: "mongodb"}, {<!-- -->title: "javascript"}]
}

db.article.find({<!-- -->"comments.title": "mongodb"})

```

##### 7.7 取反

$not是元语句，即可以用在任何其他条件之上：

```
db.article.find({<!-- -->"author": {<!-- -->"$not": /mongodb/i}})

```

只要使用$not操作符，就表示取反。

##### 7.8 统计

返回匹配数据的长度：

```
db.article.find().count()

```

##### 7.9 格式化

pretty()方法可以以格式化的方式显示所有文档：

```
db.article.find().pretty()

```

##### 7.10 不等于

$ne：表示not equals 就是的意思

```
# 查询某字段不为空的数据
db.hfijf.find({<!-- -->fieldName: {<!-- -->$ne:null}})
# 查询字段等于空的数据
db.hfijf.find({<!-- -->fieldName: {<!-- -->$eq:null}})

```

❤️ 如果觉得有用，感谢一键三连哦 ！！！❤️
