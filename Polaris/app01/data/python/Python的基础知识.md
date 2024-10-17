
--- 
title:  Python的基础知识 
tags: []
categories: [] 

---
## 前言

<img src="https://img-blog.csdnimg.cn/6a4b6695d5ae4de4b04723f6cabd8aac.png#pic_center" alt="在这里插入图片描述">

本章将介绍基础语法、基本数据类型、条件判断、循环、函数、模块几部分介绍Python的基础知识。

### **一、基础语法**

**1、注释**

Python中单行注释以 **#** 开头，实例如下：

<img src="https://img-blog.csdnimg.cn/img_convert/ab9b489c34afc866d55fc95e702d63bd.png#pic_center" alt="img">

多行注释可以用多个 **#** 号，还有 **‘’’** 和 **“”"**：实例如下：

<img src="https://img-blog.csdnimg.cn/img_convert/cd0f1b2adbcd6e2ceadba933cdf3aff6.png#pic_center" alt="img">

**2、行与缩进**

python最具特色的就是使用缩进来表示代码块，不需要使用大括号 **{}** 。

缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：

<img src="https://img-blog.csdnimg.cn/img_convert/627625f9a0e0056e75b4e6fcd43adafa.png#pic_center" alt="img">

错误的缩进

<img src="https://img-blog.csdnimg.cn/img_convert/2059b624b84b806b34d26902df6676ca.png#pic_center" alt="img">

正确的缩进

**3、变量**

Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

等号（=）用来给变量赋值。

等号（=）运算符左边是一个变量名

等号（=）运算符右边是存储在变量中的值

<mark>**【----帮助Python学习，以下所有学习资料文末免费领！----】**</mark>

### **二、基本数据类型**

Python3 中有5个标准数据类型：String（字符串）、Number（数字）、List容器、Bool（布尔）、None(空值)

容器又可分为List（列表）、Tuple（元组）、Set（集合）、Dictionary（字典）四种。

**其中**String（字符串）、Number（数字）、Tuple（元组）、Bool（布尔）、None(空值)为**不可变数据；<strong>List（列表）、Dictionary（字典）、Set（集合）为**可变数据</strong>。

**（一）、字符串（String）**

字符串就是表示一串字符，字符可以是中文，英文或者数字，或者混合的文本。

Python中的字符串用英文状态下的单引号 ’或双引号 " 括起来。

1、用+连接字符串

先定义变量再输出结果，例如：将namestr定义为马云，moneystr定义为有钱，输出namestr+moneystr结果为马云有钱

<img src="https://img-blog.csdnimg.cn/img_convert/17fdd5c698a2be42f1485277d273bd0b.png#pic_center" alt="img">

2、用%格式化字符串，基本用法是将值插入到%s占位符的字符串中。%s,表示格式化一个对象为字符。例如：将str1定义为’我叫%s,我爹叫%s’%(‘王思聪’,‘王健林’)，输出str1结果为我叫王思聪，我爹叫王健林

<img src="https://img-blog.csdnimg.cn/img_convert/cbb813bf381bde7092cafaa986b90f6e.png#pic_center" alt="img">

**（二）数字(Number)**

数字类型分为整数型和浮点型

整型：像11、60这种整数

浮点型：像3.14、2.50这种带小数的

**（三）容器（List）**

容器是用来存放数据的，是一种把多个元素组织在一起的数据结构，容器中的元素可以逐个地迭代获取，可以用in, not in关键字判断元素是否包含在容器中。容器是一种可以包含其他类型对象（如列表、元组、字典等）作为元素的对象

以下面的病例数据为例，来看容器的各项操作：

<img src="https://img-blog.csdnimg.cn/img_convert/efbaf8717d9704eaf0beb892a2f3d661.png#pic_center" alt="img">

**1、列表（list）**

列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号[]之间、用逗号分隔开的元素列表。具体操作如下：

先定义病人姓名，查看列表长度

<img src="https://img-blog.csdnimg.cn/img_convert/53dfcaeedaf8d0e9ecb947358def36cc.png#pic_center" alt="img">

增加一个元素：刘帅

<img src="https://img-blog.csdnimg.cn/img_convert/1d4268e01621965211ba1bdaf6243440.png#pic_center" alt="img">

删除一个元素：王伟

