
--- 
title:  Python课程设计：学生成绩管理系统（附源代码） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/43a720a2f2235d860c6064232d5121f6.png">

版权声明：本文为CSDN博主「大格子嘞」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。原文链接：

https://blog.csdn.net/qq_43971504/article/details/107048678

##### 

##### 

##### 1、需求分析
1. 通过类的知识实现学生成绩信息（学号、姓名、院系、三门课成绩、考试平均成绩、同学互评分、任课教师评分、综合测评总分，其中综合测评总分由：考试平均成绩70%，同学互评分10%，任课教师评分20% ）；1. 能够实现学生成绩信息的保存和读取（使用数据库对数据进行存取）；1. 实现所有相关信息的输入、输出、查找、删除、修改等功能；1. 系统界面应至少实现控制台界面（使用桌面窗体界面进行交互）；1. 通过xlrd和xlwt模块读取和写入Excel文件；
##### 2、功能设计与分析

###### 1、使用数据库对数据进行存取

###### （1）使用PyMySQL模块操作数据库对数据进行存取

先安装PyMySQL模块：`pip install PyMySQL`，再使用时直接导入即可：`import pymysql`；

###### （2）创建数据库school，创建数据表student_sore、teacher_login

可以使用Navicat for MySQL创建，也可以使用预处理语句创建表，若不存在则创建，若存在则跳过；<img src="https://img-blog.csdnimg.cn/img_convert/2a099f40a6128b258c14d00cd00d0a17.png">

###### （3）使用xlrd模块从Excel文件中读取数据到数据库

先安装xlrd模块：`pip install xlrd`，再使用时直接导入即可：`import xlrd`；打开一个Excel文件，通过sheet的索引获取sheet表，循环获取每个单元格的值，一行一行读取到数据库表中。<img src="https://img-blog.csdnimg.cn/img_convert/d78439debcb1198d2bb68063e432fdff.png"><img src="https://img-blog.csdnimg.cn/img_convert/934f224aa6e7722cd0118afe40833174.png">

###### （4）定义一个PyMySQL增删改查的工具类PyMySQLUtils
- 1）`def __init__(self)` 获取连接：打开数据库的连接，使用cursor()方法获取操作游标；<img src="https://img-blog.csdnimg.cn/img_convert/eda3c593602caff7708e1da41b7c6b99.png">- 2）`def fetchall(self, sql)` 查询获取多条数据：使用execute()方法执行SQL语句，使用fetchall()方法获取多条数据；<img src="https://img-blog.csdnimg.cn/img_convert/ea7a3abb360f6a11f3a1603b17be7fdf.png">- 3）`def fetchone(self, sql)` 查询获取单条数据：使用execute()方法执行SQL语句，使用fetchone()方法获取单条数据；<img src="https://img-blog.csdnimg.cn/img_convert/43e8343d0d399e512fef0016f1f4f5aa.png">- 4）`def execute(self, sql)` 添加删除更新操作：使用execute()方法执行SQL语句，提交到数据库执行，发生错误时回滚；<img src="https://img-blog.csdnimg.cn/img_convert/7c0a1a6f79eb36bbab289cc4d47705d9.png">- 5）`def close(self)` 关闭连接：关闭游标，关闭数据库连接；<img src="https://img-blog.csdnimg.cn/img_convert/563c2549dd1f21cda846c4b03ea5d453.png">
###### 2、使用桌面窗体界面进行交互

###### （1）使用Tkinter模块实现图形化界面GUI设计

使用时直接导入即可：

```
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import tkinter.messagebox as messagebox

```

###### （2）开始界面：教师注册、教师登录、退出系统

class StartMenu：（销毁上一个窗口）初始化一个根窗口window；添加Label标签控件，用于单行文本显示"学生成绩管理系统"；添加三个Button按钮控件，将其分别与关联函数lambda: TeacherRegister、lambda: TeacherLogin、window.destroy绑定；在主事件循环中等待用户触发事件响应。

###### （3）教师注册界面：输入账号、输入密码、确认账号、确定、返回

class TeacherRegister：（销毁上一个窗口）初始化一个根窗口window；添加Label标签控件，用于单行文本显示"教师注册页面"，“输入账号”、“输入密码”、“确认账号”；添加三个Entry输入控件，用于显示用户输入文本，添加两个Button按钮控件，将其分别与关联函数register、back绑定；在主事件循环中等待用户触发事件响应。<img src="https://img-blog.csdnimg.cn/img_convert/8d09343adfe3594b615c710e3fbcbb7b.png">

###### （4）教师登录界面：账号、密码、确定、返回

class TeacherLogin：（销毁上一个窗口）初始化一个根窗口window；添加两个Entry输入控件，用于显示用户输入文本，添加两个Button按钮控件，将其分别与关联函数login、back绑定；在主事件循环中等待用户触发事件响应。<img src="https://img-blog.csdnimg.cn/img_convert/954146ed8e7cb5583323843e0fb0829a.png">

###### （5）教师操作界面：添加、修改、查询、删除

class TeacherMenu：（销毁上一个窗口）初始化一个根窗口window；添加三个Frame框架控件，用于框架分组self.frame_center、self.frame_left、frame_right；在中心区域添加ttk.Treeview树视图窗口控件，ttk.Scrollbar 滚动条控件，设置列、表头，定义储存数据的列表，从数据库获取表格内容，设置表格内容，给表头绑定函数tree_sort_column，点击可排序，给表格绑定点击事件tree_click，获取被点击的条目；在左方区域添加八个Label标签控件，用于单行文本显示；添加八个Entry输入控件，用于显示用户输入文本，添加六个Button按钮控件，将其分别与关联函数绑定；在主事件循环中等待用户触发事件响应。<img src="https://img-blog.csdnimg.cn/img_convert/84880b9d337e0658e407ab2acf93942f.png"><img src="https://img-blog.csdnimg.cn/img_convert/deaf6cf7339978f8b8ddd7170c41894a.png">

