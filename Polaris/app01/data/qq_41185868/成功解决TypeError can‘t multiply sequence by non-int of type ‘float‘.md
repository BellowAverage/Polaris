
--- 
title:  成功解决TypeError: can‘t multiply sequence by non-int of type ‘float‘ 
tags: []
categories: [] 

---
成功解决TypeError: can't multiply sequence by non-int of type 'float'





**目录**













## 解决问题

TypeError: can't multiply sequence by non-int of type 'float'



## 解决思路

类型错误：不能将sequence乘以“float”类型的非整数







## 解决方法

两个数据类型不一致，不能够进行multiply运算！重新检查输入数据类型，本案例问题的背景是在特征工程过程中遇到的，

**feature**: string or list．feature or feature list to investigate,for one-hot encoding features, feature list is required．字符串或列表，要调查的特征或特征列表，对于one-hot编码特征，需要特征列表。

经过分析，发现输入的数据类型为object，而函数要求int或者float类型。 故更改数据变量类型即可！














