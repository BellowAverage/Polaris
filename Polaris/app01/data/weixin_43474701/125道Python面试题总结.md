
--- 
title:  125道Python面试题总结 
tags: []
categories: [] 

---
### Pyhton面试宝典

**1. 一行代码实现1-100之和**

```
res=sum(range(1,101))
print(res)  #5050

```

 **2. 如何在一个函数内部修改全局变量**

```
a=5
def func():
    global a
    a=10
    return a
func()
print(a)   #10

```

**3. 列出 5 个常用 Python 标准库？**

```
常用的有

os 提供了与操作系统关联的函数
import os
os.getcwd()
os.path.join('/usr/temp','test.log')
datatime 提供了日期和时间处理的常用方法
from datetime import datetime
# 将时间戳转换为日期类型
datetime.fromtimestamp(1638175727)
datetime.strptime('2021-12-01 13:13:13','%Y-%m-%d %H:%M:%S')
datetime.now()
random 随机数生成库
import random
# 生成1-100的随机数
print(random.randint(1,100))
# 在abcdef中随机选择一个
print(random.choice('abcdef'))
math 数学运算库
import math
print(math.pow(2,4))
print(math.sin(1))
print(math.floor(2.5))
re 正则匹配模块

import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')
if match:
    # 使用Match获得分组信息
    print(match.group())
# 搜索整个字符串
m = re.search('[a-z]+','abcdef123ghh')
print(m.group(0))
m2 = re.search('[0-9]+','abcdef123ghh')
print(m2.group(0))


```

**4. 如何合并两个字典**

```
#4、如何合并两个字典
dic1={<!-- -->'name':'psy'}
dic2={<!-- -->'age':18}
dic1.update(dic2)
print(dic1)  #{'age': 18, 'name': 'psy'}

```

**5. 谈一下Python的GIL**

```
#5、谈一下Python的GIL
"""

```

GIL是Python的全局解释器锁，同一个进程如果有多个线程，一个线程在运行Python程序的时候会占用Python解释器（加一把锁即GIL），使 该进程内的其他线程无法运行，等该线程运行完后其他县城才能运行。如果线程运行过程中遇到好事操作，则解释其锁解开，使其他线程运行。 所以在多线程中，线程的运行仍时有先后顺序的，并不是同时进行的。

补充：多进程中因为每个进程都能被系统分配资源，相当于每个进程有一个Python解释器，所以多进程可以实现多个进程的同时运行， 缺点就是进行系统资源开销大。 “”" **6、Python实现列表去重 【并保证原来的顺序】**

```
#6、Python实现列表去重  【并保证原来的顺序】
num_list = [1, 3, 1, 5, 3, 6, 1]
new_num=[]
jh=set()
for item in num_list:
    if item not in jh:
        new_num.append(item)
        jh.add(item)
print(new_num)  #[1, 3, 5, 6]

res=[num for num in set(num_list)]  #方法2
print(res)  #[1, 3, 5, 6]

```

**7、fun(args,kwargs)中的args, kwargs 什么意思？**

```
#7、fun(args,kwargs)中的args, kwargs 什么意思？
"""
*arg 表示传入的是非键值对的数据，即元祖类型
**kwargs 表示传入的是键值对数据，即字典类型

```

如果你有其他语言基础的话，你应该听说过重载的概念，对Python 为了避免这种繁琐的情况发生，引入了 args 和 kwargs； args 用来接受非键值对的数据，即元组类型，而 kwargs 则用来接受键值对数据，即字典类型。 “”" **8. Python2 和 Python3 的 range（100）的区别？**

```
#8、Python2 和 Python3 的 range（100）的区别？

python2返回的是列表
python3返回的是迭代器，节约资源

```

**9. 生成一个16位的随机字符串**

```
#9、生成一个16位的随机字符串
import random
import string  # string.printable  随机生成字符串，长度是100
res=''
for i in range(16):
    res=res+random.choice(string.printable)
print(res)  #G)_$U/#h@EhfL;6#

print(''.join((random.choice(string.printable)) for i in range(16)))  #I@}Z+Z(CS~5 AZ!+    【方法2】

```

**10、一句话解释什么样的语言能够用装饰器?**

```
#10、一句话解释什么样的语言能够用装饰器?

```

函数可以作为参数传递 **11、python内建的数据类型**

```
#11、python内建的数据类型
#整型 int    布尔型 bool    字符串  str    列表 list    元祖 tuple   字典 dict

```

**12、简述面向对象中new和init区别？**

```
#12、简述面向对象中new和init区别？
（1）__new__至少要一个参数cls，代表当前类，此参数在实例化由python解释器自动识别
（2）__new__必须要有一个返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意！
    可以return 父类（通过super(当前类名,cls)）.__new__出来的实例，或者直接是object的__new__出来的实例。
（3）__new__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，
    __init__不需要返回值
（4）如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面调用的__new__函数的第一个参数是cls来保证是当前类实例，
    如果是其他类的类名，那么实际创建返回的就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数

```

```
"""#【下面举例说明】
#__init__和__new__的区别
class Person(object):
    def __new__(cls,name,age):
        print('__new__ called')
        return super(Person,cls).__new__(cls)
    def __init__(self,name,age):
        print('__init__ called')
        self.name=name
        self.age=age
    def __str__(self):
        return 'Person:{}-{}'.format(self.name,self.age)
child=Person('psy',18)
print(child)
"""结果显示：
__new__ called
__init__ called
Person:psy-18

```

表明：

```
__new__的调用优于__init__方法；
__new__方法负责创建一个实例对象，__init__方法负责将该实例对象进行初始化；
__new__方法正式创建这个类实例的方法，返回额的对象正式__init__的self参数；
__init__用于实例化对象，__new__用于继承，是类别级的方法
#__new__的应用场景
#__new__方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径
class PositiveInt(int):
    def __new__(cls,value):
        return super(PositiveInt,cls).__new__(cls,abs(value))
print(PositiveInt(-55))  #55
class RoundFloat(float):
    def __new__(cls,value):
        return super(RoundFloat,cls).__new__(cls,round(value,2))
print(RoundFloat(3.1415926))  

```

**13、简述 with 方法打开处理文件帮我我们做了什么？**

```
"""
打开文件在进行读写操作时，可能会出现一些异常状况，如果按照常规的f.open写法，我们需要try,except，finally，做异常判断，
并且文件最终不管遇到什么情况，都要执行finally f.close()关闭文件。
其中利用with方法帮我们实现了finally中的f.close()。
"""

```

**14、列表[1,2,3,4,5]，请使用 map() 函数输出[1,4,9,16,25]，并使用列表推导式提取出大于 10 的数，最终输出 [16,25]？**

```
#14、列表[1,2,3,4,5]，请使用 map() 函数输出[1,4,9,16,25]，并使用列表推导式提取出大于 10 的数，最终输出 [16,25]？
l1=[1,2,3,4,5]
print(list(map(lambda x:x*x,l1))) #[1, 4, 9, 16, 25]
print([x for x in list(map(lambda x:x*x,l1)) if x&gt;10])  #[16, 25]

```

**15、python 中生成随机整数、随机小数、2-6 之间小数方法？**

```
#15、python 中生成随机整数、随机小数、2-6 之间小数方法？
print(random.randint(1,10))  #随机整数
print(random.random())       #随机小数
print(random.uniform(2,6))   #2-6之间的小数

```

**16、避免转义给字符串加哪个字母表示原始字符串？**

