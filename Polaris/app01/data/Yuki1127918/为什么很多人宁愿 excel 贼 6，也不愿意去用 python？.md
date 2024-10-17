
--- 
title:  为什么很多人宁愿 excel 贼 6，也不愿意去用 python？ 
tags: []
categories: [] 

---
Excel基本上每台电脑上都有，Python就差远了。很多人不会用vlookup，Python也不会玩。

非专业人士使用Excel宏就够了。学Excel编程是不可能的。语法再简单，也要有一定的编程思维，对非开发者的要求还是很高的。

主要原因是Excel学习时间长。比如大学里很多专业会教Excel，但不一定会学Python。还有一个因素就是年纪大的人习惯用Excel，所以科室的培训主要是Excel，Python是自学的，没有指导。Excel是必备技能(大部分人都用)。Python普及的有点晚，玩的好的人不多，至少不比Excel好。

接下来分析Excel和python的优缺点。

### 一、Excel数据分析

作为数据分析工作者，我们一般希望在数据分析方面更加精通，而不是在如何处理百万级别数据的问题上，停留太长时间。

有句话说，excel是数据分析的最终归宿，因为无论什么样的数据，都是要在excel上做分析的。

而我个人认为，如果你要提高自己的数据分析能力，那么应该精通excel，而不是python

因为首先，excel的功能齐全，UI操作简单，我们从小就接触，可以说门槛低，而且excel深不见底，函数，数据透视再加上VBA，已经能解决数据分析中遇到的绝大多数问题了。

而且excel拥有丰富的函数，这些函数功能齐全，可以处理字符，数学运算，逻辑判断，各种函数之间的组合，变化莫测，功能诡谲多变。

#### 数据透视表实现数据分组

数据分析python也是可以实现的，但是需要编写非常复杂的函数，如果是用excel的话，这就非常便利了。

因为excel自带的数据透视表，可以马上实现数据的分组

<img src="https://img-blog.csdnimg.cn/img_convert/16c73f0ccbac70324b5c5a26f21a6ad4.jpeg" alt="">

高级交互表。

通过灵活变动数据源，即可实现数据联动，实现其他数据的自动变动，图表自动更新。

如果你使用了数据透视表，数据透视表的入切片器、动态透视图、日程等功能，

通过使用数据透视表，您可以轻松地插入切片器、动态透视、时间表等,创造动态效果

<img src="https://img-blog.csdnimg.cn/img_convert/e9c3b9a49ac191bd6b05492645780622.jpeg" alt="">

#### Excel数据分析的缺点

**跨平台能力差**

Excel目前只能在主流的PC系统，也就是在Windows和Mac平台上运行

但是目前很多大数据企业使用的是Linux系统。这就导致excel跨平台的缺点暴露了。

**能处理的数据量有限**

这一点我们应该能体会到。只要excel的数据超过10万行，几乎动都动不了，像计算，查询和透视功能，想都不要想。这让需要面临大量数据的exceller十分尴尬

所以我们需要使用数据库产品，因为数据库产品的存储容量更大，可以让我们存储更多的数据和信息。

其实excel即便有各种各样的问题，但是依然是数据分析人，最应该熟练掌握的技能。

**然而也有不少小白连excel都用不好，更是无法用excel来进行数据分析了。**

对于excel初学者来说，如果想系统的学习Excel，可以看一系列的课程，系统的学习EXCEL，这样可以学的更快。

对于新手，我的建议是跟一个老师学，最好是既有长期教学经验又有牛逼工作经验的老师，这样才能保证自己真的是实战数据分析的大腕，真的能教到别人。少了一个，要么被人教成书呆子，要么大肚茶壶倒饺子——有货就说不清了。

### 二、Python数据分析

如果用python进行数据分析，还是有很多好处的

#### 简单易学

Python是非常简答的语法，和java不同，即便这个人没有变成基础，也可以很快掌握python。

最大的优点就是简单易学。

很多学过Java的朋友都知道，Python语法简单很多，代码非常好读写，最适合初学者学习。

如果你有编程基础，那么半天就能掌握所有python所有语法。因此很多人开发人员把python作为自己的第二编程语言

比如一个Hello World，Python只需要一个print(“Hello World”)。

当然了，python有一些常用类库，这些类库是需要花时间学习的，比如**Numpy、Pandas，这个是需要系统的学习和练习。**

#### 办公自动化

我们经常说 python 爬虫，因为python这个工具确实可以提高工作效率，主要用来自动抓取数据、抓取关键词、数据分析、自动下载等工作。

我们还可以用python批量读写CSV文件

代码如下

```
普通方法读取：

with open("fileName.csv") as file:

for line in file:

print line

用CSV标准库读取：

import csv

csv_reader = csv.reader(open("fileName.csv"))

for row in csv_reader:

print row

用pandas读取：

import pandas as pd

data = pd.read_csv("fileName.csv")

print data

data = pd.read_table("fileName.csv",sep=",")

print data

```

我们如果想要批量读写excel文件。也可以用python操作

<img src="https://img-blog.csdnimg.cn/img_convert/288d7f50be3ff7c82e6ee93834309e11.jpeg" alt="">

在写完脚本之后如果下次遇到其他类似场景，也可以使用Python脚本进行处理。

#### 制作数据报告

有些数据需求，我们需要定期更新，比如前一周销售额，前一周的成本，前一周的顾客数，前一周的roi等等各种原始数据，如果每次重新统计，并且制作出数据报告是非常麻烦的。