###### 3、实现所有相关信息的添加、修改、查询、删除等功能

###### （1）添加学生成绩信息

insert：判断输入框中的学号在不在储存学号的列表中，在则警告"该学生成绩信息已存在！"；不在则先添加输入框中的数据到数据库中，接着添加到储存储存数据的列表中，最后添加到表格内容中。<img src="https://img-blog.csdnimg.cn/img_convert/efad1b6692a56080261b85dfe1ee46c9.png">

###### （2）修改学生成绩信息

update：判断输入框中的学号在不在储存学号的列表中，不在则警告"该学生成绩信息不存在！"；在则先根据输入框中的学号修改数据库中的数据，接着根据输入框中的学号在储存学号列表的索引删除储存数据的列表中的数据，最后删除表格内容中的数据。<img src="https://img-blog.csdnimg.cn/img_convert/1c83621789399cd4a67942e564528ef7.png">

###### （3）查询学生成绩信息

select：判断输入框中的学号在不在储存学号的列表中，不在则警告"该学生成绩信息不存在！"；在则根据输入框中的学号在储存学号列表的索引直接查询储存数据的列表中的数据，把数据设置到输入框中。<img src="https://img-blog.csdnimg.cn/img_convert/cabf56ff8f1093554892f473639b27dc.png">

###### （4）删除学生成绩信息

delete：判断输入框中的学号在不在储存学号的列表中，不在则警告"该学生成绩信息不存在！"；在则先根据输入框中的学号删除数据库中的数据，接着根据输入框中的学号在储存学号列表的索引删除储存数据的列表中的数据，最后删除表格内容中的数据。<img src="https://img-blog.csdnimg.cn/img_convert/ddb2585696bcc7490f28c3a3562b0527.png">

###### （5）清空输入框的内容

clear：通过StringVar.set()方法直接把输入框的内容设置为空。<img src="https://img-blog.csdnimg.cn/img_convert/0adb31e94d263379535991f0476175ad.png">

###### （6）写入到Excel文件

先安装xlwt模块：`pip install xlwt`，再使用时直接导入即可：`import xlwt`；新建一个Excel文件，添加一个名为sheet1的表，设置允许重写覆盖，从数据库中获取数据，循环向sheet写入数据，最后保存文件中。<img src="https://img-blog.csdnimg.cn/img_convert/5dc9e020b37038519e9cf0d388854746.png"><img src="https://img-blog.csdnimg.cn/img_convert/fcd91d753aeacca7b17d88ed4c5c58dd.png">

##### 3、总结与体会

##### 4、运行结果

###### （1）开始界面

<img src="https://img-blog.csdnimg.cn/img_convert/1d03d4d57fd362b1038672f84772eb92.png">

###### （2）教师注册界面

<img src="https://img-blog.csdnimg.cn/img_convert/c35a2c58ba8bfe7dd50dd95ecd8b9a1b.png"><img src="https://img-blog.csdnimg.cn/img_convert/39e51e0f97fa51d3e0776b99fc24a0f1.png">

###### （3）教师登录界面

<img src="https://img-blog.csdnimg.cn/img_convert/ad9a592107bc8be59aeeb42e36ad0c5d.png"><img src="https://img-blog.csdnimg.cn/img_convert/9ef0b93bbe9fa4ec2f6dda46d6fd2189.png">

###### （4）教师操作界面

###### 1）添加学生成绩信息

<img src="https://img-blog.csdnimg.cn/img_convert/9ee364e1400e8b2cccbd2d1b0dec2163.png"><img src="https://img-blog.csdnimg.cn/img_convert/58a6561979aef9dd8f2d97b727e1040e.png">

###### 2）修改学生成绩信息

<img src="https://img-blog.csdnimg.cn/img_convert/15483843b0b178bfb442039ee5c74135.png"><img src="https://img-blog.csdnimg.cn/img_convert/725c1636706220b959541b5e460cb424.png">

###### 3）查询学生成绩信息

<img src="https://img-blog.csdnimg.cn/img_convert/cf728bece54f4064c0c10b68b3b8ccbc.png"><img src="https://img-blog.csdnimg.cn/img_convert/06a4ac8f2f32c14aceec59e1f22facff.png">

###### 4）删除学生成绩信息

<img src="https://img-blog.csdnimg.cn/img_convert/d651a8dbbdd6ce2d38f553a442bfa381.png"><img src="https://img-blog.csdnimg.cn/img_convert/55f7e2cbacd0da710641bbf727f15cc0.png">

###### 5）学生成绩信息排序

<img src="https://img-blog.csdnimg.cn/img_convert/33853562ac6080a57c325e4abfd9c1d7.png"><img src="https://img-blog.csdnimg.cn/img_convert/3670c41fa49986feade898d4fe9e6716.png">

###### 6）写入到Excel文件

<img src="https://img-blog.csdnimg.cn/img_convert/4616e0bd9c74ecda90d5621516494540.png"><img src="https://img-blog.csdnimg.cn/img_convert/88ce29ad0583ecfb36ebbeee8931eed3.png"><img src="https://img-blog.csdnimg.cn/img_convert/2a1ff86780dc320fdd3e8290fb06dd01.png">**在公众号Python小二后台回复成绩获取源代码+Excel文件+报告。**

**道友路过给个赞吧**~
