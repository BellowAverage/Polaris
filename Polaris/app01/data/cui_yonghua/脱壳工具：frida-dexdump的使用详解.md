
--- 
title:  脱壳工具：frida-dexdump的使用详解 
tags: []
categories: [] 

---
#### 一. **frida-dexdump概述**

**`frida-dexdump`**：是基于frida开发的脱壳工具，代码开源且操作简单。在内存中转存dex文件，能脱大部分的壳。

github地址：

#### 二. **工具使用方法有2种**:

一种是下载源码，通过运行 frida-dexdump文件中的 main.py 文件来进行脱壳; 另一种是通过命令进行脱壳，需要先安装frida-dump。

安装：`pip3 install frida-dexdump`

#### 三. **脱壳步骤**：

1、启动frida； 2、在设备中打开药脱壳的app; 3、运行frida-dexdump，可以加参数d（开启深度搜索模式）。

脱壳后的dex文件保存在同级目录下，以包名为文件名。
