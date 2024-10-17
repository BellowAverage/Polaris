
--- 
title:  Python爬虫实战（五）：根据关键字爬取某度图片批量下载到本地（附上完整源码） 
tags: []
categories: [] 

---


#### 文章目录
- - - - - <ul><li>- - - - - - - - 


## 一、爬取目标

在日常生活或工作中，我们经常需要使用某度图片来搜索相关的图片资源。然而，如果需要批量获取特定关键字的图片资源，手动一个个下载显然是非常繁琐且耗时的。因此，本文将介绍如何使用Python爬虫技术批量话下载图片：

<img src="https://img-blog.csdnimg.cn/img_convert/0fdee642a95ed548571e87a36e74700d.png" alt="">

## 二、实现效果

实现批量下载指定关键词的图片，存放到指定文件夹中：

<img src="https://img-blog.csdnimg.cn/img_convert/6655ab2a8f85e93d3d328a8bc135f130.png" alt="">

## 三、准备工作

Python：3.10

编辑器：PyCharm

第三方模块，自行安装：

```
pip install requests # 网页数据爬取
pip install lxml # 提取网页数据

```

## 四、使用代理

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

## 五、爬虫实战

### 5.1 导入模块

```
import requests # 爬虫必备
import time # 限制爬虫速度
import os # 新建指定存储文件夹

```

### 5.2 分析网页

我们右击网页点击插件，可以在network中找到图片链接存储的接口：

<img src="https://img-blog.csdnimg.cn/img_convert/b2fc2aa2691c888dd148489644c795f3.png" alt="">

接下来只需要去构造参数获取接口中的数据，发送请求即可：

<img src="https://img-blog.csdnimg.cn/img_convert/75f91e4c313ab40713021ff3599c0247.png" alt="">

### 5.3 获取图片链接

这里我们创建一个`get_img_url(keyword)`函数传入关键词，通过添加请求头和params表单构造接口参数，发送请求获取图片链接：

```
def get_img_url(keyword):
    """发送请求，获取接口中的数据"""
    # 接口链接
    url = 'https://image.baidu.com/search/acjson?'
    # 请求头模拟浏览器
    headers = {<!-- -->'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    # 构造网页的params表单
    params = {<!-- -->
        'tn': 'resultjson_com',
        'logid': '6918515619491695441',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord': f'{<!-- -->keyword}',
        'word': f'{<!-- -->keyword}',
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z': '',
        'ic': '',
        'hd': '',
        'latest': '',
        'copyright': '',
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc': '',
        'nc': '1',
        'fr': '',
        'expermode': '',
        'force': '',
        'cg': 'girl',
        'pn': 1,
        'rn': '30',
        'gsm': '1e',
    }
    # 携带请求头和params表达发送请求
    response  = requests.get(url=url, headers=headers, params=params)
    # 设置编码格式
    response.encoding = 'utf-8'
    # 转换为json
    json_dict = response.json()
    # 定位到30个图片上一层
    data_list = json_dict['data']
    # 删除列表中最后一个空值
    del data_list[-1]
    # 用于存储图片链接的列表
    img_url_list = []
    for i in data_list:
        img_url = i['thumbURL']
        # 打印一下图片链接
        print(img_url)
        img_url_list.append(img_url)
    # 返回图片列表
    return img_url_list

```

运行结果，控制台打印获取的图片链接：

<img src="https://img-blog.csdnimg.cn/img_convert/ab84181da806cf0bb3b1f61741fe3b12.png" alt="">

我们点开一个图片链接查看，的确没问题：

<img src="https://img-blog.csdnimg.cn/img_convert/55157ae2f729cecfa7180842014c5d8c.png" alt="">

### 5.4 获取代理

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

### 5.5 下载图片

图片链接有了，代理IP也有了，下面我们就可以下载图片。定义一个`get_down_img(img_url_list)`函数，传入图片链接列表，然后遍历列表，每下载一个图片切换一次代理，将所有图片下载到指定文件夹：

```
def get_down_img(img_url_list):
    # 在当前路径下生成存储图片的文件夹
    os.mkdir("小姐姐")
    # 定义图片编号
    n = 0
    for img_url in img_url_list:
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

### 5.6 调用主函数

主要步骤为明确我们需要获取的关键名，获取指定关键词的图片链接，下载图片到指定位置

```
if __name__ == '__main__':
    # 1. 修改关键词
    keyword = '小姐姐'
    # 2. 获取指定关键词的图片链接
    img_url_list = get_img_url(keyword)
    # 3. 下载图片到指定位置
    get_down_img(img_url_list)

```

### 5.7 完整代码

下面完整代码<mark>只需要修改关键词和`get_ip()`函数中的代理IP接口链接（注意：看4.2教程换成自己的API链接）</mark>

```
import requests # 爬虫必备
import time # 限制爬虫速度
import os # 新建指定存储文件夹


def get_ip():
    """获取代理IP"""
    # （注意：下面代理URL，看4.2教程换成自己的API链接）：
    url = "这里放你自己代理IP的API链接"
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



def get_img_url(keyword):
    """发送请求，获取接口中的数据"""
    # 接口链接
    url = 'https://image.baidu.com/search/acjson?'
    # 请求头模拟浏览器
    headers = {<!-- -->'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    # 构造网页的params表单
    params = {<!-- -->
        'tn': 'resultjson_com',
        'logid': '6918515619491695441',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord': f'{<!-- -->keyword}',
        'word': f'{<!-- -->keyword}',
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z': '',
        'ic': '',
        'hd': '',
        'latest': '',
        'copyright': '',
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc': '',
        'nc': '1',
        'fr': '',
        'expermode': '',
        'force': '',
        'cg': 'girl',
        'pn': 1,
        'rn': '30',
        'gsm': '1e',
    }
    # 携带请求头和params表达发送请求
    response  = requests.get(url=url, headers=headers, params=params)
    # 设置编码格式
    response.encoding = 'utf-8'
    # 转换为json
    json_dict = response.json()
    # 定位到30个图片上一层
    data_list = json_dict['data']
    # 删除列表中最后一个空值
    del data_list[-1]
    # 用于存储图片链接的列表
    img_url_list = []
    for i in data_list:
        img_url = i['thumbURL']
        # 打印一下图片链接
        print(img_url)
        img_url_list.append(img_url)
    # 返回图片列表
    return img_url_list


def get_down_img(img_url_list):
    # 在当前路径下生成存储图片的文件夹
    os.mkdir("小姐姐")
    # 定义图片编号
    n = 0
    for img_url in img_url_list:
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
    # 1. 修改关键词
    keyword = '小姐姐'
    # 2. 获取指定关键词的图片链接
    img_url_list = get_img_url(keyword)
    # 3. 下载图片到指定位置
    get_down_img(img_url_list)

```

运行结果，生成文件夹，所有图片下载到指定文件夹中：

<img src="https://img-blog.csdnimg.cn/img_convert/cd6e5f3c1b3929896fb168093f0e5a5d.png" alt="">

## 六、总结

代理IP对于爬虫是密不可分的，代理IP可以安全采集公开数据信息，有需要代理IP的小伙伴可以试试巨量家的代理IP：
