
--- 
title:  【python】自动生成类的可打印方法(toString,repr) 
tags: []
categories: [] 

---
## dataclass

在 Python 中，可以使用 `dataclasses` 模块来快速生成包含很多属性的类的 `__repr__` 方法。`dataclasses` 模块可以帮助简化类的定义，自动生成 `__init__`、`__repr__` 等方法。

以下是一个示例代码，演示如何使用 `dataclasses` 模块来快速生成包含多个属性的类及其 `__repr__` 方法：

```
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str
    address: str
    phone: str
    # 添加更多属性...

# 创建一个 User 对象
user = User(name='Alice', age=30, email='alice@example.com', address='123 Street', phone='1234567890')

# 调用对象的 __repr__ 方法
print(user)

```

在上面的示例中，通过 `@dataclass` 装饰器将 `User` 类标记为数据类，然后列出类的各个属性。当创建一个 `User` 对象并打印它时，Python 会自动调用生成的 `__repr__` 方法，从而输出对象的信息。

通过使用 `dataclasses` 模块，可以快速生成包含很多属性的类，并且不需要手动编写繁琐的 `__init__` 和 `__repr__` 方法。

## var()函数

通过使用`vars()`函数和字符串插值来生成`__repr__`方法：

```
class User:
    def __init__(self, name, age, email, address, phone):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.phone = phone
        # 添加更多属性...
    
    def __repr__(self):
        attributes = ', '.join(f"{<!-- -->k}={<!-- -->v!r}" for k, v in vars(self).items())
        return f"{<!-- -->self.__class__.__name__}({<!-- -->attributes})"

```

在上述代码中，`__repr__`方法使用了`vars(self)`函数来获取对象的属性字典，然后使用字符串插值将属性和对应的值拼接成一个字符串。最后返回一个以类名和属性字符串组成的格式化字符串作为对象的表示。

在 Python 中，`vars()` 函数是一个内置函数，用于返回对象的 `__dict__` 属性。对于用户定义的类实例，`vars(self)` 返回一个包含实例的所有属性和对应值的字典。

下面是一个简单的示例，演示了如何使用 `vars()` 函数来获取对象的属性和对应的值：

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)

# 使用 vars() 获取实例的属性和对应值
attributes = vars(person)
print(attributes)

```

在这个例子中，我们定义了一个 `Person` 类，该类有 `name` 和 `age` 两个属性。我们创建了一个 `Person` 类的实例 `person`，然后使用 `vars(person)` 函数获取了该实例的所有属性和对应的值，结果将会是一个字典 `{'name': 'Alice', 'age': 30}`。

需要注意的是，`vars()` 函数实际上是调用对象的 `__dict__` 属性来获取属性和值的，因此对于没有 `__dict__` 属性的对象（比如内置类型），`vars()` 函数将会引发 `TypeError` 异常。

总的来说，`vars(self)` 函数是一个方便的工具，可以帮助你获取对象实例的所有属性和对应的值，通常用于调试和动态检查对象的属性。
