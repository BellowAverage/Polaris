
--- 
title:  Python爬虫实战（七）——批量下载4K高清小姐姐图片（附上完整源码） 
tags: []
categories: [] 

---


#### 文章目录
- - - - - <ul><li>- - - - - 


## 一、爬取目标

<mark>本次爬取的目标是 **又又又一个** 某网站4K高清小姐姐图片：</mark>

<img src="https://img-blog.csdnimg.cn/direct/558037c1db524dc4bb3338e626a2cd85.png" alt="在这里插入图片描述">

## 二、实现效果

实现批量下载指定关键词的图片，存放到指定文件夹中：

<img src="https://img-blog.csdnimg.cn/direct/5e2960b90184485a8adbc7a002a3d175.png" alt="在这里插入图片描述">

## 三、准备工作

Python：3.10

编辑器：PyCharm

第三方模块，自行安装：

```
pip install requests # 网页数据爬取
pip install lxml # 提取网页数据

```

## 四、代码实战

### 4.1 导入模块

```
import requests  # python基础爬虫库
from lxml import etree  # 可以将网页转换为Elements对象
import time  # 防止爬取过快可以睡眠一秒
import os # 创建文件

```

### 4.2 设置翻页

首先我们来分析一下网站的翻页，一共有10页： <img src="https://img-blog.csdnimg.cn/direct/b9d7e435b4694a0bbf976d86b228d19e.png" alt="在这里插入图片描述">

第一页链接：

```
https://www.moyublog.com/95-2-2-0.html

```

第二页链接：

```
https://www.moyublog.com/95-2-2-1.html

```

第三页链接：

```
https://www.moyublog.com/95-2-2-2.html

```

可以看出每页只有`95-2-2-`后面从第二页开始依次加上`1`，所以用循环来构造所有网页链接：

```
if __name__ == '__main__':
    # 页码
    page_number = 10
    # 循环构建每页的链接
    for i in range(0,page_number+1):
        # 页数拼接
        url = f'https://www.moyublog.com/95-2-2-{<!-- -->i}.html'

```

### 4.3 获取图片链接

可以看到所有图片url都在 ul标签 &gt; li标签 &gt; a标签 &gt; img标签下：

<img src="https://img-blog.csdnimg.cn/direct/3584d4a404fc464990f87c0d1e9d52da.png" alt="在这里插入图片描述">

我们创建一个`get_imgurl_list(url)`函数传入网页链接获取 网页源码，用xpath定位到每个图片的链接：

```
def get_imgurl_list(url,imgurl_list):
    """获取图片链接"""
    # 请求头
    headers = {<!-- -->
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    # 发送请求
    response = requests.get(url=url, headers=headers)
    # 获取网页源码
    html_str = response.text
    # 将html字符串转换为etree对象方便后面使用xpath进行解析
    html_data = etree.HTML(html_str)
    # 利用xpath取到所有的li标签
    li_list = html_data.xpath("//ul[@class='clearfix']/li")
    # 打印一下li标签个数看是否和一页的电影个数对得上
    print(len(li_list))  # 输出20，没有问题
    for li in li_list:
        imgurl = li.xpath(".//a/img/@data-original")[0]
        print(imgurl)
        # 写入列表
        imgurl_list.append(imgurl)

```

运行结果： <img src="https://img-blog.csdnimg.cn/direct/d17d195669364895b81f3138ccd48db0.png" alt="在这里插入图片描述">

点开一个图片链接看看，OK没问题：

<img src="https://img-blog.csdnimg.cn/direct/9a6f4a688a9c4679b148b00e79ce1b2c.png" alt="在这里插入图片描述">

### 4.4 下载图片

图片链接有了，定义一个`get_down_img(img_url_list)`函数，传入图片链接列表，然后遍历列表，将所有图片下载到指定文件夹：

```
def get_down_img(imgurl_list):
    # 在当前路径下生成存储图片的文件夹
    os.mkdir("小姐姐")
    # 定义图片编号
    n = 0
    for img_url in imgurl_list:
        headers = {<!-- -->
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
        # 每次发送请求，获取图片
        img_data = requests.get(url=img_url, headers=headers).content
        # 拼接图片存放地址和名字
        img_path = './小姐姐/' + str(n) + '.jpg'
        # 将图片写入指定位置
        with open(img_path, 'wb') as f:
            f.write(img_data)
        # 图片编号递增
        n = n + 1

```

### 4.5 调用主函数

这里我们可以设置需要爬取的页码：

```
if __name__ == '__main__':
    page_number = 10 # 爬取页数
    imgurl_list = [] # 存放图片链接
    # 1. 循环构建每页的链接
    for i in range(0,page_number+1):
        # 页数拼接
        url = f'https://www.moyublog.com/95-2-2-{<!-- -->i}.html'
        print(url)
        # 2. 获取图片链接
        get_imgurl_list(url,imgurl_list)
    # 3. 下载图片
    get_down_img(imgurl_list)

```

### 4.6 完整源码

完整源码如下：

```
import requests  # python基础爬虫库
from lxml import etree  # 可以将网页转换为Elements对象
import time  # 防止爬取过快可以睡眠一秒
import os


def get_imgurl_list(url,imgurl_list):
    """获取图片链接"""
    # 请求头
    headers = {<!-- -->
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    # 发送请求
    response = requests.get(url=url, headers=headers)
    # 获取网页源码
    html_str = response.text
    # 将html字符串转换为etree对象方便后面使用xpath进行解析
    html_data = etree.HTML(html_str)
    # 利用xpath取到所有的li标签
    li_list = html_data.xpath("//ul[@class='clearfix']/li")
    # 打印一下li标签个数看是否和一页的电影个数对得上
    print(len(li_list))  # 输出20，没有问题
    for li in li_list:
        imgurl = li.xpath(".//a/img/@data-original")[0]
        print(imgurl)
        # 写入列表
        imgurl_list.append(imgurl)


def get_down_img(imgurl_list):
    # 在当前路径下生成存储图片的文件夹
    os.mkdir("小姐姐")
    # 定义图片编号
    n = 0
    for img_url in imgurl_list:
        headers = {<!-- -->
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
 
        # 每次发送请求，获取图片
        img_data = requests.get(url=img_url, headers=headers).content #
        # 拼接图片存放地址和名字
        img_path = './小姐姐/' + str(n) + '.jpg'
        # 将图片写入指定位置
        with open(img_path, 'wb') as f:
            f.write(img_data)
        # 图片编号递增
        n = n + 1


if __name__ == '__main__':
    page_number = 10 # 爬取页数
    imgurl_list = [] # 存放图片链接
    # 1. 循环构建每页的链接
    for i in range(0,page_number+1):
        # 页数拼接
        url = f'https://www.moyublog.com/95-2-2-{<!-- -->i}.html'
        print(url)
        # 2. 获取图片链接
        get_imgurl_list(url,imgurl_list)
    # 3. 下载图片
    get_down_img(imgurl_list)


```

运行结果：

<img src="https://img-blog.csdnimg.cn/direct/684a97089d624a60b90b75af0d92039e.png" alt="在这里插入图片描述">

下载成功了没有报错！！！
