
--- 
title:  用 Python 写了一个学生在线考试管理系统 
tags: []
categories: [] 

---
版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。本文链接：

https://blog.csdn.net/weixin_44269312/article/details/93222359

## 1. Django的简介

Django是一个基于MVC构造的框架。但是在Django中，控制器接受用户输入的部分由框架自行处理，所以 Django 里更关注的是模型（Model）、模板(Template)和视图（Views），称为 MTV模式。它们各自的职责如下：

Django里重要的概念有：
- 路由映射- 视图函数- 模板渲染- Django自带的ORM操作(对象关系映射)
需要学习Django基础的同学可以浏览以下网站（非常有用）：
- Django中文手册- Django 中文网- 自强学堂 Django 基础教程
## 2. 项目的设计思路

1.在线考试系统需求如下：（1）系统登录：验证登录用户的身份，根据用户身份进入不同的页面。（2）学生管理：供管理员使用，用于维护学生基本信息。（3）老师管理：供管理员使用，用于维护教师的基本信息。（4）试题管理：供教师管理，用于维护题库。（5）组卷：供教师使用，教师可以根据考试科目，从题库中选择一些符合条件的试题，形成一份试卷。为了方便教师组卷，应提供方便的查询功能，使教师能查询不同要求的试题。（6）在线考试：供学生使用，根据学生的班级和登录时间显示应考科目的试卷内容。试卷完成提交或考试时间到，不再允许学生修改试卷；实现自动评阅，记录学生的考试成绩，并将评阅结果提供给学生。（7）成绩统计：供教师使用，按照科目、班级等统计学生的考试成绩。（8）成绩查询：供教师和学生使用，提供不同查询方式，使教师和学生可以按需查询考试成绩。

2.设计思路（1）确定角色由需求分析看出，系统有三个基本角色，学生、教师、管理员。
- 管理员负责后台信息的维护- 系统要能实现自动阅卷功能
（2）数据库表的设计因此，我们至少需要如下几个表：
- 学生表 student- 教师表 teacher- 题库表 question（为了方便，题库中都为单项选择题）- 试卷表 paper- 学生成绩表 grade
设计完表，我们还需要确定_表间的关系_，是**1对1(1:1)，1对多(1:n)，还是多对多(n:m)**，这很_重要_，因为后面我们在models.py中创建表时，需要指出表间关系。显然
- 学生表和成绩表，1个学生可参加多门考试，会有多个成绩，学生表和成绩表为1:n- 教师表和试卷表，1个教师会发布多套试卷，但1套试卷只能由1位教师发布，教师表和试卷表为1:n- 试卷表和题库表，1套试卷里包含多道题，题库里的每道题也可出现在多个试卷中，故试卷表和题库表为n:m
表的详细设计如下：（使用MindMaster绘制，有点丑，请忽略，重点写下自己的思考和思路）

## 3. 搭建你的开发环境
- IDE使用PyCharm(profession版的)- python 3.7, Django 2.1.0- 数据库为关系数据库mysql 5.6
为了更快的下载python模块，需要切换镜像源，我使用阿里云的镜像（还有很多镜像源），方法如下：在 C:\Users\XXX(你的账户) 下建立 pip文件夹，在pip下建立 pip.ini文件，输入以下代码：

```
\[global\]  
index-url = http://mirrors.aliyun.com/pypi/simple/  
\[install\]  
trusted-host=mirrors.aliyun.com

```

安装所需模块
- Django的安装：pip install django==2.1.0（请指定版本号，最新的Django需要数据库mysql5.6以上），你可以使用pip list来查看版本，使用 pip uninstall django 来卸载django模块- 安装mysql数据库驱动 pip install pymysql配置好后建立项目
（1）在PyCharm中建立Django项目

此处没有使用虚拟环境，你也可以选择 “New environment using”选项来创建一个虚拟环境（可以避免多个项目使用不同模块的版本时发生冲突）

（2）创建app

Tools-&gt;Run manage.py task

在控制台输入 startapp student，创建一个student app。

之后需要将student app配置在项目的settings.py中，由于我的前台需要用到css、BootStrap、一些图片等文件，所以我在项目下建立static文件夹，并将其路径配置在settings.py文件中。整体目录如下：

（3）settings.py文件的配置配置settings.py文件配置如下，请看注释

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student',#将建立的app名称加入Installed_APPs中
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'onlineExam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'onlineExam.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

#配置mysql数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'exam',#使用数据库的名称
        'USER':'root',#用户名
        'PASSWORD':'123456',#密码
        'HOST':'127.0.0.1',#地址
        'PORT':'3306'#端口号
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

#修改语言为中文
LANGUAGE_CODE = 'zh-hans'

#修改时区为shanghai
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#添加static文件夹
STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),
]


```

需要注意的地方有：
- INSTALLED_APPS 添加了新建的student app- DATABASES 配置你的数据库参数- MIDDLEWARE 注释掉了 # 'django.middleware.csrf.CsrfViewMiddleware’这一行- STATICFILES_DIRS 添加新建的static文件夹
（4）在__init___.py文件添加mysql的驱动模块

```
import pymysql
pymysql.install_as_MySQLdb()

