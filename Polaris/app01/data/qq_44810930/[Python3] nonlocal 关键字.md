
--- 
title:  [Python3] nonlocal 关键字 
tags: []
categories: [] 

---
在 Python 3 中，`nonlocal` 关键字用于在嵌套函数中访问并修改位于外部函数作用域的变量。它与 `global` 关键字类似，但是 `nonlocal` 用于嵌套函数的局部作用域，而 `global` 用于模块级别的全局作用域。

下面是一个示例，展示了如何使用 `nonlocal` 关键字：

```
def outer():
    x = 10

    def inner():
        nonlocal x
        x += 5
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()

```
-  在这个示例中，定义了一个外部函数 `outer()` 和一个嵌套函数 `inner()`。 -  在 `outer()` 函数内部，我们定义了一个变量 `x` 并将其初始化为 10。 -  在 `inner()` 函数内部，使用 `nonlocal` 关键字声明 `x` 是来自 `outer()` 函数的局部变量，并对其进行修改 
在 `outer()` 函数中，我们调用了 `inner()` 函数，并在之后打印了变量 `x` 的值。由于 `x` 是被 `nonlocal` 声明的变量，所以在 `inner()` 函数中的修改也会影响到 `outer()` 函数中的变量。

运行上述代码，输出将是：

```
Inner: 15
Outer: 15

```

这表明 `inner()` 函数能够修改 `outer()` 函数中的变量 `x`，并且这种修改是可见的。
