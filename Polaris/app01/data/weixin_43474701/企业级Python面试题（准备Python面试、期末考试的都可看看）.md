
--- 
title:  企业级Python面试题（准备Python面试、期末考试的都可看看） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/b31bbd7c0d6744ef80a92d925880677d.jpeg" alt="在这里插入图片描述">



#### 一百七十个Python面试题（准备面试、期末考试的都可看看）
- <ul><li>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


记不牢运算符，记不牢字符串，记不牢列表方法……这些比较零碎的知识点在学习后很容易忘却，需要不断强化记忆。

为了让大家能够知道面试官喜欢问什么，我整理了一期热门的Python面试题，方便大家可以日常查看

### Python面试题（上部分）

### 1. 为什么学习 Python？

Python 语言简单易懂，上手容易，随着 AI 风潮，越来越火 

### 2. 解释型和编译型语言的区别

编译型语言：把做好的源程序全部编译成二进制的可运行程序。然后，可直接运行这个程序。如：C，C++ 解释型语言：把做好的源程序翻译一句，然后执行一句，直至结束！如：Python， （Java 有些特殊，java程序也需要编译，但是没有直接编译称为机器语言，而是编译称为字节码，然后用解释方式执行字节码。）

### 3. 简述下 Python 中的字符串、列表、元组和字典

字符串（str）：字符串是用引号括起来的任意文本，是编程语言中最常用的数据类型。列表（list）：列表是有序的集合，可以向其中添加或删除元素。元组（tuple）：元组也是有序集合，但是是无法修改的。即元组是不可变的。字典（dict）：字典是无序的集合，是由 key-value 组成的。集合（set）：是一组 key 的集合，每个元素都是唯一，不重复且无序的。

### 4. 简述上述数据类型的常用方法

字符串：

>  
 切片 mystr=‘luobodazahui’ mystr[1:3] output ‘uo’ 
 format mystr2 = “welcome to luobodazahui, dear {name}” mystr2.format(name=“baby”) output ‘welcome to luobodazahui, dear baby’ 
 join 可以用来连接字符串，将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串。mylist = [‘luo’, ‘bo’, ‘da’, ‘za’, ‘hui’] mystr3 = ‘-’.join(mylist) print(mystr3) outout ‘luo-bo-da-za-hui’ 
 replace String.replace(old,new,count) 将字符串中的 old 字符替换为 New 字符，count 为替换的个数 mystr4 = ‘luobodazahui-haha’ print(mystr4.replace(‘haha’, ‘good’)) 
 output luobodazahui-good 
 split 切割字符串,得到一个列表 mystr5 = ‘luobo,dazahui good’ #以空格分割 print(mystr5.split()) #以h分割 
 print(mystr5.split(‘h’)) #以逗号分割 print(mystr5.split(‘,’)) output 
 [‘luobo,dazahui’, ‘good’] [‘luobo,daza’, ‘ui good’] [‘luobo’, ‘dazahui good’] 


列表：

>  
 切片 同字符串 append 和 extend 向列表中国添加元素 mylist1 = [1, 2] mylist2 = [3, 4] mylist3 = [1, 2] mylist1.append(mylist2) print(mylist1) mylist3.extend(mylist2) print(mylist3) outout 
 [1, 2, [3, 4]] [1, 2, 3, 4] 删除元素 del：根据下标进行删除 pop：删除最后一个元素 remove：根据元素的值进行删除 mylist4 = [‘a’, ‘b’, ‘c’, ‘d’] del mylist4[0] print(mylist4) mylist4.pop() print(mylist4) mylist4.remove(‘c’) print(mylist4) output 
 [‘b’, ‘c’, ‘d’] [‘b’, ‘c’] [‘b’] 元素排序 sort：是将list按特定顺序重新排列，默认为由小到大，参数 reverse=True 可改为倒序，由大到小。reverse：是将list逆置 mylist5 = [1, 5, 2, 3, 4] mylist5.sort() print(mylist5) mylist5.reverse() print(mylist5) output 
 [1, 2, 3, 4, 5] [5, 4, 3, 2, 1] 


