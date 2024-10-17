
--- 
title:  [JSPWiki]JSPWiki安装部署与配置 
tags: []
categories: [] 

---
## 1、JSPWiki安装部署

Linux下JSPWiki的安装部署。目的是可自定义改造。 如果想先体验，可以选择docker安装。

>  
 **docker**安装看这里 // 命令 docker pull apache/jspwiki docker run -d -p 8080:8080 --name jspwiki apache/jspwiki // 访问 http://localhost:8080/ // 没有docker的百度关键词 linux yum安装配置 linux docker安装配置 




#### 目录
- - <ul><li>- - <ul><li>- 


### 1.1、介绍
- 官网: https://jspwiki.apache.org/- github： https://github.com/apache/jspwiki- 安装环境
```
前置条件：
Tomcat 9.x or higher
JDK 1.8 or higher

```

### 1.2、前置环境安装

#### 1.2.1JDK

进入https://www.oracle.com/java/technologies/downloads/archive/，选择需要的版本 <img src="https://img-blog.csdnimg.cn/e723435337234b0883255de7316f0a82.png" alt="在这里插入图片描述"> Linux对应版本为 jdk-8u331-linux-x64.tar.gz <img src="https://img-blog.csdnimg.cn/568dc4cda69a49a99acdd394ec0edfdb.png" alt="在这里插入图片描述"> 上传到服务器后使用如下命令解压

```
tar -zxvf jdk-8u331-linux-x64.tar.gz
# 进入解压后目录，pwd获取路径
pwd
# 环境变量配置,输入如下命令后按i配置
vim /etc/profile

```

配置内容如下,替换’JAVA_HOME='内容为jdk解压后目录，不用到bin

```
export JAVA_HOME=/usr/local/jdk1.8.0_331
export PATH=$PATH:${JAVA_HOME}/bin:${CATALINA_HOME}/bin
export CLASSPATH=$CLASSPATH:${JAVA_HOME}/lib:${CATALINA_HOME}/lib

```

配置完成后，使用如下命令刷新配置。**如果需要切换用户，记得其他用户也执行这个命令**

```
source /etc/profile

```

#### 1.2.2、Tomcat

>  
 先安装jdk 


进入https://tomcat.apache.org/，选择需要版本 <img src="https://img-blog.csdnimg.cn/e1e9cae6bcaf40848aada2c6efd29c68.png" alt="在这里插入图片描述"> Linux对应版本为 xx.tar.gz <img src="https://img-blog.csdnimg.cn/6537d627dc0b472bad34a19b82c21dd3.png" alt="在这里插入图片描述"> 和刚才的jdk一样上传解压，加配置就好了

```
tar -zxvf
vim /etc/profile
source /etc/profile

```

```
export CATALINA_HOME=/usr/local/tomcat
export PATH=$PATH:${JAVA_HOME}/bin:${CATALINA_HOME}/bin
export CLASSPATH=$CLASSPATH:${JAVA_HOME}/lib:${CATALINA_HOME}/lib

```

### 1.3、JSPWiki 物料下载

进入 https://archive.apache.org/dist/jspwiki/2.11.2/binaries/webapp/， 或者https://jspwiki-wiki.apache.org/Wiki.jsp?page=Downloads

<img src="https://img-blog.csdnimg.cn/5964c9f94e224be6bc8765885333f830.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/531d466e49bf4bbab22b2fb610575f0d.png" alt="在这里插入图片描述"> **下载需要中文语言包与部署用JSPWiki.war包**
- war包路径
```
/jspwiki/2.11.2/binaries/webapp/JSPWiki.war

```
- 中文语言包路径
```
/jspwiki/2.11.2/wikipages/jspwiki-wikipages-zh_CN-2.11.2.zip 

```

### 1.4、JSPWiki安装
- 一些基础定义声明
```
appname:
你的war包名称，影响访问链接
http://.../warName

```
1. 上传文件 把war包放置在 tomcat安装目录/webapps下1. tomcat启动 进入tomcat bin目录下
```
# 启动tomcat服务
nohup ./startup.sh &amp;

```
1. 初次访问 访问http://myhost/appname/Install.jsp tomcat一般是
```
http://host:8080/xxxx

```
1. 初步配置 页面存储 VersioningFileProvider ，选择一个你的linux 目录 后续可以通过配置 jspwiki-custom.properties更改 <img src="https://img-blog.csdnimg.cn/a995cbd37b42403c8ca307ba8e42784b.png" alt="在这里插入图片描述"> 点击配置，会生成jspwiki.properties文件如下
```
jspwiki.basicAttachmentProvider.storageDir = /home/xxx/jsp_wiki/jspwiki-files
jspwiki.fileSystemProvider.pageDir = /home/xxx/jsp_wiki/jspwiki-files
jspwiki.applicationName = jspwiki
jspwiki.pageProvider = VersioningFileProvider
jspwiki.workDir =  /home/xxx/jsp_wiki/cache

```
1. 提前设置语言
>  
 记得先停掉tomcat，生成的配置文件jspwiki-custom.properties 在tomcat/temp下，别找jspwiki.properties了，根本没有 find / -name jspwiki.properties 


jspwiki.fileSystemProvider.pageDir，把语言包解压拷贝到此目录下

```
# 解压语言包
unzip xxx.zip

```

配置jspwiki-custom.properties （jspwiki-custom.properties 优先级&gt; jspwiki.properties）

```
# 支持更多的图片格式
jspwiki.translatorReader.inlinePattern.1 = *.jpg 
jspwiki.translatorReader.inlinePattern.2 = *.png
jspwiki.translatorReader.inlinePattern.3 = *.gif
# 支持中文搜索
jspwiki.encoding = UTF-8 
jspwiki.lucene.analyzer = org.apache.lucene.analysis.cjk.CJKAnalyzer 

```
1. 重启tomcat 到tomcat/bin目录下
```
./shutdown.sh
 nohup ./startup.sh &amp;

```

访问wiki，http://myhost/appname/，不可以的话myhost是“ip+port”

### 1.5、JSPWiki配置自定义
-  转移tomcat/temp下的 jspwiki-custom.properties 到tomcat/lib -  指定配置文件位置 jspwiki-custom.properties 在/WEB-INF/classes的web.xml 中 
```
&lt;context-param&gt;下添加
&lt;jspwiki.custom.config&gt;your path/jspwiki-custom.properties&lt;/jspwiki.custom.config&gt;

```

## 2、JSPWiki woc

JSPWiki默认模板是不能创建页面的，没有那个按钮。 另写一篇，记录使用模板配置与使用。
