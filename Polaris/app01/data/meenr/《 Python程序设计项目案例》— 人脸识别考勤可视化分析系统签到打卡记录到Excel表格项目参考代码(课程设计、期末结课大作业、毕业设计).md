
--- 
title:  《 Python程序设计项目案例》— 人脸识别考勤可视化分析系统签到打卡记录到Excel表格项目参考代码(课程设计、期末结课大作业、毕业设计) 
tags: []
categories: [] 

---
 https://blog.csdn.net/meenr/article/details/107348867

## Python课程设计（程序设计大作业）项目

### 最新版本更新

程序优化整合，未完待续，敬请期待～～～

## 基于Python人脸识别自动考勤可视化分析签到系统



#### 目录
- - <ul><li>- - <ul><li>- - - - - - - <ul><li>- - - - - 


### 1 背景及目的

#### 1.1 项目背景和意义

脸识别技术是指利用分析比较的计算机技术识别人脸。人脸识别是一项热门的计算机技术研究领域，其中包括人脸追踪侦测，自动调整影像放大，夜间红外侦测，自动调整曝光强度等技术。人脸识别技术属于生物特征识别技术，是对生物体（一般特指人）本身的生物特征来区分生物体个体。

#### 1.2 项目目的和功能

设计本系统主要目的是为了解决公司部门、学生上课等考勤数据汇总难、不精准、代打卡、特殊工时难以有效管理等问题。因此主要功能应该具备以下几点：

（1）对面部照片的采集以提供学习训练的数据资源；

（2）通过对已采集过的人面部的识别来完成签到；

（3）对签到信息进行分析。

### 2 方案设计

#### 2.1 总体目标

总体目标是通过人脸识别的方式完成签到。为了实现和完善这一目标需要其他功能模块的支持。为此，设计的系统共有三个子程序，前期需要执行第一个子程序来采集面部照片，供作学习训练；中期需要利用前期获得的数据资源做出人脸识别完成签到；后期需要对中期记录的签到数据做可视化分析。

#### 2.2 总体方案

通过对第一个子程序的功能要求分析，该部分需要拥有一个账号密码的登录界面保证数据安全，那么登录的窗体设计需要调用easygui库及相应的方法和函数。

而对于第二个主要功能实现的程序首先还是需要调用opencv库来检测人脸。

最后一部分是对签到信息做可视化分析，首先需要输入分析哪一天的签到信息

该项目主要完成GUI登录界面、人的面部信息采集、人脸识别签到以及数据可视化分析等功能，通过对本系统基本功能要求的分析，方案设计中应用的python集成的或第三方库及模块有较多。

#### 2.3 各组成部分的功能

三个子程序的主要功能概述如下：

第一个子程序运行后，在显示器上会有登录的提示框弹出，根据提示输入正确的用户名和密码后登录使用系统，接着通过键盘输入被采集人的姓名，然后开始采集，通过调用摄像头拍摄30张面部照片并保存到本地。

第二个子程序是项目的核心，主要功能和价值体现的地方。该子程序应该具有这些功能要求，先要对采集的照片进行学习训练，而后调用摄像头开始识别人脸。另外，会获取被识别的时间，用来判断是否迟到，并将姓名、签到时间、备注的迟到与否信息写入到一个通过获取系统日期每天创建一个以当天日期作为文件名Excel表格中。

第三个子程序是对签到记录的Excel表格数据进行分析的。最后根据这一人数画出饼状图，并将绘制的饼状图保存到本地。

### 3 程序编写及实现

#### 3.1 编程环境

Windows10 系统，python3.7环境以及所需的第三方包

#### 3.2 程序设计与功能实现

三个功能模块，具体设计以及功能实现如下：

##### 3.2.1 人脸采集

**（1）流程及操作步骤说明**

这部分程序运行后根据弹出的窗体提示信息进行相应的鼠标点击或者键盘输入操作。

a. 首先是欢迎界面和有提示将要采集30张面部照片的信息，点击“Go to”继续下一个——选择界面.

