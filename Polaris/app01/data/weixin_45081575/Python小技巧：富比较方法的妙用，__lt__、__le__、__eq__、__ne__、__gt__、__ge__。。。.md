
--- 
title:  Python小技巧：富比较方法的妙用，__lt__、__le__、__eq__、__ne__、__gt__、__ge__。。。 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/c880a02d0a40482e8725961c1374b574.jpeg#pic_center" alt="在这里插入图片描述">

## 前言

>  
 这里是**Python**小技巧的系列文章。这是第二篇，`富比较`方法的妙用。 


在 **Python**中，富比较方法共`6`个，如下表所示：
- 见名知意，富比较主要用于比较。
|富比较方法|使用|释义|释义
|------
|`object.__lt__(self, other)`|`x.__lt__(y)`|x&lt;y|less than
|`object.__le__(self, other)`|`x.__le__(y)`|x&lt;=y|less and equal
|`object.__eq__(self, other)`|`x.__eq__(y)`|x==y|equal
|`object.__ne__(self, other)`|`x.__ne__(y)`|x!=y|not equal
|`object.__gt__(self, other)`|`x.__gt__(y)`|x&gt;y|greater than
|`object.__ge__(self, other)`|`x.__ge__(y)`|x&gt;=y|greater and equal

众所周知（**`我猜你大概率不知！`**），**Python**中两个字符串进行比较时候会是按照两个字符串的 **Unicode** 码位级别进行比较，而不是按照它们的长度来进行比较。如果想要根据它们的长度来进行比较，该如何实现？

带着这个疑问，下面将以 `object.__lt__(self, other)` 来展开说明它们的作用， 以及重写富比较方法，使得它们更加贴切我们的代码逻辑。

## 知识点📖📖

>  
 富比较方法是类的内置方法，一般时候用不到，除非我们去改写它！ 


**富比较方法** ：

**字符串比较**：

如下，**Nothing**是个什么都没有实现的类。

```
"""demo.py"""

class Nothing:
    ...

print(dir(Nothing))

```

打印查看当前类的所有属性，可以看到包含了上面的6个富比较方法。可见他们是类的内置方法。 <img src="https://img-blog.csdnimg.cn/eaad683692b0408b99d3f83379b8b542.png" alt="在这里插入图片描述">

## 剖析

### 正常运行

>  
 `str.__lt__(self, other)`返回的是一个布尔值。 


运行以下代码，结果打印 `True`

```
variable: str = 'hello world'
print(variable.__lt__('yes'))	# True

```

**variable**在这里是字符串，`str`是**Python**的内置类， 跟 `str.__lt__` 过去可以看到，该富比较方法返回 `self &lt; value`，即比较自身和其他值，返回布尔值。

```
def __lt__(self, *args, **kwargs): # real signature unknown
    """ Return self&lt;value. """
    pass

```

在这里，`variable &lt; 'yes'` 和 `variable.__lt__('yes')`，这两句代码的意思是一致的。

### 如何重写

>  
 带着上面的疑问，这里将`str.__lt__`改写为按照长度比较。 


以下代码执行后，打印的结果是 **False**，这说明我们改写这个富比较方法成功了。
- `len('hello world')`长度为11，`len('yes')`长度为3，`11&lt;3`，为**False**
```
"""demo.py"""


class Str(str):
    def __lt__(self, other):
        return len(self) &lt; len(other)


variable: Str = Str('hello world')
print(variable.__lt__('yes'))	# False

```

### 完善重写

>  
 在与其它类型的对象进行比较时候，会抛出**TypeError** 异常。 


将上面代码中的最后一行替换为 `print(variable.__lt__(1))`， 运行后抛出**TypeError**，如下图所示：

<img src="https://img-blog.csdnimg.cn/3d4c44fae8364e59b6cec3cd45269b85.png" alt="在这里插入图片描述">

添加一个判断： 如果参与比较的对象类型不是字符串类型，则返回一个 **NotImplemented**
- **NotImplemented**是**Python**内部常量，用于表明运算没有针对其他类型的实现。
```
class Str(str):
    def __lt__(self, other):
        if isinstance(other, str):
            return len(self) &lt; len(other)
        return NotImplemented


variable: Str = Str('hello world')
print(variable.__lt__(1))	# NotImplemented


```

## 后话

本次介绍及重写了富比较方法中的 `object.__lt__(self, other)`，对于其它富比较方法的重写，方法是完全一致的。本文当是抛砖引玉，为各位提供一点思路~

本次分享到此结束！🐱‍🏍🐱‍🏍
