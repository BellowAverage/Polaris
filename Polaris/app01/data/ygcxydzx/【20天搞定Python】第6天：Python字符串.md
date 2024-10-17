
--- 
title:  【20天搞定Python】第6天：Python字符串 
tags: []
categories: [] 

---
字符串的意思就是“一串字符”，比如"Hello world"是一个字符串，"How are you？"也是一个字符串。

Python 要求字符串必须使用引号括起来，使用单引号也行，使用双引号也行，只要两边的引号能配对即可。

字符串引号里面的的每个基本单元叫做字符，比如字符串"abc"中，"a"、"b"和"c"就是字符串组成的基本单元，它们都是字符。

如下定义的变量，存储的是字符串类型的值

>  
 a = "I'm Bob"  # 一对双引号 b = 'I am Bob'  # 一对单引号 c = 'He said:I\'m Bob'  # 转义字符 d = '''I'm Bob'''  # 三个单引号 e = """I'm Bob """  # 三个双引号 


小总结：
- 双引号或者单引号中的数据，就是字符串- 如果使用一对引号来定义字符串，当出现符号冲突时可以使用转义字符，比如变量c- 使用三个单引号或者三个双引号定义的字符串可以包裹任意文本
## 字符串的运算

Python为字符串类型提供了非常丰富的运算符，我们可以使用+运算符来实现字符串的拼接，可以使用*运算符来重复一个字符串的内容，可以使用in和not in来判断一个字符串是否包含另外一个字符串，我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符。

### 拼接和重复

下面的例子演示了使用   + 和  * 运算符来实现字符串的拼接和重复操作。

```
s1 = 'hello' + ' ' + 'world'
print(s1)    # 结果：hello world
s2 = '!' * 3
print(s2)    # 结果：!!!
s1 += s2     # s1 = s1 + s2
print(s1)    # 结果：hello world!!!
s1 *= 2      # s1 = s1 * 2
print(s1)    # 结果：hello world!!!hello world!!!
```

用  * 实现字符串的重复是非常有意思的一个运算符，在很多编程语言中，要表示一个有10个 a 的字符串，你只能写成"aaaaaaaaaa"，但是在Python中，你可以写成'a' * 10。你可能觉得"aaaaaaaaaa"这种写法也没有什么不方便的，那么想一想，如果字符   a 要重复100次或者1000次又会如何呢？

### 比较运算

对于两个字符串类型的变量，可以直接使用比较运算符比较两个字符串的相等性或大小。

需要说明的是，因为字符串在计算机内存中也是以二进制形式存在的，那么字符串的比较其实比的是：每个字符对应的编码的大小。

例如A的编码是65， 而a的编码是97，所以'A' &lt; 'a'的结果相当于就是65 &lt; 97的结果，很显然是True；

而'boy' &lt; 'bad'，因为第一个字符都是'b'比不出大小，所以实际比较的是第二个字符的大小，显然'o' &lt; 'a'的结果是False，所以'boy' &lt; 'bad'的结果也是False。

如果不清楚两个字符对应的编码到底是多少，可以使用ord函数来获得，例如ord('A')的值是65，而ord('赵')的值是36213。

下面的代码为大家展示了字符串的比较运算。

```
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2) # False
print(s1 &lt; s2)  # True
print(s2 == 'hello world')    # True
print(s2 == 'Hello world')    # False
print(s2 != 'Hello world')    # True
s3 = '赵四'
print(ord('赵'), ord('四'))  # 36213 22235
s4 = '王大拿'
print(ord('王'), ord('大'), ord('拿'))  # 29579 22823 25343
print(s3 &gt; s4, s3 &lt;= s4)  # True False
```

需要强调一下的是，字符串的比较运算比较的是字符串的内容，Python中还有一个is运算符（身份运算符），如果用is来比较两个字符串，它比较的是两个变量对应的字符串是否在内存中相同的位置（内存地址），简单的说就是两个变量是否对应内存中的同一个字符串。看看下面的代码就比较清楚is运算符的作用了。

```
s1 = 'hello world'
s2 = 'hello world1'
s3 = s2
# 比较字符串的内容
print(s1 == s2, s2 == s3)    # False True
# 比较字符串的内存地址
print(s1 is s2, s2 is s3)    # False True
```

总结：s1==s2 比较的是字符串里面的内容，只要内容相同结果就是True，不同就是False；而s1 is s2则比较的是内存地址，两者内存是不一样的所以False。

### 成员运算

Python中可以用in和not in判断一个字符串中是否存在另外一个字符或字符串，in和not in运算通常称为成员运算，会产生布尔值True或False，代码如下所示。

```
s1 = 'hello, world'
print('he' in s1)    # True
s2 = 'goodbye'
print(s2 in s1)      # False
```

**获取字符串长度**

获取字符串长度没有直接的运算符，而是使用内置函数len，我们在上节课的提到过这个内置函数，代码如下所示。

```
s = 'hello, world'
print(len(s))                  # 12
print(len('goodbye, world'))    # 14
```

## 索引与切片

