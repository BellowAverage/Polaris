
--- 
title:  【实战Flask API项目指南】之七 用JWT进行用户认证与授权 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/76c0f73140e1f6df9991e11a7cb05c44.png" alt="">

## 实战Flask API项目指南之 用JWT进行用户认证与授权

本系列文章将带你深入探索**实战Flask API项目指南**，通过跟随小菜的学习之旅，你将逐步掌握 `Flask` 在实际项目中的应用。让我们一起踏上这个精彩的学习之旅吧！

## 前言

当小菜踏入`Flask`后端开发的世界时，了解 **JSON Web Token（JWT）** 是非常有益的。**JWT** 是一种用于认证和授权的解决方案，在`Flask` 中有广泛的应用。它提供了一种安全、可扩展和灵活的方式来管理用户会话和授权。

在上一篇文章中，小菜成功将 **本地版图书管理系统后端API** 改写成 **持久化数据存储的图书管理系统后端API**。但是还存在安全隐患，因为后端并没有对每个请求做验证。换句话说，任何人都可以请求数据而不受限制，这显然是不合理的。因此，在本文中，我们将在前一篇文章的基础上，添加安全验证步骤，以增加后端 API 平台的安全性。

**JWT**具体的内容参考以下链接：
- - 
<font size="5" color="bluesky"> 注意：不要以明文形式存储密码，建议存储密码的哈希值，这里只为了作展示</font> <font size="5" color="bluesky"> 注意：不要以明文形式存储密码，建议存储密码的哈希值，这里只为了作展示</font> <font size="5" color="bluesky"> 注意：不要以明文形式存储密码，建议存储密码的哈希值，这里只为了作展示</font>

## 实现用户认证与授权

### 1. 用户认证与授权

现在，让我们深入探讨如何在 `Flask` 应用程序中使用 **Flask-JWT-Extended** 进行用户认证和授权。

#### 1.1 用户认证

用户认证是确认用户身份的过程。使用 **Flask-JWT-Extended**库，轻松实现用户登录和**JWT**生成：
- 用户提供凭据（通常是用户名和密码）进行登录。- 服务器验证凭据并生成**JWT**令牌。- 令牌返回给客户端，客户端将其存储并在以后的请求中发送。
#### 1.2 用户授权

用户授权是确定用户是否具有执行特定操作或访问特定资源的权限的过程。**JWT**的载荷通常包含有关用户的角色和权限信息。在每个请求中，服务器可以验证令牌中的角色和权限来确定用户是否被授权执行操作。

### 2. JWT简介

具体的原理戳这里查看啦：

#### 2.1 JWT结构

JWT由三部分组成：
- **头部（Header）**：通常包含令牌的类型（**JWT**）和使用的加密算法。- **载荷（Payload）**：包含有关用户或其他数据的信息。例如，用户ID、角色或其他自定义数据。- **签名（Signature）**：由头部、载荷和密钥组合而成的签名，用于验证令牌的完整性和来源可信度。
#### 2.2 生成和验证JWT
1. 用户登录时，服务器使用密钥签署JWT，并将其返回给客户端。1. 客户端在以后的请求中发送JWT作为身份验证令牌。1. 服务器验证JWT的签名以确保其完整性，然后使用载荷中的信息进行用户身份验证和授权。
### 3. Flask-JWT-Extended简介

>  
 这里只是比较基础的对 **Flask-JWT-Extended** 的应用，各位读者朋友们可以通过官网去系统的学习 **Flask-JWT-Extended**。 


**Flask-JWT-Extended**是一个**Python**库，用于在 `Flask` 应用程序中添加JSON Web令牌（JWT）支持。它是一个插件，可以通过安装它来扩展Flask应用程序的功能。

可以通过官方文档做系统的学习。
- 
#### 2.1 安装依赖

首先，需要安装 **Flask-JWT-Extended** 扩展：

```
pip install Flask-JWT-Extended

```

#### 2.2 配置

>  
 请记住更改应用程序中的 JWT 密钥，并确保其安全。 JWT 使用此密钥进行签名，如果有人得到它，他们将能够创建您的 Web Flask 应用程序接受的任意令牌。 


将`'your-secret-key'`替换为自己的密钥。这个密钥将用于签署和验证**JWT**令牌。

```
from flask import Flask
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)

app = Flask(__name__)
# 用于签名JWT的密钥
app.config['JWT_SECRET_KEY'] = 'your-secret-key' 

# 初始化JWT扩展
jwt = JWTManager(app)

```

#### 2.3 基本用法

>  
 这一 **part** 将介绍 **flask_jwt_extended** 的基础用法，以及展示 **JWT** 认证通过与不通过、获取**token**等的操作。 


##### 2.3.1 flask_jwt_extended 代码

