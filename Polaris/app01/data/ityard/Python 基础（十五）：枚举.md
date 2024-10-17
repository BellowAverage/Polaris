
--- 
title:  Python 基础（十五）：枚举 
tags: []
categories: [] 

---


#### 目录
- - - <ul><li><ul><li>- - - 


## 1 简介

起初 Python 中并未内置枚举（enum）类型，枚举是在 Python3.4 添加的新功能，此时我们可能会有一个疑问：Python3.4 之前的版本还能不能使用枚举呢？ <img src="https://img-blog.csdnimg.cn/202001041024369.gif" alt=""> 答案是可以使用，但是不能直接使用，使用之前需要先用 `pip install enum` 安装。

**什么是枚举？**

枚举可看作是一系列符号名称的集合，集合中每一个元素要保证唯一性和不可变，因此我们可以对枚举中元素进行恒等比较，通俗来讲枚举就是一系列常量的集合，枚举是可迭代的。

**枚举有什么作用？**

我们先来思考一个问题：不使用枚举我们如何定义常量呢？ <img src="https://img-blog.csdnimg.cn/20200104100014882.gif" alt="在这里插入图片描述"> 常用的做法是采用变量名大写的方式来定义，这种方式虽然简单，但问题在于我们定义的仍然是变量、是可以被修改的，而常量是什么呢？简单来说就是不可变的量，枚举就有不可变的特性，所以枚举的主要作用就是用来定义常量的。

## 2 使用

#### 2.1 创建

枚举语法与 class 语法相同，之前我们在中已经介绍过 class 了，枚举的定义可以通过继承 Enum 的方式来实现， 看一下示例：

```
from enum import Enum

class WeekDay(Enum):
    Mon = 0
    Tue = 1
    Wed = 2
    Thu = 3
    Fri = 4

```

#### 2.2 访问

枚举成员及属性的访问如下所示：

```
# 枚举成员
print(WeekDay.Mon)
# 枚举成员名称
print(WeekDay.Mon.name)
# 枚举成员值
print(WeekDay.Mon.value)  

```

枚举的迭代也很简单，如下所示：

```
# 方式 1
for day in WeekDay:
    # 枚举成员
    print(day)
    # 枚举成员名称
    print(day.name)
    # 枚举成员值
    print(day.value)

# 方式 2
print(list(WeekDay)) 

```

#### 2.3 比较

枚举成员及属性可以使用 is 进行对象比较，还可以使用 == 进行值比较，看下示例：

```
print(WeekDay.Mon is WeekDay.Thu)
print(WeekDay.Mon == WeekDay.Mon)
print(WeekDay.Mon.name == WeekDay.Mon.name)
print(WeekDay.Mon.value == WeekDay.Mon.value)

```

枚举成员不能进行大小比较，如下所示：

```
&gt;&gt;&gt; WeekDay.Mon &lt; WeekDay.Thu
TypeError: '&lt;' not supported between instances of 'WeekDay' and 'WeekDay'

```

#### 2.4 确保枚举值唯一

我们定义枚举时，成员名称是不可以重复的，但成员值是可以重复的，如果想要保证成员值不可重复，可以通过装饰器 `@unique` 来实现，如下所示：

```
 from enum import Enum, unique

@unique
class WeekDay(Enum):
	Mon = 0
    ...

```

参考： 

<img src="https://img-blog.csdnimg.cn/20191212073821865.png#pic_center" alt="" width="600">
