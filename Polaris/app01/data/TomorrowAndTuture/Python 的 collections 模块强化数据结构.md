
--- 
title:  Python 的 collections 模块强化数据结构 
tags: []
categories: [] 

---
collections 是 Python 内建的一个集合模块，提供了许多有用的集合类。包括许多常见的强化数据结构类。至于为什么会出现强化数据结构，自然是因为一般的 元组、字典等可能不太满足一些特定的需要。

## Counter

### 列表元素统计

普通实现

```
&gt;&gt;&gt; word_list = ["a", "b", "c", "c", "a", "a"]
&gt;&gt;&gt; cnt = {}
&gt;&gt;&gt; for word in set(word_list):
...     cnt[word] = word_list.count(word)
... 
&gt;&gt;&gt; cnt
{'b': 1, 'c': 2, 'a': 3}
&gt;&gt;&gt; cnt['d']
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
KeyError: 'd'

```

Counter 实现 

```
&gt;&gt;&gt; from collections import Counter
&gt;&gt;&gt; cnt = Counter()
&gt;&gt;&gt; word_list = ['a', 'b', 'c', 'c', 'a', 'a']
&gt;&gt;&gt; for word in word_list:
...     cnt[word] += 1
... 
&gt;&gt;&gt; cnt
Counter({'a': 3, 'c': 2, 'b': 1})
&gt;&gt;&gt; cnt['a']
3
&gt;&gt;&gt; cnt['d'] # 即使没有 key，也不会报 KeyError 哟，这点和 defaultdict(int) 比较像。
0

```

### 字符串字符统计

普通实现

```
&gt;&gt;&gt; word_str = 'hello world'
&gt;&gt;&gt; word_list = list(word_str)
&gt;&gt;&gt; cnt = {}
&gt;&gt;&gt; for word in set(word_list):
...     cnt[word] = word_list.count(word)
... 
&gt;&gt;&gt; cnt
{'e': 1, 'd': 1, 'h': 1, 'o': 2, 'l': 3, ' ': 1, 'r': 1, 'w': 1}

```

Counter 实现

```
&gt;&gt;&gt; from collections import Counter
&gt;&gt;&gt; word_str = 'hello world'
&gt;&gt;&gt; cnt = Counter(word_str)
&gt;&gt;&gt; cnt
Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

&gt;&gt;&gt; Counter({'red': 4, 'blue': 2})
Counter({'red': 4, 'blue': 2})
&gt;&gt;&gt; Counter(red=4, blue=2)
Counter({'red': 4, 'blue': 2})

```

### Counter.elements()

```
&gt;&gt;&gt; cnt = Counter(red=4, blue=2)
&gt;&gt;&gt; cnt
Counter({'red': 4, 'blue': 2})
&gt;&gt;&gt; list(cnt.elements())
['red', 'red', 'red', 'red', 'blue', 'blue']

```

### Counter.most_common()

```
&gt;&gt;&gt; cnt = Counter('hello world')
&gt;&gt;&gt; cnt
Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
&gt;&gt;&gt; cnt.most_common()
[('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
&gt;&gt;&gt; cnt.most_common(3)
[('l', 3), ('o', 2), ('h', 1)]

```

### Counter.subtract()

```
&gt;&gt;&gt; a = Counter(a=4, b=2, c=0, d=-2)
&gt;&gt;&gt; a
Counter({'a': 4, 'b': 2, 'c': 0, 'd': -2})
&gt;&gt;&gt; b = Counter(a=1, b=2, c=-3, d=4)
&gt;&gt;&gt; b
Counter({'d': 4, 'b': 2, 'a': 1, 'c': -3})
&gt;&gt;&gt; a.subtract(b)
&gt;&gt;&gt; a
Counter({'a': 3, 'c': 3, 'b': 0, 'd': -6})

```

### 常用操作

其实转换成 Counter 类型以后，操作和字典差不多。

