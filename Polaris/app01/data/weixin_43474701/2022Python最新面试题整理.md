
--- 
title:  2022Python最新面试题整理 
tags: []
categories: [] 

---
秋招将至，给准备跳槽找工作的准备一份面试指南，希望大家在涨薪和成长的路上多一点指引！

**<font color="#FF5809" face="FZShuTi">1、请列出 5 个 python 标准库？</font>** os：提供了不少与操作系统相关联的函数 sys: 通常用于命令行参数 re: 正则匹配 math: 数学运算 datetime:处理日期时间

**<font color="#FF5809" face="FZShuTi">2、python2和python3区别？</font>** Python3 使用 print 必须要以小括号包裹打印内容，比如 print(‘hi’)

Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比如 print ‘hi’

Python2 range(1,10)返回列表，python3中返回迭代器，节约内存

Python2 中使用 ascii 编码，python中使用 utf-8 编码

Python2 中 unicode 表示字符串序列，str 表示字节序列

Python3 中 str 表示字符串序列，byte 表示字节序列

Python2 中为正常显示中文，引入 coding 声明，python3 中不需要

Python2 中是 raw_input() 函数，python3 中是input()函数 <font color="#FF5809" face="FZShuTi">3、Python 中os和sys模块的作用分别是？</font> os模块：负责程序与操作系统的交互，提供了访问操作系统底层的接口。sys模块：负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python的运行时环境。 <font color="#FF5809" face="FZShuTi">4、请阐述在Python中split()，sub()，subn()的功能分别是什么？</font> split()： 使用正则表达式模式将给定字符串“拆分”到列表中。

sub()： 查找正则表达式模式匹配的所有子字符串，然后用不同的字符串替换它们

subn()： 它类似于sub()，并且还返回新字符串。 <font color="#FF5809" face="FZShuTi">5、解释 Python 中的可变类型和不可变类型？</font> 1.Python中的可变类型有list,dict；不可变类型有string，number,tuple.

2.当进行修改操作时，可变类型传递的是内存中的地址，也就是说，直接修改内存中的值，并没有开辟新的内存。

3.不可变类型被改变时，并没有改变原内存地址中的值，而是开辟一块新的内存，将原地址中的值复制过去，对这块新开辟的内存中的值进行操作。 <font color="#FF5809" face="FZShuTi">6、Python 中类方法、类实例方法、静态方法有何区别？</font> 类方法: 是类对象的方法，在定义时需要在上方使用 @classmethod 进行装饰,形参为cls，表示类对象，类对象和实例对象都可调用

类实例方法: 是类实例化对象的方法,只能由实例对象调用，形参为self,指代对象本身;

静态方法: 是一个任意函数，在其上方使用 @staticmethod 进行装饰，实例对象和类对象都可以调用。但是方法体中不能使用类或实例的任何属性和方法。 <font color="#FF5809" face="FZShuTi">7、请阐述同步，异步，阻塞，非阻塞的概念？</font> 同步： 多个任务之间有先后顺序执行，一个执行完下个才能执行。

异步： 多个任务之间没有先后顺序，可以同时执行，有时候一个任务可能要在必要的时候获取另一个同时执行的任务的结果，这个就叫回调！

阻塞： 如果卡住了调用者，调用者不能继续往下执行，就是说调用者阻塞了。

非阻塞： 如果不会卡住，可以继续执行，就是说非阻塞的。

同步异步相对于多任务而言，阻塞非阻塞相对于代码执行而言。 <font color="#FF5809" face="FZShuTi">8、Python代码中_args, *_kwargs 含义及用法？</font> args： arguments 的缩写，表示位置参数

kwargs： keyword arguments 的缩写，表示关键字参数 <font color="#FF5809" face="FZShuTi">9、Python赋值、浅拷贝和深拷贝的区别？</font> Python 有 3 种赋值方式：直接赋值、浅拷贝、深拷贝；

直接赋值：就是对象的引用。（相当于给原来的对象起个别名），比如有个人叫张三，外号叫小张，对象的引用就是类似，虽然换个名字，但是两个名字指的是同一个人。

浅拷贝，拷贝的是父对象，不会拷贝到内部的子对象。（单从浅字就可以看出拷贝的东西不深，可以理解为只拷贝一层） { 1、完全切片方法；2、工厂函数，如 list()；3、copy 模块的 copy()函数 }

