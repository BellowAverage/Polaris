
--- 
title:  使用Django+MySQL快速搭建一个属于自己的网站 
tags: []
categories: [] 

---
## 使用Django+MySQL快速搭建一个属于自己的网站

Hello小伙伴们，你们好啊~~ 又是日常get新技能的一天， 今天，咱们来整理一下如何使用VMware Workstation上进行openEuler操作系统的安装， 0基础入门，趁着热乎，快上车啦~~GOGOGO。

### 初始环境：

window10 python3.7.6 Django3.2.3 MySQL5.6 pymysql1.0.2 PyCharm Community Edition 2019.2.3

#### 1.下载Django框架

方法一：在cmd里输入：pip install -i https://pypi.douban.com/simple/ django==3.2.3

方法二：或者在pycharm里面左下角找到terminal

​ 或者按快捷键:F12 ，弹出terminal终端窗口。 在其中输入：pip install -i https://pypi.douban.com/simple/ django==3.2.3 这句代码 -I 参数指定使用了douban的镜像，并指定Django版本。

#### 2.创建新Django项目

本人使用的是社区版pycharm没法创建Django项目，所以使用命令行创建。

命令：django-admin startproject 项目名 [目录名]

如果没有指定目录名，那么系统就会默认目录名跟项目名一致。

命令行一（cmd）：django-admin startproject MyFirstWeb myfirstweb 命令行二（terminal终端窗口）：django-admin startproject MyFirstWeb myfirstweb

<img src="https://img-blog.csdnimg.cn/20210606091605322.png#pic_center" alt="在这里插入图片描述">

#### 3.运行Django项目

一定要进入到 MyFirstWeb 目录下（运行服务） 运行一（cmd）：python manage.py runserver 运行二（terminal）：python manage.py runserver

<img src="https://img-blog.csdnimg.cn/20210606091745246.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

关闭端口： win10上：Ctrl+C 或者关进程

#### 4.测试Django项目：

在浏览器输入：http://127.0.0.1:8000 ：或者：localhost:8000 : 可以指定端口号:8000

<img src="https://img-blog.csdnimg.cn/20210606091800906.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

#### 5.Django连接MySQL数据库：

**1.1 安装pymysql：**

方法一：在cmd里输入：pip install -i https://pypi.douban.com/simple/ pymysql==1.0.2

方法二：或者在pycharm里面左下角找到terminal

​ 或者按快捷键:F12 ，弹出terminal终端窗口。 在其中输入：pip install -i https://pypi.douban.com/simple/ pymysql==1.0.2 这句代码 -I 参数指定使用了douban的镜像，并指定pymysql版本。

**1.2 在myfirstweb目录下的 <strong>init**.py 文件中</strong>

```
import pymysql
pymysql.install_as_MySQLdb()

```

**1.3 在myfirstweb目录下的 setting.py 文件中，把DATABASES中的内容注释掉，换成下面的**

```
DATABASES = {<!-- -->
	'default': {<!-- -->
	'ENGINE': 'django.db.backends.mysql', # 数据库的类型
	'NAME': 'django_mysql',  # 所使用的的数据库的名字
	'USER': 'root',  # 数据库服务器的用户
	'PASSWORD': '123456',  # 密码
	'HOST': '127.0.0.1',  # 主机
	'PORT': '3306',  # 端口
	}
	}

```

<img src="https://img-blog.csdnimg.cn/20210606092001878.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

**1.4 生成迁移文件**

python manage.py makemigrations

创建数据库：django_mysql

要指定数据库字符集，否者报错：django.db.utils.DataError: (1366, “Incorrect string value: ‘\xE9\x9F\xB3\xE4\xB9\x90…’ for column ‘name’ at row 5”)

ALTER DATABASE django_mysql CHARACTER SET utf8;

执行迁移（此时是把项目中自带的应用的模型映射到数据库中）

python manage.py migrate