**代码释义：**
- 定义了 `/login` 路由，用于用户登录并获取JWT令牌。在这个路由中，首先从请求中获取用户名和密码（这里是 “**test**” 和 “**test**”）。如果匹配成功，就使用 `create_access_token` 函数生成JWT令牌，并返回给客户端。<li>定义了 `/protected` 路由，它是受保护的路由，只有在请求中包含有效的JWT令牌时才能访问。这是通过 `@jwt_required()` 装饰器实现的。 
  <ul>- 如果请求中没有有效的JWT令牌，访问该路由会返回未授权的响应。- 如果令牌有效，路由会使用 `get_jwt_identity()` 函数获取JWT中的身份信息（在示例中为用户名）然后返回一个JSON响应，显示已登录的用户
<font size="5" color="bluesky"> 注意：不要以明文形式存储密码，建议存储密码的哈希值，这里只为了作展示</font>

```
# -*- coding: utf-8 -*-
# Name:         basic_usage.py


from flask import (Flask, jsonify, request)
from flask_jwt_extended import (create_access_token, get_jwt_identity, jwt_required, JWTManager)

app = Flask(__name__)

# 设置 Flask-JWT-Extended 扩展
app.config["JWT_SECRET_KEY"] = "super-secret"  # 修改为你自己的密钥
jwt = JWTManager(app)


# 创建一个路由来验证您的用户并返回JWTs。create_access_token() 函数用于实际生成JWT。
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({<!-- -->"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


# 受保护的路由，需要JWT认证
@app.route("/protected", methods=["GET"])
@jwt_required()  # 这个装饰器要求请求必须携带有效的JWT令牌
def protected():
    # 使用get_jwt_identity访问当前用户的身份
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


if __name__ == "__main__":
    app.run()


```

##### 2.3.2 无token请求

请求**http://127.0.0.1:5000/protected**，
- 因为 **JWT** 认证没通过，可以看到提示缺少授权的请求头，下面去申请一个**token** <img src="https://img-blog.csdnimg.cn/img_convert/5f28fbf3f026f2e03f289d4a307a33c6.png" alt="">
##### 2.3.3 申请token

传入**data**，**username** 和 **password** 都是**test**，

```
import requests

url = 'http://127.0.0.1:5000/login'
data = {<!-- -->
    'username': 'test',
    'password': 'test'
}
resp = requests.post(url, json=data)
print(resp.status_code)
print(resp.json())

```

**代码运行效果如下：** <img src="https://img-blog.csdnimg.cn/img_convert/d66472b7fbd7df7c4b9eea8c6bbfdfde.png" alt="">

在申请到 **access_token**之后，按照下面的形式，添加到请求头中

```
Authorization: Bearer &lt;access_token&gt;

```

##### 2.3.4 有token请求

可以看到成功返回了用户的身份，

```
import requests

url = 'http://127.0.0.1:5000/protected'
headers = {<!-- -->
    'Authorization': 'Bearer xxxxxxxxxxxxxxx'
}
resp = requests.get(url, headers=headers)
print(resp.status_code)
print(resp.json())

```

**代码运行效果如下：** <img src="https://img-blog.csdnimg.cn/img_convert/9110437521369bd6cd071f4e84892e32.png" alt="">

##### 2.3.5 设置token有效期

>  
 设置JWT的过期时间是一种重要的安全措施，可以帮助确保令牌不会无限期有效，提高了应用程序的安全性。 


注意，这里使用的是访问**token**。

**方法一：**

使用 `app.config['JWT_ACCESS_TOKEN_EXPIRES']` 来设置**JWT**的访问**token**默认过期时间为1小时。

```
# 设置ACCESS_TOKEN的默认过期时间为1小时
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

```

**方法二：**

当使用`create_access_token`函数创建JWT令牌时，也可以通过传递`expires_delta`参数来覆盖默认的过期时间，例如：
- 这将覆盖默认的过期时间，使得令牌在30分钟后过期。
```
from datetime import timedelta


# 设置ACCESS_TOKEN的默认过期时间为30分钟
access_token = create_access_token(identity=username, expires_delta=timedelta(minutes=30))


```

**当 token过期后**，请求效果如下：
- 就会提示**Token**过期啦。
<img src="https://img-blog.csdnimg.cn/img_convert/2eeeb12eaee64858220c3345b55cd5c3.png" alt="">

##### 2.3.6 刷新token

这里要明确一下两个令牌概念，**token**分两种，具体可以查看下表

||访问**token**（**Access Token**）|刷新**token**（**Refresh Token**）
|------
|用途|用于访问受保护的资源|用于获取新的**访问token**
|生命周期|默认为15分钟|默认为30天
|显式指定生命周期|` JWT_ACCESS_TOKEN_EXPIRES`|`JWT_REFRESH_TOKEN_EXPIRES`
|储存方式|在请求的头信息（Header）中的 “Authorization” 字段中|一般存储在服务器端的数据库

