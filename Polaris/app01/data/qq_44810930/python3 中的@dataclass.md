
--- 
title:  python3 中的@dataclass 
tags: []
categories: [] 

---
`@dataclass` 是 Python 3.7 引入的一个装饰器，用于方便地定义符合数据类协议的类。数据类是一种只包含数据的简单类，通常用于存储数据而不包含任何业务逻辑。

使用 `@dataclass` 装饰器可以自动为类生成各种方法，例如 `__init__()`、`__repr__()`、`__eq__()` 等，这样可以更方便地创建和操作数据类。

以下是一个简单的使用 `@dataclass` 装饰器的示例代码：

```
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str

```

在这个示例中，我们定义了一个名为 `Person` 的数据类，并使用 `@dataclass` 装饰器来修饰该类。该类有三个属性：`name`、`age` 和 `city`。由于使用了 `@dataclass` 装饰器，Python 会自动生成构造函数、`__repr__()` 方法等。

你可以通过以下方式使用 `Person` 类：

```
person = Person(name="Alice", age=28, city="Beijing")
print(person)  # 输出: Person(name='Alice', age=28, city='Beijing')

```

在这个示例中，我们创建了一个 `Person` 对象，并打印其字符串表示形式。由于 Python 自动生成了 `__repr__()` 方法，因此打印结果显示了对象的属性值。

```
from dataclasses import dataclass, field

@dataclass
class Result:
    sub: dict = field(default_factory=dict)

```

`sub: dict = field(default_factory=dict)` 这一行定义了一个类属性 sub，类型为 dict，并使用 `field` 函数指定使用 dict 类型，并设置默认工厂函数为 dict()，即创建一个空字典。

field 是 dataclasses 模块提供的一个函数，用于定义数据类（data class）中属性的元数据。field 函数可以帮助我们对属性进行更精细的设置和配置。

具体来说，`field 函数`有几个常用的参数可以使用：
- default: 指定属性的默认值。- default_factory: 指定一个工厂函数，用来生成属性的默认值。- init: 控制属性是否出现在 `__init__ `方法中，如果设置为 False，则不会被包含在构造函数参数列表中。- repr: 控制属性在 repr 字符串中的显示方式。- compare: 控制属性是否参与对象比较。- hash: 控制属性是否参与对象哈希计算。
在上面的代码中，field(default_factory=dict) 的作用是定义了一个属性，并设置了默认工厂函数为 dict()，

这意味着每次创建一个新的 AsyncCallResult 对象时，该属性都会被初始化为一个空字典。

总的来说，field 函数让我们可以更加灵活地定义数据类属性的行为，使得数据类的使用更加方便和简洁。
