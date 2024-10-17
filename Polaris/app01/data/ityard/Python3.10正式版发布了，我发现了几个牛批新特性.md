
--- 
title:  Python3.10正式版发布了，我发现了几个牛批新特性 
tags: []
categories: [] 

---
来源：juejin.cn/post/7015590447745613854

Python 3.10正式发布，你尝鲜了吗？

>  
  本文参考自 Python官方文档 ：Python Release Python 3.10.0 | Python.org<sup>[1]</sup> 
 

在正值国庆假期人山人海的2021年10月4号，Python官方正式发布了Python3.10.0<sup>[2]</sup>。作为一只假期期间宅着不动的coding人，自然是第一时间体验了一波。相较于之前的版本，该版本有以下主要变更。

#### 新的 Union Type表达

新版本简化了 Union Type 的使用 ，改为更为简洁的`|`

旧版：

```
from typing import Union
a: Union[int, str] = 1
```

新的版本：

```
a: str | int = 1
```

二者完全等价：

```
Union[int, str] == int | str # True
```

这类变化在其他地方也相似：

```
# 旧版:
# def f(list: List[Union[int, str]], param: Optional[int]) -&gt; Union[float, str]
def f(list: List[int | str], param: int | None) -&gt; float | str:
    pass

f([1, "abc"], None)

# 旧版： 
# typing.List[typing.Union[str, int]]
typing.List[str | int]
list[str | int]

# 旧版： 
# typing.Dict[str, typing.Union[int, float]]
typing.Dict[str, int | float]
dict[str, int | float]
```

该特性也可用于 `isinstance`和`issubclass`

```
# True
isinstance("FunnySaltyFish", int|str)

# True 
issubclass(str, str|int)
```

#### zip 可选严格模式

zip新增可选参数`strict`， 当该选项为True时，传入zip的两个可迭代项长度必须相等，否则将抛出 `ValueError`

旧版（及不加此参数），当二者长度不等时，以长度较小的为准

```
names = ["a","b","c","d"]
numbers = [1,2,3]
z = zip(names,numbers)
for each in z:
    print(each)
    
# ('a', 1)
# ('b', 2)
# ('c', 3)
```

设置strict为True

```
# ...
z = zip(names,numbers,strict=True)
# ...

d:\projects\python\learn\Py310探索.py in &lt;module&gt;
      3 numbers = [1,2,3]
      4 z = zip(names,numbers,strict=True)
----&gt; 5 for each in z:
      6     print(each)

ValueError: zip() argument 2 is shorter than argument 1
```

#### 带括号的上下文管理器

with可以加括号了

```
with (CtxManager() as example):
    ...

with (
    CtxManager1(),
    CtxManager2()
):
    ...

with (CtxManager1() as example,
      CtxManager2()):
    ...

with (CtxManager1(),
      CtxManager2() as example):
    ...

with (
    CtxManager1() as example1,
    CtxManager2() as example2
):
    ...
```

如

```
import pathlib
p = pathlib.Path()
p1 = p/"text1.txt" # 内容：文本1的内容
p2 = p/"text2.txt" # 内容：文本2的内容
with(
    p1.open(encoding="utf-8") as f1,
    p2.open(encoding="utf-8") as f2
):
    print(f1.read(), f2.read(), sep="\n") 
    
    # 文本1的内容
 # 文本2的内容
```

#### 显式类型别名

使用 TypeAlias 显式标注类型别名，提高可读性

旧的方式：

```
x = int
def plus_int(a:x,b:x) -&gt; x:
    return a+b
```

可以看到，x很容易被搞混

新的方式：使用 TypeAlias表明这是个别名

```
from typing import TypeAlias
x : TypeAlias = int
def plus_int(a:x,b:x) -&gt; x:
    return a+b
```

#### match...case语句

对，就是其他语言的`switch-case`，python终于提供了支持，还是加强版的

完整语法参见：PEP 634 -- Structural Pattern Matching: Specification | Python.org<sup>[3]</sup>

举几个例子：

基本的类型匹配：

```
day = 6
match day:
    case 1:
        print("星期一")
    case 6 | 7:
        print("周末")
    case _ : 
        print("其他情况")
```

subject：这在处理命令行参数的时候特别有用

```
"""
    @copyright : [FunnySaltyFish](https://funnysaltyfish.github.io)
    @date : 2021/10/05 21:08:42
"""
command = "save 1.txt"
# 试着把command改成 list / copy 1.txt 2.txt 看看效果
match command.split(" "):
    case ["list"]:
        print("列出文件~")
    case ["save", file_name]:
        print(f"保存文件到 {file_name}")
    case ["copy",source,target]:
        print(f"拷贝 {source} -&gt; {target}")
```

也可以匹配对象：

```
class Person():
    pass

class Student(Person):
    def __init__(self, id: int) -&gt; None:
        self.id = id

class Teacher(Person):
    def __init__(self, name: str) -&gt; None:
        self.name = name

a = Student(1)
# a = Student(2)
# a = Teacher("FunnySaltyFish")
match a:
    case Student(id = 2):
        print(f"这是位学生，且id正好是2")
    case Student():
        print(f"这是学生，id为{a.id}")
    case Teacher():
        print(f"这是老师, 姓名为{a.name}")
```

当然也可以匹配字典：

```
d = {
    "name" : "李四", # 张三
    "age" : 18,
    "hobby" : "阅读"
} 
match d:
    case {"name":"张三", **args}:
        # **收集其他参数
        print("这是张三", args) # 这是张三 {'age': 18, 'hobby': '阅读'}
    case {"name" : name , "age" : age, "hobby": hobby}:
        print(f"我叫{name}, 今年{age}岁, 喜欢{hobby}") #我叫李四,今年18岁，喜欢阅读
```

更复杂的还有结合Guard、匹配捕获等使用，具体可以参见：PEP 635 -- Structural Pattern Matching: Motivation and Rationale | Python.org<sup>[4]</sup> 和 PEP 636 -- Structural Pattern Matching: Tutorial | Python.org<sup>[5]</sup>

#### 更友好的报错提示

现在，当你的括号、引号未闭合时，python会抛出更加清晰明了的错误

```
str = "未闭合的str

File "d:\projects\python\learn\Py310探索.py", line 90
    str = "未闭合的str
          ^
SyntaxError: unterminated string literal (detected at line 90)
```

```
arr = [1, 2, 2, 3
    
  File "d:\projects\python\learn\Py310探索.py", line 91
    arr = [1, 2, 2, 3
          ^
SyntaxError: '[' was never closed
```

#### 其他一些更新：

###### distutils 被弃用

推荐使用 setuptools

###### 需要 OpenSSL 1.1.1 及以上版本

###### 移除 Py_UNICODE编码API

###### PyUnicodeObject的wstr被弃用，并将在之后移除

完。摸鱼去了。

#### 参考资料

[1]

https://www.python.org/downloads/release/python-3100/: **https://link.juejin.cn?target=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-3100%2F**

https://www.python.org/downloads/release/python-3100/: **https://link.juejin.cn?target=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-3100%2F**

https://www.python.org/dev/peps/pep-0634/#id25: **https://link.juejin.cn?target=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0634%2F%23id25**

https://www.python.org/dev/peps/pep-0635/#id15: **https://link.juejin.cn?target=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0635%2F%23id15**

https://www.python.org/dev/peps/pep-0636/: **https://link.juejin.cn?target=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0636%2F**

<img src="https://img-blog.csdnimg.cn/img_convert/b9a62ebaabbcd2f3d3523da939006138.png" alt="b9a62ebaabbcd2f3d3523da939006138.png">
