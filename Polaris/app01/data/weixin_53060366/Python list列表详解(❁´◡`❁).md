
--- 
title:  Python list列表详解(❁´◡`❁) 
tags: []
categories: [] 

---
## Python list列表详解😊

`Python`中没有数组，但是加入了更加强大的列表。如果把数组看做是一个集装箱，那么 Python 的列表就是一个工厂的仓库。

列表可以存储整数、小数、字符串、列表、元组等任何类型的数据，并且同一个列表中元素的类型也可以不同。

列表会将所有元素都放在一对中括号`[ ]`里面，相邻元素之间用逗号`,`分隔。

```
lst=['hello','python','java',1,2]

```

>  
 注意，在使用列表时，虽然可以将不同类型的数据放入到同一个列表中，但通常情况下不这么做，同一列表中只放入同一类型的数据，这样可以提高程序的可读性。 


### python创建列表

#### 1、使用 [ ] 直接创建列表：

```
lst=[1,2,3,4,5]
name=['tom','jack','july']
emptylist = []  #空列表    

```

#### 2、使用 list() 函数创建列表

```
#将字符串转换成列表
list1 = list("hello")
print(list1)

#将元组转换成列表
tuple1 = ('Python', 'Java', 'C++', 'JavaScript')
list2 = list(tuple1)
print(list2)

#将字典转换成列表
dict1 = {<!-- -->'a':100, 'b':42, 'c':9}
list3 = list(dict1)
print(list3)

#将区间转换成列表
range1 = range(1, 6)
list4 = list(range1)
print(list4)

#创建空列表
print(list())

```

#### 3、访问列表元素

们可以使用索引（Index）访问列表中的某个元素（得到的是一个元素的值），也可以使用切片访问列表中的一组元素（得到的是一个新的子列表）。

```
#使用索引访问
lst[1,2,3,4,5,6]
print(lst[2])
print(lst[-4])  #lst数索引

#使用切片访问列表元素
print(lst[1:4:2])
print(lst[-6: -1])  #使用负数切片

```

#### 4、列表添加元素

使用`+`运算符可以将多个序列连接起来；列表是序列的一种，所以也可以使用`+`进行连接。

```
lst1=['hello','python','c++']
lst2=['java','jsp','Vue']
print(lst1+lst2)

```

>  
 注意：使用`+`会生成一个新的列表，原有的列表不会被改变。 


##### append()方法添加元素

<mark>append() 方法用于在列表的末尾追加元素。添加到列表末尾的数据，它可以是单个元素，也可以是列表、元组等。</mark>

```
l = ['Python', 'C++', 'Java']
#追加元素
l.append('PHP')
print(l)

#追加元组，整个元组被当成一个元素
t = ('JavaScript', 'C#', 'Go')
l.append(t)
print(l)

#追加列表，整个列表也被当成一个元素
l.append(['Ruby', 'SQL'])
print(l)

```

当给 append() 方法传递列表或者元组时，此方法会将它们视为一个整体，作为一个元素添加到列表中，从而形成包含列表和元组的新列表。

##### extend()方法添加元素

extend() 和 append() 的不同之处在于：extend() 不会把列表或者元祖视为一个整体，而是把它们包含的元素逐个添加到列表中。

添加到列表末尾的数据，它可以是单个元素，也可以是列表、元组等，但不能是单个的数字。

添加单个数字会报错：`TypeError: 'int' object is not iterable`，int类型是不可迭代的对象。

```
l=['hello','ds','eqw']
n=[1,2,3,4]
l.extend(n)
print(l)

```

##### insert()方法插入元素

append() 和 extend() 方法只能在列表末尾插入元素，如果希望在列表中间某个位置插入元素，那么可以使用 insert() 方法。

`listname.insert(index , obj)`

index 表示指定位置的索引值。insert() 会将 obj 插入到 listname 列表第 index 个元素的位置。

当插入列表或者元祖时，insert() 也会将它们视为一个整体，作为一个元素插入到列表中，这一点和 append() 是一样的。

```
l = ['Python', 'C', 'Java']
#插入元素
l.insert(1, 'C++')
print(l)

#插入元组，整个元祖被当成一个元素
t = ('C#', 'go')
l.insert(2, t)
print(l)

#插入列表，整个列表被当成一个元素
l.insert(3, ['hello', 'mysql'])
print(l)

#插入字符串，整个字符串被当成一个元素
l.insert(0, "http://c.biancheng.net")
print(l)

```

