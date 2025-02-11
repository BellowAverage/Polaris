
--- 
title:  整理了100个必备的Python函数，建议收藏 
tags: []
categories: [] 

---
来源：https://sslljy.blog.csdn.net/?type=blog

### 前言 

新手在做写代码的时候容易卡壳，尤其当接触的函数以及其他知识比较多的时候，经常会看完需求之后不知道自己该用什么方法来实现它，实现的逻辑可能你有，但怎么该用什么函数给忘了，这其实就是知识的储备不够，你记不住哪个函数有什么作用，自然一头雾水。

这几天我专门整理了Python常用的一些函数，从最基础的输入输出函数到正则等12个板块的，总共100多个常用函数，方便小伙伴们进行快速地记忆，每天快速过一遍，用的时候再加深一下，慢慢地你就会摆脱写代码卡壳的状况。

虽说自学编程的时候我们强调更多的东西是理解和实际去敲代码，但有些东西你是要必须牢记的，否则你写代码将寸步难行。老手当然已经烂记于心，新手想要快速得心应手开发，记住高频使用的函数就是一个好法子。

### 1. 基础函数 

**案例：**将浮点型数值转换为字符串，输出转换后的数据类型

```
f = 30.5
ff = str(f)
print(type(ff))

#输出结果为 class 'str'
```

### 2. 流程控制 

**案例：**根据用户输入的分数判断成绩，低于50分时提示“你的分数低于50分”，5059分时提示“你的分数在60分左右”，大于等于60分为及格，8090分为优秀，大于90分为非常优秀。

```
s = int(input("请输入分数:"))
if 80 &gt;= s &gt;= 60:
    print("及格")
elif 80 &lt; s &lt;= 90:
    print("优秀")
elif 90 &lt; s &lt;= 100:
    print("非常优秀")
else:
    print("不及格")
    if s &gt; 50:
        print("你的分数在60分左右")
    else:
        print("你的分数低于50分")
```

### 3. 列表 

**案例：**判断6这个数在列表[1,2,2,3,6,4,5,6,8,9,78,564,456]中的位置，并输出其下标。

```
l = [1,2,2,3,6,4,5,6,8,9,78,564,456]
n = l.index(6, 0, 9)
print(n)

#输出结果为  4
```

### 4. 元组 

**案例：**修改元组

```
#取元组下标在1~4之间的3个数，转换成列表
t = (1,2,3,4,5)
print(t[1:4])
l = list(t)
print(l)
#在列表下标为2的位置插入1个6
l[2]=6
print(l)
#讲修改后的列表转换成元组并输出
t=tuple(l)
print(t)
```

```
#运行结果为：

(2, 3, 4)
[1, 2, 3, 4, 5]
[1, 2, 6, 4, 5]
(1, 2, 6, 4, 5)
```

### 5. 字符串 

**案例：**用format（）的三种方式输出字符串

方式1：用数字占位（下标）

```
"{0} 嘿嘿".format("Python")
a=100
s = "{0}{1}{2} 嘿嘿"
s2 = s.format(a,"JAVA","C++")
print(s2)

#运行结果为：100JAVAC++ 嘿嘿
```

方式2：用{} 占位

```
a=100
s = "{}{}{} 嘿嘿"
s2 = s.format(a,"JAVA","C++","C# ")
print(s2)

#运行结果为：100JAVAC++ 嘿嘿
```

方式3：用字母占位

```
s = "{a}{b}{c} 嘿嘿"
s2 = s.format(b="JAVA",a="C++",c="C# ")
print(s2)

#运行结果为：C++JAVAC#  嘿嘿
```

### 6. 字典 

**案例：**在字典中查找数据

```
d = {"name": "小黑"}
print(d.get("name2", "没有查到"))
print(d.get("name"))
```

```
#运行结果为：
没有查到
小黑
```

### 7. 函数 

函数这块重头戏更多的是自定义函数，常用的内置函数不是很多，主要有以下几个：

**案例：**在函数中定义一个局部变量，跳出函数仍能调用该变量

```
def fun1():
    global b
    b=100
    print(b)
fun1()
print(b)
```

```
#运行结果为：
100
100
```

### 8. 进程和线程 

**案例：**继承Thread类实现

```
#多线程的创建
class MyThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        #线程要做的事情
        for i in range(5):
            print(self.name)
            time.sleep(0.2)
 #实例化子线程
t1 = MyThread("凉凉")
t2 = MyThread("最亲的人")

t1.start()
t2.start()
```

### 9. 模块与包 

**案例：**包的使用方式4

```
from my_package1 import my_module3
print(my_module3.a)
my_module3.fun4()
```

### 10. 文件操作 

**（1）常规文件操作**

关于文件操作的常规模式：

file的对象属性

file对象的方法

**（2）OS模块**
- 关于文件的功能- 关于文件夹的功能
### 11. 修饰器/装饰器 

**案例：**classmethod的用法举例

```
class B:
    age = 10
    def __init__(self,name):
        self.name = name
    @classmethod
    def eat(cls): #普通函数
        print(cls.age)

    def sleep(self):
        print(self)

b = B("小贱人")
b.eat()

#运行结果为:10
```

### 12. 正则 

**案例：**用split()函数分割一个字符串并转换成列表

```
import re
s = "abcabcacc"
l = re.split("b",s)
print(l)

#运行结果为：['a', 'ca', 'cacc']
```

### 结语 

这篇文章的目的，不是为了教大家怎么使用函数，而是为了快速、便捷地记住常用的函数名，所以没有把每个函数的用法都给大家举例，你只有记住了函数名字和它的作用之后，你才会有头绪，至于函数的用法，百度一下就出来，用了几次你就会了。

如果连函数名和它的用途都不知道，你要花的时间和精力就更多了，必然不如我们带着目的性地去查资料会更快些。

推荐阅读  点击标题可跳转
- - - - - - - - - 
<img src="https://img-blog.csdnimg.cn/img_convert/dacd24d45349434e87203aec7361fc39.gif" alt="dacd24d45349434e87203aec7361fc39.gif">
