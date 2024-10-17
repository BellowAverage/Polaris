
--- 
title:  毕设必备！Python智慧教室：考试作弊系统、动态点名等功能 
tags: []
categories: [] 

---
### 往期推荐 





### 项目简介

一个具备群体课堂专注度分析、考试作弊系统、动态点名等功能的Python智慧教室，使用多人姿态估计、情绪识别、人脸识别、静默活体检测等技术。

### 项目环境 
- Python 3.7- PyQt5- Pytorch1.8.1- 更多可参考requirements.txt文件- 人脸识别功能要使用gpu，需要自己编译gpu版的dlib- 最好用有gpu的设备运行嗷，没有gpu可能需要自己在项目里改
**补充：**

编译gpu版的dlib教程：

https://blog.csdn.net/qq_29168809/article/details/102655115

### 使用步骤 

#### 步骤1、配置环境

一些积累下来的报错和基本的解决方法，慢慢食用哦！

<img src="https://img-blog.csdnimg.cn/img_convert/c4fee6e9f324670dfc38ec0ce3e8bdf3.png" alt="c4fee6e9f324670dfc38ec0ce3e8bdf3.png">
- 安装VisualStudio，注意在Installer中勾选“单个组件”中的“用于Windows的C++ CMake工具”然后再安装，就像下图这样的：- 安装Anaconda- 在Anaconda中创建虚拟Python环境，版本是3.7- 在虚拟Python环境中安装cmake，运行如下指令：
```
pip install cmake
```
- 在虚拟Python环境中安装boost，运行如下指令：
```
pip install boost
```
- 安装项目工程根目录下的requirements.txt文件所指定的包，运行如下指令
（%REQUIREMENTS_PATH% 表示requirements.txt所在的文件夹的路径，比如requirements.txt在电脑中的绝对路径为：E:\Data\requirements.txt，则指令中的%REQUIREMENTS_PATH%就为：E:\Data，注意斜线是用 \ 还是 / 需要根据系统不同进行区分哈！）：

```
pip install -r %REQUIREMENTS_PATH%\requirements.txt
```

如果最终运行smart_classroom_app.py不成功，报错和某些包有关，记得和requirements.txt文件中的模块一个个比对，将同名的包一个个删掉再安装相同的版本。之后再试着运行smart_classroom_app.py文件。（插播一条广告：需要开通正版PyCharm的可以联系我，56元一年，正版授权激活，官网可查有效期，有需要的加我微信：poxiaozhiai6，备注：906。）
- 上pytorch官网的下载页面根据自己的机器配置找对应pytorch的安装指令，比如如下的指令：
```
pip3 install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio===0.11.0+cu113 -f
```

#### 步骤2、下载权重文件

百度云下载链接：https://pan.baidu.com/share/init?surl=6av6CXWrCgGkniCwCc3qqQ

提取码：uk26

下载smart_classroom_demo项目的权重文件放置到weights文件夹下。

#### 步骤3、运行smart_classroom_app.py

### 界面展示 

#### 作弊检测

视频是实时检测和播放的，可以选择视频文件或rtsp视频流作为视频源，视频通道下摄像头以外的选项在resource/video_sources.csv文件里设置。

#### 人脸注册

静默活体检测，照片不能用来注册

#### 动态点名

学生面向摄像头完成签到，可以多人同时进行签到

### 源码获取 

<img src="https://img-blog.csdnimg.cn/img_convert/496c098a1541ecffd378c4d2972872db.png" alt="496c098a1541ecffd378c4d2972872db.png">

长按识别下方二维码添加小二微信，发送暗号：**智慧教室**，免费领取。

<img src="https://img-blog.csdnimg.cn/img_convert/9b806a0f6e4ab20b25915e2b0ba18ca6.jpeg" alt="9b806a0f6e4ab20b25915e2b0ba18ca6.jpeg">

**不是机器人**

**耐心等待，不要着急**
