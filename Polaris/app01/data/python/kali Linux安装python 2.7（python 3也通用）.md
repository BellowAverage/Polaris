
--- 
title:  kali Linux安装python 2.7（python 3也通用） 
tags: []
categories: [] 

---
一. 去官方下载安装包

        官网地址：

<img alt="" height="878" src="https://img-blog.csdnimg.cn/43429a64004f47a68b67071a63e15ff7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG9tMHgwMA==,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

        找到需要安装的安装包进行download下载。然后再上传到kali上，进行解压安装，下面的步骤可以参考下面的方法2.

二. wget命令安装

1. 在kali的命令行输入：

```
wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz
```

 进行安装，需要哪个版本可以自行修改：

<img alt="" height="552" src="https://img-blog.csdnimg.cn/6139736d02174153b4c932ca076b0e72.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG9tMHgwMA==,size_20,color_FFFFFF,t_70,g_se,x_16" width="733">

 下载完成后便可以进行解压，编译和安装的操作

2.解压

tar -zxvf Python-2.7.9.tgz

<img alt="" height="690" src="https://img-blog.csdnimg.cn/1febc3331336451c81e1e8fe2210abc0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG9tMHgwMA==,size_20,color_FFFFFF,t_70,g_se,x_16" width="1025">

3.编译：

```
cd python-2.7.9

 ./configure --prefix=/usr/local/python2.7 --with-threads --enable-shared
```

<img alt="" height="539" src="https://img-blog.csdnimg.cn/25a4288194164074a5a90e94becd6ce3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG9tMHgwMA==,size_20,color_FFFFFF,t_70,g_se,x_16" width="743">

4.安装

```
make &amp;&amp; make altinstall
```

<img alt="" height="552" src="https://img-blog.csdnimg.cn/9700f1f7a0b045c0943e2b8a351a903f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG9tMHgwMA==,size_20,color_FFFFFF,t_70,g_se,x_16" width="727">

5.输入python时报错，可以输入以下命令：

```
update-alternatives --install /usr/bin/python python /usr/bin/python2 100

update-alternatives --install /usr/bin/python python /usr/bin/python3 150
```

然后输入：

python --version

<img alt="" height="212" src="https://img-blog.csdnimg.cn/05618f15298c49a49b2874b748aacd70.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG9tMHgwMA==,size_20,color_FFFFFF,t_70,g_se,x_16" width="543">

6.如果需要切换版本：

```
update-alternatives --config python
```

然后选你需要的python版本，输入序号就可以了。（如果需要重新切换回python版本）： 　　 update-alternatives --config python （选号）




