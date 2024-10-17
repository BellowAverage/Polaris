
--- 
title:  Python打包成EXE 
tags: []
categories: [] 

---
## 一、使用Pyinstaller

>  
 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller 


### 1.2Pyinstaller打包步骤

>  
 Pyinstaller -F -w -i apple.ico py_word.py 


结果：

<img alt="" height="629" src="https://img-blog.csdnimg.cn/9a20651265784a8394ffaff3adfa2ae9.png" width="1200">

 运行结果：

<img alt="" height="273" src="https://img-blog.csdnimg.cn/f0f79dccb8a04744bce2c0177aafac50.png" width="1159">

##  二、使用Auto-py-to-exe

auto-py-to-exe 是一个用于打包 python 程序的程序。auto-py-to-exe 是一个基于  的程序，主要用于 python 程序打包。相比于 pyinstaller ，它多了 UI 界面，这使我们使用起来更为简单，方便，非常适合新手使用。

### 2.1安装 auto-py-to-exe

首先我们要确保我们的 python 环境要大于或等于 2.7

然后在 cmd 里面输入：pip install auto-py-to-exe ，输入完成之后，pip 就会安装 auto-py-to-exe 包了。

>  
 pip install auto-py-to-exe -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller 


安装完成之后，我们就可以输入：auto-py-to-exe，来启动 auto-py-to-exe 程序了。  

>  
 auto-py-to-exe 


<img alt="" height="1008" src="https://img-blog.csdnimg.cn/74f7ff8fbb4344e7b38fdc59eaa9e6d6.png" width="975">

###  2.2介绍
- Script Location 主要是指定我们要打包的 python 文件- One Directory-那么程序打包完成后会是一个文件夹的形式展现； One File-那么程序打包完成后就一个 .exe 文件- Console Window-主要设置打包程序运行时，是否出现控制台；Console Based - 当打包的程序运行时会显示一个控制台界面；Window Based (hide the console) -会隐藏控制台界面，主要用于带有 GUI 的 python 程序打包-  Icon-用于指定打包程序的图标 
## 三、报错：包不存在

<img alt="" height="746" src="https://img-blog.csdnimg.cn/d6859ae5b0c14f1b95b497ad49fcbc14.png" width="1200">

<img alt="" height="748" src="https://img-blog.csdnimg.cn/412b05a4aaf049219bb92e4dd5dc210e.png" width="982">

<img alt="" height="283" src="https://img-blog.csdnimg.cn/6be5c1b4426845b097d77bc90c2bcbcf.png" width="991">

 把文件添加：

<img alt="" height="630" src="https://img-blog.csdnimg.cn/d55b656b749f4e06864fc7bd86977efc.png" width="946">

就可以完美运行了。