指定表的字符集:ALTER TABLE my_app_musicinfo CONVERT TO CHARACTER SET utf8;

**1.5 创建超级管理员** python manage.py createsuperuser 输入用户名，邮箱，密码，确认密码。 由于密码过于简单，y回车完成创建超级用户。

### 6.创建自己的app

**1.1 创建命令：python manage.py startapp my_app**

**1.2 配置路由**

​ 1.2.1 在目录下的 urls.py 添加子路由(根据自身需求进行更改)

​ 每当 Django 遇到 include() 时，它都会截断直到该时间点匹配的URL的任何部分，并将剩余的字符串发送到包含的 URLconf 中以进行进一步处理。

上面的这段话有2个关键点：截断已经匹配到的部分、将剩下的部分继续送给 include() 指定的 URLconf 文件

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_app/', include('my_app.my_urls'))
]

```

​ 1.2.2 在 my_app 里添加子路由：创建 my_urls.py (根据自身需求进行更改)

编辑文件：

```
from django.urls import path

from . import views


urlpatterns = [
    # path('', views.my_one_view),
    # path('index/', views.my_two_view),
    # path('zhuce/', views.my_three_view),
    path('DownLoad/', views.DownLoad),
    path('DownLoad_one/', views.DownLoad_one),
    path('music_list/', views.music_list),
    path('delete_music/', views.delete_music),
    path('adit_music/', views.adit_music),
    # path('upload_file/', views.upload_file, name="upload_file"),
    # path('image_file/', views.image_file, name="image_file"),
    # path('get_image_file/', views.get_image_file),
]

```

​ **1.3 在 my_app 的 views.py 里添加视图函数：** ​

```
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from .models import MyAppStudentinfo, Username, musicinfo
from django.template import loader
from django.db.models import *
import pymongo
import pandas as pd
import requests
import random
import time
import os
import re


# （一）模板的加载方式：通过loader获取模板，在通过HttpResponse(html)进行响应
    # t = loader.get_template('zhuche.html')
    # html = t.render()
    # return  HttpResponse(html)
    # （二）模板的加载方式：使用render直接加载并响应模板，render(request, '模板文件名', 字典数据)

    # 视图层views与templates模板层之间的交互
    # 视图层views提供： 字典数据（一定是字典）
    # templates模板层： 通过 模板语法 {<!-- -->{字典数据}} 调用视图层传进来的数据（变量）

    # form表单数据将提交到action='路由地址'

# 下载界面
def DownLoad(request):
    return render(request, 'DownLoad.html')


