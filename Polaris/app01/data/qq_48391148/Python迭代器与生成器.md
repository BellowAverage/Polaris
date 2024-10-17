
--- 
title:  Python迭代器与生成器 
tags: []
categories: [] 

---
**目录**

































## 1.0 python推导式

### 1.1  什么是推导式？

#### 1.1.1  列表推导式

```
tmp = []
for i in range(20):
    if i % 3:
        tmp.append(i*i)
print(tmp)

E:\python\python3.9.1\python.exe E:/tlbb/2022-07-08-迭代器与生成器/01.推导式.py
[1, 4, 16, 25, 49, 64, 100, 121, 169, 196, 256, 289, 361]
[1, 4, 16, 25, 49, 64, 100, 121, 169, 196, 256, 289, 361]

Process finished with exit code 0
```

**列表推导式写法：**

```
result = [ i*i for i in range(20) if i % 3 ]
print(result)

E:\python\python3.9.1\python.exe E:/tlbb/2022-07-08-迭代器与生成器/01.推导式.py
[1, 4, 16, 25, 49, 64, 100, 121, 169, 196, 256, 289, 361]

Process finished with exit code 0
```

```
result = [i for i in range(200) if math.sqrt(i).is_integer()]
print(result)

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
```

**示例：将列表里的小数保留两位小数输出到列表**

```
lst1 = [2.45345, 4.3454325, 9, 82.234321, 83.841234]
lst2 = [float("%0.2f" % j) for j in lst1 if j]
print(lst2)

['2.45', '4.35', '9.00', '82.23', '83.84']
```

**示例：找到嵌套列表中名字含有2个'e'的所有名字 **

```
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva', 'Elven']]
```

方法1：

```
for i in names:
    for j in i:
        if j.lower().count('e') &gt;= 2:
            print(j)

Jefferson
Wesley
Steven
Jennifer
Elven
```

列表推导式：

```
result1 = [j for i in names for j in i if j.lower().count('e') &gt;= 2]
print(result1)

['Jefferson', 'Wesley', 'Steven', 'Jennifer', 'Elven']
```

#### #################################

#### 1.1.2  集合推导式

因为集合的特性，集合推导式自带去重功能。

```
# 集合推导式 --》 天生去重
str1 = "qwerqwerasasfdfd"
print(set(str1))
print({i for i in str1})

E:\python\python3.9.1\python.exe E:/tlbb/2022-07-08-迭代器与生成器/01.推导式.py
{'e', 'f', 'q', 'd', 'a', 'w', 's', 'r'}
{'e', 'f', 'q', 'd', 'a', 'w', 's', 'r'}
```

#### #################################

#### ’1.1.3  字典推导式

```
# 字典推导式
print({x: y for x, y in [('a', 1), ('b', 2)]})
# 统计字符串中每一个字符出现的字数
str1 = "aleiafesl5e-e;'ree2f5a43"
print({x: str1.count(x) for x in str1})
# 过滤长度小于三的字符串，并将剩下的转换成大写字母
q1 = ['a', 'ab', 'abc', 'abcd', 'abcde']
print([i.upper() for i in q1 if len(i) &gt;= 3])
# 求（x,y）其中x是0-5之间的偶数，y是0-5之间的奇数组成的元组列表
result = [(x, y) for x in range(6) for y in range(6) if x % 2 == 0 and y % 2 ==1]
print(result)
# 快速跟换key和value
q3 = {'a': 10, 'b': 34}
print({q3[x]: x for x in q3})
# 合并大小写对应的value值，将key统一写成小写
q4 = {'B': 3, 'a': 1, 'b': 6, 'c': 3, 'A': 4}
result2 = {x.lower(): q4.get(x.lower(), 0) + q4.get(x.upper(), 0) for x, y in q4.items()}
print(result2)

str1 = "aleiafesl5e-e;'ree2f5a43"
tmp = {}
for i in str1:
    tmp[i] = tmp.get(i, 0) + 1
print(tmp)



E:\python\python3.9.1\python.exe E:/tlbb/2022-07-08-迭代器与生成器/01.推导式.py
{'a': 1, 'b': 2}
{'a': 3, 'l': 2, 'e': 6, 'i': 1, 'f': 2, 's': 1, '5': 2, '-': 1, ';': 1, "'": 1, 'r': 1, '2': 1, '4': 1, '3': 1}
['ABC', 'ABCD', 'ABCDE']
[(0, 1), (0, 3), (0, 5), (2, 1), (2, 3), (2, 5), (4, 1), (4, 3), (4, 5)]
{10: 'a', 34: 'b'}
{'b': 9, 'a': 5, 'c': 3}
{'a': 3, 'l': 2, 'e': 6, 'i': 1, 'f': 2, 's': 1, '5': 2, '-': 1, ';': 1, "'": 1, 'r': 1, '2': 1, '4': 1, '3': 1}

Process finished with exit code 0

```

