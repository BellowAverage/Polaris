
--- 
title:  Spark2.1.0安装与配置（单机版） 
tags: []
categories: [] 

---
## Spark2.1.0安装与配置（单机版）

B站同步视频：

### 前言

该安装教程是承接所制，因此所使用的安装包是在`Spark源码编译`教程中得到`spark-2.1.0-bin-rh27hive.tgz`文件以及官网的`spark-2.1.0-bin-hadoop2.7.tgz` ，其实两个文件的功能几乎相同。

>  
 关于为什么进行Spark源码编译，主要是因为个人喜好 ，编译在个人看来只是一种体验。 


下载官网`https://archive.apache.org/dist/spark/`提供的安装包，毕竟是官方的，会可靠点，其中有without-hadoop和hadoop2.x或hadoop3.x的，`spark-2.1.0-bin-hadoop2.7.tgz` 是含hive支持的，`spark-2.1.0-bin-without-hadoop.tgz` 是不含hive支持的，含支持的编译命令与自定义编译的命令是相同的（除了hadoop版本，可查看安装包文件中根目录的`RELEASE`文件）

>  
 这里主要想通过这两个含支持和不含支持的安装包介绍多版本Spark的安装，关于选择哪个安装，这里不做引导，各有各的好，不含支持的比较轻量，含支持的比较完整！ 


关于其它介绍，这里就不过多展开了，毕竟自己也是小白一枚。

### 一、单版本（含Hive支持官方版&amp;自定义编译）

官网的和自定义编译得到的两个功能一致，选其一安装即可。如步骤中不分类，则说明两者的操作是相同的。

#### 第一步 获取安装包

##### ① 官方提供的安装包

这里主要介绍`Spark2.1.0` 的安装（`spark-2.1.0-bin-hadoop2.7.tgz`），其它版本类似，如需安装其它版本，请自行更改版本哦。下载链接见上面提到的官网https://archive.apache.org/dist/spark/，请自行找到合适的版本获取下载链接。这个下载会很慢，建议是在Windows平台下使用迅雷下载，下载完再拖进去。

如果是安装Spark3.x的话可以使用清华源：https://mirrors.tuna.tsinghua.edu.cn/apache/spark/

```
cd ~
wget https://archive.apache.org/dist/spark/spark-2.1.0/spark-2.1.0-bin-hadoop2.7.tgz

```

迅雷下载会相对快一点点，这里已经下载好了的，就不演示了

##### ② 自定义编译得到的安装包

详见视频：Ubuntu下Spark2.1.0源码编译打包（https://www.bilibili.com/video/BV1eB4y187Gf?spm_id_from=333.999.list.card_archive.click&amp;vd_source=3c792130f317de0ed318a3e6ad0e583b）

得到的安装包为：`spark-2.1.0-bin-rh27hive.tgz`

#### 第二步 解压安装

##### ① 官网提供的安装包

```
sudo tar -zxf ~/spark-2.1.0-bin-hadoop2.7.tgz -C /usr/local/
cd /usr/local
sudo mv ./spark-2.1.0-bin-hadoop2.7 ./spark
sudo chmod -R 777 ./spark

```

##### ② 自定义编译得到的安装包

```
sudo tar -zxf ~/spark-2.1.0-bin-rh27hive.tgz -C /usr/local/
cd /usr/local
sudo mv ./spark-2.1.0-bin-rh27hive ./spark
sudo chmod -R 777 ./spark

```

#### 第三步 配置

因为包含`Hive支持`，这里`Hive安装配置`时是基于`MySQL 5.7`的，所以需要用到`MySQL 5.7`的驱动`mysql-connector-java-5.1.40-bin.jar` 。

##### ① 拷贝Hive配置文件（`hive-site.xml` 和MySQL驱动）

如果你的Hive是基于MySQL的，那么应该会配置过MySQL驱动，可以使用Hive的(其中`mysql-connector-java-5.1.40-bin.jar` 请改为自己的)

