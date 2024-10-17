
--- 
title:  IDEA与Maven的下载安装教程 
tags: []
categories: [] 

---
**目录**











## 一、下载IDEA

进入官网：

选择电脑对应的系统，点击社区版本下的download按钮。 

<img alt="" height="996" src="https://img-blog.csdnimg.cn/4ed3719f56a14f8a845b0c417fae9947.png" width="1200"> 点击运行exe文件

<img alt="" height="744" src="https://img-blog.csdnimg.cn/bd7b026d5c6347db87cd040d2304601f.png" width="997">

自定义下载路径

<img alt="" height="744" src="https://img-blog.csdnimg.cn/7debd3a832f6475a87f304018553cbd8.png" width="997">

按照个人需要进行勾选

<img alt="" height="744" src="https://img-blog.csdnimg.cn/82ef35dec60d4ccb8ca41bb685464672.png" width="997">

 点击安装

<img alt="" height="744" src="https://img-blog.csdnimg.cn/c39d9469aa4a4711bf0825eb775c305c.png" width="997">

<img alt="" height="744" src="https://img-blog.csdnimg.cn/0f4efa8687914900b088110953c7e89d.png" width="997">

 完成

<img alt="" height="744" src="https://img-blog.csdnimg.cn/c5cdadac127b413a91532800dd75f451.png" width="997">

## 二、下载Maven

下载地址： 

注意：maven的安装需要依赖jdk的安装，所以必须先安装完成jdk且配置好jdk环境变量后在进行maven的安装！！

<img alt="" height="1171" src="https://img-blog.csdnimg.cn/4778846464764c89bd35745eb59d6339.png" width="1200"> 下载好后进行解压缩即可。

<img alt="" height="1005" src="https://img-blog.csdnimg.cn/521e2727d4514070ae4a00e68924bc9b.png" width="1200">

##  三、maven的环境变量配置

打开环境变量

<img alt="" height="1104" src="https://img-blog.csdnimg.cn/2f788389fc454b2083b5dedca869f6a9.png" width="978">

在“环境变量”界面中，分为上下两部分，上面部分是“某某某的用户变量”的设置，针对的是当前你登录电脑的账户；下面部分是系统变量的设置，针对的是这台电脑，相当于是所有账户。对于自己使用的电脑来说，建议直接在下面部分的“系统变量”中来配置。下面来以系统变量为例讲解：

** a、在系统变量中新建一个MAVEN_HOME变量，设置变量名跟变量值**

 MAVEN_HOME这个变量里面存放maven相关的路径配置

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/7abe5614877f473790c55724e301a099.png" width="1200">

**b、将MAVEN_HOME配置到系统环境变量path中**

 双击path变量，新建一参数，输入%MAVEN_HOME%\bin后点击确定即可。

<img alt="" height="335" src="https://img-blog.csdnimg.cn/82f877b714f94b3f9cb2e8a30ac586e4.png" width="1200">

 环境变量path的作用：提供windows命令行中指令的可执行文件路径，当我们在命令行中键入指令时，根据环境变量中的path值，找到对应的指令可执行文件进行执行。简单的说就是配置在path中的目录参数，在命令行中的任何目录下都可以使用。

完成以上操作后点击确定保存并关闭配置界面。

**在cmd窗口中键入mvn -aversion后回车，如果出现下面的版本号，及说明maven安装成功。**

<img alt="" height="256" src="https://img-blog.csdnimg.cn/17e3d8ee5c5d4ca2aa79f5db1ae390f5.png" width="1200">

## 四、maven的setting文件配置

**a.本地仓库的配置**

在D盘中创建一个文件夹，取名maven_repository

打开maven的安装目录，选择conf文件夹中的setting.xml文件

<img alt="" height="348" src="https://img-blog.csdnimg.cn/8555a98ba5b14753aa00bf8d0ef64eea.png" width="1200">

 检验下是否已经设置成功 ​​​​​​，保存后控制台输入：

```
 mvn help:system
```

  再打开刚刚创建的文件夹，如果里面生成文件，即说明修改成功。<img alt="" height="208" src="https://img-blog.csdnimg.cn/21c9ccf6d4f04b328885464cf5b11918.png" width="1200">

** b.修改Maven的下载镜像地址为阿里源**

 安装好Maven时，要及时的修改Maven下载的镜像地址，最好改为国内的下载镜像，例如阿里云中央仓库，华为云中央仓库。

同样打开conf文件夹中的setting.xml文件，找到&lt;/mirrors&gt;，在&lt;/&gt;上一行中加入下面这段代码即可.

```
&lt;mirror&gt;
      &lt;id&gt;alimaven&lt;/id&gt;
      &lt;name&gt;aliyun maven&lt;/name&gt;
      &lt;url&gt;http://maven.aliyun.com/nexus/content/groups/public/&lt;/url&gt;
      &lt;mirrorOf&gt;central&lt;/mirrorOf&gt;        
&lt;/mirror&gt;
```

<img alt="" height="1062" src="https://img-blog.csdnimg.cn/41f09150c27d4438bd6c0148155183f8.png" width="1200">

##  五、在Idea上配置Maven工具

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/8cf73455ac614d1a947788efa0aa75ed.png" width="1200">