```
#16、避免转义给字符串加哪个字母表示原始字符串？
res=b'input\n'  #bytes字节符，打印以b开头
print(res)  #b'input\n'
res=r'input\n'  # 非转义原生字符，经处理'\n'变成了'\'和'n'。也就是\n表示的是两个字符，而不是换行。
print(res)  #input\n
res=u'input\n'  # unicode编码字符，python3默认字符串编码方式。
print(res)  #input + 换行

```

17、 &lt; di v class=“nam”&gt; Python，用正则匹配出标签里面的内容（“Python”），其中 class 的类名是不确定的。

```
#17、&lt;div class="nam"&gt;Python&lt;/div&gt;，用正则匹配出标签里面的内容（“Python”），其中 class 的类名是不确定的。
import re
s='&lt;div class="nam"&gt;Python&lt;/div&gt;'
res=re.findall(r'&lt;div class=".*"&gt;(.*?)&lt;.*&gt;',s)[0]
print(res) #Python

```

**18、Python 中断言方法举例？**

```
#18、Python 中断言方法举例？
age = 10
#assert 0 &lt; age &lt; 10
"""
结果显示：
Traceback (most recent call last):
  File "E:/000文章的代码/27/python面试题.py", line 157, in &lt;module&gt;
    assert 0 &lt; age &lt; 10
AssertionError
"""

```

**19、dict 中 fromkeys 的用法**

```
#19、dict 中 fromkeys 的用法
keys=('info1','info2')
res=dict.fromkeys(keys,['psy',18,'girl'])
print(res)  #{'info1': ['psy', 18, 'girl'], 'info2': ['psy', 18, 'girl']}

```

**20、请用正则表达式输出汉字**

```
import re
s="not 404 found 中国 2018 我爱你"
r1='[a-zA-Z0-9’!"#$%&amp;\'()*+,-./:;&lt;=&gt;?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+\s?'
res=re.sub(r1,'',s)
print(res) #中国 我爱你

```

**21、Python2 和 Python3 区别？列举 5 个**

```
#21、Python2 和 Python3 区别？列举 5 个
"""
（1）去除&lt;&gt;，全部使用!=
（2）print都要加()
（3）xrange()改为range()
（4）内存操作cStringIO改为StringIO
（5）加入nonlocal 作用：可以引用外部非全局变量
（6）zip() map() 和filter()都返回迭代器，而不是生成器，更加节约内存
"""

```

**22、列出 Python 中可变数据类型和不可变数据类型，为什么？**

```
"""
不可变类型：int str tuple
可变类型：list dict set
原理：可变数据类型即公用一个内存空间地址，不可变数据类型即每场一个对象就会产生一个内存地址
"""

```

**23、dict的内部实现？**

```
"""
在 Python 中，字典是通过哈希表实现的。也就是说，字典是一个数组，而数组的索引是键经过哈希函数处理后得到的。
哈希函数的目的是使键均匀地分布在数组中。由于不同的键可能具有相同的哈希值，即可能出现冲突，高级的哈希函数能够使冲突数目最小化。
"""

```

**24、s = “ajldjlajfdljfddd”，去重并从小到大排序输出"adfjl"？**

```
s='ajldjlajfdljfddd'
res1=sorted(list(set(s)))  #['a', 'd', 'f', 'j', 'l']
res=''.join(res1)
print(res)  #adfjl

```

**25、用 lambda 函数实现两个数相乘？**

```
mul=lambda x,y:x*y
print(mul(2,5))  #10

```

**26、字典根据键从小到大排序？**

```
info = {<!-- -->'name': 'Gage', 'location':'nj', 'sex': 'man'}
res_key=sorted(info.items(),key=lambda x:x[0]) #根据键排序
print(res_key)  #[('location', 'nj'), ('name', 'Gage'), ('sex', 'man')]
res_value=sorted(info.items(),key=lambda x:x[1])  #根据值排序
print(res_value)  #[('name', 'Gage'), ('sex', 'man'), ('location', 'nj')]

#若对列表中的字典进行排序
l=[{<!-- -->'name':'psy','age':18},{<!-- -->'name':'xk','age':24},{<!-- -->'name':'pyg','age':55}]
#按年龄进行排序
l.sort(key=lambda item:item['age'])
print(l)  #[{'name': 'psy', 'age': 18}, {'name': 'xk', 'age': 24}, {'name': 'pyg', 'age': 55}]

salaries={<!-- -->'psy':200,'xk':180,'gyp':300,'pyg':250}
#将salaries按照薪资的高低进行排序
res=sorted(salaries,key=lambda item:salaries[item],reverse=True)
print(res) #['gyp', 'pyg', 'psy', 'xk']

```

**27、Python 获取当前日期？**

```
import time
import datetime
print(datetime.datetime.now()) #2019-04-03 17:06:16.347417
print(time.strftime('%Y-%m-%d %H:%M:%S'))  #2019-04-03 17:06:51

```

**28、简述5条：Python的pep8-代码规范**

不要在行尾加分号, 也不要用分号将两条命令放在同一行 不要使用反斜杠连接行 不要在返回语句或条件语句中使用括号 顶级定义之间空2行, 方法定义之间空1行，顶级定义之间空两行 如果一个类不继承自其它类, 就显式的从object继承

**29、Fibonacci 数列**

```
def func(n):
    a,b=0,1
    while n:
        yield b
        a,b=b,a+b
        n-=1
print(list(func(10))) #[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

```

**30、Python 三目运算**

```
#res=a-b if a&gt;b else b-a
#解释：如果a&gt;b成立，返回a-b，否则返回b-a

```

**31、单例模式 【后面会有文章重点介绍单例模式】**

```
class Single():
    __isstance=None
    __first_init=False
    def __new__(cls, *args, **kwargs):
        if not cls.__isstance:
            cls.__isstance=object.__new__(cls)
    def __init__(self,name):
        if not self.__first_init:
            self.name=name
            Single.__first_init=True

```

**32、递归**

```
def digui(n):
    if n==1:
        return 1
    else:
        return (n*digui(n-1))
print(digui(4))  #24

```

**33、统计字符串每个单词出现的次数**

```
from collections import Counter
s3='kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h'
print(Counter(s3))  #Counter({'l': 9, ';': 6, 'h': 6, 'f': 5, 'a': 4, 'j': 3, 'd': 3, 's': 2, 'k': 1, 'b': 1, 'g': 1})

```

**34、正则 re.complie 作用**

```
#re.complie是将正则表达式编程成一个对象，加快速度，并且可以重复使用
content = 'Hello, I am Jerry, from Chongqing, a montain city, nice to meet you……'
regex=re.compile('\w*o\w*')
res=regex.findall(content)
print(res)  #['Hello', 'from', 'Chongqing', 'montain', 'to', 'you']

```

**35、filter 方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]**

```
a=[1,2,3,4,5,6,7,8,9,10]
res=list(filter(lambda x:x%2,a))
print(res)  #[1, 3, 5, 7, 9]

```

**36、列表推导式求列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]**

```
a=[1,2,3,4,5,6,7,8,9,10]
res=[x for x in a if x%2==1]
print(res)  #[1, 3, 5, 7, 9]

```

37、a=（1，）b=(1)，c=(“1”) 分别是什么类型的数据？

```
a=(1,)
print(type(a))  #&lt;class 'tuple'&gt;
b=(1)
print(type(b))  #&lt;class 'int'&gt;
c=("1")
print(type(c))  #&lt;class 'str'&gt;

```