每个用户生成的**刷新token**和**访问token**是一一对应的，

当用户登录成功后，服务器会为该用户生成一对**刷新token**和**访问token**，并将它们关联到用户的身份（通常是用户的用户名或ID）。这样，每个用户都有自己唯一的**刷新token**和**访问token**。

**刷新token**用于获取新的**访问token**，以延长用户的会话时间。只有拥有有效的**刷新token**的用户才能获取新的**访问token**，而**访问token**则用于实际访问受保护的资源。

在上面的 **flask_jwt_extended** 代码中，修改了**login**函数，和添加了**refresh**函数，

```
# 创建一个路由来验证您的用户并返回JWTs。create_access_token() 函数用于实际生成JWT。
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({<!-- -->"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)
    return jsonify(access_token=access_token, refresh_token=refresh_token)


# 使用刷新token获取新的访问token
@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)  # 使用刷新token进行验证
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify(access_token=access_token)


```

一般来说，刷新**token**的有效时长会比访问**token**的有效时长更长，所以在访问**token**失效时候，可以使用刷新**token**去获得新的访问**token**。这样做的有几个优点：
1. 用户体验：用户不需要重新输入用户名和密码，而只需提供有效的**刷新token**，就可以轻松地获取新的**访问token**。1. 安全性：如果用户的**刷新token**被泄露，攻击者仍然需要有效的用户名和密码才能获得新的**访问token**。这增加了安全性，因为攻击者无法仅凭**刷新token**获得新的**访问token**。1. 减少身份验证：用户不需要频繁地重新进行完整的身份验证，这可以减轻服务器的负担，并提高性能。
总之，`/refresh` 路由的主要目的是提供一种方便的方式来获取新的**访问token**，减少重复的登录操作，而不需要重新提供用户名和密码，同时提高了安全性。

###### 2.3.6.1 获取两种token

在加上以上的代码之后，继续来看看运行效果。

访问 ‘http://127.0.0.1:5000/login’，可以得到以下结果。可以看到获得了两种**token**，

<img src="https://img-blog.csdnimg.cn/img_convert/f7daade1f99abfc9a1329aeb500d2251.png" alt="">

###### 2.3.6.2 访问token过期

在**访问token**过期的情况下，访问如下所示，这个时候需要使用 **刷新token** 去获得新的 **访问token**。

<img src="https://img-blog.csdnimg.cn/img_convert/4aa908fbc854abddfcb90b497cd6efc4.png" alt="">

###### 2.3.6.3 获取新的访问`token`

当使用 **刷新token**去访问 **refresh**时候，服务端就会给我们返回 新的 **访问token** 。

<img src="https://img-blog.csdnimg.cn/img_convert/7822118a15bb4ceaa349f6b337492c03.png" alt="">

关于**JWT**的介绍到此结束！

### 4. 改写后端API代码

以下是添加了用户认证与授权的 **持久化数据存储的图书管理系统后端API**代码，直接拿来就用！！！
- 校验账号密码这里，密码千万不要用明文，千万不要用明文！！！
```
# -*- coding: utf-8 -*-


from datetime import timedelta

from flask_sqlalchemy import SQLAlchemy
from flask import (Flask, jsonify, request)
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity, create_refresh_token)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/flask'  # 替换为你的数据库 URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['JWT_SECRET_KEY'] = '1234567890'  # 替换为你的密钥
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=10)  # 设置JWT的默认过期时间为10分钟
# app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
jwt = JWTManager(app)


# 定义Book模型类
class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)


# 创建一个路由来验证您的用户并返回JWTs。create_access_token() 函数用于实际生成JWT。
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({<!-- -->"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)
    return jsonify(access_token=access_token, refresh_token=refresh_token)


# 受保护的路由，需要JWT认证
@app.route("/protected", methods=["GET"])
@jwt_required()  # 这个装饰器要求请求必须携带有效的JWT令牌
def protected():
    # 使用get_jwt_identity访问当前用户的身份
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


# 使用刷新令牌获取新的访问令牌
@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)  # 使用刷新令牌进行验证
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify(access_token=access_token)


# 获取所有书籍
@app.route("/books", methods=["GET"])
@jwt_required()
def get_all_books():
    books = Book.query.all()
    book_list = [{<!-- -->"id": book.book_id, "title": book.title, "author": book.author} for book in books]
    return jsonify(book_list), 200


# 获取特定书籍
@app.route("/books/&lt;int:book_id&gt;", methods=["GET"])
@jwt_required()
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify({<!-- -->"id": book.book_id, "title": book.title, "author": book.author}), 200
    return jsonify({<!-- -->"error": "Book not found."}), 404


# 创建新书籍
@app.route("/books", methods=["POST"])
@jwt_required()
def create_book():
    data = request.json
    new_book = Book(title=data["title"], author=data["author"])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({<!-- -->"id": new_book.book_id, "title": new_book.title, "author": new_book.author}), 201


# 更新书籍信息
@app.route("/books/&lt;int:book_id&gt;", methods=["PUT"])
@jwt_required()
def update_book(book_id):
    book = Book.query.get(book_id)
    if book:
        data = request.json
        book.title = data["title"]
        book.author = data["author"]
        db.session.commit()
        return jsonify({<!-- -->"id": book.book_id, "title": book.title, "author": book.author}), 200
    return jsonify({<!-- -->"error": "Book not found."}), 404


# 删除书籍
@app.route("/books/&lt;int:book_id&gt;", methods=["DELETE"])
@jwt_required()
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return "", 204
    return jsonify({<!-- -->"error": "Book not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)


```

