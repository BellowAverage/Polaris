
--- 
title:  Python 基础（七）：字典与集合 
tags: []
categories: [] 

---


#### 目录
- - <ul><li>- - - 


## 1 字典

### 1.1 简介

当看到字典这个词时，有些人包括我自己在内，首先映入眼帘的便是新华字典 <img src="https://img-blog.csdnimg.cn/201911160927512.jpg" alt="">

我清楚的记得，刚上小学时老师就让每一个学生准备一本新华字典，它的使用大家也应该都清楚，通过拼音、偏旁部首等进行查询；今天我们说的字典（dict）是 Python 的数据结构，因为都叫字典，我们不用想也知道它们是十分相似的，它们的内容都是以键-值（key-value）的方式存在的。

dict 拥有良好的查询速度，dict 中的值可以是任意 Python 对象，多次对一个 key 赋 value，后面的 value 会把前面的 value 覆盖。

### 1.2 使用

字典的内容在花括号 `{}` 内，键-值（key-value）之间用冒号 `:` 分隔，键值对之间用逗号 `,` 分隔，比如创建字典 d，如下所示：

```
d = {<!-- -->'name':'小明', 'age':'18'}

# 使用 dict 函数
# 方式一
l = [('name', '小明'), ('age', 18)]
d = dict(l)
# 方式二
d = dict(name='小明', age='18')

# 空字典
d = dict()
d = {<!-- -->}

```

字典中的值通过 key 进行访问，如下所示：

```
&gt;&gt;&gt; d = dict(name='小明', age='18')
&gt;&gt;&gt; d['name']
'小明'

# 使用 get 方法
&gt;&gt;&gt; d.get('name')
'小明'

```

修改操作，以修改 age 为例，如下所示：

```
&gt;&gt;&gt; d = dict(name='小明', age='18')
&gt;&gt;&gt; d['age'] = '20'
&gt;&gt;&gt; d['age']
'20'

```

清空集合，如下所示：

```
&gt;&gt;&gt; d = dict(name='小明', age='18')
&gt;&gt;&gt; d.clear()
&gt;&gt;&gt; d
{<!-- -->}

```

获取字典的长度，如下所示：

```
&gt;&gt;&gt; d = dict(name='小明', age='18')
&gt;&gt;&gt; len(d)
2

```

## 2 集合

### 2.1 简介

集合（set）与字典相同均存储 key，但也只存储 key，因 key 不可重复，所以 set 的中的值不可重复，也是无序的。

### 2.2 使用

集合使用花括号 `{}` 或者 `set()` 函数创建，如果创建空集合只能使用 `set()` 函数，以创建集合 s 为例，如下所示：

```
s = {<!-- -->'a', 'b', 'c'}

# 使用 set 函数
s = set(['a', 'b', 'c'])

# 空集合
s = set()

```

集合中重复的元素会被自动过滤掉，如下所示：

```
&gt;&gt;&gt; s = {<!-- -->'a', 'a', 'b', 'c', 'c'}
&gt;&gt;&gt; s
{<!-- -->'a', 'c', 'b'}

```

添加元素可以使用 `add` 或 `update` 方法，如果元素已经存在，则不进行操作，如下所示：

```
&gt;&gt;&gt; s = {<!-- -->'a', 'b', 'c'}
&gt;&gt;&gt; s.add('d')
&gt;&gt;&gt; s
{<!-- -->'a', 'd', 'c', 'b'}
&gt;&gt;&gt; s.update('e')
&gt;&gt;&gt; s
{<!-- -->'a', 'b', 'e', 'd', 'c'}
# 添加已经存在的元素 a
&gt;&gt;&gt; s.add('a')
&gt;&gt;&gt; s
{<!-- -->'a', 'b', 'e', 'd', 'c'}

```

删除元素使用 `remove` 方法，如下所示：

```
&gt;&gt;&gt; s = {<!-- -->'a', 'b', 'c'}
&gt;&gt;&gt; s.remove('c')
&gt;&gt;&gt; s
{<!-- -->'a', 'b'}

```

清空集合使用 `clear` 方法，如下所示：

```
&gt;&gt;&gt; s = {<!-- -->'a', 'b', 'c'}
&gt;&gt;&gt; s.clear()
&gt;&gt;&gt; s
set()

```

获取集合的长度，同样使用 `len` 方法，如下所示：

```
&gt;&gt;&gt; s = {<!-- -->'a', 'b', 'c'}
&gt;&gt;&gt; len(s)
3

```

**欢迎关注文末公众号，免费领取海量学习资料！**

<img src="https://img-blog.csdnimg.cn/20191118111747841.jpg#pic_center" alt="" width="600">
