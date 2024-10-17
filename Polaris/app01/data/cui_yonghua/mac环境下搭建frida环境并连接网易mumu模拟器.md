
--- 
title:  mac环境下搭建frida环境并连接网易mumu模拟器 
tags: []
categories: [] 

---
### 一. frida概述

frida是基于Hook的动态分析工具。是一款基于 python+javascript 的 hook 框架，核心是用C编写的，可运行在 android、ios、linux、win等各个平台，主要使用的动态二进制插桩技术。

官网: 

文档: 

安卓相关文件: 

关于frda学习路线了，只需要了解两方面的内容： 1）主控端和目标进程的交互（message） 2）Python接口和js接口（查文档）

frida框架分为两部分： 1）一部分是运行在系统上的交互工具frida CLI。 2）另一部分是运行在目标机器上的代码注入工具 frida-serve。

### 二. mac下环境搭建

#### 2.1 安装adb工具

参考：

#### 2.2 安装frid