深拷贝，包含对象里面的自对象的拷贝（可以理解为克隆，全拷贝过去但是两者没有任何关系了，各自是各自的）；所以原始对象的改变不会造成深拷贝里任何子元素的改变 { copy 模块的 deep.deepcopy()函数 } <font color="#FF5809" face="FZShuTi">10、合并两个列表并去除重复元素？</font>

```

list1 = ['b','c','c','a','f','r','y','e','e']
list2 = ['t','y','x','y','z','e','f']
def merge_list(*args):
    s = set()
    for i in args:
        s = s.union(i)
    print(s)
    return s

merge_list(list1,list2)

```

<font color="#FF5809" face="FZShuTi">11、如何查询和替换一个文本中的字符串?</font>

```

tempstr = "hello python,you,me,world"
print(tempstr.replace("hello","python"))

#还可以使用正则,有个sub()
tempstr = "hello python,you,me,world"
import re
rex = r'(hello|Use)'
print(re.sub(rex,"HELLO",tempstr))

```

<font color="#FF5809" face="FZShuTi">12、Python中的列表和元组有什么区别？</font> list 是可变的对象，元组 tuple 是不可变的对象。也就是说列表中的元素可以进行任意修改，而元组中的元素无法修改。 <font color="#FF5809" face="FZShuTi">12、Python数组和列表有什么区别？</font> Python中的数组和列表具有相同的存储数据方式。但是，数组只能包含单个数据类型元素，而列表可以包含任何数据类型元素。 <font color="#FF5809" face="FZShuTi">13、Python中append和extend的区别？</font> append() 向列表尾部追加一个新元素，列表只占一个索引位，在原有列表上增加

extend() 向列表尾部追加一个列表，将列表中的每个元素都追加进来，在原有列表上增加 <font color="#FF5809" face="FZShuTi">14、Python中==和is的区别</font> is用于判断两个变量引用对象是否为同一个，==用于判断引用变量的值是否相等。 <font color="#FF5809" face="FZShuTi">15、区分下break，continue和pass？</font> break：跳出循环，不执行下一个循环。同时break后面的代码也不会执行。

pass：pass后面的代码还是会继续执行，也就是当前的循环还在继续。

continue：continue后面的代码不会执行，而是直接进入下一个循环。 <font color="#FF5809" face="FZShuTi">16、Python中的局部变量和全局变量是什么？</font> 全局变量：在函数外或全局空间中声明的变量称为全局变量。这些变量可以由程序中的任何函数访问。

局部变量：在函数内声明的任何变量都称为局部变量。此变量存在于局部空间中，而不是全局空间中。 <font color="#FF5809" face="FZShuTi">17、python中range＆xrange有什么区别？</font> 在大多数情况下，xrange和range在功能方面完全相同。

它们都提供了一种生成整数列表的方法，唯一的区别是range返回一个Python列表对象，x range返回一个xrange对象。这就表示xrange实际上在运行时并不是生成静态列表。

它使用称为yielding的特殊技术根据需要创建值。该技术与一种称为生成器的对象一起使用。因此如果你有一个非常巨大的列表，那么就要考虑xrange。

<font color="#FF5809" face="FZShuTi">18、python装饰器是什么？</font> 装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。 它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。 <font color="#FF5809" face="FZShuTi">19、说一下python迭代器和生成器？</font> 介绍python生成器需要先介绍可迭代对象和迭代器。

可迭代对象（Iterable Object），简单的来理解就是可以使用 for 来循环遍历的对象。比如常见的 list、set和dict。

可迭代对象具有__iter__ 方法，用于返回一个迭代器，或者定义了 getitem 方法，可以按 index 索引的对象（并且能够在没有值时抛出一个 IndexError 异常），因此，可迭代对象就是能够通过它得到一个迭代器的对象。所以，可迭代对象都可以通过调用内建的 iter() 方法返回一个迭代器。

生成器其实是一种特殊的迭代器，不过这种迭代器更加优雅。它不需要再像上面的类一样写__iter__()和__next__()方法了，只需要一个yiled关键字。

<font color="#FF5809" face="FZShuTi">20、函数__new__和__init__的区别是什么？</font> 实际开发中__new__函数很少用到，关于__new__函数，你需要知道： **new__是静态函数,而__init__是一个实例函数. <strong>new__函数会返回一个创建的实例,而__init__什么都不返回. 只有在__new__返回一个cls的实例时后面的__init__才能被调用. 当创建一个新实例时调用__new**,初始化一个实例时用__init</strong>. 另外，**metaclass__是创建类时起作用.所以我们可以分别使用__metaclass**、__new__和__init__分别在类创建、实例创建和实例初始化的时候实现一些定制的特殊操作. <font color="#FF5809" face="FZShuTi">21、Python的主要功能是什么？</font> Python是一种解释型语言。与C语言等语言不同，Python不需要在运行之前进行编译。

