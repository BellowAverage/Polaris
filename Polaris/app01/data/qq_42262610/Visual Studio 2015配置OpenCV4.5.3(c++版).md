
--- 
title:  Visual Studio 2015配置OpenCV4.5.3(c++版) 
tags: []
categories: [] 

---
### 学习目标

<input checked disabled type="checkbox"> 学会在Visual Studio 2015部署Opencv

<input checked disabled type="checkbox"> 一个简单的C++ Opencv实例

### 一、 Visual Studio 2015配置4.5.3

#### 1.1 Visual Studio 2015

  网上关于Visual Studio 2015的下载，也有很多介绍。大家自行搜索安装。

#### 1.2 OpenCV

  OpenCV大家根据需求下载相应版本，官网地址，下载后是opencv-4.5.3-vc14_vc15.exe的应用程序，双击后解压，如下图。

#### 1.3 opencv环境变量配置

   1. 控制面板 --&gt;系统 --&gt;高级系统设置 (或者右击此电脑–&gt;属性–&gt; 高级系统设置)

 

2. 环境变量 --&gt; 系统变量中选择Path --&gt; 编辑 --&gt;新建。

   将下载安装好的opencv文件夹打开，一直打开到D:\Opencv4.5.3\opencv\build\x64\vc15\bin目录，将该路径添加进去 --&gt; 确定(每一步确定都要点)。

#### 1.4 Visual Studio 2015配置Opencv

   1. 打开Visual Studio 2015 --&gt; 新建 --&gt; 空项目。

 2. 打开视图–&gt; 其他窗口 --&gt; 属性管理器。

  3. 选择Debug | x64 --&gt; 右击选择属性 。

4. 选择VC++目录中的包含目录 --&gt; 编辑-- &gt; 将安装路径中:

D:\Opencv4.5.3\opencv\build\include

D:\Opencv4.5.3\opencv\build\include\opencv2

添加到包含目录中

下图中的D:\Opencv4.5.3\opencv\build\include\opencv不用填写

5. 选择VC++ 目录中的 库目录 --&gt; 编辑-- &gt; 将安装路径中:

D:\Opencv4.5.3\opencv\build\x64\vc15\lib

添加到库目录中

6. 选择链接器 --&gt; 输入 --&gt; 附加依赖项 --&gt; 编辑 --&gt; 将安装路径中:

 D:\Opencv4.5.3\opencv\build\x64\vc15\lib\opencv_world453d.lib

添加到附加依赖项中

注：453为OpenCV版本，我的版本为4.5.3

### 二、 简单的C++ Opencv实例

读入的图片路径应该使用‘\\分开。