字典：

>  
 清空字典 dict.clear() dict1 = {‘key1’:1, ‘key2’:2} dict1.clear() print(dict1) output 
 {} 指定删除 使用 pop 方法来指定删除字典中的某一项 dict1 = {‘key1’:1, ‘key2’:2} d1 = dict1.pop(‘key1’) print(d1) print(dict1) output 
 1 {‘key2’: 2} 遍历字典 dict2 = {‘key1’:1, ‘key2’:2} mykey = [key for key in dict2] print(mykey) myvalue = [value for value in dict2.values()] print(myvalue) key_value = [(k, v) for k, v in dict2.items() ] print(key_value) output 
 [‘key1’, ‘key2’] [1, 2] [(‘key1’, 1), (‘key2’, 2)] fromkeys 用于创建一个新字典，以序列中元素做字典的键，value 为字典所有键对应的初始值 keys = [‘zhangfei’, ‘guanyu’, ‘liubei’, ‘zhaoyun’] dict.fromkeys(keys, 0) output 
 {‘zhangfei’: 0, ‘guanyu’: 0, ‘liubei’: 0, ‘zhaoyun’: 0} 


### 5. 简述 Python 中的字符串编码

计算机在最初的设计中，采用了8 个比特（bit）作为一个字节（byte）的方式。一个字节能表示的最大的整数就是255（二进制11111111=十进制255），如果要表示更大的整数，就必须用更多的字节。最早，计算机只有 ASCII 编码，即只包含大小写英文字母、数字和一些符号，这些对于其他语言，如中文，日文显然是不够用的。后来又发明了Unicode，Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。UTF-8 是隶属于 Unicode 的可变长的编码方式。在 Python 中，以 Unicode 方式编码的字符串，可以使用 encode() 方法来编码成指定的 bytes，也可以通过 decode() 方法来把 bytes 编码成字符串。encode

```
"中文".encode('utf-8')
output

b'\xe4\xb8\xad\xe6\x96\x87'
decode

```

b’\xe4\xb8\xad\xe6\x96\x87’.decode(‘utf-8’)

>  
 output 
 ‘中文’ 


### 6. is 和 == 的区别

先来看个例子

```
c = d = [1,2]
e = [1,2]
print(c is d)
print(c == d)
print(c is e)
print(c == e)

```

>  
 output 
 True 
 True 
 False 
 True 


== 是比较操作符，只是判断对象的值（value）是否一致，而 is 则判断的是对象之间的身份（内存地址）是否一致。对象的身份，可以通过 id() 方法来查看

```
id(c)
id(d)
id(e)

```

>  
 output 
 88748080 
 88748080 
 88558288 


可以看出，只有 id 一致时，is 比较才会返回 True，而当 value 一致时，== 比较就会返回 True

### 7.一行代码实现数值交换

```
1a = 1
2b = 2
3a, b = b, a
4print(a, b)

```

>  
 output 
 12 1 


### 8.Python 函数中的参数类型

位置参数，默认参数，可变参数，关键字参数

### 9.*arg 和 **kwarg 作用

允许我们在调用函数的时候传入多个实参

```
def test(*arg, **kwarg):
    if arg:
        print("arg:", arg)
    if kwarg:
        print("kearg:", kwarg)
test('ni', 'hao', key='world')

```

>  
 output 
 arg: (‘ni’, ‘hao’) 
 kearg: {‘key’: ‘world’} 
 可以看出，*arg 会把位置参数转化为 tuple**kwarg 会把关键字参数转化为 dict 


### 10.一行代码实现1-100之和

```
sum(range(1, 101))
11.获取当前时间
import time
import datetime
print(datetime.datetime.now())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

```

>  
 output 
 2019-06-07 18:12:11.165330 
 2019-06-07 18:12:11 


