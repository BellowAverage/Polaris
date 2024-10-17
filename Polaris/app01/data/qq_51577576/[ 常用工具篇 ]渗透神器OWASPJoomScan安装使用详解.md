
--- 
title:  [ 常用工具篇 ]渗透神器OWASPJoomScan安装使用详解 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - - - <ul><li>- - - - - <ul><li>- - - - 


## 一、Joomla简介

>  
 Joomla 是类似织梦、wp等流行的一款CMS软件，可以非常快速地发布一个精美的网站。在kali下如何检测Joomla是否存在可以利用的漏洞呢？如果您的网站正在运行 Joomla，您可以对您的网站使用 JoomScan 实用程序来发现漏洞或仅提供有助于攻击您网站的一般信息。一旦您意识到该网站的弱点，您就可以采取适当的措施来保护它。JoomScan 的工作原理与 WPScan 类似，后者用于扫描 WordPress 网站的漏洞。 


## 二、OWASPJoomScan

>  
 OWASPJoomla！漏洞扫描器（JoomScan）是一个开源项目，其主要目的是实现漏洞检测的自动化，以增强Joomla CMS开发的安全性。该工具基于Perl开发，能够轻松无缝地对各种Joomla项目进行漏洞扫描，其轻量化和模块化的架构能够保证扫描过程中不会留下过多的痕迹。它不仅能够检测已知漏洞，而且还能够检测到很多错误配置漏洞和管理权限漏洞等等。除此之外，OWASP JoomScan使用起来非常简单，不仅提供了非常友好的用户界面，而且还能够以HTML或文本格式导出扫描报告。 


## 三、JoomScan的优势

```
自动化
版本枚举
漏洞枚举（基于版本）
组件枚举（支持1209款热门组件）
组件漏洞枚举（基于版本，1030+漏洞利用）
防火墙检测
文本或HTML格式导出数据
查找常见日志文件
查找常见备份文件

```

## 四、JoomScan安装详解

### 1、更新apt

```
sudo apt update 

```

<img src="https://img-blog.csdnimg.cn/69ad258114e54a75acbe95bc79ef9497.png" alt="在这里插入图片描述">

### 2、安装joomscan

```
sudo apt install joomscan

```

<img src="https://img-blog.csdnimg.cn/284855368045454580eb0b4c2ac5cb72.png" alt="在这里插入图片描述">

### 3、验证安装成功

```
joomscan -h 

```

<img src="https://img-blog.csdnimg.cn/f6560d9d7c4d46bbbe9059e5384d7985.png" alt="在这里插入图片描述">

## 五、JoomScan使用详解

### 1、JoomScan参数介绍

```
Help :
Usage:  joomscan [options]

--url | -u &lt;URL&gt;                |   The Joomla URL/domain to scan.
--enumerate-components | -ec    |   Try to enumerate components.

--cookie &lt;String&gt;               |   Set cookie.
--user-agent | -a &lt;User-Agent&gt;  |   Use the specified User-Agent.
--random-agent | -r             |   Use a random User-Agent.
--timeout &lt;Time-Out&gt;            |   Set timeout.
--proxy=PROXY                   |   Use a proxy to connect to the target URL
           Proxy example: --proxy http://127.0.0.1:8080
                                  https://127.0.0.1:443
                                  socks://127.0.0.1:414
                                  
--about                         |   About Author
--help | -h                     |   This help screen.
--version                       |   Output the current version and exit.

```

<img src="https://img-blog.csdnimg.cn/e095a849829d40dd85a94a83ed9ea50f.png" alt="在这里插入图片描述">

### 2、OWASPJoomScan使用样例

#### 1.执行默认检测

>  
 使用该–url或者-u参数指定 Joomla 站点的 URL，以便使用 JoomScan 对其进行扫描 


```
joomscan --url http://192.168.233.187/
joomscan -u http://192.168.233.187/

```

<img src="https://img-blog.csdnimg.cn/50d62fd1f92b4b98a231c340edf032f6.png" alt="在这里插入图片描述">

#### 2.枚举已安装的组件

>  
 使用该-ec或者–enumerate-components枚举组件 


```
joomscan --url http://192.168.233.187/ --enumerate-components
joomscan -u http://192.168.233.187/ -ec

```

<img src="https://img-blog.csdnimg.cn/ecbebce6f81b46ce838a88a5da892161.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b2419210a17c4584a4f4eeb1339cb61e.png" alt="在这里插入图片描述">

#### 3.设置cookie

>  
 使用该–cookie参数指定cookie对站点进行扫描 


```
joomscan --url http://192.168.233.187/ --cookie "joomla_user_state=logged_in;"
joomscan -u http://192.168.233.187/ --cookie "joomla_user_state=logged_in;"

```

<img src="https://img-blog.csdnimg.cn/b860fdb1eef54eb3818070ecc4306bc5.png" alt="在这里插入图片描述">

#### 4.设置user-agent

>  
 使用该–user-agent参数指定user-agent对站点进行扫描 


```
joomscan --url http://192.168.233.187/ --user-agent "....."
joomscan -u http://192.168.233.187/ --user-agent "....."

```

#### 5.设置随机user-agent

>  
 使用该-r或者–random-agent参数指定user-agent对站点进行扫描 


```
joomscan -u http://192.168.233.187/ --random-agent
joomscan --url http://192.168.233.187/ -r

```

### 3、扫描结果说明：

```
[+] FireWall Detector ---- 防火墙探测器
[+] Detecting Joomla Version ---- 探测Joomla的版本
[+] Core Joomla Vulnerability ---- 核心Joomla的脆弱性
[+] Checking Directory Listing ---- 检查目录清单
[+] Checking apache info/status files ---- 检查apache info/status文件
[+] admin finder ---- 后台登录界面
[+] Checking robots.txt existing ---- 检查robots.txt文件是否存在
[+] Finding common backup files name ---- 查找常用备份文件名称
[+] Finding common log files name ---- 查找常用日志文件名称
[+] Checking sensitive config.php.x file ---- 查找敏感的config.php.x文件

```

## 六、joomla指纹

```
inurl: "index.php?option-com_users 
x-Content-Encoded-By: Joomla

```

## 七、相关资源

[ 1、OWASP文档 ](https://wiki.owasp.org/index.php/Category:OWASP_Joomla_Vulnerability_Scanner_Project） [2、Github项目地址 ](https://github.com/OWASP/joomscan）
