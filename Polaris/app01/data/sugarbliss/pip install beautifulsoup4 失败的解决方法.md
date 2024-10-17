
--- 
title:  pip install beautifulsoup4 失败的解决方法 
tags: []
categories: [] 

---
#### 当我通过pip install beautifulsoup4，安装bs4时，出现了下面错误：

<img alt="" class="has" height="567" src="https://img-blog.csdnimg.cn/20191130111920193.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N1Z2FyYmxpc3M=,size_16,color_FFFFFF,t_70" width="1200">

#### 像这种安装错误大部分都是网络原因，使用pip进行安装，默认是从国外安装，所以需要将pip源设置为国内源，国内有豆瓣源、阿里源、网易源等等。

#### 使用下面的命令通过豆瓣源安装即可成功：

```
pip3 install bs4 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```

<img alt="" class="has" height="337" src="https://img-blog.csdnimg.cn/20191130112556978.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N1Z2FyYmxpc3M=,size_16,color_FFFFFF,t_70" width="1200">

#### 当然我们也可以直接配置永久国内源：

**windows配置方式：**
1. Win+R打开打开文件资源管理器，在地址栏中输入 %appdata%，回车1. 然后新建一个pip文件夹1. 在pip的文件夹里面新建一个名为 pip.ini的文件1. 文件中写如下内容
```
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com
```

#### 配置完成后就可以直接：pip install bs4了，其他库也可以愉快的直接pip安装了。 

 

 
