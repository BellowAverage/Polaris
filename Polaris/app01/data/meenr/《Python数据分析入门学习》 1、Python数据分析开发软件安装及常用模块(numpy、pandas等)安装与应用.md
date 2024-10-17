
--- 
title:  《Python数据分析入门学习》 1、Python数据分析开发软件安装及常用模块(numpy、pandas等)安装与应用 
tags: []
categories: [] 

---
## 《Python数据分析入门学习》 1、Python数据分析开发软件安装及常用模块安装与应用



#### 目录
- - <ul><li>- - <ul><li>- <ul><li>- - - - - - - - - - - <ul><li>


### 1 学习目标和内容

本次需要学习的内容主要有以下两点： (1) 熟悉Python数据分析与挖掘开发环境； (2) 了解常用的Python数据挖掘分析模块numpy、pandas、Sklearn、matplotlib；

### 2 软硬件要求与环境搭建

#### 2.1 软硬件要求

##### 2.1.1 设备要求

(1) 硬件设备要求：64位台式电脑或笔记本电脑，4G、256G以上内存 (2) 操作系统要求：Windows 7、Windows10或Mac操作系统 (3) 网络要求：连接网络

##### 2.1.2 环境要求

(1) Python版本要求：Python3.6以上 (2) 开发工具：PyCharm或Spyder

#### 2.2 开发环境搭建

##### 2.2.1 Anaconda环境

**第一步：下载Anaconda安装包** 可从官网下载所需的安装包，官网地址如下：https://www.anaconda.com/ 由于官网下载较慢，可通过此公众号链接回复相关序号或关键词可获得安装包等资料。 公众号链接地址：

**第二步：完成安装** 安装步骤可参考另一篇文章即可，点击链接可阅读，这里就不再赘述了：  https://blog.csdn.net/meenr/article/details/121452678

##### 2.2.2 开发工具

建议使用Anaconda安装后自带的 **Spyder** 软件进行代码编写和开发，如下图Anaconda安装完成后开始菜单中文件夹里可以找到。 <img src="https://img-blog.csdnimg.cn/de898de50aff4f5fa3a8dda5b0c84f0b.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_15,color_FaaFFF,t_70#pic_center" alt="在这里插入图片描述" width="260">

或者另行安装**PyCharm**。 同样的pycharm的安装包也可以在上述公众号获得，不建议安装专业版，专业版只能试用，要么付费购买要么破解，还是比较麻烦的。这里建议安装社区版就可以了，应有功能也都有，完全能够满足开发需求，官网链接如下： https://www.jetbrains.com/pycharm/download/#section=windows 如下图选择对应的操作系统，再下载社区版安装即可。 <img src="https://img-blog.csdnimg.cn/322a23feb5d24ad4b62d8a132c1b0146.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_20,color_FaaFFF,t_70#pic_center" alt="在这里插入图片描述" width="600">

### 3 常用模块的安装

#### 3.1 基于Anaconda本地环境

Anaconda已经集成本次需要使用的第三方包，无需安装

#### 3.2 基于Python3.7的虚拟环境

### 4 常用模块的简单应用

#### 4.1 测试numpy

应用numpy创建各类数组，代码如下：

```
# -*- coding: utf-8 -*-
"""==============================
#@Project : demo1
#@File    : use_numpy
#@Software: PyCharm
#@Author  : Echo
#@Email   : robot1483693261@163.com
#@Date    : 2022/5/5 21:25
#@Desc    : 
=============================="""
import numpy as np

print('''创建数组''')
arr1 = np.array([2, 3, 4])
print(arr1)
arr2 = np.array([(1.3, 9, 2.0), (7, 6, 1)])
print(arr2)
arr3 = np.zeros((2, 3))
print(arr3)
arr4 = np.identity(3)
print(arr4)
arr5 = np.random.random(size=(2, 3))
print(arr5)
arr6 = np.arange(5, 20, 3)
print(arr6)
arr7 = np.linspace(0, 2, 9)
print(arr7)

```

#### 4.2 测试pandas

应用pandas和numpy

```
# -*- coding: utf-8 -*-
"""==============================
#@Project : demo1
#@File    : use_pandas
#@Software: PyCharm
#@Author  : Echo
#@Email   : robot1483693261@163.com
#@Date    : 2022/5/5 21:33
#@Desc    : 
=============================="""
import pandas as pd
import numpy as np
data = {<!-- -->'id': ['Jack', 'Sarah', 'Mike'],
        'age': [18, 35, 20],
        'cash': [10.53, 500.7, 13.6]}
df = pd.DataFrame(data)
print(df)

df2 = pd.DataFrame(data, columns=['id', 'age', 'cash'], index=['one', 'two', 'three'])
print(df2)
print(df2['id'])

s = pd.Series({<!-- -->'a': 4, 'b': 9, 'c': 16}, name='number')
print(s)
print(s[0])
print(s[:3])
print(s['a'])

s['d'] = 25
print(s)
#
print(np.sqrt(s))
print(s * s)
print(df['id'])

df['rich'] = df['cash'] &gt; 200.0
print(df)

del df['rich']
print(df)


```

#### 4.3 测试scipy

应用scipy和numpy

```
# -*- coding: utf-8 -*-
"""==============================
#@Project : demo1
#@File    : use_scipy
#@Software: PyCharm
#@Author  : Echo
#@Email   : robot1483693261@163.com
#@Date    : 2022/5/5 22:15
#@Desc    : 
=============================="""
from scipy import poly1d
import numpy as np


p = poly1d([3, 4, 5])
print(p)
print(p * p)
print(p.integ(k=6))
print(p.deriv())
p([4, 5])


def addsubtract(a, b):
    if a &gt; b:
        return a - b
        pass
    else:
        return a + b
        pass
    pass


vec_addsubtract = np.vectorize(addsubtract)
print(vec_addsubtract([0, 3, 6, 9], [1, 3, 5, 7]))


```

#### 4.4 测试sklearn

应用sklearn

```
# -*- coding: utf-8 -*-
"""==============================
#@Project : demo1
#@File    : use_sklearn
#@Software: PyCharm
#@Author  : Echo
#@Email   : robot1483693261@163.com
#@Date    : 2022/5/5 22:19
#@Desc    : 
=============================="""
from sklearn import datasets
from sklearn import svm

print('加载数据集')
digits = datasets.load_digits()
print(digits.data)
print(digits.target)

print('训练和预测')
clf = svm.SVC(gamma=0.0001, C=100)
clf.fit(digits.data[:-1], digits.target[:-1])

# print(clf.predict(digits.data[-1]))  # 报错，可能是维度错误，加一个冒号
print(clf.predict(digits.data[:-1]))


```

#### 4.5 测试matplotlib

应用用matplotlib绘制简单函数图像：

##### 4.5.1 案例一：sin(x)函数图像和cos(x^2)函数图像

<img src="https://img-blog.csdnimg.cn/075cb336d7c14e63922345f6daf39ff6.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_20,color_FaaFFF,t_70#pic_center" alt="在这里插入图片描述" width="400">

```
# -*- coding: utf-8 -*-
"""==============================
#@Project : demo1
#@File    : use_matplotlib
#@Software: PyCharm
#@Author  : Echo
#@Email   : robot1483693261@163.com
#@Date    : 2022/5/6 19:12
#@Desc    : 
=============================="""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x ** 2)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.plot(x, z, "b--", label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2, 1.2)
plt.legend()
plt.show()


```

### 下篇预告

**《Python数据分析入门学习》系列的第二篇，即下一篇内容主要是简单的数据预处理。敬请期待~~**

### 更多内容

CSDN主页地址： 
