
--- 
title:  如何查看python安装路径 
tags: []
categories: [] 

---
在使用python的时候，有时候会需要找到python包的安装位置，来找其他安装的第三方包。下面我们来看看，在不同平台上，怎么找到python的安装路径。

很多运行的系统软件都是建立在python的基础之上，如果python出错了，那么整个系统可能会有出现重大问题的风险。在控制台先执行python

<img alt="" height="83" src="https://img-blog.csdnimg.cn/5038c1fe1a684cf58d583d415c53380c.png" width="1200">

这个时候我们能够确定的就是，python的安装路径一定被添加到了windows的环境变量中去了，因为只有添加到环境变量中去，才能够在命令行中执行。因此我们只要打开环境变量路径，就能找到python的安装路径。首先在桌面上的此电脑图标上点右键，选择属性。

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/43ae33c6906744419b25aa5f04c8cb66.png" width="1194">

高级系统设置下方可以看到环境变量，点开以后，在用户变量中找到PATH变量，然后点击右下角的编辑按钮。

 <img alt="" height="830" src="https://img-blog.csdnimg.cn/5ce9530ce5c7403eb27fae0a28a303c0.png" width="747">

 在打开的PATH变量中，我们可以清楚看到python的安装路径，如下面图中所示：

 <img alt="" height="751" src="https://img-blog.csdnimg.cn/2fb592cfd7dd4809b4b42f0c82448a48.png" width="894"><img alt="" height="781" src="https://img-blog.csdnimg.cn/29b518d0c6ca4664b8bb646ab553b9a8.png" width="786">

 

 然后我们根据PATH变量中的python路径值打开对应的文件夹，如下面图中所示，所有的python安装文件都在里面了。

<img alt="" height="754" src="https://img-blog.csdnimg.cn/d0b094b4d403496fa0d6d3bcc92ca598.png" width="1200">

 
