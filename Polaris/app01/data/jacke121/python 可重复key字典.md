
--- 
title:  python 可重复key字典 
tags: []
categories: [] 

---


如果不用key取value，则list列表也可以。

用字典加value(列表)也可以，遍历需要二级遍历。



使用`collections.defaultdict`来实现一个字典，其中键可以关联多个值的增删改查操作非常直观。以下是一个简单的例子，展示了如何对这种数据结构进行基本的操作：

#### 初始化和增加元素

pythonCopy code

```
from collections import defaultdict 
d = defaultdict(list) # 增加元素 
d["key"].append("value1") 
d["key"].append("value2")
d[1].append(2)
```

#### 查询元素

```
# 查询键对应的所有值 
print(d["key"]) 
# 输出：['value1', 'value2']
# 查询不存在的键，将返回一个空列表，而不是抛出异常 
print(d["unknown_key"]) # 输出：[]
```

#### 修改元素

pythonCopy code

`# 修改指定键的某个值（这里修改第一个值） if d["key"]: d["key"][0] = "new_value1" print(d["key"]) # 输出：['new_value1', 'value2'] `

#### 删除元素

##### 删除键对应的一个值

pythonCopy code

`# 删除键对应的一个值（这里删除第一个值） if d["key"]: d["key"].pop(0) # 或者 d["key"].remove("new_value1") 如果你知道要删除的具体值 print(d["key"]) # 输出：['value2'] `

##### 删除整个键

pythonCopy code

`# 删除整个键及其对应的所有值 del d["key"] # 尝试访问已删除的键，将返回一个空列表 print(d["key"]) # 输出：[] `

#### 检查键是否存在

pythonCopy code

`# 检查键是否存在 if "key" in d: print("Key exists") else: print("Key does not exist") `

#### 遍历字典

pythonCopy code

`# 添加更多元素进行演示 d["key1"].append("value11") d["key2"].append("value21") d["key2"].append("value22") # 遍历字典 for key, values in d.items(): print(f"{key}: {values}") `

这个例子展示了如何使用`defaultdict(list)`来管理一个键对应多个值的情况，并执行了增删改查等基本操作。这种数据结构非常适合需要将多个值关联到同一个键的场景。
