
--- 
title:  Python和JavaScript的主要区别 
tags: []
categories: [] 

---
Python和JavaScript是网络开发中使用的重要语言。Python可用于后端开发，而JavaScript则可用于前端和后端开发。本文将分析这两种语言的主要区别。

#### Python和JavaScript在现实世界中的应用

Python可以用于科学和专业应用，也可以用于网络开发。然而，JavaScript在网络开发中被广泛使用。

#### 语法、感官和功能的差异

Python和JavaScript有不同的语法。

这一点在下面得到了证明。

Python和JavaScript中的代码块

在Python中，代码行通过缩进被放在块中。

例子

```
if  t  &gt; 10:       
     print (t) #code block
复制代码
```

在JavaScript中，可以使用括号而不是空格。

让我们看一个例子。

```
if (t&gt;10)

{
    console.log(t)
}
复制代码
```

#### 变量的定义

在Python中定义变量时，变量名称后面写上一个等号（=）。

然后给变量分配一个值，即

```
&lt;variable_name&gt; = value
x = 56
复制代码
```

在JavaScript中，在变量名前加一个关键字`var` ，用分号来结束语句，即：。

```
var &lt;variable_name&gt;  = value;
var k=34;
复制代码
```

#### 变量命名规则

在Python中，使用的是`snake_case` 命名方式。名称应以`lowercase` ，并以`underscore` 分隔，如下图所示。

```
first_name
复制代码
```

在JavaScript中，`lowerCamelCase` 是首选。变量名称以小写字母开头，其他每一个新词都以大写字母开头。

```
myFirstName
复制代码
```

#### Python和JavaScript中的常量

在Python中，常量以`uppercase` 格式书写，用下划线分隔。如：`CONSTANT_NAME` 。

比如说。

```
PASS_RATE = 4
复制代码
```

在JavaScript中，在常量名称前加一个关键词`const` ，用分号来结束语句。即：`const CONSTANT_NAME = value` 。

```
const AGE=56;
复制代码
```

#### Python和JavaScript中的数据类型和值

数值数据类型

在Python中，我们有三种数字类型，可以帮助我们完成逻辑上的精确估计。

它们是
1. [int]1. [float]1. [复数]
在JavaScript中，我们有两种数字类型，`Numbers`和`BigInt` 。这两个整数和投点数字只是作为数字来看。
1. [数字]1. [bigint]
#### Python和JavaScript中的None和Null

在Python中，当一个变量没有赋值时，它被称为`None` 。在JavaScript中，我们用`null` 来表示这种变量。

#### 未定义值

在Python中，人们不能声明一个没有初始值的变量。

在Javascript中，我们有一个唯一的价值，并随之分配。当一个变量被声明而没有分配一个初始值时，它就会打印出`undefined` ，如下图所示。

```
var k; // should print undefined
复制代码
```

#### 原始数据类型

Python有四个原始数据类型。
1. [整数]1. [浮点数]1. [布尔型]1. [字符串]
另一方面，JavaScript有六个原始数据类型。
1. [未定义]1. [字符串]1. [数字]1. [BigInt]1. [布尔型]1. [符号]
#### 注释

注释有助于提高代码的可读性。例如，人们可以在某一行进行注释，以便将来参考。
1. 单行注释 在Python中，一个标签(`#`)用于在单行上进行注释。
```
# this is a  single-line comment in python
复制代码
```

在 JavaScript 中，双斜线 (`//`) 用来注释单行，如下所示。

