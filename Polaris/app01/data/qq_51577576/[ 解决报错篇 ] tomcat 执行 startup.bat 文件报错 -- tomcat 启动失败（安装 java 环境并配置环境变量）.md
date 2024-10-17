
--- 
title:  [ 解决报错篇 ] tomcat 执行 startup.bat 文件报错 -- tomcat 启动失败（安装 java 环境并配置环境变量） 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - - - <ul><li>- - - <ul><li>- - - - - 


## 一、前言

>  
 今天搭建靶场环境碰到一个报错，这里分享解决报错的过程 


```
Neither the JAVA_HOME nor the JRE_HOME environment variable is defined  At least one of these environment variable is needed to run this program

```

## 二、发现报错

>  
 直接执行startup.bat启动tomcat 


<img src="https://img-blog.csdnimg.cn/5a2e7ae35ffa4925aed6fa051b253c15.png" alt="在这里插入图片描述">

>  
 双击打开，运行窗口一闪而过，tomcat并没有起来 


<img src="https://img-blog.csdnimg.cn/7cb2178500914355b0b928b01ecb8f45.png" alt="在这里插入图片描述">

>  
 在cmd窗口使用 startup 命令启动Tomcat时，执行startup.bat，看到报错信息，这里的意思大致就是找不到java环境 


```
Neither the JAVA_HOME nor the JRE_HOME environment variable is defined  At least one of these environment variable is needed to run this program

```

<img src="https://img-blog.csdnimg.cn/dbc6cae1001f49cfb03a4c0df83400d8.png" alt="在这里插入图片描述">

## 三、分析报错

```
Neither the JAVA_HOME nor the JRE_HOME environment variable is defined  
At least one of these environment variable is needed to run this program

```

>  
 简单翻译一下报错，Java_HOME和JRE_HOME环境变量都没有定义，运行此程序至少需要其中一个环境变量。通过报错信息我们知道是由于找不到Java环境导致的报错，我们就能想到以下的思路。 1.看有没有java环境 2.有没有配置环境变量 下面我们就一步步来解决，我这里安装了jdk，存在Java环境，那就是我环境变量出了问题。 


## 四、解决办法1：

### 1、下载安装JDK

>  
 在系统环境变量中添加 JAVA_HOME 环境变量，变量的值为 JDK的安装目录。 没有java环境可以安装JDK,下载链接： 


```
https://pan.baidu.com/s/15PE5vikEHhma-2rEcjjSzA?pwd=zh57 

```

>  
 下载之后双击安装就OK了，由于我之间搭建靶场环境之前就安装了JDK，我这里就不演示安装过程了 


### 2、环境变量配置流程

>  
 配置java环境变量的方法： 


```
1、右键点击计算机，选择属性，点击高级系统设置，打开环境变量设置；
2、新建JAVA_HOME变量，并编辑Path变量；
3、新建Classpath变量并编辑即可。

```

### 3、具体配置过程

#### 1.JAVA_HOME变量设置

>  
 1、首先右击计算机进入属性然后选择其中的高级系统设置。 


<img src="https://img-blog.csdnimg.cn/94b9cbf71fa3402eb3fa5acc8d4a3aa5.png" alt="在这里插入图片描述">

>  
 2、点击进入高级中的环境变量，进入环境变量编辑界面。 


<img src="https://img-blog.csdnimg.cn/9ebf5ced1a014ded8fe37bc43c4fc30c.png" alt="在这里插入图片描述">

>  
 3、在下方的系统变量中，并不存在JAVA_HOME变量,那么我们需要点击新建 


<img src="https://img-blog.csdnimg.cn/3b77bfe84dd44c10b72217b41d65e46f.png" alt="在这里插入图片描述">

>  
 4、输入新编变量名和变量值 变量名输入：JAVA_HOME，输入jdk安装的绝对路径，点击确定 Jdk默认安装在C:\Program Files\Java路径下 


<img src="https://img-blog.csdnimg.cn/1406ad064d16464ea6e149bcfe99d91c.png" alt="在这里插入图片描述">

#### 2.Path变量设置

>  
 1、同样是在系统变量中我们可以看到path变量已经存在，那么我们只需要点击编辑，进入path变量的编辑 


<img src="https://img-blog.csdnimg.cn/a87526ff86fe44ddb190b88a9af8040c.png" alt="在这里插入图片描述">

>  
 2、在path路径下添加jdk的bin目录和jre的bin目录 


>  
 在path路径下添加两个变量值，jdk的bin目录和jre的bin目录，Java的绝对路径我们之前已经赋值给了JAVA_HOME，我们只需要用JAVA_HOME代替绝对路径即可。 当然这里也可以直接添加jdk的jre的bin目录的绝对路径 


```
%JAVA_HOME%\bin
%JAVA_HOME%\jre\bin

```

>  
 最后点击确定。 


<img src="https://img-blog.csdnimg.cn/06b5305ca0b34f88b5eba15e3778d92b.png" alt="在这里插入图片描述">

### 4、问题解决

>  
 直接双击tomcat的bin目录下的startup.bat文件（起不来记得管理员身份执行，第一次好像需要管理员身份） 


>  
 也可以使用cmd窗口运行 


>  
 也是可以起来的 


## 五、解决方法2：

### 1、简单分析

>  
 如果不方便设置环境变量，可以在setclasspath.bat 文件的开头声明JAVA_HOME环境变量。 因为启动Tomcat实际上是运行了startup.bat文件，而 startup.bat 文件中调用了catalina.bat 文件，在catalina.bat 文件中则又调用了setclasspath.bat 文件，所以，可以通过在setclasspath.bat 文件的开头声明JAVA_HOME环境变量来解决问题。 


### 2、编辑setclasspath.bat

### 3、声明JAVA_HOME环境变量

```
set JAVA_HOME= JDK安装路径，路径不需要用双引号包含
set JRE_HOME= jre文件夹路径，路径不需要用双引号包含

```

### 4、问题解决

>  
 声明JAVA_HOME环境变量，tomcat同样可以起来，直接双击tomcat的bin目录下的startup.bat文件（起不来记得管理员身份执行，第一次好像需要管理员身份） 


## 六、相关资源


