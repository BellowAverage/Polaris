
--- 
title:  基于Python tensorflow2.3实现的水果识别系统源码+模型+数据集，卷积神经网络的入门案例 
tags: []
categories: [] 

---
## 水果识别-基于tensorflow2.3实现

水果识别是卷积神经网络的入门案例，这里我将模型的训练、测试、保存以及使用整合在了一起，至于原理部分，大家可以参考知乎或者B站上的回答，在这里我就不赘述了 完整代码下载地址：

#### 数据集和模型下载地址

>  
 链接：https://pan.baidu.com/s/1ELzk3bjqhxN3Ej_5_3i1dg 提取码：vxn4 复制这段内容后打开百度网盘手机App，操作更方便哦–来自百度网盘超级会员V4的分享 


### 文件目录

```

├─ data_read.py # 数据读取
├─ data_split.py # 数据切分
├─ images  # 图片文件
│    ├─ 123.jpg
│    ├─ init.png
│    ├─ logo.png
│    ├─ target.png
│    ├─ 主页面.png
│    └─ 关于.png
├─ window.py # ui界面
├─ models # 模型
│    ├─ cnn_flower.h5
│    └─ mobilenet_flower.h5
├─ readme.md 
├─ requirements.txt # 安装需求
├─ test_model.py # 模型测试
└─ train_model.py # 模型训练

```

### 如何使用

首先你需要git项目到你的本地

确定你的电脑已经安装好了PyQt5、tensorflow2.0以及opencv-python等相关软件，你可以执行下列命令进行安装

```
cd fruits_tensorflow2.3
conda create -n fruits_demo 
pip install -r requirements.txt

```

如果你想要重新训练你的模型，请执行

```
python train_model.py

```

如果你想要测试模型的准确率，请执行

```
python test_model.py

```

如果你想看看图形化的界面，请执行

```
python window.py

```

### 执行效果

图形化界面 <img src="https://img-blog.csdnimg.cn/img_convert/ac8389ecddf5a9ec46dccfa4ca8351ba.png" alt="image-20210316094731364">

web端

<img src="https://img-blog.csdnimg.cn/img_convert/744cb15a2c6ddb110587a899c4ab1a1e.png" alt="image-20210316094613981">

完整代码下载地址：
