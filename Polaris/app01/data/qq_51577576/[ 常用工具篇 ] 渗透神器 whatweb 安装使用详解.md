
--- 
title:  [ 常用工具篇 ] 渗透神器 whatweb 安装使用详解 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - <ul><li>- - - - - <ul><li>- - - - - - - - - - - 


## 一、whatweb简介

>  
 whatweb 一款网站指纹识别工具，使用Ruby语言开发。 whatweb能够识别各种关于网站的详细信息包括：CMS类型、博客平台、中间件、web框架模块、网站服务器、脚本类型、JavaScript库、IP、cookie等等。WhatWeb还标识版本号，电子邮件地址，账户ID，Web框架模块，SQL错误等。 WhatWeb可以隐秘、快速、彻底或缓慢扫描。 WhatWeb支持攻击级别来控制速度和可靠性之间的权衡。当在浏览器中访问网站时，该交易包含许多关于Web技术为该网站提供支持的提示。有时，单个网页访问包含足够的信息来识别网站，但如果没有，WhatWeb可以进一步询问网站。默认的攻击级别称为“被动”，速度最快，只需要一个网站的HTTP请求。这适用于扫描公共网站。在渗透测试中开发了更积极的模式。 


## 二、whatweb安装

>  
 Whatweb是基于ruby语言开发，因此可以安装在具备ruby环境的系统中，目前支持Windows/Max OSX/Linux。 


### 1、kali

>  
 在kali中已经机场whatweb，我这里演示使用的是kali自带的wahtweb。 如果kali没有就使用apt-get install whatweb 安装 kali是基于debian的 


### 2、debian/ubtuntu系统安装

>  
 debian/ubtuntu系统下 


```
apt-get install whatweb 

```

### 3、redhat/centos系统安装

>  
 redhat/centos系统下 


```
yum update
yum install ruby ruby-devel rubygems
wget http://www.morningstarsecurity.com/downloads/whatweb-0.4.7.tar.gz
tar xzvf whatweb-0.4.7.tar.gz
cd whatweb-0.4.7
./whatweb url

```

## 三、whatweb特性

```
拥有超过1700+个插件
若网站返回302，会跳转到重定向的网站
可以根据服务器返回的响应头确定网站使用的服务器类型，web中间件类型，cookie信息
可以从网站的源代码中确定网站使用了哪些JavaScript库
可以通过页面hash，path等确定网站使用的cms版本
查询网站ip及所属国家
多种日志格式：XML，JSON，MagicTree，RubyObject，MongoDB
可定制化HTTP头
可进行基础的认证设置
支持批量扫描网站

```

## 四、whatweb使用

>  
 命令语法： 


```
Usage: whatweb [options] &lt;URLs&gt;

```

### 1、whatweb参数介绍

>  
 常用参数如下： 


```
-h 查看帮助信息
--version 查看版本信息
-i 指定要扫描的文件
-v 详细显示扫描的结果
-a 指定运行级别

```

>  
 所有参数： 使用添加whatweb -h查看所有参数 


```
whatweb -h

```

<img src="https://img-blog.csdnimg.cn/05684a3d23064a4d9e7852e7214c7ca5.png" alt="在这里插入图片描述">

### 2、whatweb用法介绍

#### 1.查看版本信息

```
whatweb --version

```

<img src="https://img-blog.csdnimg.cn/f8dca6a5da89400bb09571a6e8b3aac1.png" alt="在这里插入图片描述">

#### 2.查看帮助信息

```
whatweb -h

```

<img src="https://img-blog.csdnimg.cn/3d24e8311ecd4515975a1e0f2e514095.png" alt="在这里插入图片描述">

#### 3.常规扫描

```
whatweb url

```

<img src="https://img-blog.csdnimg.cn/02f6cd8918ed4025ada5e9cba22b58cb.png" alt="在这里插入图片描述">

#### 4.批量扫描

>  
 将url全部写入一个txt中，然后使用-i参数指定文件就可以了 


<img src="https://img-blog.csdnimg.cn/7d97cec9b43a4c0ea29eca1e14609f46.png" alt="在这里插入图片描述">

```
whatweb -i url.txt

```

<img src="https://img-blog.csdnimg.cn/4789891acb3a477d9280d46b64f49226.png" alt="在这里插入图片描述">

#### 5.扫描结果显示详细内容

>  
 使用-v参数就可以了，nmap查看详细信息也是-v 


```
whatweb -v http://192.168.233.181

```

<img src="https://img-blog.csdnimg.cn/b34661fe03c94bf9a5b30dd2a03db281.png" alt="在这里插入图片描述">

#### 6.设置扫描强度

>  
 whatweb有一个-aggression（简写为-a）参数，此参数后边可以跟数字1-4，分别对应4个不同的等级。 


```
1、tealthy 每个目标发送一次http请求，并且会跟随重定向
2、unused 不可用
3、aggressive 每个目标发送少量的http请求，这些请求时根据参数为1时结果确定的
4、heavy 每个目标会发送大量的http请求，会去尝试每一个插件

```

>  
 举例：可配合-v，-i一起使用 


