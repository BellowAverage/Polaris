
--- 
title:  python update()方法 
tags: []
categories: [] 

---
## python update()方法

Python dict字典 update() 函数把字典 dict2 的键/值对更新到 dict 里。

#### 语法：

```
dict.update(dict2)

```

<mark>注意： 有相同的键会直接替换成 update 的值；</mark>

#### 实例：

```
dict = {<!-- -->'Name': 'Zara', 'Age': 7}
dict2 = {<!-- -->'Sex': 'female'}
dict.update(dict2)
print(dict)  # 结果 {'Name': 'Zara', 'Age': 7, 'Sex': 'female'}

dict = {<!-- -->'Name': 'Zara', 'Age': 7}
dict2 = {<!-- -->'Age': 18, 'Sex': 'female'}
dict.update(dict2)
print(dict)  # 结果 {'Name': 'Zara', 'Age': 18, 'Sex': 'female'}

```