#### 5、列表刪除元素

##### del：根据索引值删除元素

del 不仅可以删除整个列表，还可以删除列表中的某些元素。

```
lst=['java','python','c','mysql']
del lst[3]
print(lst)

#del 可以删除列表中的单个元素
#del 也可以删除中间一段连续的元素,不包括 end 位置的元素。
del lst[1:3]

#刪除整个
del lst

```

##### pop()：根据索引值删除元素

pop() 方法用来删除列表中指定索引处的元素。如果不写 index 参数，默认会删除列表中的最后一个元素。

```
nums = [40, 36, 89, 2, 36, 100, 7]
nums.pop(3)
print(nums)

```

##### remove()：根据元素值进行删除

remove() 方法只会删除第一个和指定值相同的元素，而且必须保证该元素是存在的，否则会引发 ValueError 错误。

```
nums = [40, 36, 89, 2, 36, 100, 7]
#删除第一个 36
nums.remove(36)
print(nums)

```

##### clear()：删除列表所有元素

clear() 用来删除列表的所有元素，也即清空列表。

```
lst=['java','python','c','mysql']
lst.clear()
print(lst)

```

#### 6、修改列表元素

##### 赋值修改单个元素

修改元素直接根据索引赋值即可。

```
nums = [40, 36, 89, 2, 36, 100, 7]
nums[2] = -26  #使用正数索引
nums[-3] = -66.2  #使用负数索引
print(nums)

```

##### 切片修改多个元素

```
nums = [40, 36, 89, 2, 36, 100, 7]
#修改第 1~4 个元素的值（不包括第4个元素）
nums[1: 4] = [45.25, -77, -52.5]
print(nums)
#运行结果：
[40, 45.25, -77, -52.5, 36, 100, 7]

```

如果对空切片赋值，就相当于插入一组新的元素：

```
nums[4: 4] = [-77, -52.5, 999]
print(nums)
#运行结果：
[40, 36, 89, 2, -77, -52.5, 999, 36, 100, 7]

```

<mark>注意：使用切片语法赋值时，Python 不支持单个值</mark>

但是如果使用字符串赋值，Python 会自动把字符串转换成序列，其中的每个字符都是一个元素：

```
s = list("Hello")
s[2:4] = "XYZ"
print(s)
#运行结果：
['H', 'e', 'X', 'Y', 'Z', 'o']

```

使用切片语法时也可以指定步长（step 参数），但这个时候就要求所赋值的新元素的个数与原有元素的个数相同：

```
nums = [40, 36, 89, 2, 36, 100, 7]
#步长为2，为第1、3、5个元素赋值
nums[1:6:2] = [0.025, -99, 20.5]
print(nums)
#运行结果：
[40, 0.025, 89, -99, 36, 20.5, 7]

```

#### 7、列表查找元素

##### index() 方法

index() 方法用来查找某个元素在列表中出现的位置（也就是索引），如果该元素不存在，则会导致 ValueError 错误，所以在查找之前最好使用 count() 方法判断一下。

```
nums = [40, 36, 89, 2, 36, 100, 7, -20.5, -999]
#检索列表中的所有元素
print( nums.index(2) )
#检索3~7之间的元素
print( nums.index(100, 3, 7) )
#检索4之后的元素
print( nums.index(7, 4) )
#检索一个不存在的元素
print( nums.index(55) )

```

>  
 listname.index(obj, start, end) 
 - listname 表示列表名称，obj 表示要查找的元素，start 表示起始位置，end 表示结束位置。 
 start 和 end 参数用来指定检索范围： 
 -  start 和 end 可以都不写，此时会检索整个列表； -  如果只写 start 不写 end，那么表示检索从 start 到末尾的元素； -  如果 start 和 end 都写，那么表示检索 start 和 end 之间的元素。  


##### count()方法

count() 方法用来统计某个元素在列表中出现的次数。

如果 count() 返回 0，就表示列表中不存在该元素，所以 count() 也可以用来判断列表中的某个元素是否存在。

```
nums = [40, 36, 89, 2, 36, 100, 7, -20.5, 36]
#统计元素出现的次数
print("36出现了%d次" % nums.count(36))
#判断一个元素是否存在
if nums.count(100):
    print("列表中存在100这个元素")
else:
    print("列表中不存在100这个元素")

```

>  
 python list列表讲解结束，学编程最重要的还是多coding！！！ 

