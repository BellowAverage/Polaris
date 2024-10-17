
--- 
title:  python入门学习——6种方法求n的阶乘（8种写法） 
tags: []
categories: [] 

---
##### 一、阶乘（factorial）

**自然数n！（n的阶乘）是指从1、2……（n-1）、n这n个数的连乘积，即 n！=n×（n-1）×……2×1**

如： 1！ = 1 =1 2！= 2 * 1 = 2 3！= 3 * 2 * 1 = 6 4! = 4 * 3 * 2 * 1 = 24 5！= 5 * 4 * 3 * 2 * 1 = 120 …

>  
 了解了阶乘的基本概念之后，构思时间…，之后我们一起来编程实现一下（递归方法会着重讲解）： 


##### 二、编程求解

###### 1、普通的for循环语句来计算阶乘

```
 #函数实现
 def factorial(num):
    a=1
    #for循环遍历
    for i in range(1,num+1):
         a*=i
    return a

 n = int(input())
 print(factorial(n))

```

<img src="https://img-blog.csdnimg.cn/de9687deecc241cf95fa06ad419eed93.png" alt="在这里插入图片描述">

###### 2、while循环语句来计算阶乘

```
#输入n的值
n=int(input())            
ans=n
i=1
if n ==0:
    print(1)
else:
	#while循环
    while i &lt;n:                                              
        ans=ans*i                                            
        i=i+1                                               
    print(ans)        
 

```

<img src="https://img-blog.csdnimg.cn/74f5bfc0ef2a4c25bd202b29f2c79b4d.png" alt="在这里插入图片描述">

###### 3、使用递归函数

我们小时候或多或少应该听说这个故事：“从前有座山，山里有座庙，庙里有个老和尚和小和尚，老和尚给小和尚讲故事：从前有座山，山里有座庙……”，长大之后，仔细想想，怎么兜兜转转，这不是在"套娃"儿吗？ <img src="https://img-blog.csdnimg.cn/98e5541fff994a63bb73930d5d46c565.gif#pic_center" alt="在这里插入图片描述"> 仔细想想，这些好像跟`递归`有点儿像啊，**“自己调用自己”**。 简单了解了递归之后，我们可以去用递归写一下试试，写法如下：

`1️⃣写法一`

```
#函数实现
def factorial(n):
    if n==0:
        return 1
    else:
        #递归调用
        return factorial(n-1)*n
    
n = int(input())
print(factorial(n))

```

<img src="https://img-blog.csdnimg.cn/7a7a082aff4647e28cdb64f80ceb5d9f.png" alt="在这里插入图片描述">

`2️⃣写法二 `

```
#函数实现
def factorial(n):
      #三元运算表达式
      return 1 if n &lt; 2 else n * factorial(n - 1)
 
#输入n的值
n = int(input())
print(factorial(n))

```

【注：三元运算表达式，语法：为真时的结果 if 判定条件 else 为假时的结果】

<img src="https://img-blog.csdnimg.cn/3e843a0bb189402ea770b997504819bf.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/a5bc9345c6d040808f1bbf72bf9f74d0.png" alt="在这里插入图片描述"> 震惊我汪一整年，还能这样写？请看下图： **以用递归的方法求5的阶乘为例：**

<img src="https://img-blog.csdnimg.cn/d1913e26a42d4e1bb053a31894b24969.png" alt="在这里插入图片描述"> 看完这张图有没有感觉对递归认识清晰了一些？当然如仍有困惑，可评论回复，博主看到后会尽快做出答复。

###### 4、借助functools中的reduce模块

`1️⃣写法一`

```
#导入functools
import functools
#输入n的值
n = int(input())
#lambda函数+reduce模块
result = (lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(n)
print(result)

```

【 注：Lambda是一种不需要名字（即标识符）、由一个单独表达式成的匿名内联函数，表达式会在调用时被求值。 创建 lambda 函数的语法为：lambda [parameters]: expression 】

<img src="https://img-blog.csdnimg.cn/bd1a1910a68c4fcdb5bc723b2ecf3fa2.png" alt="在这里插入图片描述">

`2️⃣写法二`

```
#从functools中导入reduce
from functools import reduce
#函数实现
def factorial(num):
    return reduce(lambda x,y:x*y,range(1,num+1))

#输入n的值
n = int(input())
print(factorial(n))

```

<img src="https://img-blog.csdnimg.cn/e6718e776ef64d379034b307ae3804f7.png" alt="在这里插入图片描述">

###### 5、借助math库，使用math库的factorial方法

```
#导入math模块
import math
#函数实现
def fact(num):
	#借助math模块中的factorial方法
    return math.factorial(num)

#输入n的值
n = int(input())
print(fact(n))

```

【注：Python math.factorial(x) 方法返回 x 的阶乘。】

<img src="https://img-blog.csdnimg.cn/14b9aaa40e1d478480022c66bc040778.png" alt="在这里插入图片描述">

###### 6、使用eval适配表达式

```
#函数实现
def fact(num):
	#eval适配表达式实现
	return eval('*'.join(map(str,range(1,num+1))))

#输入n的值
n = int(input())
print(fact(n))

```

【注：eval() 函数用来执行一个字符串表达式，并返回表达式的值。 eval() 方法的语法:eval(expression[, globals[, locals]]) 】

<img src="https://img-blog.csdnimg.cn/491c05ef4d3d468abd8ddf0d6db538ef.png" alt="在这里插入图片描述">

>  
 ****（一个喜欢古诗词和编程的Coder😊） **如果对大家有帮助的话，希望大家能多多点赞+关注！这样我动力会更足哦！ ღ( ´･ᴗ･` )比心** 

