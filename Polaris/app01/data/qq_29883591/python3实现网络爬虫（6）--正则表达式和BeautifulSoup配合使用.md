
--- 
title:  python3实现网络爬虫（6）--正则表达式和BeautifulSoup配合使用 
tags: []
categories: [] 

---
      这一次介绍下正则表达式和BeautifulSoup结合使用。

      对于正则表达式，在python中是一种很好的工具，可以帮助我们匹配我们需要的数据，当然了这些数据肯定是符合某些共性的，才能被我们的正则表达式所捕获。我们可以先看看BeautifulSoup中的findAll函数，这个函数的特点就是根据我们提供的参数去匹配满足的内容，比如说我们使用bsObj.findAll("ul") 可以将网页中所有的ul标签的元素拿到手，这其实可以看成一个正则表达式的特例，是一个拥有很好特性的正则表达式，帮助我们将返回的数据依据ul标签进行了整合，使得更方便我们使用。然而，从我们以前学习数学的时候我们就知道，对于一个特殊解法，在解答一道特定的题目时可以发挥出很大的功效，但是对于一些普通的题目是无法入手的，这时还是要返璞归真，使用一般解法。而正则表达式我们就可以理解成一种比较通用的匹配方法，它的输入是字符串，输出的返回也是字符串，这是具有很大的普遍适用性的。其实我们完全可以通过正则表达式去完成findAll的工作，但是这是需要花费相对于findAll多的多的精力的。

   正则表达式的具体语法知识我就不进行讲解了，有不熟悉的可以自己查查资料，这次主要讲解正则表达式和BeautifulSoup结合使用的例子。

   这次的例子呢，我们要在百度贴吧的一个帖子中拿出里面所有美食的图片，网址为：（http://tieba.baidu.com/p/4792769205），进入此网页后，会看到如下图所示的图片：

<img src="https://img-blog.csdn.net/20161129230839657?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

然后呢，我们的工作自然是匹配这些图片了，那首先就是来观察规则了，第一步自然是审查元素了，看看图片对应的代码有什么特殊的标志，那么我们审查一下，如下图：

<img src="https://img-blog.csdn.net/20161129231303823?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

   首先我们看到审查到的图片元素的属性后，第一反应自然是使用findAll，对img进行查找，并且我们会发现它是有class属性的，这正好帮助我们筛掉网页中其它不符合我们要求的图片，这种想法是对的，但是我们这次不希望使用这个方法，因为这个方法我们已经掌握了，而且很有可能以后我们会遇到没有属性的图片，那么我们是不是得多掌握一个技能呢，正所谓技多不压身嘛。

   这次我们关注图中我用箭头标注出来的地方，这个src中存放的就是图片存放的网址链接，关于这一点补充说一下，网页中显示的图片都是存放在服务器中的，由自己的网页浏览器通过加载把图片显示出来的，所以我们是无法直接通过解析html代码进行图片的抓取的，我们也需要向浏览器一样，去网址所在地拿到图片，这个之后会介绍，现在我们就一门心思先拿到图片的链接，因为这个是最重要的。

   那么我们看一下图片的网址链接的格式，src="http://imgsrc.baidu.com/forum/w%3D580/sign=e5c9c67f31dbb6fd255be52e3925aba6/00a33a381f30e9240c8ae

eb544086e061c95f7b7.jpg"，当我们多去检查几张图片就会发现，这种表示美食的图片的链接中，http://imgsrc.baidu.com/forum/w%3D580/sign和后面的.jpg是固定的，那么这就是我们正则表达式的突破口了，我们只需要让正则表达式匹配前面和后面的定值，中间匹配任意字符，那就可以拿到所有的网址了，下面直接上代码：



```
#coding:utf - 8
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import random
import re

def getHtml(url,headers):
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
    req.add_header("Host","tieba.baidu.com")
    req.add_header("Referer","http://tieba.baidu.com/p/4792769205")

    html=urlopen(req)
    return html    # 返回网页的html源码

url="http://tieba.baidu.com/p/4792769205"
#这里面的my_headers中的内容由于是个人主机的信息，所以我就用句号省略了一些，在使用时可以将自己主机的
my_headers = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,。。。。。。) Chrome/54.0.2840.99 Safari/537.36"]
html=getHtml(url,my_headers)     # 得到此网页的html源码
bsObj=BeautifulSoup(html,"html.parser")
# imageList是存放img标签的列表
imageList=bsObj.findAll("img",{"src":re.compile("http://imgsrc.baidu.com/forum/w%3D580/sign=.+\.jpg")})
for image in imageList:
    print(image["src"])        # 输出img中的网址，也就是图片的网址

```



