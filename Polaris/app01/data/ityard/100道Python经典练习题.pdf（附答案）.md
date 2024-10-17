
--- 
title:  100道Python经典练习题.pdf（附答案） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/341869615ee9290b0d76056cd3cb51fe.png">

作者：Python芸芸链接：https://www.jianshu.com/p/232d3798af55

Python新手在谋求一份Python编程工作前，必须熟知Python的基础知识。编程网站DataFlair的技术团队分享了一份最常见Python面试题合集，既有基本的Python面试题，也有高阶版试题来指导你准备面试，试题均附有答案。面试题内容包括编码、数据结构、脚本撰写等话题。

##### 

##### **1：Python有哪些特点和优点？**

答：作为一门编程入门语言，Python主要有以下特点和优点：

可解释具有动态特性面向对象简明简单开源具有强大的社区支持

##### **2：深拷贝和浅拷贝之间的区别是什么？**

答：深拷贝就是将一个对象拷贝到另一个对象中，这意味着如果你对一个对象的拷贝做出改变时，不会影响原对象。在Python中，我们使用函数deepcopy()执行深拷贝，导入模块copy，如下所示：

```
&gt;&gt;&gt; import copy
&gt;&gt;&gt; b=copy.deepcopy(a)

```

<img src="https://img-blog.csdnimg.cn/img_convert/88f1c725048a4fa9d943948f9e93b8c5.png">

而浅拷贝则是将一个对象的引用拷贝到另一个对象上，所以如果我们在拷贝中改动，会影响到原对象。我们使用函数function()执行浅拷贝，使用如下所示：

```
&gt;&gt;&gt; b=copy.copy(a)

```

<img src="https://img-blog.csdnimg.cn/img_convert/8c08b775341a5b62bc35a33db8d596eb.png">

##### **3. 列表和元组之间的区别是？**

答：二者的主要区别是列表是可变的，而元组是不可变的。举个例子，如下所示：

```
&gt;&gt;&gt; mylist=[1,3,3]
&gt;&gt;&gt; mylist[1]=2
&gt;&gt;&gt; mytuple=(1,3,3)
&gt;&gt;&gt; mytuple[1]=2
Traceback (most recent call last):
File "&lt;pyshell#97&gt;", line 1, in &lt;module&gt;
mytuple[1]=2

```

会出现以下报错：

```
TypeError: ‘tuple’ object does not support item assignment

```

关于列表和元组的更多内容，可以查看这里：

从Q4到Q20都是针对新手的Python面试基础试题，不过有经验的人也可以看看这些问题，复习一下基础概念。

##### 

##### **4. 解释一下Python中的三元运算子**

不像C++，我们在Python中没有?:，但我们有这个：

```
[on true] if [expression] else [on false]

```

如果表达式为True，就执行[on true]中的语句。否则，就执行[on false]中的语句。下面是使用它的方法：

```
&gt;&gt;&gt; a,b=2,3
&gt;&gt;&gt; min=a if a&lt;b else b
&gt;&gt;&gt; min


运行结果：2
&gt;&gt;&gt; print("Hi") if a&lt;b else print("Bye")


运行结果：Hi

```

##### **5. 在Python中如何实现多线程？**

一个线程就是一个轻量级进程，多线程能让我们一次执行多个线程。我们都知道，Python是多线程语言，其内置有多线程工具包。

Python中的GIL（全局解释器锁）确保一次执行单个线程。一个线程保存GIL并在将其传递给下个线程之前执行一些操作，这会让我们产生并行运行的错觉。但实际上，只是线程在CPU上轮流运行。当然，所有的传递会增加程序执行的内存压力。

##### **6. 解释一下Python中的继承**

当一个类继承自另一个类，它就被称为一个子类/派生类，继承自父类/基类/超类。它会继承/获取所有类成员（属性和方法）。

继承能让我们重新使用代码，也能更容易的创建和维护应用。Python支持如下种类的继承：单继承：一个类继承自单个基类多继承：一个类继承自多个基类多级继承：一个类继承自单个基类，后者则继承自另一个基类分层继承：多个类继承自单个基类混合继承：两种或多种类型继承的混合

##### **7. 什么是Flask？**

Flask是Python编写的一款轻量级Web应用框架。其 WSGI 工具箱采用 Werkzeug ，模板引擎则使用 Jinja2。Flask使用 BSD 授权。其中两个环境依赖是Werkzeug和jinja2，这意味着它不需要依赖外部库。正因如此，我们将其称为轻量级框架。