```
&gt;&gt;&gt; from collections import Counter
&gt;&gt;&gt; cnt = Counter('hello world')
&gt;&gt;&gt; cnt
Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
&gt;&gt;&gt; cnt.keys()
dict_keys(['h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'])
&gt;&gt;&gt; cnt.values()
dict_values([1, 1, 3, 2, 1, 1, 1, 1])
&gt;&gt;&gt; sum(cnt.values())
11
&gt;&gt;&gt; dict(cnt)
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
&gt;&gt;&gt; cnt.items()
dict_items([('h', 1), ('e', 1), ('l', 3), ('o', 2), (' ', 1), ('w', 1), ('r', 1), ('d', 1)])
&gt;&gt;&gt; Counter(dict([('a', 1), ('b', 2), ('c', 3)]))
Counter({'c': 3, 'b': 2, 'a': 1})
&gt;&gt;&gt; cnt.clear()
&gt;&gt;&gt; cnt
Counter()

```

## deque

deque 是栈和队列的一种广义实现，俗称双端队列。有效内存地以近似 O(1) 的性能在 deque 的两端插入和删除元素，尽管 list 也支持相似的操作，但是在 pop(0) 和 insert(0,v)（会改变数据的位置和大小）上有O(n)的时间复杂度。如果抛却这些细节不顾的话，你把他当成加强版的 list 好像也没啥毛病。

```
&gt;&gt;&gt; from collections import deque
&gt;&gt;&gt; 
&gt;&gt;&gt; d = deque(['a', 'b', 'c'])
&gt;&gt;&gt; d
deque(['a', 'b', 'c'])
&gt;&gt;&gt; d.append('d')
&gt;&gt;&gt; d
deque(['a', 'b', 'c', 'd'])
&gt;&gt;&gt; d.count('b')
1
&gt;&gt;&gt; d.extend(['e', 'f', 'g'])
&gt;&gt;&gt; d
deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
&gt;&gt;&gt; d.pop()
'g'
&gt;&gt;&gt; d
deque(['a', 'b', 'c', 'd', 'e', 'f'])
&gt;&gt;&gt; d.remove('d')
&gt;&gt;&gt; d
deque(['a', 'b', 'c', 'e', 'f'])
&gt;&gt;&gt; d.reverse()
&gt;&gt;&gt; d
deque(['f', 'e', 'c', 'b', 'a'])

# 队列左端操作
&gt;&gt;&gt; d
deque(['f', 'e', 'c', 'b', 'a'])
&gt;&gt;&gt; d.popleft()
'f'
&gt;&gt;&gt; d
deque(['e', 'c', 'b', 'a'])
&gt;&gt;&gt; d.appendleft('h')
&gt;&gt;&gt; d
deque(['h', 'e', 'c', 'b', 'a'])
&gt;&gt;&gt; d.extendleft(['i', 'j', 'k'])
&gt;&gt;&gt; d
deque(['k', 'j', 'i', 'h', 'e', 'c', 'b', 'a'])
# 想想挖掘机的履带，rotate 就不难理解了
&gt;&gt;&gt; d.rotate(1)
&gt;&gt;&gt; d
deque(['a', 'k', 'j', 'i', 'h', 'e', 'c', 'b'])
&gt;&gt;&gt; d.rotate(2)
&gt;&gt;&gt; d
deque(['c', 'b', 'a', 'k', 'j', 'i', 'h', 'e'])

```

## defaultdict

defaultdict 对我来说最大的特点就是不会出现 KeyError 错误了，我们可以又回到列表元素统计那块来看看。

### 列表元素统计

普通实现

```
&gt;&gt;&gt; word_list = ["a", "b", "c", "c", "a", "a"]
&gt;&gt;&gt; cnt = {}
&gt;&gt;&gt; for word in word_list:
...     if word not in cnt:
...             cnt[word] = 1
...     else:
...             cnt[word] += 1
... 
&gt;&gt;&gt; cnt
{'a': 3, 'b': 1, 'c': 2}

&gt;&gt;&gt; cnt['d']
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
KeyError: 'd'

```

defaultdict 实现（没有用 if else 语句去判断哟）

