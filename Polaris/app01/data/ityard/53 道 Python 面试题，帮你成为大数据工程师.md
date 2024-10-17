
--- 
title:  53 道 Python 面试题，帮你成为大数据工程师 
tags: []
categories: [] 

---
不久前，我开始担任"数据科学家"的新角色，实际上是" Python工程师"。

如果我提前了解Python的线程生命周期而不是推荐系统，我会做得更好。

本着这种精神，这是我的python面试/工作准备问题和答案。大多数数据科学家编写了大量代码，因此这对科学家和工程师均适用。

无论您是面试应聘者，准备应聘工作还是只是精通Python，我都认为这份清单将是无价之宝。

问题是无序的。让我们开始。

## 1.列表和元组有什么区别？

在我进行过的每次python /数据科学访谈中，都曾问过我这个问题。像手背一样知道答案。

· 列表是可变的。创建后可以对其进行修改。

· 元组是不可变的。一旦创建了元组，就不能对其进行更改

· 列表有顺序。它们是有序序列，通常是相同类型的对象。即：按创建日期排序的所有用户名，[" Seth"，" Ema"，" Eli"]

· 元组具有结构。每个索引可能存在不同的数据类型。即：内存中的数据库记录，（2，" Ema"，" 2020–04–16"）＃id，名称，created_at

## 2.如何进行字符串插值？

在不导入Template类的情况下，有3种插值字符串的方法。

>  
  name = 'Chris' 
  # 1. f strings 
  print(f'Hello {name}') 
  # 2. % operator 
  print('Hey %s %s' % (name, name)) 
  # 3. format 
  print( "My name is {}".format((name))) 
 

## 3." is"和" =="有什么区别？

在我的python生涯的早期，我以为它们是相同的……您好错误。因此，为了记录，检查身份和==检查相等性。

我们将通过一个例子。创建一些列表并将其分配给名称。请注意，b指向与下面的a相同的对象。

```
a = [1,2,3]
b = a
c = [1,2,3]

```

检查是否相等，并注意它们是否相等。

```
print(a == b)
print(a == c)
#=&gt; True
#=&gt; True

```

但是它们具有相同的身份吗？不。

```
print(a is b)
print(a is c)
#=&gt; True
#=&gt; False

```

我们可以通过打印其对象ID进行验证。

```
print(id(a))
print(id(b))
print(id(c))
#=&gt; 4369567560
#=&gt; 4369567560
#=&gt; 4369567624

```

c与a和b具有不同的ID。

## 4.什么是装饰器？

每次面试中我都被问到另一个问题。它本身值得发布，但是如果您可以逐步编写自己的示例，那么您已经准备好了。

装饰器允许通过将现有功能传递给装饰器，从而将功能添加到现有功能，该装饰器将执行现有功能以及其他代码。

我们将编写一个装饰器，该装饰器会在调用另一个函数时记录日志。

编写装饰器函数。这需要一个函数func作为参数。它还定义了一个函数log_function_drawn，该函数调用func（）并执行一些代码print（f'{func}被调用。'）。然后返回定义的函数

```
def logging(func):
	def log_function_called():
  	print(f'{func} called.')
		func()
		return log_function_called

```

让我们编写其他函数，我们最终将装饰器添加到（但尚未）。

```
def my_name():
	print('chris')

def friends_name():
	print('naruto')

my_name()
friends_name()

#=&gt; chris
#=&gt; naruto

```

现在将装饰器添加到两者。

```
@logging
def my_name():
	print('chris')

@logging
def friends_name():
	print('naruto')

my_name()
friends_name()

#=&gt; &lt;function my_name at 0x10fca5a60&gt; called.
#=&gt; chris#=&gt; &lt;function friends_name at 0x10fca5f28&gt; called.
#=&gt; naruto

```

了解现在如何仅通过在其上面添加@logging就能轻松地将日志添加到我们编写的任何函数中。

## 5.解释范围功能

Range生成一个整数列表，有3种使用方式。

