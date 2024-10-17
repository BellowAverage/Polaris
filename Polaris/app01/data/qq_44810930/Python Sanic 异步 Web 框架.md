
--- 
title:  Python Sanic 异步 Web 框架 
tags: []
categories: [] 

---
Sanic 是一个基于 Python 3.6+ 的异步 Web 框架，它使用了 Python 的 async/await 语法来实现高效的非阻塞 IO 操作。

Sanic 的主要作用是提供一个快速、轻量级的方式来构建异步 Web 服务，适用于处理大量并发请求的场景。

以下是一个简单的示例代码，演示了如何使用 Sanic 创建一个简单的 Web 服务，并在根路径返回 “Hello, World!”：

```
from sanic import Sanic
from sanic.response import text

app = Sanic('test')

@app.route("/")
async def index(request):
    return text("Hello, World!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

```

在这个示例中，我们首先导入了 Sanic 模块，然后创建了一个应用程序实例 `app`。接着，使用 `@app.route` 装饰器来定义根路径 `/` 的处理函数 `index`，该处理函数返回 “Hello, World!”。最后，通过 `app.run` 方法来运行应用程序，监听在 8000 端口上。

当你运行这个示例代码后，你可以通过浏览器或工具向 http://localhost:8000 发送请求，就能在页面上看到 “Hello, World!” 的输出。
