
--- 
title:  爬虫响应json总结笔记 
tags: []
categories: [] 

---
特点：易于阅读、易于机器生成、有效提升网络速度。 JSON语法规则：在JS语言中，一切都是对象。因此，任何支持的类型都可以通过json来表示。例如字符串、数字，对象，数组。 Js中对象和数组是比较特殊并且常用的两种类型：

```
   1.对象表示为键值对{name:’zhangsan’,age:’7’}
   2、数据有逗号分隔[1,2,3,4,5]
   3.花括号保存对象
   4.方括号保存数组。

```

**js的对象就相当于python中的字典 js的数组就相当于Python中的列表** 因为json用来存储js的对象或者数组，所以在Python中我们可以将json转化为list或者dict。

解析json的包json： json.dumps(python的list或者dict)----&gt;（返回值）----&gt;json字符串。 json.loads(json字符串)------&gt;（返回值）-----&gt;python的list或者dict.

```
   json.dump(list/dict,fp)—&gt;list，或者字典保存到json文件中。
   json.load(fp)—&gt;list/dict:从json文件中读出json数据。

```

```
②将列表/字典转换成json格式
import requests

a = {<!-- -->'姓名': '张三', '性别': '男'}
print(json.dumps(a))
print(type(a))

```

```
   json键值对是用来保存js对象的一种方式，和js对象的写法页大同小异，比如：

```

{“firstName”:“Json”,“Class”:“aid1111”}等价于下面这条js语句：{firstName:“Json”，Class：“aid1111”}。 很多人搞不清楚json和js对象的关系，甚至谁是谁都不清楚。其实可以这么理解： **【JSON是JS对象的字符串表达式，他使用文本形式表示一个JS对象的信息，本质是一个字符串。】** 如var obj = {a:“hello”,b:“World”}这是一个js对象。注意，键名也是可以用引号包裹的var json = ’ {“a”:“hello”,“b”:“World”}'这是一个json字符串，本质上是一个字符串。 JSON作为数据包格式传输的时候具有更高的效率，这是因为JSON不想xml那样具有严格的闭合标签，这就让有效数据量与总数据包比大大提升，从而减少同等数据流量的情况下，网络的传输的压力大大减低。

```
import json
 
import requests
 
url= 'https://这里是获取json的网页链接，通过网络连接分析获得'
 
# 设置请求网络连接时的User-Agent，不设置容易被网站拦截
headers={<!-- -->'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; Win64; x64; Trident/7.0; .NET4.0C; .NET4.0E)'}
 
# 发起网页连接请求
response=requests.get(url,headers=headers)
 
# 获取响应内容（json的文本形式）
jsonText = response.text
 
# 通过loads函数解析获取得到的json文本
jsonData = json.loads(jsonText)
 
# 解析后的数据会变为python中的字典类型的数据，因此可以像字典一样对json中的内容进行读取
dataList =jsonData['data']['searchResult']['dataResults']
 
# 同样的，如果原始json中包含了list，解析后字典里相应内容也是以list的形式出现，因此可以通过list元素的序号访问其中的元素
zcTitle=jsonData[0]
 

```

<img src="https://img-blog.csdnimg.cn/b4a36e56506a4064a47ae331231deffa.png" alt=""> <img src="https://img-blog.csdnimg.cn/d0a72ccd12194557b2828c7ad73ed880.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/41c61bcfa3404af8812d627f794798ff.png" alt="在这里插入图片描述">