```
//this is a single-line comment in JavaScript
复制代码
```
1. 多行注释 这些是跨越多行的注释。在python中写多行注释时，我们用一个标签(`#`)开始每一行，如下图所示。
```
# this is a   
# multiple lines 
# comment
# as used in Python`
复制代码
```

在JavaScript中写多行注释时，我们用符号(`/*`)来打开，(`*/`)来关闭注释。

```
/*
 This is  a multi-line comment
that span many lines
*/ 
复制代码
```

#### 内置的数据结构
1. 图ples Python中的图ples类似于列表，但是是不可变的。它们存储不应该被改变的信息。
在 JavaScript 中，我们没有一个固有的结构具有这样的品质。
1. 列表和数组-&gt;
列表在Python中被用来在一个类似的结构中存储一系列的品质。

```
number = [3, 4,5]
复制代码
```

在JavaScript中，数组就是这样的等效版本。

```
var number = [3,4,5]
复制代码
```

#### 比较数值和类型

在Python中，double equal (`==`) 操作符被用来比较两个值和它们的数据类型是否相等。

```
11 == 11 #True
11 == 10 #False
复制代码
```

如上所示，`11 == 11` 是真，而`11 == 10` 是假。

在JavaScript中，一个三等分（'==='）运算符被用来检查两个质量和它们的信息类型是否相等。

```
5===5  //true
5==='5'  //false
复制代码
```

#### 逻辑运算符

在Python中，有三个逻辑运算符。
1. 和1. 或1. 不是
JavaScript也有三个逻辑运算符。
1. &amp;&amp; - 逻辑的和。1. || - 逻辑上的或。1. !-逻辑非。
#### 类型运算符

在Python中检查对象的类型，我们使用(`type()`)函数，如下所示。

```
type(instance)
复制代码
```

要在JavaScript中检查对象的类型，我们使用`type of operator` ，如下图所示。

```
type of instance
复制代码
```

#### 输入和输出

`Input` 是一个要求用户提供一些反馈的函数。

`Output`另一方面，WWW是用来打印出一个特定的信息。

#### 输入

在Python中，`input()` 函数被用来要求用户输入。

例子

```
name = input (" Enter your name : ")
复制代码
```

在 JavaScript 中，你可以用`window.prompt(message)` 的小提示来获得用户的输入，然后将结果赋给一个变量。

```
var input =window.prompt ("enter a Number :")
复制代码
```

#### 输出

在Python中，我们使用`print()` 来显示特定的结果。

例子

```
num1 = input("Enter the first  number : ")
num2 = input("Enter a second  number : ")
num3 = input("Enter a third number : ")
result = num1 + num2 + num3
print(result)
复制代码
```

在JavaScript中，我们使用`console.log()` 函数在控制台中打印一个值，并解析括号内的值。

例子

```
console.log("My name is John:");
复制代码
```

#### 条件性语句

条件语句是用来判断某个条件是真的还是假的。
1. if 语句 在Python中，缩进是用来表示属于条件语句的代码行的。
```
if condition:
     #code
复制代码
```

让我们看一个例子。

```
age = 10
if age &lt; 18:
    print('kid you are!')
复制代码
```

在 JavaScript 中，条件被包围在小括号中，代码被包围在大括号中。

```
if (condition)

    {
        code
    }
复制代码
```

一个JavaScript代码片段的例子是这样的。

```
if (hour &gt; 4) {
  task = "Clean the compound";
}
复制代码
```
1. if-else 语句 在Python中，在`else` 关键字后面写一个冒号`(:)` 。
```
if condition:

    #if code

else :

    #else code
复制代码
```

我们来看看一个例子。

```
age = 34
if age &lt; 18:
    print('kid you are!')
else:
    print('You are not a kid')
复制代码
```

在JavaScript中，属于`else`子句的代码被括在大括号中。

```
if (condition)

    {
        if code
    }

else 

    {
        else code
    }
复制代码
```

让我们看一个例子。

```
var time = new Date().getHours();
if (time &lt; 5) {
  task = "Cleaning the house";
} else {
  task = "Feeding the sheep";
}
复制代码
```
1. 多重条件 在Python中，当处理多重条件时，`elif` 关键字被使用。在每个条件之后，我们写一个`semicolon``(:)` ，属于该条件的代码在下一行缩进。
```

if condition1:

    code

elif condition2:

    code

elif condition3:

    code

else:

    code
复制代码
```

让我们看一个例子。

```
age = 40
if age &lt; 18:
    print('kid you are!')
elif age &gt;=18 and age &lt; 29:
    print('You are a young star!')
elif age &gt;=29 and age &lt; 35:
    print('You are middle aged!')
