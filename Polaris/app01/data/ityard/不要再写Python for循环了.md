
--- 
title:  不要再写Python for循环了 
tags: []
categories: [] 

---
为什么要挑战自己在代码里不写 for loop？因为这样可以迫使你去学习使用比较高级、比较地道的语法或 library。文中以 python 为例子，讲了不少大家其实在别人的代码里都见过、但自己很少用的语法。

自从我开始探索 Python 中惊人的语言功能已经有一段时间了。一开始，我给自己一个挑战，目的是让我练习更多的 Python 语言功能，而不是使用其他编程语言的编程经验。这让事情变得越来越有趣！代码变得越来越简洁，代码看起来更加结构化和规范化。下面我将会介绍这些好处。

通常如下使用场景中会用到 for 循环：
- 在一个序列来提取一些信息。- 从一个序列生成另一个序列。- 写 for 已成习惯。
幸运的是，Python 已经有很多工具可以帮助你完成这些工作，你只需要转移你的思路，并以不同的角度来思考它。

通过避免编写 for 循环，你可以获得什么好处：
- 较少的代码量- 更好的代码可读性- 更少的缩进（对 Python 还是很有意义的）
我们来看一下下面的代码结构：

```
# 1
with ...:
    for ...:
        if ...:
            try:
            except:
        else:
```

在这个例子中，我们正在处理多层嵌套的代码，这很难阅读。这个例子使用了多层嵌套的代码。我在这段代码中发现它无差别使用缩进把管理逻辑（with, try-except）和业务逻辑（for, if）混在一起。如果你遵守只对管理逻辑使用缩进的规范，那么核心业务逻辑应该立刻脱离出来。

"扁平结构比嵌套结构更好" - The Zen of Python

可以使用的已有的工具来替换 for 循环

**1.List Comprehension / Generator 表达式**

我们来看一个简单的例子。如果你想将一个数组转换为另一个数组：

```
result = []
for item in item_list:
    new_item = do_something_with(item)
    result.append(item)
```

如果你喜欢 MapReduce，你也可以使用 map，或者 Python 中的 List Comprehension：

```
result = [do_something_with(item) for item in item_list]
```

同样，如果您只想迭代数组中的元素，也可以使用一样的代码 Generator Expression。result = (do_something_with(item) for item in item_list)

**2.函数**

如果您想要将一个数组映射成另外数组，只需调用 map 函数，就可以用一个更高级、更实用的编程方式解决这个问题。

```
doubled_list = map(lambda x: x * 2, old_list)
```

如果要将序列减少为单个，请使用 reduce

```
from functools import reduce
summation = reduce(lambda x, y: x + y, numbers)
```

另外，许多 Python 内置函数都会使用 iterables：

```
&gt;&gt;&gt; a = list(range(10))
&gt;&gt;&gt; a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
&gt;&gt;&gt; all(a)
False
&gt;&gt;&gt; any(a)
True
&gt;&gt;&gt; max(a)
9
&gt;&gt;&gt; min(a)
0
&gt;&gt;&gt; list(filter(bool, a))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
&gt;&gt;&gt; set(a)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
&gt;&gt;&gt; dict(zip(a,a))
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
&gt;&gt;&gt; sorted(a, reverse=True)
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
&gt;&gt;&gt; str(a)
'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'
&gt;&gt;&gt; sum(a)
45
```

**3.Extract Functions or Generators**

上述两种方法是很好的处理更简单的逻辑。更复杂的逻辑怎么样？作为程序员，我们编写函数来抽离出复杂的业务。相同的想法适用于此。如果你是这样写的：

```
results = []
for item in item_list:
    # setups
    # condition
    # processing
    # calculation
    results.append(result)
```

显然你对一个代码块添加了太多的责任。相反，我建议你做：

```
def process_item(item):
    # setups
    # condition
    # processing
    # calculation
    return result


results = [process_item(item) for item in item_list]
```

如果换成嵌套函数会如何

```
results = []
for i in range(10):
    for j in range(i):
        results.append((i, j))
```

换成 List Comprehension 来实现是这样的：

```
results = [(i, j)
           for i in range(10)
           for j in range(i)]
```

如果你的代码块需要记录一些内部状态

```
# finding the max prior to the current item
a = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
results = []
current_max = 0
for i in a:
    current_max = max(i, current_max)
    results.append(current_max)


# results = [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]
```

我们使用 generator 来实现这一点：

```
def max_generator(numbers):
    current_max = 0
    for i in numbers:
        current_max = max(i, current_max)
        yield current_max


a = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
results = list(max_generator(a))
```

读者可能要问 “等等！你在 generator 中用到 for 循环，作弊啊！别急，再看看下面的代码。

不要自己写。itertools 会帮你实现了

这个模块很简单。我相信这个模块在大多数场景中可以替换你原先的 for 循环。例如，最后一个例子可以重写为：

```
from itertools import accumulate
a = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
resutls = list(accumulate(a, max))
```

另外，如果要迭代组合序列，则需要使用product()， permutations()， combinations()。

**结论**
- 在大多数情况下，您都不需要编写 for 循环。- 你应该避免编写 for 循环，这样会有更好的代码可读性。
推荐阅读  点击标题可跳转
- - - - - - - - 