**37、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9] 【归并排序】 l1=[1,5,7,9] l2=[2,2,6,8]**

```
def merge_sort(l1,l2):
    left_p,right_p=0,0
    result=[]
    while left_p&lt;len(l1) and right_p&lt;len(l2):
        if l1[left_p]&lt;l2[right_p]:
            result.append(l1[left_p])
            left_p+=1
        else:
            result.append(l2[right_p])
            right_p+=1
    result+=l1[left_p:]
    result+=l2[right_p:]
    return result
print(merge_sort(l1,l2))

```

**38、用 python 删除文件和用 linux 命令删除文件方法**

```
"""
python删除文件： os.remove(文件名)
linux命令删除文件： rm 文件名
"""

```

**39、logging 模块的使用？**

```
#logging是日志模块，爬虫时可能用到
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
logger=logging.getLogger('psy')  #psy我设置的文件名
logger.info('Start log')
logger.debug('Do something')
logger.warning('Something maybe fail')
logger.error('Somthing exists error')
logger.critical('Break down')

```

**40、写一段自定义异常代码**

```
def func():
    try:
        for i in range(5):
            if i&gt;2:
                raise Exception('数字大于2')
    except Exception as e:
        print(e)
func() #数字大于2

```

**41、正则表达式匹配中，（.）和（.?）匹配区别？**

```
#（.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配
#（.*?）是非贪婪匹配，会把满足正则的尽可能少匹配
s = "&lt;a&gt;哈哈&lt;/a&gt;&lt;a&gt;呵呵&lt;/a&gt;"
import re
res1 = re.findall("&lt;a&gt;(.*)&lt;/a&gt;", s)
print("贪婪匹配", res1)  #贪婪匹配 ['哈哈&lt;/a&gt;&lt;a&gt;呵呵']
res2 = re.findall("&lt;a&gt;(.*?)&lt;/a&gt;", s)
print("非贪婪匹配", res2)  #非贪婪匹配 ['哈哈', '呵呵']

```

**42、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]**

```
a=[[1,2],[3,4],[5,6]]
new_a=[]
for item in a:
    new_a.extend(item)
print(new_a)  #[1, 2, 3, 4, 5, 6]

res=[j for i in a for j in i]
print(res)  #[1, 2, 3, 4, 5, 6]

```

**43、x=“abc”,y=“def”,z=[“d”,“e”,“f”]，分别求出 x.join(y) 和 x.join(z) 返回的结果**

```
#join()括号里面的是可迭代对象，x插入可迭代对象中间，形成字符串，结果一致
x="abc"
y="def"
z=["d","e","f"]
print(x.join(y))  #dabceabcf
print(x.join(z))  #dabceabcf

```

**44、举例说明异常模块中 try except else finally 的相关意义**

```
"""
try..except..else没有捕获到异常，执行else语句
try..except..finally不管是否捕获到异常，都执行finally语句
"""
#45、python中两个值交换
a,b=1,2
a,b=b,a
print(a,b) #2 1

```

**46、举例说明 zip() 函数用法 zip()函数实质就是整合**

```
l1=[1,2,3,4]
l2=[4,5,6]
res=list(zip(l1,l2))
print(res) #[(1, 4), (2, 5), (3, 6)]

```

**47、a=“张明 98分”，用 re.sub，将 98 替换为 100**

```
import re
a="张明 98分"
res=re.sub(r'\d+','100',a)
print(res)  #张明 100分

```

**48、a="hello"和b="你好"编码成 bytes 类型**

```
a=b"hello"
b="你好".encode()
print(type(a))  #&lt;class 'bytes'&gt;
print(type(b))  #&lt;class 'bytes'&gt;

```

**49、[1,2,3]+[4,5,6]的结果是多少**

```
print([1,2,3]+[4,5,6])  #[1, 2, 3, 4, 5, 6]

```

**50、提高 python 运行效率的方法**

（1）使用生成器，因为可以节约大量内存 （2）循环代码优化，避免过多重复代码的执行 （3）核心模块用Cython PyPy等，提高效率 （4）多线程、多进程、协程 （5）多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序的判断次数，提高效率

**51、遇到 bug 如何处理**

（1）细节上的错误，通过print()打印，能执行到print()说明一般上面的代码没有问题，分段检测程序是否有问题，如果是js的话可以alter活console.log （2）如果涉及一些第三方的框架，会去查找光放文档或者一些技术博客 （3）对于bug的管理与归类总结，一般测试将测试出的bug用teambin等bug管理工具进行记录，然后我们会一条一条进行修改，修改的过程也是理解业务逻辑和提高自己编程逻辑缜密性的方法，然后自己再做一些笔记记录。 （4）导包问题、城市定位多音字造成的显示错误问题

**52、list=[2,3,5,4,9,6]，从小到大排序，不许用 sort，输出[2,3,4,5,6,9]**

```
#若使用sort
l=[2,3,5,4,9,6]
print(sorted(l))  #[2, 3, 4, 5, 6, 9]
#不使用sorted，自己定义函数
def quicksort(old_list):
    if len(old_list)&lt;2:
        return old_list
    else:
        temp=old_list[0]
        lowbeforetemp=[i for i in old_list[1:] if i&lt;=temp]
        bigbeforetemp=[i for i in old_list[1:] if i&gt;temp]
        final_list=quicksort(lowbeforetemp)+[temp]+quicksort(bigbeforetemp)
        return final_list
print(quicksort([2,3,5,4,9,6]))  #[2, 3, 4, 5, 6, 9]

```

**53、两个数相除，保留两位小数**

```
print(round(10/3,2))  #3.33

```

**54、正则匹配，匹配日期 2018-03-20**

```
s='Date：2018/03/20'
import re
res1=re.findall('(\d+)',s)  #['2018', '03', '20']
res='-'.join(res1)
print(res)  #2018-03-20

```

**55、使用 pop 和 del 分别删除字典中的"name"和"age"字段，dic={“name”:“zs”,“age”:18,“sex”:“girl”}**

```
dic={<!-- -->"name":"zs","age":18,"sex":"girl"}
dic.pop("name")
print(dic) #{'sex': 'girl', 'age': 18}
del dic["age"]
print(dic)  #{'sex': 'girl'}

```

**56、简述多线程、多进程** 进程是资源（CPU、内存等）分配的基本单位，它是程序执行时的一个实例。 线程是程序执行时的最小单位，它是进程的一个执行流。 进程有自己的独立地址空间，每启动一个进程，系统就会为它分配地址空间，建立数据表来维护代码段、堆栈段和数据段，这种操作非诚昂贵。 【所以各个进程有自己的地址空间，彼此互相不打扰】 线程是共享进程中的数据的，使用相同的地址空间，因此CPU切换一个线程的花费比进程要小很多，同时创建一个线程的开销也比进程要小很多。

**57、简述 any() 和 all() 方法** #连个返回的都是bool值 all如果存在0 None False返回False,否则返回

```
True;any与之相反
print(all([0,1,2,3]))  #False
print(all([1,2,3]))  #True
print(any([0,1,2,3]))  #True
print(any([0,False,None]))  #False

```

**58、异常分类**

```
"""
IOError 输入输出异常
AttributeError 试图访问一个对象没有的属性
ImportError 无法引入模块或包，基本都是路径的问题
IndentationError 语法错误，代码没有正确的对齐
KeyError 试图访问你字典里不存在的键
SyntaxError Python代码逻辑语法出错，不能执行
NameError 使用一个还未赋予对象的变量
"""

```

