
--- 
title:  tornado入门总结 
tags: []
categories: [] 

---
### 介绍

Tornado全称Tornado Web Server，是一个用Python语言写成的Web服务器兼Web应用框架，由FriendFeed公司在自己的网站FriendFeed中使用，被Facebook收购以后框架以开源软件形式开放给大众。

#### 特点
- 作为Web框架，是一个轻量级的Web框架，类似于另一个Python web ，其拥有异步非阻塞IO的处理方式。- 作为Web服务器，Tornado有较为出色的抗负载能力，官方用nginx反向代理的方式部署Tornado和其它Python web应用框架进行对比，结果最大浏览量超过第二名近40%
<img src="https://img-blog.csdnimg.cn/20181217100852699.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dpbGw0OTA2,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### web框架使用简述

#### 结构

主要分为两个部分，一个是application，另一个是RequestHandler的子类们.

##### Application

负责全局, 包括映射请求转发给处理程序的路由表。e.g.

```
import logging

from tornado.ioloop import IOLoop
from tornado.web import Application

from handlers.errors import DefaultHandler
from handlers.index import (IndexNonTemplateHandler, IndexTemplateHandler, RaiseErrorHandler, EchoWebSocket)

def log_func(handler):
    logging.info(handler.request)


settings = {<!-- -->
    'log_function': log_func,
    'template_path': 'templates',
    'default_handler_class': DefaultHandler
}


def make_app():
    return Application([
        (r'/', IndexNonTemplateHandler),
        (r'/index', IndexTemplateHandler),
        (r'/raise_error', RaiseErrorHandler),
        (r'/echo_websocket', EchoWebSocket),
    ], **settings)


if __name__ == '__main__':
    app = make_app()
    app.listen(9723)
    IOLoop.current().start()

```

这些配置里有个很有趣的地方，tornado的热重载是可以自己设置的，但是他的热重载会导致把命令行中断。需要在后台如任务管理器等工具中将tornado的web服务关闭。

##### RequestHandler

可以理解为就是tornado的view，

```
class IndexNonTemplateHandler(CommonHandler):
    """
    不带模板的handler
    """
    def get(self, *args, **kwargs):
        self.write(
            '''
            &lt;h1&gt;Hello Tornado&lt;/h1&gt;
            &lt;p&gt;我要尝试一下中文&lt;/p&gt;
            '''
        )

```

RequestHandler的结构比较简单，就是根据不同的http方法写不同的函数。返回内容有两种方式：
1. 一种是直接调用`self.write(content)`将内容写入返回1. 另一种是使用`self.render('index.html', greet=u'我只是传来的一句问候语')`返回模板内容，其中模板的路径是在Application的template_path定义的，而传参和django有一丢丢区别，django的context是传一个字典，而这里是传普通参数。
关于404和500页面处理的方法分别是：
- 404是在application设定默认的RequestHandler，如果找不到则会转发到这个handler中来。- 500是需要重写RequestHandler的`def write_error(self, status_code, **kwargs)`方法，可返回字符串或者template
##### 像django一样强大的用户认证系统

好的，并没有，嘻嘻。
- 不过，他的RequestHandler提供了一个`get_current_user`方法，开发者可以重写这个方法，返回一个可用的用户对象，就可以在相关view函数中通过`self.current_user`获取。- 另外tornado.auth模块还提供了Google/Gmail, Facebook, Twitter,和FriendFeed.等第三方应用的oauth认证。然而好像并没有什么卵用。- 关于csrf，只需要在Application中设置一下xsrf_cookies就可以使用
##### template

tornado的模板语法和django的默认模板语法比较相似。不过比较麻烦的是模板复用这个功能，需要在后台建立一个uimoudle。

```
class Entry(tornado.web.UIModule):
    def render(self, entry, show_comments=False):
        return self.render_string(
            "module-entry.html", entry=entry, show_comments=show_comments)

```

然后在Application中设置ui_moudle，接着RequestHandler还得把对应的uimodule以存进context中，最后才可以在template中用module调用。

```
from . import uimodules

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        entries = self.db.query("SELECT * FROM entries ORDER BY date DESC")
        self.render("home.html", entries=entries)

class EntryHandler(tornado.web.RequestHandler):
    def get(self, entry_id):
        entry = self.db.get("SELECT * FROM entries WHERE id = %s", entry_id)
        if not entry: raise tornado.web.HTTPError(404)
        self.render("entry.html", entry=entry)

settings = {<!-- -->
    "ui_modules": uimodules,
}
application = tornado.web.Application([
    (r"/", HomeHandler),
    (r"/entry/([0-9]+)", EntryHandler),
], **settings)

```

##### 数据库相关

tornado是没有自带orm的，还是得引入第三方orm才可以解决问题。

不过官方开发了个叫的库，可以方便tornado对数据库的操作。不过还是只能写sql。而且只支持了mysql。

##### 

tornado有一个特色就是默认支持websocket，实现起来也非常简单，只需要继承WebSocketHandler并重写对应的事件方法即可。e.g.

```
class EchoWebSocket(WebSocketHandler):
    def data_received(self, chunk):
        pass

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

```
