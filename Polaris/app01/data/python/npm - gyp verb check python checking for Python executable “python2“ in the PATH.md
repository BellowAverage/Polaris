
--- 
title:  npm - gyp verb check python checking for Python executable “python2“ in the PATH 
tags: []
categories: [] 

---
## 项目场景：

前端项目中依赖的包需要node sass,

## 问题描述

项目安装的时候报

```
npm - gyp verb check python checking for Python executable “python2“ in the PATH

```

node sass 需要依赖python，只好先装上python，过程不细说 装好之后，报错依旧。

## 原因分析：

会不会是装python的时候环境变量设置的python.exe这里是python2.exe，于是将python.exe复制一份改个名字python2.exe,在执行npm install，报错信息变了，报错信息的末尾打印出node版本16.3,。印象中node16.3版本跟项目中某个库的版本好像有冲突，从别的地方考了一个node12.x版本的node，配置好环境变量。

## 解决方案：

重新install，报错信息依旧，在vscode控制台打印node版本还是16.3，重启vscode，重新执行 npm install 问题解决。
