
--- 
title:  python使用ip代理抓取网页 
tags: []
categories: [] 

---
       在抓取一个网站的信息时，如果我们进行频繁的访问，就很有可能被网站检测到而被屏蔽，解决这个问题的方法就是使用ip代理 。在我们接入因特网进行上网时，我们的电脑都会被分配一个全球唯一地ip地址供我们使用，而当我们频繁访问一个网站时，网站也正是因为发现同一个ip地址访问多次而进行屏蔽的，所以这时候如果我们使用多个ip地址进行随机地轮流访问，这样被网站检测的概率就很小了，这时候如果我们再使用多个不同的headers，这时候就有多个ip+主机的组合，访问时被发现的概率又进一步减小了。



关于代码中ip代理的使用，下面介绍一下：

步骤：

1、urllib2库中的ProxyHandler类，通过此类可以使用ip代理访问网页

proxy_support=urllib2.ProxyHandler({})，其中参数是一个字典{‘类型':'代理ip:端口号'}

2、定制、创建一个opener

opener=urllib2.build_opener(proxy_support)

3、（1）安装opener

          urlib2.install_opener(opener)

       （2）调用默认的opener

         opener.open(url)



```
import urllib

url="http://www.csdn.net/"
for i in range(0,10000):
    html=urllib.urlopen(url)
    print html.info()
    print i
```



Traceback (most recent call last):   File "C:/Users/lenovo/PycharmProjects/untitled1/jt2/__init__.py", line 19, in &lt;module&gt;     html=urllib.urlopen(url)   File "C:\Python27\lib\urllib.py", line 87, in urlopen     return opener.open(url)   File "C:\Python27\lib\urllib.py", line 213, in open     return getattr(self, name)(url)   File "C:\Python27\lib\urllib.py", line 350, in open_http     h.endheaders(data)   File "C:\Python27\lib\httplib.py", line 997, in endheaders     self._send_output(message_body)   File "C:\Python27\lib\httplib.py", line 850, in _send_output     self.send(msg)   File "C:\Python27\lib\httplib.py", line 812, in send     self.connect()   File "C:\Python27\lib\httplib.py", line 793, in connect     self.timeout, self.source_address)   File "C:\Python27\lib\socket.py", line 571, in create_connection     raise err IOError: [Errno socket error] [Errno 10060]  

这就是因为我们使用了计算机的单一ip进行频繁访问而被检测出来的。

下面是使用了ip代理的代码：



```
import urllib2
import random

def getHtml(url,proxies):
    random_proxy = random.choice(proxies)
    proxy_support = urllib2.ProxyHandler({"http":random_proxy})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    html=urllib2.urlopen(url)
    return html

url="http://www.csdn.net/"
proxies=["101.53.101.172:9999","171.117.93.229:8118","119.251.60.37:21387","58.246.194.70:8080"
        "115.173.218.224:9797","110.77.0.70:80"]
for i in range(0,10000):
    try:
        html=getHtml(url,proxies)
        print html.info()     #打印网页的头部信息，只是为了展示访问到了网页，可以自己修改成想显示的内容
        print i
    except:
        print "出现故障"
```





对于有反爬虫机制的网页，下面还是以访问csdn中的博客为例：



```
#coding:utf-8
import urllib2
import random

def get_html(url,headers,proxies):

    random_userAget = random.choice(headers)
    random_proxy = random.choice(proxies)

    #下面是模拟浏览器进行访问
    req = urllib2.Request(url)
    req.add_header("User-Agent", random_userAget)
    req.add_header("GET", url)
    req.add_header("Host", "blog.csdn.net")
    req.add_header("Referer", "http://blog.csdn.net/?&amp;page=6")

    #下面是使用ip代理进行访问
    proxy_support = urllib2.ProxyHandler({"http":random_proxy})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)


    html = urllib2.urlopen(req)
    return html

url = "http://blog.csdn.net/?&amp;page=3"
"""
使用多个主机中的user_agent信息组成一个列表，当然这里面的user_agent都是残缺的，大家使用时可以自己找
身边的小伙伴借呦
"""
user_agents = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWe。。。hrome/45.0.2454.101 Safari/537.36",
    "Mozilla / 5.0(Windows NT 6.1) AppleWebKit / 537.。。。。likeGecko) Chrome / 45.0.2454.101Safari/ 537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit。。。。。Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3。。。。ML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
    "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) 。。。WebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
    "User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKi。。。。。36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) Apple。。。。。KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
    ]
#网上的ip有可能是不能用的，需要多做尝试
myproxies=["220.189.249.80:80","124.248.32.43:80"]
html = get_html(url,user_agents,myproxies)
print html.read()
```


