
--- 
title:  Python 之 Flask 框架学习 
tags: []
categories: [] 

---
毕业那会使用过这个轻量级的框架，最近再来回看一下，依赖相关的就不多说了，直接从例子开始。下面示例中的 html 模板，千万记得要放到 templates 目录下。

<img alt="" height="426" src="https://img-blog.csdnimg.cn/direct/56e3b8968a064bcb8b6ddf61094c4ca1.png" width="401">

### 快速启动

#### hello world

```
from flask import Flask, jsonify, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '&lt;h1&gt;Hello World!&lt;/h1&gt;'


if __name__ == '__main__':
    app.run()

```

### 路由

既然涉及到web框架，就必然涉及到路由。

#### 动态路由

动态路由就是将变量拼接到路由 url 当中，可以把字段编辑为&lt;variable_name&gt;，这个部分将会作为命名参数传递到你的函数。如果在动态路由中指定了变量的类型，比如 &lt;int:user_id&gt;，则需要按照指定类型进行传值，否则的话也会报错。参数也可以根据类似 request.args.get("id") 进行获取。

```
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/&lt;username&gt;')
def show_user_profile(username):
    id = request.args.get("id")
    return 'User %s, id %s' % (username, id)


@app.route('/users/&lt;int:user_id&gt;')
def show_user_id(user_id):
    return 'User id %d' % user_id


if __name__ == '__main__':
    app.run(debug=True)

```

<img alt="" height="236" src="https://img-blog.csdnimg.cn/direct/1d1bf6b9a6434f859ea8089cffcc4066.png" width="1200">

#### 构造 url

Flask 还可以用 url_for() 函数来给指定的函数构造URL，也称为反向路由。它接收函数名作为第一个参数，也接受对应 URL 规则的变量部分的命名参数。未知变量部分会添加到URL末尾作为查询条件。

```
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return url_for('article', id=1, name="look")  # /article/1?name=look


@app.route('/article/&lt;id&gt;')
def article(id):
    return f'id {id} article detail'


if __name__ == '__main__':
    app.run()

```

#### http方法

HTTP 有许多的不同的构造方法访问 URL 方法。默认情况下，路由只回应 GET 请求，当时通过route() 装饰器传递 methods 参数可以改变这个行为，至于每个 method 对应的行为，这块就不多细说了。

```
from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return "go post method"
    elif request.method == 'GET':
        return "go get method"


if __name__ == '__main__':
    app.run()

```

###  模板

html模板文件一般默认是放在 templates 目录下的，如果没有这个目录的话，可以自己新建一个。

templates/index.html

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;template&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;hello world!&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;
```

```
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

```

#### 变量替换

而且还可以将内容传递到模板文件进行展示，下面这种也是展示 hello world！只不过我们将静态文件的内容藏起来了，通过后端返回的内容再显示出来，用的是模板语法，两种方法在前端显示的都一样。

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;template&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;{<!-- -->{content}}&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;
```

```
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    content = "hello world!"
    return render_template('index.html', content=content)


if __name__ == '__main__':
    app.run()

```

当然，也可以将对象实例传递到模板中去。

user_index.html

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;user&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;hello {<!-- -->{user.name}}&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;
```

models.py

```
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

```

main.py

```
from flask import Flask, render_template
from models import User

app = Flask(__name__)


# 引用模板
@app.route('/')
def hello_world():
    content = 'hello world!'
    return render_template('index.html', content=content)


@app.route('/user')
def user_index():
    user = User(1, 'Looking')
    return render_template('user_index.html', user=user)


if __name__ == '__main__':
    app.run()

```

<img alt="" height="154" src="https://img-blog.csdnimg.cn/direct/b52cb1e26e064fc8bc1fc14785a63535.png" width="405">

#### 条件语句 

info.html

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;条件语句&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    {% if user.id == 1 %}
    &lt;h1&gt; Hello {<!-- -->{user.name}}&lt;/h1&gt;
    {% else %}
    &lt;h1&gt;There is no user!&lt;/h1&gt;
    {% endif %}
&lt;/body&gt;
&lt;/html&gt;
```

```
from flask import Flask, render_template
from models import User

app = Flask(__name__)


# 路由
@app.route('/info/&lt;user_id&gt;')
def info_judge(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1, 'Looking')
    return render_template('info.html', user=user)


if __name__ == '__main__':
    app.run()

```

<img alt="" height="191" src="https://img-blog.csdnimg.cn/direct/37334c6b4fed48c59e65a71c5e4ef774.png" width="442">

<img alt="" height="205" src="https://img-blog.csdnimg.cn/direct/b50ba0690e7148de9dc167f4ac59ab5c.png" width="449">

#### 循环语句

list.html

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;循环语句&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    {% for user in users %}
    &lt;h4&gt;user_id: {<!-- -->{user.id}}; user_name: {<!-- -->{user.name}}&lt;/h4&gt;&lt;br&gt;
    {% endfor %}
&lt;/body&gt;
&lt;/html&gt;
```

```
from flask import Flask, render_template
from models import User

app = Flask(__name__)


# 路由
@app.route('/list')
def info_judge():
    users = []
    for i in range(5):
        users.append(User(i, f"student{i}"))
    return render_template('list.html', users=users)


