
--- 
title:  Python标准数据类型-List(列表) 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主、新星计划第三季python赛道Top1🏆 📃个人主页： 🔥系列专栏： 💬个人格言：不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待💖💖💖 


<img src="https://img-blog.csdnimg.cn/bda67eea8ec641869e3c0abd5ebafe95.gif#pic_center" alt="在这里插入图片描述"> 

#### Python列表最强学习宝典
- - - <ul><li>- - - - - - - - - - - - - - - - - - - - - - 


## ✨序列概述
- 在Python中序列是最基本的数据结构- 序列是一块用于存放多个元素的内存空间- Python中内置了5个常用的序列结构，分别是`列表、字符串、元组、字典、集合`
## 序列的基本操作

### 索引
-  序列中的每一个元素都有一个编号`称为索引(indexing)` -  索引从0开始递增(`下标为0表示第一个元素、下标为1表示第二个元素以此类推`) `如下图所示`： <img src="https://img-blog.csdnimg.cn/fb035d4e954f448b990380eb619c2f2a.png" alt="在这里插入图片描述"> -  索引也可以是负数，从最后一个元素开始计数(`下标为-1表示最后一个元素、下标为-2表示倒数第二个元素以此类推`) `如下图所示`： 
<img src="https://img-blog.csdnimg.cn/f6d10d1d41614594b11a3873a0786ae6.png" alt="在这里插入图片描述">

### 切片

切片操作是访问序列中元素的另一种方法，可以访问一定范围内的元素 实现切片操作的语法格式：`sname[start:end:step]` 参数说明如下： sname：序列的名称 `start`：切片的开始位置(不指定默认为0) `end`：切片的结束位置(不指定默认为序列的长度) `step`：切片的步长(如果省略默认为1，当忽略步长时，最后一个冒号也可以省略)

`实例`：创建一个名为demo的编程语言列表，输出指定的元素

```
demo = ["Python", "Java", "HTML", "CSS", "JavaScript", "Vue"]
print(demo[0:2])  # 获取第1个和第2个元素
print(demo[0:5:2])  # 获取第1、3、5个元素

```

`运行结果如下`：

<img src="https://img-blog.csdnimg.cn/d33236e910314e4399746c3d9d6e2320.png" alt="在这里插入图片描述">

## ✨列表简介

### 创建列表
- `使用赋值运算符创建列表` 同其他类型的Python变量一样，创建列表时，可以使用赋值运算符=直接将一个列表复制给变量 创建列表语法格式：`listname = [element 1,element 2,element 3,...,element n]` 参数说明如下： `listname`：列表名称 `element`：列表中的元素
`实例`：使用`=`创建一个列表

```
demo = ["但行好事", "莫问前程"]

```

`注意事项`： 在创建列表时我们可以将不同数据类型的数据放进同一个列表中，但是通常情况下，我们会在一个列表中只放入一种类型的数据，增加程序的可读性
- `创建空列表` 在Python中，也可以创建空列表，然后再对列表进行一系列操作
`实例`：创建一个名为hacker的空列表

```
hacker = []

```
- 使用list()创建列表 在Python中可以使用list()去创建一个列表 list()语法格式：list(data) 参数说明如下： `data`：可以转换为列表的数据(可以是range对象、字符串、元组或其他可迭代类型的数据)
`实例`：创建一个0~10(不包括10)的所有偶数的列表

```
demo = list(range(0, 10, 2))
print(demo)

```

<img src="https://img-blog.csdnimg.cn/44524b83a3c94ccfafc20e5a5c99dc35.png" alt="在这里插入图片描述">

### 访问列表元素

在Python列表中，我们可以使用索引去访问列表中的元素

`实例`：创建一个名为demo的列表并访问指定索引的元素

```
demo = ["hello", "python", "world"]
print(demo[1])  # 索引从0开始以此类推

```

<img src="https://img-blog.csdnimg.cn/db48b342cb4540f3afa231cb30b827f4.png" alt="在这里插入图片描述">

### 修改列表元素

修改列表元素只需要通过索引获取该元素，然后再重新赋值即可

`实例`：定义一个名为demo的列表修改索引值为1的元素

```
demo = ["hello", "python", "world"]
print("修改之前的列表:", demo)
demo[1] = "java"
print("修改之后的列表:", demo)

```

