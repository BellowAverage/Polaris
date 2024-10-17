
--- 
title:  Python 装饰器 打印出函数执行的基本信息 
tags: []
categories: [] 

---
展示如何编写一个装饰器，在被装饰函数执行前后打印出函数的名称、入参、返回值以及执行时间等有用信息：

```
import time
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {<!-- -->func.__name__}")
        print(f"Input arguments: {<!-- -->args}, {<!-- -->kwargs}")
        
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        print(f"Returned value: {<!-- -->result}")
        print(f"Execution time: {<!-- -->end_time - start_time} seconds")
        
        return result

    return wrapper

# 使用装饰器
@my_decorator
def example_function(x, y):
    time.sleep(1)  # 模拟函数执行时间
    return x + y

# 调用被装饰的函数
result = example_function(3, 4)

```

在上面的代码中，`my_decorator` 是一个装饰器函数，它内部定义了一个 `wrapper` 函数作为装饰函数。`wrapper` 函数会在被装饰的函数执行前后分别打印出函数的名称、入参、返回值和执行时间。使用 `@wraps(func)` 装饰器可以保留被装饰函数的元信息，比如函数名称等。

通过在被装饰函数上方添加 `@my_decorator`，就可以达到在函数执行前后打印相关信息的效果。当调用 `example_function(3, 4)` 时，装饰器会打印出相关信息并计算函数的执行时间。
