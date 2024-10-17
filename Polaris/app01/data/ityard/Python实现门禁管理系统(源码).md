
--- 
title:  Python实现门禁管理系统(源码) 
tags: []
categories: [] 

---
### **项目介绍**

基于人脸识别的门禁管理系统

(Python+Django+RESTframework+JsonWebToken+Redis+Dlib)

该项目为宿舍门禁系统管理，并额外加入宿舍管理、水电费管理、在线充值、报修管理、系统日志等多项功能，详细见下方截图等。

Django为后端、H5/CSS/JS为前端、MySQL为后端数据库、Redis为缓存、Dlib为人脸识别程序库。

该项目可作为个人学校毕业设计使用，未考虑生产环境，后续开发随心。

### 

### **食用方法**

1、首先下载项目源码文件（获取方法在本文结尾处）

2、运行MySQL和Redis，并在setting.py文件中配置数据库链接信息。
- MySQL数据库使用5.7.27开发，建议使用相同版本(应该mysqlclient有向上兼容- 项目自带Windows系统调试用Redis-x64-3.2.100，默认监听127.0.0.1，6379端口，requirepass为Qq111111
3、修改setting.py文件，进行下一步配置。
- SMTP(邮箱SMTP功能，用于账户登录提示、邮箱发送验证码等功能)- ALiCloud_AFS(阿里云AFS人机验证，用于前端登录滑动验证)- CodePay(码支付，用户水电费充值时的在线支付)- QQConnect(QQ互联，用于前端QQ登录绑定)
4、生成数据表(像运行正常的Django项目一样使用指令)

```
python manage.py makemigrations
python manage.py migrate
```

5、导入初始系统设置数据

数据文件位置：/数据库/system_setting_systemsetting.sql

6、启动项目(像运行正常的Django项目一样使用指令)

```
python manage.py runserver 127.0.0.1:8080
```

### **系统运行截图**

##### **1. 前端-后台[ PC端 ]**

##### 

##### **2. 前端-前台[ 移动端 ]**

##### 3. 前端-摄像头端

### 

### **源码文件获取**

公众号**Python小二**后台回复**门禁管理**获取

推荐阅读  点击标题可跳转
- - - - - - - - 