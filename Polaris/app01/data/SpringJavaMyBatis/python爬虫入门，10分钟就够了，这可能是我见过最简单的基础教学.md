
--- 
title:  python爬虫入门，10分钟就够了，这可能是我见过最简单的基础教学 
tags: []
categories: [] 

---


#### 文章目录
- - <ul><li>- <ul><li>- <ul><li>- - - - - - - - 


## 前言

###  初学Python之爬虫的简单入门

#### 一、 什么是爬虫？

#####  1.简单介绍爬虫

**<img src="https://img-blog.csdnimg.cn/img_convert/79680d138a7b1b68ab353f58a0e888b3.png#pic_center" alt="">**

爬虫的全称为网络爬虫，简称爬虫，别名有网络机器人，网络蜘蛛等等。

网络爬虫是一种自动获取网页内容的程序，为搜索引擎提供了重要的数据支撑。搜索引擎通过网络爬虫技术，将互联网中丰富的网页信息保存到本地，形成镜像备份。我们熟悉的谷歌、百度本质上也可理解为一种爬虫。

如果形象地理解，爬虫就如同一只机器蜘蛛，它的基本操作就是模拟人的行为去各个网站抓取数据或返回数据。

#####  2.爬虫的分类

网络爬虫一般分为传统爬虫和聚焦爬虫。

传统爬虫从一个或若干个初始网页的URL开始，抓取网页时不断从当前页面上抽取新的URL放入队列，直到满足系统的一定条件才停止，即通过源码解析来获得想要的内容。

聚焦爬虫需要根据一定的网页分析算法过滤与主题无关的链接，保留有用的链接并将其放入待抓取的URL队列，再根据一定的搜索策略从队列中选择下一步要抓取的网页URL，并重复上述过程，直到满足系统的一定条件时停止。另外，所有被爬虫抓取的网页都将会被系统存储、分析、过滤，并建立索引，以便之后的查询和检索;对于聚焦爬虫来说，这一过程所得到的分析结果还可能对以后的抓取过程给出反馈和指导。

防爬虫:KS-WAF（网站统一防护系统）将爬虫行为分为搜索引擎爬虫及扫描程序爬虫，可屏蔽特定的搜索引擎爬虫节省带宽和性能，也可屏蔽扫描程序爬虫，避免网站被恶意抓取页面。使用防爬虫机制的基本上是企业，我们平时也能见到一些对抗爬虫的经典方式，如图片验证码、滑块验证、封禁 IP等等。

#####  3.爬虫的工作原理

下图是一个网络爬虫的基本框架：

<img src="https://img-blog.csdnimg.cn/img_convert/ff94ea0c9eddec014791b84f3c019696.png#pic_center" alt="">

对应互联网的所有页面可划分为五部分：

<img src="https://img-blog.csdnimg.cn/img_convert/d22c5d9208355c947bf48ad29fd0d773.png#pic_center" alt="">

1.**已下载未过期网页**。

2.**已下载已过期网页**：抓取到的网页实际上是互联网内容的一个镜像文件，互联网是动态变化的，一部分互联网上的内容已经发生了变化，这时，这部分抓取到的网页就已经过期了。

3.**待下载网页**：待抓取URL队列中的页面。

4.**可知网页**：既没有被抓取也没有在待抓取URL队列中，但可通过对已抓取页面或者待抓取URL对应页面进行分析获取到的URL，认为是可知网页。

5.**不可知网页**：爬虫无法直接抓取下载的网页。

待抓取URL队列中的URL顺序排列涉及到抓取页面的先后次序问题，而决定这些URL排列顺序的方法叫做抓取策略。下面介绍六种常见的抓取策略：

1.**深度优先遍历策略**

深度优先遍历策略是指网络爬虫从起始页开始，由一个链接跟踪到另一个链接，这样不断跟踪链接下去直到处理完这条线路，之后再转入下一个起始页，继续跟踪链接。以下图为例：

<img src="https://img-blog.csdnimg.cn/img_convert/42a2657d885cdb80a45ecffb05acf4fc.png#pic_center" alt="">

遍历路径：A-F-G E-H-I B C D

需要注意的是，深度优先可能会找不到目标节点（即进入无限深度分支），因此，深度优先策略不一定能适用于所有情况。

2.**宽度优先遍历策略**

宽度优先遍历策略的基本思路是，将新下载网页中发现的链接直接插入待抓取URL队列的末尾。也就是指网络爬虫会先抓取起始网页中链接的所有网页，然后再选择其中的一个链接网页，继续抓取在此网页中链接的所有网页。还是以上图为例：

