
--- 
title:  Python爬虫——Scrapy 的基本使用 
tags: []
categories: [] 

---
Scrapy 框架中创建项目、查看配置信息，以及运行爬虫程序都是通过指令完成。

常用指令如下所示：

     |指令   |格式   |说明  
 |------
   |startproject   |scrapy startproject &lt;项目名&gt;   |创建新项目  
   |genspider   |scrapy genspider &lt;爬虫文件名&gt; &lt;访问的域名&gt;   |新建爬虫文件  
   |runspider   |scrapy runspider &lt;爬虫文件&gt;   |运行一个爬虫文件，不需要创建项目  
   |crawl   |scrapy crawl &lt;爬虫项目名&gt;   |运行一个爬虫项目，必须要创建项目  
   |list   |scrapy list   |列出项目中所有爬虫文件  
   |view   |scrapy view &lt;url地址&gt;   |从浏览器中打开 url 地址  
   |shell   |csrapy shell &lt;url地址&gt;   |命令行交互模式  
   |settings   |scrapy settings   |查看当前项目的配置信息  

### 

### 1、创建 Scrapy 爬虫项目

创建一个名为 scrapy_01 的 Scrapy 项目：

```
scrapy startproject scrapy_01
复制代码
```

打开命令行，选择python项目路径，创
