
--- 
title:  20道常考Python面试题大总结！ 
tags: []
categories: [] 

---
**关于Python的面试经验**

一般来说，**面试官会根据求职者在简历中填写的技术及相关细节来出面试题。** 一位拿了大厂技术岗Special Offer的网友分享了他总结的面试经验。当时，面试官根据他在简历中所写的技术，面试题出的范围大致如下：

**·** 数据类型有几种、有什么区别

**·** 进程、线程、协程的定义及区别

**·** 深浅拷贝的区别

**·** 常用开发模式

**·** 函数式编程、对象式编程

**·** 闭包、装饰器

**·** 垃圾回收机制

**·** linux常用命令，举例说明

根据该网友的经验，以上是面试题的常考范围，如果能答出来大部分内容，说明技术水平基本没太大问题。**建议每个问题至少答三点，同时注意观察面试官的反应**，如果觉得面试官感兴趣的话可以多说一些，不感兴趣的话则可适当地少说。**平均每个问题回答控制在3-5分钟比较合适。**

**技术问题一般会问15个左右，一轮面试的时长基本在一小时以上。** 一小时以下的面试成功希望可能会小一些。所以，建议大家在技术基础方面一定要准备充分、多下功夫。

**20道常考Python面试题**

我们为大家精心奉上Python面试宝典中最常考的20道面试题。看看你都会做么？

**1、如何在Python中管理内存？**

Python中的内存管理由Python私有堆空间管理。对象和数据结构位于私有堆中，开发者无权访问此私有堆，是Python解释器负责处理的。Python对象的堆空间分配由内存管理器完成。核心API提供了一些开发者编写代码的工具。Python内置的垃圾回收器会回收使用所有的未使用内存，使其适用于堆空间。

**2、解释Python中的Help()函数和Dir()函数。**

Help()函数是一个内置函数，作用是查看函数和详细说明模块用途。

<img src="https://img-blog.csdnimg.cn/img_convert/4194db3888c004deda355f483f62d776.png" alt="">

运行结果是：

<img src="https://img-blog.csdnimg.cn/img_convert/901125eed7c381ce1690623af1581b5b.png" alt="">

Dir()函数是Python内置函数，Dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。

举个例子展示其使用方法：

<img src="https://img-blog.csdnimg.cn/img_convert/dfcda52803624d2e4faea48d6ccd8fd5.png" alt="">

运行结果是：

<img src="https://img-blog.csdnimg.cn/img_convert/ebdc8228cc97377741043041c224edac.png" alt="">

**3、当Python退出时，是否会清除所有分配的内存？**

答案是否。当Python退出时，对其他对象具有循环引用的Python模块，以及从全局名称空间引用的对象不会被解除分配或释放。无法解除分配C库保留的那些内存部分。退出时，由于拥有自己的高效清理机制，Python会尝试取消分配/销毁其他所有对象。

**4、什么是猴子补丁？**

在运行期间动态修改一个类或模块。

<img src="https://img-blog.csdnimg.cn/img_convert/69d0d3c537ffe0a3c10a2d3de6c8ecbf.png" alt="">

运行结果是：

<img src="https://img-blog.csdnimg.cn/img_convert/c62d0e16d6125ad060e555ac02146a89.png" alt="">

**5、Python中的字典是什么？**

字典指的是Python中的内置数据类型。它定义了键和值之间的一对一关系，包含了一对键及其对应的值。字典由键索引。

**6、解释一下Python中的逻辑运算符。**

Python中有3个逻辑运算符：and，or，not。

**7、为什么不建议以下划线作为标识符的开头？**

Python没有私有变量的概念，所以约定速成以下划线为开头来声明一个变量为私有。如果不想让变量私有，则不要使用下划线开头。

**8、什么是Flask？**

Flask是Python编写的一款轻量级Web应用框架。WSGI 工具箱采用 Werkzeug ，模板引擎使用 Jinja2。Flask使用 BSD 授权。Werkzeug和Jinja2是其中的两个环境依赖。Flask不需要依赖外部库。

**9、解释Python中的join()和split()函数。**

Join()可用于将指定字符添加至字符串中。

<img src="https://img-blog.csdnimg.cn/img_convert/31e6b574302b56e2d7ea0c6b5758402a.png" alt="">

运行结果是：

<img src="https://img-blog.csdnimg.cn/img_convert/f0322da4507b96704e6c96a9104312b8.png" alt="">

Split()可用于指定字符分割字符串。

<img src="https://img-blog.csdnimg.cn/img_convert/b8f0ff586a65da3d7c48eb14cc15e614.png" alt="">

运行结果是：

<img src="https://img-blog.csdnimg.cn/img_convert/bfdde58b42c6d00cc95346e87a9cd5b3.png" alt="">

**10、Python中的标识符长度有多长？**

标识符可以是任意长度。在命名标识符时还必须遵守以下规则：

**·** 只能以下划线或者 A-Z/a-z 中的字母开头 **·** 其余部分可以使用 A-Z/a-z/0-9 **·** 区分大小写 **·** 关键字不能作为标识符

**11、Python中是否需要缩进？**