**59、Python 中 copy 和 deepcopy 区别 【深拷贝和浅拷贝】**

```
import copy
#copy的使用
l1=[1,2,[3,4]]
l2=copy.copy(l1)
print(id(l1)==id(l2))  #False  两者id不相同
l1.append(5)
l1[2].append(5)
print(l1)  #[1, 2, [3, 4, 5], 5]
print(l2)  #[1, 2, [3, 4, 5]]
#deepcopy的使用
l1=[1,2,[3,4]]
l2=copy.deepcopy(l1)
print(id(l1)==id(l2))  #False  两者id不相同
l1.append(5)
l1[2].append(5)
print(l1)  #[1, 2, [3, 4, 5], 5]
print(l2)  #[1, 2, [3, 4]]
"""
copy()和deepcopy()是Python语言copy模块中的两个method，copy()其实是与deep copy相对的shallow copy。
对于简单的object,用shallow copy和deep copy没区别。
复杂的Object,如list中套着list的情况,shallow copy中的子list并未从原object真的独立出来，因此如果你改变原object的子list中的一个元素，你的copy就会跟着一起改变。
deep copy则更加符合我们对复制的直觉定义：一旦复制出来了，就应该是独立的了。
"""

```

**60、在python数据处理中的复制方法（下面介绍3种，需要导入numpy库）**

```
import numpy as np

```

**方法一：b=a 【此时：b和a实际指向同一个东西，改变a或b，两者一起发生变化】**

```
a=np.arange(12)
b=a
b.shape=(3,4)
print(a.shape)  #(3, 4)
print(id(a)==id(b))  #True

```

**方法二：c=a.view() 【此时：c和a不是指向同一个东西，但是共用一堆值】** a=np.arange(12)

```
c=a.view()
c.shape=(3,4)
print(a.shape)  #(12,)
print(id(a)==id(c))  #False

```

**方法三：d=a.copy() 【此时：d和a各自为各自的值，没有一点关系】**

```
a=np.arange(12)
d=a.copy()
d[0]=5
print(a)  #[ 0  1  2  3  4  5  6  7  8  9 10 11]
print(d)  #[ 5  1  2  3  4  5  6  7  8  9 10 11]
print(id(a)==id(d))  #False

```

**61、列出几种魔法方法并简要介绍用途**

```
"""
__init__ 对象初始化方法
__new__  创建对象时执行的方法，单例模式会用到
__str__ 当时用print输出对象时，只要自己定义了__str__(self)方法，则就打印在这个方法中return的数据   【必须要有return】
__del__  删除对象执行的方法
"""

```

**62、上下文管理器 with…as 的实现**

上下文管理器(context manager)用于规定某个对象的使用范围。一旦进入或者离开该使用范围，会有特殊操作被调用 比如为对象分配或者释放内存)。 它的语法形式是with…as… 常用的上下文管理器： with open(‘test.txt’,‘w’)as f:f.write(‘Hello World!’) open函数既能够当做一个简单的函数使用，又能够作为上下文管理器。这是因为open函数返回了一个文件类型变量。

要实现上下文管理器，必须实现两个方法：一个负责进入语句块的准备操作（**enter** 方法），另一个负责离开语句块的善后操作（**exit** 方法）。 当一个对象被用作上下文管理器时： **enter** 方法将在进入代码块前被调用。 **exit** 方法则在离开代码块之后被调用(即使在代码块中遇到了异常)。

自己实现的上下文管理方法，

```
class PypixOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        self.openedFile = open(self.filename, self.mode)
        return self.openedFile
    def __exit__(self, *unused):
        self.openedFile.close()
with PypixOpen(filename, mode) as writer:
    writer.write("Hello World from our new Context Manager!")

```

**注意：** （1）我们完全忽视了语句块内部可能出现的问题。 （2）如果语句块内部发生了异常，__exit__方法将被调用，而异常将会被重新抛出(re-raised)。 当处理文件写入操作时，大部分时间你肯定不希望隐藏这些异常，所以这是可以的。 而对于不希望重新抛出的异常，我们可以让__exit__方法简单的返回True来忽略语句块中发生的所有异常(大部分情况下这都不是明智之举)。 （3）上面代码*unused 指向exc_type, exc_value, traceback三个参数，当程序块中出现异常(exception)，这三个参数用于描述异常。 我们可以根据这三个参数进行相应的处理。如果正常运行结束，这三个参数都是None。

**给出的答案**

```
class Close():
    def __init__(self,obj):
        self.obj=obj
    def __enter__(self):
        return self.obj  #返回作为as目标
    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.obj.close()
        except AttributeError:
            print(exc_type)

```

63、python arg.py 1 2 命令行启动程序并传参，print(sys.argv) 会输出什么数据？

```
#[arg.py 1 2]

```

**64、请将[i for i in range(3)]改成生成器**

```
class iter():
    def __init__(self,data):
        self.data=data
        self.loop=-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.loop&gt;=self.data:
            raise StopIteration
        self.loop+=1
        return self.loop
Iter=iter(range(3))
print(Iter)  #&lt;__main__.iter object at 0x000001BA9D92F898&gt;
print(Iter.__iter__())  #&lt;__main__.iter object at 0x0000016888BDF898&gt;
print(Iter.data)  #range(0, 3)
print(Iter.__next__)  #&lt;bound method iter.__next__ of &lt;__main__.iter object at 0x0000016888BDF898&gt;&gt;

"""
#列表解析生成列表  [x*x for x in range(3)]  结果：[0,1,4]
#生成器表达式      (x*x for x in range(3))  结果：(0,1,4)
#两者之间的转换    list(x*x for x in range(3))  结果[0,1,4]
"""

```

**65、字符串转化大小写？**

```
s='MyDay'
print(s.upper())  #MYDAY
print(s.lower())  #myday

```

**66、请说明 sort 和 sorted 对列表排序的区别**

```
l=[2,4,1,3,8,6,5]
l.sort()
print(l)  #[1, 2, 3, 4, 5, 6, 8]
l=[2,4,1,3,8,6,5]
print(sorted(l))  #[1, 2, 3, 4, 5, 6, 8]
"""

```

（1）sort()与sorted()的不同在于：sort()是在原位重新排列列表，而sorted()是产生一个新的列表 sorted(L)返回一个排序后的L，不改变原始的L；L.sort()是对原始的L进行操作，调用后原始的L会改变，没有返回值 所以a=a.sort()是错的，a=sorted(a)才对！ （2）sorted()适用于任何可迭代容器，list.sort()仅支持list （3）基于以上两点，sorted的使用频率比list.sort()更高些

**67、对 foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4] 进行排序，使用 lambda 函数从小到大排序**

```
#方法一：直接使用list.sort()
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
foo.sort()
print(foo)  #[-20, -5, -4, -4, -2, 0, 2, 4, 8, 8, 9]
#方法二：使用lambda函数
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
res=sorted(foo,key=lambda x:x)
print(res)  #[-20, -5, -4, -4, -2, 0, 2, 4, 8, 8, 9]
68、对 foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4] 进行排序，将正数从小到大，负数从大到小
foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
res=sorted(foo,key=lambda x:(x&lt;0,abs(x)))
print(res)  #[0, 2, 4, 8, 8, 9, -2, -4, -4, -5, -20]
#69、Python 传参数是传值还是传址？

"""
Python 中函数参数是引用传递（注意不是值传递）。
对于不可变类型（数值型、字符串、元组），因变量不能修改，所以运算不会影响到变量自身；
而对于可变类型（列表字典）来说，函数体运算可能会更改传入的参数变量。
"""

```