Flask会话使用签名cookie让用户查看和修改会话内容。它会记录从一个请求到另一个请求的信息。不过，要想修改会话，用户必须有密钥Flask.secret_key。

##### **8. 在Python中是如何管理内存的？**

Python有一个私有堆空间来保存所有的对象和数据结构。作为开发者，我们无法访问它，是解释器在管理它。但是有了核心API后，我们可以访问一些工具。Python内存管理器控制内存分配。

另外，内置垃圾回收器会回收使用所有的未使用内存，所以使其适用于堆空间。

##### **9. 解释Python中的help()和dir()函数**

Help()函数是一个内置函数，用于查看函数或模块用途的详细说明：

```
&gt;&gt;&gt; import copy
&gt;&gt;&gt; help(copy.copy)

```

运行结果为：

```
Help on function copy in module copy:
copy(x)
 Shallow copy operation on arbitrary Python objects.
 See the module’s __doc__ string for more info.

```

Dir()函数也是Python内置函数，dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。

以下实例展示了 dir 的使用方法：

```
&gt;&gt;&gt; dir(copy.copy)

```

运行结果为：

```
[‘__annotations__’, ‘__call__’, ‘__class__’, ‘__closure__’, ‘__code__’, ‘__defaults__’, ‘__delattr__’, ‘__dict__’, ‘__dir__’, ‘__doc__’, ‘__eq__’, ‘__format__’, ‘__ge__’, ‘__get__’, ‘__getattribute__’, ‘__globals__’, ‘__gt__’, ‘__hash__’, ‘__init__’, ‘__init_subclass__’, ‘__kwdefaults__’, ‘__le__’, ‘__lt__’, ‘__module__’, ‘__name__’, ‘__ne__’, ‘__new__’, ‘__qualname__’, ‘__reduce__’, ‘__reduce_ex__’, ‘__repr__’, ‘__setattr__’, ‘__sizeof__’, ‘__str__’, ‘__subclasshook__’]

```

##### 

##### **10. 当退出Python时，是否释放全部内存？**

答案是No。循环引用其它对象或引用自全局命名空间的对象的模块，在Python退出时并非完全释放。

另外，也不会释放C库保留的内存部分。

##### **11. 什么是猴子补丁？**

在运行期间动态修改一个类或模块。

```
&gt;&gt;&gt; class A:
    def func(self):
        print("Hi")
&gt;&gt;&gt; def monkey(self):
print "Hi, monkey"
&gt;&gt;&gt; m.A.func = monkey
&gt;&gt;&gt; a = m.A()
&gt;&gt;&gt; a.func()

```

运行结果为：

`Hi, Monkey`

##### **12. Python中的字典是什么？**

字典是C++和Java等编程语言中所没有的东西，它具有键值对。

```
&gt;&gt;&gt; roots={25:5,16:4,9:3,4:2,1:1}
&gt;&gt;&gt; type(roots)
&lt;class 'dict'&gt;
&gt;&gt;&gt; roots[9]

```

运行结果为：

```
3

```

字典是不可变的，我们也能用一个推导式来创建它。

```
&gt;&gt;&gt; roots={x**2:x for x in range(5,0,-1)}
&gt;&gt;&gt; roots

```

运行结果：

`{25: 5, 16: 4, 9: 3, 4: 2, 1: 1}`

##### **13. 请解释使用args和*kwargs的含义**

当我们不知道向函数传递多少参数时，比如我们向传递一个列表或元组，我们就使用*args。

```
&gt;&gt;&gt; def func(*args):
    for i in args:
        print(i)  
&gt;&gt;&gt; func(3,2,1,4,7)

```

运行结果为：

```
3
 
2
 
1
 
4
 
7

```

在我们不知道该传递多少关键字参数时，使用**kwargs来收集关键字参数。

```
&gt;&gt;&gt; def func(**kwargs):
    for i in kwargs:
        print(i,kwargs[i])
&gt;&gt;&gt; func(a=1,b=2,c=7)

```

运行结果为：

```
a.1
 
b.2
 
c.7

```

##### **14. 请写一个Python逻辑，计算一个文件中的大写字母数量**