```

## 4. 分模块详细设计

（1）建表在student下的models.py中建表

```
from django.db import models

# Create your models here.

# 为性别,学院 指定备选字段
SEX=(
    ('男','男'),
    ('女','女'),
)
DEPT=(
    ('计算机与通信学院','计算机与通信学院'),
    ('电气与自动化学院','电气与自动化学院'),
    ('外国语学院','外国语学院'),
    ('理学院','理学院'),
)

class Student(models.Model):
    id=models.CharField('学号',max_length=20,primary_key=True)
    name=models.CharField('姓名',max_length=20)
    sex=models.CharField('性别',max_length=4,choices=SEX,default='男')
    dept=models.CharField('学院',max_length=20,choices=DEPT,default=None)
    major=models.CharField('专业',max_length=20,default=None)
    password=models.CharField('密码',max_length=20,default='111')
    email=models.EmailField('邮箱',default=None)
    birth=models.DateField('出生日期')

    class Meta:
        db_table='student'
        verbose_name='学生'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.id;

class Teacher(models.Model):
    id=models.CharField("教工号",max_length=20,primary_key=True)
    name=models.CharField('姓名',max_length=20)
    sex=models.CharField('性别',max_length=4,choices=SEX,default='男')
    dept=models.CharField('学院',max_length=20,choices=DEPT,default=None)
    email=models.EmailField('邮箱',default=None)
    password=models.CharField('密码',max_length=20,default='000000')
    birth=models.DateField('出生日期')

    class Meta:
        db_table='teacher'
        verbose_name='教师'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name;

class Question(models.Model):

    ANSWER=(
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
    )
    LEVEL={
        ('1','easy'),
        ('2','general'),
        ('3','difficult'),
    }
    id = models.AutoField(primary_key=True)
    subject = models.CharField('科目', max_length=20)
    title = models.TextField('题目')
    optionA=models.CharField('A选项',max_length=30)
    optionB=models.CharField('B选项',max_length=30)
    optionC=models.CharField('C选项',max_length=30)
    optionD=models.CharField('D选项',max_length=30)
    answer=models.CharField('答案',max_length=10,choices=ANSWER)
    level=models.CharField('等级',max_length=10,choices=LEVEL)
    score=models.IntegerField('分数',default=1)

    class Meta:
        db_table='question'
        verbose_name='单项选择题库'
        verbose_name_plural=verbose_name
    def __str__(self):
        return '&lt;%s:%s&gt;'%(self.subject,self.title);

class Paper(models.Model):
    #题号pid 和题库为多对多的关系
    pid=models.ManyToManyField(Question)#多对多
    tid=models.ForeignKey(Teacher,on_delete=models.CASCADE)#添加外键
    subject=models.CharField('科目',max_length=20,default='')
    major=models.CharField('考卷适用专业',max_length=20)
    examtime=models.DateTimeField()


    class Meta:
        db_table='paper'
        verbose_name='试卷'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.major;

class Grade(models.Model):
    sid=models.ForeignKey(Student,on_delete=models.CASCADE,default='')#添加外键
    subject=models.CharField('科目',max_length=20,default='')
    grade=models.IntegerField()

    def __str__(self):
        return '&lt;%s:%s&gt;'%(self.sid,self.grade);

    class Meta:
        db_table='grade'
        verbose_name='成绩'
        verbose_name_plural=verbose_name


