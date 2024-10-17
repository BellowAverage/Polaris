
--- 
title:  初识Python(注释、编码规范、关键字...) 
tags: []
categories: [] 

---
>  
 🥇<font size="3" color="#8A2BE2">**作者简介：CSDN内容合伙人、新星计划第三季Python赛道Top1** <font size="3" color="red">🔥**本文已收录于Python系列专栏：**  </font> <font size="3" color="#0099ff">**💬订阅专栏后可私信博主进入Python学习交流群，进群可领取Python视频教程以及Python相关电子书合集**</font> `私信未回可以加V：hacker0327 备注零基础学Python` <img src="https://img-blog.csdnimg.cn/direct/bd6c194f87224cc7a9fb30e008916b50.png#pic_center" alt="在这里插入图片描述"></font> 


>  
 `订阅专栏附赠此专栏思维导图，可直接点击链接跳转学习` <img src="https://img-blog.csdnimg.cn/direct/8e6f83db6be546b392ac6694e7e5bffe.gif#pic_center" alt="在这里插入图片描述"> 


>  
 `零基础学Python系列专栏面向零基础读者倾心打造，永久免费订阅，一个专栏带你吃透Python，旨在帮助初学者从零开始学习Python` `从搭建环境、基础语法入手到深入学习掌握各种核心库和框架，学习利用Requests、Beautiful Soup、Scrapy等库从网络上获取数据、利用Pygame库进行游戏开发、利用NumPy、Pandas、Matplotlib等库进行数据分析，数据可视化、利用Django、Flask框架构建网站和Web应用程序等等，最终掌握并应用于实际项目。学习不断，持续更新，火热订阅中🔥` <img src="https://img-blog.csdnimg.cn/direct/6ff118ba83c447f6b2e796c1bae26825.png#pic_center" alt="在这里插入图片描述"> 




#### 初识Python
- - <ul><li>- - - - - - - - - - - 


## 💬注释

### 单行注释

>  
 在Python中使用"#“作为单行注释的符号，从符号”#“开始直到换行为止，”#"后面所有的内容都作为注释内容，同时注释内容会被Python编译器忽略 单行注释可以放在要注释代码的前一行，也可放在要注释代码的右侧 


💬第一种方式

```
# 输出hello world
print("hello world")  

```

💬第二种方式

```
print("hello world")  # 输出hello world

```

上面两种方式运行结果如下：

<img src="https://img-blog.csdnimg.cn/direct/e9844e50fe90494b803fc56f6545093d.png" alt="在这里插入图片描述">

### 多行注释

>  
 在Python中，使用三对单引号或者三对双引号进行多行注释，推荐使用三对双引号进行多行注释 多行注释通常为Python文件、模块、类或者函数等添加版权、功能等信息 `多行注释主要还是用作字符串，在后面的文章讲解字符串的时候会讲到` 


💬第一种方式`(不推荐)`

```
'''
这是一个多行注释
单引号包裹的部分会被Python解释器忽略
输出hello world
'''
print("hello world")

```

当使用三对单引号进行多行注释时，Pycharm会显示出来灰色波浪线，虽然不影响代码运行，但很影响程序美观。当代码下面出现波浪线时，通常表示代码存在一些警告或者建议

<img src="https://img-blog.csdnimg.cn/direct/4fb7241727604010a868c7c0034b0b17.png" alt="在这里插入图片描述">

我们可以将鼠标悬停在波浪线上查看相应信息，根据提示修改即可 详细解决方案见此文章：

<img src="https://img-blog.csdnimg.cn/direct/c3376f844614417da160c8f9b8bc7bc8.png" alt="在这里插入图片描述">

💬第二种方式`(推荐)`

```
"""
这是一个多行注释
双引号包裹的部分会被Python解释器忽略
输出hello world
"""
print("hello world")

```

上面两种方式运行结果如下：

<img src="https://img-blog.csdnimg.cn/direct/4d1a50baf11c49759700e38473f9db74.png" alt="在这里插入图片描述">

### 文件注释

>  
 文件注释通常放在文件开头，用于描述文件的内容、功能、作者信息以及其他相关信息 在文件注释中，通常包括以下信息 
 - 模块名：模块的名称- 描述：文件的用途- 作者信息：作者的姓名或者用户名- 日期：文件创建或最后修改的日期 
 除了这些基础信息外，文件注释还可以包括其他相关信息，例如版权声明、许可证信息、文件版本等。 良好的文件注释可以帮助其他开发者更好地理解和使用代码，特别是在大型项目或者团队合作的情况下，它们是非常有价值的。 


