
--- 
title:  Python小技巧：__str__()的妙用 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/1a2cf18dddd3424693f5281ebb1d01fa.jpeg#pic_center" alt="在这里插入图片描述">

## 前言

>  
 这里是**Python**小技巧的系列文章。这是第三篇，`object.__str__(self)`方法的妙用。 


书接上回，这次还是介绍Python类的内置方法，`__str__()`

据官方文档的介绍，在使用 `str(object) 、format() 和 print() `的时候会调用`__str__() `方法，该方法会将实例转换为字符串，返回值为 **字符串** 对象。 如果`__str__()`没有被定义，就会调用 `object.__repr__()`。

实现 **str** 方法来定制一个类的实例的字符串表示。

## 知识点📖📖

`object.__str__(self)`： `object.__repr__(self)`：

关于`__repr__()`，基本用不上。建议查看官方文档，粗略了解即可。

先来看一组简单的代码（这个类没有实现任何功能

```
"""demo.py"""


class Nothing:
    ...


if __name__ == "__main__":
    print(Nothing())	# &lt;__main__.Nothing object at 0x000002C2CFD06650&gt; 0x2c2cfd06650

```

默认的打印结果是当前类的实例的名称和内存地址，如下图所示（不夸张地说，这个类实例的打印可以说是毫无用处！！！

<img src="https://img-blog.csdnimg.cn/4277e01d61044061a38189c2f7bbe789.png" alt="在这里插入图片描述">

## 剖析

在代码复杂的情况下，再打印默认的类实例，那就显得太鸡肋了。 这个时候我们就需要重写 `__str__()`方法了，使得它更加人性化。

再来看一组复杂点的代码

```
"""demo.py"""


class Nothing:
    name = 'frica'
    age = 20

    def __str__(self):
        return f'Nothing(name={<!-- -->self.name}, age={<!-- -->self.age})'


if __name__ == "__main__":
    print(Nothing())

```

代码执行效果如下：

<img src="https://img-blog.csdnimg.cn/fee1b3bfc64c403f8aa54e0f9bc33bac.png" alt="在这里插入图片描述">

重写 `__str__()` 后与 默认打印的类实例对比如下图所示：
- 孰优孰劣一目了然
<img src="https://img-blog.csdnimg.cn/a6c46afc72e8414b9e2f5eb8ff30fb31.png" alt="在这里插入图片描述">

## 后话

本次介绍及重写了 `__str__()`，在重写之后，可以更为方便且准确的描述信息类实例的信息，这对于我们的编程工作是有帮助的。

本次分享到此结束！🐱‍🏍🐱‍🏍
