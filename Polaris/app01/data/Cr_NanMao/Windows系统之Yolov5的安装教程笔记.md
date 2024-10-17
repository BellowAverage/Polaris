
--- 
title:  Windows系统之Yolov5的安装教程笔记 
tags: []
categories: [] 

---
### 第一步：安装Anaconda环境

  可以在官网下载：下载。

下载完成后会在开始菜单中多出一个快捷方式，和一些Anaconda的子程序。比如常用的“Anaconda Prompt（anaconda）”。



### 第二步：下载Yolov5的源码

    Yolov5源码的 Github地址：    解压到自定义目录中。

<img alt="" height="469" src="https://img-blog.csdnimg.cn/85b2b7235faa4a008e3e02fae64ac679.png" width="661">



### 第三步：下载Yolov5的预训练模型（`yolov5s`、`yolov5m`、`yolov5l`、`yolov5x`）

 下载地址：

（如果上面的链接下载不了，可以使用CSND里别人的共享文件：）

下载完成之后将四个.pt文件放到Yolov5的根目录下

<img alt="" height="556" src="https://img-blog.csdnimg.cn/30cfd4564cc44cb3b5c4c35021b016a6.png" width="658">





### 第四步：安装Yolov5

先安装Yolov5所需模块：

在命令行窗口打开Yolov5安装的根目录 ，如下：（安装比较慢，需要耐心等待）

<img alt="" height="441" src="https://img-blog.csdnimg.cn/21e6db62609540c2b2b110853a7c4439.png" width="745">





### 第五步：测试Yolov5

#### 1.图片测试

在源码中已有bus.jpg和zidane.jpg图片数据，路径如下：<img alt="" height="493" src="https://img-blog.csdnimg.cn/37d2cfe141394e778d80e8855fc2690f.png" width="551">

在命令行中输入：

```
python detect.py --source ./data/images/bus.jpg
```



```
python detect.py --source ./data/images/zidane.jpg
```

运行结果如下：

<img alt="" height="263" src="https://img-blog.csdnimg.cn/59a23d23f4ab4960bd6e62488d773584.png" width="962">

<img alt="" height="323" src="https://img-blog.csdnimg.cn/199a691708984fcf9c4ed7e1f9132c57.png" width="967">

 这两个模型输出的结果保存在文件夹detect中

<img alt="" height="260" src="https://img-blog.csdnimg.cn/68d546e4e7054dac87f4a160798c51e8.png" width="654"><img alt="" height="334" src="https://img-blog.csdnimg.cn/eef316a7507a4e019954f45a1ed003ae.jpeg" width="251"><img alt="" height="200" src="https://img-blog.csdnimg.cn/3d27b0a48eed40bd8927bd5c2fa54bc2.jpeg" width="355">



####  2.视频测试

使用自己拍摄的一小段视频放入images文件夹中

<img alt="" height="210" src="https://img-blog.csdnimg.cn/3be89ff89e404cdd86a8420cf664933f.png" width="486">

在命令行中输入下面这行代码：

```
python detect.py --source ./data/images/IMG_7772.mp4
```

<img alt="" height="370" src="https://img-blog.csdnimg.cn/d6ad94a371ca45f79bf914f1bb490ab6.png" width="954">

 运行结果如下：<img alt="" height="498" src="https://img-blog.csdnimg.cn/02ba51ba76304f8a97d295651d8b78e7.png" width="993">







进行完以上的测试，说明Yolov5已经安装完成了。



-------今天不学习，明天变垃圾。-------