# 播放界面
def DownLoad_one(request):
    global music_info_data
    if request.method == "POST":
        search_music = request.POST.get("music_name")

        weheader = [
            ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'],
            ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'],
            ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0']]

        # 使用列表推导式,生成请求头
        kk_header = [i for i in random.choice(weheader)]

        # 请求头（一定要有'User-Agent'，'Referer'，'csrf'，'Cookie'）
        header = {<!-- -->
            'User-Agent': str(kk_header),
            # 'Host': 'www.kuwo.cn',
            'Referer': 'http://www.kuwo.cn/',
            'csrf': 'D32I86ILA88',
            'Cookie': '_ga=GA1.2.1490969665.1620831748; _gid=GA1.2.1678093837.1620831748; _gat=1; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1620831749; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1620831749; kw_token=D32I86ILA88'}

        # 首页URL
        url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&amp;pn=1&amp;rn=30" \
              "&amp;httpsStatus=1&amp;reqId=30709280-b333-11eb-9d41-ad2a15a69fbf".format(search_music)

        # 发送请求获取首页面
        response = requests.get(url, headers=header, timeout=30).json()

        # 获取data下面的list内容
        list_response = response['data']['list']

        # 循环获取对应内容
        for info in list_response:
            # 歌曲名
            music_name = info['name']
            # rid
            music_rid = info['rid']
            # 作者
            music_artist = info['artist']
            # 作者图像
            music_Image = info['pic']
            # 专辑
            music_album = info['album']
            # 专辑发布时间
            music_releaseDate = info['releaseDate']
            # 歌曲时长
            music_songTimeMinutes = info['songTimeMinutes']

            # 下载音乐（with open()会自动调用关闭文件，所以无需f.close()）
            # with open(os.path.expanduser("~") + '\\Desktop\\music\\' + "{}.mp3".format(music_name), 'wb') as f:
            # 下载的每一首歌的URL（使用的都是统一的，rid不同）
            music_api = 'http://www.kuwo.cn/url?format=mp3&amp;rid={}&amp;response=url&amp;type=convert_url3&amp;br=128kmp3' \
                        '&amp;from=web&amp;t=1620883237037&amp;httpsStatus=1&amp;reqId=f32a4ce1-b3aa-11eb-8486-6142833c02da'.format(music_rid)

            # 将具体下载歌的response转为字典
            music_play_url = requests.get(music_api, headers=header).json()
            time.sleep(2)
            # 通过真正的URL，以二进制的形式获取
            # music_data = requests.get(music_play_url['url']).content
            # 音乐歌词URL
            geci_url = 'http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId={}'.format(music_rid)
            # 获取音乐歌词URL文本
            dome = requests.get(geci_url, headers=header, timeout=30).text
            # 通过正则表达式提取歌词数据
            music_lyric = [re.findall(r'{"lineLyric":"(.*?)","time":"(.*?)"}', dome)[i][0] for i in
                           range(len(re.findall(r'{"lineLyric":"(.*?)","time":"(.*?)"}', dome)))]

            # 以二进制形式写入文件
            # f.write(music_data)

            # 获取表，并存入表
            shujuku = musicinfo()
            shujuku.music_lyric = music_lyric
            shujuku.music_name = music_name
            shujuku.music_artist = music_artist
            shujuku.music_image = music_Image
            shujuku.music_album = music_album
            shujuku.music_releaseDate = music_releaseDate
            shujuku.music_songTimeMinutes = music_songTimeMinutes
            shujuku.music_rid = music_rid
            shujuku.music_play_url = music_play_url['url']
            shujuku.save()

            # 音乐信息内容（字典形式）
            music_info_data = {<!-- -->
                "music_lyric": music_lyric,
                "music_name": music_name,
                "music_artist": music_artist,
                "music_Image": music_Image,
                "music_album": music_album,
                "music_releaseDate": music_releaseDate,
                "music_songTimeMinutes": music_songTimeMinutes,
                "music_play_url": music_play_url['url'],
                # "music_data": music_data,
                "music_rid": music_rid,
            }

            print("下载成功：" + music_name)
            break
        return render(request, 'DownLoad_one.html', context=music_info_data)
    elif request.method == "GET":
        # 从请求头获取id
        huoqu_id = request.GET.get("id")
        # 在数据库进行匹配
        get_music = musicinfo.objects.get(pk=huoqu_id)
        # 音乐信息内容（字典形式）
        music_info_data = {<!-- -->
            "music_lyric": eval(get_music.music_lyric),
            "music_name": get_music.music_name,
            "music_artist": get_music.music_artist,
            "music_Image": get_music.music_image,
            "music_album": get_music.music_album,
            "music_releaseDate": get_music.music_releaseDate,
            "music_songTimeMinutes": get_music.music_songTimeMinutes,
            "music_play_url": get_music.music_play_url,
            "music_rid": get_music.music_rid,
        }
        return render(request, 'DownLoad_one.html', context=music_info_data)



# 音乐列表界面（思路：通过all()获取数据库所有数据all_music_s，将数据库的数据转为字典通过context传参数给"music_list.html"）
def music_list(request):
    try:
        if request.method == "GET":
            # 整表聚合查询：聚合函数：Sun(),Avg(),Count(),Max(),Min()
            # 导入方法：from djanago.db.models import *
            # 返回结果为：字典{"结果变量名": 值}
            musicinfo.objects.aggregate(shuliang=Count('music_id'))
            # 分组聚合查询：
            query = musicinfo.objects.values('music_id')
            query.annotate(shuliang=Count('music_name'))
            # 获取数据库的数据
            all_music_s = musicinfo.objects.all()
            # 将数据库的数据转为字典
            data = {<!-- -->
                "all_music_s": all_music_s
            }
            # # context = data  # 可以传参数，也可以通过python内置函数locals()默认将函数里的所有局部变量打包成字典。
            # return render(request, "music_list.html", data)
            # return render(request, "music_list.html", context = data)
            return render(request, "music_list.html", locals())

        elif request.method == "POST":
            pass
            return render(request, "music_list.html", locals())

    except ObjectDoesNotExist and MultipleObjectsReturned:

        print("Either the blog or entry doesn't exist.")


# 删除界面（思路：从请求头获取id，通过get(pk="huoqu_id")，在数据库进行匹配，delete()执行删除）
def delete_music(request):
    # 从请求头获取id
    huoqu_id = request.GET.get("id")
    # 在数据库进行匹配
    get_music = musicinfo.objects.get(pk=huoqu_id)
    # 执行删除
    get_music.delete()
    # 功能同上
    # musicinfo.objects.get(music_id=huoqu_id).delete()
    return redirect("/my_app/music_list/")


# 编辑界面（思路：分别为两次请求（GET（获取页面所需数据）和POST））
def adit_music(request):
    try:
        if request.method == "GET":
            # 从请求头获取id
            huoqu_id = request.GET.get("id")

            # 在数据库进行匹配
            get_music = musicinfo.objects.get(pk=huoqu_id)
            return render(request, "adit_music.html",{<!-- -->"get_music": get_music})

        elif request.method == "POST":
            # 此时获取的数据就是用户更改的数据
            # 从请求体获取id，music_name，music_artist
            huoqu_id = request.POST.get("id")
            huoqu_music_name = request.POST.get("music_name")
            huoqu_music_artist = request.POST.get("music_artist")

            # 方法一：（更改单个数据）
            # 在数据库进行匹配，通过 QuerySet.属性 更新数据（一定要QuerySet才行）
            # Musicinfo = musicinfo.objects.get(music_id=huoqu_id)

            # # Musicinfo.music_id = huoqu_id
            # Musicinfo.music_name = huoqu_music_name
            # Musicinfo.music_artist = huoqu_music_artist
            # Musicinfo.save()

            # 方法二：（更改多个数据）
            # 在数据库进行匹配，在更新数据。(功能同上)
            musicinfo.objects.filter(music_id=huoqu_id).update(music_name=huoqu_music_name, music_artist=huoqu_music_artist)

            return redirect("/my_app/music_list/")

    except ObjectDoesNotExist and MultipleObjectsReturned:

        print("Either the blog or entry doesn't exist.")



```

​

**1.4（1） 在 my_app 里创建 templates 文件（存放HTML文件的）**

​ 1.4（2）在 settings.py 找到 TEMPLATES 添加 ‘DIRS’: [os.path.join(BASE_DIR, ‘templates’)],

<img src="https://img-blog.csdnimg.cn/20210606092034347.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

```
1.4（3）外层的templates和应用下的templates都存在时
1.4（4）优先查找外层templates目录下的模板
1.4（5）按INSTALLED_APPS配置下的应用顺序逐层查找
1.4（6）为了解决同名模板文件：在各自的APP里的templates下在创建一个跟APP同名的文件夹。
1.1 创建静态文件 static
	在setting里的后面STATIC_URL = '/static/'
	添加如下：（静态文件，image，css，JavaScript）还可以写HTML
	存放在列表：STATICFILES_DIRS=[os.path.join(BASE_DIR,'static'),]
	或者存放在元组：STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)
	# admin显示中文
	LANGUAGE_CODE = 'zh-Hans'
	# 时间
	TIME_ZONE = 'Asia/Shanghai'		
