
--- 
title:  用300行Python代码实现一个人脸识别系统源码，基于dlib 
tags: []
categories: [] 

---
## 用300行Python代码实现一个人脸识别系统

完整代码下载地址：

今天我们来python实现一个人脸识别系统，主要是借助了dlib这个库，相当于我们直接调用现成的库来进行人脸识别，就省去了之前教程中的数据收集和模型训练的步骤了。

<img src="https://img-blog.csdnimg.cn/img_convert/d244b4b8f408fdb75d77e0e6fd4f56e5.png" alt="image-20220109232328902">

### 基本原理

人脸识别和目标检测这些还不太一样，比如大家传统的训练一个目标检测模型，你只有对这个目标训练了之后，你的模型才能找到这样的目标，比如你的目标检测模型如果是检测植物的，那显然就不能检测动物。但是人脸识别就不一样，以你的手机为例，你发现你只录入了一次你的人脸信息，不需要训练，他就能准确的识别你，这里识别的原理是通过人脸识别的模型提取你脸部的特征向量，然后将实时检测到的你的人脸同数据库中保存的人脸进行比对，如果相似度超过一定的阈值之后，就认为比对成功。不过我这里说的只是简化版本的人脸识别，现在手机和门禁这些要复杂和安全的多，也不是简单平面上的人脸识别。

总结下来可以分为下面的步骤：
1. 上传人脸到数据库1. 人脸检测1. 数据库比对并返回结果
这里我做了一个简答的示意图，可以帮助大家简单理解一下。

<img src="https://img-blog.csdnimg.cn/img_convert/b5b5362e8fe4ad3c43207b92c3c5d43f.png" alt="image-20220109232309780">

### 代码实现

废话不多说，这里就是我们的代码实现，代码我已经上传到码云，大家直接下载就行，地址就在博客开头。

不会安装python环境的兄弟请看这里：

#### 创建虚拟环境

创建虚拟环境前请大家先下载博客开头的码云源码到本地。

本次我们需要使用到python3.7的虚拟环境，命令如下：

```
conda create -n face python==3.7.3
conda activate face

```

#### 安装必要的库

```
pip install -r requirements.txt

```

#### 愉快地开始你的人脸识别吧！

执行下面的主文件即可

```
python UI.py

```

或者在pycharm中按照下面的方式直接运行即可

<img src="https://img-blog.csdnimg.cn/img_convert/5eae441eb388057cf2c69fc05ef79516.png" alt="image-20220110104320212">

首先将你需要识别的人脸上传到数据库中

<img src="https://img-blog.csdnimg.cn/img_convert/698bbdf21d5610597568e298a6cdbf91.png" alt="image-20220110102015569">

通过第二个视频检测功能识别实时的人脸

<img src="https://img-blog.csdnimg.cn/img_convert/1f42a274027a58a05f686a7e76d2d5db.png" alt="image-20220110102134504">

完整代码下载地址：
