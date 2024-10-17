
--- 
title:  python3实现网络爬虫（1）--urlopen抓取网页的html 
tags: []
categories: [] 

---
准备开始写一些python3关于爬虫相关的东西，主要是一些简单的网页爬取，给身边的同学入门看。

首先我们向网络服务器发送GET请求以获取具体的网页，再从网页中读取HTML内容。

       我们大家平时都使用网络浏览器，并且它已经成为我们上网不可或缺的软件。它创建信息的数据包，发送他们，然后把我们获取的的数据 显示 成漂亮的图像、声音、视频和文字。我们应该注意的是，浏览器就是代码，而代码是可以分解的，可以分解成许多基本组件，可重用、重写，以及做成我们想要 的任何东西。

那么现在我们就来看看如何从一个网页获取html并显示出来（代码可在pycharm等编辑器 中编写）：

```
#coding:utf-8
from urllib.request import urlopen
html=urlopen("http://tieba.baidu.com/")
print(html.read())
```

当我们执行这个程序后会得到如下的结果：

b'&lt;!DOCTYPE html&gt;&lt;!--STATUS OK--&gt;&lt;html&gt;&lt;head&gt;&lt;meta name="keywords" content="\xe8\xb4\xb4\xe5\x90\xa7,\xe7\x99\xbe\xe5\xba\xa6\xe8\xb4\xb4\xe5\x90\xa7,\xe8\xae\xba\xe5\x9d\x9b,\xe5\x85\xb4\xe8\xb6\xa3,\xe7\xa4\xbe\xe5\x8c\xba,BBS"/&gt;&lt;meta name="description" content="\xe7\x99\xbe\xe5\xba\xa6\xe8\xb4\xb4\xe5\x90\xa7\xe2\x80\x94\xe2\x80\x94\xe5\x85\xa8\xe7\x90\x83\xe6\x9c\x80\xe5\xa4\xa7\xe7\x9a\x84\xe4\xb8\xad\xe6\x96\x87\xe7\xa4\xbe\xe5\x8c\xba\xe3\x80\x82\xe8\xb4\xb4\xe5\x90\xa7\xe7\x9a\x84\xe4\xbd\xbf\xe5\x91\xbd\xe6\x98\xaf\xe8\xae\xa9\xe5\xbf\x97\xe5\x90\x8c\xe9\x81\x93\xe5\x90\x88\xe7\x9a\x84\xe4\xba\xba\xe7\x9b\xb8\xe8

这是百度贴吧的首页啊，代码还是比较长的，我就粘贴了首页的一些代码。

大家仔细看我们拿回的网页代码会发现，这个程序中拿回来的html中为什么会有些\xe8\xb4\xb4\xe5的东西，其实呢这个是编码问题，大家仔细观察会发现，在html代码最前面有b这个字母，后面的html代码用引号括起来了，这就表示这是个bytes类型的字节序列，在这种类型的序列中，中文会用16进制进行表示，所以我们看不到中文了。关于这个问题呢，是python中的编码问题，我们可以通过译码操作来对bytes进行解码，这就就要用到decode函数了

下面我们只要稍微修改下代码：



```
#coding:utf-8
from urllib.request import urlopen
html=urlopen("http://tieba.baidu.com/")
print(html.read().decode('utf-8'))
```



当我们再次执行这个程序会得到如下的结果：



```
&lt;!DOCTYPE html&gt;&lt;!--STATUS OK--&gt;&lt;html&gt;&lt;head&gt;&lt;meta name="keywords" content="贴吧,百度贴吧,论坛,兴趣,社区,BBS"/&gt;&lt;meta name="description" content="百度贴吧——全球最大的中文社区。贴吧的使命是让志同道合的人相聚。不论是大众话题还是小众话题，都能精准地聚集大批同好网友，展示自我风采，结交知音，搭建别具特色的“兴趣主题“互动平台。贴吧目录涵盖游戏、地区、文学、动漫、娱乐明星、生活、体育、电脑数码等方方面面，是全球最大的中文交流平台，它为人们提供一个表达和交流思想的自由网络空间，并以此汇集志同道合的网友。" /&gt;&lt;meta charset="UTF-8
```



