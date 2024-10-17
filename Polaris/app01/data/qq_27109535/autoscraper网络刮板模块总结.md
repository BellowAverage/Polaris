
--- 
title:  autoscraper网络刮板模块总结 
tags: []
categories: [] 

---
### autoscraper网络刮板模块总结
- requests——最普遍使用的爬虫库- you_get——最受欢迎的爬虫库- autoscraper——最智能的爬虫库- urllib——最底层的爬虫库- Httpx ——支持异步与Http2.0协议的爬虫库
### 1. 安装

```
# 首先安装autoscraper，目前只支持python3 
 
# 使用 pip 从 git 仓库安装最新版本 
# pip install git+https://github.com/alirezamika/autoscraper.git 
 
# 下载源码安装 
# python setup.py install 
 
# 从 PyPI 安装（推荐） 
# pip install autoscraper 


```

实例1

```
from autoscraper import AutoScraper

url = 'https://stackoverflow.com/questions/2081586/web-scraping-with-python'

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ["What are metaclasses in Python?"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
for i in result:
    print(i)

```

<img src="https://img-blog.csdnimg.cn/7fade80e5ad54f04bb7c898532beb046.png" alt="在这里插入图片描述"> 案例2

```
# -*- coding: utf-8 -*-
# 单个信息抓取

from autoscraper import AutoScraper

# 抓取的网址
url = 'https://bj.lianjia.com/ershoufang/pg2/'

# 输入你想抓取的标题信息（我们先随便写一个标题）
wanted_list = ["2室1厅 | 65.42平米 | 南 北 | 简装 | 中楼层(共6层) | 1990年建 | 板楼"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
for i in result:
    print(i)

```

<img src="https://img-blog.csdnimg.cn/07cc10509f324b7bb1933833bc2e0b2b.png" alt="在这里插入图片描述">

```
# -*- coding: utf-8 -*-
from autoscraper import AutoScraper


url = 'https://bj.lianjia.com/ershoufang/'

wanted_list = {<!-- -->
    "title": ["世纪星城 带电梯复式 楼上没算面积 适合三代人居住"],
    "topic": ["4室2厅 | 92.2平米 | 南 北 | 简装 | 高楼层(共10层) | 2005年建 | 板楼"],
    "times": ["17人关注 / 6天以前发布"]
}

scraper = AutoScraper()
scraper.build(url=url, wanted_dict=wanted_list)
result = scraper.get_result_similar(url=url, grouped=True)
print(result)
result = scraper.get_result_similar(url="https://bj.lianjia.com/ershoufang/pg3/", grouped=True)
print(result)

# for i in result['title']:
#     print(i)

```

<img src="https://img-blog.csdnimg.cn/75ccc5757a5d4d6cbf589697f2f77c27.png" alt="在这里插入图片描述">

```
# -*- coding: utf-8 -*-
from autoscraper import AutoScraper


url = 'https://bj.lianjia.com/ershoufang/'

wanted_list = {<!-- -->
    "title": ["世纪星城 带电梯复式 楼上没算面积 适合三代人居住"],
    "topic": ["4室2厅 | 92.2平米 | 南 北 | 简装 | 高楼层(共10层) | 2005年建 | 板楼"],
    "times": ["17人关注 / 6天以前发布"]
}

scraper = AutoScraper()
scraper.build(url=url, wanted_dict=wanted_list)
result = scraper.get_result_similar(url=url, grouped=True)
print(result)

import pandas as pd

df = pd.DataFrame()

# 批量抓取二手房信息

for n in range(1, 10):
    url = f'https://bj.lianjia.com/ershoufang/pg{<!-- -->n}'

    print(url)
    result = scraper.get_result_similar(url=url, group_by_alias=True)

    df = pd.concat([df, pd.DataFrame(result)])
    print(result)


```

<img src="https://img-blog.csdnimg.cn/4c7a2aecb432476c897604893d40daa9.png" alt="在这里插入图片描述">
