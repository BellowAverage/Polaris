
--- 
title:  Python 的 itertools 模块 
tags: []
categories: [] 

---
Python 当中的 itertools 模块在程序员中的存在感一直不高，可能是大家真正用到的时候并不多。然而，最近它却成功引起了我的注意，它在  时大放异彩，所以，不妨再来看一看，学一学，不求别的，只求在解决问题的过程当中至少能成功想到它一次。我会把自己觉得很有用的函数标红。

官方还给出了每个方法的实现方式： （既然是标准库，当然官方的文档是最权威且最具有参考性的啦 —— 关键是标题还很霸气）。

### itertools.combinations

求列表的 k 阶子列 （同一个位置的元素子列不允许重复使用），也即求列表的组合 C(n, k)。顺序与原先元素的顺序保持一致。

```
import itertools

input_list = [1, 2, 4, 3, 5]
n = len(input_list)
k = 3
k_subsequence = list(itertools.combinations(input_list, k))
print(k_subsequence)
```

```
[(1, 2, 4), (1, 2, 3), (1, 2, 5), (1, 4, 3), (1, 4, 5), (1, 3, 5), (2, 4, 3), (2, 4, 5), (2, 3, 5), (4, 3, 5)]
```

### itertools.combinations_with_replacement 

求列表的 k 阶子列 （同一个位置的元素子列允许重复使用）。

```
import itertools

input_list = [1, 2, 4, 3, 5]
n = len(input_list)
k = 3
k_subsequence = list(itertools.combinations_with_replacement(input_list, k))
print(k_subsequence)
```

```
[(1, 1, 1), (1, 1, 2), (1, 1, 4), (1, 1, 3), (1, 1, 5), (1, 2, 2), (1, 2, 4), (1, 2, 3), (1, 2, 5), (1, 4, 4), 
(1, 4, 3), (1, 4, 5), (1, 3, 3), (1, 3, 5), (1, 5, 5), (2, 2, 2), (2, 2, 4), (2, 2, 3), (2, 2, 5), (2, 4, 4),
(2, 4, 3), (2, 4, 5), (2, 3, 3), (2, 3, 5), (2, 5, 5), (4, 4, 4), (4, 4, 3), (4, 4, 5), (4, 3, 3), (4, 3, 5),
(4, 5, 5), (3, 3, 3), (3, 3, 5), (3, 5, 5), (5, 5, 5)]

```

### itertools.permutations

返回由迭代元素生成长度为 **k** 的排列。也就是求列表的排列 A(n, k)。

```
import itertools

input_list = [1, 2, 4]
k = 2
print(list(itertools.permutations(input_list, k)))

k = 3
print(list(itertools.permutations(input_list, k)))

```

```
[(1, 2), (1, 4), (2, 1), (2, 4), (4, 1), (4, 2)]
[(1, 2, 4), (1, 4, 2), (2, 1, 4), (2, 4, 1), (4, 1, 2), (4, 2, 1)]
```

### itertools.count

创建一个自定义步长的无限迭代器。（这块感觉和 range 的功能差不多，只不过一般用 range 的时候都是生成一个有限的迭代器）。不过，一般用到无限迭代的情况还真不多，所以可以使用 itertools.takewhile 从无限迭代中取出满足条件的有限迭代。

```
import itertools

start = 2
step = 3
end = 11
counts = itertools.count(start, step)
it = itertools.takewhile(lambda x: x &lt;= 11, counts)
for i in it:
    print(i)
```

```
2
5
8
11
```

### itertools.takewhile

这个感觉和 filter 有点像，但是又不同，看下区别（filter 会对每个迭代元素进行判断，takewhile 碰到第一个不满足条件的元素就退出了，然后返回满足条件的结果）：

```
import itertools

print('takewhile: ', list(itertools.takewhile(lambda x: x &lt; 5, [1, 4, 6, 4, 1])))
print('   filter: ', list(filter(lambda x: x &lt; 5, [1, 4, 6, 4, 1])))

```

```
takewhile:  [1, 4]
   filter:  [1, 4, 4, 1]
```

### itertools.dropwhile

这个刚好和 takewhile 是相反的，dropwhile 也是碰到第一个不满足条件的元素就退出了，但是返回不满足条件的结果：

```
import itertools

print('dropwhile: ', list(itertools.dropwhile(lambda x: x &lt; 5, [1, 4, 6, 4, 1])))
```

```
dropwhile:  [6, 4, 1]

```

### itertools.cycle

创建一个无限循环序列。

```
import itertools

for i in itertools.cycle('abc'):
    print(i)
```

```
a
b
c
a
...
```

### itertools.repeat

创建一个无限重复的迭代（也可以添加参数限制迭代次数）。

```
import itertools

# for i in itertools.repeat('a', 4):
for i in itertools.repeat('a'):
    print(i)

```

```
a
a
a
a
...
```

### itertools.chain