**70、w、w+、r、r+、rb、rb+ 文件打开模式区别**

r 以只读方式打开文件。文件的指针会被放在文件的开头。这是默认模式。 w 打开一个文件只用于写入。如果该文件已存在则将其覆盖，如果该文件不存在，创建新文件。 a 打开一个文件用于追加。如果该文件存在，文件指针将会放在文件的结尾。也就是说：新的内容会被写入到已有内容之后。 如果该文件不存在，创建新文件进行写入。 rb 以二进制格式打开一个文件用于只读。文件指针会放在文件的开头。这是默认模式。 wb 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 ab 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是：新的内容会被写入到已有内容之后。 如果该文件不存在，创建新文件进行写入。 r+ 打开一个文件用于读写。文件指针将会放在文件的开头。 w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会时追加模式。 如果该文件不存在，创建新文件进行写入。 rb+ 以二进制格式打开一个文件用于读写。文件指针会放在文件的开头。 wb+ 以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 ab+ 以二进制格式打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。 如果该文件不存在，创建新文件进行写入。

**71、int(“1.4”)、int(1.4)的输出结果？**

```
print(int("1.4"))  #报错ValueError: invalid literal for int() with base 10: '1.4'
print(int(1.4))  #1

```

**72、Python 垃圾回收机制？** “”" **（1）引用计数**

```
import sys
str1='hello world'
print(sys.getrefcount(str1)) #在python解释器下运行，为2  创建一次，调用一次

```

**（2）分代计数** Python默认定义了三代对象集合，索引数越大，对象存活时间越长 Python中使用了某些启发式算法（heuristics）来加速垃圾回收。 【例如，越晚创建的对象更有可能被回收。对象被创建之后，垃圾回收器会分配它们所属的代（generation）。每个对象都会被分配一个代，而被分配更年轻代的对象是优先被处理的。】 **（3）引用循环** 垃圾回收器会定时寻找这个循环，并将其回收。 举个例子，假设有两个对象o1和o2，而且符合o1.x == o2和o2.x == o1这两个条件。如果o1和o2没有其他代码引用，那么它们就不应该继续存在。但它们的引用计数都是1。 “”" **73、Python 字典和 json 字符串相互转化方法 【序列化和反序列化】**

```
import json
dic={<!-- -->"name":"psy","age":18}
#序列化  把python的对象编码转换为json格式的字符串
res1=json.dumps(dic)
print(res1,type(res1))  #{"age": 18, "name": "psy"} &lt;class 'str'&gt;     【json中一般使用""】
#反序列化 把json格式字符串解码为python数据对象。
res2=json.loads(res1)
print(res2,type(res2))  #{'name': 'psy', 'age': 18} &lt;class 'dict'&gt;

```

**74、Python 正则中 search 和 match 的区别**

```
"""
match() 从第一个字符开始找, 如果第一个字符就不匹配就返回 None, 不继续匹配. 用于判断字符串开头或整个字符串是否匹配,速度快。 
search() 会整个字符串查找,直到找到一个匹配。
"""
import re
str1='superman'
str2='hello superman'
print(re.match('super',str1))  #&lt;_sre.SRE_Match object; span=(0, 5), match='super'&gt;
print(re.match('super',str1).span())  #(0, 5)
print(re.match('super',str2))  #None

print(re.search('super',str1))  #&lt;_sre.SRE_Match object; span=(0, 5), match='super'&gt;
print(re.search('super',str1).span())  #(0, 5)
print(re.search('super',str2))  #&lt;_sre.SRE_Match object; span=(6, 11), match='super'&gt;
print(re.search('super',str2).span())  #(6, 11)

```

**75、Python 中读取 Csv、Excel 文件的方法？**

```
import pandas as pd
#read_csv=pd.read_csv('test1.csv')
#read_excel=pd.read_excel('test2.xlsx')

```

**76、输入日期， 判断这一天是这一年的第几天？**

```
import datetime
def DayOfYear():
    year=input('请输入年份：').strip()
    mon=input('请输入月份：').strip()
    day=input('请输入日：').strip()
    data1=datetime.date(year=int(year),month=int(mon),day=int(day))
    data2=datetime.date(year=int(year),month=1,day=1)
    return (data1-data2).days+1
print(DayOfYear())
"""运行结果：
请输入年份：2019
请输入月份：4
请输入日：18
108
"""

```

**77、什么是 lambda 函数？有什么好处？**

lambda 函数是一个可以接收任意多个参数（包括可选参数）并且返回单个表达式值的匿名函数 好处： （1）lambda 函数比较轻便，即用即删除，很适合需要完成一项功能，但是此功能只在此一处使用，连名字都很随意； （2）匿名函数，一般用来给filter，map这样的函数式编程服务； （3）作为回调函数，传递给某些应用，比如消息处理

**78、求两个列表的交集、差集、并集** **set()集合中有关于交集、差集、并集的方法 交集intersection() 差集difference 并集union**

```
a=[1,2,3,4]
b=[4,3,5,6]
jj1=[i for i in a if i in b]
jj2=list(set(a).intersection(set(b)))
print('交集：',jj1,jj2)  #交集： [3, 4] [3, 4]
cj1=list(set(a).difference(set(b)))
cj2=list(set(b).difference(set(a)))
print('差集：',cj1,cj2)  #差集： [1, 2] [5, 6]
bj=list(set(a).union(set(b)))
print('并集',bj)  #并集 [1, 2, 3, 4, 5, 6]
**79、什么是负索引？**
#与正索引不同，负索引是从右边开始检索

```

**80、正则匹配不是以4和7结尾的手机号？**

```
import re
tels=["13100001234","18912344321","10086","18800007777"]
#方法1：
for item in tels:
    if len(item)!=11 or item.endswith('4') or item.endswith('7'):
        print('{}不是想要的手机号'.format(item))
    else:
        print('{}是想要的手机号'.format(item))
#方法二：
for item in tels:
    res=re.match("1\d{9}[0-3,5-6,8-9]",item)
    if res:
        print('{}是想要的手机号'.format(res.group()))
    else:
        print('{}不是想要的手机号'.format(item))

```

**81、用两种方法去空格？**

```
str="hello world ha ha"
res1=str.replace(' ','')
print(res1)  #helloworldhaha
res2_l=str.split(' ')
res2=''.join(res2_l)
print(res2)  #helloworldhaha

```

**82、统计字符串中某字符出现次数？**

```
str="张三 哈哈 张三 呵呵 张三"
from collections import Counter
l=str.split(' ')
res=Counter(l)
print(res)  #Counter({'张三': 3, '哈哈': 1, '呵呵': 1})
print(Counter(l)['张三'])  #3
print(str.count('张三'))  #3

```

**83、正则表达式匹配 URL**

```
str = 'Its after 12 noon, do you know where your rooftops are? 
import re
pattern=re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
url=re.findall(pattern,str)
print(url)

```

**84、正则匹配以 163.com 结尾的邮箱？**

```
email_list= ["sdgaozhe@163.com","xiaoWang@163.comheihei", ".com.602556194g@qq.com" ]
import re
for item in email_list:
    res=re.match('[\w]{4,20}@163\.com$',item)
    if res:
        print('{}符合规定的邮件地址，匹配的结果是：{}'.format(item,res.group()))
    else:
        print('{}不符合规定的邮件地址'.format(item))

```