else:
    print('You are above middle age !')
复制代码
```

在JavaScript中，当处理多个条件时，`else if` 关键字被使用。这些条件被小括号所包围。

```
if(condition1)

    {
        //code
    }

else if(condition2)

    {
       // code
    }

else if (condition3)

    {
        //code
    }

else

    {
        //code
    }
复制代码
```

让我们看一个例子。

```
var time = new Date().getHours();
if (time &lt; 5) {
  task = "Cleaning the house";
} else if (time &lt; 15) {
  task = "Feeding the sheep";
} else {
  task = "Watching a movie";
}
复制代码
```
1. 开关 Python没有这种类型的内置控制结构，即`switch`
在JavaScript中，开关被用来根据用户的要求选择发生什么。

```
switch(expression)

    {
        case 1:
        code
        break;

        case 2:
        code
        break;

        case 3:
        code
        break;

        default:
        code
    }
复制代码
```

让我们看一个例子。

```
switch (new Month().getMonth()) {
  case 1:
    month = "January";
    break;
  case 2:
    month = "April";
    break;
  case 3:
    month = "May";
    break;
  case 4:
    month = "June";
    break;
  case 5:
    month = "August";
    break;
  case 6:
    month = "September";
    break;
  default:
  No such a month;
}    
复制代码
```

#### 循环

循环是一种控制结构，它重复一系列的指令，直到达到指定的条件。

#### 对于循环

我们可以在Python中写一个`for` 循环，如下所示。

```
for x in range(k):

    code
复制代码
```

在JavaScript中编写for循环时的语法如下。

```
for(var x = 1; x &gt;n ; x++)

{

        code
}
复制代码
```

#### While循环

这是一个预先测试的循环，在循环执行前会对条件进行评估。

在Python中，我们将表语`while` ，后面是`condition` ，再后面是冒号`(:)` 。

```
while condition: code 
复制代码
```

在JavaScript中，我们使用括号，如下所示。

```
while(condition){
    code
}
复制代码
```

#### Do-while 循环

这是一个后测试循环。条件在循环执行后被评估。在Python中，我们没有这样的控制结构`(do-while loop)`

在JavaScript中，这个循环将总是被执行一次。

```

do { code } while (condition); 
复制代码
```

#### 函数

一个函数是一个执行特定任务的代码块。

在Python中，我们使用一个观察词`def` ，后面是函数的名称，如下图所示。

```
 def function_name ( x1 , x2 , x3 , ...):
      code 
复制代码
```

在JavaScript中，我们使用`function` 关键字来创建一个方法。

```
function function_name (x1,x2,x3,...)
        {

            code
        }
复制代码
```

#### 面向对象的编程（OOP）

OOP是以对象的方式来开发程序，这些对象可以相互作用。

Python和JavaScript都支持面向对象编程。

在Python和JavaScript中定义类的语法几乎是一样的，只是有一点区别。

在`Python` ，一个`colon` ，写在关键词class后面，而在`Javascript` ，则使用卷曲的`braces` 。

Python

```
class Rectangle:

    code
复制代码
```

JavaScript

```
class Rectangle

{

    code
}
复制代码
```

#### 构造函数和属性

构造函数是一个类的成员函数，每当一个对象被创建时就会自动执行。

在Python中，一个实例化的构造函数被称为`init` ，有两个驱动和以下亮点。

```
 class Rectangle:

        def _init _(self , length , width):
            self.length= length
            self.width=width 
复制代码
```

在JavaScript中，写一个构造函数，如下图所示。

```
class Rectangle

{

    constructor(length,width){
        this.length=length;
        this.width=width;

    }
}
复制代码
```

>  
 注意：在Python中，我们用`self` 来指代一个类的实例。 


比如说。

```

self.attribute= esteem 
复制代码
```

而在JavaScript中，我们用`this` 来暗指一个类的发生。如：。

```

this.attribute=value; 
复制代码
```

#### 结论

尽管Python和JavaScript有许多不同之处，但由于其独特的语法，Python要比JavaScript容易理解得多。