<img src="https://img-blog.csdnimg.cn/845b790d9b894f8095f33c3d399bb9e9.png" alt="在这里插入图片描述">

### 删除列表元素

删除元素由两种方法：
- `根据索引删除` 删除列表中的指定元素和删除列表类似，可以使用del语句实现 实例：创建一个名为demo的列表，删除索引为1的元素
```
demo = ["hello", "python", "world"]
del demo[1]
print(demo)

```

`运行结果如下`：

<img src="https://img-blog.csdnimg.cn/238cfc562ef246f180d5ad753450c846.png" alt="在这里插入图片描述">
- `根据元素值删除`
如果想要删除不确定其所在位置的元素可以根据元素值删除，使用列表对象的remove()方法实现

`实例`：定义一个名为demo的列表删除"python"元素

```
demo = ["hello", "java", "world"]
demo.remove("java")
print(demo)

```

<img src="https://img-blog.csdnimg.cn/69c13f0505b14675a026adf27dac06fe.png" alt="在这里插入图片描述"> `注意事项`：

这里做了一个错误的示范如果在使用remove()方法进行删除元素时，如果指定的元素不存在会报以下的错误 `ValueError: list.remove(x): x not in list`：要删除的值不在列表中

<img src="https://img-blog.csdnimg.cn/a52466266970493bb33c58453e1af6f2.png" alt="在这里插入图片描述"> 当我们要用remove()方法删除元素的时候首先要判断元素是否存在，可以对以上的代码进行改进 `说明`：count()方法用于判断指定元素出现次数，如果为0该元素不存在

```
demo = ["hello", "java", "world"]
value = "python"
if demo.count(value) &gt; 0:
    demo.remove(value)
else:
    print("该元素不存在此列表中")

```

<img src="https://img-blog.csdnimg.cn/6037dcd809d348e5b7b36d80e5cf833e.png" alt="在这里插入图片描述">

### 删除列表

对于已经创建好的列表，不再使用使可以使用del语句将其删除 del语句语法格式：`del listname` 参数说明如下： `listname`：要删除的列表名称

`实例`：定义一个名为demo的列表并将其删除

```
demo = ["但行好事", "莫问前程"]
del demo

```

`注意事项`： 在删除列表前，一定要确定输入的列表名称是已经存在的，否则会报错 `NameError: name 'demo' is not define`：demo名称未定义

<img src="https://img-blog.csdnimg.cn/20e6f401e96446c3ac931736184274a5.png" alt="在这里插入图片描述">

## ✨遍历列表的两种方法

### 使用for循环遍历

直接使用for循环遍历列表，输出元素的值 使用for循环遍历语法格式：`for item in listname:` 参数说明如下： `item`：保存获取到的元素值 `listname`：要遍历的列表名称 `实例`：创建一个名为demo的列表，使用for循环遍历此列表输出元素的值

```
demo = ["hello", "python", "world"]
for item in demo:
    print(item)

```

<img src="https://img-blog.csdnimg.cn/f41f2720c30a4855af27a206fc7b8265.png" alt="在这里插入图片描述">

### 使用for循环和enumerate()函数遍历

使用for循环和enumerate()函数遍历列表可以同时输出索引值和元素值 语法格式：`for index,item in enumerate(listname):` 参数说明如下： `index`：保存元素索引 `item`：保存获取到的元素值 `listname`：要遍历的列表名称

`实例`：创建一个名为demo的列表，使用for循环和`enumerate()`函数遍历输出索引和对应的元素值

```
demo = ["hello", "python", "world"]
for index, item in enumerate(demo):
    print(index, ":", item)

```

`运行结果如下`：

<img src="https://img-blog.csdnimg.cn/107c1935a123430a9b0c0e9011920d3b.png" alt="在这里插入图片描述">

## ✨列表常用方法

### 计算列表元素个数`len()`

`len()`方法用于计算列表中元素个数 len()方法语法格式：`len(list)` 参数说明如下： `list`：要计算元素个数的列表

`实例`：定义一个数字列表demo，计算元素个数

```
demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(len(demo))

```

<img src="https://img-blog.csdnimg.cn/b76e91a17c2f4aca9676f09da7364d98.png" alt="在这里插入图片描述">

### 获取指定元素出现次数`count()`

