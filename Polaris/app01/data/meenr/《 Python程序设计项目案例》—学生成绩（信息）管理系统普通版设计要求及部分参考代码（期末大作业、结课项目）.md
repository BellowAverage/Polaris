
--- 
title:  《 Python程序设计项目案例》—学生成绩（信息）管理系统普通版设计要求及部分参考代码（期末大作业、结课项目） 
tags: []
categories: [] 

---
 https://blog.csdn.net/meenr/article/details/107141477



#### 目录
- - - <ul><li>- - - - - - - - 


## 概述

**本文代码系原创，仅供学习参考使用。若转载与引用请标注出处申明。** 本文介绍的内容是，利用python语言，设计一个学生信息成绩管理系统。

<mark>该版本是普通版，升级版请阅读：</mark> https://blog.csdn.net/meenr/article/details/122141262

## 效果演示

### 演示视频链接：

<mark>普通版：</mark>  

<mark>升级版：</mark>  

### 普通版界面截图

第一级菜单 <img src="https://img-blog.csdnimg.cn/20200712200812263.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_30,color_000FFF,t_70#pic_center" alt="选择1" width="400" height="200">

登录 <img src="https://img-blog.csdnimg.cn/2020071220083912.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="登录" width="400" height="200"> 二级菜单 <img src="https://img-blog.csdnimg.cn/20200712200928697.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_30,color_000FFF,t_70#pic_center" alt="选择2" width="400" height="200"> 统计个人输出 <img src="https://img-blog.csdnimg.cn/20200712201203806.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_30,color_000FFF,t_70#pic_center" alt="在这里插入图片描述" width="400" height="400">

## 总体要求

Python的初学者们需要灵活应用所学Python基础知识编写一个成绩管理系统，实现用户能够注册、登录，登录成功可以进行个人成绩查询，统计个人成绩，统计总评成绩等功能。

## 具体要求
1.  界面采用交互式菜单方式，一级菜单包括：注册、登录、退出。 二级菜单包括：查询个人成绩、统计个人成绩、统计总评成绩、退出成绩系统等功能。 1.  用户注册模块：实现用户的注册。用户键盘输入注册信息（用户名、密码），并用xxx.txt文本文件的方式保存。 1.  用户登录模块：实现用户名和密码的校验。用户键盘输入用户名和密码，读取用户注册文件xxx.txt中的信息进行校验，一致则显示登录成功。否则判断用户可输入用户名和密码的次数大于N(N&gt;=3)没，如果超出输入次数，显示登录失败，且等待一段时间后才可以重新输入。 1.  成绩信息建立模块：要求程序代码中直接输入本人真实信息（姓名、学号、电话、各科成绩），N名同学的真实信息（姓名、学号、电话、各科成绩）（N&gt;=6），并用字典或列表等数据类型存放。再将这些信息写入到xxx.CSV文件中长久保存。 1.  查询个人成绩模块：要求用户从键盘输入查询的姓名或学号，读取xxx.CSV文件并返回指定姓名或学号的各科成绩信息。 1.  统计个人成绩模块：要求用户从键盘输入查询的姓名或学号，读取xxx.CSV文件并返回指定姓名或学号的成绩总分和平均分等。 1.  统计总评成绩模块：读取***.CSV文件并返回所有同学的科目成绩和总分，并按总分由高到低排名。 1.  各功能模块用函数实现，主程序调用各功能模块。 1.  代码中必须涉及定义字符串、定义列表、定义字典、数据类型之间的转换、列表操作、字典操作、if语句、for循环、while循环、文件（txt、csv）操作的相关代码。 1.  用户从键盘输入不符合要求的数据用异常来捕获。 1.  可扩充以上基本功能。 
## 分析要求

　　该系统主要考察Python初学者们对基础的python知识的应用能力。 从要求可以知道需要用到的的Python知识点对初学者来说还算全面与综合，主要用到的Python知识点有：

### easygui库

 　　用使用easygui库设计一二级菜单，包括出注册、登录、查询界面。 buttonbox：设计多按钮选择界面 multpasswordbox：设计用户登录和注册界面的账号密码输入 msgbox：登陆成功与错误超过三次信息提示对话框 textbox：成绩信息显示的文本框

