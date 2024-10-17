
--- 
title:  Python 基础（十四）： 错误和异常 
tags: []
categories: [] 

---


#### 目录
- <ul><li>- - <ul><li>- - - 


程序中的错误我们通常称为 bug ，工作中我们不仅需要改自己程序中的 bug ，还需要改别人程序中的 bug ，新项目有 bug 要改，老项目也有 bug 要改，可以说 bug 几乎贯穿一个程序员的职业生涯… 我们通常将 bug 分为 Error（错误） 和 Exception（异常），我们下面来具体学习下 Python 中的 错误 和 异常。

### 1 错误

错误 通常是指程序中的 语法错误 或 逻辑错误，来通过两个 Python 例子看一下：

**语法错误示例**

```
# print前面少了 : 
if True
    print("hello python")

```

我们编写程序通常使用开发工具编写，比如：我使用 Pycharm 工具编写 Python 程序，像这种语法错误，在编写程序时，编译器就会检测出来并提示我们，因此，我们编写好的程序几乎不会出现这种问题。

**逻辑错误示例**

```
# 0 是不能作为被除数的
a  = 5
b = 0
print(a/b)

#执行结果：ZeroDivisionError: division by zero

```

逻辑错误编译器是不会提示我们的，因此，我们编写程序时，对一些基本常识要有一定了解，从而，避免出现逻辑错误。

### 2 异常

即便 Python 程序的语法是正确的，在运行它的时候，也有可能发生错误，运行期检测到的错误被称为异常；大多数的异常都不会被程序处理，都以错误信息的形式展现。

#### 2.1 内置异常

我们先来看一下异常层次结构：

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning

```

通过上面的异常层次结构，我们可以清晰的看出，BaseException为所有异常的基类，其下面分为：SystemExit、KeyboardInterrupt、GeneratorExit、Exception 四类异常，Exception 为所有非系统退出类异常的基类，Python 提倡继承 Exception 或其子类派生新的异常；Exception 下包含我们常见的多种异常如：MemoryError（内存溢出）、BlockingIOError（IO异常）、SyntaxError（语法错误异常）… 详细说明可以查看下面列表：
| 异常名称| 描述

| BaseException| 所有异常的基类
| SystemExit|解释器请求退出
| KeyboardInterrupt| 用户中断执行(通常是输入^C)
| Exception|常规错误的基类
| StopIteration |迭代器没有更多的值
| GeneratorExit |生成器(generator)发生异常来通知退出
| StandardError| 所有的内建标准异常的基类
| ArithmeticError |所有数值计算错误的基类
| FloatingPointError |浮点计算错误
| OverflowError| 数值运算超出最大限制
| ZeroDivisionError| 除(或取模)零 (所有数据类型)
| AssertionError| 断言语句失败
| AttributeError| 对象没有这个属性
| EOFError |没有内建输入,到达EOF 标记
| EnvironmentError |操作系统错误的基类
| IOError |输入/输出操作失败
| OSError |操作系统错误
| WindowsError| 系统调用失败
| ImportError |导入模块/对象失败
| LookupError |无效数据查询的基类
| IndexError| 序列中没有此索引(index)
| KeyError| 映射中没有这个键
| MemoryError| 内存溢出错误(对于Python 解释器不是致命的)
| NameError| 未声明/初始化对象 (没有属性)
| UnboundLocalError |访问未初始化的本地变量
| ReferenceError| 弱引用(Weak reference)试图访问已经垃圾回收了的对象
| RuntimeError |一般的运行时错误
| NotImplementedError| 尚未实现的方法
| SyntaxError|Python 语法错误
| IndentationError| 缩进错误
| TabError| Tab 和空格混用
| SystemError |一般的解释器系统错误
| TypeError| 对类型无效的操作
| ValueError |传入无效的参数
| UnicodeError |Unicode 相关的错误
| UnicodeDecodeError |Unicode 解码时的错误
| UnicodeEncodeError |Unicode 编码时错误
| UnicodeTranslateError| Unicode 转换时错误
| Warning |警告的基类
| DeprecationWarning| 关于被弃用的特征的警告
| FutureWarning |关于构造将来语义会有改变的警告
| OverflowWarning| 旧的关于自动提升为长整型(long)的警告
| PendingDeprecationWarning| 关于特性将会被废弃的警告
| RuntimeWarning |可疑的运行时行为(runtime behavior)的警告
| SyntaxWarning| 可疑的语法的警告
| UserWarning| 用户代码生成的警告

#### 2.2 异常处理

Python 程序捕捉异常使用 try/except 语句，先看个例子：

```
# 1.被除数为 0，未捕获异常
def getNum(n):
        return 10 / n