```
&gt;&gt;&gt; import os


&gt;&gt;&gt; os.chdir('C:\\Users\\lifei\\Desktop')
&gt;&gt;&gt; with open('Today.txt') as today:
    count=0
    for i in today.read():
        if i.isupper():
            count+=1
print(count)

```

运行结果：

`26`

##### **15. 什么是负索引？**

我们先创建这样一个列表：

```
&gt;&gt;&gt; mylist=[0,1,2,3,4,5,6,7,8]

```

负索引和正索引不同，它是从右边开始检索。

```
&gt;&gt;&gt; mylist[-3]

```

运行结果：

```
6

```

它也能用于列表中的切片：

```
&gt;&gt;&gt; mylist[-6:-1]

```

结果：

`[3, 4, 5, 6, 7]`

##### **16. 如何以就地操作方式打乱一个列表的元素？**

为了达到这个目的，我们从random模块中导入shuffle()函数。

```
&gt;&gt;&gt; from random import shuffle
&gt;&gt;&gt; shuffle(mylist)
&gt;&gt;&gt; mylist

```

```
复制代码


```

运行结果：

`[3, 4, 8, 0, 5, 7, 6, 2, 1]`

##### **17. 解释Python中的join()和split()函数**

Join()能让我们将指定字符添加至字符串中。

```
&gt;&gt;&gt; ','.join('12345')

```

运行结果：

```
‘1,2,3,4,5’

```

Split()能让我们用指定字符分割字符串。

```
&gt;&gt;&gt; '1,2,3,4,5'.split(',')

```

运行结果：

`[‘1’, ‘2’, ‘3’, ‘4’, ‘5’]`

##### **18. Python区分大小写吗？**

如果能区分像myname和Myname这样的标识符，那么它就是区分大小写的。也就是说它很在乎大写和小写。我们可以用Python试一试：

```
&gt;&gt;&gt; myname='Ayushi'
&gt;&gt;&gt; Myname
Traceback (most recent call last):
File "&lt;pyshell#3&gt;", line 1, in &lt;module&gt;

```

运行结果：

```
Myname

NameError: name ‘Myname’ is not defined

```

可以看到，这里出现了NameError，所以**Python是区分大小写**的。

##### **19. Python中的标识符长度能有多长？**

在Python中，标识符可以是任意长度。此外，我们在命名标识符时还必须遵守以下规则：

只能以下划线或者 A-Z/a-z 中的字母开头其余部分可以使用 A-Z/a-z/0-9区分大小写关键字不能作为标识符，Python中共有如下关键字：

<img src="https://img-blog.csdnimg.cn/img_convert/0e5e0914196c77811f5c3af690012c9c.png">

image

##### **20. 怎么移除一个字符串中的前导空格？**

字符串中的前导空格就是出现在字符串中第一个非空格字符前的空格。我们使用方法Istrip()可以将它从字符串中移除。

```
&gt;&gt;&gt; '   Ayushi '.lstrip()

```

结果：

```
‘Ayushi   ’

```

可以看到，该字符串既有前导字符，也有后缀字符，调用Istrip()去除了前导空格。如果我们想去除后缀空格，就用rstrip()方法。

```
&gt;&gt;&gt; '   Ayushi '.rstrip()

```

结果：

```
‘   Ayushi’

```

从Q 21到Q 35是为有Python经验者准备的进阶版Python面试题。

##### **21. 怎样将字符串转换为小写？**

我们使用lower()方法。

```
&gt;&gt;&gt; 'AyuShi'.lower()

```

结果：

```
‘ayushi’

```

使用upper()方法可以将其转换为大写。

```
&gt;&gt;&gt; 'AyuShi'.upper()

```

结果：

```
‘AYUSHI’

```

另外，使用isupper()和islower()方法检查字符春是否全为大写或小写。

```
&gt;&gt;&gt; 'AyuShi'.isupper()
False
 
&gt;&gt;&gt; 'AYUSHI'.isupper()
True
 
&gt;&gt;&gt; 'ayushi'.islower()
True
 
&gt;&gt;&gt; '@yu$hi'.islower()
True
 
&gt;&gt;&gt; '@YU$HI'.isupper()
True

```

那么，像@和$这样的字符既满足大写也满足小写。

Istitle()能告诉我们一个字符串是否为标题格式。

```
&gt;&gt;&gt; 'The Corpse Bride'.istitle()
True

```

##### **22. Python中的pass语句是什么？**

