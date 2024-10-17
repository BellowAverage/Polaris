
--- 
title:  从 Zero 到 Hero，一文掌握 Python 关键代码 
tags: []
categories: [] 

---
>  
  原文：Learning Python: From Zero to Hero    
  https://medium.freecodecamp.org/learning-python-from-zero-to-hero-120ea540b567 
 

首先，什么是 Python？根据 Python 创建者 Guido van Rossum 所言，Python 是一种高级编程语言，其设计的核心理念是代码的易读性，以及允许编程者通过若干行代码轻松表达想法创意。实际上，我选择学习 Python 的首要原因是其编程的优美性，用它编码和表达想法非常自然。

Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。

另一个原因是 Python 的编写使用方式有多种，数据科学、网页开发、机器学习皆可使用 Python。Quora、Pinterest 和 Spotify 都使用 Python 作为其后端开发语言。

**<strong>基础篇**</strong>

**变量**

简单来讲，我们可以把变量看作是存储一个值的词。

在 Python 中定义一个变量并为其赋值非常简单。想象一下你在变量「one」中存储 1，即是：

```
one = 1
```

这是多么简单，我们只要把 1 赋值给变量「one」。

```
two = 2
some_number = 10000
```

并且你可以把任意值赋给任意变量。如上所见，把整数 2 赋值给变量「two」，把 10,000 赋值给变量「some_number」。除了整数，我们也可以赋值布尔运算、字符串、浮点数以及其他数据形式。

```
# booleans
true_boolean = True
false_boolean = False

# string
my_name = "Leandro Tk"

# float
book_price = 15.80
```

**控制流：条件语句**

「if」语句通过表达式评估一个语句是真或假。如果是真，则向下执行「if」条件中的子语句。比如：

```
if True:
  print("Hello Python if")

if 2 &gt; 1:
  print("2 is greater than 1")
```

2 比 1 大，因此「print」代码被执行。如果「if」表达式是假的，则「else」下的子语句将被执行。

```
if 1 &gt; 2:
  print("1 is greater than 2")
else:
  print("1 is not greater than 2")

```

你也可以使用一个「elif」语句以添加一个执行条件。

```
if 1 &gt; 2:
  print("1 is greater than 2")
elif 2 &gt; 1:
  print("1 is not greater than 2")
else:
  print("1 is equal to 2")
```

**循环／迭代器**

在 Python 中，我们可有不同形式的迭代。我将讨论两个：while 与 for。

while 循环：当该语句为真，以下代码将被执行，并打印从 1 到 10 的数字。

```
num = 1

while num &lt;= 10:
    print(num)
    num += 1
```

while 循环需要一个「循环条件」。如果它为真，则继续迭代。在以上实例中，当 num 为 11，则循环条件为假，我们结束循环。

以下代码有助于更好地理解它：

```
loop_condition = True

while loop_condition:
    print("Loop Condition keeps: %s" %(loop_condition))
    loop_condition = False
```

循环条件为真，则继续迭代，直到它为假。对于 For 循环：你可以把变量「num」应用需要循环的代码块中，而「for」语句会为你迭代它。该代码的打印与 while 代码相同：从 1 到 10。

```
for i in range(1, 11):
  print(i)
```

看，如此简单。范围从 1 直到第 11 个元素（10 是第 10 个元素）。此外，如果我们直接确定一个数，那么 for 循环将从零开始一直迭代到该数字（不包括）。例如以下 for 循环将输出 0 到 9：

```
for i in range(10):
  print(i)
```

**列表：数组数据结构**

列表是一个数组或集合，它可用于存储一系列值（比如那些你想要的整数）。因此让我们用一下它：

```
my_integers = [1, 2, 3, 4, 5]
```

如上我们创建了一个数组并赋值到 my_integers 变量中。而我们可以通过索引取该数组中的值，如下所示，数组第一个元素的索引为 0，第二个元素的索引为 1，依次类推。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9LbVhQS0ExOWdXODF4TzhsR0VGUzRSRm85aWFyV3VmTzdlaWFQd1VNNzV5OXgzUG1xdHdyUGljVmxBY1BsV01nNHlzMnpOc2FZTFZHeks3RTdxdnc5V2RpY1EvNjQw?x-oss-process=image/format,png">

使用以下语句可能更好理解：

```
my_integers = [5, 7, 1, 3, 4]

print(my_integers[0]) # 5
print(my_integers[1]) # 7
print(my_integers[4]) # 4
```

