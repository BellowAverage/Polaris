
--- 
title:  深入浅出Python异常处理 - 你所不知道的Python异常 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/d779e495e8bd3b228e6b5030a391c7a6.jpeg" alt="6c1b62737ddb2bd3d45bfd16f4f261ee.jpg">

## 深入浅出Python异常处理 - 你所不知道的Python异常

## 前言

在`Python`编程开发中，异常处理扮演者至关重要的角色。合适的异常处理不仅可以提高代码的健壮性，还能增强程序的可读性和可维护性。在`Python`编程中，有效地管理异常是提高代码质量的关键一环。

本文旨在深入浅出地介绍`Python`中的异常处理，从基本概念到高级应用，我们将一步步探索`Python`异常处理的世界，揭示那些你可能未曾了解的知识和技巧。

## 异常处理概览

在``Python`3.12.0`的官方文档中，对异常的解释如下： 官方文档：https://docs.python.org/zh-cn/3/tutorial/errors.html

>  
 执行时检测到的错误称为 **异常**。 


**什么是异常？**

在 `Python` 中，异常指的是程序执行过程中发生的错误或意外情况。它们可能由各种原因产生，例如无效的输入、错误的操作或其他外部因素。当 `Python` 检测到这些情况时，会引发（或抛出）一个异常。异常本质上是一个对象，属于 `Exception` 类或其子类。代表了程序中出现的错误或意外。如果这个异常没有得到适当的处理，程序将终止并显示错误信息。

**异常处理的重要性**

异常处理是编写健壮且可维护代码的关键。适当的异常处理可以预防许多错误和程序崩溃，提高程序的稳定性和用户体验。通过有效的异常处理，我们可以控制程序在遇到错误时的反应，比如记录错误信息、恢复程序状态或通过警报通知用户。

**异常处理的基本结构**

`Python` 中的异常处理主要依赖于 `try-except` 语句块。将可能引发异常的代码放在 `try` 块中，并在 `except` 块中定义异常发生时的处理逻辑。此外，`finally` 和 `else` 子句提供了更多的控制选项，允许在发生或未发生异常时执行特定代码。

## 标准异常类型

`Python`中的所有异常都继承自 `BaseException` 类。最常见的异常基类是 `Exception`。`Python`标准库定义了许多不同类型的异常（如 `ValueError`, `TypeError`, `IndexError`, `KeyError` 等），它们都继承自 `Exception`。

除此之外，`Python`也允许我们定义自己的异常类型，以适应特定的业务逻辑需求。

贴一个在菜鸟教程上的关于`Python`标准异常类型的表格：

<th align="left">异常名称</th><th align="left">描述</th>
|------
<td align="left">BaseException</td><td align="left">所有异常的基类</td>
<td align="left">SystemExit</td><td align="left">解释器请求退出</td>
<td align="left">KeyboardInterrupt</td><td align="left">用户中断执行(通常是输入^C)</td>
<td align="left">Exception</td><td align="left">常规错误的基类</td>
<td align="left">StopIteration</td><td align="left">迭代器没有更多的值</td>
<td align="left">GeneratorExit</td><td align="left">生成器(generator)发生异常来通知退出</td>
<td align="left">StandardError</td><td align="left">所有的内建标准异常的基类</td>
<td align="left">ArithmeticError</td><td align="left">所有数值计算错误的基类</td>
<td align="left">FloatingPointError</td><td align="left">浮点计算错误</td>
<td align="left">OverflowError</td><td align="left">数值运算超出最大限制</td>
<td align="left">ZeroDivisionError</td><td align="left">除(或取模)零 (所有数据类型)</td>
<td align="left">AssertionError</td><td align="left">断言语句失败</td>
<td align="left">AttributeError</td><td align="left">对象没有这个属性</td>
<td align="left">EOFError</td><td align="left">没有内建输入,到达EOF 标记</td>
<td align="left">EnvironmentError</td><td align="left">操作系统错误的基类</td>
<td align="left">IOError</td><td align="left">输入/输出操作失败</td>
<td align="left">OSError</td><td align="left">操作系统错误</td>
<td align="left">WindowsError</td><td align="left">系统调用失败</td>
<td align="left">ImportError</td><td align="left">导入模块/对象失败</td>
<td align="left">LookupError</td><td align="left">无效数据查询的基类</td>
<td align="left">IndexError</td><td align="left">序列中没有此索引(index)</td>
<td align="left">KeyError</td><td align="left">映射中没有这个键</td>
<td align="left">MemoryError</td><td align="left">内存溢出错误(对于`Python` 解释器不是致命的)</td>
<td align="left">NameError</td><td align="left">未声明/初始化对象 (没有属性)</td>
<td align="left">UnboundLocalError</td><td align="left">访问未初始化的本地变量</td>
<td align="left">ReferenceError</td><td align="left">弱引用(Weak reference)试图访问已经垃圾回收了的对象</td>
<td align="left">RuntimeError</td><td align="left">一般的运行时错误</td>
<td align="left">NotImplementedError</td><td align="left">尚未实现的方法</td>
<td align="left">SyntaxError</td><td align="left">`Python` 语法错误</td>
<td align="left">IndentationError</td><td align="left">缩进错误</td>
<td align="left">TabError</td><td align="left">Tab 和空格混用</td>
<td align="left">SystemError</td><td align="left">一般的解释器系统错误</td>
<td align="left">TypeError</td><td align="left">对类型无效的操作</td>
<td align="left">ValueError</td><td align="left">传入无效的参数</td>
<td align="left">UnicodeError</td><td align="left">Unicode 相关的错误</td>
<td align="left">UnicodeDecodeError</td><td align="left">Unicode 解码时的错误</td>
<td align="left">UnicodeEncodeError</td><td align="left">Unicode 编码时错误</td>
<td align="left">UnicodeTranslateError</td><td align="left">Unicode 转换时错误</td>
<td align="left">Warning</td><td align="left">警告的基类</td>
<td align="left">DeprecationWarning</td><td align="left">关于被弃用的特征的警告</td>
<td align="left">FutureWarning</td><td align="left">关于构造将来语义会有改变的警告</td>
<td align="left">OverflowWarning</td><td align="left">旧的关于自动提升为长整型(long)的警告</td>
<td align="left">PendingDeprecationWarning</td><td align="left">关于特性将会被废弃的警告</td>
<td align="left">RuntimeWarning</td><td align="left">可疑的运行时行为(runtime behavior)的警告</td>
<td align="left">SyntaxWarning</td><td align="left">可疑的语法的警告</td>
<td align="left">UserWarning</td><td align="left">用户代码生成的警告</td>