```

（2）将模型映射到mysql数据库中，很简单，打开 Run manage.py Task,输入迁移命令，先输入makemigrate命令，作用是生成sql文件（create table student(id,sex,…) ），执行后可在student-&gt; migrations下看到执行结果。<img src="https://img-blog.csdnimg.cn/img_convert/7df7900fde83771e1105afcce8777a34.png">

再输入migrate命令，执行makemigrate生成的sql语句，表就建好了，你可以使用navicat或workBench等工具看到Django为我们建好的表。

（3）创建管理员

继续输入createsuperuser命令创建管理员，以便登陆后台。

（4）创建模板在templates中建立index.html模板，作为考试系统首页(可去官网下载BootStrap、JQuery)，在头文件里引入时注意顺序，jquery须在bootstrap.min.js之前引入

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1"&gt;
    &lt;link href="../static/bootstrap-4.3.1-dist/css/bootstrap.min.css" rel="stylesheet"&gt;
    &lt;!-- 必须在引入bootstarp.js之前引入 --&gt;
    &lt;script src="../static/jquery-3.3.1.min.js"&gt;&lt;/script&gt;

    &lt;script src="../static/bootstrap-4.3.1-dist/js/bootstrap.min.js"&gt;&lt;/script&gt;

   &lt;link href="../static/css/index.css" rel="stylesheet"&gt;

    &lt;title&gt;在线考试系统&lt;/title&gt;

&lt;/head&gt;
&lt;body&gt;

&lt;nav class="navbar navbar-expand-sm bg-light navbar-light "&gt;
    &lt;ul class="navbar-nav"&gt;
        &lt;li class="nav-item"&gt;
            &lt;a class="nav-link" href="/toIndex/"&gt;&lt;h3&gt;在线考试系统 首页&lt;/h3&gt;&lt;/a&gt;
        &lt;/li&gt;


        &lt;li&gt;
            &lt;button data-target="#stuModal" data-toggle="modal" class="btn btn-primary"&gt;学生登陆&lt;/button&gt;
        &lt;/li&gt;

        &lt;li&gt;
            &lt;button data-target="#teaModal" data-toggle="modal" class="btn btn-primary"&gt;教师登陆&lt;/button&gt;
        &lt;/li&gt;

        &lt;li class="nav-item"&gt;
            &lt;a class="nav-link" href="/admin"&gt;管理员&lt;/a&gt;
        &lt;/li&gt;


        &lt;li style="position: fixed;right: 70px; font-size: 40px;color: #9fcdff"&gt;{<!-- -->{ student.name }}{<!-- -->{ message }}&lt;/li&gt;
       &lt;a href="/logout/"&gt;&lt;li style="position: fixed;right: 20px; font-size: 20px;top:22px;color:#cc1313"&gt;退出&lt;/li&gt;&lt;/a&gt;

    &lt;/ul&gt;
&lt;/nav&gt;

&lt;div class="container"&gt;

  &lt;br&gt;
  &lt;!-- Nav pills --&gt;
  &lt;ul class="nav nav-pills" role="tablist"&gt;
    &lt;li class="nav-item"&gt;
      &lt;a class="nav-link active" data-toggle="pill" href="#home"&gt;个人信息&lt;/a&gt;
    &lt;/li&gt;
    &lt;li class="nav-item"&gt;
      &lt;a class="nav-link" data-toggle="pill" href="#menu1"&gt;考试信息&lt;/a&gt;
    &lt;/li&gt;
    &lt;li class="nav-item"&gt;
      &lt;a class="nav-link" data-toggle="pill" href="#menu2"&gt;成绩查询&lt;/a&gt;
    &lt;/li&gt;
  &lt;/ul&gt;

  &lt;!-- Tab panes --&gt;
  &lt;div class="tab-content"&gt;
    &lt;div id="home" class="container tab-pane active"&gt;&lt;br&gt;
      &lt;h3&gt;个人信息&lt;/h3&gt;

        &lt;table class="table"&gt;
    &lt;thead&gt;
      &lt;tr&gt;
        &lt;th&gt;属性&lt;/th&gt;
        &lt;th&gt;信息&lt;/th&gt;

      &lt;/tr&gt;
    &lt;/thead&gt;
    &lt;tbody&gt;
      &lt;tr&gt;
        &lt;td&gt;学号&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ student.id }}&lt;/td&gt;

      &lt;/tr&gt;
      &lt;tr class="table-primary"&gt;
        &lt;td&gt;姓名&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ student.name }}&lt;/td&gt;

      &lt;/tr&gt;
      &lt;tr class="table-success"&gt;
        &lt;td&gt;性别&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ student.sex }}&lt;/td&gt;

      &lt;/tr&gt;
      &lt;tr class="table-danger"&gt;
        &lt;td&gt;学院&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ student.dept }}&lt;/td&gt;

      &lt;/tr&gt;

       &lt;tr class="table-success"&gt;
        &lt;td&gt;专业&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ student.major }}&lt;/td&gt;

      &lt;/tr&gt;

      &lt;tr class="table-warning"&gt;
        &lt;td&gt;邮箱地址&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ student.email }}&lt;/td&gt;

      &lt;/tr&gt;
      &lt;tr class="table-active"&gt;
        &lt;td&gt;出生日期&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ student.birth }}&lt;/td&gt;

      &lt;/tr&gt;

    &lt;/tbody&gt;
  &lt;/table&gt;
    &lt;/div&gt;

    &lt;div id="menu1" class="container tab-pane fade"&gt;&lt;br&gt;
      &lt;h3&gt;考试信息&lt;/h3&gt;
      &lt;p&gt;&lt;/p&gt;
        &lt;table class="table"&gt;
    &lt;thead&gt;
      &lt;tr&gt;
          &lt;th&gt;学号&lt;/th&gt;
        &lt;th&gt;姓名&lt;/th&gt;
        &lt;th&gt;考试科目&lt;/th&gt;
          &lt;th&gt;考试时间&lt;/th&gt;
          &lt;th&gt;操作&lt;/th&gt;
      &lt;/tr&gt;
    &lt;/thead&gt;
    &lt;tbody&gt;
    {#   遍历字典  paper #}
    {% for paper1 in paper %}




     &lt;tr class="table-info"&gt;
          &lt;td&gt;{<!-- -->{ student.id }}&lt;/td&gt;
          &lt;td&gt;{<!-- -->{ student.name }}&lt;/td&gt;
          &lt;td&gt;{<!-- -->{ paper1.subject }}{<!-- -->{ paper2.subject }}&lt;/td&gt;
          &lt;td&gt;{<!-- -->{ paper1.examtime }} {<!-- -->{ paper2.examtime }}&lt;/td&gt;
          &lt;td&gt;
              &lt;a href="/startExam/?sid={<!-- -->{ student.id }}&amp;subject={<!-- -->{ paper1.subject }}"&gt;
              &lt;button class="btn btn-primary" id="toExam+{<!-- -->{ paper1.subject }}"&gt;开始考试&lt;/button&gt;
             &lt;/a&gt;
          &lt;/td&gt;
      &lt;/tr&gt;
    {% endfor %}



    &lt;/tbody&gt;
  &lt;/table&gt;
    &lt;/div&gt;

    &lt;div id="menu2" class="container tab-pane fade"&gt;&lt;br&gt;
      &lt;h3&gt;考试成绩&lt;/h3&gt;
      &lt;p&gt;&lt;/p&gt;
        &lt;table class="table"&gt;
        &lt;thead&gt;
          &lt;tr&gt;
            &lt;th&gt;姓名&lt;/th&gt;
            &lt;th&gt;科目&lt;/th&gt;
            &lt;th&gt;成绩&lt;/th&gt;

          &lt;/tr&gt;
        &lt;/thead&gt;
    &lt;tbody&gt;

    {% for grade1 in grade %}
        &lt;tr class="table-primary"&gt;
        &lt;td&gt;{<!-- -->{ student.name }}&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ grade1.subject }}&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ grade1.grade }}&lt;/td&gt;

      &lt;/tr&gt;
    {% endfor %}




    &lt;/tbody&gt;
  &lt;/table&gt;
    &lt;/div&gt;
  &lt;/div&gt;
&lt;/div&gt;


{#学生登录的模态对话框#}
&lt;div class="modal fade" tabindex="-1" role="dialog" id="stuModal"&gt;
    &lt;div class="modal-dialog" role="document"&gt;
        &lt;div class="modal-content"&gt;
            &lt;div class="modal-header"&gt;
                &lt;button type="button" class="close" data-dismiss="modal" aria-label="Close"&gt;
                    &lt;span aria-hidden="true"&gt;&amp;times;&lt;/span&gt;
                &lt;/button&gt;
                &lt;h4 class="modal-title"&gt;学生登陆&lt;/h4&gt;
            &lt;/div&gt;
            &lt;form class="form-horizontal" action="/studentLogin/" method="post"&gt;
            &lt;div class="modal-body"&gt;

                    &lt;div class="form-group"&gt;
                        &lt;label class="col-sm-3 control-label"&gt;学生学号&lt;/label&gt;
                        &lt;div class="col-sm-9"&gt;
                            &lt;input type="text" class="form-control" name="id" placeholder="输入学号"&gt;
                        &lt;/div&gt;
                    &lt;/div&gt;
                    &lt;div class="form-group"&gt;
                        &lt;label for="addr" class="col-sm-3 control-label"&gt;密码&lt;/label&gt;
                        &lt;div class="col-sm-9"&gt;
                            &lt;!--
                            &lt;textarea id="addr" class="form-control" rows="3"&gt;&lt;/textarea&gt;
                            --&gt;
                            &lt;input type="password" class="form-control" name="password" placeholder="输入密码"&gt;
                         &lt;/div&gt;
                    &lt;/div&gt;

            &lt;/div&gt;
            &lt;div class="modal-footer"&gt;
                &lt;button type="button" class="btn btn-default" data-dismiss="modal"&gt;取消&lt;/button&gt;
                &lt;button type="submit" class="btn btn-primary"&gt;登陆&lt;/button&gt;
            &lt;/div&gt;
            &lt;/form&gt;
        &lt;/div&gt;&lt;!-- /.modal-content --&gt;
    &lt;/div&gt;&lt;!-- /.modal-dialog --&gt;
&lt;/div&gt;

{#老师登录的模态对话框#}
&lt;div class="modal fade" tabindex="-1" role="dialog" id="teaModal"&gt;
    &lt;div class="modal-dialog" role="document"&gt;
        &lt;div class="modal-content"&gt;
            &lt;div class="modal-header"&gt;
                &lt;button type="button" class="close" data-dismiss="modal" aria-label="Close"&gt;
                    &lt;span aria-hidden="true"&gt;&amp;times;&lt;/span&gt;
                &lt;/button&gt;
                &lt;h4 class="modal-title"&gt;教师登陆&lt;/h4&gt;
            &lt;/div&gt;
            &lt;form class="form-horizontal" action="/teacherLogin/" method="post"&gt;
            &lt;div class="modal-body"&gt;

                    &lt;div class="form-group"&gt;
                        &lt;label for="inputEmail3" class="col-sm-3 control-label"&gt;教师工号&lt;/label&gt;
                        &lt;div class="col-sm-9"&gt;
                            &lt;input type="text" class="form-control" name="id" placeholder="输入学号"&gt;
                        &lt;/div&gt;
                    &lt;/div&gt;
                    &lt;div class="form-group"&gt;
                        &lt;label for="addr" class="col-sm-3 control-label"&gt;密码&lt;/label&gt;
                        &lt;div class="col-sm-9"&gt;
                            &lt;!--
                            &lt;textarea id="addr" class="form-control" rows="3"&gt;&lt;/textarea&gt;
                            --&gt;
                            &lt;input type="password" name="password" placeholder="输入密码" class="form-control"&gt;
                         &lt;/div&gt;
                    &lt;/div&gt;

            &lt;/div&gt;
            &lt;div class="modal-footer"&gt;
                &lt;button type="button" class="btn btn-default" data-dismiss="modal"&gt;取消&lt;/button&gt;
                &lt;button type="submit" class="btn btn-primary"&gt;登陆&lt;/button&gt;
            &lt;/div&gt;
            &lt;/form&gt;
        &lt;/div&gt;&lt;!-- /.modal-content --&gt;
    &lt;/div&gt;&lt;!-- /.modal-dialog --&gt;
&lt;/div&gt;

&lt;/body&gt;

&lt;script&gt;
    $("#toExam+{<!-- -->{ paper1.subject }}").click(function () {

    });
&lt;/script&gt;
&lt;/html&gt;

```

