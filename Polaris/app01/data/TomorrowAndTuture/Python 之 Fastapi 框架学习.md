
--- 
title:  Python 之 Fastapi 框架学习 
tags: []
categories: [] 

---
## 依赖安装

Fastapi 有版本要求，需要的 `Python `版本至少是 `Python 3.8（不要犟，按照版本要求来，我最先也是在我 Python3.6 上装的，果不其然跑不起来），幸好我 Win7 老古董能支持的 Python 最高版本可以到 3.8 ，这也算我最后的倔强了。据说这个框架有和 `**Go** 并肩的极高性能，我倒是想特别见识一下。

大家也可以直接去看用户指南  ，这里面讲解得更加详细。

### 安装 fastapi

这个用 pip 安装就是了，没啥多说的，特别是安装有多个 python 解释器的时候，要关注下 pip 和 python 解释器的对应关系。当然，用虚拟环境也是不错的选择。

```
pip3.8 install fastapi
```

### 安装ASGI 服务器

```
pip3.8 install "uvicorn[standard]"
```

这点和 flask 不太一样，flask 创建的 app 直接用 app.run() 就跑起来了，它好像不能这么做，需要使用安装的 uvicorn 去启动服务。

`Uvicorn`是一个基于`ASGI（Asynchronous Server Gateway Interface）`的异步`Web`服务器，用于运行异步`Python web`应用程序。它是由编写`FastAPI`框架的开发者设计的，旨在提供高性能和低延迟的`Web`服务。

## 快速启动

### hello world

```
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    """
    注册一个根路径
    :return:
    """
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app)
```

### <img alt="" height="154" src="https://img-blog.csdnimg.cn/direct/a9936f2981b9459ab139ad427f21132e.png" width="369">

### 文档访问

`SwaggerUi风格文档:`

有了路由的在线文档，对于接口对接或者 API 接口文档编写的时候，就真正方便多了。

<img alt="" height="956" src="https://img-blog.csdnimg.cn/direct/bc87cd76df7345cbbddb0950932c2971.png" width="1200">

### OpenAPI

`FastAPI`框架内部实现了`OpenAPI` 规范，通过访问 ,我们可以看到整个项目的 `API`对应的`JSON`描述。简单来说，这就是一个结构化的 Swagger 文档，返回的细节很详细。

```
{
  "openapi": "3.1.0",
  "info": {
    "title": "FastAPI",
    "version": "0.1.0"
  },
  "paths": {
    "/": {
      "get": {
        "summary": "Index",
        "description": "注册一个根路径\n:return:",
        "operationId": "index__get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    }
  }
}
```

## 路径

### 路径参数

类似于 Flask 的动态路由，使用 Python 标准类型注解（自从有了类型注解以后，总感觉 Python 变了，不像是原来那个不关心类型的脚步语言了），声明路径操作函数中路径参数的类型。

```
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

如果输入的参数类型不匹配的话，还会报错。

```
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "path",
        "item_id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "xyz",
      "url": "https://errors.pydantic.dev/2.6/v/int_parsing"
    }
  ]
}
```

### 路径顺序

```
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

比如要使用 `/users/me` 获取当前用户的数据。然后还要使用 `/users/{user_id}`，通过用户 ID 获取指定用户的数据。由于**路径操作**是按顺序依次运行的，因此，一定要在 `/users/{user_id}` 之前声明 `/users/me` 。这个其实好理解，相当于先写的动态路由把后面的其他路由通配了。一般如果代码审查比较严格的话，是不允许出现这种情况的。**特殊的路由就用特殊的路径，尽量不要和通配路径去碰瓷。**

### 路径预设值

路径操作使用 Python 的 `Enum` 类型接收预设的**路径参数**。**也就是说和动态路由类似，但是动态值的可选范文是提前限定好的。**

```
import uvicorn
from enum import Enum

from fastapi import FastAPI


class ModelName(Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

<img alt="" height="902" src="https://img-blog.csdnimg.cn/direct/474f80e4dc83402a909210efbd9653b8.png" width="1200">

## 查询参数

查询参数都是 URL 的组成部分，因此，它们的类型**本应**是字符串。但声明 Python 类型之后，这些值就会转换为声明的类型，并进行类型校验。

```
import uvicorn
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

<img alt="" height="124" src="https://img-blog.csdnimg.cn/direct/1f1c7330020d455db754d3fb04e12719.png" width="524">

### 默认值

即在声明类型的时候，按照上面的示例指定默认值即可。

### 可选参数

将参数的默认值设置为 None 之后，就可以将参数变为可选参数。

```
import uvicorn
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/{item_id}")
async def read_item(item_id: str, query: str = None):
    if query:
        return {"item_id": item_id, "query": query}
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

<img alt="" height="110" src="https://img-blog.csdnimg.cn/direct/291a1a68058e42b69df0ab71a197ea2a.png" width="495">

<img alt="" height="96" src="https://img-blog.csdnimg.cn/direct/963d0f5b9a90459b816d531d69adcad5.png" width="376">



内容估计有些多，先写一部分，后面再补充。

To be continued
