
--- 
title:  10个 Python 高效编程小技巧 
tags: []
categories: [] 

---
<img alt="" src="https://img-blog.csdnimg.cn/img_convert/51c0ff1d5065f4f4d7acf9513e3cef4f.webp?x-oss-process=image/format,png">

初识Python语言，觉得python满足了你上学时候对编程语言的所有要求。python语言的高效编程技巧让那些曾经苦逼学了四年c或者c++的人，兴奋的不行不行的，终于解脱了。高级语言，如果做不到这样，还扯啥高级呢？

**01 交换变量**

```
&gt;&gt;&gt;a=3

&gt;&gt;&gt;b=6
复制代码
```

这个情况如果要交换变量在c++中，肯定需要一个空变量。但是python不需要，只需一行，大家看清楚了

```
&gt;&gt;&gt;a,b=b,a

&gt;&gt;&gt;print(a)&gt;&gt;&gt;6

&gt;&gt;&gt;ptint(b)&gt;&gt;&gt;5
复制代码
```

**02 字典推导(Dictionary comprehensions)和集合推导(Set comprehensions)**

大多数的Python程序员都知道且使用过列表推导(list comprehensions)。如果你对list comprehensions概念不是很熟悉——一个list comprehension就是一个更简短、简洁的创建一个list的方法。

```
&gt;&gt;&gt; some_list = [1, 2, 3, 4, 5]

&gt;&gt;&gt; another_list = [ x + 1 for x in some_list ]

&gt;&gt;&gt; another_list
[2, 3, 4, 5, 6]
复制代码
```

自从python 3.1 起，我们可以用同样的语法来创建集合和字典表：

```
&gt;&gt;&gt; # Set Comprehensions
&gt;&gt;&gt; some_list = [1, 2, 3, 4, 5, 2, 5, 1, 4, 8]

&gt;&gt;&gt; even_set = { x for x in some_list if x % 2 == 0 }

&gt;&gt;&gt; even_set
set([8, 2, 4])

&gt;&gt;&gt; # Dict Comprehensions

&gt;&gt;&gt; d = { x: x % 2 == 0 for x in range(1, 11) }

&gt;&gt;&gt; d
{1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False, 10: True}
复制代码
```

在第一个例子里，我们以some_list为基础，创建了一个具有不重复元素的集合，而且集合里只包含偶数。而在字典表的例子里，我们创建了一个key是不重复的1到10之间的整数，value是布尔型，用来指示key是否是偶数。这里另外一个值得注意的事情是集合的字面量表示法。我们可以简单的用这种方法创建一个集合：

```
&gt;&gt;&gt; my_set = {1, 2, 1, 2, 3, 4}

&gt;&gt;&gt; my_set
set([1, 2, 3, 4])
复制代码
```

而不需要使用内置函数set()。

**03 计数时使用Counter计数对象**

这听起来显而易见，但经常被人忘记。对于大多数程序员来说，数一个东西是一项很常见的任务，而且在大多数情况下并不是很有挑战性的事情——这里有几种方法能更简单的完成这种任务。

Python的collections类库里有个内置的dict类的子类，是专门来干这种事情的：

```
&gt;&gt;&gt; from collections import Counter
&gt;&gt;&gt; c = Counter( hello world )

&gt;&gt;&gt; c
Counter({ l : 3,  o : 2,    : 1,  e : 1,  d : 1,  h : 1,  r : 1,  w : 1})

&gt;&gt;&gt; c.most_common(2)
[( l , 3), ( o , 2)]
复制代码
```

**04 漂亮的打印出JSON**

JSON是一种非常好的数据序列化的形式，被如今的各种API和web service大量的使用。使用python内置的json处理，可以使JSON串具有一定的可读性，但当遇到大型数据时，它表现成一个很长的、连续的一行时，人的肉眼就很难观看了。

为了能让JSON数据表现的更友好，我们可以使用indent参数来输出漂亮的JSON。当在控制台交互式编程或做日志时，这尤其有用：

```
&gt;&gt;&gt; import json

&gt;&gt;&gt; print(json.dumps(data))  # No indention
{"status": "OK", "count": 2, "results": [{"age": 27, "name": "Oz", "lactose_intolerant": true}, {"age": 29, "name": "Joe", "lactose_intolerant": false}]}

&gt;&gt;&gt; print(json.dumps(data, indent=2))  # With indention

{
  "status": "OK",
  "count": 2,
  "results": [

    {
      "age": 27,
      "name": "Oz",

      "lactose_intolerant": true
    },
    {
      "age": 29,

      "name": "Joe",
      "lactose_intolerant": false
    }
  ]

}
复制代码
```

同样，使用内置的pprint模块，也可以让其它任何东西打印输出的更漂亮。

**05 解决FizzBuzz**

前段时间Jeff Atwood 推广了一个简单的编程练习叫FizzBuzz，问题引用如下：

写一个程序，打印数字1到100，3的倍数打印“Fizz”来替换这个数，5的倍数打印“Buzz”，对于既是3的倍数又是5的倍数的数字打印“FizzBuzz”。

这里就是一个简短的，有意思的方法解决这个问题：

```
for x in range(1,101):
    print"fizz"[x%3*len( fizz )::]+"buzz"[x%5*len( buzz )::] or x
    
06 if 语句在行内

print "Hello" if True else "World"
&gt;&gt;&gt; Hello
复制代码
```

**07 连接**

下面的最后一种方式在绑定两个不同类型的对象时显得很cool。

```
nfc = ["Packers", "49ers"]
afc = ["Ravens", "Patriots"]
print nfc + afc
&gt;&gt;&gt; [ Packers ,  49ers ,  Ravens ,  Patriots ]

print str(1) + " world"
&gt;&gt;&gt; 1 world

print `1` + " world"
&gt;&gt;&gt; 1 world

print 1, "world"
&gt;&gt;&gt; 1 world
print nfc, 1
&gt;&gt;&gt; [ Packers ,  49ers ] 1
复制代码
```

**08 数值比较**

这是我见过诸多语言中很少有的如此棒的简便法

```
x = 2
if 3 &gt; x &gt; 1:
   print x
&gt;&gt;&gt; 2
if 1 &lt; x &gt; 0:
   print x
&gt;&gt;&gt; 2
复制代码
```

**09 同时迭代两个列表**

```
nfc = ["Packers", "49ers"]
afc = ["Ravens", "Patriots"]
for teama, teamb in zip(nfc, afc):
     print teama + " vs. " + teamb
&gt;&gt;&gt; Packers vs. Ravens
&gt;&gt;&gt; 49ers vs. Patriots
复制代码
```

**10 带索引的列表迭代**

```
teams = ["Packers", "49ers", "Ravens", "Patriots"]
for index, team in enumerate(teams):
    print index, team
&gt;&gt;&gt; 0 Packers
&gt;&gt;&gt; 1 49ers
&gt;&gt;&gt; 2 Ravens
&gt;&gt;&gt; 3 Patriots
```

 
