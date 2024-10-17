
--- 
title:  Python爬虫实战（六）——使用代理IP批量下载高清小姐姐图片（附上完整源码） 
tags: []
categories: [] 

---


#### 文章目录
- - - - - <ul><li>- - - - - - - - 


## 一、爬取目标

本次爬取的目标是某网站4K高清小姐姐图片：

<img src="https://img-blog.csdnimg.cn/img_convert/96b421f001a26c4a4e448c3825e495b1.png" alt="">

## 二、实现效果

实现批量下载指定关键词的图片，存放到指定文件夹中：

<img src="https://img-blog.csdnimg.cn/img_convert/2528846ab39cab97459d18c9d7917340.png" alt="">

## 三、准备工作

Python：3.10

编辑器：PyCharm

第三方模块，自行安装：

```
pip install requests # 网页数据爬取
pip install lxml # 提取网页数据

```

## 四、代理IP

### 4.1 使用代理的好处？

**使用代理IP可以带来以下好处：**
1. 匿名保护，保护隐私安全1. 安全采集公开数据信息1. 分散访问压力，提高爬取效率和稳定性。1. 收集不同地区或代理服务器上的数据，用于数据分析和对比。
博主经常写爬虫代码使用的是巨量IP家的高匿名代理IP，每天有1000个免费IP：

<img src="https://img-blog.csdnimg.cn/img_convert/a036003c0acbc7069e8af1903b7aa5a2.png" alt="">

### 4.2 获取免费代理

1、打开巨量IP官网：

2、输入账号信息进行注册：

<img src="https://img-blog.csdnimg.cn/img_convert/1a78180a99d94b32a93513879ce32c84.png" alt="">

3、这里需要进行实名认证，如果不会的可以看：：

<img src="https://img-blog.csdnimg.cn/img_convert/e9df43c2dbf8c4d990e07924851b6591.png" alt="">

4、进入会员中心，点击领取今日免费IP：

<img src="https://img-blog.csdnimg.cn/img_convert/ebb66eac357f612cbcd152b8de290010.png" alt="">

5、详细步骤看官方的教程文档：，领取后如下图：

<img src="https://img-blog.csdnimg.cn/img_convert/cfb95fed6a60576255b7baf28d359f95.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/8427e54f6ff911ccffcee3c127c922da.png" alt="">

6、点击产品管理》动态代理（包时），可以看到我们刚才领取到的免费IP信息：

<img src="https://img-blog.csdnimg.cn/img_convert/af992439983a07d18fa5ca15502fd9d3.png" alt="">

7、将自己电脑的IP添加为白名单能获取代理IP，点击授权信息：

<img src="https://img-blog.csdnimg.cn/img_convert/35068aecd85d8f000dc5d8ebfb5bd364.png" alt="">

8、依次点击修改授权》快速添加》确定

<img src="https://img-blog.csdnimg.cn/img_convert/edd1ca9185001a7e7cf3b4b0dc0ad389.png" alt="">

9、添加完成后，点击生成提取链接：

<img src="https://img-blog.csdnimg.cn/img_convert/92854a09f6f27d2a458d88bd254591f2.png" alt="">

10、设置每次提取的数量，点击生成链接，并复制链接：

<img src="https://img-blog.csdnimg.cn/img_convert/32d8b42cd7311b15e28d7eee50909e86.png" alt="">

11、将复制链接，复制到地址栏就可以看到我们获取到的代理IP了：

<img src="https://img-blog.csdnimg.cn/img_convert/f244cadc42adea41f9f4237f1575cefe.png" alt="">

### 4.3 获取代理

获取到图片链接后我们需要再次发送请求去下载图片，由于请求量一般会很大所以需要用到代理IP。上面我们已经手动获取到了代理IP，下面来看Python如何挂上代理IP发送请求：

1、通过爬虫去获取API接口的里面的代理IP（**注意：下面代理URL，看4.2教程换成自己的API链接**）：

```
import requests
import time
import random


def get_ip():
    url = "这里放你自己的API链接"
    while 1:
        try:
            r = requests.get(url, timeout=10)
        except:
            continue

        ip = r.text.strip()
        if '请求过于频繁' in ip:
            print('IP请求频繁')
            time.sleep(1)
            continue
        break
    proxies = {<!-- -->
        'https': '%s' % ip
    }

    return proxies



if __name__ == '__main__':
    proxies = get_ip()
    print(proxies)

```

运行结果，可以看到返回了接口中的代理IP：

<img src="https://img-blog.csdnimg.cn/img_convert/2936ed2b3b96a3d17897856c29861e9b.png" alt="">

2、接下来我们写爬虫代理的时候就可以挂上代理IP去发送请求了，只需要将`proxies`当成参数传给`requests.get`函数去请求其他网址：

```
requests.get(url, headers=headers, proxies=proxies) 

```

## 五、代理实战

### 5.1 导入模块

```
import requests  # python基础爬虫库
from lxml import etree  # 可以将网页转换为Elements对象
import time  # 防止爬取过快可以睡眠一秒
import os # 创建文件

```

### 5.2 设置翻页

首先我们来分析一下网站的翻页，一共有62页：

<img src="https://img-blog.csdnimg.cn/img_convert/933e21f5b217b632088f3221bafde8c0.png" alt="">

第一页链接：

```
https://pic.netbian.com/4kmeinv/index.html

```