if __name__ == '__main__':
    app.run()

```

 <img alt="" height="375" src="https://img-blog.csdnimg.cn/direct/b82473735e5d4df6913e9ab2e3ac0151.png" width="466">

#### **模板继承**

我们会发现有一些网页的有些部分是不变的，比如说页头页脚等，当跳转相同网页的时候只有中间部分会改变，这就要使用到模板的继承，可以使用 extends 实现对模板文件的继承。

base.html

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;模板的继承&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;H2&gt;Header 欢迎光临！&lt;/H2&gt;
    &lt;/div&gt;
    {% block content %}
    {% endblock %}
    &lt;div&gt;
        &lt;H2&gt;Footer 欢迎下次再来！&lt;/H2&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

page_one.html

```
{% extends 'base.html'%}
{% block content %}
    &lt;h3&gt;{<!-- -->{content}}&lt;/h3&gt;
{% endblock %}
```

 page_two.html

```
{% extends 'base.html'%}
{% block content %}
    &lt;h3&gt;{<!-- -->{content}}&lt;/h3&gt;
{% endblock %}
```

 main.py

```
from flask import Flask, render_template
app = Flask(__name__)


# 第一页路由
@app.route('/page_one')
def one_page():
    content = '这是第一页！'
    return render_template('page_one.html', content=content)


# 第二页路由
@app.route('/page_two')
def secend_page():
    content = '这是第二页！'
    return render_template('page_two.html', content=content)


# 运行
if __name__ == "__main__":
    app.run()
```

<img alt="" height="290" src="https://img-blog.csdnimg.cn/direct/e603fa735ef34468b97cfc3b2a1d3b27.png" width="426">

### 消息提示

使用 flash 可以将后台处理的消息提示刷新到页面

index.html

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Flask消息提示与异常捕获&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;Login&lt;/h1&gt;
    &lt;form action="/login" method="post"&gt;
        &lt;input type="text" name="username" placeholder="账号"&gt;&lt;br /&gt;
        &lt;input type="password" name="password" placeholder="密码" style="margin-top:10px"&gt;&lt;br /&gt;
        &lt;input type="submit" value="Submit" style="margin-left:50px;margin-top:10px"&gt;
    &lt;/form&gt;
    &lt;!--这里获取的是一个数组--&gt;
    {<!-- -->{get_flashed_messages()[0]}}
&lt;/body&gt;
&lt;/html&gt;
```

main.py 

```
from flask import Flask, render_template, flash, request

app = Flask(__name__)
# 对flash的内容加密
app.secret_key = '123'


@app.route('/login')
def index():
    return render_template("index.html")


# 路由
@app.route('/login', methods=['POST'])
def login():
    # 获取表单上传的数据
    form = request.form
    username = form.get('username')
    password = form.get('password')
    # 进行判断
    if not username:
        flash("please enter username")
        return render_template("index.html")
    if not password:
        flash("please enter password")
        return render_template("index.html")
    if username == "looking" and password == "123456":
        flash("login success")
        return render_template("index.html")
    else:
        flash("username and password not match！")
        return render_template("index.html")


# 运行
if __name__ == "__main__":
    app.run()

```

<img alt="" height="349" src="https://img-blog.csdnimg.cn/direct/e88a132747c34d56834f6b25ac6fa56a.png" width="416">

### 异常捕获 

如果用户输入了错误的路径，创建网站的人又没有设置异常捕获及处理，它会出现404；如果处理了的话，那就显示的为处理后的页面。所以，我们的异常处理也就是对返回的 404 页面（或者其他异常）返回我们设置的页面。

404.html

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Flask异常捕获与处理&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h2&gt;抱歉，你访问的页面去火星了......&lt;/h2&gt;&lt;br /&gt;
    &lt;h2&gt;请检查你的网址是否输入正确！&lt;/h2&gt;
&lt;/body&gt;
&lt;/html&gt;
```

user.html

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Title&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;This is user page&lt;/h1&gt;
​
&lt;/body&gt;
&lt;/html&gt;
```

 main.py

```
from flask import Flask, render_template, abort

app = Flask(__name__)


# 异常捕获一
@app.errorhandler(404)
def not_found():
    return render_template('404.html'), 404


# 异常捕获二
@app.route('/user/&lt;user_id&gt;')
def user_info(user_id):
    if int(user_id) == 1:
        return render_template("user.html")
    else:
        abort(404)


if __name__ == "__main__":
    app.run()

```

<img alt="" height="156" src="https://img-blog.csdnimg.cn/direct/d5d1e1e938b64ab899734ac6048f01ee.png" width="382">

<img alt="" height="257" src="https://img-blog.csdnimg.cn/direct/cdb5c4675fab43cdb58572388f4bed6e.png" width="491">

如果没有添加针对 404 的错误处理，就是下面这种界面。

<img alt="" height="219" src="https://img-blog.csdnimg.cn/direct/ac45d0a192f64c64ad91775b220b99d6.png" width="1200">403 是 Forbidden

<img alt="" height="190" src="https://img-blog.csdnimg.cn/direct/ef494a62a39349fa9646f49d55c04356.png" width="1190">


