
--- 
title:  脱壳工具：Youpk的使用详解 
tags: []
categories: [] 

---
#### 一. Youpk概述

`Youpk`基于ART的主动调用的脱壳机，主要针对dex整体加固和各式各样的dex抽取加固。

目前 Youpk 只支持 pixel 1代。所以必须需要 pixel 1代手机，而且需要刷入对应的系统。

Youpk可以处理大部分的加固，一些企业版的加固也能处理，脱壳效果非常好。

github地址：

基本流程如下:
1. 从内存中dump DEX1. 构造完整调用链, 主动调用所有方法并dump CodeItem1. 合并 DEX, CodeItem
常用的脱壳工具对比： <img src="https://img-blog.csdnimg.cn/1db88b7fd8bf407e85ec8a6a0b32ce96.png" alt="在这里插入图片描述">

#### 二. 使用Youpk 脱壳步骤：

**步骤一：配置包名**，配置待脱壳的app包名，生成config文件：`adb shell "echo cn.youlor.mydemo &gt;&gt; /data/local/tmp/unpacker.config"`

**步骤二：启动 APP**，每隔10秒将自动重新脱壳； **步骤三：从手机中提取数据**，pull出dump文件，dump文件路径为 /data/data/包名/unpacker **步骤四**：使用 dex2jar 导出jar 包 **步骤五**：使用 jd-gui 查看 jar 包

案例1： 案例2：

#### 三. 常见问题

1、 dump中途退出或卡死，重新启动进程，再次等待脱壳即可 2、当前仅支持被壳保护的dex, 不支持App动态加载的dex/jar