Django使用{<!-- -->{ }}来使用后台传来的数据

（5）创建视图函数

在student-&gt;views.py中创建进入首页的视图函数index()

```
from django.shortcuts import render,redirect
from student import models
from django.http import HttpResponse
from django.contrib.auth import logout
# Create your views here.
def index(request):
    return render(request,'index.html')

```

将视图函数配置在路由中，打开项目的urls.py文件

```
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from student import views

urlpatterns = [
    #管理员登陆
    path('admin/', admin.site.urls),
    #默认访问首页
    url(r'^$',views.index),
]

```

r表示使用正则表达式解析url地址，^表示开始，$表示结束，views.index表示调用视图函数index。

（6）启动服务器（可以看到效果了）

两种方式启动服务器：执行runserver命令，或点击绿色小图标。

点击网址，默认8000端口，成功后如下图：

我们还需要定制自己的后台，在student-&gt;admin.py中注册各模块

```
from django.contrib import admin
from .models import Student,Teacher,Paper,Question,Grade
# Register your models here.
# 修改名称
admin.site.site_header='在线考试系统后台'
admin.site.site_title='在线考试系统'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','sex','dept','major','password','email','birth')# 要显示哪些信息
    list_display_links = ('id','name')#点击哪些信息可以进入编辑页面
    search_fields = ['name','dept','major','birth']   #指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    list_filter =['name','dept','major','birth']#指定列表过滤器，右边将会出现一个快捷的过滤选项

```