<img src="https://img-blog.csdnimg.cn/img_convert/11c39b35f8da753e71063cafe16e0f12.png#pic_center" alt="img">

**序列中的每个值都有对应的位置值，称之为索引，第一个索引是 0，第二个索引是 1，依此类推。**

查询：第一个元素namelist[0]

<img src="https://img-blog.csdnimg.cn/img_convert/b42c3c4a3c9902f6563417ec9ff9890b.png#pic_center" alt="img">

修改：将第2个元素陈雷修改为何欢

<img src="https://img-blog.csdnimg.cn/img_convert/33d9b38ec50110026411b18678e18c86.png#pic_center" alt="img">

最终列表为

<img src="https://img-blog.csdnimg.cn/img_convert/3e47479e8c66d5de7b4bf7ffd34dcfc1.png#pic_center" alt="img">

**2、元祖（Tuple）**

元组的元素不能修改。元组写在小括号()里，元素之间用逗号隔开。

元组是不可变类型，不支持增删改，只能查询

<img src="https://img-blog.csdnimg.cn/img_convert/76c1ac0e71d654700caf7c77f49a2e4e.png#pic_center" alt="img">

元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：

<img src="https://img-blog.csdnimg.cn/img_convert/1195877a42ad01a541ff0c6d28c56946.png#pic_center" alt="img">

**3、集合（Set）**

集合（set）是一个无序的不重复元素序列。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用set() 而不是 { } ，因为 { } 是用来创建一个空字典。

创建格式：

<img src="https://img-blog.csdnimg.cn/img_convert/d5be2c1b53505e0dbdf74e985361330e.png#pic_center" alt="img">

删除元素‘京东’

<img src="https://img-blog.csdnimg.cn/img_convert/31a3cc88bcfdbb7e597ddc706bd4a15c.png#pic_center" alt="img">

在集合中查找是否有元素‘腾讯’

<img src="https://img-blog.csdnimg.cn/img_convert/1177ecfdc9570c752ef331644da0a64a.png#pic_center" alt="img">

集合的修改元素，需要将要修改的元素删除然后再增加新元素

<img src="https://img-blog.csdnimg.cn/img_convert/f4889a6e994eefeacfaad45ca5c6d4b7.png#pic_center" alt="img">

**4、字典(Dictionary)**

字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 key=&gt;value 对用冒号：分割，每个对之间用逗号(**,**)分割，整个字典包括在花括号 { } 中 ,键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字。

格式如下所示：

定义字典，将病人编号和病人姓名关联成为映射关系

<img src="https://img-blog.csdnimg.cn/img_convert/ef0189377a3b455937b23ec2b80dd011.png#pic_center" alt="img">

将上面Excel表中病人数据存储

<img src="https://img-blog.csdnimg.cn/img_convert/56ea3be113d54fb3632b391b0c1ff641.png#pic_center" alt="img">

增加005号病人信息

<img src="https://img-blog.csdnimg.cn/img_convert/79cc8139500e57ad50e1db6b9f25d85b.png#pic_center" alt="img">

删除005号病人信息

<img src="https://img-blog.csdnimg.cn/img_convert/8c4cdc61ce2a941a399e24a171ef2dc2.png#pic_center" alt="img">

查询002号病人信息

<img src="https://img-blog.csdnimg.cn/img_convert/08545a5bc7b3928531e9c79f9336875d.png#pic_center" alt="img">

将001号病人的病情进行修改

<img src="https://img-blog.csdnimg.cn/img_convert/e1504dfb79b0b6ca82f2565dce84b9bd.png#pic_center" alt="img">

最后病例数据如下

<img src="https://img-blog.csdnimg.cn/img_convert/e6e190a511cfc1b8ba7f25fda743f679.png#pic_center" alt="img">

**（四）、布尔类型**

布尔值只有两个：True 和 False

布尔值加上比较运算符,与两边的数据一起构成了布尔表达式，返回布尔值。所谓布尔表达式，其实就是条件测试的别名。

注：比较运算符

等于 == 大于等于&gt;=

小于等于&lt;= 不等于 ！=

大于 &gt; 小于 &lt;

<img src="https://img-blog.csdnimg.cn/img_convert/91a9d471f3c7d2702f80b2176a34ae74.png#pic_center" alt="img">

**（五）、空值None**