1.2 在 templates 里HTML如何使用静态文件：
	在head里加上：{% load static %}
	引用：{% static 'url' %}

```

​ **1.5 在 settings.py 找到 INSTALLED_APPS 添加 'my_app’**

<img src="https://img-blog.csdnimg.cn/20210606092058229.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

​

​ **1.6 在 models.py 文件中添加表**

```
from django.db import models

class musicinfo(models.Model):
    music_id = models.BigAutoField(primary_key=True, verbose_name='ID')
    music_name = models.CharField(max_length=30, verbose_name='歌曲名')
    music_artist = models.CharField(max_length=30, verbose_name='歌手名')
    music_image = models.ImageField(max_length=1000, verbose_name='歌手图像')
    music_album = models.CharField(max_length=30, verbose_name='专辑')
    music_releaseDate = models.CharField(max_length=30, verbose_name='专辑发布时间')
    music_songTimeMinutes = models.CharField(max_length=30, verbose_name='歌曲时长')
    music_lyric = models. TextField(max_length=1000, verbose_name='歌词')
    music_rid = models.CharField(max_length=30, verbose_name='RID')
    music_play_url = models.CharField('音乐链接地址', max_length=1000)

    # 通过 Meta 内嵌类定义模型类的属性
    class Meta:
        managed = False
        # 数据库表名
        db_table = 'my_app_musicinfo'
        # 在admin中显示
        verbose_name = '音乐列表'
        # 单复数一致
        verbose_name_plural = verbose_name

    # 自定义QuerySet输出格式，在Django shell 中可以显示出详细的数据
    # from my_app.models import 表名   (exit)--退出shell
    def __str__(self):
        return "%s_%s_%s_%s_%s_%s_%s_%s_%s" % \
               (self.music_id, self.music_name, self.music_artist, self.music_image, self.music_album, self.music_releaseDate,
                self.music_songTimeMinutes, self.music_rid, self.music_play_url)