该函数接受1到3个参数。请注意，我将每种用法都包装在列表推导中，以便我们看到生成的值。

range（stop）：生成从0到" stop"整数的整数。

[i for i in range(10)]#=&gt; [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

range（start，stop）：生成从" start"到" stop"整数的整数。

[i for i in range(2,10)]#=&gt; [2, 3, 4, 5, 6, 7, 8, 9]

range（start，stop，step）：以" step"为间隔生成从" start"到" stop"的整数。

[i for i in range(2,10,2)]#=&gt; [2, 4, 6, 8]

## 6.定义一个名为car的类，具有2个属性，即"颜色"和"速度"。然后创建一个实例并返回速度。

```
class Car :
	def __init__(self, color, speed):
  	self.color = color self.speed = speed

car = Car('red','100mph')
car.speed
#=&gt; '100mph'

```

## 7. python中的实例，静态和类方法之间有什么区别？

实例方法：接受self参数并与类的特定实例相关。

静态方法：使用@staticmethod装饰器，与特定实例无关，并且是独立的（请勿修改类或实例属性）

类方法：接受cls参数并可以修改类本身

我们将说明一个虚构的CoffeeShop类的区别。

```
class CoffeeShop:
	specialty = 'espresso'
	def __init__(self, coffee_price):
  	self.coffee_price = coffee_price
	
	# instance method
  def make_coffee(self):
  	print(f'Making {self.specialty} for ${self.coffee_price}')
	
	# static method
  @staticmethod def check_weather():
  	print('Its sunny')
	
	# class method
  @classmethod
	def change_specialty(cls, specialty):
  	cls.specialty = specialty
		print(f'Specialty changed to {specialty}')

```

CoffeeShop类具有特殊属性，默认情况下设置为" espresso"。CoffeeShop的每个实例都使用属性coffee_price初始化。它还有3种方法，实例方法，静态方法和类方法。

让我们以coffee_price为5初始化咖啡店的实例。然后调用实例方法make_coffee。

```
coffee_shop = CoffeeShop('5')
coffee_shop.make_coffee()
#=&gt; Making espresso for $5

```

现在调用静态方法。静态方法无法修改类或实例状态，因此通常用于实用程序功能，例如，添加两个数字。我们用我们的天气检查天气。大！

```
coffee_shop.check_weather()
#=&gt; Its sunny

```

现在，我们使用class方法来修改咖啡店的特色菜，然后再修改make_coffee。

```
coffee_shop.change_specialty('drip coffee')
#=&gt; Specialty changed to drip coffee
coffee_shop.make_coffee()
#=&gt; Making drip coffee for $5

```

请注意，make_coffee以前是用来制作意式浓缩咖啡的，但现在却可以制作滴滤咖啡！

## 8." func"和" func（）"有什么区别？

这个问题的目的是看看您是否了解所有函数也是python中的对象。

```
def func():
	print('Im a function')

func
#=&gt; function __main__.func&gt;

func()
#=&gt; Im a function

```

func是表示函数的对象，可以将其分配给变量或传递给另一个函数。带括号的func（）调用该函数并返回其输出。

## 9.说明Map功能的工作方式

map通过将函数应用于序列中的每个元素，返回由返回值组成的列表。

```
def add_three(x):
	return x + 3

li = [1,2,3]

[i for i in map(add_three, li)] #=&gt; [4, 5, 6]

```

上面，我为列表中的每个元素添加了3。

## 10.解释reduce函数的工作原理

将头缠起来直到您几次使用都很难。

reduce接受一个函数和一个序列，然后对该序列进行迭代。在每次迭代中，当前元素和前一个元素的输出都将传递给函数。最后，返回一个值。

```
from functools import reduce
def add_three(x,y):
	return x + y

li = [1,2,3,5]
reduce(add_three, li)
#=&gt; 11

```

返回11，它是1 + 2 + 3 + 5的总和。

## 11.解释filter功能如何工作

过滤器按字面意思执行。它按顺序过滤元素。

每个元素都传递给一个函数，如果函数返回True，则按输出顺序返回；如果函数返回False，则将其丢弃。

```
def add_three(x):
	if x % 2 == 0:
  	return True
	else: return False

li = [1,2,3,4,5,6,7,8]

[i for i in filter(add_three, li)]
#=&gt; [2, 4, 6, 8]

```

请注意如何删除所有不能被2整除的元素。

## 12. python是按引用调用还是按值调用？

如果您对这个问题进行了搜索并阅读了前几页，请准备好深入了解语义。您最好仅了解其工作原理。

不变的对象（如字符串，数字和元组）是按值调用的。请注意，在函数内部进行修改后，name的值不会在函数外部发生变化。name的值已分配给该功能范围内的内存中的新块。

```
name = 'chr'
def add_chars(s):
	s += 'is' print(s)

add_chars(name)
print(name)
#=&gt; chris
#=&gt; chr

```

可变对象（如list）是按引用调用的。注意如何在函数外部定义的列表在函数内部被修改。函数中的参数指向内存中存储li值的原始块。

```
li = [1,2]
def add_element(seq):
	seq.append(3)
	print(seq)

add_element(li)
print(li)
#=&gt; [1, 2, 3]
#=&gt; [1, 2, 3]

```

## 13.如何撤消清单？

请注意如何在列表上调用reverse（）并对其进行突变。它不会返回变异列表本身。

```
li = ['a','b','c']
print(li)
li.reverse()

print(li)
#=&gt; ['a', 'b', 'c']
#=&gt; ['c', 'b', 'a']

```

## 14.字符串乘法如何工作？

让我们看看将字符串" cat"乘以3的结果。

```
'cat' * 3
#=&gt; 'catcatcat'

```

该字符串将自身连接3次。

## 15.列表乘法如何工作？

我们来看看将列表[1,2,3]乘以2的结果。

```
[1,2,3] * 2
#=&gt; [1, 2, 3, 1, 2, 3]

```

输出包含重复两次的[1,2,3]内容的列表。

## 16.在类上"self"指的是什么？

自我是指类本身的实例。这就是我们赋予方法访问权限并能够更新方法所属对象的能力。

下面，将self传递给__init __（）使我们能够在初始化时设置实例的颜色。

```
class Shirt:
	def __init__(self, color):
  	self.color = color

s = Shirt('yellow')
s.color
#=&gt; 'yellow'

```

## 17.如何连接python中的列表？

将2个列表加在一起将它们串联在一起。请注意，数组的功能不同。

```
a = [1,2]
b = [3,4,5]
a + b
#=&gt; [1, 2, 3, 4, 5]

```

## 18.浅拷贝和深拷贝之间有什么区别？

我们将在可变对象（列表）的上下文中进行讨论。对于不可变的物体，浅与深并不重要。

我们将介绍3种情况。

i）引用原始对象。这将新名称li2指向li1指向的内存相同位置。因此，我们对li1所做的任何更改也会在li2中发生。

```
li1 = [['a'],['b'],['c']]
li2 = li1
li1.append(['d'])
print(li2)
#=&gt; [['a'], ['b'], ['c'], ['d']]

```

ii）创建原始文档的浅表副本。我们可以使用list（）构造函数来做到这一点。浅表副本会创建一个新对象，但会使用对原始对象的引用来填充它。因此，将新对象添加到原始集合li3中不会传播到li4，但是修改li3中的一个对象将传播到li4。

```
li3 = [['a'],['b'],['c']]
li4 = list(li3)
li3.append([4])
print(li4)
#=&gt; [['a'], ['b'], ['c']]

li3[0][0] = ['X']
print(li4)
#=&gt; [[['X']], ['b'], ['c']]

```

iii）创建一个深层副本。这是通过copy.deepcopy（）完成的。现在，这两个对象是完全独立的，并且对其中任何一个所做的更改不会对另一个对象产生影响。

```
import copy
li5 = [['a'],['b'],['c']]
li6 = copy.deepcopy(li5)
li5.append([4])
li5[0][0] = ['X']
print(li6)
#=&gt; [['a'], ['b'], ['c']]

```

## 19.列表和数组有什么区别？

注意：Python的标准库有一个数组对象，但在这里我专门指的是常用的Numpy数组。
- 列表存在于python的标准库中。数组由Numpy定义。- 列表可以在每个索引处填充不同类型的数据。数组需要齐次元素。- 列表上的算术从列表中添加或删除元素。每个线性代数的数组函数的算术运算。- 阵列还使用更少的内存，并具有更多的功能。
我写了另一篇有关数组的文章。

## 20.如何连接两个数组？

请记住，数组不是列表。数组来自Numpy和算术函数，例如线性代数。

我们需要使用Numpy的连接函数来实现。

```
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
np.concatenate((a,b))
#=&gt; array([1, 2, 3, 4, 5, 6])

```

## 21.您喜欢Python的什么？

Python非常易读，并且有一种Python方式可以处理几乎所有事情，这意味着一种简洁明了的首选方式。

我将其与Ruby相比，后者通常有很多方法来做某事，而没有指南是首选。

## 22.您最喜欢使用Python的哪个库？

当处理大量数据时，没有什么比熊猫那么有用了，这使得操作和可视化数据变得轻而易举。

## 23.命名可变和不可变的对象

不可变表示创建后无法修改状态。例如：int，float，bool，string和tuple。

可变表示状态可以在创建后进行修改。示例是列表，字典和集合。

## 24.您如何将数字四舍五入到小数点后三位？

使用round（value，decimal_places）函数。

```
a = 5.12345
round(a,3)
#=&gt; 5.123

```

## 25.您如何分割列表？

切片符号采用3个参数list [start：stop：step]，其中step是返回元素的间隔。

```
a = [0,1,2,3,4,5,6,7,8,9]
print(a[:2])
#=&gt; [0, 1]
print(a[8:])
#=&gt; [8, 9]
print(a[2:8])
#=&gt; [2, 3, 4, 5, 6, 7]
print(a[2:8:2])
#=&gt; [2, 4, 6]

```

## 26.什么是pickle？

酸洗是在Python中序列化和反序列化对象的首选方法。

在下面的示例中，我们对字典列表进行序列化和反序列化。

```
import pickleobj = [ {'id':1, 'name':'Stuffy'}, {'id':2, 'name': 'Fluffy'}]

with open('file.p', 'wb') as f:
	pickle.dump(obj, f)

with open('file.p', 'rb') as f:
	loaded_obj = pickle.load(f)

print(loaded_obj)
#=&gt; [{'id': 1, 'name': 'Stuffy'}, {'id': 2, 'name': 'Fluffy'}]

```

## 27.字典和JSON有什么区别？

Dict是python数据类型，是已索引但无序的键和值的集合。

JSON只是遵循指定格式的字符串，用于传输数据。

## 28.您在Python中使用了哪些ORM？

ORM（对象关系映射）将数据模型（通常在应用程序中）映射到数据库表，并简化了数据库事务。

SQLAlchemy通常在Flask的上下文中使用，而Django拥有自己的ORM。

## 29. any（）和all（）如何工作？

Any接受一个序列，如果序列中的任何元素为true，则返回true。

仅当序列中的所有元素均为true时，All才返回true。

```
a = [False, False, False]
b = [True, False, False]
c = [True, True, True]
print( any(a) )
print( any(b) )
print( any(c) )
#=&gt; False
#=&gt; True
#=&gt; True

print( all(a) )
print( all(b) )print( all(c) )#=&gt; False#=&gt; False#=&gt; True

```

## 30.字典或列表的查找速度更快吗？

在列表中查找值需要O（n）时间，因为整个列表需要遍历直到找到值为止。

在字典中查找键需要O（1）时间，因为它是一个哈希表。

如果值很多，这可能会造成巨大的时差，因此通常建议使用字典来提高速度。但是它们确实还有其他限制，例如需要唯一键。

## 31.模块和包装之间有什么区别？

