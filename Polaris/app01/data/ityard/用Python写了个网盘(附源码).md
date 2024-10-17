
--- 
title:  用Python写了个网盘(附源码) 
tags: []
categories: [] 

---
### 演示地址 

https://cloudself.net/

### 页面展示 

### 本地运行 

1、安装依赖

```
pip install -r requirements.txt
```

2、检查配置文件，修改数据库配置

```
# mycloud/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloud',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'your password',
    }
}
```

3、迁移数据库

```
python manage.py migrate
```

4、执行基础sql文件

```
mysql&gt; use cloud;
mysql&gt; source C:/Users/..../.sql;
```

5、创建超级用户

```
python manage.py createsuperuser
```

6、启动本地服务器

```
python manage.py runserver
```

### 源码获取 

1、点击**下方**图片拉到文末点**喜欢作者**赞赏 **6** 元



2、我核实后会直接回复你源码下载链接，如未能及时回复可以添加小二微信，小二直接用微信发你~

<img src="https://img-blog.csdnimg.cn/img_convert/12f14c3ac0f955e68d69b2743cf7c402.jpeg" alt="12f14c3ac0f955e68d69b2743cf7c402.jpeg">

**不是机器人**

**耐心等待，不要着急**

当然，如果介意付费的话，也是有很多免费的 Python 实战项目可以选择的。


