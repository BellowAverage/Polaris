
--- 
title:  python3操作MongoDB的crud以及聚合案例，代码可直接运行（python经典编程案例） 
tags: []
categories: [] 

---
基础篇（能解决工作中80%的问题）:
1.   1.   1.   1.   1.   1.   
进阶篇:
1.   1.   1.   1.   1.   1.   1.   
其它:
1.   1.   
其它:
1.   1.   
参考： 官方文档： github：

#### 一. 插入数据案例

```
# -*- encoding: utf-8 -*-
import time
import pymongo
import datetime

# 创建对象
client = pymongo.MongoClient('mongodb://账号:密码@主机:端口号/?authSource=admin')
# 连接DB数据库
db = client['数据库名']


def insert_one():
    # 连接集合user，集合类似于关系数据库的数据表; 如果集合不存在，就会新建集合user
    user_collection = db.user_demo
    # 设置文档格式（文档即我们常说的数据）
    user_info = {<!-- -->
        "_id": 105,
        "author": "小绿",
        "text": "Python开发",
        "tags": ["mongodb", "pymongo"],
        "date": datetime.datetime.now()}

    # 使用insert_one单条添加文档，inserted_id获取写入后的id
    # 添加文档时，如果文档尚未包含"_id"键，就会自动添加"_id"。"_id"的值在集合中必须是唯一的
    # inserted_id用于获取添加后的id，若不需要，则可以去掉
    user_id = user_collection.insert_one(user_info).inserted_id
    print("user id is ", user_id)


def insert_many():
    #批量添加
    user_infos = [{<!-- -->
        "_id": 101,
        "author": "小黄",
             "text": "Python开发",
             "tags": ["mongodb", "python", "pymongo"],
             "date": datetime.datetime.utcnow()},
     {<!-- -->
        "_id": 102,
        "author": "小黄_A",
             "text": "Python开发_A",
             "tags": {<!-- -->"db":"Mongodb","lan":"Python","modle":"Pymongo"},
             "date": datetime.datetime.utcnow()},
     ]

    user_collection = db.user_insert_many
    # inserted_ids用于获取添加后的id，若不需要，则可以直接去掉
    user_id = user_collection.insert_many(user_infos).inserted_ids
    print("user id is ", user_id)


def bulk_insert_data():
    from pymongo import UpdateOne
    data_list = [{<!-- -->'user_id': 5, 'name': '张三1', 'age': 27, 'email': 'zhangsan1@email.com'},
                 {<!-- -->'user_id': 6, 'name': '李四1', 'age': 26, 'email': 'lisi1@email.com'},
                 {<!-- -->'user_id': 7, 'name': '王五1', 'age': 29, 'email': 'wangwu1@email.com'},
                 {<!-- -->'user_id': 8, 'name': '赵六1', 'age': 26, 'email': 'zhaoliu1@email.com'}]
    bulk_data_list = []
    for data in data_list:
        one = UpdateOne({<!-- -->"_id": data['user_id']}, {<!-- -->
            "$set": {<!-- -->"name": data['name'],
                     "age": data['age'],
                     "email": data['email'],
                     "date": datetime.datetime.now()}}, upsert=True)
        bulk_data_list.append(one)

    try:
        collection_item = db.bulk_insert_demo
        collection_item.bulk_write(bulk_data_list)
    except Exception as e:
        print(f'e: {<!-- -->e}')
    print(f"{<!-- -->time.strftime('%Y-%m-%d %H:%M:%S')}, 已存mongo: {<!-- -->len(bulk_data_list)}条")


if __name__ == '__main__':
    # 插入单条数据
    insert_one()

    # 插入多条数据
    # insert_many()

    # 批量插入
    # bulk_insert_data()


```

#### 二. 查询数据案例