```
import json
import requests
import random
import time
 
# 创建一个对象
class Get_url(object):
    # 定义初始化属性
    def __init__(self, num):
        # 这条是需要我们访问的 url ，实现翻页功能在主程序入口， 到时候传参给num就能实现翻页功能
        self.url = f'https://yoopu.me/api/posts/new?page={<!-- -->num}'
        # 这是伪造头，待会会随机选取其中之一
        self.USER_AGENTS = [
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1"
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
            "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
            "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12 "
        ]
        # 这是ip代理池，待会会随机选取其中之一
        self.IP_AGENTS = [{<!-- -->'HTTP': '60.170.204.30:8060'},
                          {<!-- -->'HTTP': '111.3.118.247:30001'},
                          {<!-- -->'HTTP': '220.168.52.245:53548'},
                          {<!-- -->'HTTP': '202.116.32.236:80'},
                          {<!-- -->'HTTP': '14.215.212.37:9168'},
                          {<!-- -->'HTTP': '39.106.71.115:7890'},
                          {<!-- -->'HTTP': '220.168.52.245:53548'},
                          {<!-- -->'HTTP': '202.55.5.209:8090'},
                          {<!-- -->'HTTP': '118.163.120.181:58837'},
                          {<!-- -->'HTTP': '121.13.252.62:41564'},
                          {<!-- -->'HTTP': '106.54.128.253:999'},
                          {<!-- -->'HTTP': '202.55.5.209:8090'},
                          {<!-- -->'HTTP': '210.5.10.87:53281'},
                          {<!-- -->'HTTP': '202.55.5.209:8090'},
                          {<!-- -->'HTTP': '112.6.117.135:8085'},
                          {<!-- -->'HTTP': '61.150.96.27:36880'},
                          {<!-- -->'HTTP': '106.15.197.250:8001'},
                          {<!-- -->'HTTP': '202.109.157.65:9000'},
                          {<!-- -->'HTTP': '112.74.17.146:8118'},
                          {<!-- -->'HTTP': '183.236.123.242:8060'},
                          {<!-- -->'HTTP': '220.168.52.245:53548'},
                          {<!-- -->'HTTP': '103.37.141.69:80'},
                          {<!-- -->'HTTP': '218.75.69.50:57903'},
                          {<!-- -->'HTTP': '202.55.5.209:8090'},
                          {<!-- -->'HTTP': '202.55.5.209:8090'},
                          {<!-- -->'HTTP': '113.88.208.112:8118'},
                          {<!-- -->'HTTP': '122.9.101.6:8888'},
                          {<!-- -->'HTTP': '47.113.90.161:83'},
                          {<!-- -->'HTTP': '106.15.197.250:8001'},
                          {<!-- -->'HTTP': '61.216.156.222:60808'}, ]
 
        # 构建headers请求头 把ua伪造头通过random随机选取一个传进去
        self.headers = {<!-- -->'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                        'Connection': 'keep-alive',
                        'Cookie': 'BDUSS_BFESS=VhlWExJYUxHLUd-VDQ3VHl4WktUb2dYSXZmWEdId3ViSG41Z2tHT3FhcnBpVlppRVFBQUFBJCQAAAAAAAAAAAEAAACFlYZcyqfIpb7N1tjNt9TZwLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOn8LmLp~C5iY; BAIDUID_BFESS=42114CA345FFDDD003FDB91BC19F4B5D:FG=1; HMACCOUNT_BFESS=76DA5CF409547AE8',
                        'Host': 'hm.baidu.com',
                        'Referer': 'https://yoopu.me/',
                        'Sec-Fetch-Dest': 'image',
                        'Sec-Fetch-Mode': 'no-cors',
                        'Sec-Fetch-Site': 'cross-site',
                        'User-Agent': random.choice(self.USER_AGENTS),
                        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"'}
 
        # 构建ip， 也通过随机模块传入
        self.proxies = random.choice(self.IP_AGENTS)
 
    # 获取网页的json数据方法
    def get_url(self):
        # 让程序延迟 0.5 到 1.5秒之间的时间随机访问
        time.sleep(random.uniform(0.5, 1.5))
        # 用get请求发送， 传入url，请求头， ip代理 然后用json数据保存
        #①json格式转换成列表/字典
        response = requests.get(self.url, headers=self.headers, proxies=self.proxies).json()
        # 退出函数返回 response
        return response
 
 
 
    # 提取json 关键数据方法
    def url_date(self):
        # 用res变量接收 get_url返回的数据
        res = self.get_url()
 
        # 然后解析 我们请求下来的数据，发现我们获取的数据是一个列表，
        # 然后里面数据是字典形式存在 ， 这样的话我们就可以通过遍历列表然后通过 key查找获取到值了
        for i in res:
            # 因为发现有一些数据 里面不包含我们所需要的信息， 然后找不到就会异常
            # 所以我们就用异常处理， 如果异常就执行 except的代码
            try:
                singer = i['artist']
                print(singer)
            except Exception as a:
                print('抱歉，没有获取到乐队信息！')
 
            try:
                singer = i['title']
                print(singer)
            except Exception as a:
                print('抱歉没有获取到歌名！')
 
            try:
                singer = 'https://yoopu.me/view/' + i['id']
                print(singer)
            except Exception as a:
                print('抱歉没有获取到歌名网址！')
 
            try:
                singer = i['key']
                print(singer + '调')
            except Exception as a:
                print('抱歉没有获取到歌曲音调！')
            print('\n')
 
 
    # 创建一个方法来运行上面的代码
    def run(self):
        self.url_date()
 
# 创建主程序入口
if __name__ == '__main__':
    # 实现翻页功能 循环0-50 然后传参进Get_url对象然后实现翻页功能
    for i in range(0, 50):
        run_1 = Get_url(i)
        run_1.run()
        # 实现爬取第几页
        print(f'已经爬取第{<!-- -->i + 1}页')
    print('爬取完毕！')

```

<img src="https://img-blog.csdnimg.cn/310fda4d3e7f4ce6a8b09a0be7f50de7.png" alt="在这里插入图片描述">

```
5、案例

import requests
# Fetch/XHR对象headers-General-Request URL
url = 'https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg?_=1646270844314&amp;cv=4747474&amp;ct=24&amp;format=json&amp;inCharset=utf-8&amp;outCharset=utf-8&amp;notice=0&amp;platform=yqq.json&amp;needNewCode=1&amp;uin=1152921504801487135&amp;g_tk_new_20200303=2006272574&amp;g_tk=2006272574&amp;hostUin=0&amp;is_xml=0&amp;key=毛不易'
# 头信息
header = {<!-- -->'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
# 获取数据
res = requests.get(url, headers=header)
# 将json格式数据转换为字典/列表
res = res.json()
#从字典/列表中找到对应需要的数据
list_song = res['data']['song']['itemlist']
for song in list_song:
    print(song['name'])


```
