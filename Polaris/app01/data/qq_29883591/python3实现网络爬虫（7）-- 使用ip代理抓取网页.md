
--- 
title:  python3实现网络爬虫（7）-- 使用ip代理抓取网页 
tags: []
categories: [] 

---
在抓取一个网站的信息时，如果我们进行频繁的访问，就很有可能被网站检测到而被屏蔽，解决这个问题的方法就是使用ip代理 。在我们接入因特网进行上网时，我们的电脑都会被分配一个全球唯一地ip地址供我们使用，而当我们频繁访问一个网站时，网站也正是因为发现同一个ip地址访问多次而进行屏蔽的，所以这时候如果我们使用多个ip地址进行随机地轮流访问，这样被网站检测的概率就很小了，这时候如果我们再使用多个不同的headers，这时候就有多个ip+主机的组合，访问时被发现的概率又进一步减小了。

关于代码中ip代理的使用，下面介绍一下干货： 



步骤：

1、urllib.request库中的ProxyHandler类，通过此类可以使用ip代理访问网页

proxy_support=urllib.request.ProxyHandler({})，其中参数是一个字典{‘类型':'代理ip:端口号'}

2、定制、创建一个opener

opener=urllib.request.build_opener(proxy_support)

3、（1）安装opener

          urlib.request.install_opener(opener)

       （2）调用默认的opener

         opener.open(url)

对于没有设置反爬虫机制的网站，我们只需要直接像上面那样引入ProxyHandler类进行处理，不需考虑模仿浏览器，下面以访问csdn主页为例： 



```
from urllib.request import urlopen

url="http://www.baidu.com"
for i in range(0,10000):
    html=urlopen(url)
    print(html.info())
    print(i)

```



当上面的程序执行了351次的时候，会出现如下的错误：

Traceback (most recent call last):   File "D:/Program Files (x86)/JetBrains/PyCharm Community Edition 2016.1/untitled/我的临时/py3.5/ceshiUrllib.py", line 55, in &lt;module&gt;     html=urlopen(url)   File "D:\newinstall\anaconda3.5\lib\urllib\request.py", line 163, in urlopen     return opener.open(url, data, timeout)   File "D:\newinstall\anaconda3.5\lib\urllib\request.py", line 472, in open     response = meth(req, response)   File "D:\newinstall\anaconda3.5\lib\urllib\request.py", line 582, in http_response     'http', request, response, code, msg, hdrs)   File "D:\newinstall\anaconda3.5\lib\urllib\request.py", line 510, in error     return self._call_chain(*args)   File "D:\newinstall\anaconda3.5\lib\urllib\request.py", line 444, in _call_chain     result = func(*args)   File "D:\newinstall\anaconda3.5\lib\urllib\request.py", line 590, in http_error_default     raise HTTPError(req.full_url, code, msg, hdrs, fp) urllib.error.HTTPError: HTTP Error 502: Bad Gateway 

       这是由于我们在访问的时候，网站会记下我们的ip，当我们的ip访问量在一段时间内超过网站设定的上限值的时候，这个请求就会被拒绝了（我这个报错是有问题的，因为 测试到一半的时候网络断了，不过在继续访问一段时间后是会报请求错误的，这个就不演示了）。



```
#coding:utf-8
from urllib.request import Request
from urllib.request import urlopen
import urllib
import random

def getHtml(url,proxies):

    proxy=random.choice(proxies)     #随机取一个ip出来使用
    proxy_support = urllib.request.ProxyHandler({"http":proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    html=urlopen(url)
    return html

url = "http://www.baidu.com"
proxies=["101.53.101.172:9999","101.53.101.172:9999","171.117.93.229:8118","119.251.60.37:21387","58.246.194.70:8080"]

for i in range(10000):
    try:
       html=getHtml(url,proxies)
       print(html.info())
       print(i)
    except:
        print("故障")
```



      关于这个ip代理问题，还要从前面说过的`urllib.request.``urlopen讲起，在这个urlopen函数中，当代理被检测到的时候，`

下面是官方文档中的一些介绍：

class `urllib.request.``ProxyHandler`(**proxies=None**)

**       **Cause requests to go through a proxy. If **proxies** is given, it must be a dictionary mapping protocol names to URLs of proxies. The default is to read the list of proxies from the environment variables`&lt;protocol&gt;_proxy`. If no proxy environment variables are set, then in a Windows environment proxy settings are obtained from the registry’s Internet Settings section, and in a Mac OS X environment proxy information is retrieved from the OS X System Configuration Framework.

       To disable autodetected proxy pass an empty dictionary.

       The `no_proxy` environment variable can be used to specify hosts which shouldn’t be reached via proxy; if set, it should be a comma-separated list of hostname suffixes, optionally with `:port` appended, for example`cern.ch,ncsa.uiuc.edu,some.host:8080`.

 

`urllib.request.``install_opener`(**opener**)

    Install an  instance as the default global opener. Installing an opener is only necessary if you want urlopen to use that opener; otherwise, simply call instead of. The code does not check for a real, and any class with the appropriate interface will work.

 

`urllib.request.``build_opener`([**handler**,**...**])

Return an  instance, which chains the handlers in the order given.**handler**s can be either instances of, or subclasses of (in which case it must be possible to call the constructor without any parameters). Instances of the following classes will be in front of the**handler**s, unless the**handler**s contain them, instances of them or subclasses of them: (if proxy settings are detected),,, ,,, , .

     关于上面的三个方法就不进行翻译了，有兴趣的可以自己看一下，不过在使用性上只要掌握它的简单功能就可以了，也就是掌握文章开头部分的构造步骤就好了。
