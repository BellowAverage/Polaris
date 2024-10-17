
--- 
title:  【20天搞定Python】第3天：类型转换、运算符、分支结构 
tags: []
categories: [] 

---
Python第三天内容学习目标:

主题： 类型转换、运算符、分支结构
- 类型转换- 使用算数运算符完成简单的数学计算- 使用赋值运算符对变量进行赋值和修改- 掌握比较运算符的运算规则- 掌握逻辑运算符的运算规则- 分支结构概述
## 常见类型转换

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/8a454808e8c5831ffc1eec8f48503b30.webp?x-oss-process=image/format,png">

### 转换成为整数

```
print(int("100"))  # 100 将字符串转换成为整数

print(int(100.99))  # 100 将浮点数转换成为整数

print(int(True))  # 1 布尔值True转换成为整数是 1
print(int(False)) # 0 布尔值False转换成为整数是 0

# 以下两种情况将会转换失败
'''
99.88 和 56ab 字符串，都包含非法字符，不能被转换成为整数，会报错
print(int("99.88"))
print(int("56ab"))
'''

# 使用int()函数进行类型转换时，还可以传入两个参数，第二个参数用来表示进制。
print(int("21",8))  # 输出的结果是17.八进制的21,对应的十进制数字是17
print(int("F0",16)) # 输出的结果是240.十六进制的F0,对应的十进制数字是240

"""
以下写法会报错。八进制里允许的最大值是7,所以 29 不是一个合法的八进制数
print(int("29",8))
"""
```

### 转换成为浮点数

```
f1 = float("12.34")
print(f1)   # 12.34
print(type(f1)) # float 将字符串的 "12.34" 转换成为浮点数 12.34

f2 = float(23)
print(f2)  # 23.0
print(type(f2)) # float 将整数转换成为了浮点数
```

### 转换成为字符串

```
str1 = str(45)  # '45'
str2 = str(34.56) # '34.56'
str3 = str(True)  # 'True'
print(type(str1),type(str2),type(str3))   # 全部是str类型，也就是字符串类型
```

### 转换成为布尔值

```
print(bool(''))
print(bool(""))
print(bool(0))
print(bool({}))
print(bool([])）
print(bool(())）
print(bool(None)）
```

在python中，只有空字符串'',""，数字0,空字典{},空列表[],空元组(),和空数据None会被转换成为False,其他的都会被转换成为True

### 其他类型转换(了解)

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/ffe3eece525dedb89fa4cf186759039c.webp?x-oss-process=image/format,png">

## 运算符

### 算术运算符

下面以a=10 ,b=20为例进行计算。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/b12c69fba43fdc15c44b579611e2ef51.webp?x-oss-process=image/format,png">

>  
 注意：混合运算时，优先级顺序为： ** 高于 * / % // 高于 + - ，为了避免歧义，建议使用 () 来处理运算符优先级。 并且，不同类型的数字在进行混合运算时，整数将会转换成浮点数进行运算。 


```
print(321 + 123)     # 加法运算
print(321 - 123)     # 减法运算
print(321 * 123)     # 乘法运算
print(321 / 123)     # 除法运算
print(321 % 123)     # 求模运算
print(321 // 123)    # 整除运算
print(321 ** 123)    # 求幂运算
```

#### 算术运算符在字符串里的使用
- 如果是两个字符串做加法运算，会直接把这两个字符串拼接成一个字符串。
```
str1 ='hello'
str2 = 'world'
print(str1+str2)
```
- 如果是数字和字符串做加法运算，会直接报错。
```
str1 ='hello'
a = 1
print(a + str1)
```

报错信息如下：
- 如果是数字和字符串做乘法运算，会将这个字符串重复多次。
```
str1 = 'good'
result = str1*5
print(result)
```

结果：

```
goodgoodgoodgoodgood
```

### 赋值运算符
- 基本赋值运算符
```
# 单个变量赋值
num = 66
print(num)
```

结果：

```
66
```

```
# 同时为多个变量赋值(使用等号连接)
a = b = 8
print(a)
print(b)
```

结果：

```
8

8
```

```
# 多个变量赋值(使用逗号分隔)
num1, f1, str1 = 10, 2.99, "good"
print(num1)
print(f1)
print(str1)
```

结果：

```
10 2.99 good
```

赋值也有错误的情况，比如：

```
# 语法错误，值的个数超过变量的个数，赋值失败
num1,num2 = 1,2,3

# 语法错误，变量的个数超过值得个数，赋值失败
num1,num2,num3,num4 = 1,2,3
```

