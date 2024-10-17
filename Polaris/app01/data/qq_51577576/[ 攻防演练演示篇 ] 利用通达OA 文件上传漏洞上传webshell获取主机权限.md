
--- 
title:  [ 攻防演练演示篇 ] 利用通达OA 文件上传漏洞上传webshell获取主机权限 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ Vulhub是一个面向大众的开源漏洞靶场，无需docker知识，简单执行两条命令即可编译、运行一个完整的漏洞靶场镜像。旨在让漏洞复现变得更加简单，让安全研究者更加专注于漏洞原理本身。 




#### 文章目录
- - - - <ul><li>- - - - - - - 


## 一、前言

>  
 本次使用于帮客户搭建一个演示环境，用于给领导演示，这里我利用了通达OA11.6文件上传漏洞往靶机上上传了一个webshell，然后通过蚁剑去连接webshell从而获取主机权限 需要注意的是： 


```
1.靶机环境win10
2.通达OA版本11.6
3.攻击机需要有java
4.攻击机我这里利用的通达OA的一个综合利用工具TDOA_RCE.jar，当然使用其他的工具也是可以的

```

## 二、演示环境搭建

### 1、靶机部署通达OA11.6

>  
 下载连接在文末给出 双击TDOA11.6.exe安装程序进行安装 


<img src="https://img-blog.csdnimg.cn/b014a1894eef43f9a14f6f90700cb21d.png" alt="在这里插入图片描述">

>  
 进入安装界面 


<img src="https://img-blog.csdnimg.cn/df7fc03df1af48e6bd7b0969359f6c94.png" alt="在这里插入图片描述">

>  
 选择安装路径 


<img src="https://img-blog.csdnimg.cn/1da49e4b87b746db8091a087ab8a66cc.png" alt="在这里插入图片描述">

>  
 开始安装 


<img src="https://img-blog.csdnimg.cn/c18921478a5647cf94a31c9278d94f75.png" alt="在这里插入图片描述">

>  
 一直默认安装就OK了。 安装完成之后访问http://127.0.0.1验证安装成功 


```
http://127.0.0.1

```

<img src="https://img-blog.csdnimg.cn/9d3c17adcb8842f99158e483eed696bf.png" alt="在这里插入图片描述">

### 2、攻击机部署蚁剑

>  
 所需文件在文末下载 


```
https://blog.csdn.net/qq_51577576/article/details/126912450

```

### 3、攻击机部署java环境

>  
 安装包可在文末下载连接中下载 


```
https://blog.csdn.net/qq_51577576/article/details/128667162

```

## 三、红方操作

### 1、上传webshell

>  
 直接打开通达OA综合利用工具TDOA_RCE.exe，工具下载链接在文末给出 


<img src="https://img-blog.csdnimg.cn/2e3c167c25ea4d9da324eb86b2ae0c1f.png" alt="在这里插入图片描述">

>  
 填入url地址，点击右侧的获取cookie 


```
http://靶机IP

```

<img src="https://img-blog.csdnimg.cn/847c551d06434ddba67ad56a942eec3e.png" alt="在这里插入图片描述">

>  
 自动填充cookie值，然后选择后台上传getshell，点击一键利用，他会上传一个webshell。 Cookie可以自动获取，万一没有获取到可以自行访问获取。 


<img src="https://img-blog.csdnimg.cn/c9ec77afd2064cb0812584317dabe3c9.png" alt="在这里插入图片描述">

>  
 浏览器访问webshell，证明确实上传成功 


```
http://ip/后门名称

```

<img src="https://img-blog.csdnimg.cn/00c0ebdb705248d39e46cedcbf22fd5d.png" alt="在这里插入图片描述">

### 2、连接webshell

>  
 打开蚁剑，蚁剑安装部署在第二部分已经说明 右键添加数据，填入webshell地址和webshell连接密码，测试链接，发现连接成功 


<img src="https://img-blog.csdnimg.cn/315b241f4d16402c8b2884e19edef32c.png" alt="在这里插入图片描述">

>  
 点击左上角的添加数据 数据添加成功，我们可以进行任意操作，这里我简单访问一下文件系统 


<img src="https://img-blog.csdnimg.cn/5657d358337d4ab59d53a22635f1653e.png" alt="在这里插入图片描述">

## 四、蓝方操作

### 1、检查后门情况

>  
 运维安全人员使用火绒对网站根目录进行扫描，目的是检查有没有后门程序 


<img src="https://img-blog.csdnimg.cn/f97e07af1cbb4e2ba36f33209be1ef1b.png" alt="在这里插入图片描述">

>  
 点击病毒查杀 


<img src="https://img-blog.csdnimg.cn/d2c1c1dc4f184937b8fa12029bccfe6d.png" alt="在这里插入图片描述">

>  
 自定义查杀 


<img src="https://img-blog.csdnimg.cn/43f40fe3a92b408282f0e64e19eb5b0e.png" alt="在这里插入图片描述">

>  
 查杀TDOA网站根目录 


```
D:\MYOA\webroot

```

<img src="https://img-blog.csdnimg.cn/ef330d8509504b2eab55e5e761ed3cc0.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/0566447e1c90465384da528974d6b054.png" alt="在这里插入图片描述">

>  
 删除后门文件 


<img src="https://img-blog.csdnimg.cn/7f65619d86114078bdf58b4030d98be3.png" alt="在这里插入图片描述">

>  
 彻底删除所有扫到的后门文件 <img src="https://img-blog.csdnimg.cn/5aef87cb78a94c29a10e8633cbd8aae5.png" alt="在这里插入图片描述"> 


### 2、效果

>  
 安全运维人员使用火绒进行查杀，发现存在后门文件，并进行删除，导致攻击者无法进行持续攻击 


### 3、根治

>  
 由于在通达OAweb根目录下发现了后门文件，工作人员首先对通达OA漏洞情况进行自建，最终发现该版本存在高危漏洞并对其进行升级，从而根治了该漏洞。 


## 五、相关资源