Python是动态语言，当您声明变量或类似变量时，您不需要声明变量的类型。

Python适合面向对象的编程，因为它允许类的定义以及组合和继承。Python没有访问说明（如C ++的public，private）。

在Python中，函数是第一类对象。它们可以分配给变量。类也是第一类对象

编写Python代码很快，但运行比较慢。Python允许基于C的扩展，例如numpy函数库。

Python可用于许多领域。Web应用程序开发，自动化，数学建模，大数据应用程序等等。它也经常被用作“胶水”代码。 <font color="#FF5809" face="FZShuTi">22、如何在Python中管理内存？</font> python中的内存管理由Python私有堆空间管理。所有Python对象和数据结构都位于私有堆中。程序员无权访问此私有堆。python解释器负责处理这个问题。

Python对象的堆空间分配由Python的内存管理器完成。核心API提供了一些程序员编写代码的工具。

Python还有一个内置的垃圾收集器，它可以回收所有未使用的内存，并使其可用于堆空间。 <font color="#FF5809" face="FZShuTi">23、什么是python模块？Python中有哪些常用的内置模块？</font> Python模块是包含Python代码的.py文件。此代码可以是函数类或变量。一些常用的内置模块包括：sys、math、random、data time、JSON。 <font color="#FF5809" face="FZShuTi">24、python是否区分大小写？</font> 是。Python是一种区分大小写的语言。 <font color="#FF5809" face="FZShuTi">25、什么是Python中的类型转换？</font> 类型转换是指将一种数据类型转换为另一种数据类型。

int（）  - 将任何数据类型转换为整数类型

float（）  - 将任何数据类型转换为float类型

ord（）  - 将字符转换为整数

hex（） - 将整数转换为十六进制

oct（）  - 将整数转换为八进制

tuple（） - 此函数用于转换为元组。

set（） - 此函数在转换为set后返回类型。

list（） - 此函数用于将任何数据类型转换为列表类型。

dict（） - 此函数用于将顺序元组（键，值）转换为字典。

str（） - 用于将整数转换为字符串。

complex（real，imag）  - 此函数将实数转换为复数（实数，图像）数。 <font color="#FF5809" face="FZShuTi">26、python中是否需要缩进？</font> 缩进是Python必需的。它指定了一个代码块。循环，类，函数等中的所有代码都在缩进块中指定。通常使用四个空格字符来完成。如果您的代码没有必要缩进，它将无法准确执行并且也会抛出错误。

<font color="#FF5809" face="FZShuTi">27、Python中的函数是什么？</font> 函数是一个代码块，只有在被调用时才会执行。要在Python中定义函数，需要使用def关键字。 <font color="#FF5809" face="FZShuTi">28、什么是__init__?</font> __init__是Python中的方法或者结构。在创建类的新对象/实例时，将自动调用此方法来分配内存。所有类都有__init__方法。 <font color="#FF5809" face="FZShuTi">29、什么是lambda函数？</font> lambda函数也叫匿名函数，该函数可以包含任意数量的参数，但只能有一个执行操作的语句。 <font color="#FF5809" face="FZShuTi">30、Python中的self是什么？</font> self是类的实例或对象。在Python中，self包含在第一个参数中。但是，Java中的情况并非如此，它是可选的。它有助于区分具有局部变量的类的方法和属性。init方法中的self变量引用新创建的对象，而在其他方法中，它引用其方法被调用的对象。 <font color="#FF5809" face="FZShuTi">31、[:: - 1}表示什么？</font> [:: - 1]用于反转数组或序列的顺序。 <font color="#FF5809" face="FZShuTi">32、range＆xrange有什么区别？</font> 在大多数情况下，xrange和range在功能方面完全相同。它们都提供了一种生成整数列表的方法，唯一的区别是range返回一个Python列表对象，x range返回一个xrange对象。这就表示xrange实际上在运行时并不是生成静态列表。它使用称为yielding的特殊技术根据需要创建值。该技术与一种称为生成器的对象一起使用。因此如果你有一个非常巨大的列表，那么就要考虑xrange。 <font color="#FF5809" face="FZShuTi">33、如何在python中写注释？</font> Python中的注释以＃字符开头。也可以使用doc-strings（三重引号中包含的字符串）进行注释。