```
&gt;&gt;&gt; from collections import defaultdict
&gt;&gt;&gt; word_list = ["a", "b", "c", "c", "a", "a"]
&gt;&gt;&gt; cnt = defaultdict(int)
&gt;&gt;&gt; for word in word_list:
...     cnt[word] += 1
... 
&gt;&gt;&gt; cnt
defaultdict(&lt;class 'int'&gt;, {'a': 3, 'b': 1, 'c': 2})

```

## OrderedDict

见闻知意，就是有顺序的字典，好像没啥特别好解释的了。关于 OrderedDict 的实际应用，csv.DictReader 有部分涉及。

```
&gt;&gt;&gt; from collections import OrderedDict
&gt;&gt;&gt; d = {"banana":3,"apple":2,"pear":1,"orange":4}
&gt;&gt;&gt; order_dict = OrderedDict(d)
&gt;&gt;&gt; order_dict
OrderedDict([('banana', 3), ('apple', 2), ('pear', 1), ('orange', 4)])
&gt;&gt;&gt; order_dict.keys()
odict_keys(['banana', 'apple', 'pear', 'orange'])
&gt;&gt;&gt; order_dict.values()
odict_values([3, 2, 1, 4])
&gt;&gt;&gt; order_dict.items()
odict_items([('banana', 3), ('apple', 2), ('pear', 1), ('orange', 4)])

# 从后（前）删除元素
&gt;&gt;&gt; order_dict.popitem(last=True)
('orange', 4)
&gt;&gt;&gt; order_dict
OrderedDict([('banana', 3), ('apple', 2), ('pear', 1)])
&gt;&gt;&gt; order_dict.popitem(last=False)
('banana', 3)
&gt;&gt;&gt; order_dict
OrderedDict([('apple', 2), ('pear', 1)])

# 移动元素到末尾
&gt;&gt;&gt; order_dict
OrderedDict([('apple', 2), ('pear', 1), ('orange', 4)])
&gt;&gt;&gt; order_dict.move_to_end('apple')
&gt;&gt;&gt; order_dict
OrderedDict([('pear', 1), ('orange', 4), ('apple', 2)])

```

## namedtuple

命名元组，其实用数据库中数据表的思想理解比较容易一些：定义后的命名元组就相当于一个数据表，_fields 就相当于数据表的字段，实例化的对象就相当于生成了一条数据记录。

### 定义

```
&gt;&gt;&gt; from collections import namedtuple
&gt;&gt;&gt; User = namedtuple('User', ['name', 'age', 'id'])
&gt;&gt;&gt; User._fields
('name', 'age', 'id')

&gt;&gt;&gt; User = namedtuple('User', 'name age id')
&gt;&gt;&gt; User._fields
('name', 'age', 'id')
```

### 实例化

```
&gt;&gt;&gt; user = User('tester', '22', '12345678')
&gt;&gt;&gt; user
User(name='tester', age='22', id='12345678')

&gt;&gt;&gt; user = User._make(['looking', 25, '12345678'])
&gt;&gt;&gt; user
User(name='looking', age=25, id='12345678')
```

### 属性 

```
&gt;&gt;&gt; user = User._make(['looking', 25, '12345678'])
&gt;&gt;&gt; user.name
'looking'
&gt;&gt;&gt; user.age
25
&gt;&gt;&gt; user.id
'12345678'
```

### 与字典的相互转换 

```
&gt;&gt;&gt; user._asdict()
OrderedDict([('name', 'looking'), ('age', 25), ('id', '12345678')])
&gt;&gt;&gt; user._replace(age=22)
User(name='looking', age=22, id='12345678')

&gt;&gt;&gt; dt = {'name':'looking', 'age':25, 'id':'12345678'}
&gt;&gt;&gt; User(**dt)
User(name='looking', age=25, id='12345678')

```

### 与列表的相互转换 

```
&gt;&gt;&gt; user
User(name='looking', age=25, id='12345678')
&gt;&gt;&gt; list(user)
['looking', 25, '12345678']
&gt;&gt;&gt; User._make(['looking', 25, '12345678'])
User(name='looking', age=25, id='12345678')

```


