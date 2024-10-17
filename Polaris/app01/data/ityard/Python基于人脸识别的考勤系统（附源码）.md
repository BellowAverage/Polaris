
--- 
title:  Python基于人脸识别的考勤系统（附源码） 
tags: []
categories: [] 

---
<img alt="" src="https://img-blog.csdnimg.cn/img_convert/c8192155de65ad0e9ce0a106425b75e8.png">

原文链接：https://blog.csdn.net/weixin_39653948/article/details/89291751

## 1. 项目简介

本项目使用Python3.6编写，Qt Designer（QT5）设计主界面，PyQt5库编写控件的功能，使用开源 DeepFace人脸识别算法进行人脸识别，使用眨眼检测来实现活体识别，使用OpenCV3实现实时人脸识别。同时，将班级学生信息，各班级学生人数、考勤信息录入到MySQL数据库中，方便集中统一化管理。因为本项目仅由我一个人开发，能力精力有限，实现了预期的绝大多数功能，但是活体检测功能还存在bug，主要表现是界面卡死，如果小伙伴对本项目中有不懂的地方或者发现问题提出解决方案，欢迎私聊我或者在此博客评论亦或在github提交。项目大概持续了两三个月的时间，在开发过程中，遇到过许多难题，参考了很多教程，才有了这个项目。????相信大家看到这里，一定是在比赛中或者是作业中遇到类似问题了，我也有过类似的经历，很清楚找不到解决方案，自己盲目摸索的苦恼，这也是我选择开源的原因，个人能力有限，但是希望本项目能给需要的小伙伴提供帮助，✨完整代码在文章结尾 。????如果对你有帮助的话，点个赞吧！

## 2. 系统前端设计

使用 Qt Designer 设计前端界面。

### 2.1 主界面

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/3bb7fe28df2098a22fb9ba03497e7aa4.png">

### 2.2 信息采集界面

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/b649f776d1b28c60033ce1866ca882d9.png">

## 3. 数据库存取信息

### 3.1 数据库可视化工具 Navicat

使用该软件是为了方便管理维护信息，如果有数据库基础，当然也可以选择其它方式。其主界面如下：<img alt="" src="https://img-blog.csdnimg.cn/img_convert/74c60edfbb8503808dc6a9acc52a7656.png"><img alt="" src="https://img-blog.csdnimg.cn/img_convert/4cbf9e462f38111396affc2eecf3eb48.png"><img alt="" src="https://img-blog.csdnimg.cn/img_convert/4a3ba0e68732acb8bd1be8ef18fb119c.png">

### 3.2 创建数据库流程

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/6cfd3137d219fff423e2bab8f8fa7695.png"><img alt="" src="https://img-blog.csdnimg.cn/img_convert/8fc65ca01da2aebfdc4f782bdf4311c8.png"><img alt="" src="https://img-blog.csdnimg.cn/img_convert/cf89e90eb7b7d61ee95cd6d54e040f7f.png"><img alt="" src="https://img-blog.csdnimg.cn/img_convert/e179fc6d6ee5a684d0dc6c8f6489c4b1.png"><img alt="" src="https://img-blog.csdnimg.cn/img_convert/0e5157325cb4e5f8cef98a3c74a0820d.png">

### 3.3 PyMySQL

项目中只使用了简单的写入、查询等几个常用命令，即使没有数据库基础的话，上手这个库也比较容易。看一下文档，基本就会了。

## 4. 系统功能介绍（正在更新）

### 4.1 信息采集

### 4.2 人脸识别

### 4.3 活体检测（存在bug）

目前的bug是，活体检测开启关闭之后，关闭人脸考勤，再关闭相机的时候会卡死。

### 4.4 查询考勤信息

### 4.5 查询学生信息

### 4.6 请假登记

## 5. 使用教程

### 5.1 系统环境配置

```
opencv+contrib
安装步骤：
1.https://www.lfd.uci.edu/~gohlke/pythonlibs/ 搜索contrib
2.找到对应你系统python版本的opencv+contrib下载
3.我安装的是：opencv_python-4.1.2+contrib-cp37-cp37m-win_amd64.whl
4.打开anaconda命令行 pip install opencv_python-4.1.2+contrib-cp37-cp37m-win_amd64.whl


cmake
官网下载.msi安装包 下载即可，安装注意导入系统环境变量


dilib
直接anaconda命令行中 pip install dlib（时间比较长）


freetype
pip install freetype-py


pymysql
pip install pymysql


pyqt5
pip install pyqt5

```

### 

### 5.2 需要修改源码

文件目录树：<img alt="" src="https://img-blog.csdnimg.cn/img_convert/ed47079ab9b798feda2f8656e0057630.png">
1.  安装 msqlservice 然后修改 `exacute.py`文件中的数据库连接代码。比如 `db = pymysql.connect("localhost", "root", "mysql105", "facerecognition")`。这首先需要在 navicat中创建数据库。 1.  如果不是通过本系统的信息采集功能采集的人脸照片，请将采集的人脸照片放到 `face_dataset/XX` 路径下，其中`XX`是学号（唯一索引），如果是通过系统采集的，则会自动存放在该路径下，不需要修改。 
### 5.3 使用步骤
1.  navicat创建数据库，打开数据库录入学生信息和班级信息； 1.  修改源码，连接到创建的数据库 1.  采集人脸照片，点击界面中的信息采集，在子窗口操作即可。 1.  训练人脸识别模型，点击界面中的更新人脸库 1.  开始考勤：打开相机 --&gt; 开始考勤 1.  Have fun! 
## 6. 源码获取

在公众号**Python小二**后台回复**考勤**免费获取。
