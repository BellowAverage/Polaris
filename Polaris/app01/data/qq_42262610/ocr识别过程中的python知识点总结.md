
--- 
title:  ocr识别过程中的python知识点总结 
tags: []
categories: [] 

---
一、Python [::-1]的简单理解与用法

从结果上来看，[::-1]的作用是对列表进行翻转，其中：：分别表示切片开始的索引和切片结束的索引，比方说：

a = [1, 2, 3, 4, 5] print(a[::-1])

b = "12345" print(b[::-1]) 输出：

[5, 4, 3, 2, 1] 54321 可以发现这个东西的用法和reversed函数是相同的，只不过更为简洁：

a = [1, 2, 3, 4, 5] print(list(reversed(a)))

b = "12345" print("".join(reversed(b))) 输出：

[5, 4, 3, 2, 1] 54321 那么这个东西的原理是什么呢？一般来说，我们见过一个冒号的情况比较多，用来做列表切片：

a = [1, 2, 3, 4, 5] print(a[:-1]) print(a[1:]) print(a[:]) 输出：

[1, 2, 3, 4] [2, 3, 4, 5] [1, 2, 3, 4, 5] 多一个冒号的话，新冒号后面的数字表什么呢？其实是表步长，比如：

a = [1, 2, 3, 4, 5] print(a[:-1]) print(a[:-1:]) print(a[:-1:1]) print(a[:-1:2]) 输出：

[1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 4] [1, 3]

 步长是正数的话，[a:b]是从a到b，往右读取，b应该比a大；而步长如果改成负数，[a:b]的含义仍然是从a到b，只是往左读取，所以此时b应该比a小，比如：

print(a[3:0:-1]) 输出：

[4, 3, 2] 自然而然的，如果不指定a，b，那么处理的范围是整个列表；步长为-1，表示整个列表从右往左读取，即翻转数组。

二、np.argsort()用法： np.argsort(a, axis=-1, kind='quicksort', order=None) 函数功能：将a中的元素从小到大排列，提取其在排列前对应的index(索引)输出。

 1、一维数组

先定义一个array数组x，然后使用函数

import numpy as np x=np.array([1,4,3,-1,6,9]) y=np.argsort(x) print('一维数组的排序结果：{}'.format(y)) 输出结果如下：

一维数组的排序结果：[3 0 2 1 4 5] 中间过程详细解释： ①输入为: [1,4,3,-1,6,9]，对应索引为：[0,1,2,3,4,5]，即 x[0]=1，x[1]=4，x[2]=3，x[3]=-1，x[4]=6，x[5]=9

②排序结果为: [-1,1,3,4,6,9] argsort()是提取排序结果元素在排列前对应的index(索引)输出。 根据排序前x[3]=-1可知，排序结果中，元素-1对应排序前的索引3； 根据排序前x[5]=9可知，排序结果中，元素9对应排序前的索引5； 以此类推，输出 排序后元素在排列前对应的index(索引）： 即：[3,0,2,1,4,5]

 三、np.linalg.norm() 是什么 linalg=linear+algebra ，也就是线性代数的意思，是numpy 库中进行线性代数运算方面的函数。

使用 np.linalg 这个模块，可以计算范数、逆矩阵、求特征值、解线性方程组以及求解行列式等。

本文要讲的 np.linalg.norm()  ，就是计算范数的意思，norm 则表示 范数。

二、什么是范数 先来了解一下什么是范数，这有利于函数的使用。

首先要知道，范数是一个标量，它是对向量（或者矩阵）的度量

范数包含 0 范数、1范数、2范数........ P范数。

其中：

0 范数，表示向量中非零元素的个数。

1 范数，表示向量中各个元素绝对值之和。

2 范数，表示向量中各个元素平方和 的 1/2 次方，L2 范数又称 Euclidean 范数或者 Frobenius 范数。

p 范数，表示向量中各个元素绝对值 p 次方和 的 1/p 次方。

三、np.linalg.norm() 的用法 1.np.linalg.norm() 的官方文档 有了基础知识，我们来看看np.linalg.norm() 的用法

norm(x, ord=None, axis=None, keepdims=False)

其中：

x，表示要度量的向量

ord，表示范数的种类，默认为2 范数。ord = np.inf 表示无穷范数

axis, axis=0 表示按列向量来进行处理，求多个列向量的范数; axis =1 表示按行向量来进行处理，求多个行向量的范数

keepdims：表示是否保持矩阵的二位特性，True表示保持，False表示不保持，默认为False

注意：对于向量而言，有所不同

ord=None，表示求整体的矩阵元素平方和，再开根号 ord=1，表示求列和的最大值 ord=2，|λE-ATA|=0，求特征值，然后求最大特征值的算术平方根 ord为无穷大，表示求行和的最大值

 四、torch.argmax()函数

import torch

x = torch.randn(2, 4) print(x) ''' tensor([[ 1.2864, -0.5955,  1.5042,  0.5398],         [-1.2048,  0.5106, -2.0288,  1.4782]]) '''

# y0表示矩阵dim=0维度上（每一列）张量最大值的索引 y0 = torch.argmax(x, dim=0) print(y0) ''' tensor([0, 1, 0, 1]) '''

# y1表示矩阵dim=1维度上（每一行）张量最大值的索引 y1 = torch.argmax(x, dim=1) print(y1) ''' tensor([2, 3]) ''' 五、python 内置函数之isinstance 语法：isinstance（object，type）

作用：来判断一个对象是否是一个已知的类型。

其第一个参数（object）为对象，第二个参数（type）为类型名(int…)或类型名的一个列表((int,list,float)是一个列表)。其返回值为布尔型（True or flase）。 函数，计算传入字符串的个数 if isinstance(s,str): #args1: 数据 args2：数据类型 pass 若对象的类型与参数二的类型相同则返回True。若参数二为一个元组，则若对象类型与元组中类型名之一相同即返回True。

## 六、Python——连接数据库操作

#引入decimal模块 import pymysql   #连接数据库 db=pymysql.connect(host='localhost',user='root',password='1234',charset='utf8')   #创建一个游标对象（相当于指针） cursor=db.cursor()   #执行创建数据库语句 cursor.execute('create schema wzg default charset=utf8;') cursor.execute('show databases;')   #fetchone获取一条数据（元组类型） print(cursor.fetchone()) #现在指针到了[1]的位置   #fetchall获取全部数据（字符串类型） all=cursor.fetchall() for i in all:     print(i[0])   #关闭游标和数据库连接 cursor.close() db.close()

## 七、python中list(set(a))方法

## list(set(a))方法之

list(set(a))方法set方法是对元素进行去重，处理之后是一个字典形式，使用list是将其转化为列表

a = ['j','k','f',2,5,3,6,4,7,8,9,6,7,3,2,'j','k']

print((set(a)))

{2, 3, 4, 5, 6, 'f', 'j', 7, 8, 9, 'k'}  字典 print（b=list(set(a))） [2, 3, 4, 5, 6, 7, 'j', 8, 9, 'k', 'f']  列表

 八、python中lower的用法_Python lower()函数

中lower() 函数的作用是把一个字符串中所有大写形式的字符变为小写形式，并生成源字符串的一个副本。

lower() 函数在很多场合起着重要的作用，如有时我们需要判断一个字符串中是否包含另外一个子串，判断文件是否是特定后缀结尾的等，这时我们有必要把源字符串变成小写形式后再判断。毕竟，在实际应用过程中，用户可能使用了大小写不同的形式来表现字符串，将字符串统一变为小写形式能更加准确的进行判别。
