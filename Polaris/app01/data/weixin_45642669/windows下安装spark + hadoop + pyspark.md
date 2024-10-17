
--- 
title:  windows下安装spark + hadoop + pyspark 
tags: []
categories: [] 

---
### 选择版本
- spark依赖的是hadoop和Java spark、hadoop和python的适配- hadoop2.x都是基于java7开发的- hadoop3.x是基于java8开发的 
里面有各种依赖的关系 第二种方法：下载：在spark官网的最后一行蓝色，有老版本下载的链接 文件有两个：
- spark大小大概200M，小的不是- 如果带hadoopX版本，才是能够hadoop执行的。- hadoop是执行hadoop的版本，所以直接执行hadoop意见。 spark的JDK依赖如下： 整体的要求如下：
Spark runs on Java 8/11, Scala 2.12/2.13, Python 3.6+ and R 3.5+. Python 3.6 support is deprecated as of Spark 3.2.0. Java 8 prior to version 8u201 support is deprecated as of Spark 3.2.0. For the Scala API, Spark 3.2.1 uses Scala 2.12. You will need to use a compatible Scala version (2.12.x).

#### 一些重要的细节
- hadoop不支持windows，需要安装一个插件，但是这个插件他更新的不太频繁……凑合着用<li>建议大家用JDK8 + hadoop2.7+ spark3.X + python3.7，各个版本互相有依赖 
  <ul>- python3.9太高了，建议3.7- 对于spark3.X， jdk7太低，jdk12+太高，会出现hadoop成功而spark无法运行，就是支持的最低版本，而不是无脑最新（这个很重要！！！！！！JDK必须是8/11）
### 安装Java
<li>到官网下载JDK 
  <ul>- 有一个问题：spark不支持最新的JDK，所以建议直接JDK8（似乎有说法高版本JDK带旧版本JDK？反正不支持就是了）- 有空格不然找不到- path- java -version
如果正常提示Java有环境的话java 环境配置完成

### 下载hadoop
-  官网下载hadoop（下载带bin的、binary，大概200M） -  写入到没有空格的文件夹里面 -  选择winutils支持的hadoop和Spark版本 -  写入HADOOP_HOME为hadoop根路径 -  path写入 %HADOOP%/bin和%HADOOP%/sbin(可选) <li> 下载winutils。替换bin（这个文件很小） 
  <ul>- 这个软件更新很慢，我看的时候是3.0版本，建议大家用2.7版本
cmd执行set PATH=C

退出cmd以后执行：
- path- hadoop- start-all（不推荐，因为很多程序都用start-all）- JPS
当有5个进程同时启动，hadoop配置完成

### 下载spark
<li>官网下载spark 
  <ul>- 有两个版本，第一个版本是带hadoop支持的，sparkXXX - hadoopXXX，还有不支持的，sparkXXX。下载支持的。- path- spark-shell
如果有结果配置完成

报错信息：
- 如果找不到Path，那么就是JDK环境变量有问题。<li>spark起来是不需要hadoop的，以报错分成两部分： 
  <ul>- hadoop是否起来，是否配置成功- spark是否成功- 如果起来可以配置，
```
_JAVA_OPTIONS: -Xmx800M

```
- 提示XX类找不到，那就死JDK的版本低或者高了
### PYTHON调用spark
- pip安装pyspark和findspark- 写入%SPARK_HOME%/python和%SPARK_HOME%\python\lib\py4j-0.10.9-src.zip（以防万一）- 测试下：
```
# 必须预先配置findspark
import findspark
findspark.init()


import pyspark
from pyspark.sql import SparkSession

SparkSession.Builder.appName('aaa').getOrCreate()
# 自己找一个文件试试
df = sc.read.csv(r'F:\1.csv', encoding='GBK')
df.show()

```

执行以后如果成功没有报错，说明正确 提示：
<li>在运行之前退出，有这么几种可能：JDK环境变量没配 
  <ul>- cmd测试下spark-shell，看是否成功，错误的话可以看报错信息