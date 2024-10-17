
--- 
title:  最简单的 Django 教程 
tags: []
categories: [] 

---
### **一、Django简介**

**1. web框架介绍**

具体介绍Django之前，必须先介绍WEB框架等概念。

**web框架：**别人已经设定好的一个web网站模板，你学习它的规则，然后“填空”或“修改”成你自己需要的样子。

一般web框架的架构是这样的：

其它基于python的web框架，如tornado、flask、webpy都是在这个范围内进行增删裁剪的。例如tornado用的是自己的异步非阻塞“wsgi”，flask则只提供了最精简和基本的框架。Django则是直接使用了WSGI，并实现了大部分功能。

**2. MVC/MTV介绍**

MVC百度百科：全名Model View Controller，是模型(model)－视图(view)－控制器(controller)的缩写，一种软件设计典范，用一种业务逻辑、数据、界面显示分离的方法组织代码，将业务逻辑聚集到一个部件里面，在改进和个性化定制界面及用户交互的同时，不需要重新编写业务逻辑。

**通俗解释：**一种文件的组织和管理形式！不要被缩写吓到了，这其实就是把不同类型的文件放到不同的目录下的一种方法，然后取了个高大上的名字。当然，它带来的好处有很多，比如前后端分离，松耦合等等，就不详细说明了。

**模型(model)：**定义数据库相关的内容，一般放在models.py文件中。

**视图(view)：**定义HTML等静态网页文件相关，也就是那些html、css、js等前端的东西。

**控制器(controller)：**定义业务逻辑相关，就是你的主要代码。

**MTV: **有些WEB框架觉得MVC的字面意思很别扭，就给它改了一下。view不再是HTML相关，而是主业务逻辑了，相当于控制器。html被放在Templates中，称作模板，于是MVC就变成了MTV。这其实就是一个文字游戏，和MVC本质上是一样的，换了个名字和叫法而已，换汤不换药。

**3.Django的MTV模型组织**

目录分开，就必须有机制将他们在内里进行耦合。在Django中，urls、orm、static、settings等起着重要的作用。一个典型的业务流程是如下图所示：

### **二、Django项目实例**

**1. 程序安装**

python3.5、pip3及pycharm专业版自行安装。pycharm不要使用免费版，它不支持Django。

（1）安装Django：

http://www.cnblogs.com/qianyuliang/p/6729298.html

**2. 创建django项目**

在linux等命令行界面下，使用django提供的命令和vim也能进行项目开发。但是，这里使用eclipse

点击：file--&gt;project，出现下面的对话框。

<img src="https://img-blog.csdnimg.cn/img_convert/6310f2dc955a140eb6d0ba2cea9feb7b.png">

选择PyDev/Django栏目，输入项目名称，这里采用国际惯例的mysite。

<img src="https://img-blog.csdnimg.cn/img_convert/f1fc89849e925173d4e926811f82a095.png">

然后一直next就可以了

Django将自动生成下面的目录结构：

<img src="https://img-blog.csdnimg.cn/img_convert/d9c74d5377f1f4fb4a6e60034131aec9.png">

与项目同名的目录中是配置文件，templates目录是html文件存放也就是MTV中的T(手动新建)。manage.py是django项目管理文件。

<img src="https://img-blog.csdnimg.cn/img_convert/d06432de597c5b00b724672478e3aa87.png">
1. **创建APP**
在每个django项目中可以包含多个APP，相当于一个大型项目中的分系统、子模块、功能部件等等，相互之间比较独立，但也有联系。

所有的APP共享项目资源。

右键点击mysite---&gt;Django---&gt;Create application

<img src="https://img-blog.csdnimg.cn/img_convert/6f8d45af20bfce7c70a0a31cef7518e5.png">

这样就创建了一个叫做app01的APP，django自动生成“app01”文件夹。
1. **编写路由**
路由都在urls文件里，它将浏览器输入的url映射到相应的业务处理逻辑。

简单的urls编写方法如下图：

<img src="https://img-blog.csdnimg.cn/img_convert/d3a8b62b49b78760b578b64f41f0ce78.png">
1. **编写业务处理逻辑**
业务处理逻辑都在views.py文件里。

<img src="https://img-blog.csdnimg.cn/img_convert/97c05338f05ffd6d7f8de99159448755.png">

通过上面两个步骤，我们将index这个url指向了views里的index（）函数，它接收用户请求，并返回一个“hello world”字符串。
1. **运行web服务**
现在我们已经可以将web服务运行起来了。

记得将app01写入到settings.py中

<img src="https://img-blog.csdnimg.cn/img_convert/e18298d27eb5ffc34b92a53e009377f8.png">

命令行的方式是：python manage.py runserver 127.0.0.1:8000

在eclipse中---&gt;run configurations

<img src="https://img-blog.csdnimg.cn/img_convert/c9cfdd7e66ea4f4bf5ac60015b2fb424.png">

有这个提示，则表示启动成功，然后打开浏览器，输入127.0.0.1:8000

<img src="https://img-blog.csdnimg.cn/img_convert/08b3889c91b0abc4d28561243c4df373.png">

修改一下url，添加“/index”，就一切ok了！

<img src="https://img-blog.csdnimg.cn/img_convert/aad9ec24ece5e1ab1d102fadfb3dc43b.png">至此，一个最简单的django编写的web服务就启动成功了。
1. **返回HTML文件**
上面我们返回给用户浏览器的是什么？一个字符串！实际上这肯定不行，通常我们都是将html文件返回给用户。

下面，我们写这么一个index.html文件：

<img src="https://img-blog.csdnimg.cn/img_convert/40d1cfcf143b9f83235cf0c9a39c422b.png">

再修改一下views文件：