在用Python写代码时，有时可能还没想好函数怎么写，只写了函数声明，但为了保证语法正确，必须输入一些东西，在这种情况下，我们会使用pass语句。

```
 &gt;&gt;&gt; def func(*args):
           pass 
&gt;&gt;&gt;

```

同样，break语句能让我们跳出循环。

```
&gt;&gt;&gt; for i in range(7):
    if i==3: break
print(i)

```

结果：

```
0
 
1
 
2

```

最后，continue语句能让我们跳到下个循环。

```
&gt;&gt;&gt; for i in range(7):
    if i==3: continue
print(i)

```

结果：

```
0
 
1
 
2
 
4
 
5
 
6

```

##### 

##### **23. Python中的闭包是什么？**

当一个嵌套函数在其外部区域引用了一个值时，该嵌套函数就是一个闭包。其意义就是会记录这个值。

```
&gt;&gt;&gt; def A(x):
    def B():
        print(x)
    return B
&gt;&gt;&gt; A(7)()

```

结果：

`7`

##### **24. 解释一下Python中的//，%和 ** 运算符**

//运算符执行地板除法（向下取整除），它会返回整除结果的整数部分。

```
&gt;&gt;&gt; 7//2
3

```

这里整除后会返回3.5。

同样地，执行取幂运算。ab会返回a的b次方。

```
&gt;&gt;&gt; 2**10
1024

```

最后，%执行取模运算，返回除法的余数。

```
&gt;&gt;&gt; 13%7
6
&gt;&gt;&gt; 3.5%1.5
0.5

```

##### **25. 在Python中有多少种运算符？解释一下算数运算符。**

在Python中，我们有7种运算符：算术运算符、关系运算符、赋值运算符、逻辑运算符、位运算符、成员运算符、身份运算符。

我们有7个算术运算符，能让我们对数值进行算术运算：

1.加号（+），将两个值相加

```
&gt;&gt;&gt; 7+8
15

```

2.减号（-），将第一个值减去第二个值

```
&gt;&gt;&gt; 7-8
-1

```

3.乘号（*），将两个值相乘

```
&gt;&gt;&gt; 7*8
56

```

4.除号（/），用第二个值除以第一个值

```
&gt;&gt;&gt; 7/8
0.875
&gt;&gt;&gt; 1/1
1.0

```

5.向下取整除、取模和取幂运算，参见上个问题。

##### **26. 解释一下Python中的关系运算符**

关系运算符用于比较两个值。1.小于号（&lt;），如果左边的值较小，则返回True。

```
&gt;&gt;&gt; 'hi'&lt;'Hi'
False

```

2.大于号（&gt;），如果左边的值较大，则返回True。

```
&gt;&gt;&gt; 1.1+2.2&gt;3.3
True

```

3.小于等于号（&lt;=），如果左边的值小于或等于右边的值，则返回Ture。

```
&gt;&gt;&gt; 3.0&lt;=3
True

```

4.大于等于号（&gt;=），如果左边的值大于或等于右边的值，则返回True。

```
&gt;&gt;&gt; True&gt;=False
True

```

5.等于号（==），如果符号两边的值相等，则返回True。

```
&gt;&gt;&gt; {1,3,2,2}=={1,2,3}
True

```

6.不等于号（!=），如果符号两边的值不相等，则返回True。

```
&gt;&gt;&gt; True!=0.1
True
&gt;&gt;&gt; False!=0.1
True

```

##### **27. 解释一下Python中的赋值运算符**

这在Python面试中是个重要的面试问题。

我们将所有的算术运算符和赋值符号放在一起展示：

```
&gt;&gt;&gt; a=7
&gt;&gt;&gt; a+=1
&gt;&gt;&gt; a
8
 
&gt;&gt;&gt; a-=1
&gt;&gt;&gt; a
7
 
&gt;&gt;&gt; a*=2
&gt;&gt;&gt; a
14
 
&gt;&gt;&gt; a/=2
&gt;&gt;&gt; a
7.0 
 
&gt;&gt;&gt; a**=2
&gt;&gt;&gt; a
49
 
&gt;&gt;&gt; a//=3
&gt;&gt;&gt; a
16.0
 
&gt;&gt;&gt; a%=4
&gt;&gt;&gt; a
0.0

```

##### **28. 解释一下Python中的逻辑运算符**

