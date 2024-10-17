
--- 
title:  Python 的 random 模块 
tags: []
categories: [] 

---
真正意义上的随机数（或者随机事件）在某次产生过程中是按照实验过程中表现的分布概率随机产生的，其结果是不可预测的，是不可见的。而计算机中的随机函数是按照一定算法模拟产生的，其结果是确定的，是可见的。我们可以这样认为这个可预见的结果其出现的概率是100%。所以用计算机随机函数所产生的“随机数”并不随机，是伪随机数。

计算机的伪随机数是由随机种子根据一定的计算方法计算出来的数值。所以，只要计算方法一定，随机种子一定，那么产生的随机数就是固定的。

只要用户或第三方不设置随机种子，那么在默认情况下随机种子来自系统时钟。Python 的这个库在底层使用通用的算法，经过长久的考验，可靠性没得说，但绝对不能用于密码相关的功能。如果要用于密码相关的功能，请使用 secret 模块， 模块可用于生成高加密强度的随机数，适应管理密码、账户验证、安全凭据和相关机密数据管理的需要。

### random.seed()

初始化随机数生成器。如果 **a** 被省略或为 `None` ，则使用当前系统时间。 如果操作系统提供随机源，则使用它们而不是系统时间。如果 **a** 是 int 类型，则直接使用。随机种子最直接的感受是：**只要计算方法一定，随机种子一定，那么产生的随机数就是固定的（这也是它不能用于密码相关功能的原因之一）**，例如：

```
&gt;&gt;&gt; random.seed(10)
&gt;&gt;&gt; random.randint(0, 10)
9
&gt;&gt;&gt; random.randint(0, 10)
0
&gt;&gt;&gt; random.randint(0, 10)
6

&gt;&gt;&gt; random.seed(10)
&gt;&gt;&gt; random.randint(0, 10)
9
&gt;&gt;&gt; random.randint(0, 10)
0
&gt;&gt;&gt; random.randint(0, 10)
6

&gt;&gt;&gt; random.seed()
&gt;&gt;&gt; random.randint(0, 10)
2
&gt;&gt;&gt; random.randint(0, 10)
10
&gt;&gt;&gt; random.randint(0, 10)
8

```

可以很明显地观察到，在设置了相同的随机种子以后，使用 random.randint(0, 10) 生成的随机数序列和之前是一样的。

### random.getstate()

返回捕获生成器当前内部状态的对象。 这个对象可以传递给  来恢复状态。

### random.setstate(state)

传入一个先前利用getstate方法获得的状态对象，使得生成器恢复到这个状态。

### random.getrandbits(k)

返回一个不大于 k 位的 Python 整数（十进制），比如 k=10，则结果在0~2^10之间的整数（转换成二进制的字符串以后，长度不超过 k）。

```
&gt;&gt;&gt; random.getrandbits(5)
18
```

直接看整数的结果可能看不出来位长度方面的差异，用 bin 转换成二进制的时候就直观多了：

```
&gt;&gt;&gt; bin(random.getrandbits(5))[2:]
'1101'
&gt;&gt;&gt; bin(random.getrandbits(5))[2:]
'1111'
&gt;&gt;&gt; bin(random.getrandbits(5))[2:]
'10010'

```

### random.randrange(stop)

从 range(stop) 返回一个随机选择的元素，这相当于 choice(range(stop))

```
&gt;&gt;&gt; random.randrange(10)
3
&gt;&gt;&gt; random.randrange(10)
7
&gt;&gt;&gt; random.randrange(10)
4

```

### random.randrange(start, stop[, step])

从 `range(start, stop, step)` 返回一个随机选择的元素。 这相当于 `choice(range(start, stop, step))`

```
&gt;&gt;&gt; random.randrange(5, 10, 2)
9
&gt;&gt;&gt; random.randrange(5, 10, 2)
5
&gt;&gt;&gt; random.randrange(5, 10, 2)
5

```

### random.randint(a, b)

返回随机整数 **N** 满足 `a &lt;= N &lt;= b`。相当于 `randrange(a, b+1)`。

```
&gt;&gt;&gt; random.randint(5, 10)
5
&gt;&gt;&gt; random.randint(5, 10)
6
&gt;&gt;&gt; random.randint(5, 10)
10

```

### random.choice(seq)

从非空序列 **seq** 返回一个随机元素。 如果 **seq** 为空，则引发 。

```
&gt;&gt;&gt; random.choice([])
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib64/python3.6/random.py", line 260, in choice
    raise IndexError('Cannot choose from an empty sequence') from None
IndexError: Cannot choose from an empty sequence
&gt;&gt;&gt; random.choice([1, 0])
0
&gt;&gt;&gt; random.choice([1, 0])
1

```

### random.choices(population, weights=None, *, cum_weights=None, k=1)

从 population 中选择替换，返回大小为 **k** 的元素列表。 如果 **population** 为空，则引发 。同时可以设置 population 的权重 weights。

```
&gt;&gt;&gt; 
&gt;&gt;&gt; random.choices([1, 2, 3, 4, 5], [0, 1, 2, 3, 4], k=2)
[4, 2]
&gt;&gt;&gt; random.choices([1, 2, 3, 4, 5], [0, 1, 2, 3, 4], k=2)
[4, 5]

```

### random.shuffle(x)

将序列 **x** 随机打乱位置（洗牌）。

```
&gt;&gt;&gt; x = [1, 2, 3, 4, 5]
&gt;&gt;&gt; random.shuffle(x)
&gt;&gt;&gt; x
[3, 2, 1, 5, 4]

```

### random.sample(population, k)

返回从总体序列或集合中选择的唯一元素的 **k** 长度列表。 用于无重复的随机抽样。

```
&gt;&gt;&gt; random.sample([1, 2, 3, 4, 5], 3)
[5, 4, 3]
&gt;&gt;&gt; random.sample([1, 2, 3, 4, 5], 4)
[4, 1, 5, 2]
&gt;&gt;&gt; random.sample([1, 2, 3, 4, 5], 5)
[4, 5, 1, 2, 3]

```

### random.random()

返回 [0.0, 1.0) 范围内的下一个随机浮点数。

```
&gt;&gt;&gt; random.random()
0.5386670484231432

```

### random.uniform(a, b)

返回一个随机浮点数 **N** ，当 `a &lt;= b` 时 `a &lt;= N &lt;= b` ，当 `b &lt; a` 时 `b &lt;= N &lt;= a` 。

取决于等式 `a + (b-a) * random()` 中的浮点舍入，终点 `b` 可以包括或不包括在该范围内。

```
&gt;&gt;&gt; random.uniform(5, 4)
4.5101042412090635
&gt;&gt;&gt; random.uniform(5, 4)
4.834203559467793
&gt;&gt;&gt; random.uniform(5, 4)
4.558653182546412
&gt;&gt;&gt; random.uniform(4, 5)
4.9686781985609425
&gt;&gt;&gt; random.uniform(4, 5)
4.415173693217833
&gt;&gt;&gt; random.uniform(4, 5)
4.035317829787831

```

### 常见的字符串常量

```
&gt;&gt;&gt; string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
&gt;&gt;&gt; string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
&gt;&gt;&gt; string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
&gt;&gt;&gt; string.digits
'0123456789'
&gt;&gt;&gt; string.hexdigits
'0123456789abcdefABCDEF'
&gt;&gt;&gt; string.octdigits
'01234567'
&gt;&gt;&gt; string.printable
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&amp;\'()*+,-./:;&lt;=&gt;?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
&gt;&gt;&gt; string.whitespace
' \t\n\r\x0b\x0c'

```


