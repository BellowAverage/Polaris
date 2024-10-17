
--- 
title:  Python编程技巧 – 编写单行if条件语句 
tags: []
categories: [] 

---
## Python编程技巧 – 编写单行if条件语句

### Python Programming Skills – Program Single-liner if Conditionals

By Jackson@ML

通常，我们在写Python代码的时候，都会按部就班地一行行写完，代码的丰富足以让自己骄傲和充实。

>  
 实际上，代码的简约易读，才是编程之道。 


大家都用过 if 条件句，但是，你有没有尝试过在一行中编写完成Python的if语句？

本文简要介绍这个方法，探讨学习如何在一行中编写简洁的Python代码。

#### 1. 普通的 if 条件语句

首先，回顾一下if条件语句的工作原理。
- 如果满足一个条件，那么执行其下的语句；- 如果不满足，则用elif执行第二种可能条件的语句；- 如果还不行，则执行else后跟的语句，结构如下所示：
```
if &lt;expression 1&gt;:
  &lt;taking_action1&gt;
ellif &lt;expression 2&gt;:
  &lt;taking_action2&gt;
else:
  &lt;taking_action3&gt;

```

下面尝试编写一个程序，通过键盘输入来打印输出今天的天气状况，代码如下所示：

```
weather = input("Enter today\'s weather:")

if weather == "sunny":
    print("Great! Sunny weather lets me go out for a walk!")
elif weather == "rainy":
    print("Oh, no! I need to bring my umbrella.")
else:
    print(f'It\'s {<!-- -->weather}, but I prefer to stay at home.')    

```

该程序的条件表示：
- 如果今天是sunny(晴天)，那么很开心，要出去走走；- 如果今天下雨，则提醒自己需要带上雨伞；- 如果是其它天气（无论多云cloudy,还是什么天气），只想待在家里。
运行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/2fba6cb4e4b24c6cb07934818ee2a20f.png" alt="在这里插入图片描述">

#### 2. 单行的if/then/else语句

单行的if条件语句，将大大简化代码，在一行中集中显示，便于阅读同时使代码高效。

代码基本架构如下： if : &lt;taking_action&gt;&lt;/taking_action&gt;

##### 1） 示例一：判断奇数偶数

例如：从键盘输入任意数字，可以判断出是奇数（被2除取余为1）；判断是偶数（被2整除）；由于从键盘输入的是字符串，因此需要先转换为int整型。代码如下：

```
n = int(input("Enter an integer: "))
if n % 2 != 0 : print(f'{<!-- -->n} is an odd number.') ; print("Once again.")
if n % 2 == 0 : print(f'{<!-- -->n} is an even number.') ; print("Once again.")

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/87a8869302c643a5bfd4621add4245e2.png" alt="在这里插入图片描述">

当输入15时，结果提示为一个奇数；而当输入8时，结果提示为一个偶数。

##### 2） 示例二：判断天气

例如，判断天气是否为晴天(sunny)，可以在一行内实现代码如下：

```
if weather == ‘sunny’: print(“Great! Sunny weather lets me go out for a walk.”)

```

但如果包含几种天气情况，那么一行代码只可以表示一种天气输出，全部可能性就要用多个单行来表示。尽管这样，代码总数也可以缩减为四行：

```
weather = input("Enter today\'s weather:")

if weather == "sunny": print("Great! Sunny weather lets me go out for a walk!")
elif weather == "rainy": print("Oh, no! I need to bring my umbrella.")
else: print(f'It\'s {<!-- -->weather}, but I prefer to stay at home.')   

```

运行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/b57989438f464805b891eb7fe87bcc8a.png" alt="在这里插入图片描述">

技术好文陆续推出，敬请关注。

您的认可，我的动力。😃

#### 相关阅读：
1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 