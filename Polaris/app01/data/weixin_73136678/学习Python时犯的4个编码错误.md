
--- 
title:  学习Python时犯的4个编码错误 
tags: []
categories: [] 

---
## 我在学习Python时犯的4个编码错误

几年前，我开始了学习Python的冒险，我已经知道了一些其他的编程语言，如PHP（让我接触到网络开发的第一种语言）、JavaScript（我已经很擅长了，正在写一个UI库）和C#，这是我当时收入的来源。

我通过自己开发一个应用程序来学习Python，因此我在代码中加入了许多JavaScript和C#的做事方式，这很糟糕，虽然有时会成功。我花了一些时间，阅读其他人的代码，并与其他人一起工作，才真正在语言上变得更好。今天我想和大家一起探讨一下我在学习Python时犯的一些错误（代码方面）。

### #1 对Python作用域的误解

Python的范围解析是基于所谓的**LEGB**规则，它是**Local**、**Enclosing**、**Global**、**Builtin**的简写。尽管看起来非常简单，但当时对我来说还是有点困惑，例如，考虑下面的例子。

```
x = 5
def foo():
    x += 1
    print(x)

foo()

-----------
Output
-----------
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 2, in foo
UnboundLocalError: local variable 'x' referenced before assignment
复制代码
```

对于上面的代码，我本以为它可以工作，改变全局变量`x` ，最后打印`6` 。但是，它可以变得更奇怪，让我们看一下下面的改动后的代码。

```
y = 5
def foo_y():
    print(y)

foo_y()

-----------
Output
-----------
5
复制代码
```

这到底是怎么回事呢？在一个代码段中，全局变量`X` 给出了一个`UnboundLocalError` ，然而，当我们只是试图打印这个变量时，它却能工作。其原因与范围有关。当你在一个作用域（如函数作用域）中对一个变量进行赋值时，该变量就会成为该作用域的局部变量，并对外部作用域中的任何类似命名的变量产生阴影。这就是在第一种情况下发生的事情，当我们做`x += 1` 。

如果我们的意图是访问全局变量`x` ，就像我们的函数`foo()` ，我们可以做这样的事情。

```
x = 5
def foo():
    global x
    x += 1
    print(x)

foo()

-----------
Output
-----------
6
复制代码
```

通过使用关键字`global` ，允许内部作用域访问全局作用域中声明的变量，也就是说，没有在任何函数中定义的变量。类似地，我们可以使用`nonlocal` 来产生类似的效果。

```
def foo():
    x = 5
    def bar():
        nonlocal x
        x += 1
        print(x)
    bar()

foo()

-----------
Output
-----------
6
复制代码
```

`nonlocal` 因为 允许你从外部作用域访问变量，然而，在 的情况下，你可以绑定到父作用域或全局作用域上的一个对象。`global` `nonlocal`

### #2 在迭代列表的同时修改它

尽管这个错误不仅在 Python 中常见，但我发现这个错误在新的 Python 开发者中相当普遍，甚至对一些有经验的开发者也是如此。虽然有时看起来不是那么明显，但在某些场合下，我们最终修改了我们目前正在迭代的数组，导致了不恰当的行为，或者如果我们幸运的话，我们得到了一个错误并很容易注意到它。

但让我举个例子来说明我的意思，假设给定一个数组，你需要将该数组减少到只包含偶数元素，你可能会尝试做这样的事情。

```
def odd(x): return bool(x % 2)
numbers = [n for n in range(10)]
for i in range(len(numbers)):
    if odd(numbers[i]):
        del numbers[i]

-----------
Output
-----------
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 2, in &lt;module&gt;
IndexError: list index out of range
复制代码
```

在所描述的情况下，当在迭代时删除一个列表或数组的元素时，我们会得到一个错误，因为我们试图访问一个已经不存在的项目。这是一种不好的做法，应该避免，在 python 中有更好的方法来实现类似的事情，其中就有列表理解法。

```
def odd(x): return bool(x % 2)
numbers = [n for n in range(10)]
numbers[:] = [n for n in numbers if not odd(n)]
print(numbers)

-----------
Output
-----------
[0, 2, 4, 6, 8]
复制代码
```

你也可以使用`filter` 函数来实现同样的目的，虽然它可以工作，但有些人认为这不是Pythonic的方法，我有点同意，但我不想陷入这种讨论中。我宁愿给你选择，你可以研究和决定。

```
def even(x): return not bool(x % 2)
numbers = [n for n in range(10)]
numbers = list(filter(even, numbers))
numbers

-----------
Output
-----------
[0, 2, 4, 6, 8]
复制代码
```

### #3 闭包中的变量绑定

我想从我在twitter）上发布的一个测验开始，我问人们他们认为下面这个片段的结果会是什么。

```
def create_multipliers():
    return [lambda x : i * x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2))

-----------
Output
-----------
8
8
8
8
8
复制代码
```

对于很多人来说，包括我自己，第一次遇到这个问题时，我们认为结果会是。

```
0
2
4
6
8
复制代码
```

然而，代码的结果实际上完全不同，我们非常不解为什么。实际发生的情况是，Python 会做一个迟到的绑定行为，根据这个行为，在闭包中使用的变量的值是在调用内部函数的时候查询的。所以在我们的例子中，只要有任何一个返回的函数被调用，`i` 的值就会在调用时在周围的范围内被查找。

解决这个问题的方法看起来有点黑，但它实际上是可行的

```
def create_multipliers():
    return [lambda x, i=i : i * x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2))

-----------
Output
-----------
0
2
4
6
8
复制代码
```

通过使用lambda函数的默认参数来传递`i` 的值，我们可以生成函数来完成所需的行为。我对这个解决方案非常不解，而且我仍然认为它不是很优雅，然而，有些人喜欢它。如果你知道这个问题的另一个可能的解决方案，请在评论中告诉我，我很想读到它。

### #4 与Python标准库模块的名称冲突

这个问题在我刚开始的时候其实很常见，即使是现在，有时我也会犯这种错误。这个问题是由于你的一个模块的名字与Python标准库中的一个模块的名字相同而产生的。(例如，你的代码中可能有一个名为email.py的模块，这将与标准库中的同名模块发生冲突)。

也许名称冲突本身不会对你的代码产生任何问题，但有时我们会覆盖 Python 标准库中的一个函数或模块，该函数或模块后来被用于已安装的库中，它要么通过抛出错误，要么通过错误行为而发生冲突。无论如何，这都是一种不好的情况。

一个典型的错误是下面这个。

```
a = list()
print(a)

list = [1, 2, 3] # This is where we break it
a = list()

-----------
Output
-----------
[]
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: 'list' object is not callable
复制代码
```

通过简单地创建一个名为`list` 的变量，我们破坏了对`list` 函数的访问。而且，即使有其他的访问方式（例如：`__builtins__.list()` ），我们也应该避免这种名称。

### 总结

这篇文章并没有涵盖开发者在用Python编码时的所有常见错误，而是那些我最纠结的事情。如果你想知道更多关于如何写好Python代码和避免其他一些错误的信息，我推荐你阅读。
