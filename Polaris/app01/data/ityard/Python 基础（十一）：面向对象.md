
--- 
title:  Python 基础（十一）：面向对象 
tags: []
categories: [] 

---


#### 目录
- - - <ul><li>- - 


## 1 简介

面向对象（OOP）是一种对现实世界理解和抽象的方法，对象的含义是指在现实生活中能够看得见摸得着的具体事物，一句比较经典的描述是一切皆对象，Python 是一门面向对象的语言，面向对象编程简单来说就是一种封装代码的方式。

**面向对象相关概念**
-  类：描述具有相同属性和方法的集合，简单来说就是一个模板，通它来创建对象。 -  对象：类的实例。 -  方法：类中定义的函数。 -  类变量：定义在类中且在函数之外的变量，在所有实例化对象中公用。 -  局部变量：方法中定义的变量，只作用于当前实例。 
**面向对象三大特性**
-  封装：隐藏对象的属性和实现细节，仅对外提供公共访问方式，提高复用性和安全性。 -  继承：一个类继承一个基类便可拥有基类的属性和方法，可提高代码的复用性。 -  多态：父类定义的引用变量可以指向子类的实例对象，提高了程序的拓展性。 
## 2 基本操作

### 2.1 类

Python 中类的定义使用 `class` 关键字，语法如下所示：

```
class 类名:
	属性
	...
	方法
	...

```

比如我们定义一个类 Cat，如下所示：

```
class Cat:
	# 属性
    color = 'black'
    # 构造方法
    def __init__(self, name):
        self.name = name
    # 自定义方法
    def eat(self, food):
        self.food = food
        print(self.name, '正在吃'+food)

```

构造方法 `__init__()` 会在类实例化时自动调用。无论构造方法还是其他方法都需要将 `self` 作为第一个参数，它代表类的实例。

类创建好后，我们可以直接通过类名访问属性，格式为：`类名.属性名`，比如我们访问 Cat 类的 color 属性，如下所示：

```
print('color--&gt;', Cat.color)

```

上面 Cat 类中定义的属性和方法都是公开的，除此之外我们还可以定义私有属性和方法，声明方式为：在属性名或方法名前加两条下划线，示例如下所示：

```
class Cat:
    __cid = '1'
    def __run(self):
        pass

```

需要强调一点是：外部不能访问私有属性和调用私有方法，自然 `Cat.__cid` 是会报错的。

### 2.2 对象

创建对象也称类的实例化，比如我们通过 Cat 类创建对象，如下所示：

```
 # 创建对象
c = Cat('Tom')

```

创建好对象后，我们就可以使用它访问属性和调用方法了，如下所示：

```
# 访问属性
print('name--&gt;', c.name)
print('color--&gt;', c.color)
# 调用方法
c.eat('鱼')

```

同样对象 `c` 不能访问私有属性 `__cid` 及调用私有方法 `__run`，那我们会有这样一个疑问，这个私有属性和方法难道定义了却不能用吗？ <img src="https://img-blog.csdnimg.cn/20191219225233255.gif" alt=""> 我们来一起看个例子，如下所示：

```
class Cat:
    __cid = '1'
    def __run(self, speed):
        print('__cid是'+self.__cid+'的猫', '以'+speed+'的速度奔跑')
    def run(self, speed):
        self.__run(speed)

c.run('50迈')

```

输出结果：

```
__cid是1的猫 以50迈的速度奔跑

```

通过示例我们可以看出，在内部私有属性和方法是可以被访问和调用的。

### 2.3 继承

Python 支持类的继承，而且支持多继承，语法格式为：

```
class 基类(子类1, 子类2 ...):
	...

```

示例如下所示：

```
# 波斯猫类
class PersianCat(Cat):
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print(self.name, '正在吃'+food)
#加菲猫类
class GarfieldCat(Cat):
    def __init__(self, name):
        self.name = name
    def run(self, speed):
        print(self.name, '正在以'+speed+'的速度奔跑')
# 单继承
class SingleCat(PersianCat):
    pass
# 多继承
class MultiCat(PersianCat, GarfieldCat):
    pass

#调用
sc = SingleCat('波斯猫1号')
sc.eat('鱼')

mc = MultiCat('波斯加菲猫1号')
mc.eat('鱼')
mc.run('50迈')

```

如果继承的父类方法不能满足我们的需求，这时子类可以重写父类方法，如下所示：

```
class SingleCat(PersianCat):
    def eat(self, food ):
        print(self.name, '正在吃'+food, '十分钟后', self.name+'吃饱了')
sc = SingleCat('波斯猫1号')
sc.eat('鱼')

```