**85、s=“info:xiaoZhang 33 shandong”,用正则切分字符串输出[‘info’, ‘xiaoZhang’, ‘33’, ‘shandong’]**

```
s="info:xiaoZhang 33 shandong"
import re
res=re.split(r":| ",s)    #|表示或，根据:或 切分
print(res)  #['info', 'xiaoZhang', '33', 'shandong']

```

**86、两个有序列表，l1,l2，对这两个列表进行合并不可使用 extend 【很前面的一题很像…】**

```
l1=[1,4,7]
l2=[2,5,6]
l1.extend(l2)
print(l1)  #[1, 4, 7, 2, 5, 6]     【无序】

l1=[1,4,7]
l2=[2,5,6]
def merge_sort(l1,l2):
    left_p,right_p=0,0
    result=[]
    while left_p&lt;len(l1) and right_p&lt;len(l2):
        if l1[left_p]&lt;l2[right_p]:
            result.append(l1[left_p])
            left_p+=1
        else:
            result.append(l2[right_p])
            right_p+=1
    result+=l1[left_p:]
    result+=l2[right_p:]
    return result 
print(merge_sort(l1,l2))  #[1, 2, 4, 5, 6, 7]

```

**87、代码描述列表推导式、字典推导式、生成器？**

```
import random
tds_list=[i for i in range(10)]
print('列表推导式',tds_list,type(tds_list))  #列表推导式 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] &lt;class 'list'&gt;
tds_dict={<!-- -->k:random.randint(4,9) for k in ["a","b","c","d"]}
print('字典推导式',tds_dict,type(tds_dict))  #字典推导式 {'d': 9, 'c': 6, 'a': 9, 'b': 7} &lt;class 'dict'&gt;
generate=(i for i in range(10))
print('生成器',generate,type(generate))  #生成器 &lt;generator object &lt;genexpr&gt; at 0x0000021C8A507410&gt; &lt;class 'generator'&gt;

```

**88、根据键对字典排序，不可使用zip？**

```
dic = {<!-- -->"name":"zs","sex":"man" ,"city":"bj"}
#对字典按键key进行排序
res1=sorted(dic.items(),key=lambda x:x[0])
print(res1)  #[('city', 'bj'), ('name', 'zs'), ('sex', 'man')]
#对字典的值value进行排序
res2=sorted(dic.items(),key=lambda x:x[1])
print(res2)  #[('city', 'bj'), ('sex', 'man'), ('name', 'zs')]

```

**89、阅读一下代码他们的输出结果是什么？**

```
def multi():
    return [lambda x : i*x for i in range(4)]
print([m(2) for m in multi()])  #[6, 6, 6, 6]
"""
**分析：这是一个闭包,下面是闭包定义： 
1、闭包是一个嵌套函数 
2、闭包必须返回嵌套函数 
3、嵌套函数必须引用一个外部的非全局的局部自由变量**
def multi():
    func_list=[]
    for i in range(4):
        def lam(x):
            return i*x
        func_list.append(lam)
    return func_list
在python里，相对而言的局部变量绑定的是值，非局部变量绑定的是空间， 而不是值本身。
所以，for循环生成的i，相对于函数lam来说，是全局变量，所以绑定的是i所在的内存地址，但i最后变成了3，lam绑定的是3。
所以导致了,生成的四个函数所得值时相同的.

那实现结果为[0,2,4,6]呢? 按照刚才的思路,我们只需将lam函数中的i变成局部变量,则函数lam绑定的就是值,而不是内存地址：
def mul():
    func_list=[]
    for i in range(4):
        def lam(x,n=i):  #这时候因为n是局部变量，所以绑定的是n的值
            return x*n
        func_list.append(lam)
    return func_list
print([m(2) for m in mul()])  #[0, 2, 4, 6]
"""

```

**90、代码实现 Python 的线程同步，在屏幕上依次打印10次“ABC”**

```
from threading import Thread,Lock
mutex=Lock()
def print1(lock):
    lock.acquire()
    print('A')
    lock.release()
def print2(lock):
    lock.acquire()
    print('B')
    lock.release()
def print3(lock):
    lock.acquire()
    print('C')
    lock.release()
for i in range(10):
    t1=Thread(target=print1,args=(mutex,))
    t1.start()
    t1.join()
    t2 = Thread(target=print2, args=(mutex,))
    t2.start()
    t2.join()
    t3 = Thread(target=print3, args=(mutex,))
    t3.start()
    t3.join()

```

**91、简述 read、readline、readlines 的区别？**

read 读取整个文件 readline 读取下一行，使用生成器方法 readlines 读取整个文件到一个迭代器以供我们遍历

**92、a=" hehheh "去除首尾空格**

```
a="  hehheh  "
print(a.strip())  #hehheh

```

**93、yield方法**

yield就是保存当前程序执行状态。 你用for循环的时候，每次取一个元素的时候就会计算一次。用yield的函数叫generator,和iterator一样。 它的好处是不用一次计算所有元素，而是用一次算一次，可以节省很多空间，generator 每次计算需要上一次计算结果，所以用yield,否则一旦return，上次计算结果就没了。

**94、字符串 “123” 转换成 123，不使用内置 API，例如 int()**

```
def change(s):
    num=0
    for item in s:
        n=eval(item)  #此时n为int类型
        num=num*10+n
    return num
res=change('123')
print(res,type(res))  #123 &lt;class 'int'&gt;

```

**95、is 和 == 的区别**

```
 **is 比较的是内存地址   == 比较内容和数据类型**
a=[1,2,3]
b=a
print(id(a),id(b))  #1753026079880 1753026079880
print(a is b)  #True
print(a == b)  #True

import copy
c=copy.deepcopy(a)
print(id(a),id(c))  #1753026079880 1753026098120
print(a is c)  #False
print(a==c)  #True

```

**96、有没有一个工具可以帮助查找 python 的 bug 和进行静态的代码分析？**

PyChecker是一个python代码的静态分析工具，它可以帮助查找python代码的bug，会对代码的复杂度和格式提出警告Pylint是另外一个工具可以进行codingstandard检查

**97、文件递归**

```
import os
def print_directory_contents(s_path):
    """
    这个函数接收文件夹的名称作为输入参数
    返回该文件夹中文件的路径
    以及其包含文件夹中文件的路径
    """
    for s_child in os.listdir(s_path):
        s_child_path = os.path.join(s_path, s_child)
        if os.path.isdir(s_child_path):
            print_directory_contents(s_child_path)
        else:
            print(s_child_path)
print_directory_contents('D:\QQ')  #D:\QQ\QQ_Setup.exe

```

**98、Python 如何copy一个文件？**

```
#shutil 模块有一个 copyfile 函数可以实现文件拷贝  copyfile(source_file, destination_file)**
from shutil import copyfile
copyfile('test.py','test_new.py')  #把该目录下的test.py复制到相同目录下的test_new.py

```

**99、打乱一个排好序的 list 对象 alist？**

```
import random
alist = [1, 2, 3, 4, 5]
random.shuffle(alist)
print(alist)  #[4, 1, 2, 3, 5]
**100、对 s="hello"进行反转**

s="hello"
print(s[::-1])  #olleh

```

**101、Python 中单下划线和双下划线使用**

