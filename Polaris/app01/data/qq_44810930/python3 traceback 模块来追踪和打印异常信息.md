
--- 
title:  python3 traceback 模块来追踪和打印异常信息 
tags: []
categories: [] 

---
>  
 多线程或者多进程中可能需要使用`traceback`来捕获异常信息 




#### 文章目录
- <ul><li>- 


在 Python 3 中，你可以使用标准库中的 `traceback` 模块来追踪和打印异常信息。这个模块提供了许多函数来处理异常，并且能够输出异常的堆栈信息，帮助你定位错误的地方。以下是一个简单的示例代码，演示了如何使用 `traceback` 模块来追踪报错信息：

### `print_exc` 打印异常

```
import traceback

def function_a():
    return 1 / 0  # 触发一个除零异常

def main_function():
    try:
        function_a()
    except Exception as e:
        # 打印异常信息
        traceback.print_exc()
        # 异常信息字符串
        err = traceback.format_exc()

main_function()

```

在上面的示例中，我们定义了两个函数 `function_a` 和 `main_function`。在 `function_a` 中我们故意触发了一个除零异常。在 `main_function` 中，我们使用 `try...except` 结构来捕获异常，并调用 `traceback.print_exc()` 来打印异常信息。

当你运行这段代码时，就会看到包含了异常信息和堆栈跟踪的输出。

### `extract_tb` 提取堆栈

`traceback.extract_tb()` 函数用于提取堆栈跟踪信息，并返回一个包含各个帧信息的列表。每个帧信息都以元组的形式返回，包括文件名、行号、函数名和源代码行。以下是一个简单的示例代码，演示了如何使用 `traceback.extract_tb()` 函数：

```
import traceback

def function_a():
    return 1 / 0  # 触发一个除零异常

def main_function():
    try:
        function_a()
    except Exception as e:
        # 提取堆栈跟踪信息
        tb_list = traceback.extract_tb(e.__traceback__)
        
        # 打印每个帧的信息
        for tb in tb_list:
            print("File:", tb.filename)
            print("Line:", tb.lineno)
            print("Function:", tb.name)
            print("Code:", tb.line)
            print()

main_function()

```

在上面的示例中，我们定义了两个函数 `function_a` 和 `main_function`，其中 `function_a` 故意触发了一个除零异常。在 `main_function` 中，我们使用 `try...except` 结构捕获异常，并通过 `traceback.extract_tb(e.__traceback__)` 提取堆栈跟踪信息。

然后，我们遍历提取到的堆栈跟踪信息列表 `tb_list`，并打印每个帧的文件名、行号、函数名和源代码行。

当你运行这段代码时，就会看到输出包含了每个帧的详细信息。
