
--- 
title:  Python网络爬虫第二课----requests模块应用 
tags: []
categories: [] 

---
### 引入

Requests 唯一的一个非转基因的 Python HTTP 库，人类可以安全享用。

### 警告：

非专业使用其他 HTTP 库会导致危险的副作用，包括：安全缺陷症、冗余代码症、重新发明轮子症、啃文档症、抑郁、头疼、甚至死亡。

### 今日概要

基于requests的get请求 基于requests模块的post请求 基于requests模块ajax的get请求 基于requests模块ajax的post请求 综合项目练习：爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据

### 知识点回顾

常见的请求头 常见的相应头 https协议的加密方式

今日详情
- 基于如下5点展开requests模块的学习 什么是requests模块 requests模块是python中原生的基于网络请求的模块，其主要作用是用来模拟浏览器发起请求。功能强大，用法简洁高效。在爬虫领域中占据着半壁江山的地位。 为什么要使用requests模块 因为在使用urllib模块的时候，会有诸多不便之处，总结如下： 手动处理url编码 手动处理post请求参数 处理cookie和代理操作繁琐 …
### 使用requests模块：

自动处理url编码 自动处理post请求参数 简化cookie和代理操作 …

### 如何使用requests模块

安装： pip install requests

### 使用流程

指定url 基于requests模块发起请求 获取响应对象中的数据值 持久化存储

### 通过5个基于requests模块的爬虫项目对该模块进行学习和巩固

基于requests模块的get请求 需求：爬取搜狗指定词条搜索后的页面数据 基于requests模块的post请求 需求：登录豆瓣电影，爬取登录成功后的页面数据 基于requests模块ajax的get请求 需求：爬取豆瓣电影分类排行榜 https://movie.douban.com/中的电影详情数据 基于requests模块ajax的post请求 需求：爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/index.aspx中指定地点的餐厅数据

### 综合练习

需求：爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据http://125.35.6.84:81/xk/
- 代码展示 需求：爬取搜狗指定词条搜索后的页面数据
```
import requests
import os
#指定搜索关键字
word = input('enter a word you want to search:')
#自定义请求头信息
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
#指定url
url = 'https://www.sogou.com/web'
#封装get请求参数
prams = {
    'query':word,
    'ie':'utf-8'
}
#发起请求
response = requests.get(url=url,params=param)

#获取响应数据
page_text = response.text

with open('./sougou.html','w',encoding='utf-8') as fp:
    fp.write(page_text)

```

请求载体身份标识的伪装：

### User-Agent

：请求载体身份标识，通过浏览器发起的请求，请求载体为浏览器，则该请求的User-Agent为浏览器的身份标识，使用爬虫程序发起的请求，则该请求的载体为爬虫程序，则该请求的User-Agent为爬虫程序的身份标识。可以通过判断该值来获知该请求的载体究竟是基于哪款浏览器还是基于爬虫程序。

### 反爬机制

：某些门户网站会对访问该网站的请求中的User-Agent进行捕获和判断，如果该请求的UA为爬虫程序，则拒绝向该请求提供数据。

### 反反爬策略

：将爬虫程序的UA伪装成某一款浏览器的身份标识。

### 需求：登录豆瓣电影，爬取登录成功后的页面数据

```
import requests
import os
url = 'https://accounts.douban.com/login'
#封装请求参数
data = {
    "source": "movie",
    "redir": "https://movie.douban.com/",
    "form_email": "15027900535",
    "form_password": "bobo@15027900535",
    "login": "登录",
}
#自定义请求头信息
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
response = requests.post(url=url,data=data)
page_text = response.text

with open('./douban111.html','w',encoding='utf-8') as fp:
    fp.write(page_text)

```

### 需求：爬取豆瓣电影分类排行榜 https://movie.douban.com/中的电影详情数据

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import urllib.request
if __name__ == "__main__":

    #指定ajax-get请求的url（通过抓包进行获取）
    url = 'https://movie.douban.com/j/chart/top_list?'

    #定制请求头信息，相关的头信息必须封装在字典结构中
    headers = {
        #定制请求头中的User-Agent参数，当然也可以定制请求头中其他的参数
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }

    #定制get请求携带的参数(从抓包工具中获取)
    param = {
        'type':'5',
        'interval_id':'100:90',
        'action':'',
        'start':'0',
        'limit':'20'
    }
    #发起get请求，获取响应对象
    response = requests.get(url=url,headers=headers,params=param)

    #获取响应内容：响应内容为json串
    print(response.text)

```

### 需求：爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/index.aspx中指定地点的餐厅数据

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import urllib.request
if __name__ == "__main__":

    #指定ajax-post请求的url（通过抓包进行获取）
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    #定制请求头信息，相关的头信息必须封装在字典结构中
    headers = {
        #定制请求头中的User-Agent参数，当然也可以定制请求头中其他的参数
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }

    #定制post请求携带的参数(从抓包工具中获取)
    data = {
        'cname':'',
        'pid':'',
        'keyword':'北京',
        'pageIndex': '1',
        'pageSize': '10'
    }
    #发起post请求，获取响应对象
    response = requests.get(url=url,headers=headers,data=data)

    #获取响应内容：响应内容为json串
    print(response.text)

```

### 需求：爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据

```
import requests
from fake_useragent import UserAgent

ua = UserAgent(use_cache_server=False,verify_ssl=False).random
headers = {
    'User-Agent':ua
}

url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
pageNum = 3
for page in range(3,5):
    data = {
        'on': 'true',
        'page': str(page),
        'pageSize': '15',
        'productName':'',
        'conditionType': '1',
        'applyname':'',
        'applysn':''
    }
    json_text = requests.post(url=url,data=data,headers=headers).json()
    all_id_list = []
    for dict in json_text['list']:
        id = dict['ID']#用于二级页面数据获取
        #下列详情信息可以在二级页面中获取
        # name = dict['EPS_NAME']
        # product = dict['PRODUCT_SN']
        # man_name = dict['QF_MANAGER_NAME']
        # d1 = dict['XC_DATE']
        # d2 = dict['XK_DATE']
        all_id_list.append(id)
    #该url是一个ajax的post请求
    post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in  all_id_list:
        post_data = {
            'id':id
        }
        response = requests.post(url=post_url,data=post_data,headers=headers)
        #该请求响应回来的数据有两个，一个是基于text，一个是基于json的，所以可以根据content-type,来获取指定的响应数据
        if response.headers['Content-Type'] == 'application/json;charset=UTF-8':
            #print(response.json())
            #进行json解析
            json_text = response.json()
            print(json_text['businessPerson'])

```

### 练手习题

爬取网络上的任意图片数据 爬取百度翻译的翻译结果数据值 爬取百度贴吧指定页码下的数据值
