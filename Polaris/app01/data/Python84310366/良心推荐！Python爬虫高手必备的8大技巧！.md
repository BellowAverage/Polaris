
--- 
title:  良心推荐！Python爬虫高手必备的8大技巧！ 
tags: []
categories: [] 

---
想要快速学习爬虫，最值得学习的语言一定是Python，Python应用场景比较多，比如：**Web快速开发、爬虫、自动化运维等等，** 可以做简单网站、自动发帖脚本、收发邮件脚本、简单验证码识别脚本。

<img src="https://img-blog.csdnimg.cn/img_convert/4317cf9da78ff83447a5f49add71d478.jpeg" alt="">

爬虫在开发过程中也有很多复用的过程，今天就总结一下必备的8大技巧，以后也能省时省力，高效完成任务。

1

**基本抓取网页**

get方法

```
import urllib2

url = "http://www.baidu.com"
response = urllib2.urlopen(url)
print response.read()

```

post方法

```
import urllib
import urllib2

url = "http://abcde.com"
form = {<!-- -->'name':'abc','password':'1234'}
form_data = urllib.urlencode(form)
request = urllib2.Request(url,form_data)
response = urllib2.urlopen(request)
print response.read()

```

2

**使用代理IP**

在开发爬虫过程中经常会遇到**IP被封掉**的情况，这时就需要用到代理IP；在urllib2包中有ProxyHandler类，通过此类可以设置**代理访问网页**，如下代码片段：

```
import urllib2

proxy = urllib2.ProxyHandler({<!-- -->'http': '127.0.0.1:8087'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')
print response.read()

```

3

**Cookies处理**

cookies是某些网站为了**辨别用户身份**、进行session跟踪而储存在用户本地终端上的数据(通常经过加密)，python提供了cookielib模块用于处理cookies，cookielib模块的主要作用是提供可存储cookie的对象，以便于与urllib2模块配合使用来访问Internet资源。

代码片段：

```
import urllib2, cookielib
cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())
opener = urllib2.build_opener(cookie_support)
urllib2.install_opener(opener)
content = urllib2.urlopen('http://XXXX').read()

```

关键在于CookieJar()，它用于管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失，所有过程都不需要单独去操作。

手动添加cookie：

```
cookie = "PHPSESSID=91rurfqm2329bopnosfu4fvmu7; kmsign=55d2c12c9b1e3; KMUID=b6Ejc1XSwPq9o756AxnBAg="
request.add_header("Cookie", cookie)

```

4

**伪装成浏览器**

某些网站反感爬虫的到访，于是对爬虫一律拒绝请求。所以用urllib2直接访问网站经常会出现**HTTP Error 403: Forbidden**的情况。

对有些 header 要特别留意，Server 端会针对这些 header 做检查：
-  User-Agent 有些 Server 或 Proxy 会检查该值，用来判断是否是浏览器发起的 Request -  Content-Type 在使用 REST 接口时，Server 会检查该值，用来确定 HTTP Body 中的内容该怎样解析 
这时可以通过修改http包中的header来实现，代码片段如下：

```
import urllib2
headers = {<!-- -->
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
request = urllib2.Request(
    url = 'http://my.oschina.net/jhao104/blog?catalog=3463517',
    headers = headers
)
print urllib2.urlopen(request).read()

```

5

**页面解析**

对于页面解析最强大的当然是**正则表达式**，这个对于不同网站不同的使用者都不一样，就不用过多的说明

其次就是**解析库**了，常用的有两个lxml和BeautifulSoup

对于这两个库，我的评价是，都是HTML/XML的处理库，Beautifulsoup纯python实现，效率低，但是**功能实用**，比如能用通过结果搜索获得某个HTML节点的源码；lxml C语言编码，高效，支持Xpath。

6

**验证码的处理**

对于一些简单的验证码，可以进行简单的识别。本人也只进行过一些简单的验证码识别。但是有些反人类的验证码，比如12306，可以通过打码平台进行人工打码，当然这是要付费的。

7

**gzip压缩**