```
cd /usr/local/hive
cp ./conf/hive-site.xml /usr/local/spark/conf/
mkdir /usr/local/spark/jars/mysql
cp ./lib/mysql-connector-java-5.1.40-bin.jar /usr/local/spark/jars/mysql

```

如果hive里面没有MySQL，则请先下载

如果没有，可以通过该链接（https://wwt.lanzouf.com/ivdPR08couhc）下载，由于是动态链接，好像不能使用wget下载，所以需要在虚拟机的浏览器打开下载，默认保存在`~/下载`目录。如果是其它版本的MySQL，上述驱动应该不适用，请自行准备，至于在哪里可以下载，这里搜刮了一些版本的，请自己去查是适合哪个版本的。

（ 阿里云盘 https://www.aliyundrive.com/s/PdJJPvNuYTg 提取码: ydny）

```
cp ~/下载/mysql-connector-java-5.1.40-bin.jar /usr/local/spark/jars/mysql

```

给出 `hive-site.xml` 的内容

```
&lt;?xml version="1.0" encoding="UTF-8" standalone="no"?&gt;
&lt;?xml-stylesheet type="text/xsl" href="configuration.xsl"?&gt;
&lt;configuration&gt;
  &lt;property&gt;
    &lt;name&gt;javax.jdo.option.ConnectionURL&lt;/name&gt;
    &lt;value&gt;jdbc:mysql://localhost:3306/hive?createDatabaseIfNotExist=true&amp;amp;useSSL=false&lt;/value&gt;
    &lt;description&gt;JDBC connect string for a JDBC metastore&lt;/description&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;javax.jdo.option.ConnectionDriverName&lt;/name&gt;
    &lt;value&gt;com.mysql.jdbc.Driver&lt;/value&gt;
    &lt;description&gt;Driver class name for a JDBC metastore&lt;/description&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;javax.jdo.option.ConnectionUserName&lt;/name&gt;
    &lt;value&gt;hive&lt;/value&gt;
    &lt;description&gt;username to use against metastore database&lt;/description&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;javax.jdo.option.ConnectionPassword&lt;/name&gt;
    &lt;value&gt;hive&lt;/value&gt;
    &lt;description&gt;password to use against metastore database&lt;/description&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;hive.metastore.schema.verification&lt;/name&gt;
    &lt;value&gt;false&lt;/value&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;datanucleus.schema.autoCreateAll&lt;/name&gt;
    &lt;value&gt;true&lt;/value&gt;
  &lt;/property&gt;
  &lt;!-- Hive产生的元数据存放位置--&gt;
  &lt;property&gt;
    &lt;name&gt;hive.metastore.warehouse.dir&lt;/name&gt;
    &lt;value&gt;/user/hive/warehouse&lt;/value&gt;
  &lt;/property&gt;
&lt;/configuration&gt;

```

##### ② 添加环境变量

```
gedit ~/.bashrc

```

```
#确保配置hadoop的环境变量时下存在下面的内容，不存在则添加（取消#注释即可）
#export JAVA_LIBRARY_PATH=$HADOOP_HOME/lib/native/
#[Spark]
export SPARK_HOME=/usr/local/spark
export PATH=$PATH:$SPARK_HOME/bin

```

```
source ~/.bashrc

```

##### ③ Spark配置

关于这个slf4j-log4j12-1.7.16.jar是日志文件，因为配置了hadoop的classpath之后会重复，启动spark时会输出一些警告，当然可忽略，个人不喜欢，就去掉了一个，如果需要，可以反向操作，恢复即可。

```
cd /usr/local/spark
mv ./jars/slf4j-log4j12-1.7.16.jar ./jars/slf4j-log4j12-1.7.16.jar.template
cp ./conf/spark-env.sh.template ./conf/spark-env.sh
gedit ./conf/spark-env.sh

```

