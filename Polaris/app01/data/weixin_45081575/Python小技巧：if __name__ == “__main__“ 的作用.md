
--- 
title:  Python小技巧：if __name__ == “__main__“ 的作用 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/835dce372cf24c1ab12045f756c4ebba.png#pic_center" alt="在这里插入图片描述">

## 前言

>  
 这里是**Python**小技巧的系列文章。这是第一篇，`if __name__ == "__main__" `的作用。 


在编写Python程序时候，总是习惯性的在文件的末尾添加这么一段代码。

```
if __name__ == "__main__":
    ...

```

至于它的作用是什么，先不管，能跑就行！

相信挺多小伙伴都是**知其然，而不知其所以然**的，下面来扒一下。

**结论先说在前头：**
- 当一个 `demo.py ` 文件作为独立的程序运行时候，那么 `__name__ `变量的值 为`__main__ `- 否则（如引用），`__name__ `变量的值就会设置为 `demo.py` 文件的名称，即`demo`。
感兴趣的小伙伴可以继续往下看~

## 知识点

|知识点|释义
|------
|**dir()**|**dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。**

## 剖析

>  
 `if __name__ == “__main__“:`，是个条件式语句。判断 `__name__` 这个变量是否等于 `__main__`。 


执行`dir()`，获取当前模块的变量名

```
print(dir())

```

结果如下：
- 这里没有定义任何变量，从而知道`__name__`是Python内置的一个属性。 <img src="https://img-blog.csdnimg.cn/32b4c8fc58d74d4ca6e45aeceb23a6ce.png" alt="在这里插入图片描述">
执行`__name__`，看看该变量的值

```
print(__name__)

```

结果如下：
- 变量`__name__` 的值为 `__main__` <img src="https://img-blog.csdnimg.cn/1210c2d02c7b4baeb66c312961d4467b.png" alt="在这里插入图片描述">
打印 `__name__`的文件为 `demo.py`，现在在`demo2.py`中导入 `demo.py`，

```
import demo

```

结果如下：
- 这里可以看到， `__name__`在被引用时候，它等于模块的名称。 <img src="https://img-blog.csdnimg.cn/64e6f739c4c34d20b7449d8fb03511b2.png" alt="在这里插入图片描述">
## 后话

本次分享到此结束！
