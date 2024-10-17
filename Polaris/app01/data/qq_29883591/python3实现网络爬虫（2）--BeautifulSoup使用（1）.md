
--- 
title:  python3实现网络爬虫（2）--BeautifulSoup使用（1） 
tags: []
categories: [] 

---
这一次我们来了解一下美味的汤--BeautifulSoup，这将是我们以后经常使用的一个库，并且非常的好用。

BeautifuleSoup库的名字取自刘易斯·卡罗尔在《爱丽丝梦游仙境》里的同名诗歌。在故事中，这首歌是素甲鱼唱的。就像它在仙境中的说法一样，BeautifulSoup尝试化平淡为神奇。它通过定位HTML标签来格式化和组织复杂的网络信息，用简单易用的Python对象为我们展现XML结构信息。

由于BeautifulSoup库不是Python标准库，因此我们需要单独安装这个库，才能使用它。对于这个库的安装，我们这里秉着简单的原则，就直接利用pycharm这个IDLE进行库的自动下载和导入。

首先我们进入pycharm的主界面，单击file-〉settings-〉Project：untitled-〉Project Interpreter，如下图：

<img src="https://img-blog.csdn.net/20161107173001954?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

<img src="https://img-blog.csdn.net/20161107173021204?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

在上图中我们会看到一个绿色的加号，这时我们单击这个加号，会跳出如下的界面（pycharm在这个地方有时候很慢，会一直在这个界面刷新）：

<img src="https://img-blog.csdn.net/20161111172358991?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

这时我们在搜索框中输入“bs4”，然后选择列表中的bs4，然后进行安装，如下图：

<img src="https://img-blog.csdn.net/20161111172311709?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

这样我们就完成了BeautifulSoup这个库的安装，下面我们就可以来使用它了。

关于这个库的官方文档解释的是很详细的，一定要看一看：

下面我就简单说一下这个库的一些方面。

首先呢，我们还是从一个例子开始我们的学习：



```
#coding:utf - 8
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://tieba.baidu.com/")
bsObj=BeautifulSoup(html,"lxml")    #将html对象转化为BeautifulSoup对象
print(bsObj.title)   #输出这个网页中的标题 
```



执行上面的程序，我们会得到的结果为：&lt;title&gt;百度贴吧——全球最大的中文社区&lt;/title&gt; 首先我们来分析下bsObj=BeautifulSoup(html,"lxml")这句话对我们的html做了什么，在这句代码中，我们将html对象传入到BeautifulSoup中将它转化成BeautifulSoup对象，关于第二个参数lxml，可以到官方文档中看，解释得很详细，这里大家只要知道带上它就可以了，不需要管它。这样，我们就成功将html对象转化为了BeautifulSoup对象。 下面我们来了解下BeautifulSoup对象的结构，当我们将html转化后得到的结构为： html-&gt;&lt;html&gt;&lt;head&gt;....&lt;/head&gt;&lt;body&gt;.....&lt;/body&gt;&lt;/html&gt;       ---head-&gt;&lt;head&gt;&lt;title&gt;百度贴吧--全球最大的中文社区&lt;title&gt;&lt;/head&gt;

          ---title-&gt;&lt;title&gt;百度贴吧--全球最大的中文社区&lt;/title&gt;

     ----body-&gt;.........

关于这个页面的结构我中间省略了一些无关紧要的元素，只是为了展示下这种层次化的结构。 从上面我们可以看出，BeautifulSoup将html对象进行了层次化处理了，对它的原网页的标签进行了逐层的处理和细化，以便于我们之后使用。也就是我们只要知道，任何HTML（或XML）文件的任意节点信息都可以被提取出来，只要目标信息的旁边或者附近有标记就行了，这个标记就是我们网页中使用到的各种div、li之类的标签元素，也可以是class、id之类的属性，通过这些我们都可以对需要的信息进行提取。 

对于刚刚的bsObj.title这个提取标题的操作，由于一个网页中只有一个title，所以我们可以直接获取到它，因为它是唯一的嘛，大家可以这样理解，在一个学校中，你的学号是唯一的，我可以通过直接查找学号进而唯一的搜索你，而不会产生歧义。

对于bsObj.title我们有多重替代方案：

bsObj.html.head.title

bsObj.html.title

bsObj.head.title

关于上面的代码大家是对网页中元素的细化搜索，可以这样理解啊，假定你已经知道一个人是计科院的了，那你搜索他的时候常规思路便是直接在计科院找他，而bsObj.head中的head就相当于计科院，它是网页中的头部，title就放在这里面，所以我们使用bsObj.head.title也可以实现这个效果，其它的代码可以类似分析。

BeautifulSoup是一个对象，所以我们可以通过运算符“.”对它的属性进行提取。

如bsObj.title获取html的标题对象，bsObj.title.name获取标题的名字。。。

这里就先简单介绍这些，后面 我们将继续深入说明BeautifulSoup的好的使用方法。
