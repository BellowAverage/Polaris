
--- 
title:  在服务器上安装mediapipe遇到的问题 
tags: []
categories: [] 

---
1.

我正在尝试使用命令`pip install mediapipe`安装最新版本的Mediapipe。

根据页面，最新版本是0.8.10.1，但命令是安装我的版本0.8.3。

我曾尝试使用此命令`pip install -U mediapipe==0.8.10.1`指定版本号，但随后收到以下错误：

ERROR: Could not find a version that satisfies the requirement mediapipe==0.8.6.2 (from versions: 0.7.10, 0.8.0, 0.8.1, 0.8.2, 0.8.3) ERROR: No matching distribution found for mediapipe==0.8.6.2

解决方法：

需要安装python 3.7+和x64版本才能安装`mediapipe（我的Python版本是3.6）`

之后运行程序出现报错

2.

'cv2' has no attribute 'gapi_wip_gst_GStreamerPipeline' (most likely due to a circular import)

#### 原因：

版本兼容性问题。

### 解决办法：

pip3 install --user --upgrade opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple


