
--- 
title:  20个非常有用的Python单行代码 
tags: []
categories: [] 

---
有用的 Python 单行代码片段，只需一行代码即可解决特定编码问题！

在本文中，将分享20 个 Python 一行代码，你可以在 30 秒或更短的时间内轻松学习它们。这种单行代码将节省你的时间，并使你的代码看起来更干净且易于阅读。

**1 一行 For 循环**

for 循环是一个多行语句，但是在 Python 中，我们可以使用列表推导式方法在一行中编写 for 循环。以过滤小于250的值为例，查看下面的代码示例。

```
#For循环在一行
mylist = [200, 300, 400, 500]
#正常方式
result = [] 
for x in mylist: 
    if x &gt; 250: 
        result.append(x) 
print(result) # [300, 400, 500]
#一行代码方式
result = [x for x in mylist if x &gt; 250] 
print(result) # [300, 400, 500]

```

**2 一行 While 循环**

这个 One-Liner 片段将向你展示如何在一行中使用 While 循环代码，我已经展示了两种方法。

```
#方法 1 Single Statement 
while True: print(1) #infinite 1
#方法 2 多语句
x = 0 
while x &lt; 5: print(x); x= x + 1 # 0 1 2 3 4 5

```

**3 一行 IF Else 语句**

好吧，要在一行中编写 IF Else 语句，我们将使用三元运算符。三元的语法是“[on true] if [expression] else [on false]”。

我在下面的示例代码中展示了 3 个示例，以使你清楚地了解如何将三元运算符用于一行 if-else 语句。要使用 Elif 语句，我们必须使用多个三元运算符。

```
#if Else 在一行中
#Example 1 if else
print("Yes") if 8 &gt; 9 else print("No") # No
#Example 2 if elif else 
E = 2 
print("High") if E == 5 else print("数据STUDIO") if E == 2 else 
print("Low") # 数据STUDIO 
 
#Example 3 only if
if 3 &gt; 2: print("Exactly") # Exactly

```

**4 一行合并字典**

这个 单行代码段将向你展示如何使用一行代码将两个字典合并为一个。下面我展示了两种合并字典的方法。

```
# 在一行中合并字典
d1 = {<!-- --> 'A': 1, 'B': 2 } 
d2 = {<!-- --> 'C': 3, 'D': 4 }
#方法 1 
d1.update(d2) 
print(d1) # {<!-- -->'A': 1, 'B': 2, 'C': 3, 'D': 4}
#方法 2 
d3 = {<!-- -->**d1, **d2} 
print(d3) # {<!-- -->'A': 1, 'B': 2, 'C': 3, 'D': 4}

```

**5 一行函数**

我们有两种方法可以在一行中编写函数，在第一种方法中，我们将使用与三元运算符或单行循环方法相同的函数定义。

第二种方法是用 lambda 定义函数。查看下面的示例代码以获得更清晰的理解。

```
#函数在一行中
#方法一
def fun(x): return True if x % 2 == 0 else False 
print(fun(2)) # False
#方法2
fun = lambda x : x % 2 == 0 
print(fun(2)) # True 
print(fun(3)) # False

```

**6 一行递归**

这个单行代码片段将展示如何在一行中使用递归。我们将使用一行函数定义和一行 if-else 语句。下面是查找斐波那契数的示例。

```
# 单行递归
#Fibonaci 单行递归示例
def Fib(x): return 1 if x in {<!-- -->0, 1} else Fib(x-1) + Fib(x-2)
print(Fib(5)) # 8
print(Fib(15)) # 987

```

**7 一行数组过滤**

Python 列表可以通过使用列表推导方法在一行代码中进行过滤。以过滤偶数列表为例。

```
# 一行中的数组过滤
mylist = [2, 3, 5, 8, 9, 12, 13, 15]
#正常方式
result = [] 
for x in mylist: 
    if x % 2 == 0: 
        result.append(x)
print(result) # [2, 8, 12]
# 单线方式
result = [x for x in mylist if x % 2 == 0] 
print(result) # [2, 8, 12]

```

**8 一行异常处理**

我们使用异常处理来处理 Python 中的运行时错误。你知道我们可以在一行中编写这个 Try except 语句吗？通过使用 exec() 语句，我们可以做到这一点。

```
# 一行异常处理
#原始方式
try:
    print(x)
except:
    print("Error")
#单行方式
exec('try:print(x) \nexcept:print("Error")') # 错误

```

**9 一行列表转字典**

我们可以使用 Python enumerate() 函数将 List 转换为一行字典。在enumerate() 中传递列表并使用dict() 将最终输出转换为字典格式。

```
# 字典在一行
mydict = ["John", "Peter", "Mathew", "Tom"]
mydict = dict(enumerate(mydict))
print(mydict) # {<!-- -->0: 'John', 1: 'Peter', 2: 'Mathew', 3: 'Tom'}

```

**10 一行多变量**

Python 允许在一行中进行多个变量赋值。下面的示例代码将向你展示如何做到这一点。

```
#多行变量
#正常方式
x = 5 
y = 7 
z = 10 
print(x , y, z) # 5 7 10
#单行方式
a, b, c = 5, 7, 10 
print(a, b, c) # 5 7 10

```

**11 一行交换值**

交换是编程中一项有趣的任务，并且总是需要第三个变量名称 temp 来保存交换值。这个单行代码段将向你展示如何在没有任何临时变量的情况下交换一行中的值。

```
#换成一行
#正常方式
v1 = 100
v2 = 200
temp = v1
v1 = v2 
v2 = temp
print(v1, v2) # 200 100
# 单行交换
v1, v2 = v2, v1 
print(v1, v2) # 200 100

```

**12 一行排序**

排序是编程中的一个普遍问题，Python 有许多内置的方法来解决这个排序问题。下面的代码示例将展示如何在一行中进行排序。

```
# 在一行中排序
mylist = [32, 22, 11, 4, 6, 8, 12] 
# 方法 1
mylist.sort() 
print(mylist) # # [4, 6, 8, 11, 12, 22, 32]
print(sorted(mylist)) # [4, 6, 8, 11, 12, 22, 32]

```

**13 一行读取文件**

不使用语句或正常读取方法，也可以正确读取一行文件。

```
#一行读取文件
#正常方式
with open("data.txt", "r") as file: 
    data = file.readline() 
    print(data) # Hello world
#单行方式
data = [line.strip() for line in open("data.txt","r")] 
print(data) # ['hello world', 'Hello Python']

```

**14 一行类**

上课总是多线工作。但是在 Python 中，有一些方法可以在一行代码中使用类特性。

```
# 一行中的类
#普通方式
class Emp: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age
        emp1 = Emp("云朵君", 22) 
print(emp1.name, emp1.age) # 云朵君 22
#单行方式
#方法 1 带有动态 Artibutes 的 Lambda

Emp = lambda:None; Emp.name = "云朵君"; Emp.age = 22
print(Emp.name, Emp.age) # 云朵君 22

#方法 2 
from collections import namedtuple
Emp = namedtuple('Emp', ["name", "age"]) ("云朵君", 22) 
print(Emp.name, Emp.age) # 云朵君 22

```

**15 一行分号**

一行代码片段中的分号将向你展示如何使用分号在一行中编写多行代码。

```
# 一行分号
# 例 1 
a = "Python"; b = "编程"; c = "语言"; print(a, b, c)
# 输出
# Python 编程语言

```

**16 一行打印**

这不是很重要的片段，但有时当你不需要使用循环来执行任务时它很有用。

```
# 一行打印
#正常方式
for x in range(1, 5):
    print(x) # 1 2 3 4
#单行方式
print(*range(1, 5)) # 1 2 3 4
print(*range(1, 6)) # 1 2 3 4 5

```

**17 一行map函数**

Map 函数是适用的高阶函数。这将函数应用于每个元素。下面是我们如何在一行代码中使用 map 函数的示例。

```
#在一行中map
print(list(map(lambda a: a + 2, [5, 6, 7, 8, 9, 10])))
# 输出
# [7, 8, 9, 10, 11, 12]

```

**18 删除列表第一行中的 Mul 元素**

你现在可以使用 del 方法在一行代码中删除 List 中的多个元素，而无需进行任何修改。

```
# 删除一行中的Mul元素
mylist = [100, 200, 300, 400, 500]
del mylist[1::2]
print(mylist) # [100, 300, 500]

```

**19 一行打印图案**

现在你不再需要使用for循环来打印相同的图案。你可以使用 print 语句和星号 (*) 在一行代码中执行相同的操作。

```
# 在一行中打印图案# 
# 正常方式
for x in range(3):
    print('😀')
# 输出
# 😀 😀 😀
#单行方式
print('😀' * 3) # 😀 😀 😀 
print('😀' * 2) # 😀 😀 
print('😀' * 1) # 😀

```

**20 一行查找质数**

此代码段将向你展示如何编写单行代码来查找范围内的素数。

```
# 查找质数
print(list(filter(lambda a: all(a % b != 0 for b in range(2, a)),
                  range(2,20))))
# 输出
# [2, 3, 5, 7, 11, 13, 17, 19]

```

### 关于Python技术储备

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

#### 一、Python所有方向的学习路线

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<img src="https://img-blog.csdnimg.cn/8a20de9e31f144dfba0e4996caded17d.png" alt="在这里插入图片描述">

#### 二、Python必备开发工具

<img src="https://img-blog.csdnimg.cn/e0452e0b045c4a17b6af25b9b41d1063.png" alt="在这里插入图片描述">

#### 三、精品Python学习书籍

当我学到一定基础，有自己的理解能力的时候，会去阅读一些前辈整理的书籍或者手写的笔记资料，这些笔记详细记载了他们对一些技术点的理解，这些理解是比较独到，可以学到不一样的思路。 <img src="https://img-blog.csdnimg.cn/904cb6a6cf3944f399edd97fed156269.png" alt="在这里插入图片描述">

#### 四、Python视频合集

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/17662d7608844f9388bf2e61d8699866.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/7ac60955ca564260bf08ccee6b89c10b.png" alt="在这里插入图片描述">

#### 五、实战案例

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。 <img src="https://img-blog.csdnimg.cn/89a5fe04ea344a3baa7954caf914217a.png" alt="在这里插入图片描述">

#### 六、Python练习题

检查学习结果。 <img src="https://img-blog.csdnimg.cn/260c5d1f9a4846f59f38b5320917623c.png" alt="在这里插入图片描述">

#### 七、面试资料

我们学习Python必然是为了找到高薪的工作，下面这些面试题是来自阿里、腾讯、字节等一线互联网大厂最新的面试资料，并且有阿里大佬给出了权威的解答，刷完这一套面试资料相信大家都能找到满意的工作。 <img src="https://img-blog.csdnimg.cn/97c454a3e5b4439b8600b50011cc8fe4.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/111f5462e7df433b981dc2430bb9ad39.png" alt="在这里插入图片描述">

###### 这份完整版的Python全套学习资料已经上传CSDN，朋友们如果需要可以微信扫描下方CSDN官方认证二维码免费领取【`保证100%免费`】

<img src="https://img-blog.csdnimg.cn/1d2a69f2d57e4d1cb444037b17af8607.png" alt="">

>  
 **Python资料、技术、课程、解答、咨询也可以直接点击下面名片，`添加官方客服斯琪`**`↓` 