同样我们列表元素的类型也可以是字符型，如下我们创建了一个元素为字符的列表：

```
relatives_names = [
  "Toshiaki",
  "Juliana",
  "Yuji",
  "Bruno",
  "Kaio"
]

print(relatives_names[4]) # Kaio
```

以上我们了解了列表的定义和索引使用方法，以下我们将了解如何添加一个元素到列表数据结构中。添加元素到列表最常见的方法是 append：

```
bookshelf = []
bookshelf.append("The Effective Engineer")
bookshelf.append("The 4 Hour Work Week")
print(bookshelf[0]) # The Effective Engineer
print(bookshelf[1]) # The 4 Hour Work Week
```

append 方法非常简单，我们只需要对需要添加的元素应用该方法就能将其添加到列表的末尾。

**字典：键-值数据结构**

我们已经知道列表是通过整数索引来获取某个元素，而若我们不希望使用整数作为索引，那么就可以使用字典数据结构。通过这种数据结构，我们可以使用数值型、字符型或其它类型的索引。字典的每个键值 (key=&gt;value) 对用冒号 (:) 分割，每个对之间用逗号 (,) 分割，整个字典包括在花括号 ({})中。如下，字典（Dictionary）是键（Key）与值（Value）的集合：

```
dictionary_example = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}
```

其中键是指向对应值的索引，我们需要使用键而访问对应的元素值：

```
dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

print("My name is %s" %(dictionary_tk["name"])) # My name is Leandro
print("But you can call me %s" %(dictionary_tk["nickname"])) # But you can call me Tk
print("And by the way I'm %s" %(dictionary_tk["nationality"])) # And by the way I'm Brazilian
```

以上创建了一个字典，其中定义了四个键与对应的值，print 函数内使用了字典的键以获取对应的值。此外，字典的值可以使用任何类型的数据，如下我们添加了一个键为字符型，值为数值型的键-值对。

```
dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian",
  "age": 24
}

print("My name is %s" %(dictionary_tk["name"])) # My name is Leandro
print("But you can call me %s" %(dictionary_tk["nickname"])) # But you can call me Tk
print("And by the way I'm %i and %s" %(dictionary_tk["age"], dictionary_tk["nationality"])) # And by the way I'm 24 and Brazilian
```

下面我们需要了解如何添加元素到字典中，其实字典的本质就是指向特定值的关键字的集合。因此我们可以直接将某个值赋予到字典某个关键字（可以不存在）中而修改或添加键值对。

```
dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

dictionary_tk['age'] = 24
print(dictionary_tk) # {'nationality': 'Brazilian', 'age': 24, 'nickname': 'Tk', 'name': 'Leandro'}
```

**迭代：数据结构中的循环**

列表循环同样十分简单，我们可以循环地修改或输出某个列表。如下，我们常用 for 循环依次提取列表中的元素：

```
bookshelf = [
  "The Effective Engineer",
  "The 4 hours work week",
  "Zero to One",
  "Lean Startup",
  "Hooked"
]

for book in bookshelf:
    print(book)
```

对于哈希数据结构，我们同样可以使用字典中的键和 for 循环依次读取键与对应的值：

```
dictionary = { "some_key": "some_value" }

for key in dictionary:
    print("%s --&gt; %s" %(key, dictionary[key]))
# some_key --&gt; some_value
```

使用 iteritems 方法同样可以实现相同的效果：

```
dictionary = { "some_key": "some_value" }

for key, value in dictionary.items():
    print("%s --&gt; %s" %(key, value))
# some_key --&gt; some_value
```

我们命名了两个参数 key 和 value，但我们同样可以命名为其它的，如下我们使用 attribute 和 value 作为字典键值的参数，它同样有效：

```
dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian",
  "age": 24
}

for attribute, value in dictionary_tk.items():
    print("My %s is %s" %(attribute, value))

# My name is Leandro
# My nickname is Tk
# My nationality is Brazilian
# My age is 24
```

**类与对象**

对象（Object）表征的是真实世界中的目标，如狗、猫和自行车等，一般对象有两个特征，即数据（Data）与行为（Behavior）。对象「车辆」有一些数据，如车轮的数量、车门的数量与作为容量等，它同样还有一些行为，例如车辆可以加速、刹车、展示燃油使用量等。

在面向对象的编程中，我们将数据表示为属性，将行为表示为方法。