<img src="https://img-blog.csdnimg.cn/img_convert/151f7cd1b44a287262f6d8556a76d96b.png#pic_center" alt="">

遍历路径：第一层：A-B-C-D-E-F，第二层：G-H，第三层：I

广度优先遍历策略会彻底遍历整个网络图，效率较低，但覆盖网页较广。

3.**反向链接数策略**

反向链接数是指一个网页被其他网页链接指向的数量。反向链接数反映一个网页的内容受到其他人推荐的程度。因此，很多时候搜索引擎的抓取系统会使用这个指标来评价网页的重要程度，从而决定不同网页的抓取先后顺序。

而现实是网络环境存在各种广告链接、作弊链接的干扰，使得许多反向链接数反映的结果并不可靠。

4.**Partial PageRank策略**

Partial PageRank策略借鉴了PageRank算法的思想：对于已下载网页，连同待抓取URL队列中的URL，形成网页集合，计算每个页面的PageRank值，然后将待抓取URL队列中的URL按照PageRank值的大小进行排列，并按照该顺序抓取页面。

若每次抓取一个页面，就重新计算PageRank值，则效率太低。

一种折中方案是：每抓取K个页面后，重新计算一次PageRank值。而对于已下载页面中分析出的链接，即暂时没有PageRank值的未知网页那一部分，先给未知网页一个临时的PageRank值，再将这个网页所有链接进来的PageRank值进行汇总，这样就形成了该未知页面的PageRank值，从而参与排序。以下图为例：

<img src="https://img-blog.csdnimg.cn/img_convert/1bd760fa31a3440f920a1f01d6fb55b3.png#pic_center" alt="">

设k值为3，即每抓取3个页面后，重新计算一次PageRank值。

已知有{1,2,3}这3个网页下载到本地，这3个网页包含的链接指向待下载网页{4,5,6}（即待抓取URL队列），此时将这6个网页形成一个网页集合，对其进行PageRank值的计算，则{4,5,6}每个网页得到对应的PageRank值，根据PageRank值从大到小排序，由图假设排序结果为5,4,6，当网页5下载后，分析其链接发现指向未知网页8，这时先给未知网页8一个临时的PageRank值，如果这个值大于网页4和6的PageRank值，则接下来优先下载网页8，由此思路不断进行迭代计算。

5.**OPIC策略**

此算法其实也是计算页面重要程度。在算法开始前，给所有页面一个相同的初始现金（cash）。当下载了某个页面P之后，将P的现金分摊给所有从P中分析出的链接，并且将P的现金清空。对于待抓取URL队列中的所有页面按照现金数大小进行排序。

6.**大站优先策略**

对于待抓取URL队列中的所有网页，根据所属的网站进行分类。待下载页面数多的网站优先下载。

####  二、爬虫的基本流程

首先简单了解关于Request和Response的内容：

Request：浏览器发送消息给某网址所在的服务器，这个请求信息的过程叫做HTTP Request。

Response:服务器接收浏览器发送的消息，并根据消息内容进行相应处理，然后把消息返回给浏览器。这个响应信息的过程叫做HTTP Response。浏览器收到服务器的Response信息后，会对信息进行相应处理，然后展示在页面上。

根据上述内容将网络爬虫分为四个步骤：

1.**发起请求**：通过HTTP库向目标站点发起请求，即发送一个Request，请求可以包含额外的headers等信息，等待服务器响应。

常见的请求方法有两种，GET和POST。get请求是把参数包含在了URL（Uniform Resource Locator,统一资源定位符）里面，而post请求大多是在表单里面进行，也就是让你输入用户名和秘密，在url里面没有体现出来，这样更加安全。post请求的大小没有限制，而get请求有限制，最多1024个字节。

2.**获取响应内容**：如果服务器能正常响应，会得到一个Response，Response的内容便是所要获取的页面内容，类型可能有HTML，Json字符串，二进制数据（如图片视频）等类型。

3.**解析内容**：得到的内容可能是HTML，可以用正则表达式、网页解析库进行解析。可能是Json，可以直接转为Json对象解析，可能是二进制数据，可以做保存或者进一步的处理。

在Python语言中，我们经常使用Beautiful Soup、pyquery、lxml等库，可以高效的从中获取网页信息，如节点的属性、文本值等。

Beautiful Soup库是解析、遍历、维护“标签树”的功能库，对应一个HTML/XML文档的全部内容。安装方法非常简单，如下：

```
#安装方法
pips install beautifulsoup4

#验证方法
from bs4 import BeautifulSoup


```

4.**保存数据**：如果数据不多，可保存在txt 文本、csv文本或者json文本等。如果爬取的数据条数较多，可以考虑将其存储到数据库中。也可以保存为特定格式的文件。

