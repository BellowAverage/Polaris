
--- 
title:  【解决方案】ubuntu 解决办法 ImportError: cannot import name ‘_gi‘ from ‘gi‘ 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>解决办法 ImportError: cannot import name ‘_gi’ from ‘gi’</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - -  
  
  


## 问题描述

ubuntu上安装使用python3.7解决 ppa 执行` sudo add-apt-repository ppa:ubuntu-toolchain-r/test` 报错如下

```
 mm@mm-desktop:~$  sudo add-apt-repository ppa:ubuntu-toolchain-r/test
 
 ppa:ubuntu-toolchain-r/test Traceback (most recent call last):   File
 "/usr/bin/add-apt-repository", line 12, in &lt;module&gt; 
 from softwareproperties.SoftwareProperties import SoftwareProperties, shortcut_handler   File
 "/usr/lib/python3/mm@mmdist-packages/softwareproperties/SoftwareProperties.py", line 67, in &lt;module&gt; 
 from gi.repository import Gio   File 
 "/usr/lib/python3/dist-packages/gi/__init__.py", line 42, in &lt;module&gt; 
 from . import _gi

```

```
 mm@mm-desktop:~$  sudo add-apt-repository ppa:s-mankowski/ppa-kf5

Traceback (most recent call last):
  File "/usr/bin/add-apt-repository", line 11, in &lt;module&gt;
    from softwareproperties.SoftwareProperties import SoftwareProperties, shortcut_handler
  File "/usr/lib/python3/dist-packages/softwareproperties/SoftwareProperties.py", line 67, in &lt;module&gt;
    from gi.repository import Gio
  File "/usr/lib/python3/dist-packages/gi/__init__.py", line 42, in &lt;module&gt;
    from . import _gi
ImportError: cannot import name '_gi' from 'gi' (/usr/lib/python3/dist-packages/gi/__init__.py)

```

## 解决方案1：

在python3.7的ubuntu系统中使用如下命令：

```
sudo ln -s /usr/lib/python3/dist-packages/gi/_gi.cpython-{<!-- -->36m,37m}-x86_64-linux-gnu.so

```

然后再添加 ppa。

## 解决方案2：

执行如下命令将你的python版本添加到 `alternatives `，以我的python3.6/3.7/3.8为例：

```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1  # 1表示最高优先级
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2  # 2表示次高优先级
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 3  # 3表示最低优先级

```

执行如下命令将python3版本切换到python 3.6

```
sudo update-alternatives --config python3

```

然后再执行命令添加 ppa。
