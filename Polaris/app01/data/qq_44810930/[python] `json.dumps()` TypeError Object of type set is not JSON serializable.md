
--- 
title:  [python] `json.dumps()` TypeError: Object of type set is not JSON serializable 
tags: []
categories: [] 

---
在Python中，当你尝试将一个集合（set）类型的对象转换为JSON格式时，可能会遇到“TypeError: Object of type set is not JSON serializable”的错误。这是因为标准的JSON格式不支持Python中的集合类型，JSON格式支持的数据类型包括：对象（字典）、数组、字符串、数字、布尔值和null。

为了解决这个问题，你可以采取以下几种方法：

#### 1. 将集合转换为列表

由于JSON支持列表（数组），你可以先将集合转换为列表，然后再进行序列化。这是最简单直接的方法。

```
import json

my_set = {<!-- -->1, 2, 3}
# 将集合转换为列表
my_list = list(my_set)

# 序列化列表
json_data = json.dumps(my_list)
print(json_data)

```

#### 2. 使用自定义编码器

如果你需要频繁地处理集合和其他不直接支持的类型，可以考虑实现一个自定义的JSON编码器。通过继承`json.JSONEncoder`类，并重写`default`方法来实现。

```
import json

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)  # 将集合转换为列表
        return json.JSONEncoder.default(self, obj)

my_set = {<!-- -->1, 2, 3}

# 使用自定义编码器
json_data = json.dumps(my_set, cls=SetEncoder)
print(json_data)

```

#### 3. 使用`default`参数

`json.dumps()`方法接受一个`default`参数，该参数可以是一个函数，用于处理无法直接序列化的对象。这提供了一种快速自定义序列化方式，而不需要定义一个新的编码器类。

```
import json

my_set = {<!-- -->1, 2, 3}

# 使用default参数提供的函数处理集合
json_data = json.dumps(my_set, default=lambda o: list(o) if isinstance(o, set) else o)
print(json_data)

```

#### 结论

在处理“TypeError: Object of type set is not JSON serializable”错误时，最简单的解决方案是将集合转换为列表。对于更复杂的情况或者需要支持多种特殊类型，实现自定义编码器或使用`default`参数提供的函数是更灵活的选择。
