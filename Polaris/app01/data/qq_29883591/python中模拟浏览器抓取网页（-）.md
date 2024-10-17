
--- 
title:  python中模拟浏览器抓取网页（-） 
tags: []
categories: [] 

---
      对于平时我们抓取网页的内容时，比较倾向于直接利用urllib进行抓取（这里我就基于python的2.7版本进行解说，对于python3之后的版本，是将python中的urllib和urllib2和并成了urllib），但有些网站设置了防采集的功能，会拒绝爬虫进行数据的采集，这时候便可以模拟浏览器进行网页访问，然后抓取需要的数据。

下面是一个简单的访问：

```
import urllib

url="http://www.csdn.net/"
html=urllib.urlopen(url)
print html.read()
```



我们再来看下面的例子：

```
import urllib

url="http://blog.csdn.net/beliefer/article/details/51251757"
html=urllib.urlopen(url)
print html.read()
```



&lt;html&gt; &lt;head&gt;&lt;title&gt;403 Forbidden&lt;/title&gt;&lt;/head&gt; &lt;body bgcolor="white"&gt; &lt;center&gt;&lt;h1&gt;403 Forbidden&lt;/h1&gt;&lt;/center&gt; &lt;hr&gt;&lt;center&gt;nginx&lt;/center&gt; &lt;/body&gt; &lt;/html&gt;

     从其中的403 Forbidden我们便可以发现，此时网站禁止了程序的访问，这便是因为csdn网站设置了反爬虫机制，当网站检测到爬虫时，将会拒绝访问，所以我们会得到上述的结果。

     这时候我们便需要模拟浏览器进行访问，才能躲过网站的反爬虫机制，进而顺利的抓取我们想要的内容。

     下面就将用到一个神奇的库urllib2进行我们的模拟工作，这次同样是先上代码，然后进行解释：



```
#coding=utf-8
import urllib2
import random

def getContent(url,headers):
    """
    此函数用于抓取返回403禁止访问的网页
    """
    random_header = random.choice(headers)

    """
    对于Request中的第二个参数headers，它是字典型参数，所以在传入时
    也可以直接将个字典传入，字典中就是下面元组的键值对应
    """
    req =urllib2.Request(url)
    req.add_header("User-Agent", random_header)
    req.add_header("GET",url)
    req.add_header("Host","blog.csdn.net")
    req.add_header("Referer","http://www.csdn.net/")

    content=urllib2.urlopen(req).read()
    return content

url="http://blog.csdn.net/beliefer/article/details/51251757"
#这里面的my_headers中的内容由于是个人主机的信息，所以我就用句号省略了一些，在使用时可以将自己主机的User-Agent放进去
my_headers = ["Mozilla/5.0 (Windows NT 6.3; Win64; x64) 。。。 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"]
print getContent(url,my_headers)
```



      既然我们是要模拟浏览器进行网页访问，那么这些参数自然需要我们去浏览器中寻找了。

     首先我们点击进入将要爬取的那个网页，然后鼠标右击页面，点击审查元素，将会出现下面的的框架，然后我们点击Network，这时候会发现并没有出现我们所在的页面的信息，没关系，这时候我们刷新一下页面，便会出现如下图所示的信息了。

<img src="https://img-blog.csdn.net/20160724101850666?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="">  

     这时候我们会看见第一行的51251757，而这正是我们网页的网址的后面的标号，这时候我们点击这个标号，便会出现下图所示的内容：

<img src="https://img-blog.csdn.net/20160724101922964?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

       这时候我们会发现Headers，是不是有种眼前一亮的感觉，没错，你的直觉是对的，我们所需要的信息正在这个Headers里面。

然后对照着代码中的需要的参数，将这些信息拷贝回去便可以使用了，因为这里面显示的信息刚好是键值对应的，所以我们拷贝使用也就很方便了。

     对于上述代码中的my_headers用的是一个列表大家或许会想你这是不是太作了，没事放那么多干嘛，用一个不就好了，其实对这一个网页来说这确实是多此一举，但这样写的话这个函数的用处就扩大了，当我们单个访问时，将列表中放入一个主机的信息就行了，但当我们要抓取一个网站的多个网页时，会很容易因为一台主机频繁访问而被网站检测出来，进而遭到屏蔽。而如果我们在列表中多放些不同的主机号，然后随机使用，是不是就不容易被发现了，当然，当我们为了防范这个时更加好的方法是使用IP代理，因为我们不是很容易就能获得很多主机信息的，而IP代理是很容易从网上搜索到的，关于多次访问相关问题我会在下一篇博客中解释，在此就不多说了。

        对于解释中有什么不对的地方欢迎大家指正灌水。
