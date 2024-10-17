
--- 
title:  【实战Flask API项目指南】之二 Flask基础知识 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/c09fc25801ca000c30f3abedf4cc5c53.png" alt="">

## **实战Flask API项目指南之 Flask基础知识**

本系列文章将带你深入探索**实战Flask API项目指南**，通过跟随小菜的学习之旅，你将逐步掌握`Flask` 在实际项目中的应用。让我们一起踏上这个精彩的学习之旅吧！

## 前言

当小菜踏入`Flask`后端开发的世界，掌握`Flask`应用的基本结构是起步的关键。本文将深入探讨基本的`Flask`应用结构，以及如何构建一个简单的`Flask`应用。

<font color="red" size="3">注意：本文叙述的比较详细（即比较啰嗦），不喜欢长篇大论的读者朋友们直接看末尾的 **<font color="bluesky" size="5"> 运行Flask应用 </font>** 即可。</font>

## 安装

在开始之前，小菜需要安装`Flask`。可以通过以下步骤进行安装：
1. 打开命令行终端。1. 运行以下命令来安装 `Flask`
```
pip install flask

```

## 基础知识

接下来，会在这里介绍有关于`Flask`的基础知识。

### 0. 最小的 Flask 应用程序



代码如下：

```
# hello.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "&lt;p&gt;Hello, World!&lt;/p&gt;"

```

**代码释义：**
- 首先导入 `Flask `类。此类的一个实例将是我们的 WSGI 应用程序。- 接下来我们创建该类的一个实例。第一个参数是应用程序的模块或包的名称。 **__name__** 是一个方便的快捷方式，适用于大多数情况。这是必要的，以便 `Flask` 知道在哪里寻找模板和静态文件等资源。- 然后使用**route()装饰器**告诉`Flask`什么`URL`应该触发我们的函数。- 该函数返回我们想要在用户浏览器中显示的消息。默认内容类型是 HTML，因此字符串中的 HTML 将由浏览器呈现。
在命令行终端，输入`flask --app hello run`（这个方式有些麻烦，不推荐）
- `--app`参数指定了`Flask`应用的名称或导入路径（这里是`hello`，即文件名`hello.py`）。- `run`命令将启动一个开发服务器来运行你的`Flask`应用。它会启动一个简单的服务器用于测试和开发。
```
$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

```

此时在浏览器访问`http://127.0.0.1:5000`，可以看到以下画面，这就说明这个web程序成功启动啦！

<img src="https://img-blog.csdnimg.cn/img_convert/98c352d761d54252f058098e01875d0a.png" alt="">

**应用程序发现行为**
- 作为快捷方式，如果文件名为 **app.py** 或 **wsgi.py**，则不必添加 --app。直接使用 `flask run` 即可启动**flask**- 有关更多详细信息，请参阅命令行界面（这个在下面再做介绍）
为了可以让小菜更深入的去理解，下面来拆解一下上面的这份 **最小的 Flask 应用程序** 代码。

### 1. Flask应用的基本结构

`Flask`应用通常由 `Python` 文件构成，其中包含了应用的**设置、路由、视图函数**等。一个简单的`Flask` 应用通常包含以下几个主要部分：
- 导入`Flask`类：`from flask import Flask`- 创建应用实例：`app = Flask(__name__)`
```
# 导入Flask类
from flask import Flask

# 创建应用实例
app = Flask(__name__)

```

### 2. 路由与视图函数

>  
 路由：**routes** 
 视图函数：**view function** 


在`Flask`中，（在下一章节中，会对该概念进行详细介绍）
- 路由用于定义URL与对应的视图函数之间的映射关系。 它告诉`Flask`应用在哪个URL路径下执行哪个视图函数。例如，`@app.route('/')` 装饰器告诉应用当访问根路径 “/” 时，执行后面的视图函数。- 视图函数则负责处理具体的请求并返回响应。它们包含了你希望在特定URL被访问时执行的逻辑。在下面代码中，`def hello_world()` 是一个视图函数，它返回一个简单的HTML段落，即 “Hello, World!”。
```
@app.route("/")
def hello_world():
    return "&lt;p&gt;Hello, World!&lt;/p&gt;"

```

### 3. 请求与响应

当涉及到Web应用程序时，
-  **请求** 的是客户端（通常是浏览器）发送给服务器的信息， -  **响应** 是服务器对请求作出的回应。 -  当在浏览器中输入URL并按下回车键时，浏览器会向服务器发出一个HTTP请求。在这种情况下，由于装饰器`@app.route("/")`指定了根路径 (“/”) 对应于`hello_world`函数，因此它会匹配到这个路由。 -  服务器接收到请求后，`hello_world`函数被调用。这个函数并不需要接收任何参数，因为它只是简单地返回一个字符串。 -  在函数内部，`return`语句告诉服务器要返回一个响应。在这种情况下，响应是一个简单的HTML段落，即`&lt;p&gt;Hello, World!&lt;/p&gt;`。 -  服务器将响应发送回给浏览器，浏览器会将响应内容解析为HTML并显示在页面上。这就是为什么你在浏览器中访问根路径`http://127.0.0.1:5000`时，会看到 **Hello, World!** 个段落。 
总结来说，在代码示例中，`hello_world`函数处理请求，并生成包含 **Hello, World!** 的响应，最终在浏览器中显示出来。

```
@app.route("/")
def hello_world():
    return "&lt;p&gt;Hello, World!&lt;/p&gt;"

```

### 4. 运行Flask应用

>  
 这里的两种运行方式效果一致 


#### **<font color="bluesky" size="5">命令行 运行</font>**

还是上面 **最小的 Flask 应用程序** 的代码，
- 在命令行终端，输入`flask --app hello run`
```
$ flask --app hello run

```

作为快捷方式，如果文件名为 **app.py** 或 **wsgi.py**，则不必添加 --app。直接使用 `flask run` 即可启动**flask**

```
$  flask run

```

#### **<font color="bluesky" size="5">Python 运行</font>**

修改 **最小的 Flask 应用程序** 的代码，
- **`app.run()`：** 这是在Python代码中直接调用`Flask`应用实例的`run()`方法来运行应用。
```
# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "&lt;p&gt;Hello, World!&lt;/p&gt;"


# 追加的代码
if __name__ == '__main__':
    app.run()

```

这将使应用在调试模式下运行，以便在开发过程中进行实时调试和错误查找。

```
if __name__ == '__main__':
    app.run(debug=True)

```

#### tips

在 `app.run()` 设置了 `debug=True`，当代码发生改动时服务器会自动重新加载，并且在出错时提供详细的调试信息。

换句话说，当你的代码发生变化时，`Flask` 服务器会自动识别修改，并且重新加载你的应用，无需手动停止并重新开始你的服务器。

即热启动。

## 总结

通过本文，小菜深入了解了`Flask`应用的基本结构，包括创建应用实例、定义路由和视图函数，以及运行应用的两种方式。

`Flask`为我们提供了一个简单而强大的方式来构建Web应用程序，让我们能够更好地掌握后端开发的基础。随着不断的实践和学习，小菜将能够更加熟练地运用`Flask`来开发出功能丰富的API接口的后端平台。