<img src="https://img-blog.csdnimg.cn/img_convert/6a29861a1d9ca09d1ad2c8252f738b0f.png">

为了让django知道我们的html文件在哪里，需要修改settings文件的相应内容。但默认情况下，它正好适用，你无需修改。

<img src="https://img-blog.csdnimg.cn/img_convert/4ea7db70fac52317528474c4b9a3d41e.png">

接下来，我们可以重新启动web服务。在浏览器刷新一下，你会看到带有样式的“hello world”。
1. **使用静态文件**
我们已经可以将html文件返还给用户了，但是还不够，前端三大块，html、css、js还有各种插件，它们齐全才是一个完整

的页面。在django中，一般将静态文件放在static目录中。接下来，在mysite中新建个static目录。

<img src="https://img-blog.csdnimg.cn/img_convert/fbc79934b687456ee7d0252fb0f4f841.png">

你的CSS,JS和各种插件都可以放置在这个目录里。

为了让django找到这个目录，依然需要对settings进行配置：

<img src="https://img-blog.csdnimg.cn/img_convert/445c4ad6afea2ca20778cb27f6d0d646.png">

同样，在index.html文件中，可以引入js文件了：

<img src="https://img-blog.csdnimg.cn/img_convert/6ba01892a759d6b36721d65faca2068e.png">

重新启动web服务，刷新浏览器，查看结果。
1. **接收用户发送的数据**
上面，我们将一个要素齐全的html文件返还给了用户浏览器。但这还不够，因为web服务器和用户之间没有动态交互。

下面我们设计一个表单，让用户输入用户名和密码，提交给index这个url，服务器将接收到这些数据。

先修改index.html文件

<img src="https://img-blog.csdnimg.cn/img_convert/8eae46c67e88915104ba8ddcba815fb0.png">

然后修改views.py文件

<img src="https://img-blog.csdnimg.cn/img_convert/e478899bd8ee9dbce42822fafc78b7ad.png">

此时 ，重启web服务时，会出错，因为django有一个跨站请求保护机制，我们在settings文件中将它关闭。

<img src="https://img-blog.csdnimg.cn/img_convert/b97c0755020018b0854953a4bd669f2d.png">

再次进入浏览器，刷新页面：

<img src="https://img-blog.csdnimg.cn/img_convert/25f72c56038e5577e8bc10223274e04c.png">输入点东西，然后我们在eclipse中可以看到相应的数据。
1. **返回动态页面**
我们收到了用户的数据，但返回给用户的依然是个静态页面，通常我们会根据用户的数据，进行处理后在返回给用户。

这时候，django采用jinja2语言编写动态模板，jinja2会根据提供的数据，替换掉html中的相应部分，详细语法入门后再深入学习。

先改造views.py文件：

<img src="https://img-blog.csdnimg.cn/img_convert/5378de5a72e7fa7a5017b94e6a220943.png">

再改造index.html文件：

<img src="https://img-blog.csdnimg.cn/img_convert/de3bd690c3c3b9b3c96b390e42d90e5f.png">

重启服务，刷新浏览器：

<img src="https://img-blog.csdnimg.cn/img_convert/313198c1231a003b6f4ca711cc74c3b4.png">

可以看到，我们获得了用户实时输入的数据，并将它实时展示在了用户页面上，这是个不错的交互过程。
1. **使用数据库**
流程走到这里，django的MTV框架基本已经浮出水面了，只剩下最后的数据库部分了。

上面我们虽然和用户交互得很好，但并没有保存任何数据，页面一旦关闭，或服务器重启，一切都将回到原始状态。

使用数据库是毫无疑问的，下面使用mysql数据

在settings中，配置数据库相关的参数，如果使用自带的sqlite，不需要修改。然后在mysql数据库创建mysite库

<img src="https://img-blog.csdnimg.cn/img_convert/34d907a39ba5c4e60b5add9134ede750.png">

再编辑models.py文件，也就是MTV中的M。

<img src="https://img-blog.csdnimg.cn/img_convert/752fbe180ef7e3cb9d5c22a243dbff3e.png">

这里我们创建了2个字段，分别保存用户的名字和密码。

接下来要在后台中通过命令创建数据库的表了。有2条命令，分别是：

python manage.py makemigrations

再输入命令：python manage.py migrate

或者在eclipse中，右键点击mysite---&gt;django---&gt;makemigrations

<img src="https://img-blog.csdnimg.cn/img_convert/c185ef1dd40a1c8d6f7ebf3192a5859e.png">

<img src="https://img-blog.csdnimg.cn/img_convert/c532cec49b2a04a42a0d98334ca89522.png">

然后右键点击mysite---&gt;django---&gt;migrate

<img src="https://img-blog.csdnimg.cn/img_convert/f4bc3e015dda71f9e5d5e0dd18a49d41.png">

修改views.py中的业务逻辑

<img src="https://img-blog.csdnimg.cn/img_convert/8b5bf0b03788b8e41989174c4b69bfbe.png">

重启web服务后，刷新浏览器页面，之后和用户交互的数据都能保存到数据库中。任何时候都可以从数据库中读取数据，展示到页面上。

至此，一个要素齐全，主体框架展示清晰的django项目完成了，其实很简单是不是？

### **三、 Django总结**

作为python必须web框架的Django，它的功能强大，内容全面，但同时也意味着限制颇多，灵活性低，可修改性差，这就是鱼和熊掌不可兼得了。

我们学习Django，其实就是学习一个软件，要理解它的基本原理，把握它整体框架，牢记一些基本规则，剩下的就是不断深入细节，然后熟能生巧、经验多少的问题了，不存在多高深的不可掌握技术。

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/fd96868ee4216d505c2ddc55bb986a48.gif">

微信扫码关注，了解更多内容