模块是可以一起导入的文件（或文件集合）。

```
import sklearn

```

包是模块的目录。

```
from sklearn import cross_validation

```

因此，包是模块，但并非所有模块都是包。

## 32.如何在Python中递增和递减整数？

可以使用+-和-=进行递增和递减。

```
value = 5
value += 1
print(value)
#=&gt; 6
value -= 1
value -= 1
print(value)
#=&gt; 4

```

## 33.如何返回整数的二进制？

使用bin（）函数。

```
bin(5)
#=&gt; '0b101'

```

## 34.如何从列表中删除重复的元素？

可以通过将列表转换为集合然后返回列表来完成。

```
a = [1,1,1,2,3]
a = list(set(a))
print(a)
#=&gt; [1, 2, 3]

```

## 35.如何检查列表中是否存在值？

用于。

```
'a' in ['a','b','c']
#=&gt; True
'a' in [1,2,3]
#=&gt; False

```

## 36. append和extend有什么区别？

append将值添加到列表，而extend将另一个列表中的值添加到列表。

```
a = [1,2,3]
b = [1,2,3]
a.append(6)
print(a)
#=&gt; [1, 2, 3, 6]
b.extend([4,5])
print(b)
#=&gt; [1, 2, 3, 4, 5]

```

## 37.如何取整数的绝对值？

这可以通过abs（）函数来完成。

```
abs(2)
#=&gt; 2
abs(-2)
#=&gt; 2

```

## 38.如何将两个列表组合成一个元组列表？

您可以使用zip函数将列表组合成一个元组列表。这不仅限于仅使用两个列表。也可以用3个或更多来完成。

```
a = ['a','b','c']
b = [1,2,3]
[(k,v) for k,v in zip(a,b)]
#=&gt; [('a', 1), ('b', 2), ('c', 3)]

```

## 39.如何按字母顺序对字典排序？

您无法对字典进行"排序"，因为字典没有顺序，但是您可以返回已排序的元组列表，其中包含字典中的键和值。

```
d = {'c':3, 'd':4, 'b':2, 'a':1}
sorted(d.items())
#=&gt; [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

```

## 40.一个类如何从Python中的另一个类继承？

在下面的示例中，奥迪继承自Car。继承带来了父类的实例方法。

```
class Car():
	def drive(self):
  	print('vroom')

class Audi(Car):
	pass
  
audi = Audi()
audi.drive()

```

## 41.如何从字符串中删除所有空格？

最简单的方法是在空白处分割字符串，然后重新连接而没有空格。

```
s = 'A string with white space'
''.join(s.split())
#=&gt; 'Astringwithwhitespace'

```

## 42.为什么要在序列上迭代时使用enumerate（）？

enumerate（）允许在序列上进行迭代时跟踪索引。它比定义和递增代表索引的整数更具Python感。

```
li = ['a','b','c','d','e']
for idx,val in enumerate(li):
	print(idx, val)
#=&gt; 0 a
#=&gt; 1 b
#=&gt; 2 c
#=&gt; 3 d
#=&gt; 4 e

```

## 43.pass，continue和break之间有什么区别？

通过意味着什么都不做。我们之所以通常使用它，是因为Python不允许在其中没有代码的情况下创建类，函数或if语句。

在下面的示例中，如果i&gt; 3中没有代码，则会引发错误，因此我们使用pass。

```
a = [1,2,3,4,5]
for i in a:
	if i &gt; 3
  	: pass
  print(i)

#=&gt; 1
#=&gt; 2
#=&gt; 3
#=&gt; 4
#=&gt; 5

```

继续继续到下一个元素，并暂停当前元素的执行。因此对于i &lt;3的值，永远不会达到print（i）。

```
for i in a:
	if i &lt; 3:
  	continue
	print(i)

#=&gt; 3
#=&gt; 4
#=&gt; 5

```

break打破了循环，序列不再重复。因此，不会打印3以后的元素。

```
for i in a:
	if i == 3:
  	break
	print(i)

#=&gt; 1
#=&gt; 2

```