## 异常基本信息 &amp; 语法

>  
 `Python`提供了一套异常处理机制，允许程序在发生异常时优雅地处理。 


下面的这些部分共同构成了`Python`中异常处理的基础，在对它们充分理解后，可以帮助我们写出更健壮和易于维护的代码哦。

### 基本语法

在`Python`中，异常处理的基本结构包括 `try`, `except`, `else`, 和 `finally` 块。

**基本结构**

```
try:
    # 尝试执行的代码
except ExceptionType:
    # 当上述代码引发ExceptionType异常时执行的代码
else:
    # 如果没有异常发生执行的代码
finally:
    # 无论是否发生异常都会执行的代码

```
- `try` 块中放置的是可能引发异常的代码。- `except` 块定义了当特定异常发生时的处理逻辑。- `else` 块中的代码仅在没有异常发生时执行。- `finally` 块中的代码无论是否发生异常都会执行，通常用于执行一些清理工作。
**示例**

```
try:
    result = 10 / 2
except ZeroDivisionError:
    print("发生了除以零的错误")
else:
    print("结果是", result)
finally:
    print("执行完毕，无论是否发生异常")


```

在这个示例中，如果 `try` 块中的代码成功执行（即没有发生异常），那么 `else` 块中的代码将被执行。无论是否发生异常，`finally` 块中的代码都会被执行，通常用于资源释放或清理工作。

通过这种结构，`Python`的异常处理不仅可以处理错误情况，还能在正常情况下执行特定代码，并且确保最终总能执行某些必要的清理操作。

### 引发异常 (raise)

我们可以使用 `raise` 语句手动引发异常。这通常在检测到某些条件下，继续执行程序会导致问题时使用。

```
def check_age(age):
    if age &lt; 18:
        raise ValueError("年龄不足18岁")


```

### 捕获异常 (try-except)

使用 `try-except` 语句块可以捕获和处理异常，防止程序意外崩溃。

```
try:
    check_age(15)
except ValueError as error:
    print("捕获到异常:", error)


```

### 获取详细异常信息（sys.exc_info）

在处理异常时，有时仅知道发生了异常并不足够，我们可能还需要了解异常发生时的更多上下文信息。`Python`提供了 `sys.exc_info()` 函数，它可以在异常处理块内被调用，以获取正在处理的异常的详细信息。

当在一个 `except` 块中调用 `sys.exc_info()` 时，它会返回一个包含三个值的元组，分别是：
1. **异常类型 (`exc_type`)**: 引发的异常的类型。1. **异常值 (`exc_value`)**: 异常实例本身，通常包含错误消息。1. **追踪回溯对象 (`exc_traceback`)**: 包含异常发生时调用堆栈的详细信息的对象。
这些信息对于调试问题和记录错误日志非常有用。

