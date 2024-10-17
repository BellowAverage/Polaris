
--- 
title:  【Linux】修改Python命令默认指向Python3（通过软链接实现） 
tags: []
categories: [] 

---
### 引言

很多 Linux 发行版本，比如 Ubuntu 都会默认安装 Python2 和 Python3，当我们直接使用 Python 命令时，默认调用的是Python2，但我们实际想调用的却是 Python3。如何让 Python 命令直接指向 Python3 呢？

### 教程

在之前的文章中，我们介绍过。当然，我们也常称符号链接为软链接。其实上述问题就可以通过建立一个符号链接来实现。
1. 首先我们需要对 Python2 进行备份
```
sudo mv /usr/bin/python /usr/bin/python.bak

```
1. 建立指向 Python3 的软链接
```
sudo ln -s /usr/bin/python3 /usr/bin/python

```
1. 配置完成后，直接在终端命令行输入 python 就能看到结果了
```
$ python
Python 3.8.10 (default, Nov 26 2021, 20:14:08) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; 

```

### 总结

这其实就是 Linux 软链接非常典型的一个应用了，能够实现类似 Windows 桌面快捷方式的效果。
