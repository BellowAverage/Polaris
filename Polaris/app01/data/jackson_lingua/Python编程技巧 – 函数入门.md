
--- 
title:  Python编程技巧 – 函数入门 
tags: []
categories: [] 

---
## Python编程技巧 – 函数入门

### Python Programming Skills - Fundamentals of functions

本文简要介绍Python编程中，如何定义并使用函数，以及实现输入输出的功能。

>  
 在交互式开发环境中，要先定义函数，再调用函数，这样可以让编程变得很轻松。 定义函数需要def关键字，后跟一对括号;括号内可以有参数，于是，简单的函数很快要诞生了。 


#### 1. 简单的函数

如下代码，实现一个简单的函数，返回变量a与b的相加结果。

```
def add(a, b):
    return a + b

print(“2 + 3 = “, add(2, 3))

```

执行得到结果：

```
2 + 3 = 5

```

#### 2. 带有输入输出的函数

如果需要将输入的数值进行计算，那么，用input函数可以实现。以下函数计算得到长方体的体积。

```
def volume():
    w = float(input("Enter a width:"))
    h = float(input("Enter a height:"))
    l = float(input("Enter a length:"))
	return w * h * l

print("The volume is w * h * l = ", volume())

```

执行结果如下：

```
Enter a width: 3
Enter a height: 4
Enter a length: 5
The volume is w * h * l =  60.0

```

#### 3. 带嵌套的函数

Python代码块没有“开始”或者“结束”语法，而是依靠缩进来表明语句块开始和结束位置的。因此，每行语句缩进一定要有层次且一致。特别是代码块内部还有嵌套的情况。

如下代码：

```
def main():
    age = int(input("Enter your age: "))
    name = input("Enter your name: ")
    if age &lt; 30:
        print("Hello", name)
        print("I see you are less than 30.")
        print("You are so young.")
main()

```

代码执行结果如下：

```
Enter your age:  28
Enter your name:  Jackson
Hello Jackson
I see you are less than 30.
You are so young.

```

#### 4. 总结

小结一下，创建一个Python函数，就像创建一个自己的小程序，需使用def 语句，并在函数中不断输入内容，直到结束定义。

接下来，输入空白行，之后通过键入函数名和括号来运行该函数。 定义好函数后，可以根据需要多次执行（调用）该函数。

感谢关注！喜欢就点赞哈 😃