### 12.PEP8 规范

简单列举10条：尽量以免单独使用小写字母’l’，大写字母’O’，以及大写字母’I’等容易混淆的字母。函数命名使用全部小写的方式，可以使用下划线。常量命名使用全部大写的方式，可以使用下划线。使用 has 或 is 前缀命名布尔元素，如: is_connect = True; has_member = False 不要在行尾加分号, 也不要用分号将两条命令放在同一行。不要使用反斜杠连接行。顶级定义之间空2行, 方法定义之间空1行，顶级定义之间空两行。如果一个类不继承自其它类, 就显式的从object继承。内部使用的类、方法或变量前，需加前缀_表明此为内部使用的。要用断言来实现静态类型检测。

### 13.Python 的深浅拷贝

**浅拷贝**

```
import copy
list1 = [1, 2, 3, [1, 2]]
list2 = copy.copy(list1)
list2.append('a')
list2[3].append('a')
print(list1, list2)

```

output

[1, 2, 3, [1, 2, ‘a’]] [1, 2, 3, [1, 2, ‘a’], ‘a’] 能够看出，浅拷贝只成功”独立“拷贝了列表的外层，而列表的内层列表，还是共享的

**深拷贝**

```
import copy
list1 = [1, 2, 3, [1, 2]]
list3 = copy.deepcopy(list1)
list3.append('a')
list3[3].append('a')
print(list1, list3)

```

>  
 output 
 [1, 2, 3, [1, 2]] [1, 2, 3, [1, 2, ‘a’], ‘a’] 


深拷贝使得两个列表完全独立开来，每一个列表的操作，都不会影响到另一个

### 14.re 的 match 和 search 区别

match()函数只检测要匹配的字符是不是在 string 的开始位置匹配，search()会扫描整个 string 查找匹配

### 15.可变类型与不可变类型

可变数据类型：list、dict、set

不可变数据类型：int/float、str、tuple

### 16.打印九九乘法表

```
for i in range(1, 10):
    for j in range(1, i+1):
        print("%s*%s=%s " %(i, j, i*j), end="")
    print()

```

output

```
1*1=1 
2*1=2 2*2=4 
3*1=3 3*2=6 3*3=9 
4*1=4 4*2=8 4*3=12 4*4=16 
5*1=5 5*2=10 5*3=15 5*4=20 5*5=25 
6*1=6 6*2=12 6*3=18 6*4=24 6*5=30 6*6=36 
7*1=7 7*2=14 7*3=21 7*4=28 7*5=35 7*6=42 7*7=49 
8*1=8 8*2=16 8*3=24 8*4=32 8*5=40 8*6=48 8*7=56 8*8=64 
9*1=9 9*2=18 9*3=27 9*4=36 9*5=45 9*6=54 9*7=63 9*8=72 9*9=81

```

print 函数，默认是会换行的，其有一个默认参数 end，如果像例子中，我们把 end 参数显示的置为""，那么 print 函数执行完后，就不会换行了，这样就达到了九九乘法表的效果了

### 17.filter、map、reduce 的作用

filter 函数用于过滤序列，它接收一个函数和一个序列，把函数作用在序列的每个元素上，然后根据返回值是True还是False决定保留还是丢弃该元素

```
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list(filter(lambda x: x%2 == 1, mylist))

```

output

[1, 3, 5, 7, 9] 保留奇数列表

map 函数传入一个函数和一个序列，并把函数作用到序列的每个元素上，返回一个可迭代对象

```
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list(map(lambda x: x*2, mylist))

```

output

[2, 4, 6, 8, 10, 12, 14, 16, 18] reduce 函数用于递归计算，同样需要传入一个函数和一个序列，并把函数和序列元素的计算结果与下一个元素进行计算

```
from functools import reduce
reduce(lambda x, y: x+y, range(101))

```

output

5050 可以看出，上面的三个函数与匿名函数相结合使用，可以写出强大简洁的代码

### 18.查看下面代码的输出