与SQL中null是一个意思，表示该值是一个空对象。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。可以将None赋值给任何变量，也可以给None值变量赋值。

<img src="https://img-blog.csdnimg.cn/img_convert/ff6e47cacf31fd5cc2d22f78ae501b44.png#pic_center" alt="img">

### **三、条件判断**

Python 条件语句是通过一条或多条语句的执行结果（True 或者 False）来决定执行的代码块。

Python 中用elif代替了else if，所以if语句的关键字为：if – elif – else。一般形式如下所示：

<img src="https://img-blog.csdnimg.cn/img_convert/d2b30cd2056299957f97d321ac737fb4.png#pic_center" alt="img">

**注意：**

**1、每个条件后面要使用冒号：，表示接下来是满足条件后要执行的语句块。**

**2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。3、在Python中没有switch – case语句。**

<img src="https://img-blog.csdnimg.cn/img_convert/dc5097c1d5a85824917fa124ee530f72.png#pic_center" alt="img">

常见的边界条件分为两种

1.值比较：即&gt;(大于),&lt;(小于),&gt;=(大于等于),&lt;=(小于等于),!=(不等于),==(等于)

2.逻辑比较：and（并且），or（或者），not（不是）

**3、多条件判断：当有多个条件时，如何根据条件进行判断**

<img src="https://img-blog.csdnimg.cn/img_convert/b45576a7918a05e708600dd3d6aff9b6.png#pic_center" alt="img">

### **四、循环**

循环就是把容器中每一个的数据都按照特定的规则进行重复处理数据的方式。Python 中的循环语句有 for 和 while两种。这里主要介绍for循环。

for循环的一般格式如下：

```
for i in 容器: 
     要做的事情

```

例如：

<img src="https://img-blog.csdnimg.cn/img_convert/5d55021b1aa3f895bf00a21d711e31a3.png#pic_center" alt="img">

**continue用于跳出当前循环**

例如：当key=苹果时，跳出苹果的循环，继续下一个循环

<img src="https://img-blog.csdnimg.cn/img_convert/f0adbf185c622633c84c15994a50bfb7.png#pic_center" alt="img">

**break用于退出整个循环**

例如：当key=苹果时，结束循环

<img src="https://img-blog.csdnimg.cn/img_convert/f3e4f2ac64f99d51660ad70ea082acfa.png#pic_center" alt="img">

### **五、函数**

函数是根据一定的规则进行运算，可以重复使用的代码段。函数的3个功能为：实现特定功能、输入数据、输出结果。大部分时候我们只需要调用系统自带的函数或者第三方包里的函数即可，有的时候在处理复杂数据时，需要自定义函数。

函数一般格式如下：

```
def 函数名称（参数1，参数2）：
    函数体
    Return 输出

```

以下面函数为例，先输入x,y两个数，定义z是x,y两个数相加，输入z（两个数相加的和），有两种方法：方法一按照函数输入的先后顺序对应传参，方法二按照参数名对应传参，当我们定义的函数参数较多时，用参数名进行传参既不用考虑参数赋值的先后顺序，也方便阅读和理解。

<img src="https://img-blog.csdnimg.cn/img_convert/859a82a9c35579a3e57c3b6f893f3e00.png#pic_center" alt="img">

<img src="https://img-blog.csdnimg.cn/img_convert/37ca48d798bffab4e278c510ecd788ad.png#pic_center" alt="img">

方法一

<img src="https://img-blog.csdnimg.cn/img_convert/6fc053660fa2fc067de9b1c4e65321b7.png#pic_center" alt="img">

方法二

**当函数参数为不可变数据类型（字符串、数字，元祖，布尔，空值None），如果我们定义的是改变列表的值，传递的只是该数据类型的值，不会改变数据结果。**

<img src="https://img-blog.csdnimg.cn/img_convert/944917bdee6434a678429d1dd6f4416e.png#pic_center" alt="img">

当函数参数为可变数据类型（列表、集合、字典）**如果我们定义的是改变列表的值，传递的是该变量的引用地址，会改变数据结果。**

<img src="https://img-blog.csdnimg.cn/img_convert/34ee87fa6c97f51468d179a1bd7f16d4.png#pic_center" alt="img">

变量作用域

Python的作用域一共有2种：全局作用域，局部作用域。

定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。