print(getNum(0))
#输出结果： ZeroDivisionError: division by zero

# 2.捕获异常
def getNum(n):
    try:
        return 10 / n
    except IOError:
        print('Error: IOError argument.')
    except ZeroDivisionError:
        print('Error: ZeroDivisionError argument.')
print(getNum(0))
'''
输出结果：
Error: ZeroDivisionError argument.
None
'''

```

try 语句的工作方式为：
-  首先，执行 try 子句 （在 try 和 except 关键字之间的部分）； -  如果没有异常发生， except 子句 在 try 语句执行完毕后就被忽略了； -  如果在 try 子句执行过程中发生了异常，那么该子句其余的部分就会被忽略； -  如果异常匹配于 except 关键字后面指定的异常类型，就执行对应的except子句，然后继续执行 try 语句之后的代码； -  如果发生了一个异常，在 except 子句中没有与之匹配的分支，它就会传递到上一级 try 语句中； -  如果最终仍找不到对应的处理语句，它就成为一个 未处理异常，终止程序运行，显示提示信息。 
try/except 语句还可以带有一个 else、finally子句，示例如下：

```
def getNum(n):
    try:
        print('try --&gt; ',10 / n)
    except ZeroDivisionError:
        print('except --&gt; Error: ZeroDivisionError argument.')
    else:
        print('else --&gt;')
    finally:
        print('finally --&gt;')

'''
1.调用：getNum(0)
输出结果：
except --&gt; Error: ZeroDivisionError argument.
finally --&gt;

2.调用：getNum(1)
输出结果：
try --&gt;  10.0
else --&gt;
finally --&gt;
'''

```

其中，else 子句只能出现在所有 except 子句之后，只有在没有出现异常时执行；finally 子句放在最后，无论是否出现异常都会执行。

#### 2.3 抛出异常

使用 raise 语句允许强制抛出一个指定的异常，要抛出的异常由 raise 的唯一参数标识，它必需是一个异常实例或异常类（继承自 Exception 的类），如：

```
raise NameError('HiThere')

```

#### 2.4 自定义异常

正常来说，Python 提供的异常类型已经满足我们的使用了,但是有时候我们有定制性的需求，我们可以自定义异常类，继承自 Error 或 Exception 类就可以了，看个例子：

```
# 自定义异常类 MyExc
class MyExc(Exception):  #继承Exception类
    def __init__(self, value):
        self.value = value
    def __str__(self):
        if self.value == 0:
            return '被除数不能为0'
# 自定义方法
def getNum(n):
    try:
        if n == 0:
            exc = MyExc(n)
            print(exc)
        else:
            print(10 / n)
    except:
        pass
'''
1.调用 getNum(1)，输出结果为：
10.0

2.调用 getNum(0)，输出结果为：
被除数不能为0
'''

```

在这个自定义的异常例子中，当参数 n 不为 0 时，则正常，当 n 等于 0，则抛出异常，自定义异常在实际应用中很少用到，了解即可。

参考：  

<img src="https://img-blog.csdnimg.cn/20191212073821865.png#pic_center" alt="" width="600">
