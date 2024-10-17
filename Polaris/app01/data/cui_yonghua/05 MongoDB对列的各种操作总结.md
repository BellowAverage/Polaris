
--- 
title:  05 MongoDB对列的各种操作总结 
tags: []
categories: [] 

---
基础篇（能解决工作中80%的问题）:
1.   1.   1.   1.   1.   1.   
进阶篇:
1.   1.   1.   1.   1.   1.   1.   
其它:
1.   1.   
#### 一. 修改列名

**`案例1：`** 修改age为 31 的列的address列的名称修改为address2，只会修改一条记录。

```
db.person.update({<!-- -->age:31},{<!-- -->$rename:{<!-- -->address:'address2'}})

```

**`案例2：`** name为张三的address列的名修改为address2，会修改所有满足条件的记录。

```
db.person.update({<!-- -->name:'张三'},{<!-- -->$rename:{<!-- -->address:'address2'}},{<!-- -->multi:true})

```

#### 二. 对列的增加或者删除操作

更新特定字段：

```
db.game.update({<!-- -->"_id": 123}, {<!-- --> "$set": {<!-- -->"count": 10000}})

# 相当于sql中的
update game set count = 10000 where _id = 123;

```

删除特定字段：

```
db.game.update({<!-- -->"_id":123}, {<!-- -->"$unset": {<!-- -->"author":1}})

```

案例1：增加列名为name的值是张三的列，只会增加一条。

```
db.person.update({<!-- -->name:'张三'},{<!-- -->$set:{<!-- -->age:''}})　

```

案例2：在集合中增加一列age, 默认为空, 该所有文档中都会增加该列：

```
db.person.update({<!-- -->name:'张三'},{<!-- -->$set:{<!-- -->age:''}}, {<!-- -->multi:true})　

```

案例3：删除列名为name的值是张三的列，列名和列值都会删除，只会删除一条。

```
db.person.update({<!-- -->name:'张三'},{<!-- -->$unset:{<!-- -->age:''}})

```

案例4：删除列名为name的值是张三的列，列名和列值都会删除，满足条件的都会删除。

```
db.person.update({<!-- -->name:'张三'},{<!-- -->$unset:{<!-- -->age:''}},{<!-- -->multi:true})

```

#### 三. 某列字段的更新和插入操作

##### 3.1 `$inc`: 进行递增或者递减

对应的字段必须是数字，而且递增或递减的值也必须是数字。

案例1：给某一列自增长 $inc ，_id 为1的记录,age 增加 1

```
# 每次age都加10
db.person.update({<!-- -->_id:1},{<!-- -->$inc: {<!-- -->age:10}})　　　

```

案例2：改变1条记录

```
db.person.update({<!-- -->name:'张三'},{<!-- -->$inc:{<!-- -->age:10}})

```

案例3：改变所有满足条件的记录

```
db.person.update({<!-- -->name:'张三'},{<!-- -->$inc:{<!-- -->age:10}},{<!-- -->multi:ture})

```

##### 3.2 数组追加

`$push` 进行数组追加，

案例1：追加一个元素

```
db.game.update({<!-- -->"_id": 123}, {<!-- --> "$push": {<!-- -->"score": 123}})

```

案例2：追加多个元素

```
db.game.update({<!-- -->"_id": 123}, {<!-- -->"$push": {<!-- -->"score": [12,123]}})

```

注：追加字段必须是数组。如果数组字段不存在，则自动新增，然后追加。

##### 3.3 一次追加多个元素

`$pushAll` 一次追加多个元素

```
db.game.update({<!-- -->"_id": 123}, {<!-- -->"$pushAll": {<!-- -->"score": [12,123]}})

```

##### 3.4 追加不重复元素

`$addToSet`：追加不重复元素，类似集合Set，只有当这个值不在元素内时才增加：

```
db.game.update({<!-- -->"_id": 123}, {<!-- -->"$addToSet": {<!-- -->"score": 123}})

```

##### 3.5 其它字段操作

案例1：如果没有_id 为 4 的记录，则插入

```
db.person.update({<!-- -->_id:4},{<!-- -->$set: {<!-- -->name:'李四',class:'三班',score:90}},{<!-- -->upsert:true})

# 插入的数据结果
{<!-- --> "_id" : 4, "name" : "李四", "class" : "三班", "score" : 90 }

```

案例2：如果没有更新行，插入额外的列：$setOnInsert，upsert:true

```
db.person.update({<!-- -->_id:5},{<!-- -->$setOnInsert:{<!-- -->name:'王五',like:'football'}},{<!-- -->upsert:true})

# 执行后，数据库中多出如下记录：
{<!-- --> "_id" : 5, "like" : "football", "name" : "王五" }

# 假如数据库中有_id 为 5 的记录，执行以下的语句，不会有任何影响，不会新增，也不会修改。
db.person.update({<!-- -->_id:5},{<!-- -->$setOnInsert:{<!-- -->name:'王五',like:'football',height:178}},{<!-- -->upsert:true});

```

案例：如果没有更新行，插入额外的列：$setOnInsert，upsert:true

```
db.person.update({<!-- -->_id:5},{<!-- -->$setOnInsert:{<!-- -->name:'王五',like:'football'}},{<!-- -->upsert:true})

# 假如有_id 为5的记录，执行以下的语句，不会有任何影响，不会新增也不会修改
db.person.update({<!-- -->_id:5},{<!-- -->$setOnInsert:{<!-- -->name:'王五',like:'football',height:178}},{<!-- -->upsert:true})

```

#### 四. 删除元素

##### 4.1 删除一个元素

`$pop` 删除元素, 每次只能删除数组中的一个元素，1表示删除最后一个，-1表示删除第一个。

```
# 删除最后一个元素
db.game.update({<!-- -->"_id": 123}, {<!-- -->"$pop": {<!-- -->"score": 1}})

# 删除第一个元素
db.game.update({<!-- -->"_id": 123}, {<!-- -->"$pop": {<!-- -->"score": -1}})

```

案例：删除特定元素

```
db.game.update({"_id": 123}, {"$pull": {"score": 123}})

```

##### 4.2 删除特定元素

`$pull` 删除特定元素

```
# 删除数组score内值等于123的元素。
db.game.update({<!-- -->"_id": 123}, {<!-- -->"$pull": {<!-- -->"score": 123}})

```

##### 4.3 删除多个特定元素

`$pullAll` 删除特定元素

```
# 删除数组内值等于123或12的元素。
db.game.update({<!-- -->"_id": 123}, {<!-- -->"$pullAll": {<!-- -->score: [123,12]}})

```

❤️ 如果觉得有用，感谢一键三连哦 ！！！❤️
