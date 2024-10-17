
--- 
title:  第五章 YOLOv3训练自己的数据集 
tags: []
categories: [] 

---
#### 数据集的准备

      在官网中下载VOC2012数据集（或在本文附件5中下载）

<img alt="" height="117" src="https://img-blog.csdnimg.cn/direct/cee00c3144934128b9de2bd233299654.png" width="317">

图13

      使用voc_annotation.py生成2012_train.txt和2012_val.txt标注文件，如图14所示：

<img alt="" height="175" src="https://img-blog.csdnimg.cn/direct/7045924ced494c6d8b1e46aaf1b9b534.png" width="329">

图14

#### 模型训练

（1）训练所需要的环境如下：

>  
 Python==3.5.6 
 Keras==2.1.5 
 Tensorflow==1.10.0 


（2）下载附件5 yolov3-keras，解压后，使用vs code打开项目文件夹（图15），并使用上述环境运行train.py进行模型训练。

<img alt="" height="608" src="https://img-blog.csdnimg.cn/direct/c0304ff47b4a4b02a2218f3f74a8e565.png" width="290">

图15

<img alt="" height="466" src="https://img-blog.csdnimg.cn/direct/ee5d462530944618a27350c252a4c93b.png" width="1011">

图16

      （3）训练结束后，项目根目录下会生成logs/000文件夹，文件夹中存放的是网络结构文件.h5和日志文件。前者用于.pb文件的生成，而后者可用来分析训练状态与可视化网络，如图17所示。

<img alt="" height="74" src="https://img-blog.csdnimg.cn/direct/e351b2cbb22f469091e13760474b9109.png" width="431">

图17

今天不学习，明天变垃圾！！！