**示例**
- 通过使用 `sys.exc_info()`，可以获取到有关当前异常的更详尽的信息。
```
import sys
import traceback

try:
    # 可能引发异常的代码
    1/ 0
except ZeroDivisionError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("异常类型:", exc_type)
    print("异常值:", exc_value)
    print("追踪回溯:")
    # 直接打印异常的追踪信息到标准输出
    traceback.print_tb(exc_traceback)


```

代码运行结果如下：

<img src="https://img-blog.csdnimg.cn/img_convert/61bf57f77a35ddd8bb92801b1d7686a3.png" alt="610fe31b88b24a5fb9940df05f132bb5.png">

### 基础异常处理代码

在实际应用中，通常会将引发和捕获异常结合起来，以确保程序的健壮性和可维护性。

**示例**

```
import sys
import traceback

def check_age(age):
    if age &lt; 18:
        raise ValueError("年龄不足18岁")

try:
    age = 15
    check_age(age)
except ValueError as error:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("捕获到异常:", error)
    print("异常类型:", exc_type)
    print("异常信息:", exc_value)
    print("追踪回溯:")
    # 获取异常的追踪信息。返回的是追踪信息的字符串列表，每个字符串代表追踪信息中的一行
    print(''.join(traceback.format_tb(exc_traceback)))
finally:
    print("处理完毕")


```

在这个示例中，当 `check_age` 函数引发 `ValueError` 异常时，`except` 块不仅会打印出异常信息，还会通过 `sys.exc_info()` 获取并打印出异常的类型、具体信息以及追踪回溯。这样做可以帮助我们更准确地理解异常发生的上下文，对于调试和记录错误日志非常有用。

**代码运行效果如下：**

<img src="https://img-blog.csdnimg.cn/img_convert/bcf5856536b2622811a7162bb9199c9a.png" alt="870c9755917140b8b26a8d70245ed690.png">

## 自定义异常 (Custom Exceptions)

**应用场景**
- **特定业务逻辑**：当标准异常无法准确描述特定业务逻辑错误时。
**优势**
- **代码清晰度**：使错误处理更直观，提高代码的可读性。- **错误分类**：方便对特定类型的错误进行特殊处理。
**基础示例：**

```
class MyCustomError(Exception):
    """一个自定义的异常类，用于特定的错误情况。"""


def my_function(value):
    if not value:
        raise MyCustomError("值不能为空")


```

再来一个接近真实编程环境中的示例代码，

**示例代码**

```
class NegativeValueError(Exception):
    """当输入值为负数时引发的异常。"""

    def __init__(self, value):
        self.value = value
        self.message = "输入值不应为负数"
        super().__init__(self.message)


def check_positive(number):
    if number &lt; 0:
        raise NegativeValueError(number)
    return number


try:
    result = check_positive(-10)
except NegativeValueError as e:
    print(f"错误：{<!-- -->e.message} - 输入值: {<!-- -->e.value}")


```

**代码释义：**

这段代码定义了一个名为 `NegativeValueError` 的自定义异常类，用于处理输入值为负数的错误情况：
<li>**自定义异常类 `NegativeValueError`**： 
  1. 继承自`Python`的基本`Exception`类。1. 包含一个构造函数，接受一个`value`参数，并设置一个错误消息`"输入值不应为负数"`。1. 通过`super().__init__(self.message)`调用基类构造函数，将错误消息传递给基类。 </li><li>**函数 `check_positive`**： 
  1. 这个函数接受一个数字作为参数。1. 如果数字小于零，函数将引发`NegativeValueError`异常，传递该数字作为参数。1. 如果数字非负，函数正常返回该数字。 </li><li>**异常处理**： 
  1. 使用`try-except`块来捕获`NegativeValueError`异常。1. 如果捕获到此异常，将打印出错误消息和导致异常的值。 </li>- 这个函数接受一个数字作为参数。- 如果数字小于零，函数将引发`NegativeValueError`异常，传递该数字作为参数。- 如果数字非负，函数正常返回该数字。
**代码运行效果：**

<img src="https://img-blog.csdnimg.cn/img_convert/f3d74122e4026ce81ede820ff4e609df.png" alt="e3b0116bcfc74e5496d6f9495d934adc.png">

## 异常链 (Exception Chaining)

**应用场景**
- **复杂的错误处理**：在一个复杂的程序中，处理异常时可能会引发另一个异常，异常链可以帮助追踪这一过程。- **调试和日志记录**：当需要详细记录或调试一个异常的整个发生过程时，异常链提供了一种追踪原始异常源的方法。
**优势**
- **保留异常上下文**：允许开发人员看到异常的“历史”，从最初的异常到最终的异常。- **提高可调试性**：通过保留异常链，开发者可以更容易地理解错误的根本原因，特别是在复杂的系统中。
**基础语法：**
- 异常链是通过在`raise`语句中使用`from`关键字来实现的。- `SomeException`是尝试捕获的异常类型，`NewException`是想要引发的新异常类型。通过使用`from e`，将原始的异常信息附加到新的异常上，从而创建了一个异常链。
```
try:
    # 尝试执行某些可能引发异常的操作
except SomeException as e:
    # 处理这个异常
    raise NewException("An error occurred") from e


```

