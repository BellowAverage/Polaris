
--- 
title:  Centos7部署JDK 
tags: []
categories: [] 

---
## Centos7部署Oracle JDK



#### 文章目录
- - <ul><li><ul><li>- - - - - - - 


#### 1）下载文件

#### 2）将window主机 的Oracle JDK上传到Centos7 的/usr

<img src="https://img-blog.csdnimg.cn/bc8201174b4f43c68a2323f821dd99e1.png#pic_center" alt="在这里插入图片描述">

#### 3）新建java目录

```
[hadoop@masterroot]#mkdir /usr/java

```

<img src="https://img-blog.csdnimg.cn/c71c69ee7c7c460fbee50e2e9f777809.png#pic_center" alt="在这里插入图片描述">

#### 4）将java的安装包解压到java目录

```
[root@localhost java]# tar -zxvf jdk-8u341-linux-x64.tar.gz -C /usr/java/

```

<img src="https://img-blog.csdnimg.cn/e91d00b4bf574c1db976c6fd08f07217.png#pic_center" alt="在这里插入图片描述">

```
[root@localhost java]# cd /usr/java
[root@localhost java]# ls

```

<img src="https://img-blog.csdnimg.cn/cd7ac29478ed44a9acb3e11b75b773a1.png#pic_center" alt="在这里插入图片描述">

#### 5）配置环境变量

```
[hadoop@masterroot]# vim /etc/profile 

```

<img src="https://img-blog.csdnimg.cn/1965d4ecd8ae495a8b4e37b0bad07514.png#pic_center" alt="在这里插入图片描述">

在文件后面添加环境变量：

```
export JAVA_HOME=/usr/java/jdk1.8.0_341
export JRE_HOME=/usr/java/jdk1.8.0_341/jre
export CLASSPATH=.:$CLASSPATH:$JAVA_HOME/lib:$JRE_HOME/lib
export PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin

```

<img src="https://img-blog.csdnimg.cn/c57651bd063e467dbe3796da78f0c915.png#pic_center" alt="在这里插入图片描述">

#### 6）使环境变量生效

[hadoop@masterroot]$source /etc/profile

<img src="https://img-blog.csdnimg.cn/99ef5fdc8b16488dade879c2a85df70c.png#pic_center" alt="在这里插入图片描述">

#### 7）将Centos7自带的openjdk替换成Oracle jdk

[root@localhost bin]# ln -s -f /usr/java/jdk1.8.0_341/jre/bin/java /usr/bin [root@localhost bin]# ln -s -f /usr/java/jdk1.8.0_341/bin/javac /usr/bin

#### 8）验证安装

[hadoop@master~]$java -version <img src="https://img-blog.csdnimg.cn/7bc5ddb43077402898ed82d54aa72be9.png#pic_center" alt="在这里插入图片描述">