保存后的数据可以直接分析，主要使用的库如下：NumPy、Pandas、 Matplotlib。

NumPy：它是高性能科学计算和数据分析的基础包。

Pandas : 基于 NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。它可以算得上作弊工具。

Matplotlib：Python中最著名的绘图系统Python中最著名的绘图系统。它可以制作出散点图，折线图，条形图，直方图，饼状图，箱形图散点图，折线图，条形图，直方图，饼状图，箱形图等。

####  三、爬虫简单实例

运行平台： Windows

Python版本： Python3.7

首先查看网址的源代码，使用google浏览器，右键选择检查，查看需要爬取的网址源代码，在Network选项卡里面，点击第一个条目可看到源代码。

第一部分是General，包括了网址的基本信息，比如状态 200等，第二部分是Response Headers,包括了请求的应答信息,还有body部分，比如Set-Cookie,Server等。第三部分是，Request headers，包含了服务器使用的附加信息，比如Cookie,User-Agent等内容。

上面的网页源代码，在python语言中，我们只需要使用urllib、requests等库实现即可，具体如下。

```
import urllib.request
import socket
from urllib import error
try:
    response \= urllib.request.urlopen('https://www.python.org')
    print(response.status)
    print(response.read().decode('utf-8'))
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\\n')
except error.URLError as e:
    print(e.reason)
else:
print('Request Successfully')


```

运行结果如下：

<img src="https://img-blog.csdnimg.cn/img_convert/9f0c318e1504b7371dacafa11d8eb29d.png" alt="">

####  四、关于入门爬虫

在如今这个信息爆炸的大数据时代，数据的价值是可观的，而网络爬虫无疑是一个获取数据信息的便捷途径。合理利用爬虫爬取有价值的数据，可以为我们的生活提供不少帮助。

实际上，关于网络爬虫，我完全是一个新手，写下这篇博客的途中也同时在零基础学习。

首先，我了解到python3的语法是需要掌握的，因为要打好基础。不过python3语法很简洁，学起来应该不会过分吃力。

接着是python的各种库，目前接触的不多，像我这种还是从基础的库开始学习会比较好，比如urlib、requests。

在学习过程中也了解到现在很多大型企业在使用反爬虫机制，爬虫过程中可能会返回非法请求，需要使用代理防止封禁IP，爬取网页需要伪装成平时正常使用浏览器那样。这又是另外要解决的问题了。

总之，对于新手来说是需要一步一步花时间深入学习的，平时也得多加练习，毕竟学习之事并非一朝一夕就能促成，重要的是坚持吧。

**-END-**

<mark>**读者福利：如果大家对Python感兴趣，这套python学习资料一定对你有用**</mark>

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以根据这些资料规划好学习计划和方向。 


<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习、Python量化交易等习教程。带你从零基础系统性的学好Python！</mark>

## 零基础Python学习资源介绍

① Python所有方向的<mark>学习路线图</mark>，清楚各个方向要学什么东西

② 600多节<mark>Python课程视频</mark>，涵盖必备基础、爬虫和数据分析

③ 100多个<mark>Python实战案例</mark>，含50个超大型项目详解，学习不再是只会理论

④ 20款主流手游迫解 <mark>爬虫手游逆行迫解教程包</mark>

⑤ <mark>爬虫与反爬虫攻防</mark>教程包，含15个大型网站迫解

⑥ <mark>爬虫APP逆向实战</mark>教程包，含45项绝密技术详解

⑦ 超<mark>300本Python电子好书</mark>，从入门到高阶应有尽有

⑧ 华为出品独家<mark>Python漫画教程</mark>，手机也能学习

⑨ 历年互联网企业<mark>Python面试真题</mark>,复习时非常方便

<img src="https://img-blog.csdnimg.cn/7c1055f9bb6e41af9262556bdf20e084.png#pic_center" alt="在这里插入图片描述">

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取哈）**</mark> <img src="https://img-blog.csdnimg.cn/9f969354b48f4e3ab0253e89203deca2.png#pic_center" alt="在这里插入图片描述">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉实战案例👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/6cf364e7eeb64b0da07021bce5a59ec6.png#pic_center" alt="在这里插入图片描述">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

## 资料领取

<mark>这份完整版的Python全套学习资料已为大家备好，朋友们如果需要可以微信扫描下方二维码添加，输入"领取资料" 可免费领取全套资料</mark>【<font color="#CC0033" size="3" face="微软雅黑">有什么需要协作的还可以随时联系我</font>】<mark>朋友圈也会不定时的更新最前言python知识。↓↓↓</mark><font color="red" size="3"> **或者**</font> 【】领取
