
--- 
title:  Python编程技巧 – 迭代器(Iterator) 
tags: []
categories: [] 

---
## Python编程技巧 – 迭代器(Iterator)

By Jackson@ML

>  
 Iterator(迭代器)是Python语言的核心概念之一。它常常与装饰器和生成器一道被人们提及，也是所有Python书籍需要涉及的部分。 


本文简要介绍迭代器的功能以及实际的案例，希望对广大读者和学生有所帮助。

#### 1. 迭代器概念

迭代器有时会被误以为可迭代对象。其实，迭代器是一个对象(Object)， 它可以逐个地生成一系列的值。

下面先看一个列表（List）的遍历示例。

```
lst = ['China','Russia','Vietnam','Korea','Germany','France','Brasil']

for i in lst:
    print(i)

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/fc100ad4bd6449478d2bdebbe4422d26.png" alt="在这里插入图片描述"> 显而易见，**列表是可以迭代的**。但并非所有迭代器都仅仅是列表。

现实中，有许多函数（例如：reversed）会产生出非列表的迭代器。

迭代器是一种无法以现有方式直接进行索引或输出的对象。

看以下迭代器代码示例：

```
iter1 = reversed([1, 2, 3, 4])
print(iter1)

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/6e68dc60317a439c848fe689509dcc89.png" alt="在这里插入图片描述"> 打印输出的是该对象（反向迭代器）的地址，并非列表的值。

上述代码可以将迭代器转换为列表，然后再次输出，或者做其它操作。添加下面代码到程序：

```
print(list(iter1))

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/b5cf6f0b46204c51b2843d3d59654680.png" alt="在这里插入图片描述">

#### 2. 遍历迭代器

Python中的迭代器常与for循环语句一起使用。例如，iter1是一个迭代器，以下代码运行良好：

```
iter1 = reversed([1, 2, 3, 4])
for i in iter1:
    print(i, end=' ')
    

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/b9530dda66eb4a2787eeacc6bcf4ff12.png" alt="在这里插入图片描述">

迭代器自身具有状态信息监控机制。当迭代到达序列末尾时，该迭代器将耗尽。

此时，如果再次使用iter1而不重置，它将不再产生任何其它值。

#### 3. 迭代器模式

迭代器除了作为对象，处理数据之外，还形成了面向对象编程的一个流行模式，即**迭代器模式**。

用设计模式广泛流行的述语来讲，迭代器就是一个拥有next()和done()方法的对象，后者在序列中没有其它元素时，返回True.

在没有内置支持迭代器的编程语言中，也许迭代器的遍历过程看起来像下面这样：

```
while not iterator.done():
	item = iterator.next()
# other operations to item

```

在Python编程语言中，迭代是一个特殊的特征，因此，这个方法有个特殊名称：**next**, 这一方法可以通过内置的next(iterator)函数访问。

当遍历结束时，迭代器协议会抛出异常StopIterator,而不是通过done方法。

技术不断演进，博客也会不断创新跟进，敬请关注。

喜欢就点赞哈，您的认可，我的动力！😊

#### 相关阅读：
1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 