在开头`第二行空白`位置，添加下面内容，里面的XXX_HOME是环境变量中自己已经配置好的。，其中`PYSPARK_PYTHON`只能指向小于3.6的，因为Spark2.1.0还不支持3.6及以上的。

```
export SPARK_DIST_CLASSPATH=$(${<!-- -->HADOOP_HOME}/bin/hadoop classpath)
export LD_LIBRARY_PATH=${JAVA_LIBRARY_PATH}
export JAVA_HOME=${JAVA_HOME}
export CLASSPATH=$CLASSPATH:${HIVE_HOME}/lib
export SCALA_HOME=${SCALA_HOME}
export HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop
export HIVE_CONF_DIR=${HIVE_HOME}/conf
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip:$PYTHONPATH
export PYSPARK_PYTHON=python3.5
# 单机版配置为本机 ip
export SPARK_MASTER_IP=127.0.0.1
export SPARK_LOCAL_IP=127.0.0.1

```

##### ④ 设置输出日志的等级

```
cd /usr/local/spark
cp ./conf/log4j.properties.template ./conf/log4j.properties
gedit ./conf/log4j.properties

```

在开头位置找到下面的内容

```
# Set everything to be logged to the console
log4j.rootCategory=INFO, console

```

将`INFO`改为`WARN`

```
log4j.rootCategory=WARN, console

```

##### ⑤ 设置类(依赖包)路径

```
cd /usr/local/spark
cp ./conf/spark-defaults.conf.template ./conf/spark-defaults.conf
gedit ./conf/spark-defaults.conf

```

在最后添加以下两行内容

extraJavaOptions属性中是定向使用日志文件的配置，如果适用该文件进行配置，原日志文件的配置不会自动生效，可能是被覆盖的原因，这里需要重新指向，

extraClassPath属性是类路径，如果后续需要添加例如Hbase或kafka依赖，就可以在后面继续添加，就不用在程序提交时指定这些依赖的路径，多个类路径以`:` 分隔

```
spark.driver.extraJavaOptions      -Dlog4j.configuration=file:/usr/local/spark/conf/log4j.properties
spark.driver.extraClassPath        /usr/local/spark/jars/*:/usr/local/spark/jars/mysql/*

```

给出一个添加Hbase类路径的例子

```
cd  /usr/local/spark/jars
mkdir  hbase
cp  /usr/local/hbase/lib/hbase*.jar  ./hbase
cp  /usr/local/hbase/lib/guava-12.0.1.jar  ./hbase
cp  /usr/local/hbase/lib/htrace-core-3.1.0-incubating.jar  ./hbase
cp  /usr/local/hbase/lib/protobuf-java-2.5.0.jar  ./hbase
cd  /usr/local/spark
gedit ./conf/spark-defaults.conf

```

在extraClassPath属性原有基础上加上：`:/usr/local/spark/jars/hbase/*`

```
spark.driver.extraClassPath        /usr/local/spark/jars/*:/usr/local/spark/jars/mysql/*:/usr/local/spark/jars/hbase/*

```

到这里就安装完成了！！

#### 第四步 测试

下面进行简单的测试，输出圆周率的近似数

```
cd /usr/local/spark
./bin/run-example SparkPi 2&gt;&amp;1 | grep "Pi is roughly"

```

为了测试连接Hadoop，这里做点前期工作

```
gedit ~/test.csv

```

```
X国,1,1,0,0,2020-01-20
Y国,0,1,0,0,2020-01-21
Z国,0,1,0,0,2020-01-22
Q国,0,1,0,0,2020-01-23
A国,1,2,0,0,2020-01-24
C国,0,2,0,0,2020-01-25

```

```
cd /usr/local/hadoop
./sbin/start-dfs.sh
./bin/hdfs dfs -mkdir /SparkTest
./bin/hdfs dfs -put ~/test.csv /SparkTest
./bin/hdfs dfs -cat /SparkTest/test.csv | head -5

```

启动mysql服务（一般安装后是默认自启动的）

```
sudo service mysql start

```