### 基本数据类型

 用到的基本数据类型： 字符串、列表、字典

### 基本逻辑顺序

 常用的逻辑循环与判断语句： while循环、for循环 if判断、if…else判断、if…elif…else判断 　　以及上述这些语句的组合都是在GUI设计时常用到的，以满足GUI一级、二级菜单为用户提供的选择功能。判断若输入密码错误三次后将触发延时函数，等待一段时间后重新输入密码。

### pandas库

 对原始数据进行预处理方便后续使用。 将字典转为DataFrame类型，然后进行增删改查与行列变换等操作，再将处理好的数据写入到本地文件中。

### TXT文件和CSV或Excel文件的读写

 TXT文件主要用于保存用户的账号与密码。CSV或Excel文件用来作为保存与处理后的学生成绩信息表格。

## 代码结构

本文提供的代码主要分为四大部分：
1. 设计GUI注册登录界面1. 成绩信息CSV文件读写操作1. 设计GUI查询界面1. 主程序
　　上述四个部分代码写在三个文件中由对应的四个函数组成。 查询函数调用了登录和写入CSV文件函数，那么在主程序中调用查询函数即可。 但是实际上成绩写入程序只需执行一次即可，它生成的CSV文件已经保存在本地文件夹中了。同时将登录界面的函数与查询界面的函数写在了一个GUI的.py文件中。而用户若要手动输入学生的成绩信息，可以在CSV文件中输入。pycharm工程文件目录见下图： <img src="https://img-blog.csdnimg.cn/20200712164631980.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_30,color_000FFF,t_70#pic_center" alt="文件目录" width="400" height="300">

## 示例代码

GUI查询界面的代码如下：

```
def Find():
 
    if Login():
        while True:
            choose2 = g.buttonbox(msg="已进入学生成绩管理系统,请选择",
                                  title="学生成绩管理系统",
                                  choices=("查询个人", "统计个人","统计总评", "退出"))
            if choose2 == "查询个人":
                data1 = read_csv('学生信息成绩表.csv')
                name_num = g.enterbox(msg='输入学生姓名或学号', title='查询个人成绩')
      
                    elif match:
                        name = name_num
                        result1 = data1.loc[data1['姓名'] == name]
 
                text1 = str(result1)
                g.textbox(msg='学生信息成绩如下：', title='学生成绩信息', text=text1, codebox=1)
           
            elif choose2 == "统计个人":
                data2 = read_csv('学生信息成绩表.csv')
                name_num = g.enterbox(msg='输入学生姓名或学号', title='统计个人成绩')
                zhmodel = re.compile(u'[\u4e00-\u9fa5]')
                match = zhmodel.search(name_num)
                if name_num.isdigit() or match:
                    total = 0
            else:
  


```

## 直接获取.py源文件

因为源代码太多，篇幅的限制，这里不再赘述，读者如要需要全部参考代码可通过下面两种途径获取。 **优先推荐途径一，若遇途径一失效，请再尝试途径二。** **2贰进制–Echo 2020年6月** 如果您已阅读至此，请点赞＋评论＋收藏，要是关注那更是对我极大地支持了，您的支持便是我前进的动力！ 如果本文对你有所帮助，解决了您的困扰，那就请我吃包辣条吧： <img src="https://img-blog.csdnimg.cn/20210424133535613.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="400" height="200">

### 途径一

**优先推荐该途径** 第一步：扫描下方二维码，或打开微信搜索并关注“ **2贰进制** ”公众号； 第二步：回复:“ **python学生管理** ”即可获取。 <img src="https://img-blog.csdnimg.cn/2020070300554991.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="二维码" width="250" height="250">

### 途径二

**优先推荐途径一，该途径管理可能不能秒回** 扫描下方二维码，加入学习交流QQ群“ **480558240** ”，联系管理员获取包括但不限于本篇内容的更多学习资料。 <img src="https://img-blog.csdnimg.cn/2020071217121655.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="300" height="300">

此致 感谢您的阅读、点赞、评论、收藏与打赏。