需要。Python指定了一个代码块。循环，类，函数等中的所有代码都在缩进块中指定。通常使用四个空格字符来完成。如果开发者的代码没有缩进，Python将无法准确执行并且也会抛出错误。

**12、请解释使用*args的含义。**

当我们不知道向函数传递多少参数时，比如我们向传递一个列表或元组，我们就使用*args。

<img src="https://img-blog.csdnimg.cn/img_convert/8db6a804639dca3d46f8cb41945b2793.png" alt="">

运行结果是：

<img src="https://img-blog.csdnimg.cn/img_convert/253f80d92a69fb77af08396cd96322d1.png" alt="">

**13、深拷贝和浅拷贝之间的区别是什么？**

浅拷贝是将一个对象的引用拷贝到另一个对象上，如果在拷贝中改动，会影响到原对象。深拷贝是将一个对象拷贝到另一个对象中，如果对一个对象的拷贝做出改变时，不会影响原对象。

**14、Python中如何实现多线程？**

Python是多线程语言，其内置有多线程工具包。多线程能让我们一次执行多个线程。Python中的GIL（全局解释器锁）确保一次执行单个线程。一个线程保存GIL并在将其传递给下个线程之前执行一些操作，看上去像并行运行的错觉。事实上是线程在CPU上轮流运行。所有的传递会增加程序执行的内存压力。

**15、Python中的闭包是什么？**

当一个嵌套函数在其外部区域引用了一个值时，该嵌套函数就是一个闭包。其意义就是会记录这个值。

比如：

<img src="https://img-blog.csdnimg.cn/img_convert/640f560eb2b4c457bcd122bf80194421.png" alt="">

运行结果是：

<img src="https://img-blog.csdnimg.cn/img_convert/692352148f49b3b34b2def1e78bc2a6e.png" alt="">

**16、Python的优势有哪些？**

**·** Python 易于学习

**·** 完全支持面向对象

**·** 高效的高级数据结构，可用少量代码构建出多种功能

**·** 拥有最成熟的程序包资源库之一

**·** 跨平台而且开源

**17、什么是元组的解封装？**

首先，我们先展示解封装：

<img src="https://img-blog.csdnimg.cn/img_convert/682d91c8a4096cd8deff303a7dd3ff74.png" alt="">

将 3，4，5 封装到元组 mytuple 中，再将值解封装到变量 x，y，z 中：

<img src="https://img-blog.csdnimg.cn/img_convert/9a8dcb04f70307ac71e259e0a2e720a7.png" alt="">

得到结果为12。

**18、什么是PEP？**

PEP代表Python Enhancement Proposal，是一组规则，指定如何格式化Python代码以获得最大可读性。

**19、列表和元组之间的区别是什么？**

主要区别是列表是可变的，元组是不可变的。比如以下举例：

<img src="https://img-blog.csdnimg.cn/img_convert/fdd8f0d42b215dcec4390071ad77bdf9.png" alt="">

会出现以下报错：

<img src="https://img-blog.csdnimg.cn/img_convert/bbd66da4479833a0bbb4f9e9a7a3dbdb.png" alt="">

**20、什么是Python模块？Python中有哪些常用的内置模块？**

Python模块是包含Python代码的.py文件。此代码可以是函数类或变量。常用的内置模块包括：random、data time、JSON、sys、math等。

## 关于Python学习指南

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后给大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、自动化办公等学习教程。带你从零基础系统性的学好Python！</mark>

#### 👉Python所有方向的学习路线👈

Python所有方向路线就是把Python常用的技术点做整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取）**</mark>

<img src="https://img-blog.csdnimg.cn/3c4ee87941694f3789398db3d52a2637.png#pic_center" alt="在这里插入图片描述">

#### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。

<img src="https://img-blog.csdnimg.cn/64c89bf6293d4699bf7ee8f34b9e69fd.png#pic_center" alt="在这里插入图片描述">

#### <mark>温馨提示：篇幅有限，已打包文件夹，获取方式在：文末</mark>

#### 👉Python70个实战练手案例&amp;源码👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/2017b67544f94e8898db755e2703224a.png#pic_center" alt="在这里插入图片描述">

#### 👉Python大厂面试资料👈

我们学习Python必然是为了找到高薪的工作，下面这些面试题是来自**阿里、腾讯、字节等一线互联网大厂**最新的面试资料，并且有阿里大佬给出了权威的解答，刷完这一套面试资料相信大家都能找到满意的工作。

<img src="https://img-blog.csdnimg.cn/3055c54d3224495987c589f150324d73.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/b0751719fe914aec8c8d09f62f772e44.png#pic_center" alt="在这里插入图片描述">

#### 👉Python副业兼职路线&amp;方法👈

学好 Python 不论是就业还是做副业赚钱都不错，但要学会兼职接单还是要有一个学习规划。

<img src="https://img-blog.csdnimg.cn/01bcd7cbfd6d43fb85ef410766735154.png#pic_center" alt="在这里插入图片描述">

**👉** **这份完整版的Python全套学习资料已经上传，朋友们如果需要可以扫描下方CSDN官方认证二维码或者点击链接免费领取**【**`保证100%免费`**】

<font color="red">**点击免费领取《CSDN大礼包》： 安全链接免费领取**</font>