```

​

​ **1.6.1 将数据模型迁移到数据库**

**（1）先创建数据库：django_mysql**

要指定数据库字符集，否则报错：django.db.utils.DataError: (1366, “Incorrect string value: ‘\xE9\x9F\xB3\xE4\xB9\x90…’ for column ‘name’ at row 5”)

ALTER DATABASE django_mysql CHARACTER SET utf8;

**（2）生成迁移文件（会生成0001_initial.py）**

python manage.py makemigrations my_app (my_app是app名) <img src="https://img-blog.csdnimg.cn/20210606092302957.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

**（3）执行迁移（此时是把项目中自带的应用的模型映射到数据库中）迁移到数据库**

python manage.py migrate <img src="https://img-blog.csdnimg.cn/20210606092335535.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

一定要指定表的字符集:ALTER TABLE my_app_musicinfo CONVERT TO CHARACTER SET utf8;

**我们还可以将建好的数据库表映射到 models.py** python manage.py inspectdb &gt; my_app/models.py

### 6.Django的ORM操作

**创建数据（方法一：插入数据明确）** 类名.objects.create(属性1=值1, 属性2=值2) 成功：返回创建好的实体对象 失败：抛出异常

**创建实例对象，并调用save()进行保存** （方法二：数据不明确，需要获取数据） obj = 类名(属性1=值1, 属性2=值2) obj.属性 = 值 obj.save() --（一定要调用）

**查询数据：** 语法：类名.objects.all() 作用：查询所有数据，返回QuerySet容器（存放对象） 相当于SQL语句：SELECT * FROM 表名;

​ 语法：类名.objects.values() ​ 作用：–查询部分列的数据并返回QuerySet容器（存放字典） ​ 相当于SQL语句：SELECT 字段名1, 字段名2 FROM 表名; ​  ​ 语法：类名.objects.values_list() ​ 作用：–查询部分列的数据并返回QuerySet容器（存放元组） ​ 相当于SQL语句：SELECT 字段名1, 字段名2 FROM 表名;（下标拿数据） ​  ​ 语法：类名.objects.order_by(’-列’,‘列’) ​ 作用：–查询所有指定列的数据，返回QuerySet容器（存放对象）（默认按照升序排序，-列则为降序）

​ 语法：类名.objects.exists() ​ 作用：如果 QuerySet 包含任何结果，则返回 True，如果不包含，则返回 False。 ​ 该函数试图以最简单、最快速的方式执行查询，但它 执行 的查询与普通的 QuerySet 查询几乎相同。 ​ entry = Entry.objects.get(pk=123) ​ if some_queryset.filter(pk=entry.pk).exists(): ​ print(“Entry contained in queryset”)

**条件查询：** 语法：类名.objects.filter(属性1=值1, 属性2=值2) （这里的逗号“与”并且的意思） 作用：查询包含此条件的数据，返回QuerySet容器（存放对象） 相当于SQL语句：SELECT 字段名 FROM 表名 WHERE 条件 AND 条件;

​ 语法：类名.objects.exclude(属性1=值1) ​ 作用：返回不包括此条件的全部数据 ​  ​ 语法：类名.objects.get(属性1=值1) ​ 作用：返回包括此条件的一条obj对象数据，没有数据（ObjectDoesNotExist） ​ 或者多于一条数据则报错（MultipleObjectsReturned）

**查询谓词：**(类属性前面都有双下划线) 语法：类属性__exact :等值匹配（常用于 is null） 类名.objects.filter(id__exact=1) 相当于SQL语句：SELECT 字段名 FROM 表名 WHERE 条件;

​ 语法：类属性__contains :指定值匹配 ​ 类名.objects.filter(name__contains=“H”) ​ 相当于SQL语句：SELECT 字段名 FROM 表名 WHERE name like “%H%”; ​  ​ 语法：类属性__startswith :指定值匹配  ​ 类名.objects.filter(name__startswith=“H”) ​ 相当于SQL语句：SELECT 字段名 FROM 表名 WHERE name like “H%”; ​  ​ 语法：类属性__endswith :指定值匹配 ​ 类名.objects.filter(name__endswith=“H”) ​ 相当于SQL语句：SELECT 字段名 FROM 表名 WHERE name like “%H”; ​  ​ __gt:大于指定值 ​ __gte:大于等于 ​ __lt:小于 ​ __lte小于等于 ​ __in:查找数据是否在指定范围内：类名.objects.filter(name__in=[“杰哥”,“牛逼”,“牛逼”]) ​ SELECT 字段名 FROM 表名 WHERE in (“杰哥”,“牛逼”,“牛逼”); ​ __range:查找数据是否在指定区间范围内：类名.objects.filter(shuzi__range=(90,190)) ​ SELECT 字段名 FROM 表名 WHERE BETWEEN 90 AND 190;

**更新单个数据：** 1.查 – 通过get()获得要修改的实体对象 2.改 – 通过 对象.属性 的方法修改数据 3.保存 – 通过 对象.save()保存数据

**更新多个数据：** 1.查 2.改 ：musicinfo.objects.filter(music_id=huoqu_id).update(music_name=huoqu_music_name, music_artist=huoqu_music_artist)

**删除单个数据：** 1.查 – 通过get()获得要修改的实体对象 3.删除 – 通过 对象.delete()删除数据

**删除多个数据：** 1.查 2.改 ：musicinfo.objects.filter(music_id=huoqu_id).delete() **伪删除：** 1.在 models.py 文件里，创建数据库表时，在字段里要添加 布尔型字段 is_active=models.BooleanField(“是否活跃”,default=True)True (默认为True) 执行删除时，将欲删除数据的 is_active 字段设置为 False。 注意：用伪删除时，确保显示数据的地方，均添加了 is_active=True 的过滤查询。

### 7.**admin后台管理：**

​ 注册自定义模型类: ​ （如要将自己定义的模型类也能在admin后台管理界面中显示和管理 ​ 需要将自己的类注册到后台管理界面）

```
1. 在APP中的admin.py中导入注册要管理的模型models类
	from .models import musicinfo
