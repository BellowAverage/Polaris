
--- 
title:  MongoDB 遇见 spark（进行整合） 
tags: []
categories: [] 

---
基础篇（能解决工作中80%的问题）:
1.   1.   1.   1.   1.   1.   
进阶篇:
1.   1.   1.   1.   1.   1.   1.   
其它:
1.   1.   
#### 一. 与HDFS相比，MongoDB的优势

1、在存储方式上，HDFS以文件为单位，每个文件大小为 64M~128M, 而mongo则表现的更加细颗粒化； 2、MongoDB支持HDFS没有的索引概念，所以在读取速度上更快； 3、MongoDB更加容易进行修改数据； 4、HDFS响应级别为分钟，而MongoDB响应类别为毫秒； 5、可以利用MongoDB强大的 Aggregate功能进行数据筛选或预处理； 6、如果使用MongoDB，就不用像传统模式那样，到Redis内存数据库计算后，再将其另存到HDFS上。

#### 二. 大数据的分层架构

MongoDB可以替换HDFS, 作为大数据平台中最核心的部分，可以分层如下： 第1层：MongoDB或者HDFS; 第2层：资源管理 如 YARN、Mesos、K8S; 第3层：计算引擎 如 MapReduce、Spark; 第4层：程序接口 如 Pig、Hive、Spark SQL、Spark Streaming、Data Frame等

参考：
1.  github： 1.  mongo-python-driver:  1.  官方文档： 
#### 三. 源码介绍

`mongo-spark/examples/src/test/python/introduction.py`

```
# -*- coding: UTF-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# To run this example use:
# ./bin/spark-submit --master "local[4]"  \
#                    --conf "spark.mongodb.input.uri=mongodb://127.0.0.1/test.coll?readPreference=primaryPreferred" \
#                    --conf "spark.mongodb.output.uri=mongodb://127.0.0.1/test.coll" \
#                    --packages org.mongodb.spark:mongo-spark-connector_2.11:2.0.0 \
#                    introduction.py
from pyspark.sql import SparkSession
if __name__ == "__main__":
    spark = SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()
    logger = spark._jvm.org.apache.log4j
    logger.LogManager.getRootLogger().setLevel(logger.Level.FATAL)
    # Save some data
    characters = spark.createDataFrame([("Bilbo Baggins",  50), ("Gandalf", 1000), ("Thorin", 195), ("Balin", 178), ("Kili", 77), ("Dwalin", 169), ("Oin", 167), ("Gloin", 158), ("Fili", 82), ("Bombur", None)], ["name", "age"])
    characters.write.format("com.mongodb.spark.sql").mode("overwrite").save()
    # print the schema
    print("Schema:")
    characters.printSchema()
    # read from MongoDB collection
    df = spark.read.format("com.mongodb.spark.sql").load()
    # SQL
    df.registerTempTable("temp")
    centenarians = spark.sql("SELECT name, age FROM temp WHERE age &gt;= 100")
    print("Centenarians:")
    centenarians.show()

```
