
--- 
title:  hadoop套件的安装与配置个人笔记 
tags: []
categories: [] 

---
### hadoop的官网



### 下载并安装hadoop（本人使用的是2.10.1）
1. 下载：1. 安装：`tar -zxvf 解压文件`1. 在linux 环境下也可以 直接用 wget http地址 的形式下载
### 配置hadoop及启动
<li> 集群最好改动一下hadoop的java配置地址：准备启动 Hadoop 群集，解包下载的 Hadoop 分发。在分发中，编辑文件etc/hadoop/hadoop-env.sh以定义一些参数，如下所示 <pre><code class="prism language-java"># set to the root of your Java installation
export JAVA_HOME=/usr/java/latest
</code></pre> </li><li> 单个机子部署（使用伪分布式）配置： 修改etc/hadoop/core-site.xml 文件 <pre><code class="prism language-java">&lt;configuration&gt;
	#配置成hdfs模式
    &lt;property&gt;
        &lt;name&gt;fs.defaultFS&lt;/name&gt;
        &lt;value&gt;hdfs://localhost:9000&lt;/value&gt;
    &lt;/property&gt;
    #将生产模式的运行日志生成到指定位置
    &lt;property&gt;
            &lt;name&gt;hadoop.tmp.dir&lt;/name&gt;
            &lt;value&gt;/opt/hadoop/hadoop-2.10.1/data/tmp&lt;/value&gt;
    &lt;/property&gt;
&lt;/configuration&gt;
</code></pre> 修改etc/hadoop/hdfs-site.xml 文件 <pre><code class="prism language-java">&lt;configuration&gt;
    &lt;property&gt;
        &lt;name&gt;dfs.replication&lt;/name&gt;
        &lt;value&gt;1&lt;/value&gt;
    &lt;/property&gt;
&lt;/configuration&gt;
</code></pre> </li><li> 第一次启动namenode 一定要格式化（只在第一次启动时需要格式化，其他情况不需要） <pre><code class="prism language-java">bin/hdfs namenode -format
</code></pre> </li><li> 启动namenode <pre><code class="prism language-java">#启动
sbin/hadoop-daemon.sh start namenode
#停止
sbin/hadoop-daemon.sh stop namenode
</code></pre> </li><li> 启动datanode <pre><code class="prism language-java">#启动
sbin/hadoop-daemon.sh start datanode
#停止
sbin/hadoop-daemon.sh stop datanode
</code></pre> </li>-  启动好之后可以通过`服务器ip:50070`查看情况 <li> 创建文件（需要配置使用hdfs才能用） <pre><code class="prism language-java">bin/hdfs dfs -mkdir /user
bin/hdfs dfs -mkdir /user/&lt;username&gt;
#将输入文件复制到分布式文件系统中
bin/hdfs dfs -mkdir input
bin/hdfs dfs -put etc/hadoop/*.xml input
#运行提供的一些示例
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.1.jar grep input output 'dfs[a-z.]+'
#检查输出文件：将输出文件从分布式文件系统复制到本地文件系统并检查它们
bin/hdfs dfs -get output output
cat output/*
#或者
bin/hdfs dfs -cat output/*
</code></pre> </li>
**配置下hadoop的环境**

```
vim /etc/profile

#hadoop
export HADOOP_HOME=/home/wj/hadoop2.7.7
export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH

source /etc/profile

```

### 安装hive

<img src="https://img-blog.csdnimg.cn/20201122195325210.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 官网下载相应的包

配置环境（一定要先配置好 hadoop的环境）

```
vim /etc/profile

#hive  
export HIVE_HOME=/usr/local/hive
export PATH=$PATH:$HIVE_HOME/bin

source /etc/profile

```

<img src="https://img-blog.csdnimg.cn/20201122195538823.png#pic_center" alt="在这里插入图片描述"> **建立Hive专用的元数据库**

>  
 在Hive的conf目录下的文件“hive-site.xml”中增加如下配置 原目录没有，可以vim 创建一个hive-site.xml 


```
&lt;configuration&gt;
&lt;property&gt;
    &lt;name&gt;javax.jdo.option.ConnectionURL&lt;/name&gt;
    &lt;value&gt;jdbc:mysql://gz-cdb-73kggk47.sql.tencentcdb.com:63524/hive?createDatabaseIfNotExist=true&lt;/value&gt;
&lt;/property&gt;
&lt;property&gt;
    &lt;name&gt;javax.jdo.option.ConnectionDriverName&lt;/name&gt;
    &lt;value&gt;com.mysql.jdbc.Driver&lt;/value&gt;
&lt;/property&gt;
&lt;property&gt;
    &lt;name&gt;javax.jdo.option.ConnectionUserName&lt;/name&gt;
    &lt;value&gt;root&lt;/value&gt;
&lt;/property&gt;
&lt;property&gt;
    &lt;name&gt;javax.jdo.option.ConnectionPassword&lt;/name&gt;
    &lt;value&gt;ccnfgame001&lt;/value&gt;
&lt;/property&gt;
&lt;/configuration&gt;

```

**把MySQL的JDBC驱动包复制到Hive的lib目录下（略，下载地址：https://dev.mysql.com/downloads/connector/j/）**

>  
 （驱动包名为：mysql-connector-java-5.1.46-bin.jar）看自己数据库什么版本，就下载什么版本就行了 


**检查连接 在bin目录下运行以下代码**

```
./schematool -initSchema -dbType mysql

```

<img src="https://img-blog.csdnimg.cn/20201123103735723.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> **hive 远程服务 (端口号10000) 启动方式 （Thrift服务）**

```
bin/hive –service hiveserver2 &amp;（&amp;表示后台运行）
用java，python等程序实现通过jdbc等驱动的访问hive就用这种起动方式了，这个是程序员最需要的方式了

```



### 安装spark

官网下载相应的包

scala

配置环境（一定要先配置好 hadoop的环境）

```
vim /etc/profile

#scala
export SCALA_HOME=/home/ubuntu/ljq/hadoopAll/spark/scala-2.12.12
export PATH=$PATH:$SCALA_HOME/bin


source /etc/profile

```


