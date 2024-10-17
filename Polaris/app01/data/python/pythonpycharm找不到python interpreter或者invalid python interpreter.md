
--- 
title:  python:pycharm找不到python interpreter或者invalid python interpreter 
tags: []
categories: [] 

---
之前python安装在D盘，并且用pycharm已经编译运行过该工程，之后卸载了python重装到C盘，导致再次运行该工程的时候一直提示invalid python interpreter，因为pycharm一直会关联之前D盘的python，解决方法是先清理编译文件，再运行工程，就可以重新设置python interpreter了。

选中工程，右键选择“clean python compiled files”.

<img alt="" height="597" src="https://img-blog.csdnimg.cn/f1cd6331e3b24910afd43ff28e1d0d6e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA57KJ5pyr55qE5rKJ5reA,size_16,color_FFFFFF,t_70,g_se,x_16" width="546">