`count()`方法用于获取指定元素在列表中出现次数 count()方法语法格式：`listname.count(obj)` 参数说明如下： `listname`：列表名称 `obj`：要指定获取次数的元素 `返回值`：元素在列表中出现次数

`实例`：创建一个数字列表，获取7出现的次数

```
demo = [1, 2, 4, 2, 7, 6, 3, 7, 7, 5, 9]
print(demo.count(7))

```

<img src="https://img-blog.csdnimg.cn/8c925fbd1abc476d96ecae34b5d1e451.png" alt="在这里插入图片描述">

### 返回列表元素最大值`max()`

`max()`方法返回列表元素最大值 max()方法语法格式：`max(list)` 参数说明如下： `list`：要返回最大值的列表

`实例`：返回demo和demo1中元素最大值

```
demo = ["python", "java", "javascript"]
demo1 = [400, 777, 100]
print("demo最大元素值:", max(demo), "\n" + "demo1最大元素值:", max(demo1))

```

：

<img src="https://img-blog.csdnimg.cn/339ef5100e0b4ce3b292c34e0587d859.png" alt="在这里插入图片描述">

### 返回列表元素最小值`min()`

`min()`方法返回列表元素最大值 min()方法语法格式：`min(list)` 参数说明如下： `list`：要返回最小值的列表

`实例`：返回demo和demo1中元素最小值

```
demo = ["python", "java", "javascript"]
demo1 = [400, 777, 100]
print("demo最小元素值:", min(demo), "\n" + "demo1最小元素值:", min(demo1))

```

<img src="https://img-blog.csdnimg.cn/6554dbdf65ee4c37917c49d339c5d656.png" alt="在这里插入图片描述">

### 清空列表`clear()`

clear()方法用于清空列表，与del()方法类似，但是del()是将列表直接删除，clear()只是清空，打印出来是空列表

```
demo = ["hello", "python", "world"]
demo.clear()
print("列表清空后:", demo)

```

<img src="https://img-blog.csdnimg.cn/fb679814ee3440a88d78759c1744b000.png" alt="在这里插入图片描述">

### 复制列表`copy()`

copy()方法用于复制列表 copy()方法语法格式：`list.copy()`

实例：复制一份demo列表名为为demo1

```
demo = ["hello", "python", "world"]
demo1 = demo.copy()
print("demo1列表:", demo1)

```

<img src="https://img-blog.csdnimg.cn/9e3b1cfbed7245fdb0afe30569931b92.png" alt="在这里插入图片描述">

### 在列表末尾添加新的元素`append()`

`append()`方法用于在列表末尾追加元素 append()方法语法格式：`listname.append(obj)` 参数说明如下： `listname`：要添加元素的列表名称 `obj`：要添加到列表末尾的元素

`实例`：创建一个名为demo的列表并在列表末尾追加一个元素

```
demo = ["hello"]
demo.append("world")
print(demo)

```

<img src="https://img-blog.csdnimg.cn/40ca9c09dbc147fa92e6b89bbc587753.png" alt="在这里插入图片描述">

### 将一个列表中的多个元素添加到另一个列表`extend()`

`extend()`方法用于将一个列表多个元素添加到另一个列表，也可以理解为用新列表扩展原来的列表 extend()方法语法格式：`list.extend(seq)` 参数说明如下： `seq`：元素列表，可以是列表、元组、集合、字典

实例：用demo1列表去扩展demo列表

```
demo = ["hacker707"]
demo1 = ["嘎嘎宠粉"]
demo.extend(demo1)
print("扩展后的列表:", demo)

```

<img src="https://img-blog.csdnimg.cn/613b45118a07428787ef58dce9233ce4.png" alt="在这里插入图片描述">

### 检索指定元素在列表中首次出现的索引位置`index()`

`index()`方法用于检索指定元素在列表中首次出现的索引位置 index()方法语法格式：`listname.index(obj)` 参数说明如下： `listname`：列表的名称 `obj`：要检索的对象 `返回值`：元素首次出现的索引值

`实例`：检索元素"a"首次出现的索引位置

```
demo = ["h", "a", "c", "k", "e", "r"]
print("a元素首次出现位置:", demo.index("a"))

```

<img src="https://img-blog.csdnimg.cn/70b013cfd707426785cb322b48e6de1d.png" alt="在这里插入图片描述">

### 计算数值列表中各元素的和`sum()`

