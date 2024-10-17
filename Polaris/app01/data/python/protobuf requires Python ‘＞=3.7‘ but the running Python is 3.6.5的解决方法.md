
--- 
title:  protobuf requires Python ‘＞=3.7‘ but the running Python is 3.6.5的解决方法 
tags: []
categories: [] 

---
安装tensorflow的时候遇到几个坑，先是tensorflow不支持最新版本的python，于是重新安装python3.6版。安装tensorflow仍报错，通过百度无果，后自己尝试解决，故在此记录此坑。

报错信息：protobuf requires Python '&gt;=3.7' but the running Python is 3.6.5

解决方法：更新pip后重新安装tensorflow。

更新命令：python -m pip install --upgrade pip
