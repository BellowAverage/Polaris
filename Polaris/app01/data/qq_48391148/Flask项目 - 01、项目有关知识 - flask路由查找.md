
--- 
title:  Flask项目 - 01、项目有关知识 - flask路由查找 
tags: []
categories: [] 

---
**目录**



































### web开发知识

>  
 **1、web开发 网站 工具平台 ** 
 **2、基于http协议 ** 
 **3、web服务器  nginx只支持 -- 静态服务器 -- 展示静态页面 ** 
 **4、后端api开发 （前端-- 用户看到的界面（html，css，js） 后端 -- 业务逻辑 -- flask）** 


### 如何动态生成html？如何接受http请求，解析http请求，发送http响应？

>  
  **        这些tcp，http原始请求和响应应该有专门的的服务器软件实现，我们只需要关心业务逻辑就可以了需要统一的接口规则，去让python应用的web服务器与python编写web业务之间做一个统一** 
 **这个接口就是 ： WSGI（Python Web Server Gateway Interface） 它是python语言定义的web服务器和web应用程序或框架之间一种简单而通用的接口规范** 


### 专门的 WSGI 服务器 -- python web服务器 -- gunicorn ， uwsgi

>  
 ** gunicorn -- 跑整个逻辑 配置简单，能做到高并发** 
 **uwsgi  --  配置复杂点** 


###  web开发 模式

>  
 **1、mvc 设计模式 ** 
 **        模型（Model）：数据保存 ** 
 **        视图（View）：用户界面展示 ** 
 **        控制器（Controller）：业务逻辑处理** 
 **2、前后端分离 api（用户程序接口） 前后端分离 -- 提高效率** 


<img alt="" height="545" src="https://img-blog.csdnimg.cn/b6b31a255fbd419abdae3a8b454d65cf.png" width="1144">

###  Flask框架

<img alt="" height="515" src="https://img-blog.csdnimg.cn/d2c5324150aa4e6fbaa2e54df9106cb6.png" width="1200">

>  
 <pre><strong>**flask 和 Django 是python中常用web框架之一**

flask             vs         django
轻量级（需要什么就装什么）        重（有很多东西都已经集成好，不管需不需要）
自由、灵活、扩展性强             笨重，不灵活
适合web服务 api开发</strong></pre> 
   


```
from flask import Flask
# 通常实例化的时候要传入一个import_name，通常使用__name__
# 生成flask核心对象，app就是核心对象
app = Flask(__name__)
# 有专门的服务器来运行flask，app.run只能测试用的，不能用作生产环境
# app.run()
#
#
# # 路由也是要绑定到app核心对象
@app.route("/")
def index():
    return "this is index"


app.run()
```

####  在Pycharm里面设置刚才虚拟环境的解释器

###  使用app.run方式进行测试

<img alt="" height="301" src="https://img-blog.csdnimg.cn/949cf5e8e76c44ea83bdc8da8b33e7d1.png" width="1200">

测试结果

<img alt="" height="351" src="https://img-blog.csdnimg.cn/cb1e976f582042138ccdf0502c5cfbe2.png" width="1200">

** ##########################################################################**

### 使用gunicorn测试

注意：gunicorn要放到linux环境下运行，在windows会报错。 

#### 1、安装 flask 和 gunicorn

```
[root@wangsh python_test]# pip3 install flask
[root@wangsh python_test]# pip3 install gunicorn

```

### 2、在linux下测试gunicorn

```
gunicorn -w 4 -b 0.0.0.0:8000 server:app

```

>  
 ** -w  4   ：开启4个进程** 
 **-b 0.0.0.0:8000  绑定本机0.0.0.0的8000端口** 
 **server:app  :  server文件的app核心对象** 