## 44.将以下for循环转换为列表推导。

这个for循环。

```
a = [1,2,3,4,5]
a2 = []
for i in a:
	a2.append(i + 1)
	print(a2)

#=&gt; [2, 3, 4, 5, 6]

```

成为。

```
a3 = [i+1 for i in a]
print(a3)

#=&gt; [2, 3, 4, 5, 6]

```

列表理解通常被认为是更具Python性的，但仍易于阅读。

## 45.举例说明三元运算符。

三元运算符是单行if / else语句。

语法看起来像一个if条件else b。

```
x = 5
y = 10
'greater'  if x &gt; 6 else 'less'
#=&gt; 'less'

'greater' if y &gt; 6 else 'less'
#=&gt; 'greater'

```

## 46.检查字符串是否仅包含数字。

您可以使用isnumeric（）。

```
'123a'.isnumeric()
#=&gt; False

'123'.isnumeric()
#=&gt; True

```

## 47.检查字符串是否仅包含字母。

您可以使用isalpha（）。

```
'123a'.isalpha()
#=&gt; False

'a'.isalpha()
#=&gt; True

```

## 48.检查字符串是否仅包含数字和字母。

您可以使用isalnum（）。

```
'123abc...'.isalnum()
#=&gt; False

'123abc'.isalnum()
#=&gt; True

```

## 49.从字典返回键列表。

这可以通过将字典传递给python的list（）构造函数list（）来完成。

```
d = {'id':7, 'name':'Shiba', 'color':'brown', 'speed':'very slow'}

list(d)
#=&gt; ['id', 'name', 'color', 'speed']

```

## 50.如何对字符串进行大写和小写？

您可以使用upper（）和lower（）字符串方法。

```
small_word = 'potatocake'
big_word = 'FISHCAKE'

small_word.upper()
#=&gt; 'POTATOCAKE'
big_word.lower()
#=&gt; 'fishcake'

```

## 51. remove，del和pop有什么区别？

remove（）删除第一个匹配值。

```
li = ['a','b','c','d']
li.remove('b')

li
#=&gt; ['a', 'c', 'd']

```

del按索引删除元素。

```
li = ['a','b','c','d']
del li[0]

li
#=&gt; ['b', 'c', 'd']

```

pop（）按索引删除一个元素并返回该元素。

```
li = ['a','b','c','d']
li.pop(2)
#=&gt; 'c'

li
#=&gt; ['a', 'b', 'd']

```

## 52.举一个字典理解的例子。

在下面，我们将创建字典，以字母作为键，并以字母索引作为值。

```
# creating a list of letters
import string
list(string.ascii_lowercase)
alphabet = list(string.ascii_lowercase)
# list comprehensiond = {val:idx for idx,val in enumerate(alphabet)}

d
#=&gt; {'a': 0,
#=&gt; 'b': 1,
#=&gt; 'c': 2,
#=&gt; ...
#=&gt; 'x': 23,
#=&gt; 'y': 24,
#=&gt; 'z': 25}

```

## 53.如何在Python中执行异常处理？

Python提供了3个单词来处理异常，请尝试使用" except"和" finally"。

语法如下所示。

```
try:
# try to do this
except:
# if try block fails then do this
finally:
# always do this

```

在下面的简单示例中，try块失败，因为我们无法在字符串中添加整数。else块设置val = 10，然后finally块打印完成。

```
try:
	val = 1 + 'A'
except:
	val = 10
finally:
	print('complete')

print(val)

#=&gt; complete
#=&gt; 10

```

## 结论

您永远不会知道面试中会遇到什么问题，最好的准备方法是拥有大量编写代码的经验。

就是说，此列表应涵盖您需要以python方式查询数据科学家或初级/中级python开发人员角色的所有内容。

我希望这对您有帮助。

本文翻译自Chris的文章《53 Python Interview Questions and Answers》，

参考：https://towardsdatascience.com/53-python-interview-questions-and-answers-91fa311eec3f<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 
