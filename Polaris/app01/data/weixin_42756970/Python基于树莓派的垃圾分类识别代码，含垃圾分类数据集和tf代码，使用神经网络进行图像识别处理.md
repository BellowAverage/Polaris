
--- 
title:  Python基于树莓派的垃圾分类识别代码，含垃圾分类数据集和tf代码，使用神经网络进行图像识别处理 
tags: []
categories: [] 

---
Python基于树莓派的垃圾分类识别代码，含垃圾分类数据集和tf代码，使用神经网络进行图像识别处理 完整代码下载地址：

#### 材料清单

>  
 -  树莓派 1个 -  pca9685 16路舵机驱动板 1个 -  7寸可触摸显示屏一个 -  MG996R 舵机4个 -  垃圾桶4个 -  usb免驱动摄像头1个 -  树莓派GPIO扩展板转接线柱1个 -  硅胶航模导线若干  


#### 环境需求

#### 1.开发环境

>  
 神经网络搭建—python 依赖 tensorflow,keras 
 训练图片来源华为云2019垃圾分类大赛提供 
 <blockquote> 
  训练图片地址：https://developer.huaweicloud.com/hero/forum.php?mod=viewthread&amp;tid=24106 
  下载图片文件后将文件解压覆盖为 garbage_classify 放入 垃圾分类-本地训练/根目录 
 

神经网络开源模型— resnet50

>  
  models 目录需要手动下载resnet50 的模型文件放入 
  resnet50模型文件名：resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5 
  百度就可以找到下载放入即可：https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5 
 

#### 2.运行开发环境

>  
 进入 "垃圾分类-本地训练"目录 


>  
 <h2>环境初始化</h2> 
 - python3- 安装框架flask`pip3 install flask`- 安装tensorflow，keras等依赖 
 <blockquote> 
  - `pip3 install tensorflow==1.13.1`- `pip3 install keras==2.3.1 ` 
 

## 运行
- 1.命令`python3 train.py`开启训练- 2.命令`python3 predict_local.py`开启输入图片测试
###### 

#### 3. 训练服务模型部署

>  
 进入 "垃圾分类-服务部署"目录 
 <ol>-  output_model 目录存放的是本地训练完成导出的h5模型文件 <li> models 目录需要手动下载resnet50 的模型文件放入 
   <blockquote> 
    resnet50模型文件名：resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5 
    百度就可以找到下载放入即可：https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5 
   
1.  output_model 目录存放的是本地训练完成导出的h5模型文件 <li> models 目录需要手动下载resnet50 的模型文件放入 
   <blockquote> 
    resnet50模型文件名：resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5 
    百度就可以找到下载放入即可：https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5 
   </blockquote> </li>
>  
 <h2>环境初始化</h2> 
 - 安装框架flask`pip3 install flask`- 安装tensorflow，keras等依赖 
 <blockquote> 
  - `pip3 install tensorflow==1.13.1`- `pip3 install keras==2.3.1 ` 
 

## 运行
- 1.命令`python3 run.py`开启窗口本地调试- 2.命令`python3 flask_sever.py`开启服务部署- 3.命令`sh ./start.sh`开启后台运行服务部署
#### 4.树莓派界面搭建

>  
 基于nodejs electron-vue 
 强烈建议使用cnpm来安装nodejs库 
 进入 "树莓派端/garbage_desktop"目录 
 <h2>安装依赖</h2> 
 cnpm install 
 <h2>开发模式</h2> 
 cnpm run dev 
 <h2>打包发布</h2> 
 cnpm run build 


## 开发模式

#### 5.树莓派端flask-api接口操作硬件

>  
 进入"进入 “树莓派端/garbage_app_sever"目录” 
 注意树莓派应该开启I2C，确保pca9685 I2C方式接入后可显示地址 
 <blockquote> 
  命令：i2cdetect -y 1 
  查看 地址项 0x40是否已经接入树莓派 
 

运行 python3 app_sever.py 或者 sh start.sh 启动

若提示缺少依赖：
1. pip3 install adafruit-**pca9685**1. pip3 install flask
完整代码下载地址：