对其他4个model注册后台

```
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'dept', 'password', 'email', 'birth')
    list_display_links = ('id', 'name')
    search_fields = ['name', 'dept', 'birth']
    list_filter = ['name','dept']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','subject','title','optionA','optionB','optionC','optionD','answer','level','score')

```

刷新，点击首页管理员超链接，进入后台，使用前边创建的superuser账户和密码登陆

进入后台

使用后台添加学生信息

（7）实现学生的登陆这里需要用到Django内置的ORM模块，不在赘述，需要的同学看前边网站入门。
- 在views.py中创建studentLogin函数- 学生登陆的form表单将学生输入的学号（id）,密码（password）通过post方式提交给服务器，所以视图函数先接受表单参数，判断用户名和密码与数据库是否一致，若一致，则登陆成功。- 登陆成功后，我需要发送至少三条信息给index.html，（1）该学生的基本信息，（2）该学生考试信息，可通过该学生的专业名称在试卷表中查到有哪些要进行的考试，（3）该学生的考试成绩信息，可通过学生的学号在paper表中查询
代码如下：

```
def studentLogin(request):
    if request.method=='POST':
        # 获取表单信息
        stuId=request.POST.get('id')
        password=request.POST.get('password')
        print("id",stuId,"password",password)
        # 通过学号获取该学生实体
        student=models.Student.objects.get(id=stuId)
        print(student)
        if password==student.password:  #登录成功
            #查询考试信息
            paper=models.Paper.objects.filter(major=student.major)
            #查询成绩信息
            grade=models.Grade.objects.filter(sid=student.id)
            # 渲染index模板
            return render(request,'index.html',{'student':student,'paper':paper,'grade':grade})

        else:return render(request,'index.html',{'message':'密码不正确'})

```

（8）模板的渲染（数据的显示）登陆成功后，发送三个字典数据给index，index模板使用{<!-- -->{ }}、for等模板语句渲染