2. 调用admin.site.register()方法进行注册
	admin.site.register(musicinfo)
	
3. ```python
  from django.contrib import admin
  from .models import musicinfo
  # Register your models here.
  
  
  class musicinfoManager(admin.ModelAdmin):
      # 列表页显示哪些字段的列
      list_display = ['music_id' ,'music_name', 'music_artist', 'music_image',
                      'music_album', 'music_releaseDate', 'music_songTimeMinutes',
                      'music_rid', 'music_play_url']
      # 控制 list_display 中的哪些字段可以超链接到修改页（添加的字段必须是 list_display 里面的）
      list_display_links = ['music_name']
      # 添加过滤器
      list_filter = ['music_artist']
      # 添加搜索框[模糊查询]
      search_fields = ['music_name', 'music_artist']
      # 添加可在列表页编辑字段与 list_display_links 不能共存
      # list_editable = ['']
  admin.site.register(musicinfo, musicinfoManager)
  ```

```

模型管理器类： 作用：为后台管理界面添加便于操作的新功能 说明：后台管理类必须继承Django.contrib.admin 里的ModelAdmin类

零碎笔记：

快速排列代码：快捷键：ctrl+shift+alt+L 放大admin界面快捷键：ctrl++

直接运行 python3 manage.py 可列出所有的django 子命令

Django是根据路由找文件的，在找路径的

在使用url时： 自己测试用就用：绝对路径

​ 用相对路径的时候：带‘/’的路由浏览器默认会把当前地址栏里的（协议+IP+端口号）最终访问地址。

URL反向解析：是指在视图或模板中，用path定义的名称来动态查找或计算出相对应的路由。 path(’/luyou/’, views.luyou, name=‘唯一名称’) {% url ‘唯一名称’ ‘参数值1’ ‘参数值2’ %} {% url ‘唯一名称’ id=‘1’ name=‘jiege’ %}==127.0.0.1:8000/xxx/xxx/?id=1&amp;name=jiege

实例对象 = musicinfo.objects.filter().get().update() print(实例对象.query) # 翻译成SQL语句

进入Django shell 环境：python manage.py shell

able = [’’] admin.site.register(musicinfo, musicinfoManager) ```