```
[root@wangsh python_test]# gunicorn -w 4 -b 0.0.0.0:8000 server:app
[2022-08-15 14:59:53 +0800] [7374] [INFO] Starting gunicorn 20.1.0
[2022-08-15 14:59:53 +0800] [7374] [INFO] Listening at: http://0.0.0.0:8000 (7374)
[2022-08-15 14:59:53 +0800] [7374] [INFO] Using worker: sync
[2022-08-15 14:59:53 +0800] [7377] [INFO] Booting worker with pid: 7377
[2022-08-15 14:59:53 +0800] [7378] [INFO] Booting worker with pid: 7378
[2022-08-15 14:59:53 +0800] [7379] [INFO] Booting worker with pid: 7379
[2022-08-15 14:59:53 +0800] [7380] [INFO] Booting worker with pid: 7380

```

<img alt="" height="306" src="https://img-blog.csdnimg.cn/fb05d00759ec4caaa5935afefd371331.png" width="1200">

** ##########################################################################**

###  Flask路由查找

<img alt="" height="649" src="https://img-blog.csdnimg.cn/e455ae690ecd47c99fa3a392bec71a0c.png" width="1081">

>  
 ** 当用户访问时，先在url_map里面找有没有请求的url，如果没有就会抛出404错误** 
 **找到对应的url后，再找对应的endpoint** 
 **然后再在view_function字典里面找对应endpoint的视图函数** 


```
# #############################flask路由
# 路由表示为用户请求的url找出其对应的处理函数的意思

from flask import Flask
# 通常实例化的时候要传入一个import_name，通常使用__name__
# 生成flask核心对象，
htapp = Flask(__name__)

@htapp.route("/")
def index():
    return "this is index"

@htapp.route("/sc/xx/yy", endpoint="sc_index")
def index():
    return "this is index"


htapp.run()
```

<img alt="" height="165" src="https://img-blog.csdnimg.cn/70fa2ca185f44a4484e19676372e9ada.png" width="1200">

** ##########################################################################** 

###  动态url  --  使用methods指定http访问方法，如果方法不被允许会返回405异常

```
@htapp.route('/v1/user/&lt;int:user_id&gt;', methods=["POST", "GET"])
def show_userid(user_id):  # 如果是动态url 这里需要接受参数
    return f"user_id is {user_id}"
```

<img alt="" height="182" src="https://img-blog.csdnimg.cn/02d2f463bbf74137b47e9809eabec750.png" width="700">

 <img alt="" height="611" src="https://img-blog.csdnimg.cn/f182b165d4ea455b8ee4faf1f9eb3a08.png" width="1183">

** ##########################################################################** 

###  构造url - url_for  --  根据endpoint得到对应的url

```
from flask import url_for
@htapp.route("/urlfor")
def geturl():
    result = url_for('show_userid', user_id=10)
    return f"index2 endpoint route is {result}"
```

 <img alt="" height="184" src="https://img-blog.csdnimg.cn/fca96cc1024042898c20956df16dc72a.png" width="811">

###  返回html页面  --  使用 render_template函数

**新建两个文件夹 static  和  templates**

<img alt="" height="103" src="https://img-blog.csdnimg.cn/1cc9d551869f4b4794d071f942bb39d9.png" width="308">

 先编写html页面

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;测试&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;图片展示&lt;/h1&gt;
&lt;img src="{<!-- -->{ url_for('static', filename='images/1.jpg')}}"&gt;
&lt;h1&gt;文本展示&lt;/h1&gt;
&lt;p&gt;姓名：{<!-- -->{ content.name}}&lt;/p&gt;
&lt;p&gt;年龄：{<!-- -->{ content.age}}&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
```

 然后编写返回页面函数  

```
# 返回页面  -- render_template -- 渲染函数，生成动态页面的。
from flask import url_for,render_template
@htapp.route("/img")
def getimg():
    user = {"name":"sc","age":18}
    result = render_template('index.html', content = user)
    return result
```

 <img alt="" height="872" src="https://img-blog.csdnimg.cn/ff1ac1dfa67740f4a9aea6111bcb231f.png" width="1138">

 开启debug功能       --    开启后修改代码就不用再重新执行。

```
# 内置小型web服务器配置
htapp.debug = True  # 开启debug模式，只用作测试环境
# 或者还可以指定 ip和端口
htapp.run(debug=True, host='0.0.0.0', port=8000)
# htapp.run()
```

 

 


