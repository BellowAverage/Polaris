
--- 
title:  别再用print输出来调试Python代码了 
tags: []
categories: [] 

---
>  
  作者：changqing，腾讯互娱品质管理部Turing Lab研究员 
  公众号：腾讯技术工程 
 

导语：最近在github上冒出了一个python的debug神器PySnooper，号称在debug时可以消灭print。那么该工具有哪些优点呢，如何使用该工具呢。本文就介绍该工具的优缺点和使用方式。

#### 

**前言：**

使用python开发过程中，总是避免不了debug。传统的debug过程大致分为两种：

a) 断点+单步调试。

断点+单步调试估计是用的最多的了，对于较大型项目来说，其流程大致为：先在关键的代码位置加上print语句，通过分析print的值将范围缩小，这个过程可能需要重复多次，使用print的方法，一般可以将范围缩小到一个比较完整的功能模块中；然后在可能出现bug的模块中的关键部分打上断点，进入到断点后使用单步调试，查看各变量的值是否正确，最后根据错误的变量值定位到具体的代码行，最后进行修改。

b) pdb调试。

pdb是python自带的一个包，为 python 程序提供了一种交互的源代码调试功能，主要特性包括设置断点、单步调试、进入函数调试、查看当前代码、查看栈片段、动态改变变量的值等。pdb的调试流程和1）基本差不多，其具体的使用方法大家可以网上搜一下。

传统的debug的方法的缺点包括：

a)需要在代码中添加print语句，这就改变了原有的代码; 

b)在断点调试和单步调试过程中，需要保持持续的专注，一旦跳过了关键点就要从头开始。

最近在github上冒出了一个debug工具，可以解决传统debug过程中的缺点。下面一块来看看这个工具的使用和神奇之处。

**1. PySnooper是什么**

<img src="https://img-blog.csdnimg.cn/img_convert/d3689609d929e352fdcd5cd221802f15.jpeg" alt="d3689609d929e352fdcd5cd221802f15.jpeg">

该工具使用采用装饰器的形式，将函数的运行过程以日志的形式打印到文件中，其记录了运行了哪些代码行，运行的时间及运行到当前代码时各变量的值。根据变量的变化就可以定位问题了。亲自试用该工具后，其优点可总结为以下几点：

1、无需为了查看变量的值，使用print打印变量的值，从而修改了原有的代码。

2、接口的运行过程以日志的形式保存，方便随时查看。

3、可以根据需要，设置函数调用的函数的层数，方便将注意力集中在需要重点关注的代码段。

4、多个函数的日志，可以设置日志前缀表示进行标识，方便查看时过滤。

该工具有这么多优点，那么如何使用呢，下面结合demo来介绍该工具的使用。

**2. 使用方式介绍**

**1. 工具安装**

```
pip install pysnooper
```

**2. 官方demo介绍**

官方demo代码：

```
import pysnooper
@pysnooper.snoop()
def number_to_bits(number):
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]
number_to_bits(6)
```

 控制台输出：

<img src="https://img-blog.csdnimg.cn/img_convert/512c9da580700c03096422f71b543e1d.jpeg" alt="512c9da580700c03096422f71b543e1d.jpeg">

控制台的输出如上图，从图中可以看到，从进入到函数开始，会记录每一行代码的执行及记录新增局部变量或已有局部变量的变化，直到函数结束。以装饰器的形式使用该工具后，会将函数运行的中间结果打印出来，这样方便后续的bug定位和分析。

**3. 参数介绍**

以装饰器的形式使用该工具，其包含了四个参数，参数包括output, variables, depth, prefix，如下图。

<img src="https://img-blog.csdnimg.cn/img_convert/9e1895ed3b5aa4f77215c07c1c8055bb.jpeg" alt="9e1895ed3b5aa4f77215c07c1c8055bb.jpeg">

1、output参数。该参数指定函数运行过程中产生的中间结果的保存位置，若该值为空，则将中间结果输出到控制台。

2、variables参数。该参数是vector类型, 因为在默认情况下，装饰器只跟踪局部变量，要跟踪非局部变量，则可以通过该字段来指定。默认值为空vector。

3、depth参数。该参数表示需要追踪的函数调用的深度。在很多时候，我们在函数中会调用其他函数，通过该参数就可以指定跟踪调用函数的深度。默认值为1。

4、prefix参数。该参数用于指定该函数接口的中间结果前缀。当多个函数都使用的该装饰器后，会将这些函数调用的中间结果保存到一个文件中，此时就可以通过前缀过滤不同函数调用的中间结果。默认值为空字符串。

**3. 工具应用**

要使用该工具只需要理解该装饰器（snoop）的参数的含义，下面结合几个demo介绍参数的使用及对结果的影响。

**1. output 参数使用**

若使用默认参数，则将中间结果输出到控制台，若填写该参数，则将中间结果写入到该参数指定的目录下，如运行以下代码，其中间结果会保存在装饰器snoop中设置日志保存的路径中，注意这里不会自动创建目录，所以需要事先创建目录，如测试代码中填写路径后需要创建log目录。

测试代码：

```
import pysnooper


def add(num1, num2):
    return num1 + num2


@pysnooper.snoop("./log/debug.log", prefix="--*--")
def multiplication(num1, num2):
    sum_value = 0
    for i in range(0, num1):
        sum_value = add(sum_value, num2)
    return sum_value


value = multiplication(3, 4)
```

