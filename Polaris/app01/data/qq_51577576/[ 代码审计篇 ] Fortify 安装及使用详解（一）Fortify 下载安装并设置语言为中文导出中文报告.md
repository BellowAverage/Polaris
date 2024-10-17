
--- 
title:  [ 代码审计篇 ] Fortify 安装及使用详解（一）Fortify 下载安装并设置语言为中文导出中文报告 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - <ul><li>- - - - - - - - - - - - - - - - - - - - - - <ul><li>- - - - - - - - - - - - 


## 一、Fortify介绍

### 1、Fortify简介

>  
 Fortify 是一个静态的、白盒的软件源代码安全测试工具。它通过内置的五大主要分析引擎：数据流、语义、结构、控制流、配置流等对应用软件的源代码进行静态的分析，通过与软件安全漏洞规则集进行匹配、查找，从而将源代码中存在的安全漏洞扫描出来，并可导出报告。扫描的结果中包括详细的安全漏洞信息、相关的安全知识、修复意见。 


### 2、Fortify原理

>  
 首先通过调用语言的编译器或者解释器把前端的语言代码（如JAVA，C/C++源代码）转换成一种中间媒体文件NST（Normal Syntax Tree），将其源代码之间的调用关系，执行环境，上下文等分析清楚。 通过分析不同类型问题的静态分析引擎分析NST文件，同时匹配所有规则库中的漏洞特征，将漏洞抓取出来，然后形成包含详细漏洞信息的FPR结果文件，用AWB打开查看。 


### 3、Fortify SCA引擎介绍：

>  
 数据量引擎：跟踪、记录并分析程序中的数据传递过程所产生的安全问题。 语义引擎：分析过程中不安全的函数，方法的使用的安全问题。 结构引擎：分析程序上下文环境、结构中的安全问题。 控制流引擎：分析程序特定时间、状态下执行操作指令的安全问题。 配置引擎：分析项目配置中的敏感信息和配置确实的安全问题。 


### 4、Fortify支持语言

>  
 FortifySCA支持的21语言，分别是： 


```
1、asp.net
2、VB.Net
3、c#.Net
4、ASP
5、VBscript
6、VS6
7、java
8、JSP
9、javascript
10、HTML
11、XML
12、C/C++
13、PHP
14、T-SQL
15、PL/SQL
16、Action script
17、Object-C (iphone-2012/5)
18、ColdFusion5.0 - 选购
19、python -选购
20、COBOL - 选购
21、SAP-ABAP -选购

```

## 二、Fortify下载

>  
 CSDN有积分的小伙伴可以在CSDN直接下载，方便快捷，还能给我加几个积分，哈哈哈 CSDN下载链接： 


```
https://download.csdn.net/download/qq_51577576/87341637

```

>  
 把百度网盘链接删除之后就提示不限流了 。。。。。。文章质量就提高了 ？？？？？？ 


>  
 这里是我添加了两个链接，其中有一个是我自己百度网盘分享的，一个是我传到CSDN的，提示文章质量低下，然后我删了百度网盘分享链接。。。。。。 为了照顾到CSDN没有积分的小伙伴们，我最终还是把百度网盘的链接加上来了 




<img src="https://img-blog.csdnimg.cn/aeb6bec93d0e45fda0d296ba627a23cb.png" alt="在这里插入图片描述">

>  
 把百度网盘链接删除之后就提示不限流了 。。。。。。文章质量就提高了 ？？？？？？ 


<img src="https://img-blog.csdnimg.cn/3558a6382d2f4880be68930648118258.png" alt="在这里插入图片描述">

## 三、Fortify安装

### 1、双击exe文件

<img src="https://img-blog.csdnimg.cn/1d151c77aeef4d3e8a58a613a3cebde8.png" alt="在这里插入图片描述">

### 2、点击next

<img src="https://img-blog.csdnimg.cn/1cb8b397d72347beb6f5f629cd860d85.png" alt="在这里插入图片描述">

