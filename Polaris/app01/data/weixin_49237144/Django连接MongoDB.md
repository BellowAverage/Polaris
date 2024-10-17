
--- 
title:  Django连接MongoDB 
tags: []
categories: [] 

---
Hello小伙伴们，你们好啊~~ 又是日常get新技能的一天， 今天，咱们来整一下如何使用Django连接MongoDB， 0基础入门，趁着热乎，快上车啦~~。



#### 1. 初始环境

django == 3.2.3 mongoengine == 0.23.1

1.1

需要依赖第三方库：pip install mongoengine

1.2

MongoEngine 是一个文档对象映射器（想想 ORM，但用于文档数据库），用于从 Python 处理 MongoDB。

它使用一个简单的声明式 API，类似于 Django ORM。



#### 2.进入Django进行设置



1.在setting.py里设置DATABASES

```
 from mongoengine import connect
 DATABASES = {
     'default': {
         'ENGINE': None, # 把默认的数据库连接至为None
     }
 }
 connect('dj_mon', host='127.0.0.1', port=27017) # 连接的数据库名称dj_mon
```



1.2 配置总路由urls.py

```
 """FirstMongo URL Configuration
 ​
 The `urlpatterns` list routes URLs to views. For more information please see:
     https://docs.djangoproject.com/en/3.2/topics/http/urls/
 Examples:
 Function views
     1. Add an import:  from my_app import views
     2. Add a URL to urlpatterns:  path('', views.home, name='home')
 Class-based views
     1. Add an import:  from other_app.views import Home
     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
 Including another URLconf
     1. Import the include() function: from django.urls import include, path
     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
 """
 from django.contrib import admin
 from django.urls import path, include
 ​
 ​
 urlpatterns = [
     path('admin/', admin.site.urls),
     path('mon/', include('mon.urls')),
 ​
 ]
```



2.进入到项目下创建自己的APP

1.1 python manage.py startapp mon



3.在APP里的urls里配置：urls和视图

```
 from . import views
     urlpatterns = [
     path('Student/', views.get),
 ]
```



4.在APP里的models里配置：新建数据模型

```
 import mongoengine
 ​
 # 类名就是表名，继承基类mongoengine.Document,为普通文档
 class StudentModel(mongoengine.Document):
     name = mongoengine.StringField(max_length=16)
     age = mongoengine.IntField(default=0)
```



5.在APP里的views里配置：创建视图函数

```
 
```

```
import mongoengine
 from django.http import HttpResponse
 from django.shortcuts import render
 from .models import StudentModel
 from django.views.generic import View
 ​
 def get(request):
     #stu = StudentModel()
     #stu.name = '定心'
     #stu.age = 12
     #stu.save()
     if request.method == "GET":
         StudentModel.objects.create(name='定心', age=12)
         return HttpResponse('hello word')
```



6.不用makemigrations和migrate，直接就能用，不过必须要先创建好数据库，并且指定字符集

7.参考文献

MongoEngine官网： [

MongoEngine官网教程：
