
--- 
title:  如何用pip升级python版本,python的pip升级没反应 
tags: []
categories: [] 

---
大家好，小编为大家解答python的pip如何更新到最新版本的问题。很多人还不知道如何用pip升级python版本，现在让我们一起来看看吧！

### 1、pip如何升级

第一步：首先检测一下我们电脑是否安装了python，打开命令提示框，输入python，如果安装了python就会提示出版本信息。

第二步：执行exit()命令退出python运行环境。

第三步：查看我们的python环境是否安装了pip，执行pip命令会出现如下信息。

第四步：查看我们目前pip版本的信息，执行pip show pip命令，会提出相信的版本信息。

第五步：执行pip升级命令进行升级，命令是python -m pip install -U pip就行了，安装成功会提示你卸载了旧版本并且安装了最新版本的pip

### 2、python3.6的pip升级不到22.31



您可以尝试使用以下命令来升级您的pip：python3 -m pip install --upgrade pip。如果仍然无法升级到22.31，则可能是由于Python 3.6版本过低所导致的。在这种情况下，您可以尝试升级到Python 3.7或更高版本，之后再尝试升级pip。

### 3、如何通过pip命令升级python

安装Python包，的确是pip最为方便了，简单快捷，因为它直接是从pypi上面下载文件，保证文件的安全性和可靠性，并且资源丰富；



下面是安装步骤：



下载 setuptools，注意对应 Python 的版本，完成后运行 exe 即可完成安装







下载 pip







安装 pip



5.1 解压



5.2 运行CMD，进入



5.3 用CD命令进入 pip 解压目录



5.4 输入 "python install"



5.5 添加 path = C:\Python26\ArcGIS10.0\Scripts



验证是否安装成功，运行CMD，进入命令行，输入pip；



如果出现pip的用法介绍，说明安装成功。



进入命令行，输入 "pip install package"，package为名称，就可以随意使用了。
