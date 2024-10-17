
--- 
title:  linux安装jdk1.8环境 
tags: []
categories: [] 

---
#### 1、官网下载jdk的包：<img src="https://img-blog.csdnimg.cn/img_convert/a50130261e5f18e58b1458055a12bcdf.png#averageHue=#fcfbfa&amp;clientId=ue6d32847-d8bb-4&amp;from=paste&amp;height=42&amp;id=u03879afb&amp;originHeight=53&amp;originWidth=866&amp;originalType=binary&amp;ratio=1&amp;rotation=0&amp;showTitle=false&amp;size=4217&amp;status=done&amp;style=none&amp;taskId=u0856603b-94c9-4064-aea4-e6c628f0f8d&amp;title=&amp;width=692.8" alt="image.png">

#### 2、检查当前系统是否安装jdk：

```
java -version
# 查看java包
rpm -aq | grep java
# 若有原先自带的先卸载，卸载OpenJDK
rpm -e --nodeps java-1.8.0-openjdk-1.8.0.242.b08-1.el7.x86_64
# 或者
yum remove *openjdk*

# 再次查看
rpm -aq | grep java

```

#### 3、上传jdk包到服务器，手动安装JDK：

```
#安装JDK包
rpm -ivh jdk-8u331-linux-x64.rpm
# 进入到安装目录
cd /usr/java/jdk1.8.0_331-amd64/

#添加环境变量
vi /etc/profile
export JAVA_HOME=/usr/java/jdk1.8.0_331-amd64
export CLASSPATH=$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar
export PATH=$JAVA_HOME/bin:$PATH

#刷新配置文件
source /etc/profile

```

```
JAVA_HOME = /opt/jdk1.8.0_181
CLASSPATH = . : $JAVA_HOME/lib/dt.jar : $JAVA_HOME/lib/tools.jar
PATH = $JAVA_HOME/bin : $PATH
export JAVA_HOME CLASSPATH PATH

```

#### 4、检查新安装的JDK

```
java -version
java
javac

```