可以把一组迭代对象串联起来，形成一个更大的迭代器。

```
import itertools

for i in itertools.chain('ABC', ('D', 'E'), {'F': 1, 'G': 2}, range(3)):
    print(i)
```

```
import itertools

for i in itertools.chain.from_iterable(['ABC', ('D', 'E'), {'F': 1, 'G': 2}, range(3)]):
    print(i)
```

```
A
B
C
D
E
F
G
0
1
2
```

### itertools.groupby

返回一个产生按照 key 进行分组后的值集合的迭代器。

```
import itertools

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
```

```
A ['A', 'A', 'A']
B ['B', 'B', 'B']
C ['C', 'C']
A ['A', 'A', 'A']
```

**注意：key 是可以重复的**。它只是将相邻元素中具有相同 key 的归为一类，和 dict 里边不能有相同 key 的情况还是不一样的。

```
import itertools

a = ['aa', 'ab', 'abc', 'bcd', 'bc', 'de', 'abcde']
for i, k in itertools.groupby(a, lambda x: len(x)):
    print(i, list(k))

```

```
2 ['aa', 'ab']
3 ['abc', 'bcd']
2 ['bc', 'de']
5 ['abcde']
```

### itertools.zip_longest

这个就没啥多说的了，把它和 zip 放到一块，对比一下输出结果就很容易理解其功效了。

```
import itertools

words = ['nice', 'to', 'meet', 'you']
print(list(zip(*words)))
print(list(itertools.zip_longest(*words)))
```

```
[('n', 't', 'm', 'y'), ('i', 'o', 'e', 'o')]
[('n', 't', 'm', 'y'), ('i', 'o', 'e', 'o'), ('c', None, 'e', 'u'), ('e', None, 't', None)]
```

### itertools.accumulate

这个和 functools 的 reduce 有点像，只不过 reduce 对数组作用之后只返回一个结果，accumulate 则是返回每次迭代过程操作的结果。两个都可以自定义 func ，所以灵活性还是很高的。

```
import itertools

for i in itertools.accumulate([1, 4, 6, 4, 1], func=lambda x, y: x + y):
    print(i)
```

```
from functools import reduce

input_list = [1, 4, 6, 4, 1]
for i in range(len(input_list)):
    print(reduce(lambda x, y: x + y, input_list[:i + 1]))
```

```
1
5
11
15
16
```

### itertools.compress

创建一个迭代器，它返回 **data** 中经 **selectors** 真值测试为 `True` 的元素。迭代器在两者较短的长度处停止。

```
import itertools

data = 'ABCDEFG'
selectors = [1, 0, 1, 0, 1, 1]
print(list(itertools.compress(data, selectors)))
```

```
['A', 'C', 'E', 'F']
```

官方给的实现是下面这种，我还是比较认同的：

```
def compress(data, selectors):
    # compress('ABCDEF', [1,0,1,0,1,1]) --&gt; A C E F
    return (d for d, s in zip(data, selectors) if s)
```

### itertools.product

生成可迭代对象的笛卡儿积。

```
import itertools

first_list = ['a', 'b', 'c', 'd']
second_list = [1, 2, 3]
print(list(itertools.product(first_list, second_list)))

# first_list = ['a', 'b', 'c', 'd']
# second_list = [1, 2, 3]
# third_list = ['X', 'Y']
# print(list(itertools.product(first_list, second_list, third_list)))
# [('a', 1, 'X'), ('a', 1, 'Y'), ('a', 2, 'X'), ('a', 2, 'Y'), ('a', 3, 'X'), ('a', 3, 'Y'), ('b', 1, 'X'), ...]
```

```
[('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3), ('d', 1), ('d', 2), ('d', 3)]
```

### itertools.starmap

这个方法，从我目前做的小测试来看，似乎和 map 就差了个 zip 对数据作用的区别。下面的例子可以做下参考。

pow

```
import itertools

print(list(itertools.starmap(pow, [(2, 5), (3, 2), (10, 3)])))
```

```
import itertools

print(list(itertools.starmap(pow, zip([2, 3, 10], [5, 2, 3]))))
print(list(map(pow, [2, 3, 10], [5, 2, 3])))
```

```
[32, 9, 1000]
```

 int

```
import itertools

print(list(itertools.starmap(int, [(2, ), (3, ), (10, )])))
print(list(itertools.starmap(int, zip([2, 3, 10]))))
print(list(map(int, [2, 3, 10])))
```

```
[2, 3, 10]
```

```
import itertools

print(list(itertools.starmap(int, [('1001', 2), ('0011', 2), ('1011', 2)])))
print(list(itertools.starmap(int, zip(['1001', '0011', '1011'], [2, 2, 2]))))
print(list(map(int, ['1001', '0011', '1011'], [2, 2, 2])))

```

```
[9, 3, 11]
[9, 3, 11]
[9, 3, 11]
```


