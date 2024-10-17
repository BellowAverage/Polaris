
--- 
title:  脱壳工具：dumpDex的使用详解 
tags: []
categories: [] 

---
#### 一. dumpDex概述

`dumpDex`： 一个开源的 Android 脱壳插件工具，需要xposed支持。可以用来脱掉当前市场上大部分的壳。（360加固、腾讯乐固、梆梆加固、百度加固均可脱壳）

支持大多数xposed环境的手机，暂不支持模拟器

github地址：，可以直接下载release的apk，也可以自行编译打包成apk安装到手机

#### 二. **使用方法**：

安装插件，重启手机，打开加固的apk，脱壳的后的dex会在/data/data/对应包路径/dump文件夹下

#### 三. 脱壳原理：

1、根据类名查找当前运行的 APP 是否存在支持的加密壳（360加固、爱加密、梆梆加固、腾讯加固、百度加固）；

2、存在支持的加密壳的情况下，根据手机的 Android 版本进行不同的处理，Android 8.0 及以上手机走 NDK 方式，其它低版本手机则走 Hook 方式；

3、Hook 方式，主要是通过 Hook Instrumentation 类的 newApplication() 方法和 ClassLoader 类的 loadClass() 方法，获取 Application 或 Activity 所在的 dex 的数据；

4、将这些数据导出到 APP 所在路径的 dump 子文件夹里的 dex 文件。
