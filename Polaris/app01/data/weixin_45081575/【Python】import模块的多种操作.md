
--- 
title:  【Python】import模块的多种操作 
tags: []
categories: [] 

---
## 前言

记录一下关于Python在导入模块时候一些操作~

## 知识点📖📖

Python魔法方法：`__all__` Python内置模块：`importlib`

## 实现

### 指定导出的变量

当你在使用 `from xxx import *` 时候，可以通过 `__all__` 来指定可被导出的变量 虽然 `from xxx import *` 极其不优雅，但如果在编程中定义了许多变量的话，那导入还是令人头疼的

**项目组织如下：**

```
demo_package/
	__init__.py
	a.py
	b.py

```

**a.py**

```
def say_hi():
    print('hi')


def say_hello():
    print('hello')


# 只导出 say_hi 方法
__all__ = ['say_hi']

```

**b.py**

```
from a import *

say_hi()
say_hello()

```

**程序b.py** 执行如下所示：
- 如不指定导出的变量，是无法调用的。
<img src="https://img-blog.csdnimg.cn/60f7b09a2a784307a11c0b0665cf22a0.png" alt="在这里插入图片描述">

### 优雅的导包

在package里，如果有多个文件，这时候需要导入这些文件的变量， 可以通过在__init__.py 中里填写需要导入的变量，从而使得可以根据 package 名称导入变量，使得代码更加优雅

**项目组织如下：**

```
demo_package/
	__init__.py
	a.py
	b.py

```

**a.py**

```
def func_a():
    ....

```

**b.py**

```
def func_b():
    ....

```

__init__.py 填写以下内容

**__init__.py**

```
from .a import func_a
from .b import func_b

```

一般的导入是

```
from demo_package.a import func_a
from demo_package.b import func_b

```

而做了上述修改之后，导入这些变量的代码如下：

```
from demo_package import func_a
from demo_package import func_b

```

### 重新加载模块

在生产环境中，应该是用不上这个功能； 但如果是在调试时候，这个功能还是挺好用的。因为当你修改了你的代码后，可以通过重新加载模块就立即生效，而不用等待下一次执行再生效。

```
# 导入模块
import module

"""中间你对module 做了修改"""

# 重新导入模块
importlib.reload(module)

```

### 字符串导入模块

通过字符串来导入模块，这个功能我是找不到应用场景~ 只是觉得有趣，就记录一下！！

**通过字符串导入模块.py**

```
import importlib

module_name = importlib.import_module('module_name')

```

**简单示例.py**

```
import importlib


def create_func(_str: str):
    return importlib.import_module(_str)


func = create_func('math')
print(func.__name__)
print(func.sin(2))

```

**output：**

```
math
0.9092974268256817

```

## 后话

怎么样，用不上的知识又增加了吧！！ 本次分享到此结束，🐱‍🏍🐱‍🏍 see you~