类（Class）是创建独立对象的蓝图。在现实世界中，我们经常发现很多相同类型的对象。例如车辆，同型号的车辆都有引擎、车轮、座位等组件，而每一辆车都是根据相同的设计图构建且有相同的组件。

因此，对象是对客观事物的抽象，类是对对象的抽象。对象是类的实例，类是对象的模板。

Python 是一种面向对象的程序语言，因此它也有类（Class）与对象（Object）这两个概念。在了解 Python 面向对象编程的案例前，我们需要先熟悉面向对象编程的一些基本概念：
- 类 (Class)：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。- 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。- 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。- 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。- 实例变量：定义在方法中的变量，只作用于当前实例的类。- 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，一个「狗」类的对象派生自「动物」类，这是模拟"是一个（is-a）"关系（狗是一种动物）。- 实例化：创建一个类的实例，类的具体对象。- 方法：类中定义的函数。- 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
下面首先查看通过声明定义类的语句：

```
class Vehicle:
    pass
```

目标是类的实例，我们可以使用类的名称创建一个实例：

```
car = Vehicle()
print(car) # &lt;__main__.Vehicle instance at 0x7fb1de6c2638&gt;
```

如上，car 为 Vehicle 类的一个对象或实例。

若我们的 vehicle 类有四个属性，即车轮数、储能类型、座位容量和最大时速，那么我们在创建 vehicle 类时可以设置这些属性。下面，我们定义了初始化类时所接受的数据。self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。

```
class Vehicle:

    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
```

__init__() 方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建 vehicle 类的实例时就会调用该方法来定义这些属性。若我们希望能创建 Tesla Model S 这一个对象，根据其有四个车轮、电力驱动、四座容量和最大时速为 250km/hour 的特征，我们能创建对象：

```
tesla_model_s = Vehicle(4, 'electric', 5, 250)
```

现在所有的属性已经设定了，那么我们该如何访问这些属性值？我们将发送信息到对象的过程称为方法，即对象的行为：

```
class Vehicle:

    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def number_of_wheels(self):
        return self.number_of_wheels

    def set_number_of_wheels(self, number):
        self.number_of_wheels = number
```

以上语句实现了两个方法，number_of_wheels 和 set_number_of_wheels。我们可以称为 getter &amp; setter，因为第一个方法获取了属性值，而第二个方法将为该属性设置一个新的值。在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数。

在 Python 中，我们能使用 @property (decorators) 定义 getter &amp; setter：

```
class Vehicle:

    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    @property
    def number_of_wheels(self):
        return self.number_of_wheels

    @number_of_wheels.setter
    def number_of_wheels(self, number):
        self.number_of_wheels = number
```

同样我们能使用这些方法作为属性：

```
tesla_model_s = Vehicle(4, 'electric', 5, 250)
print(tesla_model_s.number_of_wheels) # 4
tesla_model_s.number_of_wheels = 2 # setting number of wheels to 2
print(tesla_model_s.number_of_wheels) # 2
```

这和定义方法有一些不同，这些方法作为了一种属性。如上当我们设定新的车轮数量，我们不需要将「2」作为参数设定，而是将 number_of_wheels 数值设定为 2。

我们还能使用方法做一些其他的操作，例如方法「make_noise」可以设置为：

```
class Vehicle:

    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def make_noise(self):
        print('VRUUUUUUUM')
```

当我们调用该方法时，它将返回字符串「VRRRRUUUUM」。

```
tesla_model_s = Vehicle(4, 'electric', 5, 250)
tesla_model_s.make_noise() # VRUUUUUUUM
```

**封装：隐藏信息**

封装是一种限制直接访问目标属性和方法的机制，但同时它又有利于对数据（对象的方法）进行操作。

>  
  封装是一种将抽象性函数接口的实现细节部分包装、隐藏起来的方法。同时，它也是一种防止外界调用端，去访问对象内部实现细节的手段，这个手段是由编程语言本身来提供的。 
 

对象所有的内部表征对于外部来说都是隐藏的，只有对象能直接与内部数据交互。首先，我们需要理解公开（public）和私有（non-public）实例变量和方法。

**公开实例变量**

对于 Python 的类，我们可以使用 constructor 方法初始化公开实例变量：

```
class Person:

    def __init__(self, first_name):
        self.first_name = first_name
```

下面我们应用 first_name 的值作为公开实例变量的变元。

```
tk = Person('TK')
print(tk.first_name) # =&gt; TK
```

在类内：

```
class Person:
    first_name = 'TK'
```

现在我们不需要再对 first_name 赋值，所有赋值到 tk 的目标都将有类的属性：

