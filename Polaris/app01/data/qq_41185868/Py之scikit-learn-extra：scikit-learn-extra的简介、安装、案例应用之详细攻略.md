
--- 
title:  Py之scikit-learn-extra：scikit-learn-extra的简介、安装、案例应用之详细攻略 
tags: []
categories: [] 

---
Py之scikit-learn-extra：scikit-learn-extra的简介、安装、案例应用之详细攻略





**目录**













## **scikit-learn-extra的简介**

scikit-learn-extra - 与scikit-learn兼容的一组有用工具。scikit-learn-extra是一个用于机器学习的Python模块，它扩展了scikit-learn。它包括一些有用的算法，但由于其新颖性或引用数量较低等原因，不符合scikit-learn的包含标准。

scikit-learn-extra 是一个 Python 模块，用于机器学习，它扩展了 scikit-learn。与 scikit-learn 不同，scikit-learn-extra 包含一些非常有用的算法，但由于它们的新颖性或引用数量较低，不符合 scikit-learn 的包含标准。这些算法可能包括一些实验性的或者专门用于特定任务的模型。



## **scikit-learn-extra的安装**

scikit-learn-extra需要：

Python (&gt;=3.7) scikit-learn (&gt;=0.24)，以及其依赖项

```
pip install -i https://mirrors.aliyun.com/pypi/simple scikit-learn-extra
```

<img alt="" height="380" src="https://img-blog.csdnimg.cn/direct/e73b3f86fbc645d9b5d90bd56a326320.png" width="1200">









## **scikit-learn-extra的案例应用**

### **<strong><strong>1、使用 scikit-learn-extra 中的 IsolationForest 模型进行异常检测**</strong></strong>

```
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn_extra.ensemble import IsolationForest

# 创建一个示例数据集
X, _ = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

# 将数据集分成训练集和测试集
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# 初始化 IsolationForest 模型
isolation_forest = IsolationForest(random_state=42)

# 在训练集上拟合模型
isolation_forest.fit(X_train)

# 使用模型进行异常检测
outliers = isolation_forest.predict(X_test)

# 打印异常检测结果
print("Outliers:", outliers)

```








