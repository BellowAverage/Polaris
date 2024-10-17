
--- 
title:  python3实现网络爬虫（5）--模拟浏览器抓取网页 
tags: []
categories: [] 

---
      本来准备继续分析BeautifulSoup的，但是好多网页都是反爬虫的，想分析没法分析了 ，那么就跳一节吧，我们先看看如何模拟浏览器进行访问网页，然后再折回去继续说BeautifulSoup。

      由于前面我已经用python2写过这方面的内容了，那么这次偷个懒，我就在以前的博客上进行简单的移植了，这个博客的网址为：



下面是一个简单的访问：



```
#coding:utf-8
from urllib.request import urlopen

url="http://www.csdn.net/"
html=urlopen(url)
print(html.read().decode("utf-8"))
```



     我们再来看下面的例子： 



```
#coding:utf - 8
from urllib.request import urlopen

url="http://blog.csdn.net/beliefer/article/details/51251757"
html=urlopen(url)
print(html.read().decode("utf-8"))
```



Traceback (most recent call last):   File "D:/python/python3.5/first.py", line 7, in &lt;module&gt;     html=urlopen(url)   File "D:\newinstall\python3.5\lib\urllib\request.py", line 163, in urlopen     return opener.open(url, data, timeout)   File "D:\newinstall\python3.5\lib\urllib\request.py", line 472, in open     response = meth(req, response)   File "D:\newinstall\python3.5\lib\urllib\request.py", line 582, in http_response     'http', request, response, code, msg, hdrs)   File "D:\newinstall\python3.5\lib\urllib\request.py", line 510, in error     return self._call_chain(*args)   File "D:\newinstall\python3.5\lib\urllib\request.py", line 444, in _call_chain     result = func(*args)   File "D:\newinstall\python3.5\lib\urllib\request.py", line 590, in http_error_default     raise HTTPError(req.full_url, code, msg, hdrs, fp) urllib.error.HTTPError: HTTP Error 403: Forbidden 



     从其中的403 Forbidden我们便可以发现，此时网站禁止了程序的访问，这便是因为csdn网站设置了反爬虫机制，当网站检测到爬虫时，将会拒绝访问，所以我们会得到上述的结果。

     这时候我们便需要模拟浏览器进行访问，才能躲过网站的反爬虫机制，进而顺利的抓取我们想要的内容。

    下面就将用到一个神奇的库urllib.request.Request进行我们的模拟工作，这次同样是先上代码，然后进行解释，不过这次我要提醒一下，下面的代码不可以直接用，需要将其中的my_headers中的User-Agent替换成自己的，因为为了保密，我添加了省略号，所以是不可以直接使用的，替换方法见后面的图片解释，这次为了使用的方便，我们 引入函数： 



```
#coding:utf - 8
from urllib.request import urlopen
from urllib.request import Request
import random
import re

def getContent(url,headers):
    """
    此函数用于抓取返回403禁止访问的网页
    """
    random_header = random.choice(headers)

    """
    对于Request中的第二个参数headers，它是字典型参数，所以在传入时
    也可以直接将个字典传入，字典中就是下面元组的键值对应
    """
    req =Request(url)
    req.add_header("User-Agent", random_header)
    req.add_header("GET",url)
    req.add_header("Host","blog.csdn.net")
    req.add_header("Referer","http://www.csdn.net/")

    content=urlopen(req).read().decode("utf-8")
    return content

url="http://blog.csdn.net/beliefer/article/details/51251757"
#这里面的my_headers中的内容由于是个人主机的信息，所以我就用句号省略了一些，在使用时可以将自己主机的
my_headers = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/53 。。。Chrome/54.0.2840.99 Safari/537.36"]
print(getContent(url,my_headers))
```





       既然我们是要模拟浏览器进行网页访问，那么这些参数自然需要我们去浏览器中寻找了。

       首先我们点击进入将要爬取的那个网页，然后鼠标右击页面，点击审查元素，将会出现下面的的框架，然后我们点击Network，这时候会发现并没有出现我们所在的页面的信息，没关系，这时候我们刷新一下页面，便会出现如下图所示的信息了。

       这时候我们会看见第一行的51251757，而这正是我们网页的网址的后面的标号，这时候我们点击这个标号，便会出现下图所示的内容： 

<img src="https://img-blog.csdn.net/20161201010714820?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

下面是我现在直接用这个网址访问得到的截图：

<img src="https://img-blog.csdn.net/20161201124421650?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

对于前两张图，我是以前写版本2的访问时的，现在直接拿过来用的，那个时候是在csdn首页点到这个博客的，所以在代码和前两张图中我header中的referer填的是

blog.csdn.net，而这张图是我直接用网址链接输入到浏览器访问的，所以从图片中可以看出，referer是http://blog.csdn.net/beliefer/article/details/51251757，这正是我们的网址，这里也是为了让大家更好地理解这个referer，才贴了不一样的图。在这张图片中，我已经将需要填写的四个内容用红色的线标记出来了，大家在测试的时候，一定不要用我给的那个User-Agent，因为我中间用省略号替换掉了一些，大家要用自己的补上去。



     这时候我们会发现Headers，是不是有种眼前一亮的感觉，没错，你的直觉是对的，我们所需要的信息正在这个Headers里面。

     然后对照着代码中的需要的参数，将这些信息拷贝回去便可以使用了，因为这里面显示的信息刚好是键值对应的，所以我们拷贝使用也就很方便了。

     现在来介绍下这个urllib.request.Request的用法（从官方文档中翻译过来 的）：



```
#coding:utf - 8
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import random
import re

def getContent(url,headers):
    """
    此函数用于抓取返回403禁止访问的网页
    """
    random_header = random.choice(headers)

    """
    对于Request中的第二个参数headers，它是字典型参数，所以在传入时
    也可以直接将个字典传入，字典中就是下面元组的键值对应
    """
    # req =Request(url)
    # req.add_header("User-Agent", random_header)
    # req.add_header("GET",url)
    # req.add_header("Host","blog.csdn.net")
    # req.add_header("Referer","http://www.csdn.net/")

    header = {"User-Agent": random_header, "GET": url, "Host": "blog.csdn.net", "Referer": "http://www.csdn.net/"}
    req=Request(url,None,header)
    content=urlopen(req).read().decode("utf-8")
    return content

url="http://blog.csdn.net/beliefer/article/details/51251757"
#这里面的my_headers中的内容由于是个人主机的信息，所以我就用句号省略了一些，在使用时可以将自己主机的&lt;span style="color: rgb(84, 84, 84); font-family: 'Segoe UI', Tahoma, sans-serif;  white-space: pre-wrap;"&gt;&lt;strong&gt;User-Agent放进去&lt;/strong&gt;&lt;/span&gt;
my_headers = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/53。。。(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"]
print(getContent(url,my_headers))
```



     当我们要抓取一个网站的多个网页时，会很容易因为一台主机频繁访问而被网站检测出来，进而遭到屏蔽。而如果我们在列表中多放些不同的主机号，然后随机使用，是不是就不容易被发现了，当然，当我们为了防范这个时更加好的方法是使用IP代理，因为我们不是很容易就能获得很多主机信息的，而IP代理是很容易从网上搜索到的，关于多次访问相关问题我会在以后的博客中解释，在此就不多说了。





 
