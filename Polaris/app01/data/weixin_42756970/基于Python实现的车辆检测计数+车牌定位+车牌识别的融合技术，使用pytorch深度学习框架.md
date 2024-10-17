
--- 
title:  基于Python实现的车辆检测计数+车牌定位+车牌识别的融合技术，使用pytorch深度学习框架 
tags: []
categories: [] 

---
## 车辆检测+计数+车牌检测与车牌识别

##### 介绍

基于pytorch深度学习框架，实用开源模型yolov4实现模板检测与yolov5实现车牌检测与LPRNet实现车牌检测 完整代码下载地址： 基于win10系统，实用anaconda配置python环境，在anaconda里面下载vscode对项目进行编辑，

##### 软件架构

<img src="https://img-blog.csdnimg.cn/594e192abcf54ba1880a884b9e8ba27c.png" alt="在这里插入图片描述">

##### 安装教程



##### [简洁版环境配置：]
-  last.pt 权重文件太大，不能直接上传到码云，通过百度云方式分享，下载后，放入weights文件夹。 -  链接：https://pan.baidu.com/s/1OmMVqckyMDosopfwv52zTQ -  提取码：je0x -  有码友发来这样的消息： <img src="https://img-blog.csdnimg.cn/d4d28fe1c10e4cdfb2b5e068c199d7a0.png" alt="在这里插入图片描述"> -  所以上传到百度云： 链接：https://pan.baidu.com/s/1sG9VdVt_HR-mi53UcII3ZA 提取码：n7uc 
编辑器我选择的是vscode，用anaconda创建虚拟python环境可以很好的分离项目，独立起来，方便。
- pytorch安装：- 官网推荐的安装代码如下，我使用的是Cuda10的版本：
```
-  CUDA 10.0
- pip install torch===1.2.0 torchvision===0.4.0 -f https://download.pytorch.org/whl/torch_stable.html

-  CUDA 9.2
- pip install torch==1.2.0+cu92 torchvision==0.4.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html

-  CPU only
- pip install torch==1.2.0+cpu torchvision==0.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

```
- 给出网盘链接：- 链接：https://pan.baidu.com/s/1YwcoaSRmNaeWZfHWkZ8lJg- 提取码：9i28- 这样下载的速度比较慢，可以通过下载whl文件在本地进行安装。
下载完成后找到安装路径： <img src="https://img-blog.csdnimg.cn/73b7ebdaabe0435680891194df14f542.png" alt="在这里插入图片描述">

在cmd定位过来后利用文件全名进行安装即可 <img src="https://img-blog.csdnimg.cn/80c1e546dcf54c4ca26fa8a154ab777c.png" alt="在这里插入图片描述">

安装有问题可以跳转到保姆级教程：

##### 使用说明
1. 运行detect.py：实现对 /inference/images 路径下的图片和视频进行目标检测，卡车计数，和车牌检测与识别1. 在/inference/output 路径下可看到输出情况 <img src="https://img-blog.csdnimg.cn/ff0a008cf8584c9b87d0b417eca2f1a6.png" alt="在这里插入图片描述">
##### 结果展示

<img src="https://img-blog.csdnimg.cn/d6a9e92abf9c48c98a23be36066d28f1.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b6d2050387a646df89fbbeb89699ae59.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d2d0d7fe75d445e4b95bd397dc833b3f.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/9704923f9e1b4ba09586e65a1050f2a6.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/0f36520ec75347768b0c5199546c1e9e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/a0037774552947d0851d0a96013a0bb2.png" alt="在这里插入图片描述">

##### 小鸡汤：

很多坑要自己去踩才能成长的，动不动就把问题抛给我，我除了又成长了一遍，你们还得到了什么。 你们碰到99%的问题，通过搜索引擎都是能解决的。 要善于自己动手，发现问题不是啥本事，发现问题并解决问题才是本事。 我的代码已经写得很清楚了，在框架方向基本无误的情况下，是可以通过debug调通代码的。

完整代码下载地址：
