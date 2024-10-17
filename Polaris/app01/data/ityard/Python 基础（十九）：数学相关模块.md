
--- 
title:  Python 基础（十九）：数学相关模块 
tags: []
categories: [] 

---


#### 目录
- - - - 


## 1. 简介

我们来看一下 Python 中数学相关模块，如下所示：

<th align="center">模块</th><th align="left">描述</th>
|------
<td align="center">math</td><td align="left">提供了对 C 标准定义的数学函数的访问（不适用于复数）</td>
<td align="center">cmath</td><td align="left">提供了一些关于复数的数学函数</td>
<td align="center">decimal</td><td align="left">为快速正确舍入的十进制浮点运算提供支持</td>
<td align="center">fractions</td><td align="left">为分数运算提供支持</td>
<td align="center">random</td><td align="left">实现各种分布的伪随机数生成器</td>
<td align="center">statistics</td><td align="left">提供了用于计算数字数据的数理统计量的函数</td>

本文具体介绍一下相对比较常用的模块：math、decimal 和 random。

## 2. math 模块

先来看一下 math 模块中包含内容，如下所示：

```
&gt;&gt;&gt; import math
&gt;&gt;&gt; dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

```

接下来具体看一下该模块的常用函数和常量。

**ceil(x)** 返回 x 的上限，即大于或者等于 x 的最小整数。看下示例：

```
import math

x = -1.5
print(math.ceil(x))

```

**floor(x)** 返回 x 的向下取整，小于或等于 x 的最大整数。看下示例：

```
import math

x = -1.5
print(math.floor(x))

```

**fabs(x)** 返回 x 的绝对值。看下示例：

```
import math

x = -1.5
print(math.fabs(x))

```

**fmod(x, y)** 返回 x/y 的余数，值为浮点数。看下示例：

```
import math

x = 3
y = 2
print(math.fmod(x, y))

```

**factorial(x)** 返回 x 的阶乘，如果 x 不是整数或为负数时则将引发 ValueError。看下示例：

```
import math

x = 3
print(math.factorial(3))

```

**pow(x, y)** 返回 x 的 y 次幂。看下示例：

```
import math

x = 3
y = 2
print(math.pow(x, y))

```

**fsum(iterable)** 返回迭代器中所有元素的和。看下示例：

```
import math

print(math.fsum((1, 2, 3, 4, 5)))

```

**gcd(x, y)** 返回整数 x 和 y 的最大公约数。看下示例：

```
import math

x = 9
y = 6
print(math.gcd(x, y))

```

**sqrt(x)** 返回 x 的平方根。看下示例：

```
import math

x = 9
print(math.sqrt(x))

```

**trunc(x)** 返回 x 的整数部分。看下示例：

```
import math

x = 1.1415926
print(math.trunc(x))

```

**exp(x)** 返回 e 的 x 次幂。看下示例：

```
import math

x = 2
print(math.exp(2))

```

**log(x[, base])** 返回 x 的对数，底数默认为 e。看下示例：

```
import math

x = 10
y = 10
# 不指定底数
print(math.log(x))
# 指定底数
print(math.log(x, y))

```

**常量**

```
import math

# 常量 e
print(math.e)
# 常量 π
print(math.pi)

```

**tan(x)** 返回 x 弧度的正切值。看下示例：

```
import math

print(math.tan(math.pi / 3))

```

**atan(x)** 返回 x 的反正切值。看下示例：

```
import math

print(math.atan(1))

```

**sin(x)** 返回 x 弧度的正弦值。看下示例：

```
import math

print(math.sin(math.pi / 3))

```

**asin(x)** 返回 x 的反正弦值。看下示例：

```
import math

print(math.asin(1))

```

**cos(x)** 返回 x 弧度的余弦值。看下示例：

```
import math

print(math.cos(math.pi / 3))

```

**acos(x)** 返回 x 的反余弦值。看下示例：

```
import math

print(math.acos(1))

```

## 3. decimal 模块

decimal 模块为正确舍入十进制浮点运算提供了支持，相比内置的浮点类型 float，它能更加精确的控制精度，能够为精度要求较高的金融等领域提供支持。

decimal 在一个独立的 context 下工作，可以使用 getcontext() 查看当前上下文，如下所示：

```
&gt;&gt; from decimal import *
&gt;&gt;&gt; getcontext()
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

```

从上面的结果中我们可以看到 `prec=28`，这就是默认的精度，我们可以使用 `getcontext().prec = xxx` 来重新设置精度。接下来通过具体示例看一下。

**基本运算**

```
import decimal

d1 = decimal.Decimal(1.1)
d2 = decimal.Decimal(9.9)
print(d1 + d2)
print(d1 - d2)
print(d1 * d2)
print(d1 / d2)

```

执行结果：

```
11.00000000000000044408920985
-8.800000000000000266453525910
10.89000000000000127009514017
0.1111111111111111160952773272

```

上面结果是用了默认精度，我们重新设置下精度再来看一下：

```
import decimal

decimal.getcontext().prec = 2
d1 = decimal.Decimal(1.1)
d2 = decimal.Decimal(9.9)
print(d1 + d2)
print(d1 - d2)
print(d1 * d2)
print(d1 / d2)

```

执行结果：

```
11
-8.8
11
0.11

```

## 4. random 模块

random 模块可以生成随机数，我们来看一下其常用函数。

**random()** 返回 [0.0, 1.0) 范围内的一个随机浮点数。看下示例：

```
import random

print(random.random())

```

**uniform(a, b)** 返回 [a, b) 范围内的一个随机浮点数。看下示例：

```
import random

print(random.uniform(1.1, 9.9))

```

**randint(a, b)** 返回 [a, b] 范围内的一个随机整数。看下示例：

```
import random

print(random.randint(1, 10))

```

**randrange(start, stop[, step])** 返回 [start, stop) 范围内步长为 step 的一个随机整数。看下示例：

```
import random

print(random.randrange(1, 10))
print(random.randrange(1, 10, 2))

```

**choice(seq)** 从非空序列 seq 返回一个随机元素。 看下示例：

```
import random

print(random.choice('123456'))
print(random.choice('abcdef'))

```

**shuffle(x[, random])** 将序列 x 随机打乱位置。看下示例：

```
import random

l = [1, 2, 3, 4, 5, 6]
random.shuffle(l)
print(l)

```

**sample(population, k)** 返回从总体序列或集合中选择的唯一元素的 k 长度列表，用于无重复的随机抽样。看下示例：

```
import random

l = [1, 2, 3, 4, 5, 6]
print(random.sample(l, 3))

```

参考： https://docs.python.org/3/library/numeric.html

<img src="https://img-blog.csdnimg.cn/20200127132036938.png#pic_center" alt="" width="600">