```
&lt;div class="tab-content"&gt;
    &lt;div id="home" class="container tab-pane active"&gt;&lt;br&gt;
      &lt;h3&gt;个人信息&lt;/h3&gt;
        &lt;table class="table"&gt;
    &lt;thead&gt;
      &lt;tr&gt;
        &lt;th&gt;属性&lt;/th&gt;
        &lt;th&gt;信息&lt;/th&gt;
      &lt;/tr&gt;
    &lt;/thead&gt;
    &lt;tbody&gt;
      &lt;tr&gt;
        &lt;td&gt;学号&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ student.id }}&lt;/td&gt;
      &lt;/tr&gt;
      &lt;tr class="table-primary"&gt;
        &lt;td&gt;姓名&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ student.name }}&lt;/td&gt;
      &lt;/tr&gt;
      &lt;tr class="table-success"&gt;
        &lt;td&gt;性别&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ student.sex }}&lt;/td&gt;
      &lt;/tr&gt;
      &lt;tr class="table-danger"&gt;
        &lt;td&gt;学院&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ student.dept }}&lt;/td&gt;
      &lt;/tr&gt;
       &lt;tr class="table-success"&gt;
        &lt;td&gt;专业&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ student.major }}&lt;/td&gt;
      &lt;/tr&gt;

      &lt;tr class="table-warning"&gt;
        &lt;td&gt;邮箱地址&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ student.email }}&lt;/td&gt;
      &lt;/tr&gt;
      &lt;tr class="table-active"&gt;
        &lt;td&gt;出生日期&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ student.birth }}&lt;/td&gt;
      &lt;/tr&gt;

    &lt;/tbody&gt;
  &lt;/table&gt;
    &lt;/div&gt;

    &lt;div id="menu1" class="container tab-pane fade"&gt;&lt;br&gt;
      &lt;h3&gt;考试信息&lt;/h3&gt;
      &lt;p&gt;&lt;/p&gt;
        &lt;table class="table"&gt;
    &lt;thead&gt;
      &lt;tr&gt;
          &lt;th&gt;学号&lt;/th&gt;
        &lt;th&gt;姓名&lt;/th&gt;
        &lt;th&gt;考试科目&lt;/th&gt;
          &lt;th&gt;考试时间&lt;/th&gt;
          &lt;th&gt;操作&lt;/th&gt;
      &lt;/tr&gt;
    &lt;/thead&gt;
    &lt;tbody&gt;
    {#   遍历字典  paper #}
    {% for paper1 in paper %}
        
     &lt;tr class="table-info"&gt;
          &lt;td&gt;{<!-- -->{ student.id }}&lt;/td&gt;
          &lt;td&gt;{<!-- -->{ student.name }}&lt;/td&gt;
          &lt;td&gt;{<!-- -->{ paper1.subject }}{<!-- -->{ paper2.subject }}&lt;/td&gt;
          &lt;td&gt;{<!-- -->{ paper1.examtime }} {<!-- -->{ paper2.examtime }}&lt;/td&gt;
          &lt;td&gt;
              &lt;a href="/startExam/?sid={<!-- -->{ student.id }}&amp;subject={<!-- -->{ paper1.subject }}"&gt;
              &lt;button class="btn btn-primary" id="toExam+{<!-- -->{ paper1.subject }}"&gt;开始考试&lt;/button&gt;
             &lt;/a&gt;
          &lt;/td&gt;
      &lt;/tr&gt;
    {% endfor %}
    
    &lt;/tbody&gt;
  &lt;/table&gt;
    &lt;/div&gt;
    &lt;div id="menu2" class="container tab-pane fade"&gt;&lt;br&gt;
      &lt;h3&gt;考试成绩&lt;/h3&gt;
      &lt;p&gt;&lt;/p&gt;
        &lt;table class="table"&gt;
        &lt;thead&gt;
          &lt;tr&gt;
            &lt;th&gt;姓名&lt;/th&gt;
            &lt;th&gt;科目&lt;/th&gt;
            &lt;th&gt;成绩&lt;/th&gt;
          &lt;/tr&gt;
        &lt;/thead&gt;
    &lt;tbody&gt;

    {% for grade1 in grade %}
        &lt;tr class="table-primary"&gt;
        &lt;td&gt;{<!-- -->{ student.name }}&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ grade1.subject }}&lt;/td&gt;
        &lt;td&gt;{<!-- -->{ grade1.grade }}&lt;/td&gt;
      &lt;/tr&gt;
    {% endfor %}
    &lt;/tbody&gt;
  &lt;/table&gt;
    &lt;/div&gt;
  &lt;/div&gt;

```

（9）教师登陆同上，学生在线考试和系统自动阅卷怎么实现呢？我是这样做的
- 学生登陆成功后，点击"开始考试"按钮，按钮将两个请求信息发送到服务器，自己的学号和试卷的科目。- startExam视图函数接收到学号和试卷的科目，找到试卷信息发送给另一模板（exam.html）渲染，因此，建立继续建立exam.html模板和startExam视图函数
```
def startExam(request):
    sid = request.GET.get('sid')
    subject1=request.GET.get('subject')
    #得到学生信息
    student=models.Student.objects.get(id=sid)
    #试卷信息
    paper=models.Paper.objects.filter(subject=subject1)
    # print('学号',sid,'考试科目',subject1)
    return render(request,'exam.html',{'student':student,'paper':paper,'subject':subject1})

```