启动Spark-Shell（注意`hive`中不能存在`global_temp`数据库）

```
cd /usr/local/spark
./bin/spark-shell

```

第一行的`global_temp`数据库警告可忽略，因为这个是缓存数据库，如果hive中事先已经存在，那么Spark启动时会报错的。这个警告应该只是输出一下，并没有影响。

第一次启动会出现hive版本的问题，前面的hive-site.xml中配置了不进行版本验证，可能第一次会验证，后续启动就不会了

测试hadoop

```
val inputDF = spark.read.csv("hdfs://localhost:9000/SparkTest/test.csv")
inputDF.show()

```

测试是否有hive支持，（hbase），支持时会重复输出导包内容和hive中存在的数据库

关于hive支持与spark sql的区别，这里不太清楚，因为spark sql是spark本身的一部分

```
import org.apache.spark.sql.hive.HiveContext
spark.sql("show databases").show()
import org.apache.hadoop.hbase.mapreduce.TableInputFormat
:quit

```

启动pyspark

```
cd /usr/local/spark
./bin/pyspark
exit()

```

### 二、多版本（官方版without-hadoop）

这里提供`官方版without-hadoop`的`单版本`安装和`多版本`安装两个方法，自行选择。

这里前面已经安装过一个了，就演示多版本的安装。

多版本在这里认为的是，上面已经安装的是`主版本`，而其它额外安装的为`子版本`，如果需要将原版本作为子版本，则请先对原版本安装目录更名（`sudo mv /usr/local/spark /usr/local/spark-sub`），再对原版本进行该模块的教程更改内容，或者卸载原版本也可以，再重装。方法很多，看个人喜欢。

卸载就是删除原安装目录文件和移除环境变量即可

```
##如无需卸载，请勿执行该内容
sudo rm -rf /usr/local/spark
gedit ~/.bashrc
source ~/.bashrc

```

#### 第一步 获取安装包

##### 官方提供的安装包

这里主要介绍`Spark2.1.0` 的安装（`spark-2.1.0-bin-without-hadoop.tgz`），其它版本类似，如需安装其它版本，请自行更改版本哦。下载链接见上面提到的官网https://archive.apache.org/dist/spark/，请自行找到合适的版本获取下载链接。这个下载会很慢，建议是在Windows平台下使用迅雷下载，下载完再拖进去。

```
cd ~
wget https://archive.apache.org/dist/spark/spark-2.1.0/spark-2.1.0-bin-without-hadoop.tgz

```

##### 

#### 第二步 解压安装

##### ① 单版本安装

```
sudo tar -zxf ~/spark-2.1.0-bin-without-hadoop.tgz -C /usr/local/
cd /usr/local
sudo mv ./spark-2.1.0-bin-without-hadoop ./spark
sudo chmod -R 777 ./spark

```

##### ② 多版本安装

注意多版本安装时，安装的目录名时不一致的，这里使用的是spark-sub，可以改成自己喜欢的，但不能与已存在的相同

```
sudo tar -zxf ~/spark-2.1.0-bin-without-hadoop.tgz -C /usr/local/
cd /usr/local
sudo mv ./spark-2.1.0-bin-without-hadoop ./spark-sub
sudo chmod -R 777 ./spark-sub

```

#### 第三步 配置

虽然不包含hive支持，但可能需要操作MySQL，所以也是需要用到`MySQL 5.7`的驱动`mysql-connector-java-5.1.40-bin.jar` 。

##### ① 拷贝MySQL驱动

如果没有，可以通过该链接（https://wwt.lanzouf.com/ivdPR08couhc）下载，由于是动态链接，好像不能使用wget下载，所以需要在虚拟机的浏览器打开下载，默认保存在`~/下载`目录。如果是其它版本的MySQL，上述驱动应该不适用，请自行准备，至于在哪里可以下载，这里搜刮了一些版本的，请自己去查是适合哪个版本的。

（ 阿里云盘 https://www.aliyundrive.com/s/PdJJPvNuYTg 提取码: ydny）