```
whatweb -a 1 http://192.168.233.181
whatweb -a 3 -v http://192.168.233.181
whatweb -a 4 http://192.168.233.181
whatweb -a 1 -v -i url.txt

```

<img src="https://img-blog.csdnimg.cn/11561ea21fde4548978c91315abf3154.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/8f943573c9664242b75d8b048703f6c1.png" alt="在这里插入图片描述">

#### 7.扫描网段

>  
 扫描单网段 


```
whatweb --no-errors -t 255 192.233.0.0/24    

```

>  
 可结合-a -v -i一起使用 


<img src="https://img-blog.csdnimg.cn/07d535121af34d48ae363932569fa4da.png" alt="在这里插入图片描述">

#### 8.导出扫描结果

>  
 导出文件格式： 


```
--log-brief=FILE            简单的记录，每个网站只记录一条返回信息
--log-verbose=FILE            详细输出
--log-xml=FILE            返回xml格式的日志
--log-json=FILE            以json格式记录日志
--log-json-verbose=FILE            记录详细的json日志
--log-magictree=FILE            xml的树形结构
--log-object=FILE            ruby对象格式
--log-mongo-database            mongo数据库格式
json格式需要安装json依赖sudo gem install json
Mongo格式需要安装mongo依赖sudo gem install mongo

```

>  
 扫描单网站输出xml文件 


```
whatweb  http://192.168.233.181 --log-xml=output.txt

```

<img src="https://img-blog.csdnimg.cn/04dd524e02e249c99989d57b1d32639e.png" alt="在这里插入图片描述">

>  
 扫描单网段输出xml文件 


```
whatweb  --no-errors -t 255 192.168.233.0/24 --log-xml=output1.txt

```

<img src="https://img-blog.csdnimg.cn/87b1ea39029b469f88c327d715c63e79.png" alt="在这里插入图片描述">

#### 9.查看whatweb插件信息

```
whatweb -l

```

<img src="https://img-blog.csdnimg.cn/cdc2921201c94af5aecd788b60522628.png" alt="在这里插入图片描述">

## 五、whatweb插件编写

>  
 whatweb对国内的网站识别不是很友好，我们可以自己写插件，兼容更多国内的网站。 


### 1、官方模板

>  
 whatweb的官方模板如下： 


```
Plugin.define "Plugin-Template" do
    author "Enter Your Name"
    version "0.1"
    description "Describe what the plugin identifies. Include the homepage of the software package"
    examples %w| include-some.net example-websites.com here.com |
 
    \# a comment block here is a good place to make notes for yourself and others 
 
    \# There are four types of matches: regexp, text, ghdb 
    \# Matches are enclosed in {<!-- -->} brackets and separated by commas 
    matches [
    {<!-- -->:name=&gt;"a brief description of the match, eg. powered by in footer",
    :certainty=&gt;100, # 100 is certain, 75 is probably and 25 is maybe. if omitted, it defaults to 100. 
    :regexp=&gt;/This page was generated by http://www.genericcms.com\/en\/products\/generic-cms\/"&gt;Generic CMS&lt;\/a&gt;/ },
 
    {:name=&gt;"title",
    :certainty=&gt;75,
    :text=&gt;"&lt;title&gt;Generic Homepage&lt;/title&gt;" }
    ]
end

```

### 2、解释模板

>  
 第一行定义的为插件的名字，可以直接在命令行中使用。 第二行作者，第三行版本，第四行插件描述，第五行，插件所使用网站的例子 第五行是一个matchs列表，也是whatweb的关键，里边定义了一些匹配规则 {:name=&gt;”meta generator tag”, : 包含匹配的文件名称，这个文件必须是网站中唯一存在的文件。 :regexp=&gt; 是包含的要匹配的模式，它是一个正则表达式，可以有以下选项： 


```
:regexp标准的 ruby 正则表达式
:text 字符
:ghdb google hack 数据库，包含以下几个模式
inurl:包含的字符串在 url
intitle:包含的字符串在 title
filetype:包含的文件名，如 PDF, JPG, RB 等
:md5 请求页面的 md5 hash 值
:tagpattern html 标签
:version 可以设置正则表达式或直接字符串匹配
:string 可以设置正则表达式或直接字符串匹配
:filepath 可以设置正则表达式或直接字符串匹配，通常显示系统错误或配置文件等
:account 经常用在登陆页面或用户列表等
:module 可以设置正则表达式或直接字符串匹配，如网络设备可能使用了一个ruby 模块等
:model 可以设置正则表达式或直接字符串匹配
:firmware 可以设置正则表达式或直接字符串匹配，设备的固件版本

```

### 3、实例

```
Plugin.define "DedeCMS" do
author "xxxxx"
version "0.1"
description "dedecms - homepage:http://www.dedecms.com/"
 
# Examples # 
examples %w|
www.dedecms.com|
 
matches [
 
# Version detection # Powered by text 
{<!-- -->:name=&gt;"Powered by DedeCms",
:regexp=&gt;/Powered by .*DedeCMS.*/}
]
end

```
