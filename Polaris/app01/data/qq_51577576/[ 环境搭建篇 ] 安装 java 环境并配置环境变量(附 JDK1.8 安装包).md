
--- 
title:  [ 环境搭建篇 ] 安装 java 环境并配置环境变量(附 JDK1.8 安装包) 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - <ul><li>- - - 


## 一、下载安装JDK

### 1、下载JDK

>  
 下载链接： 


```
https://pan.baidu.com/s/15PE5vikEHhma-2rEcjjSzA?pwd=zh57 

```

>  
 下载之后是一个jdk的exe程序 


<img src="https://img-blog.csdnimg.cn/9c6cad9da636408f8401f7875bd9921d.png" alt="在这里插入图片描述">

### 2、安装jdk

>  
 下载之后双击安装就OK了 双击打开exe文件开始安装，点击下一步 


<img src="https://img-blog.csdnimg.cn/e04767ae50f14322bc1033548e337b26.png" alt="在这里插入图片描述">

>  
 下一步 


<img src="https://img-blog.csdnimg.cn/34daa05154ea4f5aaec3da2a4b23314b.png" alt="在这里插入图片描述">

>  
 选择安装路径，我就默认了，直接下一步 


<img src="https://img-blog.csdnimg.cn/736ab7d7401044a8a12155397c8f540a.png" alt="在这里插入图片描述">

>  
 开始安装JDK了 


<img src="https://img-blog.csdnimg.cn/e2987067ab94471ea00a2dc687a4d05b.png" alt="在这里插入图片描述">

>  
 安装成功 


<img src="https://img-blog.csdnimg.cn/b66f5c859a2f438d9487cb7d40e7fd4d.png" alt="在这里插入图片描述">

## 二、环境变量配置流程

>  
 配置java环境变量的方法： 1、右键点击计算机，选择属性，点击高级系统设置，打开环境变量设置； 2、新建JAVA_HOME变量，并编辑Path变量； 3、新建Classpath变量并编辑即可。 


## 三、具体配置过程

### 1.JAVA_HOME变量设置

>  
 1、首先右击计算机进入属性然后选择其中的高级系统设置。 


<img src="https://img-blog.csdnimg.cn/094ac1b120ea46deabb25f050fe6acf9.png" alt="在这里插入图片描述">

>  
 2、点击进入高级中的环境变量，进入环境变量编辑界面。 


<img src="https://img-blog.csdnimg.cn/c70cfc8362af4b09a13becd11921f031.png" alt="在这里插入图片描述">

>  
 3、在下方的系统变量中，并不存在JAVA_HOME变量,那么我们需要点击新建 


<img src="https://img-blog.csdnimg.cn/0033ad638ecd417c8fc0be36ed3ff8d6.png" alt="在这里插入图片描述">

>  
 4、输入新编变量名和变量值 变量名输入：JAVA_HOME，输入jdk安装的绝对路径，点击确定 Jdk默认安装在C:\Program Files\Java路径下 


<img src="https://img-blog.csdnimg.cn/3d519defb0ed49c79a6888a767260ac5.png" alt="在这里插入图片描述">

### 2.Path变量设置

>  
 1、同样是在系统变量中我们可以看到path变量已经存在，那么我们只需要点击编辑，进入path变量的编辑 


<img src="https://img-blog.csdnimg.cn/f30e58c9511741a787557782484bbfa4.png" alt="在这里插入图片描述">

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


<img src="https://img-blog.csdnimg.cn/24c1a4e3c51342e8a1ce59879d3eba53.png" alt="在这里插入图片描述">

## 四、配置成功

>  
 打开cmd，然后在键入java及javac，出现如图所示信息，说明配置成功。 


<img src="https://img-blog.csdnimg.cn/10f7928eeaa5469f8d803d217689fb87.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d766b1243a21492bb90fecfc9005d1a9.png" alt="在这里插入图片描述">

## 五、相关资源