**#################################**

## 2.0  python可迭代对象

之前只学习了一部分内容的时候说过，可以for循环的都属可迭代对象，那么有哪些常见可迭代对象？

list， set， dict，tuple，str，file等这些都属容器数据结构

**#################################**

### 2.1  什么是容器？：

**#################################**

### 2.2  可迭代对象

```
str1 = "abc"
# 一般来说容器类型都是可迭代对象
print(dir(str1))


E:\python\python3.9.1\python.exe E:/tlbb/2022-07-08-迭代器与生成器/02.迭代器和生成器.py
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

```
print(hasattr(str1, "__iter__"))

True
```

```
class A:
    def __iter__(self):
        return None

```

**#################################**

#### 2.2.1  判断一个对象是不是可迭代对象

使用iterable判断

```
from collections import Iterable
a='abc'
b = [1,2,3]
c=(4,5,6)
d={"name": 'tom', "age": 22}
if isinstance(a, Iterable):
    print("a是可迭代对象")
if isinstance(b, Iterable):
    print("b是可迭代对象")

E:\python\python3.9.1\python.exe E:/tlbb/2022-07-08-迭代器与生成器/01.推导式.py
a是可迭代对象
b是可迭代对象
```

**#################################**

## 3.0  迭代器（iterator）

 任何实现了__iter__()和__next__()都是迭代器

### 3.1 编写迭代器，实现range

```
class Myrange():
    def __init__(self, num):
        self.num = num
        self.start = 0

    def __iter__(self):
        self.cur_val = self.start - 1
        return self

    def __next__(self):
        self.cur_val += 1
        if self.cur_val &lt; self.num:
            return self.cur_val
        else:
            raise StopIteration


for i in Myrange(10):
    print(i)
```

```
E:\python\python3.9.1\python.exe E:/tlbb/2022-07-08-迭代器与生成器/02.迭代器和生成器.py
0
1
2
3
4
5
6
7
8
9
```

**#################################**

### 3.2 编写迭代器，实现斐波拉契数列

```
class Fblq():
    n = 0
    def __init__(self, num):
        self.num = num
        self.next = 0
        self.start = 1
        self.middle = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        if self.n == 1 or self.n == 2:
            return self.middle
        if self.next &lt;= self.num:
            self.next = self.start + self.middle
            self.middle = self.start
            self.start = self.next
            return self.next
        else:
            raise StopIteration

for i in Fblq(6):
    print(i)

```

```
E:\python\python3.9.1\python.exe E:/tlbb/2022-07-08-迭代器与生成器/02.迭代器和生成器.py
1
1
2
3
5
8
```

**#################################**

## 4.0 生成器（generator）

### 4.1 什么是生成器？

>  
   
   生成器算得上是Python语言中最吸引人的特性之一，生成器其实是一种特殊的迭代器，  
   
   
   不过这种迭代器更加优雅。它不需要手动编写__iter__()和__next__()方法，只需要一个  
   
   
   yiled关键字。 
   
 

### 4.2 生成器表达式

```
def get_content():
    print("start yield...")
    yield 3
    print("second yield")
    yield 4
    print("end...")

g1 = get_content()
print(dir(g1))
print('*'*20)
print(next(g1))
print('*'*20)
print(next(g1))
print('*'*20)
print(next(g1))
```

```
********************
start yield...
3
********************
second yield
4
********************
end...
Traceback (most recent call last):
  File "E:\tlbb\2022-07-08-迭代器与生成器\02.迭代器和生成器.py", line 115, in &lt;module&gt;
    print(next(g1))
StopIteration

Process finished with exit code 1

```

**使用生成器编写range**

```
def Myrange(num):
    i = 0
    while i &lt; num:
        yield i
        i += 1
for i in Myrange(3):
    print(i)

```

```
E:\python\python3.9.1\python.exe E:/tlbb/2022-07-08-迭代器与生成器/02.迭代器和生成器.py
0
1
2

Process finished with exit code 0
```


