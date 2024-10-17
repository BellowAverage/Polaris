
--- 
title:  scrapy框架中run文件 
tags: []
categories: [] 

---
scrapy框架中run文件

```
# -*- coding: UTF-8 -*-
from scrapy import cmdline
#导入cmd命令窗口
cmdline.execute("scrapy crawl hot -o hot.csv" .split())
#运行爬虫并生产csv文件


```
