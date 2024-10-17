
--- 
title:  [python] `sys.settrace` 跟踪函数 
tags: []
categories: [] 

---
`sys.settrace` 是 Python 中的一个调试工具，它允许你设置一个跟踪函数，在程序执行过程中对每个函数调用进行跟踪。当设置了跟踪函数后，Python 解释器在每次函数调用、返回或异常抛出时都会调用该跟踪函数，从而使你能够观察和记录程序的执行流程。

>  
 获取函数调用时的参数和返回值 


下面是一个简单的示例代码，演示了如何使用 `sys.settrace` 方法来跟踪函数的调用和返回：

```
import sys


def trace_calls(frame, event, arg):
    if event == 'call':
        function_name = frame.f_code.co_name
        args = frame.f_locals
        print(f'Calling function: {<!-- -->function_name}, {<!-- -->args}')
    elif event == 'return':
        function_name = frame.f_code.co_name
        return_value = arg
        print(f'Returning from function: {<!-- -->function_name}, Return value: {<!-- -->return_value}')
    return trace_calls


def add(a, b):
    return a + b


def main():
    sys.settrace(trace_calls)
    result = add(3, 4)
    sys.settrace(None)  # 停止跟踪
    print(f"Result: {<!-- -->result}")


main()


```

在这个示例中，我们定义了一个名为 `trace_calls` 的跟踪函数，它接收三个参数 `frame`, `event`, 和 `arg`。在跟踪函数中，我们通过检查 `event` 参数的值来判断函数是被调用还是返回，并打印相应的信息。最后，我们使用 `sys.settrace` 来启用和停用跟踪函数。

当你运行这段代码时，你将会看到如下输出：

```
Calling function: add, {'a': 3, 'b': 4}
Returning from function: add, Return value: 7
Result: 7

```

这表明我们的跟踪函数成功地捕获了函数的调用和返回。

在 `sys.settrace` 中，`event` 参数可以取以下几种值：
1. `'call'`：表示函数被调用时触发。1. `'return'`：表示函数返回时触发。1. `'exception'`：表示函数抛出异常时触发。
通过检查这些事件类型，你可以在跟踪函数中执行相应的操作，例如记录函数的调用和返回、处理异常等。这使得你能够对程序的执行流程进行详细的跟踪和记录。

### frame对象

当使用 `sys.settrace()` 设置的跟踪函数被调用时，传递给它的 `frame` 参数是一个帧对象，它代表了当前执行栈的一个帧。这个帧对象提供了多个属性，允许你访问当前帧的各种信息。以下是这些属性的简要介绍：
1.  `f_back`: 指向当前帧的调用者（上一个帧对象）的引用。如果当前帧是全局帧或最外层的帧，则此值为 `None`。 1.  `f_builtins`: 一个字典，包含了当前帧的内建函数和变量的引用。这通常是 `__builtins__` 模块的内容。 1.  `f_code`: 一个代码对象，表示当前帧正在执行的代码。你可以通过它访问函数的字节码、常量、变量名等信息。 1.  `f_globals`: 一个字典，包含了当前帧的全局变量的引用。对于函数来说，这通常是定义它的模块的全局命名空间。 1.  `f_lasti`: 一个整数，表示在当前帧中字节码指令的索引，该指令将在下一次执行时被执行。 1.  `f_lineno`: 一个整数，表示当前帧正在执行的代码行号。 1.  `f_locals`: 一个字典或其他的映射对象，包含了当前帧的局部变量的引用。注意，在函数内部修改这个字典的内容可能会影响实际的局部变量，但在某些情况下（如优化过的函数）可能不起作用。 1.  `f_trace`: 如果当前帧有一个跟踪函数，则此属性引用该函数；否则为 `None`。这不同于使用 `sys.settrace()` 设置的全局跟踪函数，它更局部于特定的帧。 1.  `f_trace_lines`: 一个布尔值，表示是否应该为当前帧的每一行都调用跟踪函数。这通常由全局跟踪函数通过返回一个新的跟踪函数并设置此属性来控制。 1.  `f_trace_opcodes`: 一个布尔值，表示是否应该为当前帧的每一个字节码指令都调用跟踪函数。类似于 `f_trace_lines`，但它针对的是字节码指令而不是源代码行。 
需要注意的是，`clear` 并不是帧对象的一个属性。可能是你在提问时将某个方法或操作与属性混淆了。帧对象本身没有名为 `clear` 的方法或属性。

另外，要注意的是，直接修改帧对象的某些属性（如 `f_locals`）可能会导致未定义的行为或错误，因为它们是解释器内部状态的一部分。通常，你应该只读取这些属性以获取有关当前执行环境的信息，而不是尝试修改它们。
