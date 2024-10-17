
--- 
title:  Python爬虫实战（四）：利用代理IP爬取某瓣电影排行榜并写入Excel（附上完整源码） 
tags: []
categories: [] 

---
## 1. 爬虫和代理IP的关系

爬虫和代理IP之间的关系密切，代理IP可以安全采集公开数据信息，保证爬虫的持续运行和数据采集。 <img src="https://img-blog.csdnimg.cn/img_convert/21ce4c210d7165b67dcbad079d52cf6e.png" alt="">

## 2. 使用代理IP的好处

使用代理IP可以带来以下好处：
- 匿名保护，保护隐私安全- 安全采集公开数据信息- 分散访问压力，提高爬取效率和稳定性。- 收集不同地区或代理服务器上的数据，用于数据分析和对比。
然而，使用代理IP也存在一些挑战和注意事项：
-  IP安全性低，无法高效采集公开数据。 -  使用代理IP可能增加网络请求的延迟和复杂性，需要合理配置和调整爬虫程序。 -  使用代理IP需要遵守相关法律法规和目标网站的使用规则，不得进行非法活动或滥用代理IP服务。 
博主最近使用的是亮数据家的代理IP，IP质量很高个人感觉还不错：

<img src="https://img-blog.csdnimg.cn/img_convert/4e6dde300a16cb1b190ae04cd603482c.png" alt="">

## 3. 爬取目标

这次爬虫实战的目标是某瓣电影Top250排行榜，爬取的字段：排名、电影名、评分、评价人数、制片国家、电影类型、上映时间、主演、影片链接

<img src="https://img-blog.csdnimg.cn/img_convert/609f764117e32bac65f2ebf24237a26d.png" alt="">

预期效果写入Excel： <img src="https://img-blog.csdnimg.cn/img_convert/df0479d15801179524b430c3e61e64f3.png" alt="">

## 4. 准备工作

Python：3.10

编辑器：PyCharm

第三方模块，自行安装：

```
pip install requests # 网页数据爬取
pip install pandas # 数据处理
pip install xlwt # 写入Excel
pip install lxml # 提取网页数据

```

## 5. 爬虫实现

### 5.1 获取代理IP

1、打开亮数据的官网，点击立刻使用：

<img src="https://img-blog.csdnimg.cn/img_convert/e0e938d9115f8f9cb4cbaafa9211aa03.png" alt="">

2、输入账号密码注册账号：

<img src="https://img-blog.csdnimg.cn/img_convert/b109e5493f3a1298562e33e586674f68.png" alt="">

3、注册后以后点击查看代理IP产品：

<img src="https://img-blog.csdnimg.cn/img_convert/a59680554637a76a2ccdd01559f71087.png" alt="">

4、选择适合自己ide产品，如果你使用公司邮件注册，可以找客服开通免费试用：

<img src="https://img-blog.csdnimg.cn/img_convert/07333992ea7c909296151cadca3876ae.png" alt="">

5、获取代理IP后通过proxies参数添加代理发送请求，案例代码：

```
proxies = {
  "http": "http://IP地址:端口号",   # http型
  "https": "https://IP地址:端口号"   # https型
}
response = requests.get(url,headers=headers,proxies=proxies)

```

### 5.2 导入模块

```
import re # 正则，用于提取字符串
import pandas as pd # pandas，用于写入Excel文件
import requests  # python基础爬虫库
from lxml import etree  # 可以将网页转换为Elements对象
import time  # 防止爬取过快可以睡眠一秒

```

### 5.3 设置翻页

首先我们来分析一下网站的翻页，一共有10页：

<img src="https://img-blog.csdnimg.cn/img_convert/c982db2b558571bae320006e266b3216.png" alt="">

第一页主页为：

```
https://movie.douban.com/top250?start=0&amp;filter=

```

第二页：

```
https://movie.douban.com/top250?start=25&amp;filter=

```

第三页：

```
https://movie.douban.com/top250?start=50&amp;filter=

```

可以看出每页只有`start=`后面的参数每次上涨25，所以用循环来构造10页网页链接：

```
def main():
    data_list = [] # 空列表用于存储每页获取到的数据
    for i in range(10):
        url = 'https://movie.douban.com/top250?start='+str(i*25)+'&amp;filter='

```

### 5.4 发送请求

这里我们创建一个`get_html_str(url)`函数传入网页url链接，通过添加请求头和代理IP发送请求获取网页源码（注意：这里代理IP这里需要看`5.1 获取代理IP`自己去获取，博主的已过期）：

