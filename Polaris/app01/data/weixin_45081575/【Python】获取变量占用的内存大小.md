
--- 
title:  【Python】获取变量占用的内存大小 
tags: []
categories: [] 

---
## 前言

>  
 记录一下，查看python运行当前范围内的变量、方法和定义的类型 会占用多少memory 


## 准备工作

>  
 借助内置模块 `sys`的 `getsizeof`即可。 


看到该函数的介绍，返回字对象的字节大小。

```
def getsizeof(p_object, default=None): # real signature unknown; restored from __doc__
    """
    getsizeof(object [, default]) -&gt; int
    
    Return the size of object in bytes.
    """
    return 0

```

使用起来也很简单，只需要将任意对象传到 `getsizeof `就可以了。

```
from sys import getsizeof as getsize
var = object()
print(getsize(var))

```

## 使用

**计算所占用内存，单位为 KB || MB**
- bytes转换为kb或mb- 这个方法只取两位小数
```
def binary_conversion(var: int):
    """
    二进制单位转换
    :param var: 需要计算的变量，bytes值
    :return: 单位转换后的变量，kb 或 mb
    """
    assert isinstance(var, int)
    if var &lt;= 1024:
        return f'占用 {<!-- -->round(var / 1024, 2)} KB内存'
    else:
        return f'占用 {<!-- -->round(var / (1024 ** 2), 2)} MB内存'

```

### 查看当前变量占用内存的大小

下面的方法是查看当前的运行环境所有的变量和方法所占用的内存。 可以从下图中看到多数内置的函数，占不到多少内容。

```

# 返回当前范围内的变量、方法和定义的类型列表
keys = dir()

for variable in keys:
    print(variable, binary_conversion(getsize(eval(variable))), '\n')

```

<img src="https://img-blog.csdnimg.cn/d2f0770e0d784888b3f9c028904b2858.png" alt="在这里插入图片描述">

### 生成器和列表你会怎么选？

一个装有0~1亿的生成器和列表，它们所占用的`memory` 如下图所示。
- 生成器占用的内存为` 0.1KB`- 列表占用的内存为 `762.94MB`
所以在针对这种情况时候，选择哪种迭代器应该了然于心了吧！

```
# 生成器
var_a = (_ for _ in range(100000000))
print(f'变量{<!-- -->"var_a"}, 类型为{<!-- -->type(var_a)}, 占用{<!-- -->binary_conversion(getsize(var_a))}')

# 列表
var_b = list(range(100000000))
print(f'变量{<!-- -->"var_b"}, 类型为{<!-- -->type(var_b)}, 占用{<!-- -->binary_conversion(getsize(var_b))}')


```

<img src="https://img-blog.csdnimg.cn/a1e5bd19929445ab915bdcee83cac116.png" alt="在这里插入图片描述">

## 后话

本文具体用处不大，但也记录一下。 本次到此结束，有问题请利用强大的搜索引擎，自行解决。
