
--- 
title:  python中sort和sorted函数 
tags: []
categories: [] 

---
     在学习python的过程中，感觉python中的排序相和c++中的泛型算法还是比较相似的，但相对于c++而言更加简单易用。

python中列表的内置函数sort（）可以对列表中的元素进行排序，而全局性的sorted（）函数则对所有可迭代的序列都是适用的；并且sort（）函数是内置函数，会改变当前对象，而sorted（）函数只会返回一个排序后的当前对象的副本，而不会改变当前对象。

1、内置函数sort（）

原型：sort（fun，key，reverse=False）

参数fun是表明此sort函数是基于何种算法进行排序的，一般默认情况下python中用的是归并排序，并且一般情况下我们是不会重写此参数的，所以基本可以忽略；

参数key用来指定一个函数，此函数在每次元素比较时被调用，此函数代表排序的规则，也就是你按照什么规则对你的序列进行排序；

参数reverse是用来表明是否逆序，默认的False情况下是按照升序的规则进行排序的，当reverse=True时，便会按照降序进行排序。

下面 通过简单的例子进行解说：

（由于个人爱好原因，我的编译器是pycharm，所以接下来的所有示例都是在pycharm中可以运行的。）



```
#coding:utf-8
from operator import attrgetter,itemgetter

list1 = [(2,'huan',23),(12,'the',14),(23,'liu',90)]

#使用默认参数进行排序，即按照元组中第一个元素进行排序
list1.sort()
print list1
#输出结果为[(2, 'huan', 23), (12, 'the', 14), (23, 'liu', 90)]

#使用匿名表达式重写key所代表的函数,按照元组的第二个元素进行排序
list1.sort(key=lambda x:(x[1]))
print list1
#[(2, 'huan', 23), (23, 'liu', 90), (12, 'the', 14)]

#使用匿名表达式重写key所代表的函数,按照元组的第三个元素进行排序
list1.sort(key=lambda x:(x[2]))
print list1
#[(12, 'the', 14), (2, 'huan', 23), (23, 'liu', 90)]

#使用匿名函数重写key所代表的函数，先按照元组中下标为2的进行排序，
# 对于下标2处元素相同的，则按下标为0处的元素进行排序
list1.sort(key=lambda x:(x[2],x[0]))
print list1
#[(12, 'the', 14), (2, 'huan', 23), (23, 'liu', 90)]

#使用operator模块中的itemgetter函数进行重写key所代表的函数，按照下标为1处的元素进行排序
list1.sort(key=itemgetter(1))
print list1
#[(2, 'huan', 23), (23, 'liu', 90), (12, 'the', 14)]

#使用operator模块中的itemgetter函数进行重写key所代表的函数，按照下标为2处的元素进行排序
list1.sort(key=itemgetter(2))
print list1
# [(12, 'the', 14), (2, 'huan', 23), (23, 'liu', 90)]

# 此处可以类比lambda中的排序方法，就不再解释
list1.sort(key=itemgetter(2,0))
print list1
#[(12, 'the', 14), (2, 'huan', 23), (23, 'liu', 90)]
```

对于上述中的匿名函数大家如果 不了解的可以自己去了解一下，这里我就不展开了。

这里我想解释一下operator这个模块中的两个函数：

（1）itemgetter





2、全局函数sorted（）

对于sorted（）函数中key的重写，和sort（）函数中是一样的，所以刚刚对于sort（）中讲解的方法，都是适用于sorted（）函数中，在下面的解释中我也就不再列举了，并且下面将要讲解的key的重写也同样是适用于sort（）函数的，那么为什么不再sort（）函数中列举完呢，那是为了不偏不倚，给大家一个客观地理解。

下面仍然从一个例子切入：



```
from operator import attrgetter
class Data:
    article_name = str()
    readers = 0
    def __init__(self,tpl):
        self.article_name = tpl[0]
        self.readers = tpl[1]
    def getKey(self):
        return self.readers
    def __str__(self):
        return str(str(self.article_name)+str(':')+str(self.readers))

list1 = [Data(("java",100)),Data(("c++",100)),Data(("python",89)),Data(("c++",90))]

#此处调用attrgetter函数使得按照readers进行排序
list2 = sorted(list1,key=attrgetter("readers"))
"""结果为
python:89
c++:90
java:100
c++:100
"""

#此处使得list1先按照article_name进行排序，对于名字相同的再按照readers进行排序
list3 = sorted(list1,key=attrgetter("article_name","readers"))
"""
结果为：
c++:90
c++:100
java:100
python:89
"""

#使用类中的自定义函数也同样可以操作
list4 = sorted(list1,key = Data.getKey)
"""
结果为：
python:89
c++:90
java:100
c++:100
"""
```



对于sorted（）函数，同样可以使用sort（）函数中介绍的方法，大家可以自己进行尝试。

当然最后说一下，在上面所有的例子中我都没有使用到reverse参数，对于这个参数，是用于控制排序的方向的，大家可以自己试试，在这里也就不介绍了。