```
def get_html_str(url):
    """发送请求，获取响应"""
    # 请求头模拟浏览器
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

    # 添加代理IP（这里代理IP这里需要看`5.1 获取代理IP`自己去获取，博主的已过期）
    proxies = {
        "http": "http://183.134.17.12:9181",
    }
    # 添加请求头和代理IP发送请求
    response = requests.get(url,headers=headers,proxies=proxies)
    # 获取网页源码
    html_str = response.content.decode()
    # 返回网页源码
    return html_str

```

### 5.5 提取数据

当我们拿到网页源码后，创建一个`get_data(html_str,data_list)`函数传入html_str也就是网页源码、data_list用于存储数据，就可以使用xpath开始解析数据了

1、分析网页结构，可以看到每一个电影都在ol标签下的li标签下：

<img src="https://img-blog.csdnimg.cn/img_convert/1f7b9cf9bd96afac42e35605e739d916.png" alt="">

2、然后我们看li标签的数据是否完整，可以看到我们需要的字段都有：

<img src="https://img-blog.csdnimg.cn/img_convert/23f3c3276193779bd55b2c7e56f8ebf1.png" alt="">

3、接下来开始写解析代码：

```
def get_data(html_str, data_list):
    """提取数据写入列表"""
    # 将html字符串转换为etree对象方便后面使用xpath进行解析
    html_data = etree.HTML(html_str)
    # 利用xpath取到所有的li标签
    li_list = html_data.xpath("//ol[@class='grid_view']/li")
    # 打印一下li标签个数看是否和一页的电影个数对得上
    print(len(li_list))  # 输出25，没有问题
    # 遍历li_list列表取到某一个电影的对象
    for li in li_list:
        # 用xpath获取每一个字段信息
        # 排名
        ranking = li.xpath(".//div[@class='pic']/em/text()")[0]
        # 电影名
        title = li.xpath(".//div[@class='hd']/a/span[1]/text()")[0]
        # 评分
        score = li.xpath(".//span[@class='rating_num']/text()")[0]
        # 评价人数
        evaluators_number = li.xpath(".//div[@class='star']/span[4]/text()")[0]
        evaluators_number = evaluators_number.replace('人评价', '')  # 将'人评价'替换为替换为空，更美观
        # 导演、主演
        str1 = li.xpath(".//div[@class='bd']/p[1]//text()")[0]
        # 利用正则提取导演名
        try:
            director = re.findall("导演: (.*?)主演", str1)[0]
            director = re.sub('\xa0', '', director)
        except:
            director = None
        # 利用正则提取主演
        try:
            performer = re.findall("主演: (.*)", str1)[0]
            performer = re.sub('\xa0', '', performer)
        except:
            performer = None
        # 上映时间、制片国家、电影类型都在这里标签下
        str2 = li.xpath(".//div[@class='bd']/p[1]//text()")[1]
        #
        try:
            # 通过斜杠进行分割
            str2_list = str2.split(' / ')
            # 年份
            year = re.sub('[\n ]', '', str2_list[0])
            # 制片国家
            country = str2_list[1]
            # 影片类型
            type = re.sub('[\n ]', '', str2_list[2])
        except:
            year = None
            country = None
            type = None
        url = li.xpath(".//div[@class='hd']/a/@href")[0]
        print({'排名': ranking, '电影名': title, '评分': score, '评价人数': evaluators_number, '导演': director,
               '主演': performer, '年份': year, '制片国家': country, '影片类型': type, '影片主页链接': url})
        data_list.append(
            {'排名': ranking, '电影名': title, '评分': score, '评价人数': evaluators_number, '导演': director,
             '主演': performer, '年份': year, '制片国家': country, '影片类型': type, '影片主页链接': url})

```

运行结果：

<img src="https://img-blog.csdnimg.cn/img_convert/44738a6141521fef16ae25ec8bebb112.png" alt="">

### 5.6 保存数据

当我们提取完数据以后就可以写入用pandas写入Excel表格中，创建`into_excel(data_list)`函数，将存储数据的data_list列表作为参数传入，然后用pandas的`to_excel`函数写入excel表格：

```
def into_excel(data_list):
    # 创建DataFrame对象
    df = pd.DataFrame(data_list)
    # 写入excel文件
    df.to_excel('电影Top250排行.xlsx')

```

### 5.7 调用主函数

第一步设置翻页，然后获取网页源码，接着提取数据，限制爬取的速度，最后写入Excel文件