exam模板如下：

```
&lt;!DOCTYPE HTML&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
&lt;meta http-equiv="content-type" content="text/html;charset=UTF-8"&gt;
&lt;meta name="viewport" content="width=device-width, initial-scale=1.0" /&gt;
&lt;title&gt;在线答题考试系统&lt;/title&gt;

    &lt;link href="../static/bootstrap-4.3.1-dist/css/bootstrap.min.css" rel="stylesheet"&gt;
    &lt;!-- 必须在引入bootstarp.js之前引入 --&gt;
    &lt;script src="../static/jquery-3.3.1.min.js"&gt;&lt;/script&gt;

    &lt;script src="../static/bootstrap-4.3.1-dist/js/bootstrap.min.js"&gt;&lt;/script&gt;

    &lt;script src="../static/js/jquery-1.11.3.min.js"&gt;&lt;/script&gt;
    &lt;script src="../static/js/jquery.countdown.js"&gt;&lt;/script&gt;
    &lt;!--时间js--&gt;
    &lt;link href="../static/css/main.css" rel="stylesheet" type="text/css" /&gt;

    &lt;link href="../static/css/test.css" rel="stylesheet" type="text/css" /&gt;
&lt;style&gt;
.hasBeenAnswer {
 background: #5d9cec;
 color:#fff;
}
&lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;

&lt;nav class="navbar navbar-expand-sm bg-light navbar-light "&gt;
    &lt;ul class="navbar-nav"&gt;
        &lt;li class="nav-item active"&gt;
            &lt;a class="nav-link"&gt;&lt;h3&gt;在线考试系统&lt;/h3&gt;&lt;/a&gt;
        &lt;/li&gt;

        &lt;li class="nav-item active"&gt;
            &lt;a class="nav-link"&gt;&lt;h3&gt;当前科目:{<!-- -->{ subject }}&lt;/h3&gt;&lt;/a&gt;
        &lt;/li&gt;
        &lt;li style="position: fixed;right: 70px; font-size: 30px;color: #9fcdff"&gt;{<!-- -->{ student.name }}&lt;/li&gt;

    &lt;/ul&gt;
&lt;/nav&gt;
&lt;div class="main"&gt;
 &lt;!--nr start--&gt;
 &lt;div class="test_main"&gt;
  &lt;div class="nr_left"&gt;
   &lt;div class="test"&gt;
    &lt;form action="/calGrade/" method="post"&gt;
                &lt;input type="hidden" name="sid" value="{<!-- -->{ student.id }}"&gt;
                &lt;input type="hidden" name="subject" value="{<!-- -->{ subject }}"&gt;
     &lt;div class="test_title"&gt;
      &lt;p class="test_time"&gt;
       &lt;i class="icon iconfont"&gt;&amp;#xe6fb;&lt;/i&gt;&lt;b class="alt-1"&gt;01:40&lt;/b&gt;
      &lt;/p&gt;
      &lt;font&gt;&lt;input type="submit" name="tijiao" value="交卷"&gt;&lt;/font&gt;
     &lt;/div&gt;

      &lt;div class="test_content"&gt;
       &lt;div class="test_content_title"&gt;
        &lt;h2&gt;单选题&lt;/h2&gt;
        &lt;p&gt;
         &lt;span&gt;共&lt;/span&gt;&lt;i class="content_lit"&gt;10&lt;/i&gt;&lt;span&gt;题，&lt;/span&gt;
                                    &lt;span&gt;合计&lt;/span&gt;&lt;i class="content_fs"&gt;10&lt;/i&gt;&lt;span&gt;分&lt;/span&gt;
        &lt;/p&gt;
       &lt;/div&gt;
      &lt;/div&gt;
      &lt;div class="test_content_nr"&gt;
       &lt;ul&gt;
                                {% for paper1 in paper %}
                                   {% for test in paper1.pid.all %}
                                       &lt;li id="{<!-- -->{ forloop.counter }}"&gt;
                                        &lt;div class="test_content_nr_tt"&gt;
           &lt;i&gt;{<!-- -->{ forloop.counter}}&lt;/i&gt;&lt;span&gt;({<!-- -->{ test.score }}分)&lt;/span&gt;
                                            &lt;font&gt;{<!-- -->{ test.title }}&lt;/font&gt;

          &lt;/div&gt;
                                       &lt;div class="test_content_nr_main"&gt;
           &lt;ul&gt;
             &lt;li class="option"&gt;
               &lt;input type="radio" class="radioOrCheck" name="{<!-- -->{ test.id }}"
                                                            value="A"/&gt;
              &lt;label&gt;A.
                                                            &lt;p class="ue" style="display: inline;"&gt;{<!-- -->{ test.optionA }}&lt;/p&gt;
              &lt;/label&gt;
             &lt;/li&gt;

             &lt;li class="option"&gt;
               &lt;input type="radio" class="radioOrCheck" name="{<!-- -->{ test.id }}"
                                                            value="B"/&gt;
              &lt;label&gt;
               B.&lt;p class="ue" style="display: inline;"&gt;{<!-- -->{ test.optionB }}&lt;/p&gt;
              &lt;/label&gt;
             &lt;/li&gt;

             &lt;li class="option"&gt;
               &lt;input type="radio" class="radioOrCheck" name="{<!-- -->{ test.id }}"
                                                            value="C"/&gt;
              &lt;label&gt;
               C.&lt;p class="ue" style="display: inline;"&gt;{<!-- -->{ test.optionC }}&lt;/p&gt;
              &lt;/label&gt;
             &lt;/li&gt;

             &lt;li class="option"&gt;
               &lt;input type="radio" class="radioOrCheck" name="{<!-- -->{ test.id }}"
                                                            value="D"/&gt;
              &lt;label&gt;
               D.&lt;p class="ue" style="display: inline;"&gt;{<!-- -->{ test.optionD }}&lt;/p&gt;
              &lt;/label&gt;
             &lt;/li&gt;
           &lt;/ul&gt;
          &lt;/div&gt;
                                        &lt;/li&gt;
                                   {% endfor %}
                                {% endfor %}
       &lt;/ul&gt;
      &lt;/div&gt;
    &lt;/form&gt;
   &lt;/div&gt;
  &lt;/div&gt;

 &lt;/div&gt;
 &lt;!--nr end--&gt;
 &lt;div class="foot"&gt;&lt;/div&gt;
&lt;/div&gt;

&lt;/body&gt;
&lt;/html&gt;


```

