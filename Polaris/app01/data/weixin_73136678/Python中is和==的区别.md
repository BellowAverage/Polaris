
--- 
title:  Python中is和==的区别 
tags: []
categories: [] 

---
在Python中一切都是对象。

Python中对象包含的三个基本要素，分别是：id(身份标识)、type(数据类型)和value(值)。对象之间比较是否相等可以用==，也可以用is。

is和==都是对对象进行比较判断作用的，但对对象比较判断的内容并不相同。下面来看看具体区别在哪?

**is比较的是两个对象的id值是否相等，也就是比较两个对象是否为同一个实例对象，是否指向同一个内存地址。**

**==比较的是两个对象的内容是否相等，默认会调用对象的__eq__()方法。**



以下代码在Python3.5下测试通过。

#### ==比较操作符和is同一性运算符区别

==是python标准操作符中的比较操作符，用来比较判断两个对象的value(值)是否相等。

代码1：

```
&gt;&gt;&gt; a = [1, 2, 3]
&gt;&gt;&gt; b = a
&gt;&gt;&gt; b is a 
True
&gt;&gt;&gt; b == a
True
&gt;&gt;&gt; b = a[:]
&gt;&gt;&gt; b is a
False
&gt;&gt;&gt; b == a
True复制代码
```



解释一下为什么？is也被叫做同一性运算符，也就是id是否相同。看下面代码， a和b变量的id不同， 所以b==a是True， b is a 是False.

代码2：

```
&gt;&gt;&gt; id(a)
4364243328
&gt;&gt;&gt; 
&gt;&gt;&gt; id(b)
4364202696复制代码
```

#### 哪些情况下is和==结果是完全相同的？

代码3：

```
&gt;&gt;&gt; a = 256
&gt;&gt;&gt; b = 256
&gt;&gt;&gt; a is b
True
&gt;&gt;&gt; a == b
True
&gt;&gt;&gt;
&gt;&gt;&gt; a = 1000
&gt;&gt;&gt; b = 10**3
&gt;&gt;&gt; a == b
True
&gt;&gt;&gt; a is b
False
&gt;&gt;&gt;复制代码
```

结论：数字类型不完全相同。 



为什么256时相同， 而1000时不同？

因为出于对性能的考虑，Python内部做了很多的优化工作，对于整数对象，Python把一些频繁使用的整数对象缓存起来，保存到一个叫small_ints的链表中，在Python的整个生命周期内，任何需要引用这些整数对象的地方，都不再重新创建新的对象，而是直接引用缓存中的对象。Python把这些可能频繁使用的整数对象规定在范围[-5, 256]之间的小对象放在small_ints中，但凡是需要用些小整数时，就从这里面取，不再去临时创建新的对象。



代码4：

```
&gt;&gt;&gt; c = 'pythontab.com'
&gt;&gt;&gt; d = 'pythontab.com'
&gt;&gt;&gt; c is d
False
&gt;&gt;&gt; c == d
True
&gt;&gt;&gt; c = 'pythontabcom'
&gt;&gt;&gt; d = 'pythontabcom'
&gt;&gt;&gt; c is c
True
&gt;&gt;&gt; c == d
True复制代码
```



结论：字符串类型不完全相同。这个和解释器实现有关。



代码5：

```
&gt;&gt;&gt; a = (1,2,3) #a和b为元组类型
&gt;&gt;&gt; b = (1,2,3)
&gt;&gt;&gt; a is b
False
&gt;&gt;&gt; a = [1,2,3] #a和b为list类型
&gt;&gt;&gt; b = [1,2,3]
&gt;&gt;&gt; a is b
False
&gt;&gt;&gt; a = {'python':100,'com':1} #a和b为dict类型
&gt;&gt;&gt; b = {'python':100,'com':1}
&gt;&gt;&gt; a is b
False
&gt;&gt;&gt; a = set([1,2,3])#a和b为set类型
&gt;&gt;&gt; b = set([1,2,3])
&gt;&gt;&gt; a is b
False复制代码
```



#### 结论

当变量是数字、字符串、元组，列表，字典时，is和==都不相同， 不能互换使用！当比较值时，要使用==，比较是否是同一个内存地址时应该使用is。当然，开发中比较值的情况比较多。



