
--- 
title:  （计算机视觉、Mac）LibSVM在python环境的下载与安装配置（PyCharm） 
tags: []
categories: [] 

---
        在学习《python计算机视觉》这本书中，8.3.1--使用LibSVM 这小节内容需要下载LibSVM。

在阅读书本附录及其他大佬的教程之后完美安装了LibSVM。以下介绍下载和安装的流程。

1.打开下载地址：下载zip文件，并解压。

<img alt="" height="117" src="https://img-blog.csdnimg.cn/548ccbec474348bfb056b9f1b12b5f98.png" width="441">



2.打开终端输入：

$ cd libsvm-x.x(x.x是版本号)

$ make

然后进入python目录，同样输入make

$ cd python/

$ make

完成以上操作后，可以在libsvm-x.x文件夹中看见多出一个libsvm.so.2文件。

3.前往/lib/python3.9/site-packages，将libsvm.so.2复制到这个文件夹中；

在这个文件夹中创建libsvm文件夹，在libsvm中新建__init__.py文件；

将下载的libsvm-x.x-&gt;python中的.py和svmutil.py复制到这个libsvm文件夹中。

4.完成以上操作就可以在PyCharm中安装libsvm就正常使用了。<img alt="" height="1200" src="https://img-blog.csdnimg.cn/ce6a57361ba94d848951f258d3697a48.png" width="1200">

----今天不学习，明天变废物。---- 