### 3、同意协议，点击下一步

<img src="https://img-blog.csdnimg.cn/90bfca58065f452695c5551116523f8a.png" alt="在这里插入图片描述">

### 4、选择安装路径、点击下一步

<img src="https://img-blog.csdnimg.cn/f962e53a16f74b5a9645ea9921dabba8.png" alt="在这里插入图片描述">

### 5、选择组件、点击下一步

<img src="https://img-blog.csdnimg.cn/b7f42c4ce0de45f5ac6b299be12c7129.png" alt="在这里插入图片描述">

### 6、选择license、点击下一步

>  
 License在下载文件里面有 


<img src="https://img-blog.csdnimg.cn/59284b799dbe4e6aa6eb2d4acc00730e.png" alt="在这里插入图片描述">

### 7、选择更新服务器，这里可以不用填写

<img src="https://img-blog.csdnimg.cn/bbdb7f104a5548d49b9c448e0895b668.png" alt="在这里插入图片描述">

### 8、移除之前版本选择No

<img src="https://img-blog.csdnimg.cn/19a3231e7c88462884451cd9803557d4.png" alt="在这里插入图片描述">

### 9、安装实例代码项目选择No

<img src="https://img-blog.csdnimg.cn/5ec36e8ee4d94370912f248a6a5dbe75.png" alt="在这里插入图片描述">

### 10、准备安装、点击下一步

<img src="https://img-blog.csdnimg.cn/1a80ea651f644d7494a07aafd3e838e3.png" alt="在这里插入图片描述">

### 11、等待安装中

<img src="https://img-blog.csdnimg.cn/e39f55128dc043f1851529dfa28da7cb.png" alt="在这里插入图片描述">

### 12、安装完成、点击Finish及完成安装

>  
 记得把自动更新取消，我们后续会设置中文 


<img src="https://img-blog.csdnimg.cn/9d68ee8366374e60b7351e2a0a790145.png" alt="在这里插入图片描述">

### 13、替换jar包

>  
 fortify安装：安装好之后，将下载的fortify-common-20.1.1.0007.jar包替换掉fortify安装目录下的Core\lib目录下的同名包 


<img src="https://img-blog.csdnimg.cn/31793d6282b345ad81afdd3364404f89.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/6d2fa9cf777f40838ebfaa83284e5386.png" alt="在这里插入图片描述">

### 14、添加rules和ExternalMetadata

>  
 将规则包rules，将文件放入\Core\config\目录下； 


<img src="https://img-blog.csdnimg.cn/000fff855470455aaa8918d6c0807007.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e23286a364a74f8cac807d8261e495f9.png" alt="在这里插入图片描述">

### 15、运行fortify

<img src="https://img-blog.csdnimg.cn/c09b0fb846ab4f5d9f5571fb9b470f92.png" alt="在这里插入图片描述">

### 16、提示是否更新规则，我们选No

>  
 这里我直接截图标注标注反了 


<img src="https://img-blog.csdnimg.cn/ef4d6c95c5784ab8afc5bd841ce5427e.png" alt="在这里插入图片描述">

### 17、打开后界面如下

<img src="https://img-blog.csdnimg.cn/d02d5dde54a5417089e7bc2479e2f235.png" alt="在这里插入图片描述">

## 四、修改语言为中文

>  
 其实上面完成就已经是中文了，关键在于第十六步，一定要选择NO，不能让他自动更新规则。 那么如果不是中文如何改成中文呢，有两种方式。 


### 1、运行scapostinstall.cmd修改为中文

#### 1. 运行scapostinstall.cmd

>  
 安装路径\Fortify\Fortify_SCA_and_Apps_20.1.1\bin 


<img src="https://img-blog.csdnimg.cn/3edf8e475ed746bd94e9fabca73511a1.png" alt="在这里插入图片描述">

#### 2. 选择设置

>  
 我们直接输入2就行 


