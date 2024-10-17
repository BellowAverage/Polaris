
--- 
title:  10天get搞懂python爬虫？！ 
tags: []
categories: [] 

---
>  
 前段时间，知乎上有人提问：**有哪些足不出户，能用十天左右时间掌握的新技能？** 由于疫情，很多人不得不在家隔离，这段难得的‘假期’不用来学习简直暴殄天物。理财、自媒体、英语、编程…推荐啥的都有，不经意的我随手一答[逃，意外地获得了超过50w的阅读量。 鲁迅曾‘说’过：有好东西就得拿出来。有这么多人看必然不是什么坏东西，贴出来给诸君看看，我的回答是：**爬虫**。 


以下原文

get新技能，学习写爬虫？！ <img src="https://img-blog.csdnimg.cn/img_convert/5d295be2fefc769642c7707f0b1004b3.webp?x-oss-process=image/format,png" alt="">

### 一、为啥学爬虫？

看到一个帖子，有人用python爬虫在京东抢口罩，实现实时监测、实时抢购。

可以说很调皮了~ <img src="https://img-blog.csdnimg.cn/img_convert/7c043417dcb6f115e52f755dd3932b80.webp?x-oss-process=image/format,png" alt=""> <img src="https://img-blog.csdnimg.cn/img_convert/82397d3338d6498d3cc2e6705545cffc.webp?x-oss-process=image/format,png" alt="">

这是爬虫在电商领域的一个小应用，除此之外你还能使用爬虫进行：商品抓取、价格监控、评论抓取、竞品分析、动态定价等等。

其他领域，你可以使用爬虫做：房源监控分析、网络舆情监测、精准客户获取、新闻资讯筛选、地信数据抓取、金融股票分析等等。

这些对于从事相关行业的分析人员还是很有学习意义的。

<img src="https://img-blog.csdnimg.cn/img_convert/42b39ae06461937a86494f6be93d5db9.webp?x-oss-process=image/format,png" alt="">

当然你还可以用爬虫搞一下骚操作：知乎妹子高清图片、言情小说、b站学习视频、豆瓣电影书籍、抖音美女视频…这些都可以爬下来收藏。[逃

<img src="https://img-blog.csdnimg.cn/img_convert/506283089b0ea5cff30c4b4ddc5fec03.webp?x-oss-process=image/format,png" alt="">

之前一直很火的用python登录12306抢票，也是爬虫的杰作，不过现在越来越难了，各种反爬设置。大家有兴趣可以去github上看一下这个项目开源代码。

学爬虫当然离不开python，所以这10天你还能get python编程，当今最火的AI编程语言。

当然你也可以用集成好的第三方软件来爬，像八爪鱼、后羿之类的，但我还是建议用python来写爬虫，能学到更多东西。

### 二、什么是爬虫？

爬虫是一个形象的叫法，网络爬虫其实是网络数据采集，针对性地用代码实现网络上各种数据（文字、图片、视频）的抓取。我们熟知的谷歌、百度等搜索引擎，也是使用的爬虫技术。

通俗点说，爬虫就像是一个穿梭于网络世界的智能蜘蛛，你给它一个网址（url），然后设定规则，它就能突破重重险阻，把你想要的数据抓取下来，然后保存。

<img src="https://img-blog.csdnimg.cn/img_convert/79738d0614b2561c23bbc298f40cdd56.webp?x-oss-process=image/format,png" alt="">

能实现爬虫的语言有很多，像Java、PHP、Python、C#…都可以用各种方式达到你的要求，那为什么要用python呢？

人生苦短，python当歌！

python是一门高级编程语言，语法简介，十分适合初学者。因此拥有了超级强大的开发社区，捣鼓出各种神奇的第三方库，比如requests、beautifulsoup、scrapy、xpath、selenium等，都是爬虫界的利器。

当然网络爬虫有利有弊，你可以爬人家的数据，但也要承担可能存在的法律风险。慎重！

### 三、python爬虫有些学习资源？

本来想先简单介绍一下如何学习python爬虫，但还是先把学习资源讲一讲，毕竟好多资源控￣□￣

对于小白来说，首先是学习python语法。

python学习家族有三个派别：视频派、教程派、书籍派。

喜欢看视频的就去b站吧，python视频教学相当丰富，选择播放量前几名的系统学习下，听说小甲鱼的就还不错。

<img src="https://img-blog.csdnimg.cn/img_convert/8bafe99ba3a986646a273b15d1bce565.webp?x-oss-process=image/format,png" alt="">

当然有钱的你，可以选择一些网上课程，像腾讯课堂、网易云课堂里面的课。

不要问为什么，花钱买心安。比如我猜大方的你，会打赏这篇回答[hah

教程派的选择很多了，像菜鸟教程、w3cschool、廖雪峰、python官档…

推荐大家先看菜鸟教程、再看廖雪峰，官档随时查询。

<img src="https://img-blog.csdnimg.cn/img_convert/96ea68e7d7d18678a6c8ca611cceaf10.webp?x-oss-process=image/format,png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/e1a3eaa845f0773a5b02f4ae51516451.webp?x-oss-process=image/format,png" alt="">

### 四、如何入门python爬虫？

终于讲到入门实操了，想要入门Python 爬虫首先需要解决四个问题
- 熟悉python编程- 了解HTML- 了解网络爬虫的基本原理- 学习使用python爬虫库
#### 1、你应该知道什么是爬虫？

网络爬虫，其实叫作网络数据采集更容易理解。

就是通过编程向网络服务器请求数据（HTML表单），然后解析HTML，提取出自己想要的数据。

归纳为四大步：
- 根据url获取HTML数据- 解析HTML，获取目标信息- 存储数据- 重复第一步
这会涉及到数据库、网络服务器、HTTP协议、HTML、数据科学、网络安全、图像处理等非常多的内容。但对于初学者而言，并不需要掌握这么多。

#### 2、python要学习到什么程度

如果你不懂python，那么需要先学习python这门非常easy的语言（相对其它语言而言）。

编程语言基础语法无非是数据类型、数据结构、运算符、逻辑结构、函数、文件IO、错误处理这些，学起来会显枯燥但并不难。

刚开始入门爬虫，你甚至不需要去学习python的类、多线程、模块之类的略难内容。找一个面向初学者的教材或者网络教程，花个十几天功夫，就能对python基础有个三四分的认识了，这时候你可以玩玩爬虫喽！

当然，前提是你必须在这十几天里认真敲代码，反复咀嚼语法逻辑，比如列表、字典、字符串、if语句、for循环等最核心的东西都得捻熟于心、于手。

教材方面比较多选择，我个人是比较推荐**python官方文档**以及**python简明教程**，前者比较系统丰富、后者会更简练。

#### 3、为什么要懂HTML

前面说到过爬虫要爬取的数据藏在网页里面的HTML里面的数据，有点绕哈！

维基百科是这样解释HTML的

>  
 **超文本标记语言**（英语：**H**yper**T**ext**M**arkup**L**anguage，简称：**HTML**）是一种用于创建网页的标准标记语言。HTML是一种基础技术，常与CSS、JavaScript一起被众多网站用于设计网页、网页应用程序以及移动应用程序的用户界面。网页浏览器可以读取HTML文件，并将其渲染成可视化网页。HTML描述了一个网站的结构语义随着线索的呈现，使之成为一种标记语言而非编程语言。 


总结一下，HTML是一种用于创建网页的标记语言，里面嵌入了文本、图像等数据，可以被浏览器读取，并渲染成我们看到的网页样子。

所以我们才会从先爬取HTML，再 解析数据，因为数据藏在HTML里。

学习HTML并不难，它并不是编程语言，你只需要熟悉它的标记规则，这里大致讲一下。

HTML标记包含标签（及其属性）、基于字符的数据类型、字符引用和实体引用等几个关键部分。

HTML标签是最常见的，通常成对出现，比如`&lt;**h1**&gt;`与`&lt;/**h1**&gt;`。

这些成对出现的标签中，第一个标签是开始标签，第二个标签是结束标签。两个标签之间为元素的内容（文本、图像等），有些标签没有内容，为空元素，如`&lt;**img**&gt;`。

以下是一个经典的Hello World程序的例子：

```
&lt;!DOCTYPE html&gt;
&lt;html&gt;
  &lt;head&gt;
    &lt;title&gt;This is a title&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;p&gt;Hello world!&lt;/p&gt;
  &lt;/body&gt;
&lt;/html&gt;


```

HTML文档由嵌套的HTML元素构成。它们用HTML标签表示，包含于尖括号中，如`&lt;**p**&gt;`

在一般情况下，一个元素由一对标签表示：“开始标签”`&lt;**p**&gt;`与“结束标签”`&lt;/**p**&gt;`。元素如果含有文本内容，就被放置在这些标签之间。

#### 4、了解python网络爬虫的基本原理

在编写python爬虫程序时，只需要做以下两件事：
- 发送GET请求，获取HTML- 解析HTML，获取数据
这两件事，python都有相应的库帮你去做，你只需要知道如何去用它们就可以了。

### 关于Python技术储备

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以找到适合自己的学习方案 


包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习等习教程。带你从零基础系统性的学好Python！

## 零基础Python学习资源介绍

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。**（全套教程文末领取哈）** <img src="https://img-blog.csdnimg.cn/img_convert/673b13641cf2ddf5e18b5c58afd50200.png#pic_center" alt="">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

###### 这份完整版的Python全套学习资料已经上传CSDN，朋友们如果需要可以微信扫描下方CSDN官方认证二维码免费领取【`保证100%免费`】

<img src="https://img-blog.csdnimg.cn/1d2a69f2d57e4d1cb444037b17af8607.png" alt="">
