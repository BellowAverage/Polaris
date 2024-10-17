
--- 
title:  symbol lookup error: ./Log4cppTest: undefined symbol: _ZN7log4cpp8Appender29AppenderMapStorageInitia 
tags: []
categories: [] 

---
### 错误：

linux （centos7）环境下运行搭建有 log4cpp 框架的 C/C++文件，出现如下错误：

```
[root@node2 test]# ./Log4cppTest 
./Log4cppTest: symbol lookup error: ./Log4cppTest: undefined symbol: _ZN7log4cpp8Appender29AppenderMapStorageInitializerC1Ev


```

### 问题：

出现上述问题的原因是找不到到 _ZN7log4cpp8Appender29AppenderMapStorageInitializerC1Ev 符号，是因为程序找不到相关的共享库，例如：liblog4cpp.so.5。

### 解决：

将 log4cpp 的相关 lib 目录，加入到 **ld.so.conf** 中：具体方法可以查看：

```
vim /etc/ld.so.conf
ldconfig

```