```
[1] Migration...
[2] Settings...
[s] Display all settings
[q] Exit
Please select the desired action (1,2,s,q): 2

```

<img src="https://img-blog.csdnimg.cn/121444d4fe7149249763992d5363e48a.png" alt="在这里插入图片描述">

#### 3. 选择常规设置

>  
 直接输入1就可以了 


<img src="https://img-blog.csdnimg.cn/dba5e30df4494ca0997dd04831e01de6.png" alt="在这里插入图片描述">

#### 4. 选择本地的

>  
 直接输入1就可以了 


<img src="https://img-blog.csdnimg.cn/96b2bab6541247ec87ceb8cee89acb5e.png" alt="在这里插入图片描述">

#### 5. 选择中文

>  
 输入zh_CN按回车就ok了 


<img src="https://img-blog.csdnimg.cn/ac93440a7d6a490c9f4ecb4cd90f86ba.png" alt="在这里插入图片描述">

#### 6. 退出设置面板

>  
 直接键入q退出就ok了 


<img src="https://img-blog.csdnimg.cn/eef2d5288f27482fab47a60cb66dacca.png" alt="在这里插入图片描述">

### 2、直接再fortify前端面板修改设置

#### 1. 进入选项

>  
 重启fortify，选择菜单栏的options，接着选择options 


<img src="https://img-blog.csdnimg.cn/8d583a39ab1f4cc49718e75d0b4f3aea.png" alt="在这里插入图片描述">

#### 2. 选择语种

>  
 根据如图选择，然后点击ok就设置完成了 


<img src="https://img-blog.csdnimg.cn/25752cbe4224426993092b8b14199e82.png" alt="在这里插入图片描述">

## 五、Fortify简单扫描并导出报告

### 1、打开工作台

<img src="https://img-blog.csdnimg.cn/cf4a987659104680b7ae75a31828f79a.png" alt="在这里插入图片描述">

### 2、选择静态代码所在目录，进行扫描

>  
 我这里选择高级，让他自动识别 


<img src="https://img-blog.csdnimg.cn/708f00616a62457396a4ef418218a453.png" alt="在这里插入图片描述">

>  
 点击之后，跳转到文件目录，我们选择一个demo 


<img src="https://img-blog.csdnimg.cn/25974875350448a7a7af71b2d50685a7.png" alt="在这里插入图片描述">

>  
 确认信息，下一步 


<img src="https://img-blog.csdnimg.cn/81a6cf9ffafb4a0eaa7c23cc5666ca96.png" alt="在这里插入图片描述">

>  
 scan 


<img src="https://img-blog.csdnimg.cn/cb12bd685a994416a251f7c1c771c437.png" alt="在这里插入图片描述">

### 3、扫描完成

<img src="https://img-blog.csdnimg.cn/260e18c5911b4e8f81a6bcca51b3f033.png" alt="在这里插入图片描述">

>  
 查看扫描结果详细信息 


<img src="https://img-blog.csdnimg.cn/22faa2f904114fb7beaedc4cfe2f6eee.png" alt="在这里插入图片描述">

### 4、导出报告

>  
 我们设置了中文语言之后导出的报告就是中文报告。 


<img src="https://img-blog.csdnimg.cn/8cbbf0f9630548039dba78ee12818236.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/e09a7186abe7417ab978048495cdf5c0.png" alt="在这里插入图片描述">

>  
 导出成功 


<img src="https://img-blog.csdnimg.cn/3aa950c1d5aa434eb9e887ecc03f4225.png" alt="在这里插入图片描述">

### 5、查阅报告

>  
 这是我刚刚下载的PDF 


<img src="https://img-blog.csdnimg.cn/ac7a5c43dcc342b5b247f03cc0b7d219.png" alt="在这里插入图片描述">

>  
 打开发现是中文的，非常nice 


<img src="https://img-blog.csdnimg.cn/735f7aa710ff4e7ebd3fc6af36acea85.png" alt="在这里插入图片描述">

## 六、相关资源


