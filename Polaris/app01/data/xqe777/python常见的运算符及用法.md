
--- 
title:  python常见的运算符及用法 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主🏆 📃个人主页： 🔥系列专栏： 💬个人格言：但行好事，莫问前程 


<img src="https://img-blog.csdnimg.cn/d4a86179638f4642a803d806d976bd02.jpeg#pic_center" alt="在这里插入图片描述">

💖python中的运算符主要包括算术运算符，关系(比较)运算符，赋值运算符，逻辑运算符，成员运算符，身份运算符，三目运算符。使用运算符将不同类型的数据按照一定的规则连接起来的式子，称为表达式。下面将介绍一些常用的运算符💖



#### 💖python运算符💖
- - - - - - - - - 


## 算术运算符

|运算符|描述
|------
|+|两个数相加两个数相加，或是字符串连接
|-|两个数相减
|*|两个数相乘，或是返回一个重复若干次的字符串
|/|两个数相除，结果为浮点数
|%|取模，返回两个数相除的余数
|//|两个数相除，返回商的整数部分
|**|幂运算，返回乘方结果

```
print(1 + 2)  # 3
print(2 - 1)  # 1
print(2 * 3)  # 6
print(3 / 2)  # 1.5
print(6 % 5)  # 1
print(8 // 2)  # 4
print(3 ** 2)  # 9

```

如果想同时得到商和余数，可以用<mark>divmod</mark>这个方法 该方法的返回值是tuple (x//y, x%y).

```
print(divmod(10,3)) # (3,1)

```

因为浮点数精度的问题，Python还存在一些计算方面的小问题

```
print(0.1+0.1+0.1-0.3)  # 5.551115123125783e-17

```

要解决这个问题，可以导入<mark>decimal</mark>模块

```
from decimal import Decimal
# 计算结果:0.0
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))

```

## 关系运算符

|运算符|描述
|------
|==|比较对象是否相等
|!=|比较对象是否不相等
|&gt;|大于，例如a&gt;b,将比较a与b的大小，a&gt;b返回True,否则返回False
|&lt;|小于，例如a&lt;b,将比较a与b的大小，a&lt;b返回True,否则返回False
|&gt;=|大于等于，例如a&gt;=b,将比较a与b的大小，a&gt;=b返回True,否则返回False
|&lt;=|小于等于，例如a&lt;=b,将比较a与b的大小，a&lt;=b返回True,否则返回False

```
a = 10
b = 20
print(a == b)  # False
print(a != b)  # True
print(a &gt; b)  # False 
print(a &lt; b)  # True
print(a &gt;= b)  # False
print(a &lt;= b)  # True

```

1.返回值为bool值

```
print(True == 1)  # True
print(False == 0)  # True

```

==比较数值（int与str不能直接比较）

```
print(2.0 == 2)  # True
print('2' == 2)  # False

```

字符串与字符串之间是比较<mark>ASCII</mark>值

```
# True
print('abc' &lt; 'xyz') # 97 98 99 &lt; 120 121 122

```

连续比较，python的解释机制

```
print(3 &gt; 2 &gt; 1)  # True
print(3 &gt; 2 &gt; 2)  # False
print((3 &gt; 2) &gt; 1) # False

```

## 赋值运算符

|运算符|描述
|------
|=|常规赋值运算符，将运算结果赋值给变量
|+=|加法赋值运算符，例如 a+=b 等效于 a=a+b
|-=|减法赋值运算符，例如 a-=b 等效于 a=a-b
|*=|乘法法赋值运算符，例如 a*=b 等效于 a=a*b
|/=|除法赋值运算符，例如 a/=b 等效于 a=a/b
|//=|取整除赋值运算符，例如 a//=b 等效于 a=a//b
|%=|取模赋值运算符，例如 a%=b 等效于 a=a%b
|**=|幂运算赋值运算符，例如 a**=b 等效于 a=a*b

```
a = 1   	# 将等号右边 赋值 等号左边
a = a + 1   # 先等号右边计算 再赋值给 等号左边
a += 1		# a = a + 1

```

## 逻辑运算符

|运算符|描述
|------
|and|与运算，如果a 为False,a and b返回False 否则返回y的计算值
|or|或运算，如果a非0,返回a的值，否则返回b的值
|not|非运算，如果a为True,返回False,如果a为False,返回True

```
a = 10
b = 20
print(a and b)  # 20
print(a or b)  # 10
print(not a)  # False

```

a and b 两者都为True时结果才为True a or b 两者有一个为True则结果就为True

<mark>短路(懒惰)原则</mark> False and True 当and运算符时,遇到第一个为False则不会往后了 True or False 当or运算符时,遇到第一个为True则不会往后了

## 成员运算符

|运算符|描述
|------
|in|如果在指定的序列中找到值返回True，否则返回False
|not in|如果在指定的序列中找到值返回True,否则返回False

```
list1 = [1, 2, 3, 4, 5]
a = 1
if a in list1:
    print("a是list1的元素之一")
else:
    print("a不是list1的元素")

```

## 身份运算符

|运算符|描述
|------
|is|判断两个标识符是不是引用自一个对象
|is not判断两个标识符是不是引用自不同对象|

<mark>is 和比较运算符 == 的区别</mark> is 用于判断两个变量是否引自同一个对象（可使用id()查看），而 ==用于判断变量的值是否相等！

```
a = [1, 2, 3]
b = [1, 2, 3]
# 可通过id()查看内存地址
print(id(a))  # 2042443551304
print(id(b))  # 2042443551816
print(a is b)  # False
print(a == b)  # True

```

```
a = 2
b = 2.0
# 可通过id()查看内存地址
print(id(a))  # 140722443350320
print(id(b))  # 2336678499216
print(a is b)  # False
print(a == b)  # True

```

## 三目运算符

三目运算符的表示方法：<mark>True_statements if expression else False_statements</mark>

```
a = 1
b = 2
# a+b不大于3执行后面的else语句 b-a = 1
print(a+b if a+b&gt;3 else b-a)

```

## 运算符优先级

|运算符|描述
|------
|**|指数（最高优先级）
|*/%//|乘，除，取模和取整除
|±|加法减法
|&lt;= &gt;=|比较运算符
|== !=|等于运算符
|= %= 、= 、、=-= += *= **=|赋值运算符
|is is not|身份运算符
|in not in|成员运算符
|not or and|逻辑运算符

## 结束语

>  
 以上就是python常见的运算符及用法 你们的支持就是hacker创作的动力💖💖💖 


<img src="https://img-blog.csdnimg.cn/5b80ea7dab574ae5bb3fda934fe3f872.gif#pic_center" alt="在这里插入图片描述">
