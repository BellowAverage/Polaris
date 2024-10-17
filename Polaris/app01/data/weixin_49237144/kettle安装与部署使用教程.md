
--- 
title:  kettle安装与部署使用教程 
tags: []
categories: [] 

---
## kettle 官网下载与部署使用



#### 文章目录
- - <ul><li><ul><li><ul><li>- - - <ul><li>- - - - - - 


##### 1. 前言：

```
1. kettle 如今这款软件已更名为：pantaho data intergration 。
2. Pentaho最初由Pentaho公司创建，后来该公司于2015年被Hitachi Vantara收购，现已成为Hitachi Data Systems的一部分。 
3. Pentaho 是一款基于Java开发的开源商业智能（BI）工具套件，提供了全面的数据集成、数据分析、报表、仪表板、数据挖掘和工作流管理等功能。
4. 下载Pentaho Community Edition (CE)：
   - 如果您需要免费的开源版本，通常可以在官网提供的链接指引下前往社区版的下载源，例如 SourceForge 或 Github、其他托管平台。

5. 在安装PDI之前，请确保已完成以下安装：
    前提条件：
    - 在需要运行PDI (Pentaho Data Integration)的工作站或笔记本电脑上安装64位Java SE 11到18之间的任何Java SE版本都可以使用。
    - 对于Linux/Ubuntu安装，还需要安装libwebkitgtk-1.0-0以使PDI正常工作。

```

##### 2. 访问官方网站：

Pentaho在被Hitachi Vantara收购后，其官方网站可能会有所变动。请访问最新官方网站来获取下载链接：

|Pantaho Data Intergration 官网链接：
|------
|

<img src="https://img-blog.csdnimg.cn/direct/a5d50d579c6243999a4ef46ff59f798d.png#pic_center" alt="在这里插入图片描述">

##### 3. Download Pentaho

###### 3.1 官网首页**滑动到最底**，寻找下载链接：

<img src="https://img-blog.csdnimg.cn/direct/653abbe0c24c4840a0dac7a5050da0e4.png#pic_center" alt="在这里插入图片描述">

###### 3.2 跳转到下载界面后，选择 Pentaho Community Edition (CE)

<img src="https://img-blog.csdnimg.cn/direct/068fd9bcbabb433c902f6e73236487fe.jpeg#pic_center" alt="在这里插入图片描述">

###### 3.3 点击同意开源许可

<img src="https://img-blog.csdnimg.cn/direct/6d2961c33f6f4dfe811bb64fa9100ce3.png#pic_center" alt="在这里插入图片描述">

###### 3.4 选择Pentaho Data Integration (Base Install) 版本

<img src="https://img-blog.csdnimg.cn/direct/839412f322b14a8f82459f8a3f5e7cd0.png#pic_center" alt="在这里插入图片描述">

##### 4. 安装指南：
-  下载相应的安装包后，请参照官方提供的安装文档或社区指南进行安装和配置。 -  安装PDI客户端工具安装PDI (Pentaho Data Integration)客户端工具只有三个简单步骤 -  下载压缩包 从Hitachi Vantara Pentaho Community页面： https://www.hitachivantara.com/en-us/products/lumada-dataops/data-integration-analvtics/pentahocommunity-edition.htmlThe 下载适合您操作系统的压缩PDI构件的相应版本。 构件的版本和构建命名为：pdi -ce--.zip 
###### 4.2 解压 ZIP

右键解压缩，提取全部文件到当前文件下。

<img src="https://img-blog.csdnimg.cn/direct/6b4a0a2cdf144ecb891a81214efaa387.png#pic_center" alt="在这里插入图片描述">

###### 4.3 启动 PDI

进入 data integration 文件，找到 spoon.bat 双击运行，这时候就可以启动PDI。

<img src="https://img-blog.csdnimg.cn/direct/063155fcd6fd4b1a8a387670897a5aa7.png#pic_center" alt="在这里插入图片描述">

###### 4.4 成功进入后的界面如下：

<img src="https://img-blog.csdnimg.cn/direct/31747f9c33e74552bbce57382278e9f8.png#pic_center" alt="在这里插入图片描述">
