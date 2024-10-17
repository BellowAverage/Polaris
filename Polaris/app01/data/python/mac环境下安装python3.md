
--- 
title:  mac环境下安装python3 
tags: []
categories: [] 

---
一、查看当前mac上的python版本

-首先打开终端

1.打开后输入python3确定电脑上是否已安装python3，如果输入python是查看mac上的自带版本

 命令：python3【直接回车】

出现下面是页面，表示已经安装python3 【退出时可输入：exit（）然后点回车】

<img alt="" height="570" src="https://img-blog.csdnimg.cn/a04cfbedf00843918e106edbb56e2c79.png" width="1138">

如果出现下面页面，表示还不存在python3哦（我电脑已经安装啦。所以只能用代码形式展示）

<img alt="" height="96" src="https://img-blog.csdnimg.cn/0142350c5030403abc495706f50d4d88.png" width="1200">

二、安装python3
- 1.第一种方法brew 安装python3：brew install python3- 2.第二种方法官网下载【链接: .】根据自己的需求下载自己需要的版本<img alt="" height="943" src="https://img-blog.csdnimg.cn/3f19c4cb53784b858649ee7a2f92cd87.png" width="1200">
 



三、安装pip

pip介绍：pip 是 Python 包管理工具，该工具提供了对Python 包的查找、下载、安装、卸载的功能。

如果你在 python.org 下载最新版本的安装包，则是已经自带了该工具。

Python 2.7.9 + 或 Python 3.4+ 以上版本都自带 pip 工具。

————————————————
<li> 
  <ul>- 1.查看pip是否安装
pip3 --version【python3版本的命令】

如下图是已经成功安装pip的状态

<img alt="" height="106" src="https://img-blog.csdnimg.cn/7690c17fa72f485dab05f4a8ee5277c9.png" width="1114"> 出现下面是页面，表示没有安装pip3

<img alt="" height="102" src="https://img-blog.csdnimg.cn/3b5d25a558f843ae9597b3f239fa9537.png" width="1200">2.安装pip3

终端输入命令：

curl  -o get-pip.py # 下载安装脚本

sudo python3 get-pip.py # 运行安装脚本

注意：用哪个版本的 Python 运行安装脚本，pip 就被关联到哪个版本。一般情况 pip 对应的是 Python 2.7，pip3 对应的是 Python 3.x。

3.pip3常用命令





显示版本和路径 pip3 --version

升级 pip pip3 install -U pip

安装包

pip install SomePackage # 最新版本

pip install SomePackage==1.0.4 # 指定版本

pip install 'SomePackage&gt;=1.0.4' # 最小版本