sum()方法用于计算数值列表中各元素的和 sum()方法语法格式：`sum(iterable[,start])` 参数说明如下： `iterable`：要计算的列表 `start`：可选参数，表示计算结果从哪个数开始(默认为0)

`实例`：定义保存10名学生数学成绩的列表并计算总成绩

```
score = [97, 90, 100, 77, 73, 96, 89, 77, 79, 92]
print("10名学生数学总成绩:", sum(score))

```

<img src="https://img-blog.csdnimg.cn/fa76d022758d4fec9a98e14410f7613b.png" alt="在这里插入图片描述">

### 对列表进行排序`sort()`

`sort()`方法用于对原列表元素进行排序 sort()方法语法格式：`list.sort( key=None, reverse=False)` 参数说明如下： `key`：用于指定排序规则(例如设置"key=str.lower"表示在排序时不区分字母大小写) `reverse`：可选参数(设置为True降序，设置为False升序)

`实例`：对10名学生数学成绩进行升序，降序操作

```
score = [97, 90, 100, 77, 73, 96, 89, 77, 79, 92]
print("原列表", score)
score.sort()
print("升序:", score)
score.sort(reverse=True)
print("降序:", score)

```

<img src="https://img-blog.csdnimg.cn/b2090d6ef0ae4b1b876fa9bd61ee739c.png" alt="在这里插入图片描述">

### 对所有可迭代对象进行排序`sorted()`

sorted()方法语法格式：`sorted(iterable, key=None, reverse=False)` 参数说明如下：
- `iterable`：可迭代对象，例如列表、元组、集合、字符串等。- `key`：排序时比较的函数，用于指定一个自定义函数来为每个元素生成一个键值，排序时会根据键值进行比较和排序。- `reverse`：排序规则， reverse=True 表示降序排序， reverse=False 表示升序排序(默认)
`实例`：将alist列表进行升序和降序排序

```
alist = [10, 8, 1, 4, 3, 6, 5, 7, 2, 9]
print("升序排序:", sorted(alist))
print("降序排序:", sorted(alist, reverse=True))

```

<img src="https://img-blog.csdnimg.cn/45a280c8e07a4da69d94e346ec1bab91.png" alt="在这里插入图片描述"> `sorted()和sort()的区别`：
- `sorted()`不会修改原始可迭代对象，而是返回一个新的排序列表- `sort()`对原始可迭代对象进行排序
### 删除列表中的一个元素`pop()`

pop()方法语法格式：list.pop(index) 参数说明如下：
- `index`：可选参数，列表中要移除的元素的索引位置，默认为 -1，即移除列表中的最后一个元素。
`实例`：移除demo列表中索引为1的元素

```
demo = ["python", "java", "javascript", "mysql"]
print("移除的元素:", demo.pop(1))
print("移除后的列表", demo)

```

<img src="https://img-blog.csdnimg.cn/33e6e37240a94add8681941368b3e02e.png" alt="在这里插入图片描述">

### 删除列表中某个值的第一个匹配项`remove()`

remove()方法语法格式：`list.remove(element)` 参数说明如下：
- `element`:要移除的元素
```
demo = ["python", "java", "javascript", "mysql"]
print("原列表:", demo)
demo.remove("java")
print("移除后的列表:", demo)

```

<img src="https://img-blog.csdnimg.cn/0e7d3826623646769b0035719242fefd.png" alt="在这里插入图片描述"> ✅如果要移除的元素出现多次，可以使用while循环多次调用remove()方法进行移除

```
demo = ["python", "java", "javascript", "mysql", "mysql", "mysql"]
print("原列表:", demo)
while "mysql" in demo:
    demo.remove("mysql")
print("移除后的列表:", demo)

```

<img src="https://img-blog.csdnimg.cn/2f15b430b79f43c9b3bb0d3b168e3721.png" alt="在这里插入图片描述">

## 结束语🥇

>  
 以上就是Python基础入门篇之Python标准数据类型-List(列表) 
 - `欢迎大家订阅系列专栏:`- `此专栏内容会持续更新直到完结为止(如有任何纰漏请在评论区留言或者私信）` 


>  
 感谢大家一直以来对hacker的支持 你们的支持就是博主无尽创作的动力💖💖💖 


<img src="https://img-blog.csdnimg.cn/bdd237d869be4fee9ba4de0f100e35a8.gif#pic_center" alt="在这里插入图片描述">