### 5. 请求端代码

下面展示了用户如何使用 Python 的 `requests` 库来发送带有 JWT 令牌的请求，以获取受保护的数据：
- 如果**访问token**（Access Token）过期，Flask-JWT-Extended会自动返回错误响应，不需要手动验证过期。- @jwt_required() # 这个装饰器会自动验证令牌的有效性和过期状态- 这里使用 装饰器实现了当 **访问token**失效后通过 **刷新token**来生成一个新的 **访问token**
```
# -*- coding: utf-8 -*-


import time
import requests

# 定义 API 服务的基本 URL
BASE_URL = 'http://127.0.0.1:5000'
access_token = str()
refresh_token = str()


def login(uname: str, passwd: str):
    login_url = f"{<!-- -->BASE_URL}/login"
    data = {<!-- -->"username": uname, "password": passwd}
    resp = requests.post(login_url, json=data)
    if resp.status_code == 200:
        return resp.json().get("access_token"), resp.json().get("refresh_token")
    else:
        print("Login failed.")
        return None, None


def refresh_access_token():
    global access_token
    refresh_url = f"{<!-- -->BASE_URL}/refresh"
    headers = {<!-- -->
        "Authorization": f"Bearer {<!-- -->refresh_token}"
    }
    resp = requests.post(refresh_url, headers=headers)
    if resp.status_code == 200:
        access_token = resp.json().get("access_token")
        return True
    else:
        print("Token refresh failed.")
        return None


def with_refresh(func):
    def wrapper(*arg, **kwargs):
        try:
            resp = func(*arg, **kwargs)
            if resp.status_code == 401:
                raise Exception(resp.json().get('msg'))
            else:
                return resp
        except Exception as e:
            print(f"Error: {<!-- -->e}")
            new_access_token = refresh_access_token()
            if new_access_token:
                return func(*arg, **kwargs)
            else:
                print("Token refresh failed.")
                return None
    return wrapper


@with_refresh
def get_protected_data():
    headers = {<!-- -->"Authorization": f"Bearer {<!-- -->access_token}"}
    protected_url = f"{<!-- -->BASE_URL}/books"
    return requests.get(protected_url, headers=headers)


if __name__ == "__main__":
    access_token, refresh_token = login("test", "test")
    response = get_protected_data()
    print(response.json())
    time.sleep(62)
    response = get_protected_data()
    print(response.json())


```

在这个示例中，
-  `login` 函数负责发送登录请求并获取 **JWT** 令牌。 -  获得令牌后，`get_protected_data` 函数使用获得的 JWT 令牌来获取受保护的数据。 -  如果 **访问token**失效了，则会调用 `refresh_access_token` 函数来获取新的 **访问token** 
## 总结

这篇文章介绍了如何在 `Flask` 中使用 **JSON Web Token（JWT）** 进行用户认证和授权。它包括以下主要内容：
1. **JWT介绍**：解释了**JWT**的基本原理，包括JWT的结构和生成验证过程。1. **Flask-JWT-Extended简介**：介绍了**Flask-JWT-Extended**扩展，它是一个用于在 `Flask` 应用程序中添加**JWT**支持的插件。1. **JWT的基础用法**：演示了如何使用 **Flask-JWT-Extended** 实现用户登录、**JWT**生成以及受保护路由的访问。还包括了设置JWT过期时间和刷新令牌的功能。1. **改写后端API代码**：提供了一个示例，展示如何将JWT用户认证与授权集成到持久化数据存储的图书管理系统后端API中。1. **请求端代码**：展示了如何使用**Python**的**requests**库发送带有JWT**令牌**的请求来获取受保护的数据，并在访问令牌过期时自动刷新令牌。
总的来说，这篇文章为小菜提供了使用**JWT**进行用户认证和授权的详细指南。