```
def num():
    return [lambda x:i*x for i in range(4)]
print([m(1) for m in num()])

```

>  
 output 
 [3, 3, 3, 3] 


通过运行结果，可以看出 i 的取值为3，很神奇

### 19.面向对象中__new__ 和 **init** 区别

__new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例对象，是个静态方法。__init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值，通常用在初始化一个类实例的时候，是一个实例方法

1、__new__至少要有一个参数 cls，代表当前类，此参数在实例化时由 Python 解释器自动识别。2、__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以 return 父类（通过 super(当前类名, cls)）__new__出来的实例，或者直接是 object 的__new__出来的实例。3、__init__有一个参数 self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值。4、如果__new__创建的是当前类的实例，会自动调用__init__函数，通过 return 语句里面调用的__new__函数的第一个参数是 cls 来保证是当前类实例，如果是其他类的类名，；那么实际创建返回的就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数

### 20.三元运算规则

a, b = 1, 2 #若果 a&gt;b 成立 就输出 a-b 否则 a+b h = a-b if a&gt;b else a+b output

3

### 21.生成随机数

print(random.random()) print(random.randint(1, 100)) print(random.uniform(1,5)) output

0.03765019937131564 18 1.8458555362279228

### 22.zip 函数用法

zip() 函数将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表

list1 = [‘zhangfei’, ‘guanyu’, ‘liubei’, ‘zhaoyun’] list2 = [0, 3, 2, 4] list(zip(list1, list2)) output

[(‘zhangfei’, 0), (‘guanyu’, 3), (‘liubei’, 2), (‘zhaoyun’, 4)]

### 23.range 和 xrange 的区别

range([start,] stop[, step])，根据start与stop指定的范围以及step设定的步长，生成一个序列。而 xrange 生成一个生成器，可以很大的节约内存

### 24.with 方法打开文件的作用

开文件在进行读写的时候可能会出现一些异常状况，如果按照常规的 f.open 写法，我们需要 try,except,finally，做异常判断，并且文件最终不管遇到什么情况，都要执行 finally f.close() 关闭文件，with 方法帮我们实现了 finally 中 f.close

### 25.什么是正则的贪婪匹配

Python 中默认是贪婪匹配模式

贪婪模式：正则表达式一般趋向于最大长度匹配

非贪婪模式：在整个表达式匹配成功的前提下，尽可能少的匹配

### 26.为什么不建议函数的默认参数传入可变对象

例如：

def test(L=[]): L.append(‘test’) print(L) output

test() # [‘test’] test() # [‘test’, ‘test’] 默认参数是一个列表，是可变对象[],Python 在函数定义的时候，默认参数 L 的值就被计算出来了，是[]，每次调用函数，如果 L 的值变了，那么下次调用时，默认参数的值就已经不再是[]了

### 27.字符串转整数

mylist = [‘1’, ‘2’, ‘3’] list(map(lambda x: int(x), mylist)) output

[1, 2, 3]

### 28.字符串转列表

mystr = ‘1,2,3’ mystr.split(‘,’) output

[‘1’, ‘2’, ‘3’]

### 29.删除列表中的重复值

mylist = [1, 2, 3, 4, 5, 5] list(set(mylist))

### 30.字符串单词统计

from collections import Counter mystr = ‘sdfsfsfsdfsd,were,hrhrgege.sdfwe!sfsdfs’ Counter(mystr) output Counter({‘s’: 9, ‘d’: 5, ‘f’: 7, ‘,’: 2, ‘w’: 2, ‘e’: 5, ‘r’: 3, ‘h’: 2, ‘g’: 2, ‘.’: 1, ‘!’: 1})

### 31.列表推导，求奇偶数

[x for x in range(10) if x%2 == 1] output

[1, 3, 5, 7, 9] 32.一行代码展开列表 list1 = [[1,2],[3,4],[5,6]] [j for i in list1 for j in i] output

[1, 2, 3, 4, 5, 6]