以上赋值都是有误的。
- 复合赋值运算符
```
# 示例：+=
a = 10
a += 1  # 相当于执行 a = a + 1
print(a)
```

结果：

```
11
```

```
# 示例：*=
a = 100
a *= 5  # 相当于执行 a = a * 5
print(a)
```

结果：

```
500
```

```
# 示例：*=，运算时，符号右侧的表达式先计算出结果，再与左边变量的值运算
a = 10
a *= 1 + 1  # 相当于执行 a = a * (1+1)
print(a)
```

结果：

```
20
```

注意：赋值运算符是从右往左运算，将等号右边的值赋值给等号左边，所以，**等号的左边一定不能是常量或者表达式。**

### 比较运算符

以下假设变量a为10，变量b为20：

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/fc130f76b32be16d71026040eb684d66.webp?x-oss-process=image/format,png">

**字符串使用比较运算符**
- 数字和字符串做==运算结果是false,除了 == 以外的逻辑运算时，会直接报错。
```
str1 = 'good'
a = 2
print(str1==a)
print(str1&gt;a)
```

结果：

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/140da1d2bff3eba7da1cd979054d0bcb.webp?x-oss-process=image/format,png">
- 如果是两个字符串进行比较，会将每个字符都转换成对应的编码，然后逐一进行对比。
```
str1='a'
str2='ABC'
# 将字符转换成为对应的编码  a对应的编码是97,A对应的编码是65
print(str1 &gt; str2)
```

结果：

```
True
```

### 逻辑运算符

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/5e4fd93dfe469c1fe02a6fc6bfd2b356.webp?x-oss-process=image/format,png">

示例：

```
# 声明变量a、b
a = 45
b = 28

# 使用逻辑运算符and
print((a &gt; b) and (b &gt; 10) )
# 即:35&gt;28 and 28&gt;10 ---&gt; True and True ---&gt;True

print((a &gt; b) and (b &gt; 10) and (a &gt; 20) )
# 即: 35&gt;28 and 28&gt;10 and 45&gt;20 ---&gt; True and True and False ---&gt;False

print(a and b and 'hello')
# a、b、'hello'都是有值的即为True，所以取最后一个值

print(a and b and 'hello' and 0)


# 使用逻辑运算符or
print((a &gt; 50) or (b &lt; 10) or (a == b))
# 即：False or False or False --&gt; False

print((a &gt; 50) or (b &gt; 10) or a &lt; b)
# 即：False or True or False --&gt; True

# None,0,''的表示
print(0 or None )
print(a or '')
print(0 or "" or None)
```

运行结果：

```
True False hello 0 False True None 45 None
```

### 运算符优先级

当多种运算符做混合运算时，就会涉及到先运算哪个，后运算哪个问题。以下表格列出了从最高到最低优先级的所有运算符：

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/9fc8329449e31680ab69999284380658.webp?x-oss-process=image/format,png">

### 生活中的判断场景

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/7850aa385dfad87df74436413a533f5e.webp?x-oss-process=image/format,png">

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/bad9ec90f0c1cc16c8a70fa8d8172ba1.webp?x-oss-process=image/format,png">

if语句的使用
- if语句是用来进行判断的，其使用格式如下：
```
if 要判断的条件:
    条件成立时，要做的事情
```
- 案例一:
```
age = 30
print("------if判断开始------")
if age &gt;= 18:
    print("我已经成年了")
print("------if判断结束------")
```
- 运行结果:
```
------if判断开始------
我已经成年了
------if判断结束------
```
- 案例二:
```
age = 16
print("------if判断开始------")
if age &gt;= 18:
    print("我已经成年了")
print("------if判断结束------")
```
- 运行结果:
```
------if判断开始------
------if判断结束------
```

**小总结：**

以上2个案例仅仅是age变量的值不一样，导致结果却不同；能够看得出if判断语句的作用：就是当满足一定条件时才会执行代码块语句，否则就不执行代码块语句。

注意：代码的缩进为一个tab键，或者4个空格

## 总结

本节课主要介绍了数据类型的转换，并且学会了使用运算符以及由运算符构成的表达式，其实变量、数据类型、运算符结合使用可以解决很多我们生活中的实际问题。所以运算符和表达式对于任何一门编程语言都是非常重要的。最后我们还简单介绍了if的使用，详细使用我们下一次课带领大家继续学习。 