有没有遇到过某些网页，不论怎么转码都是一团乱码。哈哈，那说明你还不知道**许多web服务具有发送压缩数据的能力**，这可以将网络线路上传输的大量数据**消减 60%****以上**。这尤其适用于XML web 服务，因为 XML 数据 的压缩率可以很高。

但是一般服务器不会为你发送压缩数据，除非你告诉服务器你可以处理压缩数据。

于是需要这样修改代码：

```
import urllib2, httplib
request = urllib2.Request('http://xxxx.com')
request.add_header('Accept-encoding', 'gzip')
opener = urllib2.build_opener()
f = opener.open(request)

```

>  
 这是关键：创建Request对象，添加一个 Accept-encoding 头信息告诉服务器你能接受 gzip 压缩数据。 


然后就是解压缩数据：

```
import StringIO
import gzip

compresseddata = f.read()
compressedstream = StringIO.StringIO(compresseddata)
gzipper = gzip.GzipFile(fileobj=compressedstream)
print gzipper.read()

```

8

**多线程并发抓取**

单线程太慢的话，就需要多线程了，这里给个简单的线程池模板 这个程序只是简单地打印了1-10，但是可以看出是并发的。

虽然说Python的多线程很鸡肋，但是对于爬虫这种网络频繁型，还是能一定程度提高效率的。

```
from threading import Thread
from Queue import Queue
from time import sleep
# q是任务队列
#NUM是并发线程总数
#JOBS是有多少任务
q = Queue()
NUM = 2
JOBS = 10
#具体的处理函数，负责处理单个任务
def do_somthing_using(arguments):
    print arguments
#这个是工作进程，负责不断从队列取数据并处理
def working():
    while True:
        arguments = q.get()
        do_somthing_using(arguments)
        sleep(1)
        q.task_done()
#fork NUM个线程等待队列
for i in range(NUM):
    t = Thread(target=working)
    t.setDaemon(True)
    t.start()
#把JOBS排入队列
for i in range(JOBS):
    q.put(i)
#等待所有JOBS完成
q.join()

```

## 关于Python学习指南

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后给大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、自动化办公等学习教程。带你从零基础系统性的学好Python！</mark>

#### 👉Python所有方向的学习路线👈

Python所有方向路线就是把Python常用的技术点做整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取）**</mark>

<img src="https://img-blog.csdnimg.cn/3c4ee87941694f3789398db3d52a2637.png#pic_center" alt="在这里插入图片描述">

#### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。

<img src="https://img-blog.csdnimg.cn/64c89bf6293d4699bf7ee8f34b9e69fd.png#pic_center" alt="在这里插入图片描述">

#### <mark>温馨提示：篇幅有限，已打包文件夹，获取方式在：文末</mark>

#### 👉Python70个实战练手案例&amp;源码👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/2017b67544f94e8898db755e2703224a.png#pic_center" alt="在这里插入图片描述">

#### 👉Python大厂面试资料👈

我们学习Python必然是为了找到高薪的工作，下面这些面试题是来自**阿里、腾讯、字节等一线互联网大厂**最新的面试资料，并且有阿里大佬给出了权威的解答，刷完这一套面试资料相信大家都能找到满意的工作。

<img src="https://img-blog.csdnimg.cn/3055c54d3224495987c589f150324d73.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/b0751719fe914aec8c8d09f62f772e44.png#pic_center" alt="在这里插入图片描述">

#### 👉Python副业兼职路线&amp;方法👈

学好 Python 不论是就业还是做副业赚钱都不错，但要学会兼职接单还是要有一个学习规划。

<img src="https://img-blog.csdnimg.cn/01bcd7cbfd6d43fb85ef410766735154.png#pic_center" alt="在这里插入图片描述">

**👉** **这份完整版的Python全套学习资料已经上传，朋友们如果需要可以扫描下方CSDN官方认证二维码或者点击链接免费领取**【**`保证100%免费`**】

<font color="red">**点击免费领取《CSDN大礼包》： 安全链接免费领取**</font>