```
def main():
    data_list = []  # 空列表用于存储每页获取到的数据
    # 1. 设置翻页
    for i in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&amp;filter='
        # 2. 获取网页源码
        html_str = get_html_str(url)
        # 3. 提取数据
        get_data(html_str, data_list)
        # 4. 限制爬取的速度
        time.sleep(5)
    # 5. 写入excel
    into_excel(data_list)

```

### 5.8 完整源码

这里附上完整源码（注意：`get_html_str(url)`函数中的代理IP这里需要看`5.1 获取代理IP`自己去获取，博主的已过期），然后直接运行程序即可：

```
import re # 正则，用于提取字符串
import pandas as pd # pandas，用于写入Excel文件
import requests  # python基础爬虫库
from lxml import etree  # 可以将网页转换为Elements对象
import time  # 防止爬取过快可以睡眠一秒


def get_html_str(url):
    """发送请求，获取响应"""
    # 请求头模拟浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

    # 添加代理IP（这里代理IP这里需要看`5.1 获取代理IP`自己去获取，博主的已过期）
    proxies = {
        "http": "http://183.134.17.12:9181",
    }
    # 添加请求头和代理IP发送请求
    response = requests.get(url, headers=headers, proxies=proxies)  #
    # 获取网页源码
    html_str = response.content.decode()
    # 返回网页源码
    return html_str


def get_data(html_str, data_list):
    """提取数据写入列表"""
    # 将html字符串转换为etree对象方便后面使用xpath进行解析
    html_data = etree.HTML(html_str)
    # 利用xpath取到所有的li标签
    li_list = html_data.xpath("//ol[@class='grid_view']/li")
    # 打印一下li标签个数看是否和一页的电影个数对得上
    print(len(li_list))  # 输出25，没有问题
    # 遍历li_list列表取到某一个电影的对象
    for li in li_list:
        # 用xpath获取每一个字段信息
        # 排名
        ranking = li.xpath(".//div[@class='pic']/em/text()")[0]
        # 电影名
        title = li.xpath(".//div[@class='hd']/a/span[1]/text()")[0]
        # 评分
        score = li.xpath(".//span[@class='rating_num']/text()")[0]
        # 评价人数
        evaluators_number = li.xpath(".//div[@class='star']/span[4]/text()")[0]
        evaluators_number = evaluators_number.replace('人评价', '')  # 将'人评价'替换为替换为空，更美观
        # 导演、主演
        str1 = li.xpath(".//div[@class='bd']/p[1]//text()")[0]
        # 利用正则提取导演名
        try:
            director = re.findall("导演: (.*?)主演", str1)[0]
            director = re.sub('\xa0', '', director)
        except:
            director = None
        # 利用正则提取主演
        try:
            performer = re.findall("主演: (.*)", str1)[0]
            performer = re.sub('\xa0', '', performer)
        except:
            performer = None
        # 上映时间、制片国家、电影类型都在这里标签下
        str2 = li.xpath(".//div[@class='bd']/p[1]//text()")[1]
        #
        try:
            # 通过斜杠进行分割
            str2_list = str2.split(' / ')
            # 年份
            year = re.sub('[\n ]', '', str2_list[0])
            # 制片国家
            country = str2_list[1]
            # 影片类型
            type = re.sub('[\n ]', '', str2_list[2])
        except:
            year = None
            country = None
            type = None
        url = li.xpath(".//div[@class='hd']/a/@href")[0]
        print({'排名': ranking, '电影名': title, '评分': score, '评价人数': evaluators_number, '导演': director,
               '主演': performer, '年份': year, '制片国家': country, '影片类型': type, '影片主页链接': url})
        data_list.append(
            {'排名': ranking, '电影名': title, '评分': score, '评价人数': evaluators_number, '导演': director,
             '主演': performer, '年份': year, '制片国家': country, '影片类型': type, '影片主页链接': url})


def into_excel(data_list):
    # 创建DataFrame对象
    df = pd.DataFrame(data_list)
    # 写入excel文件
    df.to_excel('电影Top250排行.xlsx')


def main():
    data_list = []  # 空列表用于存储每页获取到的数据
    # 1. 设置翻页
    for i in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&amp;filter='
        # 2. 获取网页源码
        html_str = get_html_str(url)
        # 3. 提取数据
        get_data(html_str, data_list)
        # 4. 限制爬取的速度
        time.sleep(5)
    # 5. 写入excel
    into_excel(data_list)


if __name__ == "__main__":
    main()

```

程序运行完毕后生成excel文件：

<img src="https://img-blog.csdnimg.cn/img_convert/df0479d15801179524b430c3e61e64f3.png" alt="">
