
--- 
title:  python中有哪些属于序列的_python序列类型有哪些 
tags: []
categories: [] 

---
python序列类型有哪些？在Python中什么才是序列类型，通过本文来详细了解。

序列：字符、列表、元组

所有序列都支持迭代

序列表示索引为非负整数的有序对象集合

字符和元组属于不可变序列，列表可变

1)字符

字符串字面量:把文本放入单引号、双引号或三引号中；' '' '''

&gt;&gt;&gt; str1 = ' hello, fanison '

&gt;&gt;&gt; type(str1)

str

如果要使用unicode编码，则在字符之前使用字符u进行标识&gt;&gt;&gt; str2 = u'你好，fanison'

&gt;&gt;&gt; type(str2)

unicode

文档字串：模块、类或函数的第一条语句是一个字符的话，该 字符串就成为文档字符串，可以使用__doc__属性引用；

例：&gt;&gt;&gt; def printName():

"the function is print hello"

print 'hello'

&gt;&gt;&gt; printName.__doc__

运算符：

索引运算符 s[i] 返回一个序列的元素i

切片运算符 s[i:j] 返回一个切片

扩展切片运算符 s[i:j:stride]

例：&gt;&gt;&gt; str3 = 'hello,fanison'

&gt;&gt;&gt; str2[0:]

'hello,fanison' 返回所有元素

&gt;&gt;&gt; str2[0:7]

'hello,f' 返回索引7之前的所有元素

&gt;&gt;&gt; str2[0:7:2]

'hlof' 返回从索引0到6内步径为2的元素，即隔一个取一个

&gt;&gt;&gt; str2[7:0:-2]

'a,le' 从索引7处倒着隔一个取一个取到索引1处

&gt;&gt;&gt; str2[-4:-1]

'iso' 从索引-4处取到-2处

&gt;&gt;&gt; str2[-4::-1]

'inaf,olleh' 从-4处到开始处倒着取

注意：

步径为正表示 正着取，索引从小到大 i &lt; j

步径为负表示 倒着取，索引从大到小 i &gt; j

支持运算：

索引、切片、min()、max()、len()等

len(s) s中的元素个数

min(s) s的最小值

max(s) s的最大值

支持方法：

S.index(sub [,start [,end]]) 找到指定字符串sub首次出现的位置

S.upper() 将一个字符串转换为大写形式

S.lower() 将一个字符串转化为小写形式

S.join(t) 使用s作为分隔符连接序列t中的字符串&gt;&gt;&gt; l1 = list(str1)

&gt;&gt;&gt; l1

['h', 'e', 'l', 'l', 'o', ',', 'f', 'a', 'n', 'i', 's', 'o', 'n']

&gt;&gt;&gt; ''.join(l1)

'hello,fanison' 使用空字符作为分隔符连接列表l1

S.replace(old, new[, count]) 替换一个字符串

&gt;&gt;&gt; str1.replace('fan','FAN')

'hello,FANison'

注意：

使用 help()获取其帮助

&gt;&gt;&gt; help(str.join)

2)列表

列表：容器类型

任意对象的有序集合，通过索引访问其中的元素，可变对象，长度可变，异构，任意嵌套

支持在原处修改

修改指定的索引元素，修改指定的分片，删除语句，内置方法

&gt;&gt;&gt; list1 = [ 1,2,3,'x','n' ]

&gt;&gt;&gt; list1[1]=56

&gt;&gt;&gt; print list1

[1, 56, 3, 'x', 'n']

&gt;&gt;&gt; list1[1:3]=[] 会删除索引1到索引3之前的元素

&gt;&gt;&gt; print list1

[1, 'x', 'n']

&gt;&gt;&gt; del(list1[1]) 使用del函数删除list索引为1的元素

&gt;&gt;&gt; print list1

[1, 'n']

注意：

因为支持原处修改，不会改变内存位置，可使用 id() 查看其位置变化

内置方法：

L.count(value) 计算value值出现的次数

L.append(object) 将一个新元素追加到L末端

L.extend(iterable) 增加合并列表(第二个列表内容会以单个元素追加至末端)&gt;&gt;&gt; l1 = [ 1,2,3 ]

&gt;&gt;&gt; l2 = [ 'x','y','z']

&gt;&gt;&gt; l1.append(l2)

&gt;&gt;&gt; l1

[1, 2, 3, ['x', 'y', 'z']] 使用append方法会以其原有存在形式追加

&gt;&gt;&gt; l1 = [ 1,2,3 ]

&gt;&gt;&gt; l1.extend(l2)

&gt;&gt;&gt; l1

[1, 2, 3, 'x', 'y', 'z'] 注意两种增加的区别

L.pop([index]) 返回元素index并从列表中移除它，如果省略则返回并移除列表最后一个元素

L.remove(key) 移除值为key的元素&gt;&gt;&gt; l1 = [ 'x',2,'abc',16,75 ]

&gt;&gt;&gt; l1.pop(2) pop方法是按索引移除

