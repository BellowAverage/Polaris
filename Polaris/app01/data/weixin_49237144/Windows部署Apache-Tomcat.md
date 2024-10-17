
--- 
title:  Windows部署Apache-Tomcat 
tags: []
categories: [] 

---
### Windows独立部署Apache-Tomcat服务器



#### 文章目录
- <ul><li>- <ul><li>- - - - - - - 


#### 前言：

​ 1）这篇文档以在 Windows 系统中独立部署Apache-Tomcat 服务器为例，详细介绍独立部署的操作步骤。

​ 2）独立部署需要用户自行和 Web 应用服务器Apache-Tomcat 来配置部署的环境，再将 FineReport 的报表工程拷贝到 Web 应用服务器下。

#### 1. apache Tomcat 官网下载 Tomcat并解压缩

<th align="center">apache Tomcat官网：</th><th align="center">https://tomcat.apache.org/</th>
|------

<img src="https://img-blog.csdnimg.cn/4393dd5baf584c9486226d0f87ee542d.png#pic_center" alt="在这里插入图片描述">

#### 1.1下载 apache-tomcat 9.0.65

<th align="center">Tomcat 版本</th><th align="center">JDK 版本</th>
|------
<td align="center">推荐使用 Tomcat8.5.57 及以上版本，或者 Tomcat8 最新版本注：使用推荐版本可减少因 Tomcat 版本过低导致的安全问题。支持Tomcat7.0~9.0 版本不支持 Tomcat10.0 版本</td><td align="center">JDK 1.8 且小版本需在 JDK8u102 以上</td>

<img src="https://img-blog.csdnimg.cn/938a46ae4bc643f68ba8027b00fa20d1.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/9312cf60c8754e08b6328c5ee75b9d84.png#pic_center" alt="在这里插入图片描述">

#### 1.2 解压缩apache-tomcat 9.0.65

<img src="https://img-blog.csdnimg.cn/b38ecbe6574342b88708bdd1b062243e.png#pic_center" alt="在这里插入图片描述">

#### 2. 拷贝webroot 文件夹

将%FR_HOME%\webapps下的 webroot 文件夹拷贝到%Tomcat_HOME%\webapps下

<img src="https://img-blog.csdnimg.cn/d68c1c8d7c104d45993add015d582891.png#pic_center" alt="在这里插入图片描述">

注：报表工程名 webroot 可以自定义修改，但是需要注意的是后面访问决策系统时地址http:// ip地址:端口/工程名/decision中的工程名也要随之更改。

#### 2.1 拷贝 tools.jar

将%JAVA_HOME%\jdk\lib下的 tools.jar 拷贝到%Tomcat_HOME%\lib和%Tomcat_HOME%\webapps\webroot\WEB-INF\lib下

<img src="https://img-blog.csdnimg.cn/1627868f06904f3ba2896d737e3769f4.png#pic_center" alt="在这里插入图片描述">

#### 2.2 启动 Tomcat 服务器

压缩包安装的 Tomcat，执行%Tomcat_HOME%\bin下的 startup.bat 或 startup.sh 文件，启动 Tomcat 服务器。

以 Windows 系统为例，双击 startup.bat，启动 Tomcat 服务器。

<img src="https://img-blog.csdnimg.cn/81da1c95ea9847ea9255b6c2f5288528.png#pic_center" alt="在这里插入图片描述">

```
### 	2.3 访问Apache-Tomcat

```

<img src="https://img-blog.csdnimg.cn/61d2edd6cf8f4f8ab14692e6ceec0933.png#pic_center" alt="在这里插入图片描述">

#### 2.4 访问数据决策系统

访问数据决策系统也就是访问部署好的报表工程，在浏览器中输入访问地址http:// IP:端口号/工程名/decision，打开决策系统配置页面，即部署成功。

<img src="https://img-blog.csdnimg.cn/e79edc1344ba481cba0bc3ad19263337.png#pic_center" alt="在这里插入图片描述">
