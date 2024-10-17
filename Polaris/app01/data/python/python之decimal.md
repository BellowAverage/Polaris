
--- 
title:  python之decimal 
tags: []
categories: [] 

---
decimal是python的标准库之一，我们通常用它来进行浮点数的运算和比较。

#### 为什么需要使用decimal

因为使用浮点数计算比较会有误差，请看下面的例子

```
a1 = 1.01
b1 = 1.02

if a1+b1 == 2.03:
    print('ok')
else:
    print('no')
# 有精度的误差
print(a1+b1)

```

结果:

```
no
2.0300000000000002

```

#### decimal实现

我们建议浮点数的运算和比较采用Decimal来实现

```
from decimal import Decimal
a2 = Decimal('1.01')
b2 = Decimal('1.02')

if a2+b2 == Decimal('2.03'):
    print('ok')
else:
    print('no')
print(a2+b2)
print(type(a2+b2))

```

结果:

```
ok
2.03
&lt;class 'decimal.Decimal'&gt;

```

#### 注意事项

Decimal初始化值必须是数字字符串或者是整数,浮点数的要转成字符串后才传入

```
print(Decimal('1.01'))
print(Decimal(1.01))

```

结果:

```
1.01
1.0100000000000000088817841970012523233890533447265625

```