```
# -*- encoding: utf-8 -*-
import re
import pymongo
# 创建对象
# client = pymongo.MongoClient()
client = pymongo.MongoClient('mongodb://账号:密码@主机:端口号/?authSource=admin')
# 连接DB数据库
db = client['数据库名']


def find_by_condition():
    # 连接集合user，集合类似于关系数据库的数据表, 如果集合不存在，就会新建集合user
    user_collection = db.user
    # 1. 查询文档: find({"_id":101})，其中{"_id":101}为查询条件, 若查询条件为空，则默认查询全部
    # find_value = user_collection.find({"_id": 103})
    # print(list(find_value))

    # 2. 如果要实现多条件查询，$and和$or，使用方法如下：
    # AND条件查询
    # find_value = user_collection.find({"$and": [{"_id": 104}, {"author": "小蓝"}]})
    # print(list(find_value))
    # OR条件查询
    # find_value = user_collection.find({"$or": [{"author": "小黄_A"}, {"author": "小黄"}]})
    # print(list(find_value))

    # 3. 根据范围查找: $gt: 大于, $gte: 大于等于, $lt: 小于, $lte: 小于等于, $ne: 不等于,
    # 如查找id&gt;102且id&lt;104(_id=101)的文档
    # find_value = user_collection.find({"_id": {"$gt": 102, "$lt": 104}})
    # print(list(find_value))
    # 查找id在[100,101]的文档
    # find_value = user_collection.find({"_id": {"$in": [100, 101]}})
    # print(list(find_value))
    # find_value = user_collection.find({"and": [{"_id": {"$gt": 102, "$lt": 105}},
    #                                           {"_id": {"$in": [100, 105]}}]})
    # print(list(find_value))

    # 4. 模糊查询实际上是加入正则表达式实现的
    # # 方法一
    # find_value = user_collection.find({"author": {"$regex": ".*小.*"}})
    # print(list(find_value))
    # #方法二
    regex = re.compile(".*小.*")
    find_value = user_collection.find({<!-- -->"author": regex})
    print(list(find_value))

    # 5. 查询嵌入/嵌套文档
    # 查询字段"tags":{"db":"Mongodb","lan":"Python","modle":"Pymongo"}
    # 查询嵌套字段，只需要查询嵌套里的某个值即可
    find_value = user_collection.find({<!-- -->"tags.db": "Mongodb"})
    print(list(find_value))

    # 6. 查询字段"tags":{"db":
    # {"Mongodb":"NoSql","MySql":"Sql"},"lan":"Python","modle":"Pymongo"}
    # find_value = user_collection.find({"tags.db.Mongodb": "NoSql"})
    # print(list(find_value))


def find_many():
    user_collection = db.user

    # 1. 查询文档数量
    # result_data = user_collection.count_documents({})
    # print(result_data)

    # 2. 限定返回结果
    # result_data_limit = user_collection.find({}).limit(2)
    # for result in result_data_limit:
    #     print(result)

    # 3. 对查询结果进行排序: 字段值1表示正序， -1表示倒序
    # user_collection = db.bulk_insert_demo
    # result_data_sort = user_collection.find({'age': {'$gt': 22}}).sort([('age', -1)])
    # print(list(result_data_sort))

    # 4. 对数据进行去重
    user_collection = db.bulk_insert_demo
    # 对age字段去重
    result_data_distinct = user_collection.distinct('age')
    print(list(result_data_distinct))
    # 对满足特定条件的age字段去重
    # result_data_distinct = user_collection.distinct('age', {'age': {'$gte': 22}})
    # print(list(result_data_distinct))

    # 5.偏移
    # results = collection.find().sort('id', pymongo.ASCENDING).skip(1)
    # for result in results:
    #     print(result)


if __name__ == '__main__':
    # 根据条件查询文档
    # find_by_condition()

    # 查询数据
    find_many()

```

#### 三. 更新数据案例

```
# -*- encoding: utf-8 -*-
import pymongo
# 创建对象
client = pymongo.MongoClient('mongodb://账号:密码@主机:端口号/?authSource=admin')
# 连接DB数据库
db = client['数据库名']


def update_one():
    # update_one(筛选条件,更新内容)，筛选条件为空，默认更新第一条文档
    # 如果查询有多条数据，就按照排序先后更新第一条数据
    # {"author": "小蓝"}, {"$set": {"author": "小黄", "text": "数据挖掘"}}
    user_collection = db.user
    user_collection.update_one({<!-- -->"author": "小蓝"}, {<!-- -->"$set": {<!-- -->"author": "小黄", "text": "数据挖掘"}})


def replace_one():
    # replace_one(筛选条件,更新内容)用于将整条数据替换
    # 如果文档的部分数据没有更新，就去除这部分数据
    # topic_data.update_one({"_id": ObjectId(mongo_id)}, {"$set": {'tag_field': 0}})
    user_collection = db.user
    user_collection.replace_one({<!-- -->"author": "小绿"},
                                {<!-- -->"author": "小绿", "text": "Python_django"})


def update_many():
    # update_many(筛选条件,更新内容)用于批量更新文档, 如果查询有多条数据，就会对全部数据进行更新处理
    # topic_data.update_many({"tag_field": {"$exists": False}}, {"$set": {'tag_field': 0}})
    user_collection = db.user
    user_collection.update_many({<!-- -->"author": "小黄"},
                                {<!-- -->"$set": {<!-- -->"text": "Python_web开发"}})


if __name__ == '__main__':
    # 更新单条文档
    # update_one()

    # 替换一条数据
    replace_one()

    # 更新多条数据
    # update_many()

```

#### 四. 删除数据案例

```
# -*- encoding: utf-8 -*-
import pymongo
# 创建对象
# client = pymongo.MongoClient()
client = pymongo.MongoClient('mongodb://账号:密码@主机:端口号/?authSource=admin')
# 连接DB数据库
db = client['数据库名']
user_collection = db.user


def delete_one():
    # 删除单条文档
    # delete_one(筛选条件)，筛选条件为空，默认删除第一条文档
    user_collection.delete_one({<!-- -->"_id": 100})


def delete_many():
    # delete_many(筛选条件)用于删除多条数据
    user_collection.delete_many({<!-- -->"author": "小黄"})


if __name__ == '__main__':
    # 删除单条文档
    delete_one()

    # 删除多条数据
    # delete_many()



```

#### 五. 聚合查询案例

```
import pymongo

handler = pymongo.MongoClient().monog_db.example_user

rows = handler.aggregate([
    {<!-- -->'$lookup': {<!-- -->
        'from': 'example_post',
        'localField': 'id',
        'foreignField': 'user_id',
        'as': 'weibo_info'
        }
    },
    {<!-- -->'$unwind': '$weibo_info'},
    {<!-- -->'$project': {<!-- -->
        'name': 1,
        'work': 1,
        'content': '$weibo_info.content',
        'post_time': '$weibo_info.post_time'}}
])
for row in rows:
    print(row)


```

❤️ 如果觉得有用，感谢一键三连哦 ！！！❤️