现在我们就可以读懂这个html了。

有兴趣的话可以将抓取到的html代码粘贴到自己记事本中，将文件后缀名保存成.html，然后用浏览器打开，你会发现百度贴吧首页已经在你自己的电脑上了。



一番观赏之后，我们来解释下这个程序中用到的技术啊，程序中我们导入了一个urllib包中的函数用于访问网页。

首先来介绍下urlopen函数：

函数原型：def urlopen(url, data=None, proxies=None) 

形参：

（1）url：符合URL规范的字符串（包括http,ftp,gopher,local-file标准)，其实就是我们平时输入在浏览器中的网址。 

（2）data ： 向指定的URL发送的数据字符串，GET和POST都可以，但必须符合标准格式，即key=value&amp;key1=value1.... 

（3）proxies ： 

         代理服务器地址字典，如果未指定，在WINDOWS平台上则依据IE的设置，不支持需要验证的代理服务器。           例如:proxies = {'http': 'http://www.someproxy.com:3128'}，该例子表示一个http代理服务器http://www.someproxy.com:3128 

从代码可以看到，我只用到了第一个参数url，后两个参数是可选的，可以根据自己的需求进行定义的，也可以不指定，这时使用的是默认的参数。

返回值：

返回一个类似文件对象的对象(file_like) object

该对象拥有的方法为：

 info()返回从服务器传回的MIME标签头，即网页的头部信息。

 geturl()返回真实的URL,之所以称为真实，是因为对于某些重定向的URL,将返回被重定后的，大部分情况下可以认为就是我们输入的网址 

getcode()：获取网页的状态码，200是正常访问，301是重定向，404是网页不存在，403是禁止访问（有可能网页不存在，也可能是此网站有反爬虫机制，无法爬取；500是网站正忙）。

 其它的函数如 read()、readline()、 readlines()、fileno()、close()则和我们的文件对象类似了。



```
#coding:utf-8
from urllib.request import urlopen
html=urlopen("http://tieba.baidu.com/")
print(html.info())
```



Content-Type: text/html; charset=UTF-8 Date: Sat, 05 Nov 2016 07:54:57 GMT P3p: CP=" OTI DSP COR IVA OUR IND COM " Server: Apache Set-Cookie: TIEBAUID=cb23caae14130a0d384a57f1; expires=Thu, 31-Dec-2020 15:59:59 GMT; path=/; domain=tieba.baidu.com Set-Cookie: TIEBA_USERTYPE=6a1c7afddb7bc564bf21c11e; expires=Thu, 31-Dec-2020 15:59:59 GMT; path=/; domain=tieba.baidu.com Set-Cookie: BAIDUID=071A5C2537394FD906AA0DDCDC3E138D:FG=1; expires=Sun, 05-Nov-17 07:54:57 GMT; max-age=31536000; path=/; domain=.baidu.com; version=1 Tracecode: 32974281920539063562110515 Tracecode: 32974281920790459658110515 Vary: Accept-Encoding Vary: Accept-Encoding X-Bd-Id: 12371245289908688739 X-Bd-Oc: 0 X-Bd-Ul: 752bcb03d01cc2fed9326fe0daa239d7 Connection: close Transfer-Encoding: chunked

虽然这个返回的结果是很多的，但都是以键值对的形式展现给我们的，还是比较清晰易于理解的。

我们看看这句：Content-Type: text/html; charset=UTF-8，它告诉我们这个网页的文本格式是text/html，字符集是utf-8，后面的一些信息大家有兴趣的可以自己去查查资料，这里就不一一说明了。

下面我们来看看网页的状态码：



```
#coding:utf-8
from urllib.request import urlopen
html=urlopen("http://tieba.baidu.com/")
print(html.getcode())
```



好了，这一次就介绍到这里，还有很多好玩的就留给大家自己去体验了。

  

  



    