```
tk = Person()
print(tk.first_name) # =&gt; TK
```

现在我们已经学会如何使用公开实例变量和类属性。除此之外，我们还能管理公开部分的变量值，即对象可以管理其变量的值：Get 和 Set 变量值。保留 Person 类，我们希望能给 first_name 变量赋另外一个值：

```
tk = Person('TK')
tk.first_name = 'Kaio'
print(tk.first_name) # =&gt; Kaio
```

如上我们将另外一个值（kaio）赋予了 first_name 实例变量，因为它又是一个公开变量，所以会更新变量值。

**私有实例变量**

和公开实例变量一样，我们可以使用 constructor 方法或在类的内部声明而定义一个私有实例变量。语法上的不同在于私有实例变量在变量名前面加一个下划线：

```
class Person:

    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email
```

上述定义的 email 变量就是私有变量。

```
tk = Person('TK', 'tk@mail.com')
print(tk._email) # tk@mail.com
```

我们可以访问并且更新它，私有变量仅是一个约定，即他们需要被视为 API 非公开的部分。所以我们可以使用方法在类的定义中完成操作，例如使用两种方法展示私有实例的值与更新实例的值：

```
class Person:

    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email

    def update_email(self, new_email):
        self._email = new_email

    def email(self):
        return self._email
```

现在我们可以使用方法更新或访问私有变量。

```
tk = Person('TK', 'tk@mail.com')
print(tk.email()) # =&gt; tk@mail.com

tk._email = 'new_tk@mail.com'
print(tk.email()) # =&gt; tk@mail.com

tk.update_email('new_tk@mail.com')
print(tk.email()) # =&gt; new_tk@mail.com
```

我们先初始化 Person 类并赋值，然后通过定义的方法访问并打印私有变量的值。如我们直接赋值给私有变量新的值，那么打印出来还是原有的值，我们只能通过在类里面定义的方法进行操作而更新私有变量。

公开方法

对于公开方法（public methods），我们同样能在类以外的地方调用，以下定义了一个类与方法：

```
class Person:

    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def show_age(self):
        return self._age
```

让我们测试一下该方法：

```
tk = Person('TK', 25)
print(tk.show_age()) # =&gt; 25
```

**私有方法**

但是对于私有方法来说，并不能这样操作。若我们定义相同的类，且使用下划线定义 show_age 为私有方法：

```
class Person:

    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def _show_age(self):
        return self._age
```

我们同样能调用对象的私有方法：

```
tk = Person('TK', 25)
print(tk._show_age()) # =&gt; 25
```

我们也能访问并更新它，私有方法应该要看作 API 的私有部分。下面的案例可以展示了如何使用它：

```
class Person:

    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def show_age(self):
        return self._get_age()

    def _get_age(self):
        return self._age

tk = Person('TK', 25)
print(tk.show_age()) # =&gt; 25
```

如上我们声明了私有方法_get_age 和公开方法 show_age。show_age 方法可以在类的外部调用，而_get_age 只能在类内部使用。

**封装小结**

通过程序封装，我们确保了对象的内部表征对外是隐藏的。而面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。继承完全可以理解成类之间的类型和子类型关系。

若我们有一辆车，且知道车轮数、座位容量和最大时速，那么一辆电动车类就继承常规汽车类中的相同属性。

```
class Car:

    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
```

更新类中的一个对象：

```
my_car = Car(4, 5, 250)

print(my_car.number_of_wheels)
print(my_car.seating_capacity)
print(my_car.maximum_velocity)
```

初始化对象后，Python 可以将父类（parent class）作为参数应用到子类（child class）中。因此电动车类可以从汽车类继承对象。

```
class ElectricCar(Car):

    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Car.__init__(self, number_of_wheels, seating_capacity, maximum_velocity
```

我们不需要实现其他方法，因为电动汽车类已经从汽车类继承了对象：

```
my_electric_car = ElectricCar(4, 5, 250)

print(my_electric_car.number_of_wheels) # =&gt; 4
print(my_electric_car.seating_capacity) # =&gt; 5
print(my_electric_car.maximum_velocity) # =&gt; 250
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcmNjSFVSRTF0ZmRnOWo5em9zbzYwNGdvWmtBeGpkdGNQSHo4WmFtaWJjakZiTUhMZGxNOG1RbWhveHZxbUpIUzRpY09hN2dSVGp2M1dBLzY0MA?x-oss-process=image/format,png">