效果是这样的：

自动阅卷就简单了：
- 学生提交自己的作答给服务器（同时发送自己的学号和考试科目）- 服务器根据考试科目找到该试卷，并逐个比较学生作答和答案是否一致，若一致，则得到该题的分数，并累加学生成绩- 将学生的学号、该科成绩、科目名称作为一条记录插入到grade表中，返回首页
这里有个细节，试卷中会有很多选择题，后台一次会接收到多个提交答案，我是这样处理的，让每个单选题（有4个选项，使用同一name）的name属性和该题在题库表中的id 保持一致，这样在获取到题号后可以得到该题的答案，以便判断是否作答正确，详见exam.html。

计算成绩的calGrade()视图函数如下：

```
def calGrade(request):

    if request.method=='POST':
        # 得到学号和科目
        sid=request.POST.get('sid')
        subject1 = request.POST.get('subject')

        # 重新生成Student实例，Paper实例，Grade实例，名字和index中for的一致，可重复渲染
        student= models.Student.objects.get(id=sid)
        paper = models.Paper.objects.filter(major=student.major)
        grade = models.Grade.objects.filter(sid=student.id)

        # 计算该门考试的学生成绩
        question= models.Paper.objects.filter(subject=subject1).values("pid").values('pid__id','pid__answer','pid__score')

        mygrade=0#初始化一个成绩为0
        for p in question:
            qId=str(p['pid__id'])#int 转 string,通过pid找到题号
            myans=request.POST.get(qId)#通过 qid 得到学生关于该题的作答
            # print(myans)
            okans=p['pid__answer']#得到正确答案
            # print(okans)
            if myans==okans:#判断学生作答与正确答案是否一致
                mygrade+=p['pid__score']#若一致,得到该题的分数,累加mygrade变量

        #向Grade表中插入数据
        models.Grade.objects.create(sid_id=sid,subject=subject1,grade=mygrade)
        # print(mygrade)
        # 重新渲染index.html模板
        return render(request,'index.html',{'student':student,'paper':paper,'grade':grade})

```

（10）使用百度e-charts可视化数据教师查看学生成绩，可以统计各个分数段的人数<img src="https://img-blog.csdnimg.cn/img_convert/e43ced5bc0176ed0ae9c056f577af536.png"><img src="https://img-blog.csdnimg.cn/img_convert/53683f5a2890bcbf9b1e188a6aa0acfd.png">

我的思路：
- 教师查看学生成绩，点击查看成绩按钮后，发送该科科目名称给后台- 后台视图函数接收科目名，从grade表计算该科目各个分数段的人数，发送给前台模板渲染，并可视化
视图函数如下：

```
#教师查看成绩
def showGrade(request):
    subject1=request.GET.get('subject')
    grade=models.Grade.objects.filter(subject=subject1)

    data1 = models.Grade.objects.filter(subject=subject1, grade__lt=60).count()
    data2 = models.Grade.objects.filter(subject=subject1, grade__gte=60, grade__lt=70).count()
    data3 = models.Grade.objects.filter(subject=subject1, grade__gte=70, grade__lt=80).count()
    data4 = models.Grade.objects.filter(subject=subject1, grade__gte=80, grade__lt=90).count()
    data5 = models.Grade.objects.filter(subject=subject1, grade__gte=90).count()

    data = {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5}

    return render(request,'showGrade.html',{'grade':grade,'data':data,'subject':subject1})
```

源码在公众号**Python小二**后台回复**考试系统**获取。

**路过的道友给个赞吧**