**foo**:一种约定,Python内部的名字,用来区别其他用户自定义的命名,以防冲突，就是例如__init__(),**del**(),**call**()这些特殊方法 _foo:一种约定,用来指定变量私有.程序员用来指定私有变量的一种方式.不能用from module import * 导入，其他方面和公有一样访问； __foo:这个有真正的意义:解析器用_classname__foo来代替这个名字,以区别和其他类相同的命名,它无法直接像公有成员一样随便访问,通过对象名._类名__xxx这样的方式可以访问.

**102、反转一个整数**

```
class Solution(object):
    def reverse(self, x):
        if -10 &lt; x &lt; 10:
            return x
        str_x = str(x)
        if str_x[0] != "-":
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[1:][::-1]
            x = int(str_x)
            x = -x
        return x if -2147483648 &lt; x &lt; 2147483647 else 0
s=Solution()
res=s.reverse(-120)
print(res)  #-21

```

**103、代码描述静态方法 (staticmethod)，类方法(classmethod) 和实例方法**

```
class Method():
    def foo(self,x):
        print('running foo {}-{}'.format(self,x))
    @classmethod
    def class_foo(cls,x):
        print('running class_foo {}-{}'.format(cls,x))
    @staticmethod
    def static_foo(x):
        print('running static_foo {}'.format(x))
m=Method()
m.foo('psy')  #running foo &lt;__main__.Method object at 0x000002498DF18B00&gt;-psy
m.class_foo('psy')  #running class_foo &lt;class '__main__.Method'&gt;-psy
m.static_foo('psy')  #running static_foo psy

```

**104、新式类和旧式类的区别？**

a. 在python里凡是继承了object的类，都是新式类 b. Python3里只有新式类 c. Python2里面继承object的是新式类，没有写父类的是经典类 d. 经典类目前在Python里基本没有应用

**105、请写出一个在函数执行后输出日志的装饰器以及计时器**

```
"""
简单的装饰器模板：
def outter(func):
    def wrapper(*args,**kwargs):
        f=func()
    return wrapper
    
def timmer(func):  #计时器
    def wrapper(*args,**kwargs):
        start=time.time()
        func(*args,**kwargs)
        end=time.time()
        spend=round(end-start,2)
        print('该程序执行花费时间为{}'.format(spend))
    return wrapper
"""
def do_log(func):  #日志装饰器
    def wrapper(*args,**kwargs):
        if func.__name__=='debug':
            msg="debug {}".format(args[0])
        elif func.__name__=='info':
            msg="info {}".format(args[0])
        else:
            msg="{} {}".format(func.__name__,args[0])
        return func(msg,**kwargs)
    return wrapper
@do_log
def debug(msg):
    print(msg)
@do_log
def info(msg):
    print(msg)
debug('123')  #debug 123
info('456')  #info 456

```

**106、请解释一下协程的优点**

子程序切换不是线程切换，而是由程序自身控制 没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显 不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁

**107、闭包必须满足那几点**

1.必须有一个内嵌函数 2.内嵌函数必须引用外部函数中的变量 3.外部函数的返回值必须是内嵌函数

**108、面试技巧**

**你的缺点是什么？** 缺点真的是一个非常不好答的问题，但是只要掌握了以下这个原则，这道问题也只是小菜一碟，那就是：避重就轻。 什么是重？性格方面的问题，人际方面的问题，工作能力方面的原因。如果你说：“我的缺点就是耐心太差”，“我的缺点就是沟通能力有待提高”，那你真的是一个大傻帽。 什么是轻？举点例子：我方向感不太好，不善于理财（金融岗位除外）之类的。有人会问了，我说了这些缺点，面试官会不会觉得我很虚伪？那我告诉你，只要你的虚伪不至于让他想吐（比如“我最大的缺点就是太追求完美”），那虚伪绝对要比傻乎乎的坦诚好。

**你有什么想问我的吗？** 一般问到这个问题，整个面试就要结束了，但是不要掉以轻心，因为最后这个问题决定了面试官对你的最终印象。 所以这个问题背后的潜台词是什么呢？那就是：你还想了解一些什么，帮助你更好地留在这个公司？换言之，就是你有多想留在这个公司？ 如果你说“没有”，那么面试官说不定心里咯噔一下：原来你对这个职位兴趣也就这点啊……这个问题其实给了你表忠心的机会，你可以很认真地问她：“那如果我来到了这个公司，那每天的日常大概会是什么样的？”或者“这个公司的氛围是什么样的？”（暗示你来这里工作的强烈欲望）。

**109、对列表去重并保持原来的顺序**

```
#方法一
l1=[11,2,3,22,2,4,11,3]
res=[]
for item in l1:
    if item not in res:
        res.append(item)
print(res)  #[11, 2, 3, 22, 4]
#方法二：利用sort方法
l1=[11,2,3,22,2,4,11,3]
l2=list(set(l1))   #将列表用set去重，再转换回列表（没有按照之前的顺序）
l2.sort(key=l1.index)  #将上一步得到的列表排序，按照l1中的顺序排序
print(l2)  #[11, 2, 3, 22, 4]

```

**110、#将列表中的数据按照age排序**

```
l=[{<!-- -->"name":"psy","age":18},{<!-- -->"name":"mama","age":54},{<!-- -->"name":"baba","age":55},{<!-- -->"name":"xk","age":24},{<!-- -->"name":"gyp","age":25}]
l.sort(key=lambda x:x["age"])
print(l)  #[{'name': 'psy', 'age': 18}, {'name': 'xk', 'age': 24}, {'name': 'gyp', 'age': 25}, {'name': 'mama', 'age': 54}, {'name': 'baba', 'age': 55}]

```

**111、下面的输出是什么**

```
def extend_list(v,li=[]):
    li.append(v)
    return li
list1=extend_list(10)
list2=extend_list(123,[])
list3=extend_list('a')
print(list1)  #[10,'a']
print(list2)  #[123]
print(list3)  #[10,'a']
print(list1 is list3)  #True

```

**112、下列代码的输出结果是什么？**

```
l=['a','b','c','d','e']
print(l[10:])   #[]

```

**113、下面代码执行完的输出**

```
def func(m):
    for k,v in m.items():
        m[k+2]=v+2
m={<!-- -->1:2,3:4}
l=m  #浅拷贝
l[9]=10
func(l)
m[7]=8
print("l:",l)
print("m:",m)

"""
结果=====》报错如下：
Traceback (most recent call last):
  File "E:/000文章的代码/0000_2018老男孩教育上海python脱产班vip/python面试题/题目3.py", line 11, in &lt;module&gt;
    func(l)
  File "E:/000博客文章的代码/0000_2018老男孩教育上海python脱产班vip/python面试题/题目3.py", line 5, in func
    for k,v in m.items():
RuntimeError: dictionary changed size during iteration
#【原理！】
    在迭代一个列表或者字典的时候，不能修改列表或字典的大小！！！！！！
"""

```

**114、#4种操作的比较：= 切片 copy deepcopy**

```
import copy
l1=[11,22,[33,44]]
l2=l1
l3=l1[:]
l4=copy.copy(l1)
l5=copy.deepcopy(l1)

l1[2].append(55)
print(l1)  #[11, 22, [33, 44, 55]]
print(l2)  #[11, 22, [33, 44, 55]]
print(l3)  #[11, 22, [33, 44, 55]]
print(l4)  #[11, 22, [33, 44, 55]]
print(l5)  #[11, 22, [33, 44]]

```

