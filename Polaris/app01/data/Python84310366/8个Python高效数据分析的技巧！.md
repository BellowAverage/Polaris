
--- 
title:  8个Python高效数据分析的技巧！ 
tags: []
categories: [] 

---
**一行代码定义List**

定义某种列表时，写For 循环过于麻烦，幸运的是，Python有一种内置的方法可以在一行代码中解决这个问题。下面是使用For循环创建列表和用一行代码创建列表的对比。

```
x = [1,2,3,4]
out = []
for item in x:
  out.append(item**2)
print(out)

[1, 4, 9, 16]

# vs.

x = [1,2,3,4]
out = [item**2 for item in x]
print(out)

[1, 4, 9, 16]

```

**Lambda表达式**

厌倦了定义用不了几次的函数？Lambda表达式是你的救星！Lambda表达式用于在Python中创建小型，一次性和匿名函数对象， 它能替你创建一个函数。

lambda表达式的基本语法是：

```
lambda arguments: expression

```

注意！**只要有一个lambda表达式，就可以完成常规函数可以执行的任何操作。**

你可以从下面的例子中，感受lambda表达式的强大功能：

```
double = lambda x: x * 2
print(double(5))

10

```

**Map和Filter**

一旦掌握了lambda表达式，学习将它们与Map和Filter函数配合使用，可以实现更为强大的功能。具体来说，map通过对列表中**每个元素执行某种操作并将其转换为新列表。**

在本例中，它遍历每个元素并乘以2，构成新列表。 （注意！list()函数只是将输出转换为列表类型）

```
# Map
seq = [1, 2, 3, 4, 5]
result = list(map(lambda var: var*2, seq))
print(result)

[2, 4, 6, 8, 10]

```

Filter函数接受一个列表和一条规则，就像map一样，但它通过比较每个元素和布尔过滤规则来返回原始列表的一个子集。

```
# Filter
seq = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x &gt; 2, seq))
print(result)


[3, 4, 5]

```

**Arange和Linspace**

Arange返回给定步长的等差列表。它的三个参数start、stop、step分别表示起始值，结束值和步长， 请注意！stop点是一个“截止”值，因此它不会包含在数组输出中。

```
# np.arange(start, stop, step)
np.arange(3, 7, 2)


array([3, 5])

```

Linspace和Arrange非常相似，但略有不同。Linspace以指定数目均匀分割区间，所以给定区间start和end，以及等分分割点数目num，linspace将返回一个NumPy数组。

这对绘图时数据可视化和声明坐标轴特别有用。

```
# np.linspace(start, stop, num)
np.linspace(2.0, 3.0, num=5)

array([ 2.0,  2.25,  2.5,  2.75, 3.0]

```

**Axis代表什么？**

在Pandas中，删除一列或在NumPy矩阵中求和值时，可能会遇到Axis。我们用删除一列（行）的例子：

```
df.drop('Column A', axis=1)

df.drop('Row A', axis=0)

```

如果你想处理列，将Axis设置为1，如果你想要处理行，将其设置为0。但为什么呢？ 回想一下Pandas中的shape。

```
df.shape
(# of Rows, # of Columns)

```

从Pandas DataFrame中调用shape属性返回一个元组，第一个值代表行数，第二个值代表列数。

如果你想在Python中对其进行索引，则行数下标为0，列数下标为1，这很像我们如何声明轴值。

**Concat，Merge和Join**

如果您熟悉SQL，那么这些概念对你来说可能会更容易。 无论如何，这些函数本质上就是以特定方式组合DataFrame的方式。 在哪个时间跟踪哪一个最适合使用可能很困难，所以让我们回顾一下。

Concat允许用户在表格下面或旁边追加一个或多个DataFrame（取决于您如何定义轴）。

<img src="https://img-blog.csdnimg.cn/img_convert/6aeac1006d5d192e56c7a91f85be5755.jpeg" alt="">

Merge将多个DataFrame合并指定主键（Key）相同的行。