b. 选择界面是选择登陆还是修改用户名和密码。若选择登陆则点击“login”，若选择修改用户名及密码则点击 “change password”

c. 接着是登录界面，需要输入用户名“username”和密码“password”，然后点击“OK”若有错误则重新输入，若累计错误三次则等待三分钟后重新输入（程序实际是等待5秒钟）；若用户名和密码正确，点击“OK”则提示登陆成功，点击OK“”进入下一个界面，输入被采集人的姓名，点击“OK”，提示即将开始拍摄，请面向镜头等信息。点击“OK”，开始调用摄像头采集面部照片，采集时在终端会打印采集多少张面部照片了，到30张时自动停止采集，提示采集完毕等信息，“点击OK”退出程序。

d. 选择修改用户名及密码，需输入原用户名及原密码来验证身份，错误则程序退出，正确则进入下一个界面，输入新的用户名及密码，点击“OK”，提示修改成功，退出重新登录。

**（2）程序代码及注释**

```
def gui():
  global anser
  if anser == "login":
	msg = "Please enter username and password"
    title = "Administrator"
    user_list = GUI.multpasswordbox(msg, title, ("username", "password"))
    file = open("user.txt")
      GUI.msgbox("Account or password error, please try again!")
      return False
    if name == user_list[0] and password == user_list[1]:
      msg = "Please enter your username and password"
      title = "New username/password"
      file = open("user.txt", "w", 1)
      file.write(re_list[0] + '\n')
      file.write(re_list[1])
      file.close()
      GUI.msgbox('Change successful!Please login again!')
      exit(0)
      pass
    pass
  else:
  	exit(0)
    pass
  pass


```

**（3）运行结果及分析**

首先弹出欢迎界面，由一张图片和文本构成。点击“Go to”，继续运行。欢迎界面如图2所示： <img src="https://img-blog.csdnimg.cn/20210112173947341.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="450" height="300">

图2 欢迎界面

欢迎界面的下一个界面——选择界面如图3所示，由一张图片、提示信息和提供选择的两个按钮构成。

<img src="https://img-blog.csdnimg.cn/20210112174037218.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="450" height="300">

图3 选择界面

若选择登录即点击“login”则进入登陆输入界面，如图4所示。

<img src="https://img-blog.csdnimg.cn/20210112174043110.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="500" height="250">

图4 登录输入界面

若选择修改密码，运行结果图见附图1，需输入原用户名和原密码，其他修改成功后返回重新登录。修改密码若出错，会直接停止程序。

##### 3.2.2 人脸识别签到

**（1）流程及操作步骤说明**

运行程序，完成学习构建模型后，则可以开始识别并进行签到。由于程序中有while死循环，所以程序会一直运行。

**（2）程序代码及详细注释**

```
def study_face():
  path1 = "collect_photograph/after_processing_photo"
  dirs = os.listdir(path1)
  for j, dir in enumerate(dirs):
​    for i in range(30):
​      gray = cv2.cvtColor(img, code=cv2.COLOR_RGB2GRAY)
​      X.append(gray)
​    pass
  return [X, Y, dirs]
  pass



```

**（3）运行结果及分析**

每天创建一个Excel表格，表格名称是当天日期，如图5所示。 <img src="https://img-blog.csdnimg.cn/20210112174114870.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="600" height="250">

图5 每天的签到记录文件

只要识别到人脸就会在当日的Excel表格中存入签到时间、姓名、迟到与否等信息。例如2019年11月20日签到记录，记录在Excel表格信息如图6所示。

<img src="https://img-blog.csdnimg.cn/20210112210033390.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="600" height="250"> 图6 Excel中的签到记录

##### 3.2.3 可视化数据分析

**（1）流程及操作步骤说明**

程序运行后，弹出输入界面，根据提示信息输入要分析哪一天的签到数据（注意日期格式）。如图7所示，随后弹出迟到与未迟到的人数（见附图8），并将绘制的饼状图（见附图9）以.jpg格式保存到与Excel文件同名同路径的文件夹中（见附图10）。