### 33.实现二分法查找函数

二分查找算法也称折半查找，基本思想就是折半，对比大小后再折半查找，必须是有序序列才可以使用二分查找

**递归算法**

def binary_search(data, item): # 递归

```
  n = len(data)
     if n &gt; 0:
         mid = n // 2
         if data[mid] == item:
             return True
         elif data[mid] &gt; item:
             return binary_search(data[:mid], item)
        else:
            return binary_search(data[mid+1:], item)
    return False
list1 = [1,4,5,66,78,99,100,101,233,250,444,890]
binary_search(list1, 999)

```

**非递归算法**

```
 def binary_search(data, item):
     # 非递归
     n = len(data)
     first = 0
     last = n - 1
     while first &lt;= last:
         mid = (first + last)//2
         if data[mid] == item:
             return True
        elif data[mid] &gt; item:
            last = mid - 1
        else:
            first = mid + 1
    return False
list1 = [1,4,5,66,78,99,100,101,233,250,444,890]
binary_search(list1, 99)

```

### 34.字典和 json 转换

字典转 json

```
import json
dict1 = {<!-- -->'zhangfei':1, "liubei":2, "guanyu": 4, "zhaoyun":3}
myjson = json.dumps(dict1)
myjson
output
'{"zhangfei": 1, "liubei": 2, "guanyu": 4, "zhaoyun": 3}'
json 转字典
mydict = json.loads(myjson)
mydict
output

{<!-- -->'zhangfei': 1, 'liubei': 2, 'guanyu': 4, 'zhaoyun': 3}

```

### 35.列表推导式、字典推导式和生成器

```
import random
td_list=[i for i in range(10)]
print("列表推导式", td_list, type(td_list))
ge_list = (i for i in range(10))
print("生成器", ge_list)
dic = {<!-- -->k:random.randint(4, 9)for k in ["a", "b", "c", "d"]}
print("字典推导式",dic,type(dic))

```

>  
 output 
 列表推导式 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] &lt;class ‘list’&gt; 生成器 &lt;generator object at 0x0139F070&gt; 字典推导式 {‘a’: 6, ‘b’: 5, ‘c’: 8, ‘d’: 9} &lt;class ‘dict’&gt; 


### 36.打乱一个列表

list2 = [1, 2, 3, 4, 5, 6] random.shuffle(list2) print(list2) output

[4, 6, 5, 1, 2, 3]

### 37.简述 read、readline、readlines 的区别

read 读取整个文件

readline 读取下一行,使用生成器方法

readlines 读取整个文件到一个迭代器以供我们遍历

### 38.单下划线和双下划线的作用

**foo**：一种约定，Python 内部的名字，用来区别其他用户自定义的命名，以防冲突，就是例如__init__(),**del**(),**call**()些特殊方法

_foo：一种约定，用来指定变量私有。不能用 from module import * 导入，其他方面和公有变量一样访问

__foo：这个有真正的意义：解析器用_classname__foo 来代替这个名字，以区别和其他类相同的命名，它无法直接像公有成员一样随便访问，通过对象名._类名__xxx 这样的方式可以访问

### 39.反转字符串

str1 = ‘luobodazahui’ str1[::-1] output

‘iuhazadoboul’

### 40.新式类和旧式类

a. 在 python 里凡是继承了 object 的类，都是新式类

b. Python3 里只有新式类

c. Python2 里面继承 object 的是新式类，没有写父类的是经典类

d. 经典类目前在 Python 里基本没有应用

### 41.Python 面向对象中的继承有什么特点

a. 同时支持单继承与多继承，当只有一个父类时为单继承，当存在多个父类时为多继承

b. 子类会继承父类所有的属性和方法，子类也可以覆盖父类同名的变量和方法

c. 在继承中基类的构造（**init**()）方法不会被自动调用，它需要在其派生类的构造中专门调用

d. 在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。区别于在类中调用普通函数时并不需要带上 self 参数