这种重复性的工作，就需要python来进行了，如果是用Excel的话，就还是比较低效的。

```
if __name__ == '__main__':  
    # 创建内容对应的空列表  
    content = list()  
    
    # 添加标题   
    content.append(Graphs.draw_title('数据分析就业薪资'))   
    
    # 添加图片   
    content.append(Graphs.draw_img('资料全集.jpg'))  
    
    # 添加段落文字  
    content.append(Graphs.draw_text('众所周知，大数据分析师岗位是香饽饽，近几年数据分析热席卷了整个互联网行业，与数据分析的相关的岗位招聘、培训数不胜数。很多人前赴后继，想要参与到这波红利当中。那么数据分析师就业前景到底怎么样呢？需要学习Python + 大数据分析，可以添加我：CoderWanFeng'))   
    
    # 添加小标题  
    content.append(Graphs.draw_title(''))  
    content.append(Graphs.draw_little_title('全网同名：程序员晚枫'))   
    
    # 添加表格   
    data = [    
        ('平台名称', '关注人数', '较上年增长率'),    
        ('公众号', '18.5K', '25%'),     
        ('B站', '25.5K', '14%'),    
        ('微博', '29.3K', '10%') 
    ]  
    content.append(Graphs.draw_table(*data)) 
    
    # 生成图表  
    content.append(Graphs.draw_title(''))  
    content.append(Graphs.draw_little_title('热门城市的就业情况'))  
    b_data = [(25400, 12900, 20100, 20300, 20300, 17400), (15800, 9700, 12982, 9283, 13900, 7623)]  
    ax_data = ['BeiJing', 'ChengDu', 'ShenZhen', 'ShangHai', 'HangZhou', 'NanJing'] 
    leg_items = [(colors.red, '平均薪资'), (colors.green, '招聘量')]   
    content.append(Graphs.draw_bar(b_data, ax_data, leg_items))  
    
    # 生成pdf文件   
    doc = SimpleDocTemplate('report.pdf', pagesize=letter)  
    doc.build(content)

```

对函数进行封装，然后每次只需要修改数据路径，就能满足我们的数据报告需求了

#### 丰富的第三方库

Python 的标准库是随着 Pyhon 安装的时候默认自带的库，提供了有文本处理、系统管理、网络处理等功能。Python 的第三方库，是由各家厂商和 Python 爱好者开发的库，这些库包含多种功能，能够节省大量重复造轮子的时间，节约了使用者的生命

我们一般使用pip 来对Python 包的查找、下载、安装、卸载。

这个pip 其实就是 Python 包管理工具。

我们会用 pip install package-name 命令来安装库

下面是几个常用的模块

<img src="https://img-blog.csdnimg.cn/img_convert/b4db921ec705e577db25714469ea20ad.jpeg" alt="">

我简单介绍几个模块

#### numpy 模块

这个模块支持对数组和矩阵进行运算，它包含了大量的数学函数库。作为一个运算速度非常快的数学库，他的功能包括，但不限于
- 一个强大的 N 维数组对象 ndarray- 统计函数- 线性代数、傅里叶变换、随机数生成- 矩阵运算
<img src="https://img-blog.csdnimg.cn/img_convert/99c368ec5040395a239b75d2a972ba4c.jpeg" alt="">

#### pygame 模块

如果你喜欢打游戏的话，这个模块你一定喜欢。

这是一组用来开发游戏软件的 Python 程序模块，基于 SDL 库的基础上开发。

你可以通过pygame创建丰富多彩的游戏。

下面这个就是用pygame开发出的小游戏。你一看就非常熟悉是不是？

<img src="https://img-blog.csdnimg.cn/img_convert/e3fd9b8f98d8dde22b2078e614983bfe.png" alt="">

### pymysql 模块

看这个写法就知道，这是一个mysql 数据库的功能呢

你可以通过这个模块实现与数据库的连接

还可以执行SQL 语句，获得数据

下面这个案例是查询 sql 数据库中的 users表的案例

```
import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="", db='QA')
cursor = conn.cursor()

cursor.execute("SELECT userId,password FROM users");
rows = cursor.fetchall()
for row in rows:
    print(row[0], row[1])

cursor.close()
conn.close()

```

conn = pymysql.connect(host=“localhost”, user=“root”, passwd=“”, db=‘QA’) 成功连接数据库

然后用cursor.execute(“SELECT userId,password FROM users”) 执行sql的SELECT查询语句

最后用fetchall()返回sql的查询结果。

### 三、学习方法

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以找到适合自己的学习方案 


包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习等习教程。带你从零基础系统性的学好Python！

## 零基础Python学习资源介绍

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。**（全套教程文末领取哈）** <img src="https://img-blog.csdnimg.cn/img_convert/673b13641cf2ddf5e18b5c58afd50200.png#pic_center" alt="">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉实战案例👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。 <img src="https://img-blog.csdnimg.cn/68b02d39486d4e4c96b6cb9da7dd54de.png#pic_center" alt="在这里插入图片描述">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

###### 这份完整版的Python全套学习资料已经上传CSDN，朋友们如果需要可以微信扫描下方CSDN官方认证二维码免费领取【`保证100%免费`】

<img src="https://img-blog.csdnimg.cn/1d2a69f2d57e4d1cb444037b17af8607.png" alt="">