作者：一个普普通通简简单单 链接：https://juejin.cn/post/6844903538737299464 来源：稀土掘金 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注处。

在Python中一切都是对象。

Python中对象包含的三个基本要素，分别是：id(身份标识)、type(数据类型)和value(值)。对象之间比较是否相等可以用==，也可以用is。

is和==都是对对象进行比较判断作用的，但对对象比较判断的内容并不相同。下面来看看具体区别在哪?

**is比较的是两个对象的id值是否相等，也就是比较两个对象是否为同一个实例对象，是否指向同一个内存地址。**

**==比较的是两个对象的内容是否相等，默认会调用对象的__eq__()方法。**



以下代码在Python3.5下测试通过。

#### ==比较操作符和is同一性运算符区别

==是python标准操作符中的比较操作符，用来比较判断两个对象的value(值)是否相等。

代码1：

```
&gt;&gt;&gt; a = [1, 2, 3]
&gt;&gt;&gt; b = a
&gt;&gt;&gt; b is a 
True
&gt;&gt;&gt; b == a
True
&gt;&gt;&gt; b = a[:]
&gt;&gt;&gt; b is a
False
&gt;&gt;&gt; b == a
True复制代码
```



解释一下为什么？is也被叫做同一性运算符，也就是id是否相同。看下面代码， a和b变量的id不同， 所以b==a是True， b is a 是False.

代码2：

```
&gt;&gt;&gt; id(a)
4364243328
&gt;&gt;&gt; 
&gt;&gt;&gt; id(b)
4364202696复制代码
```

#### 哪些情况下is和==结果是完全相同的？

代码3：

```
&gt;&gt;&gt; a = 256
&gt;&gt;&gt; b = 256
&gt;&gt;&gt; a is b
True
&gt;&gt;&gt; a == b
True
&gt;&gt;&gt;
&gt;&gt;&gt; a = 1000
&gt;&gt;&gt; b = 10**3
&gt;&gt;&gt; a == b
True
&gt;&gt;&gt; a is b
False
&gt;&gt;&gt;复制代码
```

结论：数字类型不完全相同。 



为什么256时相同， 而1000时不同？

因为出于对性能的考虑，Python内部做了很多的优化工作，对于整数对象，Python把一些频繁使用的整数对象缓存起来，保存到一个叫small_ints的链表中，在Python的整个生命周期内，任何需要引用这些整数对象的地方，都不再重新创建新的对象，而是直接引用缓存中的对象。Python把这些可能频繁使用的整数对象规定在范围[-5, 256]之间的小对象放在small_ints中，但凡是需要用些小整数时，就从这里面取，不再去临时创建新的对象。



代码4：

```
&gt;&gt;&gt; c = 'pythontab.com'
&gt;&gt;&gt; d = 'pythontab.com'
&gt;&gt;&gt; c is d
False
&gt;&gt;&gt; c == d
True
&gt;&gt;&gt; c = 'pythontabcom'
&gt;&gt;&gt; d = 'pythontabcom'
&gt;&gt;&gt; c is c
True
&gt;&gt;&gt; c == d
True复制代码
```



结论：字符串类型不完全相同。这个和解释器实现有关。



代码5：

```
&gt;&gt;&gt; a = (1,2,3) #a和b为元组类型
&gt;&gt;&gt; b = (1,2,3)
&gt;&gt;&gt; a is b
False
&gt;&gt;&gt; a = [1,2,3] #a和b为list类型
&gt;&gt;&gt; b = [1,2,3]
&gt;&gt;&gt; a is b
False
&gt;&gt;&gt; a = {'python':100,'com':1} #a和b为dict类型
&gt;&gt;&gt; b = {'python':100,'com':1}
&gt;&gt;&gt; a is b
False
&gt;&gt;&gt; a = set([1,2,3])#a和b为set类型
&gt;&gt;&gt; b = set([1,2,3])
&gt;&gt;&gt; a is b
False复制代码
```



#### 结论

当变量是数字、字符串、元组，列表，字典时，is和==都不相同， 不能互换使用！当比较值时，要使用==，比较是否是同一个内存地址时应该使用is。当然，开发中比较值的情况比较多。