模型管理器类： 作用：为后台管理界面添加便于操作的新功能 说明：后台管理类必须继承Django.contrib.admin 里的ModelAdmin类

零碎笔记：

快速排列代码：快捷键：ctrl+shift+alt+L 放大admin界面快捷键：ctrl++

直接运行 python3 manage.py 可列出所有的django 子命令

Django是根据路由找文件的，在找路径的

在使用url时： 自己测试用就用：绝对路径

​ 用相对路径的时候：带‘/’的路由浏览器默认会把当前地址栏里的（协议+IP+端口号）最终访问地址。

URL反向解析：是指在视图或模板中，用path定义的名称来动态查找或计算出相对应的路由。 path(’/luyou/’, views.luyou, name=‘唯一名称’) {% url ‘唯一名称’ ‘参数值1’ ‘参数值2’ %} {% url ‘唯一名称’ id=‘1’ name=‘jiege’ %}==127.0.0.1:8000/xxx/xxx/?id=1&amp;name=jiege

实例对象 = musicinfo.objects.filter().get().update() print(实例对象.query) # 翻译成SQL语句

进入Django shell 环境：python manage.py shell

在 models 写上models.ImageField(max_length=30)可能要下载pillow

参考文献： Django对应的python版本：  

本文章仅供个人使用参考，非商用，其中参考了其他的文献资料，如有不妥之处，请联系本人 邮箱：wurenjie8@163.com
