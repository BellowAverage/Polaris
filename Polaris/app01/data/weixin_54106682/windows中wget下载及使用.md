
--- 
title:  windows中wget下载及使用 
tags: []
categories: [] 

---
①安装网址：

②选择x64 EXE进行下载；

x86\x64\ARM64的区别可参考该博客：http://t.csdnimg.cn/bNY6v

按照我的理解即，x86是指32位处理器、x64是指64位处理器，而arm则是IOS系统所采用的。

<img alt="" height="552" src="https://img-blog.csdnimg.cn/direct/d145dad1fda5496aa4cae7d78ebd7ca6.png" width="868">

③下载完成后，将下载下来的wget.exe文件放到C:\Windows\System32即可，以便在任何路径下都可以使用wget命令；

<img alt="" height="292" src="https://img-blog.csdnimg.cn/direct/e0146f8356834fd4b6062ab8034512a8.png" width="1200">wget获取的文件将保存在运行该条命令下的目录中；

若想保存到指定目录下，使用`wget -P 目录 网址`指令即可。
