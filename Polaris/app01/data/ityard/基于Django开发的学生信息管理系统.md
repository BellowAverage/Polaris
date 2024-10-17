
--- 
title:  基于Django开发的学生信息管理系统 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/695f56cc7c8ee26a940002fbc7f7c082.png">

来源：http://nxw.so/584pM

#### 

#### 一、 功能
1. 实现对学生对个人信息的增删查改1. 实现后台对所有学生信息的操作
#### 二、开发工具

Windows + Pycharm + Mysql + Django

#### 三、代码实现

1. model

```
from django.db import models
 
# Create your models here.
# 课程表
class CourseModel(models.Model):
    cour_id = models.CharField(max_length=15, verbose_name='学生ID')
    course = models.CharField(max_length=30, verbose_name='课程')
    grade = models.IntegerField(default=60, verbose_name='分数')
    class Meta():
        db_table = 'course'
    def __str__(self):
        return '学生Id：课程：分数：'.format(self.cour_id, self.course, self.grade)
 
# 学生信息表
class StudentInformationModel(models.Model):
    stu_id = models.CharField(max_length=15, verbose_name='学生ID')
    stu_name = models.CharField(max_length=30, verbose_name='学生姓名')
    stu_phone = models.CharField(max_length=20, verbose_name='学生电话')
    str_addr = models.TextField(verbose_name='学生地址')
    stu_faculty = models.CharField(max_length=20, verbose_name='院系')
    stu_major = models.CharField(max_length=30, verbose_name='专业')
    # 取消外键（外键是可用的）
    # stu_course = models.ForeignKey('CourseModel', on_delete=True)
    class Meta():
        db_table = 'studentinformation'
 
# 学生用户名密码表
class StudentModel(models.Model):
    stu_id = models.CharField(max_length=15, verbose_name='学生ID')
    username = models.CharField(max_length=10, verbose_name='用户名')
    password = models.CharField(max_length=10, verbose_name='密码')
    class Meta():
        db_table = 'student'

```

2. urls

```
from django.urls import path
from studentManagement import views
 
app_name = 'studentManager'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add/', views.add, name='add'),
    path('select/', views.select, name='select'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update')
]

```

3.  views