第二页链接：

```
https://pic.netbian.com/4kmeinv/index_2.html

```

第三页链接：

```
https://pic.netbian.com/4kmeinv/index_3.html

```

可以看出每页只有`index`后面从第二页开始依次加上`_页码`，所以用循环来构造所有网页链接：

```
if __name__ == '__main__':
    # 页码
    page_number = 1
    # 循环构建每页的链接
    for i in range(1,page_number+1):
        # 第一页固定，后面页数拼接
        if i ==1:
            url = 'https://pic.netbian.com/4kmeinv/index.html'
        else:
            url = f'https://pic.netbian.com/4kmeinv/index_{<!-- -->i}.html'

```

### 5.3 获取图片链接

可以看到所有图片url都在 ul标签 &gt; a标签 &gt; img标签下：

<img src="https://img-blog.csdnimg.cn/img_convert/6b4d400d0870f4680403ec0ed59e7e69.png" alt="">

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
        imgurl = li.xpath(".//a/img/@src")[0]
        # 拼接url
        imgurl = 'https://pic.netbian.com' +imgurl
        print(imgurl)
        # 写入列表
        imgurl_list.append(imgurl)

```

运行结果：

<img src="https://img-blog.csdnimg.cn/img_convert/f7107ede6a0d88f27775915f23e06381.png" alt="">

点开一个图片链接看看：

<img src="https://img-blog.csdnimg.cn/img_convert/8d215e4cdd324b78796e5a2814b05e8b.png" alt="">

OK没问题!!!

### 5.4 下载图片

图片链接有了，代理IP也有了，下面我们就可以下载图片。定义一个`get_down_img(img_url_list)`函数，传入图片链接列表，然后遍历列表，每下载一个图片切换一次代理，将所有图片下载到指定文件夹：

```
def get_down_img(imgurl_list):
    # 在当前路径下生成存储图片的文件夹
    os.mkdir("小姐姐")
    # 定义图片编号
    n = 0
    for img_url in imgurl_list:
        headers = {<!-- -->
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
        # 调用get_ip函数，获取代理IP
        proxies = get_ip()
        # 每次发送请求换代理IP，获取图片，防止被封
        img_data = requests.get(url=img_url, headers=headers, proxies=proxies).content
        # 拼接图片存放地址和名字
        img_path = './小姐姐/' + str(n) + '.jpg'
        # 将图片写入指定位置
        with open(img_path, 'wb') as f:
            f.write(img_data)
        # 图片编号递增
        n = n + 1

```

### 5.5 调用主函数

这里我们可以设置需要爬取的页码：

```
if __name__ == '__main__':
    # 1. 设置获取的页数
    page_number = 63
    imgurl_list = [] # 用于存储所有的图片链接
    # 2. 循环构建每页的链接
    for i in range(1,page_number+1):
        # 第一页固定，后面页数拼接
        if i ==1:
            url = 'https://pic.netbian.com/4kmeinv/index.html'
        else:
            url = f'https://pic.netbian.com/4kmeinv/index_{<!-- -->i}.html'
        # 3. 获取图片链接
        get_imgurl_list(url,imgurl_list)
    # 4. 下载图片
    get_down_img(imgurl_list)

```

### 5.6 完整源码

<mark>**注意：下面代理URL，看4.2教程换成自己的API链接：**</mark>

```
import requests  # python基础爬虫库
from lxml import etree  # 可以将网页转换为Elements对象
import time  # 防止爬取过快可以睡眠一秒
import os


def get_ip():
    url = "这里放你自己的API链接"
    while 1:
        try:
            r = requests.get(url, timeout=10)
        except:
            continue

        ip = r.text.strip()
        if '请求过于频繁' in ip:
            print('IP请求频繁')
            time.sleep(1)
            continue
        break
    proxies = {<!-- -->
        'https': '%s' % ip
    }

    return proxies


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
        imgurl = li.xpath(".//a/img/@src")[0]
        # 拼接url
        imgurl = 'https://pic.netbian.com' +imgurl
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
        # 调用get_ip函数，获取代理IP
        proxies = get_ip()
        # 每次发送请求换代理IP，获取图片，防止被封
        img_data = requests.get(url=img_url, headers=headers, proxies=proxies).content
        # 拼接图片存放地址和名字
        img_path = './小姐姐/' + str(n) + '.jpg'
        # 将图片写入指定位置
        with open(img_path, 'wb') as f:
            f.write(img_data)
        # 图片编号递增
        n = n + 1

if __name__ == '__main__':
    # 1. 设置获取的页数
    page_number = 50
    imgurl_list = [] # 用于存储所有的图片链接
    # 2. 循环构建每页的链接
    for i in range(1,page_number+1):
        # 第一页固定，后面页数拼接
        if i ==1:
            url = 'https://pic.netbian.com/4kmeinv/index.html'
        else:
            url = f'https://pic.netbian.com/4kmeinv/index_{<!-- -->i}.html'
        # 3. 获取图片链接
        get_imgurl_list(url,imgurl_list)
    # 4. 下载图片
    get_down_img(imgurl_list)

```

运行结果：

<img src="https://img-blog.csdnimg.cn/img_convert/2d1d22c1ac907c57086ea888464865bf.png" alt="">

下载成功了没有报错，代理IP的质量还是不错的！！！