**115、Python中字符串的格式化（%和format），你一般用哪种，为什么？** 答：1、简单的用%，超过两个值的一般都用format 2、如果一个字符串格式化的时候变量是一个元祖的话，利用%容易犯错；并且在python3里面都推荐使用format进行格式化！

```
"""
#控制精度
print('{:.2f}'.format(3.141592653))  #3.14
#千位分隔符【金钱显示】
res='{:,}'.format(1234567890)
print(res)  #1,234,567,890

```

**116、生成如下列表：[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8],[0,3,6,9,12]]**

```
#方式一
list1=[]
for i in range(4):
    tmp=[]
    for j in range(5):
        tmp.append(i*j)
    list1.append(tmp)
print(list1)  #[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12]]
#方式二
res=[[i*j for j in range(5)] for i in range(4)]
print(res)  #[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12]]

```

**117、装饰器知识点**

1.装饰器的原理及为什么要用装饰器 2. 装饰器的基本用法 3. 带参数的装饰器 4. 被装饰的函数有返回值怎么处理 5. 多个装饰器的执行顺序 6. 装饰类的装饰器

**118、os和sys都是干什么的**

```
#os是和系统相关的，sys是与系统交互有关的
import os  
BASE_DIR=os.path.abspath(__file__)  #取当前文件的绝对路径   
base_dir=os.path.dirname(os.path.abspath(__file__))  #取当前文件的父目录的路径   #E:\000文章的代码\27
path=os.path.join(base_dir,"abc")  #在当前父目录下拼接一个abc的文件夹目录  
path1=base_dir+"\\abc"  #不建议使用这种硬编码的形式拼接路径  
import sys
sys.path.append()  #向当前运行的环境变量中添加一个指定的路径
sys.argv  #返回一个列表，用户在cmd中输入的参数

```

**119、面向对象的三大特性：** 封装、继承、多态 **120、谈谈你对面向对象的理解？** 面向对象的理解 在我理解,面向对象是向现实世界模型的自然延伸，这是一种“万物皆对象”的编程思想。在现实生活中的任何物体都可以归为一类事物，而每一个个体都是一类事物的实例。 面向对象有三大特性，封装、继承和多态。 封装就是将一类事物的属性和行为抽象成一个类，使其属性私有化，行为公开化，提高了数据的隐秘性的同时，使代码模块化。这样做使得代码的复用性更高。 继承则是进一步将一类事物共有的属性和行为抽象成一个父类，而每一个子类是一个特殊的父类–有父类的行为和属性，也有自己特有的行为和属性。这样做扩展了已存在的代码块，进一步提高了代码的复用性。 如果说封装和继承是为了使代码重用，那么多态则是为了实现接口重用。多态的一大作用就是为了解耦–为了解除父子类继承的耦合度。如果说继承中父子类的关系式IS-A的关系，那么接口和实现类之之间的关系式HAS-A。简单来说，多态就是允许父类引用(或接口)指向子类(或实现类)对象。很多的设计模式都是基于面向对象的多态性设计的。 总结一下，如果说封装和继承是面向对象的基础，那么多态则是面向对象最精髓的理论。掌握多态必先了解接口，只有充分理解接口才能更好的应用多态。

**121、python面向对象中的继承有什么特点？**

继承的优点： 1、建造系统中的类，避免重复操作。 2、新类经常是基于已经存在的类，这样就可以提升代码的复用程度。 继承的特点： 1、在继承中基类的构造（**init**()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。有别于C# 2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数 3、Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。

**122、面向对象深度优先和广度优先是什么？**

"深度优先遍历"考察递归, 将子节点为空作为终止递归的条件 "广度优先遍历"考察队列的结构, 消除父节点(出队列,顺便打印), 添加子节点(进队列),当队列内元素个数为零, 完成遍历 python3中不区分深度优先和广度优先 python2中才区分

**123、面向对象中super的作用？**

super() 函数是用于调用父类(超类)的一个方法。 super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。 MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。

```
"""
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Male(Person):
    def __init__(self,name,age,location):
        super().__init__(name,age)
        self.location=location
man=Male('psy',18,'nuist')

```

**124、编写Python脚本，分析xx.log文件，按域名统计访问次数**

```
import re
#1读取文本
with open('xx.log','r',encoding='utf-8')as f:
    data=f.read()
#2取域名
res=re.findall("https://(.*?)/",data)  #返回列表
#3统计
res_dic={<!-- -->}
for item in res:
    if item not in res_dic:
        res_dic[item]=1
    else:
        res_dic[item] +=1
#4排序
res2=sorted(res_dic,key=lambda x:res_dic[x],reverse=True)
for key in res2:
    print(res_dic[key],key)

```

**125、数据库【设计表结构（外键约束怎么建？！）】** 设计 图书管理系统 表结构： - 书（pk 书名） - 作者（pk 姓名） - 出版社（pk 出版社名称 地址） 分析： 一本书只能由一家出版社出版 【多对一，多个出版社对应一本书】<mark>》设置外键，外键放置在“一”的表里面，大家都可以用 一本书可以有多个作者，一个作者也可以写多本书 【多对多】</mark>》通过第三张表，分别与书和作者建立联系

```
"""
"""MySQL中建表的语句
CREATE TABLE book(
    id INT PRIMARY KEY AUTO_INCREMENT,title VARCHAR(64),publisher_id INT,
    FOREIGN KEY (publisher_id) REFERENCES publisher(id));
CREATE TABLE author(
    id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(32));
CREATE TABLE book2author(
    id INT PRIMARY KEY AUTO_INCREMENT,book_id INT,author_id INT,
    FOREIGN KEY (book_id) REFERENCES book(id),
    FOREIGN KEY (author_id) REFERENCES author(id));
CREATE TABLE publisher(
    id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(64),address VARCHAR(255));
"""

```

**阿里模拟笔试题：** 题目： 国内最大的web站点统计服务商CNZZ,监测某客户站点正在进行首页广告位更新，该首页有n个广告位，有3种广告（A,B,C），A广告占用1个广告位，B广告占用2个广告位；C广告占用3个；广告连在一起，可任意组合，为了保证首页的美观，A广告的左右相邻不能出现A广告，B和C则无限制。 问该站点首页有多少种广告位布局方案。 输入：n个广告位 输出：z种布局方案

编译器版本: Python 2.7.6 请使用标准输出(sys.stdout)；已禁用图形、文件、网络、系统相关的操作，如Process , httplib , os；缩进可以使用tab、4个空格或2个空格，但是只能任选其中一种，不能多种混用；如果使用sys.stdin.readline，因为默认会带换行符，所以要strip(’ ')进行截取；建议使用raw_input() 时间限制: 3S (C/C++以外的语言为: 5 S) 内存限制: 128M (C/C++以外的语言为: 640 M) 输入: 输入：n个广告位，n为大于0的正整数 输出: 输出：z种布局方案，z为大于0的正整数 输入范例: 输入范例：3 输出范例: 输出范例：3

```
"""
#代码
def cut(n,isA):
    if n&lt;=0:
        return 0  #当广告位为0时，返回0
    if n==1:
        return 1  #广告位为1时，返回1 A
    if n==2:
        return 1  #广告位为2时，返回2 B
    if n==3:
        if isA:
            return 2
        else:
            return 3  #广告位为3时，返回2 AB  BA C
    if isA:
        return cut(n-2,False)+cut(n-3,False)
    else:
        return cut(n-1,True)+cut(n-2,False)+cut(n-3,False)
print(cut(6,False))  



```
