
--- 
title:  python中 map函数 的使用 
tags: []
categories: [] 

---
## 1. 概念

map函数也是python中的一个内置函数，用法同之前讲过的filter函数类似。map在这里的意思是映射的意思，会根据提供的函数对指定序列做映射。

map函数会返回一个迭代器，如果要转换为列表，可以使用 list() 来转换。

## 2. 语法

```
map(function, iterable)

&gt; function -- 函数
&gt; iterable -- 序列

```

map函数的第一个参数是一个函数，第二个参数是一个序列，里面的每个元素作为函数的参数进行计算和判断。函数返回值则被作为新的元素存储起来。

## 3. 示例

```
def add(x):
    return x**2			#计算x的平方

lists = range(11)       #创建包含 0-10 的列表
a = map(add,lists)      #计算 0-10 的平方，并映射
print(a)                # 返回一个迭代器：&lt;map object at 0x0000025574F68F70&gt;
print(list(a))          # 使用 list() 转换为列表。结果为：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 使用lambda匿名函数的形式复现上面的代码会更简洁一些
print(list(map(lambda x:x**2,range(11))))   # 结果为：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

```

**以上就是对于python中 map函数 的理解，如有补充和建议请评论区留言，共同进步，感谢！**
