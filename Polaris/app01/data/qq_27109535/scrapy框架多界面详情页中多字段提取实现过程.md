
--- 
title:  scrapy框架多界面详情页中多字段提取实现过程 
tags: []
categories: [] 

---
## scrapy框架详情页中多字段提取实现过程

Scrapy，Python开发的一个快速、高层次的屏幕抓取和web抓取框架，用于抓取web站点并从页面中提取结构化的数据。Scrapy用途广泛，可以用于数据挖掘、监测和自动化测试.

其最初是为了页面抓取 (更确切来说, 网络抓取 )所设计的， 后台也应用在获取API所返回的数据(例如 Amazon Associates Web Services ) 或者通用的网络爬虫.

## 前言

#### Scrapy五大基本构成:

Scrapy框架主要由五大组件组成，它们分别是调度器(Scheduler)、下载器(Downloader)、爬虫（Spider）和实体管道(Item Pipeline)、Scrapy引擎(Scrapy Engine)。下面我们分别介绍各个组件的作用。

##### (1)、调度器(Scheduler):

调度器，说白了把它假设成为一个URL（抓取网页的网址或者说是链接）的优先队列，由它来决定下一个要抓取的网址是 什么，同时去除重复的网址（不做无用功）。用户可以自己的需求定制调度器。

##### (2)、下载器(Downloader):

下载器，是所有组件中负担最大的，它用于高速地下载网络上的资源。Scrapy的下载器代码不会太复杂，但效率高，主要的原因是Scrapy下载器是建立在twisted这个高效的异步模型上的(其实整个框架都在建立在这个模型上的)。

##### (3)、 爬虫（Spider）

:

爬虫，是用户最关心的部份。用户定制自己的爬虫(通过定制正则表达式等语法)，用于从特定的网页中提取自己需要的信息，即所谓的实体(Item)。 用户也可以从中提取出链接,让Scrapy继续抓取下一个页面。

##### (4)、 实体管道(Item Pipeline):

实体管道，用于处理爬虫(spider)提取的实体。主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。

##### (5)、Scrapy引擎(Scrapy Engine):

Scrapy引擎是整个框架的核心.它用来控制调试器、下载器、爬虫。实际上，引擎相当于计算机的CPU,它控制着整个流程。

三、整体架构图 本图按顺序说明整个程序执行时候发生的顺序。 <img src="https://img-blog.csdnimg.cn/3e54145baac5465098d8bbe8acf54f7b.png" alt="在这里插入图片描述">

注意在调用下载器时，往往有一个下载器中间件，使下载速度提速。

官网架构图

<img src="https://img-blog.csdnimg.cn/bd28e3ba1a5241f98f81ffe380636c52.png" alt="在这里插入图片描述">

 - 为了统计某地区的二手房交易情况，需要获取大量二手房交易数据。链家网是一个专业的房地产“O2O”交易平台，主营二手房、新房、租房、房价查询等业务。链家网展示的房源众多、房屋信息详实并且页面设计工整。

### 一、项目需求

使用Scrapy爬取链家网中苏州市二手房交易数据并保存于CSV文件中。苏州市二手房信息的主页面，地址为https://su.lianjia.com/ershoufang/。爬取的房屋数据有： ： <img src="https://img-blog.csdnimg.cn/2c49c1b5aa894bb49dc1e236de27faf3.png" alt="在这里插入图片描述">

```
                                               **图4-9所示为苏州市二手房信息的主页面**

```

·房屋名称； ·房屋户型； ·建筑面积； ·房屋朝向； ·装修情况； ·有无电梯； ·房屋总价； ·房屋单价； ·房屋产权。 要求： <img src="https://img-blog.csdnimg.cn/ffb8248a331c4cbdad685a393f371c31.png" alt="在这里插入图片描述"> 4-10房屋信息详情页 房屋面积、总价和单价只需要具体的数字，不需要单位名称。 删除字段不全的房屋数据，如有的房屋朝向会显示“暂无数据”，应该剔除。 保存到CSV文件中的数据，字段要按照如下顺序排列：房屋名称，房屋户型，建筑面积，房屋朝向，装修情况，有无电梯，房屋总价，房屋单价，房屋产权。

### 二、项目分析

#### 1．使用Spider提取数据

```
	通过页面分析发现，爬取的二手房交易数据分布在两个页面中，每个页面包含一部分数据。房屋名称、房屋户型、建筑面积、房屋朝向、装修情况、有无电梯、总价、单价的数据可以在房屋信息主页面中（图4-9）获取，但是产权数据需要进入房屋详情页面中（图4-10）获取。因此，要想获取一条完整的房屋交易数据，就需要解析两个页面，再将两个页面的数据合并发送给引擎保存到CSV文件中。如图4-11所示为项目实现的流程。
	首先在start_requests()方法中生成访问初始页的Request对象。页面下载后，主页面解析函数提取页面中的部分房屋信息（不含产权信息），同时获取详情页的URL。将详情页的URL和已提取的房屋信息作为参数生成详情页的Request对象提交给引擎。详情页下载后，详情页解析函数提取房屋产权信息，并与主解析函数中得到的部分房屋数据合并，形成一条完整的房屋数据，最后将数据提交给Pipeline处理。

```

#### 2．使用Item封装数据

数据提取后，使用Item封装数据

<img src="https://img-blog.csdnimg.cn/2c5c4024348a4d72a0bc4901cd27c1a1.png" alt="在这里插入图片描述">

#### 3．使用Pipeline处理数据

数据处理主要分为以下两大部分： （1）过滤、清理数据（FilterPipeline）。 从爬取到的房屋面积、单价和产权文本中提取出数字，并且过滤掉字段不全的房屋。 （2）将数据保存于CSV文件（CSVPipeline）中。 因为使用命令生成的CSV文件中，字段的排列是随机的，而本项目要求字段固定排列，因此需要通过Pipeline将数据保存于CSV文件中。 本项目建立了两个Pipeline类分别对应上述两种数据处理功能，体现了模块化的设计思想。

### 三 代码实现及解析

#### 1．创建项目

创建一个名为lianjia_home的Scrapy项目。

```
scrapy startproject lianjia_home

```

#### 2．使用Item封装数据

打开项目lianjia_home中的items.py源文件，添加二手房信息字段。实现代码如下：

```
# -*- coding: UTF-8 -*-
import scrapy
class LianjiaHomeItem(scrapy.Item):
     name = scrapy.Field()               # 名称
     type = scrapy.Field()               # 户型
     area = scrapy.Field()               # 面积
     direction = scrapy.Field()          # 朝向
     fitment = scrapy.Field()            # 装修情况
     elevator = scrapy.Field()           # 有无电梯
     total_price = scrapy.Field()        # 总价
     property = scrapy.Field()           # 产权信息
     unit_price = scrapy.Field()         # 单价

```

#### 