###### 1）单版本

```
mkdir /usr/local/spark/jars/mysql
cp ~/下载/mysql-connector-java-5.1.40-bin.jar /usr/local/spark/jars/mysql

```

###### 2）多版本

```
mkdir /usr/local/spark-sub/jars/mysql
cp ~/下载/mysql-connector-java-5.1.40-bin.jar /usr/local/spark-sub/jars/mysql

```

##### ② 添加环境变量

###### 1）单版本

```
gedit ~/.bashrc

```

```
#确保配置hadoop的环境变量时下存在下面的内容，不存在则添加（取消#注释即可）
#export JAVA_LIBRARY_PATH=$HADOOP_HOME/lib/native/
#[Spark]
export SPARK_HOME=/usr/local/spark
export PATH=$PATH:$SPARK_HOME/bin

```

```
source ~/.bashrc

```

###### 2）多版本

因为是安装多个spark，这里需要采用`临时添加环境变量`的方式，即在启动时重新更新环境变量SPARK_HOME，更新后并不会影响原本的spark配置，如不添加，则会启动默认（原有）的spark。当然有添加不同的环境变量的方式，但这样会使启动命令有所改变，而临时添加的方式不需要更改命令（看个人习惯），不过需要注意到是：临时添加环境变量的方式需要使用完整路径才能启动子版本，因为它只在启动的时候才会重定向。对于添加不同的环境变量，这种话方式比较麻烦，需要移除原有的SPARK_HOME环境变量，使用不同的名称，例如SPARK1_HOME，SPARK2_HOME，因为一旦存在SPARK_HOME，不管哪个版本，都会指向配置的那个版本。

```
cd /usr/local/spark-sub
gedit ./bin/spark-shell

```

开头空白行添加内容

```
export SPARK_HOME=/usr/local/spark-sub
export PATH=$PATH:SPARK_HOME/bin

```

对pyspark，sparkR，spark-sql，spark-submit也需要进行同样的操作

```
cd /usr/local/spark-sub
gedit ./bin/pyspark
gedit ./bin/sparkR
gedit ./bin/spark-sql
gedit ./bin/spark-submit

```

##### ③ Spark配置

###### 1)单版本

```
cd /usr/local/spark

```

###### 2)多版本

```
cd /usr/local/spark-sub

```

1,2共同内容：

```
mv ./jars/slf4j-log4j12-1.7.16.jar ./jars/slf4j-log4j12-1.7.16.jar.template  #没有没关系
cp ./conf/spark-env.sh.template ./conf/spark-env.sh
gedit ./conf/spark-env.sh

```

在开头`第二行空白`位置，添加下面内容，里面的XXX_HOME是环境变量中自己已经配置好的。

```
export SPARK_DIST_CLASSPATH=$(${<!-- -->HADOOP_HOME}/bin/hadoop classpath)
export JAVA_HOME=${JAVA_HOME}
export SCALA_HOME=${SCALA_HOME}
export HADOOP_HOME=${HADOOP_HOME}
export HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop
export LD_LIBRARY_PATH=${JAVA_LIBRARY_PATH}
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip:$PYTHONPATH
export PYSPARK_PYTHON=python3.5
# 单机版配置为本机 ip
export SPARK_MASTER_IP=127.0.0.1
export SPARK_LOCAL_IP=127.0.0.1

```

##### ④ 设置输出日志的等级

###### 1)单版本

```
cd /usr/local/spark

```

###### 2)多版本

```
cd /usr/local/spark-sub

```

1,2共同内容：

```
cp ./conf/log4j.properties.template ./conf/log4j.properties
gedit ./conf/log4j.properties

```

在开头位置找到下面的内容

```
# Set everything to be logged to the console
log4j.rootCategory=INFO, console

```

将`INFO`改为`WARN`

```
log4j.rootCategory=WARN, console

```

##### ⑤ 设置类(依赖包)路径