**（2）程序代码及详细注释**

```

def get_data():
  date_date = GUI.enterbox(msg="Please enter the date of drawing(format: 2019-11-11):",
​               title='Facial acquisition') 
  file_path = "s.xlsx" % date_date 
  note_content = []
  a = 0
  b = 0
​    note_content.append(x[0]) 


```

**（3）运行结果及分析**

运行后弹出了需要输入的窗体（见图7），根据提示信息，按照格式要求，输入要分析那一天的日期。

<img src="https://img-blog.csdnimg.cn/20210112174137628.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="500" height="250">

图7 输入分析日期界面

完成输入后，点击“OK”，结果将显示在显示器上，如图8所示。弹出统计迟到和未迟到人数的一个窗体。在开发软件中将显示出绘制的图形。另外在与Excel同文件夹下将保存绘制图形的.jpg格式（见附图10）。

<img src="https://img-blog.csdnimg.cn/20210112174145591.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="500" height="250"> 图8 分析结果截图

##### 3.2.4 整体性能测试

三个程序全部设计调试完后，开始依次执行。对于没有被采集过面部照片的人，是必须先执行第一个面部照片采集程序，完成采集，以便学习及识别。

### 4 总结

本次的基于python语言的人脸识别考勤系统程序设计，通过设计三个程序分别完成一部分功能，最终总体上实现了设计目标。

### **<strong><strong>Echo作品**</strong></strong>

### 直接获取.py源文件

读者如要获取全部参考代码可通过下面两种途径获取全部代码的.py文件。

#### 途径1

**优先推荐该途径** 第一步：扫描下方二维码，或vx搜索并关注“ **2贰进制** ”公主号； 第二步：回复:“ **python人脸识别考勤** ”即可获取参考代码。 <img src="https://img-blog.csdnimg.cn/2020070300554991.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="二维码" width="200" height="200">

#### 途径2

扫描下方二维码，加入学习交流Q群“ **480558240** ”，可联系管理员咨询，获取包括但不限于本篇内容的更多学习资料。 <img src="https://img-blog.csdnimg.cn/2020071217121655.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="250" height="250"> **2贰进制–Echo 2019年9月** 如果您觉得本文还不错，请点赞＋评论＋收藏，要是关注那更是对我更大的支持了。如果本文对你有所帮助，解决了您的困扰，可以通过赞赏来给予我更大支持： <img src="https://img-blog.csdnimg.cn/20210424133535613.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="400" height="200"> 此致 感谢您的阅读、点赞、评论、收藏与打赏。

## 附录 运行截图

附图1 修改则需输入原信息 <img src="https://img-blog.csdnimg.cn/20210112174227175.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="500" height="250">

附图2 提示开始采集 <img src="https://img-blog.csdnimg.cn/20210112174239150.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="500" height="250">

附图3 提示用户名或密码错误重试

<img src="https://img-blog.csdnimg.cn/20210112174351148.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="500" height="250">

附图4 提示错误3次3分钟后重试 <img src="https://img-blog.csdnimg.cn/20210112174346789.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="500" height="250">

附图5 打印等待倒计时 <img src="https://img-blog.csdnimg.cn/20210112174341195.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="300" height="200">

附图6 输入被采集人姓名 <img src="https://img-blog.csdnimg.cn/20210112174335701.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="500" height="250">

附图7 提示采集完毕

<img src="https://img-blog.csdnimg.cn/20210112174326953.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="500" height="250">

附图8 迟到/未迟到人数显示

<img src="https://img-blog.csdnimg.cn/20210112174320894.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="500" height="250">

附图9 绘制的图形 <img src="https://img-blog.csdnimg.cn/202101121743168.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="400" height="250">

附图10 签到记录文件夹中文件 <img src="https://img-blog.csdnimg.cn/20210112174303490.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="600" height="250">
