
--- 
title:  毕业设计！Python实现学生教师刷脸签到系统 
tags: []
categories: [] 

---
大家好，我是小二，今天分享一个 Python 毕业设计项目：学生教师刷脸签到系统。

**简介**

利用Python语言、Flask框架、Dlib库、MySQL数据库等工具设计并实现一套基于Web端的刷脸签到系统。

学生可以在闲暇时在系统录入人脸，等到上课签到时，只需在网页上刷脸即可完成签到，签到页实时显示签到人信息，整个过程简便流畅。同时，也实现了与考勤相关的一系列功能，满足用户需求。

**实现工具**
- 语言：Python- 工具库：Dlib OpenCV- 框架：Flask Bootstrap- 数据库：MySQL
**数据库设计**

共设计了六张表：
- attendance：学生的考勤情况- course：所有课程信息- student_course：学生选课情况- student_faces:学生的人脸特征- students：所有学生信息- teachers：所有老师信息
**功能介绍**

**教师端**
- 新建课程- 开发或关闭选课- 导入选课记录- 课程刷脸签到- 考勤查询与修改- 考勤导出- 拍照权限设置- 批量导入账号（管理员教师）
**学生端**
- 人脸录入- 选退课- 考勤查询
**其他**
- 用户登录- 登陆时间提醒- 修改密码- 拦截器
<img src="https://img-blog.csdnimg.cn/img_convert/a4f57d8f4fd20f60510d97de911e498c.png" alt="a4f57d8f4fd20f60510d97de911e498c.png">

**总结**

本项目主要采用了Python语言基于Flask框架开发，利用Dlib库中68特征点检测器和深度残差网络模型，欧氏距离，目标跟踪方法实现了人脸识别，采用MySQL数据库记录系统相关数据，并用Bootstrap框架进行页面美化。最后完成的系统可以适用于具有带摄像头的联网设备的教学场所。

**项目源码**

源码已经打包整理好了，有需要的小伙伴可以在下方公众号**Python数据分析之美**后台回复**刷脸签到**直接获取。

**<strong>往期回顾：**</strong>
- - - - - - - - <img src="https://img-blog.csdnimg.cn/img_convert/7cf8f2b92b1cd85b910899d6aa031b57.gif" alt="7cf8f2b92b1cd85b910899d6aa031b57.gif">