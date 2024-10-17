
--- 
title:  Python安装第三方库的命令,Python安装matplotlib库 
tags: []
categories: [] 

---
大家好，本文将围绕Python安装扩展库常用工具展开说明，Python安装第三方库的命令是一个很多人都想弄明白的事情，想搞清楚Python安装matplotlib库需要先了解以下几个事情。



<img alt="" height="394" src="https://img-blog.csdnimg.cn/img_convert/4efdeddf27d17771554512f22ac2acef.jpeg" width="759">



**快速阅读**

主要是安装easytrader过程中踩到的一个又一个坑以及换到thstrade后的一个又一个坑，到处都是坑，坑无极限坑无止境。

本以为easytrader直接pip下载下来安装一下就可以了。没想到踩了一个又一个的坑。
1.  <h6>解决在Python中使用Win32api报错的问题，No module named win32api</h6> <pre class="has"></pre>  1.  <h6>UserWarning: 32-bit application</h6> E:\me\test\lib\site-packages\pywinauto\application.py:1064: UserWarning: 32-bit application should be automated using 32-bit Python (you use 64-bit Python) 这个是提示，不用改也可以。不过感觉源码可以给去掉了。等有空。就给他去掉  1.  <h6>requirements.txt 必装包的解释</h6> python 中requirements.txt中把所有需要安装的包放进去-i http://mirrors.aliyun.com/pypi/simple/  ：表示从阿里云的镜像下载 --trusted-host mirrors.aliyun.com 表示 信任这个host，否则有的包下载不了。 <pre class="has"></pre>  
###### UserWarning: 32-bit application
1.  <h6>pycharm 解释器的配置</h6> 在Location中填写项目路径、项目名; 在Base interpreter下拉框中选择Python解释器； **勾选Inherit global site-packages可以使用base interpreter中的第三方库，不选将和外界完全隔离；** **勾选Make available to all projects可将此虚拟环境提供给其他项目使用。**   1.  <h6>pycharm中解释器的选择</h6> <img alt="640?wx_fmt=png" src="https://img-blog.csdnimg.cn/img_convert/d055494121a37fa668be9e8dba91ca62.png"> 项目解释器中选择已经存在的，如果默认没有的话，点击右边的...打开然后选择系统解释器<img alt="640?wx_fmt=png" src="https://img-blog.csdnimg.cn/img_convert/921803caff4b634a1173e9211205a1c4.png"> 在右边选择你安装的python解释器。总结：每个项目可以有各自的解释器，也可以直接使用公共的解释器 一般是继承公共的，再下载所需要的包到自己的文件夹里最好。 <img alt="640?wx_fmt=png" src="https://img-blog.csdnimg.cn/img_convert/e403c84d411bff0ad80f619c0db806c5.png"> 但是默认会弹出错误对话框 ，因为你安装的解释器不在默认的这个目录 ， 这个安装目录还没找到在哪里改，感觉应该是pycharm中的一个设置 。 因为我都没有往这个目录下安装 <img alt="640?wx_fmt=png" src="https://img-blog.csdnimg.cn/img_convert/2f36b36b7cdc53e492498a0ac7c0df86.png">  
###### pycharm中解释器的选择

###### 6.更新skeletons

<img alt="640?wx_fmt=png" src="https://img-blog.csdnimg.cn/img_convert/659b480082ee8b5e564451f5dbbe9836.png">



##### 7.改换成thstrader

根据作者所说，所者在用easytrader调用同花顺的时候，发现代码过时了。所以自己看了下源码，改动了一下，

https://github.com/nladuo/THSTrader

下载完以后， 同样先安装requrements.txt的包。

###### 8.在安装numpy的时候，发现报错，

根据错误提示，删除默认自带的numpy，再下载就可以了。

删除默认自带numpy时要关掉pycharm.
1.  ModuleNotFoundError: No module named 'Image' 或者：cannot import name 'PILLOW_VERSION' from 'PIL' 错误解决方法 
###### 9.from PIL import Image 报错

=&gt;解决方法是把Pillow 以及Pollow相关的全部卸载掉，再重新安装一个就可以了，

如果卸载=》在pycharm的解释器里，选中相对应项目的解释器，然后点-号就可以了。

<img alt="640?wx_fmt=png" src="https://img-blog.csdnimg.cn/img_convert/f8f4c9b1d27842edd30b9af95c2778dd.png">

###### 10.pip版本低的坑

前面又弄了一次配置 ，把pip给换回去了，这次又得升回来。

又一堆错误

<img alt="640?wx_fmt=png" src="https://img-blog.csdnimg.cn/img_convert/c03e858357e36fb50f49f7b999df0630.png">

按说明应该是pip版本太低，我们先升级。

升完级以后继续走



###### 11.numpy安装不上的坑

<img alt="640?wx_fmt=png" src="https://img-blog.csdnimg.cn/img_convert/70b3a5480deef87998d1ed422a9e7353.png">

先在pycharm中直接在解释器里搜索安装，可以安装上了。继续往下



###### 12.不看报错了，不按说明了。直接来

下面还有错，不管了，先把requirements里的安装上去吧，

不看后面根的版本。

<img alt="640?wx_fmt=png" src="https://img-blog.csdnimg.cn/img_convert/b1ef3069b9be5b0c70bfa9a10d22e1fa.png">



直接全安装好，继续往下走

终于没有报错了，第一步算是过了。不过感觉好像结果不对。后面继续撸

下面是调试的图片

<img alt="640?wx_fmt=png" src="https://img-blog.csdnimg.cn/img_convert/0394de043a5bd27352d2fb4f3f373b09.png">




