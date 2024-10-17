
--- 
title:  python基本数据类型（一）数字（number）类型 
tags: []
categories: [] 

---
### 数字（整型、浮点型、复数型）

#### 1. int 整型,表示范围无穷大

```
a = 1
print(a, "是", type(a), "类型")
a = -1
print(a, "是", type(a), "类型")
a = 2**100
print(a, "是", type(a), "类型")

```

运行结果：

```
1 是 &lt;class 'int'&gt; 类型
-1 是 &lt;class 'int'&gt; 类型
1267650600228229401496703205376 是 &lt;class 'int'&gt; 类型

```

##### 进制 （print进行输出的时候，默认情况下是十进制方式输出）

###### 二进制（0、1）

```
a = 0b10101
print(a, "是", type(a), "类型")

```

运行结果：

```
21 是 &lt;class 'int'&gt; 类型

```

###### 十六进制（0-9，a-f）

```
a = 0x1fb
print(a, "是", type(a), "类型")

```

运行结果：

```
507 是 &lt;class 'int'&gt; 类型

```

###### 八进制（1-7）

```
a = 0o172
print(a, "是", type(a), "类型")

```

运行结果：

```
122 是 &lt;class 'int'&gt; 类型

```

###### 进制转换 bin oct hex

###### **bin()**

```
help(bin) 
#bin(number) =&gt; 二进制字符串

a = 10
print(a, "转换为二进制的结果是", bin(a))
a = 0x10
print(a, "转换为二进制的结果是", bin(a))

```

运行结果：

```
10 转换为二进制的结果是 0b1010
16 转换为二进制的结果是 0b10000

```

###### **hex()**

```
help(hex)

a=10
print(a, "转换为十六进制的结果是", hex(a))
a = 0x10
print(a, "转换为十六进制的结果是", hex(a))

```

运行结果：

```
10 转换为十六进制的结果是 0xa
16 转换为十六进制的结果是 0x10

```

###### **oct()**

```
help(oct)

a=10
print(a, "转换为八进制的结果是", oct(a))
a = 0x10
print(a, "转换为八进制的结果是", oct(a))

```

运行结果：

```
10 转换为八进制的结果是 0o12
16 转换为八进制的结果是 0o20

```

###### int()

int的参数<mark>可以是数字也可以是字符串</mark>，当参数是一个<mark>字符串</mark>时，<mark>指定base（给的参数是几进制数，默认base是10）</mark>，<mark>返回一个十进制int</mark>

```
a = 10
a_oct = oct(a)
a_int = int(a_oct, base=8)
print(a_int)
a_int = int('111')
print(a_int)
a_int = int('111', base=10)
print(a_int)
a_int = int('1010', base=2)
print(a_int)
a_int = int('0b1010', base=2)
print(a_int)

int的参数是数字时
a = 0b101110
print(int(a))
a = 0o10523
print(int(a))
a = 0x134a
print(int(a))


```

运行结果：

```
10
111
111
10
10

```

```
46
4435
4938

```

#### 2. float浮点型

##### 表示方法

```
b = 1.1
print(b,"的数据类型是",type(b))
b = 1.
print(b,"的数据类型是",type(b))
b = 4.2E-10
print(b,"的数据类型是",type(b))

```

```
1.1 的数据类型是 &lt;class 'float'&gt;
1.0 的数据类型是 &lt;class 'float'&gt;
4.2e-10 的数据类型是 &lt;class 'float'&gt;

```

##### float是<mark>不精确</mark>的

```
i = 1
i = i-0.1
print(i)
i = i-0.1
print(i)
i = i-0.1
print(i)

```

```
0.9
0.8
0.7000000000000001

```

###### 不精确的原因：

```
十进制5表示为101
5 =&gt; 101
0.1 =&gt;  0.5 , 0.20 , 0.125 , 0.0625
    =&gt;  部分小数是无法用二进制精确的表示
    =&gt;  0b0.1 =&gt; 0.5
条件判断 如果用浮点型数据变量尽量要使用&lt;或&gt;来进行比较
避免使用等于来比较     a==0.6

```

##### Decimal 定点型 ，可以表示精确地浮点数

```
# Decimal 可以表示精确地浮点数
# 2.1 =&gt; 整数位和小数位分别存储 =&gt; 使用整数的存储方式来存储的
# 2 =&gt; 10
# 1 =&gt; 1

```

```
from decimal import Decimal
# Decimal 数据类型
my_dec = Decimal('0.1') #表示精确的0.1数据
print(my_dec,type(my_dec))

my_dec = Decimal(0.1)
print(my_dec,type(my_dec))

my_dec = Decimal('0.7')
print(my_dec,type(my_dec))

my_dec = Decimal(0.7)
print(my_dec,type(my_dec))

```

运行结果：

```
0.1 &lt;class 'decimal.Decimal'&gt;
0.1000000000000000055511151231257827021181583404541015625 &lt;class 'decimal.Decimal'&gt;
0.7 &lt;class 'decimal.Decimal'&gt;
0.6999999999999999555910790149937383830547332763671875 &lt;class 'decimal.Decimal'&gt;

```

#### 3.复数

```
c = 1+1j
print(c,type(c))
d = 4-2j
print(d.real,d.imag,type(d))

```

```
(1+1j) &lt;class 'complex'&gt;
4.0 -2.0 &lt;class 'complex'&gt;

```