###### 1)单版本

```
cd /usr/local/spark

```

###### 2)多版本

```
cd /usr/local/spark-sub

```

1,2共同内容：

```
cp ./conf/spark-defaults.conf.template ./conf/spark-defaults.conf
gedit ./conf/spark-defaults.conf

```

在最后添加以下两行内容

extraJavaOptions属性中是定向使用日志文件的配置，如果适用该文件进行配置，原日志文件的配置不会自动生效，可能是被覆盖的原因，这里需要重新指向，

extraClassPath属性是类路径，如果后续需要添加例如Hbase或kafka依赖，就可以在后面继续添加，就不用在程序提交时指定这些依赖的路径，多个类路径以`:` 分隔

###### 1)单版本

```
spark.driver.extraJavaOptions      -Dlog4j.configuration=file:/usr/local/spark/conf/log4j.properties
spark.driver.extraClassPath        /usr/local/spark/jars/*:/usr/local/spark/jars/mysql/*

```

###### 2)多版本

```
spark.driver.extraJavaOptions      -Dlog4j.configuration=file:/usr/local/spark-sub/conf/log4j.properties
spark.driver.extraClassPath        /usr/local/spark-sub/jars/*:/usr/local/spark-sub/jars/mysql/*

```

到这里就安装完成了！！

#### 第四步 测试

为了测试连接Hadoop，这里做点前期工作，如果前面已经做过，可跳过

```
gedit ~/test.csv

```

```
X国,1,1,0,0,2020-01-20
Y国,0,1,0,0,2020-01-21
Z国,0,1,0,0,2020-01-22
Q国,0,1,0,0,2020-01-23
A国,1,2,0,0,2020-01-24
C国,0,2,0,0,2020-01-25

```

```
cd /usr/local/hadoop
./sbin/start-dfs.sh
./bin/hdfs dfs -mkdir /SparkTest
./bin/hdfs dfs -put ~/test.csv /SparkTest
./bin/hdfs dfs -cat /SparkTest/test.csv | head -5

```

##### ① 单版本

下面进行简单的测试，输出圆周率的近似数

```
cd /usr/local/spark
./bin/run-example SparkPi 2&gt;&amp;1 | grep "Pi is roughly"

```

启动Spark-Shell

```
cd /usr/local/spark
./bin/spark-shell

```

测试hadoop

```
val inputDF = spark.read.csv("hdfs://localhost:9000/SparkTest/test.csv")
inputDF.show()

```

测试是否有hive支持，应该是不支持的

```
import org.apache.spark.sql.hive.HiveContext
:quit

```

启动pyspark

```
cd /usr/local/spark
./bin/pyspark
exit()

```

##### ② 多版本

下面进行简单的测试，输出圆周率的近似数

```
cd /usr/local/spark-sub
./bin/run-example SparkPi 2&gt;&amp;1 | grep "Pi is roughly"

```

启动Spark-Shell

```
cd /usr/local/spark-sub
./bin/spark-shell

```

测试hadoop

```
val inputDF = spark.read.csv("hdfs://localhost:9000/SparkTest/test.csv")
inputDF.show()

```

测试是否有hive支持，应该是不支持的，支持时会重复输出

```
import org.apache.spark.sql.hive.HiveContext
:quit

```

如果把临时添加环境变量去掉，再测试是否支持Hive，因为启动的是支持hive的，这个效果在使用不同Spark版本时，可能会更明显。

`可以看到启动without hadoop的是没有那个数据库警告的，但去掉临时环境变量之后，就出现了，说明启动的并不是without -hadoop的spark，而且也含有hive支持`

```
cd /usr/local/spark-sub
gedit ./bin/spark-shell

```

将配置的环境变量注释

```
#export SPARK_HOME=/usr/local/spark-sub
#export PATH=$PATH:SPARK_HOME/bin

```

再执行上面的操作。

启动pyspark

```
cd /usr/local/spark-sub
./bin/pyspark
exit()

```