字符串中的每个字符都有表示位置的下标值，下标范围从左往右从0开始依次增加或者从右往左从-1开始依次减少。

比如我们有字符串"soldier",现在它的下标怎么命名的？

如果希望从字符串中取出某个字符，我们可以对字符串进行索引运算，运算符是[n]，其中n是一个整数，假设字符串的长度为N，那么n可以是从0到N-1的整数，其中0是字符串中第一个字符的索引，而N-1是字符串中最后一个字符的索引，通常称之为正向索引；

<img alt="" height="209" src="https://img-blog.csdnimg.cn/20210617171817178.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lnY3h5ZHp4,size_16,color_FFFFFF,t_70" width="628">

在Python中，字符串的索引也可以是从-1到-N的整数，其中-1是最后一个字符的索引，而-N则是第一个字符的索引，通常称之为负向索引。注意，因为字符串是不可变类型，所以不能通过索引运算修改字符串中的字符。

<img alt="" height="220" src="https://img-blog.csdnimg.cn/20210617171859962.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lnY3h5ZHp4,size_16,color_FFFFFF,t_70" width="627">

```
s = 'abc123456'
n = len(s)

# 获取第一个字符
print(s[0], s[-n])    # a a

# 获取最后一个字符
print(s[n-1], s[-1])  # 6 6

# 获取索引为2或-7的字符
print(s[2], s[-7])    # c c

# 获取索引为5和-4的字符
print(s[5], s[-4])    # 3 3
```

需要提醒大家注意的是，在进行索引操作时，如果索引越界（正向索引不在0到N-1范围，负向索引不在-1到-N范围），会引发IndexError异常，错误提示信息为：string index out of range（字符串索引超出范围）。

如果要从字符串中取出多个字符，我们可以对字符串进行切片，运算符是[i:j:k]，其中i是开始索引，索引对应的字符可以取到；j是结束索引，索引对应的字符不能取到；k是步长，默认值为1，表示从前向后获取相邻字符的连续切片，所以:k部分可以省略。

假设字符串的长度为N，当k &gt; 0时表示正向切片（从前向后获取字符），如果没有给出i和j的值，则i的默认值是0，j的默认值是N；当k &lt; 0时表示负向切片（从后向前获取字符），如果没有给出i和j的值，则i的默认值是-1，j的默认值是-N - 1。如果不理解，直接看下面的例子，记住第一个字符的索引是0或-N，最后一个字符的索引是N-1或-1就行了。

```
s = 'abc123456'

# i=2, j=5, k=1的正向切片操作
print(s[2:5])       # c12

# i=-7, j=-4, k=1的正向切片操作
print(s[-7:-4])     # c12

# i=2, j=9, k=1的正向切片操作
print(s[2:])        # c123456

# i=2, j=9, k=2的正向切片操作
print(s[2::2])      # c246

# i=0, j=9, k=2的正向切片操作
print(s[::2])       # ac246

# i=1, j=-1, k=2的正向切片操作
print(s[1:-1:2])  # b135

# i=7, j=1, k=-1的负向切片操作
print(s[7:1:-1])    # 54321c

# i=-2, j=-8, k=-1的负向切片操作
print(s[-2:-8:-1])  # 54321c

# i=7, j=-10, k=-1的负向切片操作
print(s[7::-1])     # 54321cba

# i=-1, j=1, k=-1的负向切片操作
print(s[:1:-1])     # 654321c

# i=0, j=9, k=1的正向切片
print(s[:])         # abc123456
```

## 循环遍历

如果希望从字符串中取出每个字符，可以使用for循环对字符串进行遍历，有两种方式。

方式一：

```
s1 = 'hello'
for index in range(len(s1)):
    print(s1[index])
```

方式二：

```
s1 = 'hello'
for ch in s1:
    print(ch)
```

## 字符串的方法

在Python中，我们可以通过字符串类型自带的方法对字符串进行操作和处理，对于一个字符串类型的变量，我们可以用变量名.方法名()的方式来调用它的方法。所谓方法其实就是跟某个类型的变量绑定的函数，后面我们讲面向对象编程的时候还会对这一概念详加说明。

**大小写相关操作**

下面的代码演示了和字符串大小写变换相关的方法。

>  
 capitalize(): 字符串首字母大写 title(): 字符串中每个单词首字母大写 upper(): 字符串全部大写 lower(): 字符串全部小写 


```
s1 = 'hello, world!'

# 使用capitalize方法获得字符串首字母大写后的字符串
print(s1.capitalize())   # Hello, world!
# 使用title方法获得字符串每个单词首字母大写后的字符串
print(s1.title())        # Hello, World!
# 使用upper方法获得字符串大写后的字符串
print(s1.upper())        # HELLO, WORLD!
s2 = 'GOODBYE'
# 使用lower方法获得字符串小写后的字符串
print(s2.lower())        # goodbye
```

查找操作

如果想在一个字符串中从前向后查找有没有另外一个字符串，可以使用字符串的find或index方法。

>  
 find(): 从字符串中查找另一个字符串(参数)所在的位置，如果存在则返回匹配的字符串的首字母下标，没有找到则返回-1 index(): 与find方法类似,如果找不到则会引发异常。 