<img src="https://img-blog.csdnimg.cn/img_convert/f2a95c841c4004ca6b5e876a2c8e5879.png#pic_center" alt="img">

### **六、模块**

我们之前介绍函数是完成特定功能的一段程序，是可复用程序的最小组成单位；类是包含一组数据及操作这些数据或传递消息的函数的集合。模块是在函数和类的基础上，将一系列相关代码组织到一起的集合体。在 Python 中，一个模块就是一个扩展名为 .py 的源程序文件。 为了方便调用将一些功能相近的模块组织在一起，或是将一个较为复杂的模块拆分为多个组成部分，可以将这些 .py 源程序文件放在同一个文件夹下，按照 Python 的规则进行管理，这样的文件夹和其中的文件就称为包，库则是功能相关联的包的集合。python常用的模块包括内置模块和第三方工具包。

**1.调用python内置模块的方式如下，使用Tab键可以读取内置模块的函数LIST**

<img src="https://img-blog.csdnimg.cn/img_convert/661a49b8263627f7062a961c874480d2.png#pic_center" alt="img">

<img src="https://img-blog.csdnimg.cn/img_convert/56ead75aaf4fd7e768ce11e2a7736142.png#pic_center" alt="img">

**引入内模块的三种语法：**

**import 包名称**

**import 包名称 as 别名**

**from 包名称 Import 模块名**

**2、调用第三方包方式如下：**

<img src="https://img-blog.csdnimg.cn/img_convert/27a912d81eac07887133a1a495cfb356.png#pic_center" alt="img">

### **七、数据结构**

除了上边提到的五种数据类型，python还有一些常用的数据结构，在集合collections这个python内建的数据模块中，我们可以定义一些常用的数据结构有队列双向链表：queue、栈，计数器counter。

**1、列表作为队列使用**

像排队一样先添加的元素被最先取出 (先进先出，后进后出）

<img src="https://img-blog.csdnimg.cn/img_convert/6ed629cd5230223444114f7c52a6aa62.png#pic_center" alt="img">

**2、列表作为栈使用**

最后一个插入，最先取出（“后进先出”）

<img src="https://img-blog.csdnimg.cn/img_convert/50357999ffe380946575e6e34c219375.png#pic_center" alt="img">

**3、计数器（Counter）**

<img src="https://img-blog.csdnimg.cn/img_convert/ae6664fc7de3297b57f427e491470c4a.png#pic_center" alt="img">

以上便是Python的一些基础内容，看起来很简单，但还是需要多敲代码才能熟练，各位伙伴我们一起加油吧！

<mark>**读者福利：如果大家对Python感兴趣，这套python学习资料一定对你有用**</mark>

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以根据这些资料规划好学习计划和方向。 


<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习等习教程。带你从零基础系统性的学好Python！</mark>

## 零基础Python学习资源介绍

① Python所有方向的<mark>学习路线图</mark>，清楚各个方向要学什么东西

② 600多节<mark>Python课程视频</mark>，涵盖必备基础、爬虫和数据分析

③ 100多个<mark>Python实战案例</mark>，含50个超大型项目详解，学习不再是只会理论

④ 20款主流手游迫解 <mark>爬虫手游逆行迫解教程包</mark>

⑤ <mark>爬虫与反爬虫攻防</mark>教程包，含15个大型网站迫解

⑥ <mark>爬虫APP逆向实战</mark>教程包，含45项绝密技术详解

⑦ 超<mark>300本Python电子好书</mark>，从入门到高阶应有尽有

⑧ 华为出品独家<mark>Python漫画教程</mark>，手机也能学习

⑨ 历年互联网企业<mark>Python面试真题</mark>,复习时非常方便

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取哈）**</mark> <img src="https://img-blog.csdnimg.cn/img_convert/673b13641cf2ddf5e18b5c58afd50200.png#pic_center" alt="">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉实战案例👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。 <img src="https://img-blog.csdnimg.cn/94e5ddc9daa6482097eeaddcadd0efa5.png#pic_center" alt="在这里插入图片描述">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

## 资料领取

<mark>这份完整版的Python全套学习资料已经上传网盘，朋友们如果需要可以点击下方微信卡片免费领取 **↓↓↓**【保证100%免费】</mark> <font color="red" size="3"> **或者**</font> 【】领取

## 好文推荐

**了解python的前景：**

**了解python的兼职副业：**
