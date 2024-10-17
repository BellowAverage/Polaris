
--- 
title:  sc.toDF 报错 
tags: []
categories: [] 

---
“ValueError: Cannot run multiple SparkContexts at once; existing SparkContext(app=PySparkShell, master=local[*]) ” 原因：出现这个错误是因为之前已经启动了SparkContext 解决方法：查看代码，看是否有多次运行SparkContext实例；也可以先关闭spark（sc.stop() // 关闭spark ），然后再启动。 报错2： “AttributeError: ‘PipelinedRDD’ object has no attribute ‘toDF’” 原因：toDF()是运行在Sparksession（1.X版本的Spark中为SQLContext）内部的一个补丁，如果有其他函数用到toDF()，那么需要先创建SparkSession（）。 解决方法：以IndexedRow()为例，当利用IndexedRow（）产生RDD时，需要

sc=SparkContext() SparkSession(sc)#利用SparkSession来使sc具有处理PipelinedRDD的能力
