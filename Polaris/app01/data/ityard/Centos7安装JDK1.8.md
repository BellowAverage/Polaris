
--- 
title:  Centos7安装JDK1.8 
tags: []
categories: [] 

---
### 1. 下载

`wget https://repo.huaweicloud.com/java/jdk/8u202-b08/jdk-8u202-linux-x64.tar.gz`

<img src="https://img-blog.csdnimg.cn/8bfd28486f1d47459c86387c30d364c2.png" alt=""> 创建安装路径：`mkdir /usr/local/java/`

解压：`tar -zxvf jdk-8u202-linux-x64.tar.gz -C /usr/local/java`

### 2. 配置环境变量

打开配置文件：`vim /etc/profile`

添加配置：

```
export JAVA_HOME=/usr/local/java/jdk1.8.0_202
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH

```

保存：`:wq!`

刷新配置：`source /etc/profile`

添加软链接：`ln -s /usr/local/java/jdk1.8.0_202/bin/java /usr/bin/java`
