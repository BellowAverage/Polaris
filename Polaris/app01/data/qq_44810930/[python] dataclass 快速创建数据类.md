
--- 
title:  [python] dataclass 快速创建数据类 
tags: []
categories: [] 

---
在Python中，dataclass是一种用于快速创建数据类的装饰器和工具。自Python 3.7起，通过标准库中的dataclasses模块引入。它的主要目的是简化定义类来仅存储数据的代码量。通常，这样的类包含多个初始化属性，但没有复杂的方法（尽管你可以添加方法）。使用dataclass装饰器，Python会自动为你生成一些特殊方法，如`__init__()、__repr__()、__eq__()`等。

#### 定义数据类

```
from dataclasses import dataclass, asdict
import json

@dataclass
class Address:
    street: str
    city: str

@dataclass
class User:
    name: str
    age: int
    email: str
    address: Address  # User 包含一个 Address 类型的属性

```

#### 转换为JSON

由于`Address`也是一个`@dataclass`，使用`asdict()`将`User`实例转换为字典时，`Address`实例也会被递归地转换为字典。因此，整个转换过程相对直接：

```
user = User(name="John Doe", age=30, email="john.doe@example.com",
            address=Address(street="123 Elm Street", city="Gotham"))

# 将数据类实例转换为字典，包括嵌套的数据类
user_dict = asdict(user)

# 将字典转换为JSON字符串
user_json = json.dumps(user_dict)

print(user_json)

```

#### 处理复杂或特殊类型

如果你的数据类包含不能直接被`json.dumps()`处理的复杂或特殊类型（如日期时间对象），你可以通过提供一个自定义的处理函数给`json.dumps()`的`default`参数来解决这个问题。例如，如果`User`包含一个`datetime`类型的生日属性，你可以这样做：

```
from datetime import datetime

@dataclass
class User:
    name: str
    age: int
    email: str
    address: Address
    birthday: datetime  # 假设我们添加了一个 datetime 类型的属性

def datetime_converter(o):
    if isinstance(o, datetime):
        return o.__str__()

user = User(name="John Doe", age=30, email="john.doe@example.com",
            address=Address(street="123 Elm Street", city="Gotham"),
            birthday=datetime(1990, 1, 1))

user_dict = asdict(user)

# 使用 default 参数处理 datetime 对象
user_json = json.dumps(user_dict, default=datetime_converter)

print(user_json)

```

通过这种方式，你可以灵活地将包含嵌套`@dataclass`属性甚至更复杂类型的数据类实例转换成JSON格式。



#### 文章目录
- <ul><li><ul><li>- - - - - - 


#### `dataclasses`模块中的重要函数

除了自动生成的方法外，`dataclasses`模块还提供了一些有用的函数来处理数据类：
1.  **`fields(class_or_instance)`**： 返回一个包含数据类的所有`Field`对象的元组，每个`Field`对象包含关于字段的信息，如名称、类型和默认值。 1.  **`asdict(instance, *, dict_factory=dict)`**： 将数据类实例转换为字典。这对于将数据类实例序列化为JSON非常有用。 1.  **`astuple(instance, *, tuple_factory=tuple)`**： 将数据类实例转换为元组。这在需要将数据类实例与其他基于元组的APIs交互时很有用。 1.  **`is_dataclass(obj)`**： 检查一个对象是否是数据类或其实例。 1.  **`replace(instance, **changes)`**： 创建一个新的数据类实例，其中包含通过`changes`指定的字段值更改。这在`frozen=True`（即不可变数据类）的情况下特别有用，因为你不能直接修改字段值。 
#### 示例

```
from dataclasses import dataclass, asdict, astuple, replace

@dataclass
class Point:
    x: int
    y: int

p = Point(10, 20)
print(p)  # 输出: Point(x=10, y=20)

p_dict = asdict(p)
print(p_dict)  # 输出: {'x': 10, 'y': 20}

p_tuple = astuple(p)
print(p_tuple)  # 输出: (10, 20)

p_new = replace(p, x=100)
print(p_new)  # 输出: Point(x=100, y=20)

```

通过使用`dataclass`，Python程序员可以更加专注于数据的逻辑，而不是编写重复的方法代码，大大提高了开发效率和代码的可读性。

#### `Field`对象

`Field`对象是`dataclasses`模块定义的一个类，它包含以下主要属性：
- `name`：字符串，字段的名称。- `type`：字段的类型，使用类型注解指定。- `default`：字段的默认值。如果字段没有默认值，则此属性为`dataclasses._MISSING_TYPE`。- `default_factory`：用于生成字段默认值的工厂函数。如果字段没有默认工厂，则此属性为`dataclasses._MISSING_TYPE`。- `init`：一个布尔值，指示是否在自动生成的`__init__`方法中包含该字段。- `repr`：一个布尔值，指示是否在自动生成的`__repr__`方法中包含该字段。- `compare`：一个布尔值，指示是否在比较方法中包含该字段（如`__eq__`）。- `hash`：一个布尔值或`None`，指示是否在计算哈希值时包含该字段。- `metadata`：一个映射，包含字段的元数据。这是在定义字段时通过`metadata`参数传递的任意字典。
#### 使用`fields()`函数的示例

```
from dataclasses import dataclass, field, fields

@dataclass
class Person:
    name: str
    age: int = field(default=18, metadata={<!-- -->"description": "Age of the person"})
    is_student: bool = False

# 获取Person数据类的字段信息
for f in fields(Person):
    print(f"name={<!-- -->f.name}, type={<!-- -->f.type}, default={<!-- -->f.default}, metadata={<!-- -->f.metadata}")

# 输出示例：
# name=name, type=&lt;class 'str'&gt;, default=&lt;dataclasses._MISSING_TYPE object at 0x...&gt;, metadata={}
# name=age, type=&lt;class 'int'&gt;, default=18, metadata={'description': 'Age of the person'}
# name=is_student, type=&lt;class 'bool'&gt;, default=False, metadata={}

```

在这个示例中，我们定义了一个`Person`数据类，并使用`fields()`函数遍历其字段，打印出每个字段的名称、类型、默认值和元数据。这种方式特别有用于动态地处理数据类字段，例如在序列化或验证场景中。