运行该代码后，在./log/debug.log的内容如下：

<img src="https://img-blog.csdnimg.cn/img_convert/32efecdc6e04fb9db65ad55a7c493aa9.jpeg" alt="32efecdc6e04fb9db65ad55a7c493aa9.jpeg">

从运行代码的中间结果中可以看出，文件中记录了各行代码的执行过程及局部变量的变化。在debug时，通过分析该文件，就可以跟踪每一步的执行过程及局部变量的变化，这样就能快速的定位问题所在；由于运行的中间结果保存在文件中，方便随时分析其运行的中间结果，也便于共享。

**2. variables参数使用**

在默认参数的情况下，使用该工具只能查看局变量的变化过程，当需要查看局部变量以外变量时，则可以通过variables参数进行设置，比如下方代码，在Foo类型，需要查看类实例的变量self.num1, self.num2, self.sum_value,则可以看将该变量设置当参数传入snoop的装饰器中。

测试代码：

```
import pysnooper


class Foo(object):
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.sum_value = 0


    def add(self, num1, num2):
        return num1 + num2
    @pysnooper.snoop(output="./log/debug.log", variables=("self.num1", "self.num2", "self.sum_value"))
    def multiplication(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        sum_value = 0
        for i in range(0, num1):
            sum_value = self.add(sum_value, num2)
        self.sum_value = sum_value
        return sum_value


foo = Foo()
foo.multiplication(3, 4)
```

为了体现该参数的作用，这里分别使用默认参数和上述参数（代码中设置的参数）运行代码，得到的结果如下：

<img src="https://img-blog.csdnimg.cn/img_convert/3b683247f61fe926c9f93dda6da55c40.jpeg" alt="3b683247f61fe926c9f93dda6da55c40.jpeg">

使用默认参数的结果

<img src="https://img-blog.csdnimg.cn/img_convert/02a9b36503fa3a43282ca85aee57ff1e.jpeg" alt="02a9b36503fa3a43282ca85aee57ff1e.jpeg">

使用代码中参数的结果

从两个中间结果中可以看出，若变量不是局部变量，哪怕在函数中使用了该变量，如果不显示设置打印该变量的中间结果，则不会将该变量的中间结果打印到文件中。

**3. depth参数使用**

该参数用来指定记录函数调用层数的结果，默认值为1，若要查看多层函数调用的中间结果，则可将该参数设置为&gt;=2。

测试代码：

```
import pysnooper


def add(num1, num2):
    return num1 + num2


@pysnooper.snoop("./log/debug.log", depth=2)
def multiplication(num1, num2):
    sum_value = 0
    for i in range(0, num1):
        sum_value = add(sum_value, num2)
    return sum_value


value = multiplication(3, 4)
```

为了对比，将depth的值分别设置为1和2，其结果如下：

<img src="https://img-blog.csdnimg.cn/img_convert/70f46a8f85f62abd65fb6177af07d4a7.jpeg" alt="70f46a8f85f62abd65fb6177af07d4a7.jpeg">

depth=1的结果

<img src="https://img-blog.csdnimg.cn/img_convert/4cf24cbccba9ba1c854b336c8413ffec.jpeg" alt="4cf24cbccba9ba1c854b336c8413ffec.jpeg">

depth=2的结果

从上述结果中可以看出，若要查看更深层次函数调用的情况，则可以通过设置depth值进行查看。这样方便用户有选择性的查看函数的调用情况。

**4. prefix参数使用**

该参数主要用于设置中间结果的前缀，这样就可以区分不同的函数调用的中间结果，默认参数为""。

测试代码：

```
import pysnooper


def add(num1, num2):
    return num1 + num2


@pysnooper.snoop("./log/debug.log", prefix="--*--")
def multiplication(num1, num2):
    sum_value = 0
    for i in range(0, num1):
        sum_value = add(sum_value, num2)
    return sum_value


value = multiplication(3, 4)
```

运行代码后的中间结果如下：

<img src="https://img-blog.csdnimg.cn/img_convert/1a4f0ea224a1beb5fababba0193a1cb1.jpeg" alt="1a4f0ea224a1beb5fababba0193a1cb1.jpeg">

从结果中可以看到，中间结果的每一行都包含了prefix设置的前缀，这样便于区分不同的函数调用的中间结果。

上述的介绍为了将注意力集中到具体的参数，采取设置单一参数的形式进行介绍（output+其他单个参数）。在实际使用时，可以同时设置多个参数。使用PySnooper工具来记录函数运行的中间结果，比起传统的使用断点+单步调试，pdb等调试方法，PySnooper工具有着巨大的优势。

**4. 该工具的不足之处**

虽然使用debug在使用PySnooper很方便，但还是存在一些问题（以4月26号拉取代码为依据），比如：

1、无法很好的支持递归调用。

2、调用每个函数的中间结果只能保存在一个文件中，如果需要区分不同文件的结果，需要使用prefix来进行前缀标识。

3、对于跨文件函数调用，不支持记录调用函数所在的文件名。

当然PySnooper是最近在github上火起来的项目，还不够完善是正常的，相信这些不足之处后续也会得到完善，期待一个更好的PySnooper。

**5. 总结**

本文介绍PpySnooper的工具，先介绍了该工具是什么，相比传统debug方法的优势，然后介绍了该工具的参数及说明该参数作用的demo。最后介绍了该工具的不足之处。
- - - - - 