以下是一个典型的Python文件注释示例：

```
"""
模块: 初识Python.py
描述: 讲解Python基础知识，包括输出、变量、运算符等
作者: hacker707
日期: 2024-04-09
"""
print("hello world")  # 输出hello world
a = 10  # 定义变量a
b = 20  # 定义变量b
print(a + b)  # 输出a + b的值

```

### 文档注释

在Python中，文档注释（docstrings）是用来描述函数、类、模块等代码单元的文本。这些注释以三对单引号 ‘’’ 或者三对双引号’‘’‘’'包裹起来，推荐使用`三对双引号''''''` 可以跨越多行，并且可以被Python解释器识别为文档字符串。文档注释可以通过`__doc__属性`进行访问。 文档注释的主要目的是提供有关代码单元的使用方法、功能说明、参数说明、返回值说明等信息。这些信息可以被工具和IDE用来提供代码提示、文档查看等功能，也可以用于自动生成文档。

以下是一个简单的函数文档注释示例：

```
def calculate_area(inner_radius):
    """
    计算圆的面积

    该函数接受一个半径值作为参数，并返回对应圆的面积。

    参数:
    inne_radius (float): 圆的半径值，必须为非负实数。

    返回:
    float: 圆的面积，以平方单位表示。
    """
    if inner_radius &lt; 0:
        raise ValueError("半径值必须为非负实数")
    return 3.14159 * inner_radius ** 2


# 使用示例
outer_radius = 5.0
area = calculate_area(outer_radius)
print("圆的面积:", area)

```

在这个示例中，文档注释清晰地描述了函数的功能、参数和返回值，以及参数的数据类型。 良好的文档注释可以提高代码的可读性和可维护性，让其他开发者更容易理解和使用你的代码。

运行结果如下： <img src="https://img-blog.csdnimg.cn/direct/29d22cacc9b846f981d11f46f385f35d.png" alt="在这里插入图片描述">

### 代码注释

>  
 代码注释是给阅读源代码的人参考的，起到解释说明，帮助阅读者理解代码功能的作用 ，一般使用单行或者多行注释 


<img src="https://img-blog.csdnimg.cn/direct/d65504e1be514ad3afc96b428d0b3f19.png" alt="在这里插入图片描述">

### TODO注释

>  
 在 PyCharm 中，TODO 注释是一种特殊类型的注释，用于标记代码中需要完成或者需要注意的任务。这些注释通常用于标记临时的、尚未完成的工作，或者需要后续处理的问题，以便开发者可以方便地找到并跟踪这些任务。 通常，TODO 注释以 `TODO: `开头，后面跟着任务的描述或者说明。在 PyCharm 中，TODO 注释通常会被特殊地高亮显示，以便开发者更容易地识别它们。 


以下是一个示例 TODO 注释：

```
# TODO: 1. 输出hello world
print("hello world")
# TODO: 2. 使用for循环分别输出a字符串中每个字符
a = "hello world"
for i in a:
    print(i)

```

通过在代码中添加 TODO 注释，开发者可以快速识别出需要处理的任务，并在后续的开发过程中进行跟踪和处理。PyCharm 还提供了工具和功能，可以让开发者方便地查看项目中所有的 TODO 注释，并跳转到相应的位置进行处理。这有助于提高代码的可维护性和开发效率。

`可以在View—&gt;Tool Windows中点击TODO即可进入TODO视图界面`

<img src="https://img-blog.csdnimg.cn/direct/5b1ecc8ce1944f9abb926f5ddf7731e4.png" alt="在这里插入图片描述">

>  
 我的图标与默认的不同是因为使用了PyCharm里的一个美化图标的插件，感兴趣的可以看以下文章自行探索：  


`也可以在Pycharm左下角点击TODO视图图标即可打开TODO视图界面`

<img src="https://img-blog.csdnimg.cn/direct/5773300f251b4c46a1f2bcf19ae7c5c2.png" alt="在这里插入图片描述">

`点击即可跳转至相应的TODO注释位置`

<img src="https://img-blog.csdnimg.cn/direct/81d76a2a0aae42e1a8b46473ad7926ba.png" alt="在这里插入图片描述">

## 💬代码缩进

>  
 Python不像其他程序设计语言（如Java或者C语言）采用大括号"{}"来分隔代码块，而是采用代码缩进来区分代码之间的层次。Python 的语法规定，代码块之间的缩进必须保持一致. 注意事项：缩进可以使用空格或者Tab键实现，其中，使用空格时，通常情况下采用4个空格作为一个缩进单位，而使用tab键，则采用一个Tab键作为一个缩进单位。通常情况下建议采用空格进行缩进。 


```
num = 10

if num &gt; 5:
    print("num is greater than 5")

else:
    print("num is not greater than 5")

print("This line is outside the if-else block")

```

<img src="https://img-blog.csdnimg.cn/direct/2262a95fe6dc40f79eceb838458eeb49.png" alt="在这里插入图片描述"> `代码讲解(通过讲解代码来了解代码缩进级别)`

>  
 以上代码实现的功能是当num的值大于5也就是符合条件时输出num is greater than 5，否则输出num is not greater than 5 这段代码中红色块、蓝色块分别表示一个缩进级别，同一个级别缩进量必须相同。如果同级缩进量不同就会报错，详细报错解决方案见此文章：： num的值大于5，满足条件所以会执行if代码块中的print语句，而else代码块中的print语句不会执行。在这段代码中还有一个print语句也会执行，因为该代码块和最外层缩进一样，属于最外层的代码，无论符不符合条件都会执行 <img src="https://img-blog.csdnimg.cn/direct/6b9500cee1cf4234a2740be425bd7d04.png" alt="在这里插入图片描述"> 


## 💬标识符命名规范

>  
 在Python中，标识符是用来命名变量、函数、类以及其他对象的名称。 以下是Python标识符的命名规范： 
 - 标识符可以包含字母（大小写均可）、数字和下划线- 标识符不能以数字开头- 标识符不能包含空格，可以使用下划线 _ 来分隔单词- 标识符不能使用Python中的关键字- 标识符不能使用Python中的内置函数- Python是区分大小写的，因此大写字母和小写字母被视为不同的标识符 
 遵循这些命名规范可以使你的代码更易读、易维护，并且与Python社区的约定保持一致。 


❎错误示例：

```
1variable = 10  # 使用数字开头
my variable = 10 # 使用空格
my@variable = 10 # 使用特殊字符
if = 10 # 使用关键字
max = 10 # 使用内置函数

```

✅正确示例：

```
variable_name = 10  # 包含字母和下划线，但不以数字开头
my_variable1 = 10  # 包含字母、数字和下划线，但不以数字开头
_variable = 10  # 包含字母和下划线，以下划线开头
variable1 = 10  # 包含字母和数字，但不以数字开头

```

💬Python 的标识符命名规范通常包括以下几种分类：
- 变量名：用于标识存储数据的名称。变量名应当具有描述性，清晰地表达所代表的含义，变量名通常使用蛇形命名法 ✨示例：`my_variable、num_of_students、total_sum`- 常量名：用于标识不可变的值，通常在程序中固定不变。变量名通常使用大写字母，使用下划线分割单词 ✨示例：`PI 、DEFAULT_TIMEOUT、MAX_SIZE`- 函数名：用于标识可调用的代码块，执行特定任务或操作数据，函数名应当具有描述性，函数名通常使用蛇形命名法 ✨示例：`calculate_total 、display_results 、get_user_input`- 类名：用于定义对象类型，类名通常使用驼峰命名法 ✨示例：`Student 、FetchUserDetailsFromDatabase 、generateRandomNumber`- 模块名：用于组织代码，并将相关功能组织成单个单元，模块名应当简介明了，使用小写字母，使用下划线分割单词 ✨示例：`math 、random、requests `
遵循这些命名规范可以使你的代码更易读、易维护，并且与Python社区的约定保持一致。

## 💬编码规范

Python中采用PEP8作为编码规范，官方详细参考文档： 下面列出一些需要严格遵守的编码规范
- 每个import语句只导入一个模块，尽量避免一次导入多个模块 推荐写法：`import math`- 不要在行尾添加`;`号- 每行代码建议不超过79个字符，如果超过，可以使用`()`将多行内容连接起来 ✨示例：
```
motto = ("不断的翻越一座又一座的高山，那样的人生才是我想要的。"
         "这一马平川，一眼见底的活，我不想要。我的人生，我自己书写"
         "余生很长，请多关照，我的人生，敬请期待")

```

## 💬变量与常量

### 变量

>  
 变量是用来存储数据值的标识符。 在 Python 中，变量不需要显式声明类型，可以直接进行赋值操作。 变量的值可以随时被改变。 变量名是由字母、数字和下划线组成，但不能以数字开头。 


✨示例：

```
x = 5  # 将整数值 5 赋给变量 x
name = "Alice"  # 将字符串值 "Alice" 赋给变量 name

```

### 常量

>  
 在 Python 中，没有严格的常量概念，因为 Python 不提供内置的常量类型。 通常，程序员会使用全大写字母命名的变量来表示常量，表示这个变量的值不应该被修改。 尽管 Python中的常量并不是真正意义上的常量，但这种命名约定有助于提高代码的可读性和维护性。 


✨示例：

```
PI = 3.14159  # 表示圆周率的常量，通常使用全大写字母命名
MAX_SIZE = 100  # 表示最大尺寸的常量，通常使用全大写字母命名

```

总之，变量是可变的、可以被赋予不同值的标识符，而常量是不可变的，通常通过使用全大写字母命名的变量来表示。

## 💬Python关键字

### 关键字简介

>  
 关键字是Python语言中被赋予特殊含义的单词，开发程序时，不可以把这些关键字作为变量、函数、类、模块、和其他对象的名称来使用 如果使用关键字进行命名会报以下异常：`SyntaxError: invalid syntax`：语法错误 


<img src="https://img-blog.csdnimg.cn/direct/7a299b19f9544de095d276cbbca03ebd.png" alt="在这里插入图片描述">

在Python3.12.2版本中，一共有35个关键字，如下表所示 `False、None、True首字母为大写，其他关键字为小写`

|False|None|True|and|as|assert|async
|------
|await|break|class|continue|def|del|elif
|else|except|finally|for|from|global|if
|import|in|is|lambda|nonlocal|not|or
|pass|raise|return|try|while|with|yield

### 查看Python关键字

`如果想要查看Python中所有的关键字可以使用以下代码进行查看`

```
import keyword  # 引入关键字模块

print(keyword.kwlist)  # 打印关键字列表

```

<img src="https://img-blog.csdnimg.cn/direct/79513922fb124749a50491f25a189053.png" alt="在这里插入图片描述">

`如果想要依次输出关键字可以使用列表中的for循环和enumerate()函数遍历(后面讲解列表的时候会讲到，这里仅作了解即可)`

```
import keyword  # 引入关键字模块

# 输出所有关键字
for index, key in enumerate(keyword.kwlist):
    # 输出序号和关键字
    print(index + 1, key)

```

<img src="https://img-blog.csdnimg.cn/direct/8f66c86f1af545a0a5aa04a3b54383ae.png" alt="在这里插入图片描述">

## import与from…import…

### import

1️⃣使用import语句导入整个模块，然后通过模块名访问其中的对象 ✨示例：

```
import math  # 导入math模块

print(math.pi)  # 输出圆周率

```

2️⃣导入整个模块并使用别名 ✨示例：

```
import math as m  # 导入math模块并重命名为m

print(m.pi)  # 输出圆周率

```

### from…import…

1️⃣导入模块中单个对象 ✨示例：

```
from math import pi  # 导入math模块中的pi

print(pi)  # 输出圆周率

```

2️⃣导入模块中多个对象 ✨示例：

```
from math import pi, sqrt  # 导入math模块中的pi和sqrt函数

print(pi, sqrt(100))  # 输出圆周率和100的平方根

```

3️⃣导入模块中所有对象(不推荐)

>  
 这样会导入 math 模块中的所有对象到当前命名空间。不推荐在实际开发中使用，因为可能导致命名冲突和代码可读性问题。 


✨示例：

```
from math import *

```

## 💬结束语

>  
 以上就是零基础学Python之初识Python(注释、编码规范、关键字…) 
 - `专栏订阅地址:` - `专栏订阅者可私信博主领取专栏订阅福利，进入Python学习交流群，如私信未回可以加V：hacker0327 备注零基础学Python`- `此专栏内容会持续更新直到完结为止(如有任何纰漏请在评论区留言或者私信）` 


<img src="https://img-blog.csdnimg.cn/direct/58bfd8c234304ff38ff6a5d4680bbbf4.png#pic_center" alt="在这里插入图片描述">
