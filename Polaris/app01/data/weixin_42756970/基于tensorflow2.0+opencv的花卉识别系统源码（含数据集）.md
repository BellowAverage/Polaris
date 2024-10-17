
--- 
title:  基于tensorflow2.0+opencv的花卉识别系统源码（含数据集） 
tags: []
categories: [] 

---
## 花卉识别-基于tensorflow2.3实现

完整代码下载地址：

### 文件目录

```
# 数据下载地址 https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz
# 参考代码 https://tensorflow.google.cn/tutorials/images/classification
flower_tensorflow2.0
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
cd flower_tensorflow2.3
conda create -n flower_demo 
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

图形化界面 <img src="https://img-blog.csdnimg.cn/8d222adc6122415fa34a7f5f2a68af0d.png" alt="在这里插入图片描述">

完整代码下载地址：