```
from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import StudentModel, StudentInformationModel, CourseModel
# Create your views here.
 
# 主界面
def index(request):
    context = {
        'status': '未登录状态'
    }
    return render(request, 'studentManage/index.html', context)
 
# 登录界面
def login(request):
    if request.method == "POST":
        id = request.POST.get('id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not all([id, username, password]):
            return HttpResponse('参数不全')
        else:
            student = StudentModel.objects.filter(username=username, password=password)
            if len(student):
                # request.session['username'] = username
                # 用以下方法，将用户的信息存放到session中，session在中间件中是默认启用的
                request.session['user'] = {
                    'id': id,
                    'username': username,
                    'password': password
                }
                context = {
                    'status': username,
                    'aa': '已登录',
                    'lenght': 1
                }
                return render(request, 'studentManage/index.html', context)
 
            else:
                context = {
                    'aa': '用户名密码错误'
                }
                return render(request, 'studentManage/login.html', context)
    else:
        context = {
            'status': '未登录状态',
            'length': 0
        }
        return render(request, 'studentManage/login.html', context)
 
# 退出界面
def logout(request):
    # 注销掉用户，从删除session中保存的信息
    del request.session['user']
    return render(request, 'studentManage/index.html')
 
# 增加数据 增加只能root用户或者管理员才能操作
def add(request):
    if request.method == "POST":
        root_information = request.session['user']
        id = root_information['id']
        root_id = StudentModel.objects.get(pk=1).stu_id
        if id == root_id:
            stu_id = request.POST.get('stu_id')
            stu_name = request.POST.get('stu_name')
            if not all([stu_id, stu_name]):
                context = {
                    'msg': '学号和名字有遗漏',
                }
                return render(request, 'studentManage/add.html', context)
            stu_phone = request.POST.get('stu_phone')
            stu_addr = request.POST.get('str_addr')
            stu_faculty = request.POST.get('stu_faculty')
            stu_major = request.POST.get('stu_major')
            stu_data = StudentInformationModel()
            stu_data.stu_id = stu_id
            stu_data.stu_name = stu_name
            stu_data.stu_phone = stu_phone
            stu_data.str_addr = stu_addr
            stu_data.stu_faculty = stu_faculty
            stu_data.stu_major = stu_major
            stu_data.save()
            context = {
                'sucess': '增加成功',
            }
            return render(request, 'studentManage/add.html', context)
        else:
            context = {
                'error': '只用root用户和管理员才能操作'
            }
            return render(request, 'studentManage/add.html', context)
    else:
        return render(request, 'studentManage/add.html')
 
 
# 查询
def select(request):
    if request.method == "POST":
        id = request.POST.get('stu_id')
        stu_data = StudentInformationModel.objects.get(stu_id=id)
        stu_id = stu_data.stu_id
        stu_name = stu_data.stu_name
        stu_phone = stu_data.stu_phone
        str_addr = stu_data.str_addr
        stu_faculty = stu_data.stu_faculty
        stu_major = stu_data.stu_major
        stu_course = CourseModel.objects.filter(cour_id=id)
        dct = {}
        for stu in stu_course:
            dct[stu.course] = stu.grade
        context = {
            'stu_id': stu_id,
            'stu_name': stu_name,
            'stu_phone': stu_phone,
            'str_addr': str_addr,
            'stu_faculty': stu_faculty,
            'stu_major': stu_major,
            'course_data': dct,
            'msg': True
        }
        return render(request, 'studentManage/select.html', context)
    else:
        root_information = request.session['user']
        id = root_information['id']
        context = {
            'msg': False,
            'id': id
        }
        return render(request, 'studentManage/select.html', context)
 
# 删除
def delete(request):
    if request.method == "POST":
        id = request.POST.get('id')
        StudentInformationModel.objects.filter(stu_id=id).delete()
        context = {
            'msg': '成功删除'
        }
        return render(request, 'studentManage/delete.html', context)
    else:
        root_information = request.session['user']
        id = root_information['id']
        context = {
            'id': id
        }
        return render(request, 'studentManage/delete.html', context)
 
 
# 修改
def update(request):
    user_information = request.session['user']
    id = user_information['id']
    stu_data = StudentInformationModel.objects.get(stu_id=id)
    stu_id = stu_data.stu_id
    stu_name = stu_data.stu_name
    stu_phone = stu_data.stu_phone
    stu_addr = stu_data.str_addr
    stu_faculty = stu_data.stu_faculty
    stu_major = stu_data.stu_major
    context = {
        'stu_id': stu_id,
        'stu_name': stu_name,
        'stu_phone': stu_phone,
        'stu_addr': stu_addr,
        'stu_faculty': stu_faculty,
        'stu_major': stu_major,
    }
    if request.method == "POST":
        stu_id = request.POST.get('stu_id')
        stu_name = request.POST.get('stu_name')
        stu_phone = request.POST.get('stu_phone')
        stu_addr = request.POST.get('stu_addr')
        stu_faculty = request.POST.get('stu_faculty')
        stu_major = request.POST.get('stu_major')
        # StudentInformationModel.objects.filter(stu_id=id).update(stu_id=stu_id, stu_name=stu_name, stu_phone=stu_phone, str_addr=stu_addr, stu_faculty=stu_faculty, stu_major=stu_major)
        # 或者 以下这种，对单个数据进行修改
        stu_data = StudentInformationModel.objects.get(stu_id=id)
        stu_data.stu_id = stu_id
        stu_data.stu_name = stu_name
        stu_data.stu_phone = stu_phone
        stu_data.stu_addr = stu_addr
        stu_data.stu_faculty = stu_faculty
        stu_data.stu_major = stu_major
        stu_data.save()
        context = {
            'stu_id': stu_id,
            'stu_name': stu_name,
            'stu_phone': stu_phone,
            'stu_addr': stu_addr,
            'stu_faculty': stu_faculty,
            'stu_major': stu_major,
            'msg': '修改成功'
        }
        return render(request, 'studentManage/update.html', context)
    else:
        return render(request, 'studentManage/update.html', context)

```

#### 四、功能展示

首页：

<img src="https://img-blog.csdnimg.cn/img_convert/db9368a67e6d3c9a61c8fa817f6318bc.png" height="293" width="617">

登录后

<img src="https://img-blog.csdnimg.cn/img_convert/f1acd5cb72d163d77b58763935bc0442.png">

增加： 只有root用户才能增加，我默认了id为1的是root用户

<img src="https://img-blog.csdnimg.cn/img_convert/988bb33e86f8a6cfd91386c217731147.png">

修改：将当前学生信息展现出来，方便我们修改，前端页面中加了placeholder属性

<img src="https://img-blog.csdnimg.cn/img_convert/41ecea79da742c1b252dc0e59d514269.png">

删除：

             <img src="https://img-blog.csdnimg.cn/img_convert/00514c4187dd18b9501c5d1dfd793835.png" height="343" width="703">

查询

<img src="https://img-blog.csdnimg.cn/img_convert/1858f0ec5bdc13ca96faa47f84d6ca51.png" height="468" width="892">

#### 五、源码地址

https://github.com/Gscsd8527/StudentSystem

<img src="https://img-blog.csdnimg.cn/img_convert/c48726d42bf2d66733ecffd81fbf723f.png">

**长按识别上方二维码**加我个人微信，

备注**666**免费领取电子书