**先来看官方文档的示例：**

```
def func():
    raise ConnectionError


try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc


```

**代码运行效果如下：**
- 上述异常是导致以下异常的直接原因（直接就明说了，第2行是导致第8行错误的直接原因）
<img src="https://img-blog.csdnimg.cn/img_convert/4c04c5ee61d81db4cb853d6a6b971bad.png" alt="7188ace7be92472dae2a3f478c06f561.png">

进一步的，我使用一个真实的例子，以方便大家的理解。

```
import json
import sys
import traceback


class DatabaseConnectionError(Exception):
    """自定义数据库连接异常"""

    def __init__(self, message):
        super().__init__(message)


def save_to_database(data):
    # 假设的数据库保存操作
    # 这里我们故意抛出一个异常来模拟数据库连接错误
    raise DatabaseConnectionError("数据库连接失败")


def process_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            save_to_database(data)
    except FileNotFoundError as e:
        raise RuntimeError("文件未找到") from e
    except DatabaseConnectionError as e:
        raise RuntimeError("数据库操作失败") from e


if __name__ == '__main__':
    # 调用函数
    try:
        process_file("data.json")
    except RuntimeError as e:
        print(f"捕获到异常: {<!-- -->e}")
        print(f"原始异常: {<!-- -->e.__cause__}")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback_details = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        print("\nTraceback details:\n", traceback_details)


```

**代码释义：**
1.  **自定义异常类**：定义 `DatabaseConnectionError`，创建了一个异常类型，用于数据库连接错误。 1.  **异常封装**：在 `process_file` 函数中，捕获了两种类型的异常（`FileNotFoundError` 和 `DatabaseConnectionError`），并将它们封装成 `RuntimeError`，同时保留了原始异常的信息。这是通过 `from e` 语法实现的，它创建了一个异常链，保留了底层异常的上下文。 1.  **异常信息打印**：在外层的 `try-except` 块中，不仅打印了捕获的 `RuntimeError` 的信息，还打印了原始异常（`e.__cause__`）的信息，这有助于理解异常发生的完整路径。 1.  **完整的调用栈信息**：通过使用 `sys.exc_info()` 和 `traceback.format_exception`，能够获取并打印出异常发生时的完整调用栈信息。这对于定位异常发生的具体位置非常有用。 
**代码运行效果如下：**
- 异常信息打印的非常清晰~ <img src="https://img-blog.csdnimg.cn/img_convert/4f91872d98a2357bb00da0df48535421.png" alt="5e5fb9d5f2024a33839fecde9573a03b.png">
## 最佳实践和常见错误

### 最佳实践
1. **使用具体的异常**：捕获特定异常，避免通用异常捕获，以提供更准确的错误处理和反馈。1. **避免空的异常处理**：不留空的`except`块，即使是简单记录错误也好。1. **使用异常链**：在处理异常时保留原始异常信息，有助于调试和理解错误源。1. **资源清理**：使用`finally`块或`with`语句确保资源（如文件和网络连接）得到适当清理。1. **自定义异常**：当标准异常不足以表达特定错误时，定义自定义异常，使代码更易理解和维护。1. **异常消息的清晰度**：提供清晰、具体的异常消息，有助于快速定位问题。1. **避免过多的异常处理**：避免不必要或过度的异常捕获，以防隐藏代码中的真正问题。
### 常见错误
1. **捕获太宽泛的异常**：避免使用过于广泛的异常捕获（如`except Exception:`），可能会掩盖其他错误。1. **重复的异常处理**：避免在多层函数调用中重复处理相同的异常，以免导致代码冗余和混乱。1. **忽视异常**：不使用空的`except`块或完全忽视异常，以免错过潜在的错误。1. **异常滥用**：避免使用异常来控制正常的程序流程，这不是异常设计的初衷。
## 总结✨✨

本文全面地介绍了`Python`中异常处理的各个方面，从基础知识到高级应用，提供了深入理解和有效管理异常的方法。

`Python`的异常处理是一个强大且灵活的机制，允许我们以优雅和有效的方式处理错误和意外情况。

重要的是要理解异常处理的原则和目的，即在不正常或意外的情况下保护程序的稳定性和可预测性。通过遵循最佳实践并避免常见的错误，我们可以编写更健壮、更可读且易于维护的代码。

## 后话

本次分享到此结束，

see you~🐱‍🏍🐱‍🏍
