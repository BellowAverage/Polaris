
--- 
title:  Python中如何选择Web开发框架？ 
tags: []
categories: [] 

---
`Python`开发中`Web`框架可谓是百花齐放，各式各样的`web`框架层出不穷，那么对于需要进行`Python`开发的我们来说，如何选择`web`框架也就变成了一门学问了。本篇文章主要是介绍目前一些比较有特点受欢迎的`Web`框架，我们可以根据各个`Web`框架的特性进行选择应用。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/264838c7d69f2d07f83573537513df3e.webp?x-oss-process=image/format,png">

#### Django

`Django`是市面上比较大而全的一个系列`Web`开发框架。`Django`官网上的介绍是：`Django `可以更轻松地以更少的代码更快地构建更好的 `Web `应用程序。它提供了一站式的`web`应用框架解决方案。如实现了缓存、`ORM`、权限验证、管理后台、插件扩展等多项功能。发展到现在，我更愿意认为`Django`是一个功能强大的`Python CMS`系统。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/f01ae2c4766100423245c507f620ef7e.webp?x-oss-process=image/format,png">

我们可以通过一个`django`项目来简单了解下`Django`项目：

```
$ pip install django
$ django-admin startproject djdemo                                                   
 cd djdemo                                                                                                                               
$ django-admin startapp djapp                                                   
$ tree -L 3             
.
├── djapp
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── djdemo
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── settings.cpython-37.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
复制代码
```

#### Flask

是一个轻量级的`Web`应用框架，它本身不包含任何模块，却又支持扩展所有需要的内容，秉承着需要多少用多少的理念，是一个不可多得的`Python Web`框架。而且Flask的开发生态也是欣欣向荣，各种组件均可在社区找到对应的实现工具包。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/c2a434bbd1d4a68cc90c0e751f367329.webp?x-oss-process=image/format,png">

当我们创建一个`Flask`框架应用后，我们可以通过下面的代码来启动一个简单的flask程序：

```
from flask import Flask        # 导入Flask类
 
app = Flask(__name__)          # 实例化Flask类
 
@app.route('/func')            # 编写视图函数及配置路由
def func():
    return '这是Flask框架'
 
if __name__ == '__main__':     # 启动服务
    app.run()
复制代码
```

#### Pyramid

`Pyramid `是一个小巧、快速、实用的开源` Python Web` 框架。它使现实世界的 `Web `应用程序开发和部署更有趣、更可预测且更高效。它是 `Pylons Project` 的一部分。采用的授权协议是` BSD-like license`。`Pyramid`在国内的知名度并不高，其框架代码量和flask差不多，但是性能却比Flask高很多。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/ae68a8f2fc39f4d0461aedf168d25e5b.webp?x-oss-process=image/format,png">

示例代码：

```
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello World!')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
复制代码
```

#### Bottle

是一个用于 `Python `的快速、简单和轻量级的 `WSGI `微型网络框架。它的特点是单文件，代码只使用了`Python`标准库，而不需要额外依赖其他第三方库。可以说`Bottle`完美的发挥了“极简主义”风格，好处是显著的，它让我们的项目尽可能的小，但是弊端也是毋庸置疑的，过少的功能支持导致稍微大点的系统就需要自己去开发添加功能。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/82558b612c39815918333570d5bc7329.webp?x-oss-process=image/format,png">

示例代码参考：

```
from bottle import route, request, run
 
@route('/hello', method=['GET', 'POST'])
def dh():     
  return 'hello ' + request.query.str
 
if __name__ == "__main__":
  run(host='0.0.0.0', port=8080)
复制代码
```

#### Tornado

最初是由`FriendFeed`开发的非阻塞式`Web`服务器。由于是非阻塞式服务器，所以它的访问加载速度比较快，`Tornado`可以支持每秒数千计的连接。对于长轮询、`WebSocket`等实时性`web`服务来说，`Tornado`是一个理想的`Web`框架。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/97797d8294c3e7fc4b12238efda6dcce.webp?x-oss-process=image/format,png">

示例代码：

```
import asyncio

import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
复制代码
```

#### Web.py

是由`Reddit`联合创始人、`RSS`规格合作创作人、著名黑客`Aaron Swartz`开发。`Web.py`使用基于类的视图，可以轻松创建动态网站和强大的互联网应用程序。它提供 `SQL/JDBC `作为其数据库接口，包括对 `Google App Engine `的支持，以及为初学者和专家设计的文档齐全、正确且清晰的界面。

**`web2py`**被定义为一个用于敏捷开发的免费开源`Web`框架，涉及数据库驱动的`Web`应用程序。它是用`Python`编写和编程的。它是一个完整的堆栈框架，由开发人员创建功能齐全的`Web`应用程序所需的所有必要组件组成。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/83705b82af3e9f5381f44bdf8a84119b.webp?x-oss-process=image/format,png">

#### Quixote

`Quixote `是一个使用 `Python `编写基于 `Web `的应用程序的框架。它的目标是按此顺序实现灵活性和高性能。`Quixote` 应用程序的结构往往类似于传统应用程序。格式化网页的逻辑由 `Python `类和函数组成。`Quixote `不强制分离表示逻辑和 “后端” 逻辑。相反，我们鼓励您使用传统技术。例如，一种解决方案是将表示逻辑放在其自己的子包中。

`Quixote`使用的是目录式的`URL`分发规则，使用`python`来编写模板。`PTL`模板更适合程序员，但并不适合美工参与前端代码的编写和修改，且`Quixote`的更新频率较低、社区活跃度不够，所以并不建议在生产环境选用`Quixote`作为`web`开发框架。

#### Sanic

是一个` Python 3.6+ web` 服务器和web框架，它的编写速度很快，号称 Python 中性能最高的异步 Web 框架。它允许使用`python 3.5`中添加的 `async/await` 语法，这使得您的代码不阻塞，速度更快。`Sanic`参考了`Flask`的设计思想，这使得习惯于使用`Flask`开发的程序员能更快的适应`Sanic`的开发。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/48c001bd8c3ac625ce1208d80ba5d3a3.webp?x-oss-process=image/format,png">

代码示例：

```
from sanic import Sanic
from sanic.response import json

app = Sanic("hello_example")

@app.route("/")
async def test(request):
  return json({"hello": "world"})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)
```