### 42.super 函数的作用

super() 函数是用于调用父类(超类)的一个方法

```
 class A():
     def funcA(self):
         print("this is func A")
 class B(A):
     def funcA_in_B(self):
         super(B, self).funcA()
 
     def funcC(self):
         print("this is func C")

ins = B()
ins.funcA_in_B()
ins.funcC()

```

output

>  
 this is func A 
 this is func C 


### 43.类中的各种函数

主要分为实例方法、类方法和静态方法

**实例方法**

定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）

调用：只能由实例对象调用

**类方法**

定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）

调用：实例对象和类对象都可以调用

**静态方法**

定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法

调用：实例对象和类对象都可以调用

静态方法是类中的函数，不需要实例。静态方法主要是用来存放逻辑性的代码，主要是一些逻辑属于类，但是和类本身没有交互。即在静态方法中，不会涉及到类中的方法和属性的操作。可以理解为将静态方法存在此类的名称空间中

类方法是将类本身作为对象进行操作的方法。他和静态方法的区别在于：不管这个方式是从实例调用还是从类调用，它都用第一个参数把类传递过来

### 44.如何判断是函数还是方法

与类和实例无绑定关系的 function 都属于函数（function）

与类和实例有绑定关系的 function 都属于方法（method）

普通函数：

```
def func1():
    pass
print(func1)
output
&lt;function func1 at 0x01379348&gt;
类中的函数：
 class People(object):
     def func2(self):
         pass
     @staticmethod
     def func3():
         pass
     @classmethod
     def func4(cls):
         pass
people = People()
print(people.func2)
print(people.func3)
print(people.func4)

```

output

&lt;bound method People.func2 of &lt;**main**.People object at 0x013B8C90&gt;&gt; &lt;function People.func3 at 0x01379390&gt; &lt;bound method People.func4 of &lt;class ‘**main**.People’&gt;&gt; 45.isinstance 的作用以及与 type()的区别 isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()

区别：

type() 不会认为子类是一种父类类型，不考虑继承关系

isinstance() 会认为子类是一种父类类型，考虑继承关系

```
 class A(object):
     pass
 class B(A):
     pass
 a = A()
 b = B()
 print(isinstance(a, A))
 print(isinstance(b, A))
 print(type(a) == A)
print(type(b) == A)

```

>  
 output 
 True 
 True 
 True 
 False 


### 46.单例模式与工厂模式

单例模式：主要目的是确保某一个类只有一个实例存在

工厂模式：包涵一个超类，这个超类提供一个抽象化的接口来创建一个特定类型的对象，而不是决定哪个对象可以被创建

### 47.查看目录下的所有文件

import os print(os.listdir(‘.’))

### 48.计算1到5组成的互不重复的三位数

```
 # 1到5组成的互不重复的三位数
 k = 0
 for i in range(1, 6):
     for j in range(1, 6):
         for z in range(1, 6):
             if (i != j) and (i != z) and (j != z):
                 k += 1
                 if k%6:
                     print("%s%s%s" %(i, j, z), end="|")
                else:
                    print("%s%s%s" %(i, j, z))

```

output

```
123|124|125|132|134|135
 142|143|145|152|153|154
 213|214|215|231|234|235
 241|243|245|251|253|254
 312|314|315|321|324|325
 341|342|345|351|352|354
 412|413|415|421|423|425
 431|432|435|451|452|453
 512|513|514|521|523|524
531|532|534|541|542|543

```

### 49.去除字符串首尾空格

```
str1 = "   hello nihao    "
str1.strip()

```

output

>  
 ‘hello nihao’ 


### 50.去除字符串中间的空格

```
str2 = "hello you are good"
print(str2.replace(" ", ""))
"".join(str2.split(" "))

```

>  
 output 
 helloyouaregood ‘helloyouaregood’ 


好了，这就是今天分享的全部内容，120个没写完的下次再继续分享，如果喜欢就点个赞吧~