```
s = 'hello, world!'

# find方法从字符串中查找另一个字符串所在的位置
# 找到了返回字符串中另一个字符串首字符的索引
print(s.find('or'))        # 8
# 找不到返回-1
print(s.find('good'))      # -1
# index方法与find方法类似
# 找到了返回字符串中另一个字符串首字符的索引
print(s.index('or'))       # 8
# 找不到引发异常
print(s.index('good'))     # ValueError: substring not found
```

在使用find和index方法时还可以通过方法的参数来指定查找的范围，也就是查找不必从索引为0的位置开始。find和index方法还有逆向查找（从后向前查找）的版本，分别是rfind和rindex，

>  
 在使用find和index方法时还可以通过方法的参数来指定查找的范围，也就是查找不必从索引为0的位置开始。find和index方法还有逆向查找（从后向前查找）的版本，分别是rfind和rindex， 


代码如下所示。

```
s = 'hello good world!'

# 从前向后查找字符o出现的位置(相当于第一次出现)
print(s.find('o'))       # 4
# 从索引为5的位置开始查找字符o出现的位置
print(s.find('o', 5))    # 7
# 从后向前查找字符o出现的位置(相当于最后一次出现)
print(s.rfind('o'))      # 12
```

**判断**

可以通过字符串的startswith、endswith来判断字符串是否以某个字符串开头和结尾；还可以用is开头的方法判断字符串的特征，这些方法都返回布尔值，

>  
 startswith():判断字符串是否以指定的字符串开头，返回布尔值结果 endswith()：判断字符串是否以指定的字符串结尾，返回布尔值结果 isdigit()：判断字符串是否由数字构成，返回布尔值结果 isalpha()：判断字符串是否以字母构成，返回布尔值结果 isalnum()：判断字符串是否以数字和字母构成，返回布尔值结果 


代码如下所示。

```
s1 = 'hello, world!'

# startwith方法检查字符串是否以指定的字符串开头返回布尔值
print(s1.startswith('He'))    # False
print(s1.startswith('hel'))   # True
# endswith方法检查字符串是否以指定的字符串结尾返回布尔值
print(s1.endswith('!'))       # True

s2 = 'abc123456'

# isdigit方法检查字符串是否由数字构成返回布尔值
print(s2.isdigit())    # False
# isalpha方法检查字符串是否以字母构成返回布尔值
print(s2.isalpha())    # False
# isalnum方法检查字符串是否以数字和字母构成返回布尔值
print(s2.isalnum())    # True
```

**去除空格**

字符串的strip方法可以帮我们获得将原字符串修剪掉左右两端空格之后的字符串。这个方法非常有实用价值，通常用来将用户输入中因为不小心键入的头尾空格去掉，strip方法还有lstrip和rstrip两个版本，相信从名字大家已经猜出来这两个方法是做什么用的。

```
s = '   helloworld@126.com  \t\r\n'
# strip方法获得字符串修剪左右两侧空格之后的字符串
print(s.strip())    # helloworld@126.com
```

**格式化字符串**

在Python中，字符串类型可以通过center、ljust、rjust方法做居中、左对齐和右对齐的处理。

```
s = 'hello, world'

# center方法以宽度20将字符串居中并在两侧填充*
print(s.center(20, '*'))  # ****hello, world****
# rjust方法以宽度20将字符串右对齐并在左侧填充空格
print(s.rjust(20))        #         hello, world
# ljust方法以宽度20将字符串左对齐并在右侧填充~
print(s.ljust(20, '~'))   # hello, world~~~~~~~~
```

我们之前讲过，在用print函数输出字符串时，可以用下面的方式对字符串进行格式化。

```
a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))
```

当然，我们也可以用字符串的方法来完成字符串的格式，代码如下所示。

```
a = 321
b = 123
print('{0} * {1} = {2}'.format(a, b, a * b))
```

从Python 3.6开始，格式化字符串还有更为简洁的书写方式，就是在字符串前加上f来格式化字符串，在这种以f打头的字符串中，{变量名}是一个占位符，会被变量对应的值将其替换掉，代码如下所示。

```
a = 321
b = 123
print(f'{a} * {b} = {a * b}')
```

如果需要进一步控制格式化语法中变量值的形式，可以参照下面的表格来进行字符串格式化操作。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/3e7a65f51bb29a464978722f3fc25d63.webp?x-oss-process=image/format,png">

**其他方法**

除了上面讲到的方法外，字符串类型还有很多方法，如拆分、合并、编码、解码等，这些方法等我们用到的时候再为大家进行续点讲解。

对于字符串类型来说，还有一个常用的操作是对字符串进行匹配检查，即检查字符串是否满足某种特定的模式。

例如，一个网站对用户注册信息中用户名和邮箱的检查，就属于模式匹配检查。

实现模式匹配检查的工具叫做正则表达式，Python语言通过标准库中的re模块提供了对正则表达式的支持，我们会在后续的文章中为大家讲解这个知识点。 
