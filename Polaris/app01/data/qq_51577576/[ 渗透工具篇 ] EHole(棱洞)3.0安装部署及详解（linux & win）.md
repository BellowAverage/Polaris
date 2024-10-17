
--- 
title:  [ 渗透工具篇 ] EHole(棱洞)3.0安装部署及详解（linux & win） 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - <ul><li>- - - <ul><li>- - - - - - - - 


## 一、介绍

### 1、EHole简介

>  
 EHole是一款对资产中重点系统指纹识别的工具，在红队作战中，信息收集是必不可少的环节，如何才能从大量的资产中提取有用的系统(如OA、vpn、Weblogic…)。 EHole旨在帮助红队人员在信息收集期间能够快速从C段、大量杂乱的资产中精准定位到易被攻击的系统，从而实施进一步攻击。 这款工具是棱角安全社区联合出品，配合其漏洞总结，这款工具是在平时渗透中无意发现的，效果非常好。 


### 2、项目地址

>  
 项目地址： 


```
https://github.com/EdgeSecurityTeam/Ehole

```

>  
 社区地址： 


```
https://forum.ywhack.com/bountytips.php?Vulnerability

```

>  
 该社区对常见web漏洞以及利用方法做了一个全面而详细的总结 


<img src="https://img-blog.csdnimg.cn/57345cb88ad242aebac59a0357d537df.png" alt="在这里插入图片描述">

## 二、下载go环境

>  
 需要使用go环境，我没有部署go环境，我先进行部署（我记得好像在使用go build他也会自动部署让你确认部署，我这里先进行部署了） 


## 三、部署Ehole

### 1、linux安装部署Ehole

#### 1.下载Ehole

```
https://github.com/EdgeSecurityTeam/EHole/releases

```

<img src="https://img-blog.csdnimg.cn/4f2e1284b61648029cd2fd6d1c96884a.png" alt="在这里插入图片描述">

>  
 我这里下载了linux版本，我在kali里面演示一下 


#### 2.迁移到kali虚拟机

>  
 我下载到了本机解压了，移到kali虚拟机 


<img src="https://img-blog.csdnimg.cn/33854fc3fa8545d18c453e357abc0941.png" alt="在这里插入图片描述">

>  
 如果你想在kali解压，解压命令 


```
unzip Ehole3.0-linux.zip -d EHole

```

>  
 -d参数把文件解压到指定的目录下，没有就新建 


<img src="https://img-blog.csdnimg.cn/31ad98e2cffa4ca4b7e94d8cadf58e34.png" alt="在这里插入图片描述">

#### 3.验证部署成功

>  
 进入Ehole3.0-linux目录 


<img src="https://img-blog.csdnimg.cn/f846d399e61a4ebcb35f81218672981f.png" alt="在这里插入图片描述">

>  
 执行如下命令，回显出帮助信息，则部署成功 


```
./Ehole3.0-linux -h

```

<img src="https://img-blog.csdnimg.cn/798cb07fbab24c60b7bf787f9c352cce.png" alt="在这里插入图片描述">

#### 2、windows安装部署Ehole

### 1.下载Ehole

```
https://github.com/EdgeSecurityTeam/EHole/releases

```

<img src="https://img-blog.csdnimg.cn/70e5b07d2e2d42e3bd27f3b1c7dc84b0.png" alt="在这里插入图片描述">

>  
 我这里下载了windows版本，我在本机演示一下 


### 2.解压Ehole文件

>  
 下载解压 


<img src="https://img-blog.csdnimg.cn/a20b1fdb84b140dfba8ec09275e5a19d.png" alt="在这里插入图片描述">

>  
 解压后的文件内容如下 


<img src="https://img-blog.csdnimg.cn/40223269104d480eb10926b3bcf4b9a7.png" alt="在这里插入图片描述">

### 3.验证部署成功

>  
 进入cmd 


<img src="https://img-blog.csdnimg.cn/881e4565b19e4790a723433d6b59ce9b.png" alt="在这里插入图片描述">

```
Ehole3.0-Win.exe -h

```

<img src="https://img-blog.csdnimg.cn/6319f199e0b9478ea5a0f39718d79754.png" alt="在这里插入图片描述">

## 四、使用

>  
 在红队场景下首先对多个目标进行了资产收集，如同时几千上万个IP，EHole(棱洞)可以快速的从这些资产中获取重要的系统或者直接能 RCE 的系统。 EHole(棱洞)提供了两种指纹识别方式，可从本地读取识别 也可以从FOFA进行批量调用API识别(需要FOFA密钥)，同时支持结果JSON格式输出。 


### 1、参数介绍

```
-h    			帮助
-u string			目标网址
-t string			线程（默认为“ 100”）
-l string			基于本地文件探测
-json string		输出 json
-f string			FOFA搜索资产，支持IP和IP段。（192.168.1.1 | 192.168.1.0/24）
-fall string		FOFA批处理搜索IP
-fofa string		FOFA搜索资产，支持所有FOFA搜索语法。
-ftime string		FOFA超时（默认为“ 10”）
-log string		日志文件名（默认“ server.log”）

```

### 2、本地识别：

>  
 URL地址需带上协议,每行一个 


```
Ehole3.0-Win.exe -l url.txt  

```

<img src="https://img-blog.csdnimg.cn/db9102d4ef464374b769586a300659ae.png" alt="在这里插入图片描述">

>  
 URL.txt文件格式： 


<img src="https://img-blog.csdnimg.cn/e796cebc1d6649a08e7929ca1e41686e.png" alt="在这里插入图片描述">

### 3、FOFA识别:

>  
 注意：从FOFA识别需要配置FOFA 密钥以及邮箱，在config.ini内配置好密钥以及邮箱即可使用。 进入fofa.info获取自己的Email和Fofa_token 写入配置文件 


<img src="https://img-blog.csdnimg.cn/4f29a374723447bfad57a9cb1ebfae4c.png" alt="在这里插入图片描述">

>  
 支持单IP或IP段 


```
Ehole3.0-Win.exe -f ip 
Ehole3.0-Win.exe -f ip段

```

### 4、结果输出：

>  
 结果输出至export.json文件 


```
Ehole3.0-Win.exe -l url.txt -json export.json

```

<img src="https://img-blog.csdnimg.cn/44185e082d9b42709da9f6c472102897.png" alt="在这里插入图片描述">

>  
 生成的export.json如下 


<img src="https://img-blog.csdnimg.cn/bc5485ddbec749b0b75cf5003bae5e7a.png" alt="在这里插入图片描述">

>  
 生成的export.json文件内容如下 


<img src="https://img-blog.csdnimg.cn/9ad94c72722e4e44ad7a3e6f7fc3726e.png" alt="在这里插入图片描述">

### 5、常用的几种扫描探测方法

>  
 url地址需要带上协议，每行一个，用于批量扫描 


```
Ehole3.0-Win.exe -l url.txt 

```

>  
 支持单ip扫描或者ip段扫描，支持fofa接口，但是需要配置fofa邮箱和密钥 


```
Ehole3.0-Win.exe -f 192.168.80.1/24 	 

```

>  
 结果输出到json文件中 


```
Ehole3.0-Win.exe -l url.txt -json test.json 	

```
