
--- 
title:  python 多进程存为csv 
tags: []
categories: [] 

---
python 多进程存为csv案例，直接在项目中应用

```
import requests
from fake_useragent import UserAgent
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import time


# 爬取一页数据
def download_one_page(data: dict):
    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    headers = {<!-- -->
        'user-agent': UserAgent().random,
        'referer': 'http://www.xinfadi.com.cn/priceDetail.html'
    }

    resp = requests.post(url=url, headers=headers, data=data)
    data_list = resp.json().get('list')
    # 保存数据
    with open('北京新发地.csv', 'a', encoding='utf-8') as fp:
        for elem in tqdm(data_list, desc=f'下载第 {<!-- -->data["current"]} 页数据 当前状告码:{<!-- -->resp.status_code}', ascii=True):
            info = (elem['prodCat'], elem['prodPcat'], elem['prodName'], elem['lowPrice'], elem['avgPrice'],
                    elem['highPrice'], elem['specInfo']
                    , elem['place'], elem['unitInfo'], elem['pubDate'])
            fp.write(','.join(info) + '\n')


def download_pages(page_start: int, page_end: int, page_limit: int = 20):
    fp = open('北京新发地.csv', 'w', encoding='utf-8')
    title = ['一级分类', '二级分类', '品名', '最低价', '平均价', '最高价', '规格', '产地', '单位', '发布日期']
    fp.write(','.join(title) + '\n')
    fp.close()
    with ThreadPoolExecutor(2048) as t:
        for i in range(page_start, page_end + 1):
            data = {<!-- -->
                'limit': f'{<!-- -->page_limit}',
                'current': f'{<!-- -->i}',
                'pubDateStartTime': '',
                'pubDateEndTime': '',
                'prodPcatid': '',
                'prodCatid': '',
                'prodName': ''
            }
            t.submit(download_one_page, data)


if __name__ == '__main__':
    start_time = time.time()
    download_pages(page_start=1, page_end=100, page_limit=20)
    end_time = time.time()
    print(f'总耗时{<!-- -->end_time - start_time}s')



```

<img src="https://img-blog.csdnimg.cn/9acb8cd69dbd44719c207456e93d5539.png" alt="在这里插入图片描述">
