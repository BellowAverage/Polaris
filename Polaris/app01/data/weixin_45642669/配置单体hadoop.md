
--- 
title:  配置单体hadoop 
tags: []
categories: [] 

---
### 配置依赖环境

hadoop是Apache的项目，所以依赖java。

有两个必须安装的：
- ssh- Java
##### 安装Java

如果是yum安装的话，那么执行

```
yum list|grep java*

```

看：

```
java-1.8.0-openjdk.x86_64                1:1.8.0.312.b07-1.el7_9       installed

```

这样就可以了。

如果Java不在的话：

```
yum install java-1.8.0-openjdk.x86_64 // 或者其他版本

```

##### 添加path

hadoop是个很奇怪的东西，不能直接：

```
JAVA_PATH = ${JAVA_PAHTH}

```

所以需要先找一下JAVA_PATH（测试一下JAVA_PATH是否可用）

正常情况下，执行

```
cd /usr/lib/jvm

```

里面能找到可用的JDK。

然后选择：

```
export JAVA_HOME=/usr/lib/jvm/jre-openjdk
source ~/.bashrc

```

然后测试一下：

```
$JAVA_HOME/bin/java -version

```

如果有数据的话，那么会：

```
[root@VM-4-6-centos jvm]# $JAVA_HOME/bin/java -version
openjdk version "1.8.0_312"
OpenJDK Runtime Environment (build 1.8.0_312-b07)
OpenJDK 64-Bit Server VM (build 25.312-b07, mixed mode)

```

### 安装hadoop并解压

获取安装路径，选择二进制安装（），不是源码（resource）

推荐的话，文件安装在：/opt

程序安装在：/usr/local

```
cd /opt
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.2/hadoop-3.3.2.tar.gz

```

然后解压

```
tar -xzvf hadoop-3.3.2.tar.gz
mv hadoop-3.3.2 hadoop
mv hadoop /usr/local

```
- 修改命名的原因，是让hadoop容易找
### 修改配置文件

```
vim /usr/local/hadoop/etc/hadoop/hadoop-env.sh

```

两个说法:
- 如果你不写入JAVA_PATH,那么就需要在配置文件写入- 如果写入，那么预先从配置文件找，如果找不到用JAVA_PATH
然后：如果想直接执行hadoop，需要执行：

```
$ cd /usr/local/hadoop
$ ./bin/hadoop version

```

出现这么一个设置，即为单体hadoop配置成功