'abc'

&gt;&gt;&gt; l1

['x', 2, 16, 75]

&gt;&gt;&gt; l1.remove(16) remove方法是按值移除

&gt;&gt;&gt; l1

['x', 2, 75]

L.index(value) 指定值首次出现的位置

L.insert(index, object) 在索引index处插入值&gt;&gt;&gt; l1.insert(1,'abc')

&gt;&gt;&gt; l1

['x', 'abc', 2, 75]

L.sort() 排序

L.reverse() 逆序&gt;&gt;&gt; l1.sort()

[2, 75, 'abc', 'x']

&gt;&gt;&gt; l1.reverse()

['x', 'abc', 75, 2]

l1 + l2: 合并两个列表，返回一个新的列表；不会修改原列表；&gt;&gt;&gt; l1 = [ 1,2,3]

&gt;&gt;&gt; l2 = [ 'x','y','z']

&gt;&gt;&gt; l1 + l2

[1, 2, 3, 'x', 'y', 'z']

l1 * N: 把l1重复N次，返回一个新列表;&gt;&gt;&gt; l1 * 3

[1, 2, 3, 1, 2, 3, 1, 2, 3] 使用id()查看是否生成新列表

成员关系判断字符：

in 用法： item in container

not in item not in container&gt;&gt;&gt; l1 = [ 'x','y',3 ]

&gt;&gt;&gt; 'y' in l1

True

&gt;&gt;&gt; 'x' not in l1

False

列表解析：[]

列表复制方式：

浅复制:两者指向同一内存对象&gt;&gt;&gt; l1 = [ 1,2,3,4 ]

&gt;&gt;&gt; l2 = l1

&gt;&gt;&gt; id(l1) == id(l1)

True 可以看出两者内存地址相同

&gt;&gt;&gt; l1.append('x')

&gt;&gt;&gt; print l1

[ 1,2,3,4,'x' ]

&gt;&gt;&gt; print l2

[ 1,2,3,4,'x' ]

深复制：两者指向不同内存对象

1)导入copy模块，使用deepcoop方法&gt;&gt;&gt; import copy

&gt;&gt;&gt; l3 = copy.deepcopy(l1)

&gt;&gt;&gt; id(l3) == id(l1)

False 地址不同

2)复制列表的所有元素，生成一个新列表&gt;&gt;&gt; l4 = l1[:]

&gt;&gt;&gt; print l4

[ 1,2,3,4,'x' ]

&gt;&gt;&gt; l1.append(6)

&gt;&gt;&gt; print l1

[ 1,2,3,4,'x',6 ] l1改变

&gt;&gt;&gt; print l4

[ 1,2,3,4,'x' ] l4不变

3)元组

表达式符号：()

容器类型

任意对象的有序集合，通过索引访问其中的元素，不可变对象，长度固定，异构，嵌套

常见操作：&gt;&gt;&gt; t1 = ( 1,2,3,'xyz','abc')

&gt;&gt;&gt; type(t1)

tuple

&gt;&gt;&gt; len(t1)

5

&gt;&gt;&gt; t2 = () 定义一个空元组

&gt;&gt;&gt; t3 = ( , )

SyntaxError: invalid syntax 报错：使用逗号分隔的条件是最少要有一个元素

(1,)&gt;&gt;&gt; t1[:]

( 1,2,3,'xyz','abc' )

&gt;&gt;&gt; t1[1:]

(2, 3, 'xyz', 'abc')

(1,2)&gt;&gt;&gt; t1[1:4]

(2, 3, 'xyz')

&gt;&gt;&gt; t4 = 'x',1,'yz',45,[2,4,6] 注意!!!这样也可以生成元组

&gt;&gt;&gt; t4

('x', 1, 'yz', 45, [2, 4, 6])

t1 + t4: 合并两个元组，返回一个新的元组；不会修改原元组；&gt;&gt;&gt; t1 + t4

(1, 2, 3, 'xyz', 'abc', 'x', 1, 'yz', 45, [2, 4, 6])

t1 * N: 把l1重复N次，返回一个新元组;&gt;&gt;&gt; t1 * 3

(1, 2, 3, 'xyz', 'abc', 1, 2, 3, 'xyz', 'abc', 1, 2, 3, 'xyz', 'abc')

成员关系判断

in

not in

注意：

虽然元组本身不可变，但如果元组内嵌套了可变类型的元素，那么此类元素的修改不会返回新元组；

例：&gt;&gt;&gt; t4 = ('x', 1, 'yz', 45, [2, 4, 6])

&gt;&gt;&gt; id(t4)

44058448

&gt;&gt;&gt; t4[4]

[2, 4, 6]

&gt;&gt;&gt; t4[4].pop() 弹出列表内一个元素

6

&gt;&gt;&gt; print t4[4]

[2, 4]

&gt;&gt;&gt; print t4

('x', 1, 'yz', 45, [2, 4])

&gt;&gt;&gt; id(t4)  
