
--- 
title:  Py之tensorflow-addons：tensorflow-addons的简介、安装、使用方法之详细攻略 
tags: []
categories: [] 

---
Py之tensorflow-addons：tensorflow-addons的简介、安装、使用方法之详细攻略







**目录**















## **tensorflow-addons的简介**

TensorFlow Addons 是一个符合成熟 API 模式的贡献仓库，但实现了在核心 TensorFlow 中尚不可用的新功能。TensorFlow 本身原生支持大量运算符、层、度量、损失和优化器。然而，在像机器学习这样快速发展的领域中，存在许多有趣的新发展，这些发展尚不能整合到核心 TensorFlow 中（因为它们的广泛适用性尚不明确，或者主要由社区的较小子集使用）。



## **tensorflow-addons的安装**

```
pip install tensorflow-addons
pip install -i https://mirrors.aliyun.com/pypi/simple tensorflow-addons
```

<img alt="" height="300" src="https://img-blog.csdnimg.cn/direct/16790523b9d84e9a88f9606d5b45b4c2.png" width="1200">





## **tensorflow-addons的使用方法**

### **<strong><strong>1、使用 TensorFlow Addons 中的功能：**</strong></strong>

TensorFlow Addons 提供了许多不在核心 TensorFlow 中的操作和功能。你可以根据你的需求选择合适的模块，比如 layers、activations、optimizers 等。例如，使用其中的 tfa.layers.SpectralNormalization 层：

```
import tensorflow as tf
import tensorflow_addons as tfa

from tensorflow_addons.layers import SpectralNormalization

model = tf.keras.Sequential([
    SpectralNormalization(tf.keras.layers.Dense(128)),
    tf.keras.layers.Activation('relu'),
    # 其他层和配置
])
```