<img src="https://img-blog.csdnimg.cn/img_convert/09b803fb9cca06f226663df5392aceeb.png" alt="">

Join，和Merge一样，合并了两个DataFrame。但它不按某个指定的主键合并，而是根据相同的列名或行名合并。

<img src="https://img-blog.csdnimg.cn/img_convert/369c0aded5269476ad6f6ab3176668f2.png" alt="">

**Pandas Apply**

##### 

##### Apply是为Pandas Series而设计的。如果你不太熟悉Series，可以将它想成类似Numpy的数组。

Apply将一个函数应用于指定轴上的每一个元素。使用Apply，可以将DataFrame列（是一个Series）的值进行格式设置和操作，不用循环，非常有用！

```
df = pd.DataFrame([[4, 9],] * 3, columns=['A', 'B'])
 df
   A  B
0  4  9
1  4  9
2  4  9

df.apply(np.sqrt)
     A    B
0  2.0  3.0
1  2.0  3.0
2  2.0  3.0

df.apply(np.sum, axis=0)
A    12
B    27

df.apply(np.sum, axis=1)
0    13
1    13
2    13

```

**Pivot Tables**

如果您熟悉Microsoft Excel，那么你也许听说过数据透视表。

Pandas内置的pivot_table函数以DataFrame的形式创建电子表格样式的数据透视表,，它可以帮助我们快速查看某几列的数据。

下面是几个例子：

非常智能地将数据按照“Manager”分了组：

```
pd.pivot_table(df, index=["Manager", "Rep"])

```

<img src="https://img-blog.csdnimg.cn/img_convert/4d5dbb91b3aafb7cee7990d386c3847d.png" alt="">

或者也可以筛选属性值

```
pd.pivot_table(df,index=
["Manager","Rep"],values=["Price"])

```

<img src="https://img-blog.csdnimg.cn/img_convert/6b42cc8ee47f491fff8be35a4d739046.png" alt="">

希望上面的这些描述能够让你发现Python一些好用的函数和概念。

## 关于Python学习指南

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后给大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、自动化办公等学习教程。带你从零基础系统性的学好Python！</mark>

#### 👉Python所有方向的学习路线👈

Python所有方向路线就是把Python常用的技术点做整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取）**</mark>

<img src="https://img-blog.csdnimg.cn/3c4ee87941694f3789398db3d52a2637.png#pic_center" alt="在这里插入图片描述">

#### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。

<img src="https://img-blog.csdnimg.cn/64c89bf6293d4699bf7ee8f34b9e69fd.png#pic_center" alt="在这里插入图片描述">

#### <mark>温馨提示：篇幅有限，已打包文件夹，获取方式在：文末</mark>

#### 👉Python70个实战练手案例&amp;源码👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/2017b67544f94e8898db755e2703224a.png#pic_center" alt="在这里插入图片描述">

#### 👉Python大厂面试资料👈

我们学习Python必然是为了找到高薪的工作，下面这些面试题是来自**阿里、腾讯、字节等一线互联网大厂**最新的面试资料，并且有阿里大佬给出了权威的解答，刷完这一套面试资料相信大家都能找到满意的工作。

<img src="https://img-blog.csdnimg.cn/3055c54d3224495987c589f150324d73.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/b0751719fe914aec8c8d09f62f772e44.png#pic_center" alt="在这里插入图片描述">

#### 👉Python副业兼职路线&amp;方法👈

学好 Python 不论是就业还是做副业赚钱都不错，但要学会兼职接单还是要有一个学习规划。

<img src="https://img-blog.csdnimg.cn/01bcd7cbfd6d43fb85ef410766735154.png#pic_center" alt="在这里插入图片描述">

**👉** **这份完整版的Python全套学习资料已经上传，朋友们如果需要可以扫描下方CSDN官方认证二维码或者点击链接免费领取**【**`保证100%免费`**】

<font color="red">**点击免费领取《CSDN大礼包》： 安全链接免费领取**</font>
