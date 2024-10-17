
--- 
title:  Python中Requests模块的使用 
tags: []
categories: [] 

---
        Requests模块是Python中的一款第三方包，也是基于在Python中的urllib上编写的。它的作用是模拟浏览器进行网络请求。

#### Requests的特点
- 功能强大-  简单便捷- 效率高
####  Requests的安装

        由于它是第三方包，所以需要进行安装。它的安装方式和其他包的安装方式是一致的，使用pip命令安装

>  
 pip install requests 


#### Requests的使用

Requests的使用主要分为三步：
1. 找到需要请求的URL地址1. 模拟浏览器发起请求1.  获取相应数据
#### Requests属性/方法介绍
|delete(**url**, **args**)|发送 DELETE 请求到指定 url
|get(**url**, **params, args**)|发送 GET 请求到指定 url
|head(**url**, **args**)|发送 HEAD 请求到指定 url
|patch(**url**, **data, args**)|发送 PATCH 请求到指定 url
|post(**url**, **data, json, args**)|发送 POST 请求到指定 url
|put(**url**, **data, args**)|发送 PUT 请求到指定 url
|request(**method**, **url**, **args**)|向指定的 url 发送指定的请求方法

#### Requests实例

        实例：使用Requests模拟请求获取豆瓣电影排名前100的电影内容

**1. 找到豆瓣中分类为剧情的排行榜地址。**

        这里我们使用开发者工具找到url地址为下图所示<img alt="" height="173" src="https://img-blog.csdnimg.cn/798d582eacbf4746a58d5ac25ba15585.png" width="838">

**2. 模拟浏览器发起请求**

        找到请求头部的用户标识，User-Agent

<img alt="" height="139" src="https://img-blog.csdnimg.cn/8483e4522f9d4727a49196c96c7601a7.png" width="864">

        找到请求的参数 

<img alt="" height="159" src="https://img-blog.csdnimg.cn/ff2c5a1df6e047e49dcd68270c3469ed.png" width="521">

** 3. 使用代码模拟发起请求并获取数据**

>  
 <pre>import json
import requests

# 需要请求的URL地址
url = "https://movie.douban.com/j/chart/top_list"
# 模拟请求头部
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# 数据按分页请求
for i in range(5):
    print("获取第%d页数据\n" % i)
    # 模拟请求的参数
    param = {
        'type': '11',
        'interval_id': '100:90',
        'action': '',
        'start': i*20,
        'limit': '20'
    }
    # 模拟发送请求
    rq = requests.get(url=url, params=param, headers=header)
    # 获取请求结果并存入文件中
    with open('result.html', 'a', encoding='utf-8') as f:
        list_result = rq.json()
        f.write(f"第{i}页数据\n"+json.dumps(list_result, ensure_ascii=False)+'\n')</pre> 


 