http://imgsrc.baidu.com/forum/w%3D580/sign=e5c9c67f31dbb6fd255be52e3925aba6/00a33a381f30e9240c8aeeb544086e061c95f7b7.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=1186d7e69022720e7bcee2f24bca0a3a/3eaa333fb80e7bec4c967165272eb9389a506b14.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=2cfaec76751ed21b79c92eed9d6fddae/29d899d4b31c87010ae5cf622f7f9e2f0608ff0a.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=67c043f2fa1fbe091c5ec31c5b610c30/2885ab389b504fc2c969cc81eddde71191ef6dae.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=212881a57a8b4710ce2ffdc4f3cfc3b2/4d3be403738da977a29bffafb851f8198718e32d.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=a8bd86b444086e066aa83f4332097b5a/3d582887e950352ad6783f8d5b43fbf2b3118b40.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=0b2d45468a025aafd3327ec3cbecab8d/f0a8838fa0ec08fa8b03102151ee3d6d54fbda64.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=9d9a55916ad0f703e6b295d438fb5148/968885dda144ad344e0b8401d8a20cf430ad852e.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=39aa5a835182b2b7a79f39cc01afcb0a/1e73ae3eb13533fa1a6551a9a0d3fd1f43345b95.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=77f08fb852afa40f3cc6ced59b65038c/9624b2ec08fa513d22975454356d55fbb3fbd9a1.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=54d4b935845494ee87220f111df4e0e1/a3696f1ed21b0ef4bcdfa0d4d5c451da80cb3eab.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=c54554523101213fcf334ed464e636f8/a02ddb177f3e67098168257433c79f3df9dc557f.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=8943af685f2c11dfded1bf2b53266255/94b8a27eca806538e74dcc989fdda144af3482c5.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=99a1d88eeddde711e7d243fe97eecef4/75205510b912c8fc8f0d9e46f4039245d48821ed.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=089f4f83b00e7bec23da03e91f2fb9fa/78957509c93d70cf0a59f181f0dcd100b8a12bc1.jpg http://imgsrc.baidu.com/forum/w%3D580/sign=3209bd4316178a82ce3c7fa8c602737f/75a51ef3d7ca7bcbba6980a0b6096b63f724a85e.jpg 

     看到这个是不是很开心，没错，这个就是我们需要的图片的网址。对于上面的代码，和上一篇博客中说到的一样啊，my_headers要用自己主机User-Agent进行构造，具体方法见博客：

        也许大家对这些链接并不特写敏感，那我们就来把这些图片用程序下载到我们的电脑 上来，直观感受下：



```
#coding:utf - 8
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
from urllib.request import urlretrieve
import random
import re

def getHtml(url,headers):
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
    req.add_header("Host","tieba.baidu.com")
    req.add_header("Referer","http://tieba.baidu.com/p/4792769205")

    html=urlopen(req)
    return html    # 返回网页的html源码

url="http://tieba.baidu.com/p/4792769205"
#这里面的my_headers中的内容由于是个人主机的信息，所以我就用句号省略了一些，在使用时可以将自己主机的
my_headers = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"]
html=getHtml(url,my_headers)     # 得到此网页的html源码
bsObj=BeautifulSoup(html,"html.parser")
# imageList是存放img标签的列表
imageList=bsObj.findAll("img",{"src":re.compile("http://imgsrc.baidu.com/forum/w%3D580/sign=.+\.jpg")})
for index,image in enumerate(imageList):
    imageUrl=image["src"]      # img中的网址，也就是图片的网址
    imageLocation="D://picture/"+str(index+1)+".jpg"     # 图片保存的地址，这里动态命名为数字.jpg
    urlretrieve(imageUrl,imageLocation)     # 下载图片
    print("图片：",index+1,"下载完毕")

```



图片： 1 下载完毕 图片： 2 下载完毕 图片： 3 下载完毕 图片： 4 下载完毕 图片： 5 下载完毕 图片： 6 下载完毕 图片： 7 下载完毕 图片： 8 下载完毕 图片： 9 下载完毕 图片： 10 下载完毕 图片： 11 下载完毕 图片： 12 下载完毕 图片： 13 下载完毕 图片： 14 下载完毕 图片： 15 下载完毕 图片： 16 下载完毕

       打开图片所存储的位置，可以看到图片都已经保存好了

<img src="https://img-blog.csdn.net/20161201132638750?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="">   

          这个程序中，只是添加了一个下载的函数urlretrieve，这个函数可以根据提供的图片网址和图片存储在电脑中的位置帮我们到服务器端把图片拿回来，这个函数通用是在

urllib.request中的，所以我们要import它。这次就不详细介绍这个函数了，有兴趣的可以自己去查下资料，这里我们只需要知道这个函数的前两个参数的用法就足够我们以后使用了。

         对于图片的命名，贴吧中其实指出了名字，有兴趣的可以尝试抓取这个名字，用于图片的命名，会比我的1、2、3、4的数字更帅气哦。

 