Python中有3个逻辑运算符：and，or，not。

```
&gt;&gt;&gt; False and True
False
 
&gt;&gt;&gt; 7&lt;7 or True
True
 
&gt;&gt;&gt; not 2==2
False

```

##### **29. 解释一下Python中的成员运算符**

通过成员运算符‘in’和‘not in’，我们可以确认一个值是否是另一个值的成员。

```
&gt;&gt;&gt; 'me' in 'disappointment'
True
 
&gt;&gt;&gt; 'us' not in 'disappointment'
True

```

##### **30. 解释一下Python中的身份运算符**

这也是一个在Python面试中常问的问题。

通过身份运算符‘is’和‘is not’，我们可以确认两个值是否相同。

```
&gt;&gt;&gt; 10 is '10'
False
 
&gt;&gt;&gt; True is not False
True

```

##### **31. 讲讲Python中的位运算符**

该运算符按二进制位对值进行操作。

1.与（&amp;），按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0

```
&gt;&gt;&gt; 0b110 &amp; 0b010
2

```

2.或（|），按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。

```
&gt;&gt;&gt; 3|2
3

```

3.异或（^），按位异或运算符：当两对应的二进位相异时，结果为1

```
&gt;&gt;&gt; 3^2
1

```

4.取反（~），按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1

```
&gt;&gt;&gt; ~2
-3

```

5.左位移（&lt;&lt;），运算数的各二进位全部左移若干位，由 &lt;&lt; 右边的数字指定了移动的位数，高位丢弃，低位补0

```
&gt;&gt;&gt; 1&lt;&lt;2
4

```

6.右位移（&gt;&gt;），把"&gt;&gt;"左边的运算数的各二进位全部右移若干位，&gt;&gt; 右边的数字指定了移动的位数

```
&gt;&gt;&gt; 4&gt;&gt;2
1

```

##### **32. 在Python中如何使用多进制数字？**

我们在Python中，除十进制外还可以使用二进制、八进制和十六进制。

1.二进制数字由0和1组成，我们使用 0b 或 0B 前缀表示二进制数。

```
&gt;&gt;&gt; int(0b1010)
10

```

2.使用bin()函数将一个数字转换为它的二进制形式。

```
&gt;&gt;&gt; bin(0xf)
‘0b1111’

```

3.八进制数由数字 0-7 组成，用前缀 0o 或 0O 表示 8 进制数。

```
&gt;&gt;&gt; oct(8)
‘0o10’

```

4.十六进数由数字 0-15 组成，用前缀 0x 或者 0X 表示 16 进制数。

```
&gt;&gt;&gt; hex(16)
‘0x10’
 
&gt;&gt;&gt; hex(15)
‘0xf’

```

##### **33. 怎样获取字典中所有键的列表？**

使用 keys() 获取字典中的所有键

```
&gt;&gt;&gt; mydict={'a':1,'b':2,'c':3,'e':5}
&gt;&gt;&gt; mydict.keys()
dict_keys(['a', 'b', 'c', 'e'])

```

##### **34. 为何不建议以下划线作为标识符的开头**

因为Python并没有私有变量的概念，所以约定速成以下划线为开头来声明一个变量为私有。所以如果你不想让变量私有，就不要使用下划线开头。

##### **35. 怎样声明多个变量并赋值？**

一共有两种方式：

```
&gt;&gt;&gt; a,b,c=3,4,5 #This assigns 3, 4, and 5 to a, b, and c respectively
&gt;&gt;&gt; a=b=c=3 #This assigns 3 to a, b, and c

```

##### **36. 元组的解封装是什么？**

首先我们来看解封装：

```
&gt;&gt;&gt; mytuple=3,4,5
&gt;&gt;&gt; mytuple
(3, 4, 5)

```

这将 3，4，5 封装到元组 mytuple 中。

现在我们将这些值解封装到变量 x，y，z 中：

```
&gt;&gt;&gt; x,y,z=mytuple
&gt;&gt;&gt; x+y+z

```

得到结果12

**100道练习题**

为了帮助大家学习，已经整理好了100道Python经典练习题PDF，长按识别下方二维码加我个人微信，备注【**100**】免费领取。

<img src="https://img-blog.csdnimg.cn/img_convert/d01534ed0b5531cdef666818bbc5e911.png">

```
长按????二维码+我个人微信

备注100领取

```
