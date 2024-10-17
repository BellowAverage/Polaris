
--- 
title:  【实战Flask API项目指南】之五 RESTful API设计 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/dbc375e01a1dc1e45ed2a6a91dccd105.png" alt="">

## 实战Flask API项目指南之 RESTful API设计

本系列文章将带你深入探索**实战Flask API项目指南**，通过跟随小菜的学习之旅，你将逐步掌握 `Flask` 在实际项目中的应用。让我们一起踏上这个精彩的学习之旅吧！

## 前言

当小菜踏入`Flask`后端开发的世界时，遵循**RESTful API**规范尤为重要。

**RESTful API**（Representational State Transfer）是一种设计规范，用于构建可扩展、灵活且易于维护的Web服务。它强调使用HTTP方法来操作资源，并将资源的状态以及操作结果表示为数据。接下来让我们更详细地了解**RESTful API**的核心概念和实际设计。

**RESTful API**具体的内容参考以下链接：
-   -   -   
<font color="red" size="3">注意：本文直接直接上代码，干货满满。</font>

## 为什么使用**RESTful API**

RESTful 架构可以充分的利用 HTTP 协议的各种功能，是 HTTP 协议的最佳实践

**RESTful API** 是一种软件架构风格、设计风格，可以让软件更加清晰，更简洁，更有层次，可维护性更好

## **RESTful API** 设计

### 请求设计

<img src="https://img-blog.csdnimg.cn/img_convert/89abc869cc06fd6a0d93f57ead57ed33.png" alt="">

### 响应设计

<img src="https://img-blog.csdnimg.cn/img_convert/94b585bc820cce834a9412e7466d8943.png" alt="">

## 实践

理论说完了，是很枯燥的。下面开始写代码。

这里参考该  文章来设计一个包含 **RESTful API**的基本要素的图书管理系统后端API平台。

### 示例代码

看以下代码，这份代码体现了**RESTful API**设计的一些重要原则。

下面会对它进行解析。

```
from flask import (Flask, jsonify, request)

app = Flask(__name__)

# 示例数据，用于模拟书籍数据库
books = [
    {<!-- -->"id": 1, "title": "Book 1", "author": "Frica01"},
    {<!-- -->"id": 2, "title": "Book 2", "author": "Frica02"}
]


# 获取所有书籍
@app.route("/books", methods=["GET"])
def get_all_books():
    return jsonify(books), 200


# 获取特定书籍
@app.route("/books/&lt;int:book_id&gt;", methods=["GET"])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book), 200
    return jsonify({<!-- -->"error": "Book not found."}), 404


# 创建新书籍
@app.route("/books", methods=["POST"])
def create_book():
    new_book = {<!-- -->"id": len(books) + 1, "title": request.json.get("title")}
    books.append(new_book)
    return jsonify(new_book), 201


# 更新书籍信息
@app.route("/books/&lt;int:book_id&gt;", methods=["PUT"])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        book["title"] = request.json.get("title")
        return jsonify(book), 200
    return jsonify({<!-- -->"error": "Book not found."}), 404


# 删除书籍
@app.route("/books/&lt;int:book_id&gt;", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)


```

### RESTful API的体现

#### 1. URL

如上面文章所说，**URL**的设计是动词+宾语，如`GET /books`这个命令，`GET`是动词， `books`是宾语；
- 动词指的是HTTP方法，对应**CRUD**操作
上面的图书管理系统的API，使用如下的**URL**来表示书籍资源：
- 获取所有书籍：`GET /books`- 获取特定书籍：`GET /books/{book_id}`- 创建新书籍：`POST /books`- 更新书籍信息：`PUT /books/{book_id}`- 删除书籍：`DELETE /books/{book_id}`
#### 2. HTTP方法

**RESTful API**使用HTTP方法来操作资源，这与**CRUD**（Create、Read、Update、Delete）操作相对应。
- GET：用于获取资源的信息。- POST：用于在服务器上创建新资源。- PUT：用于更新现有资源，或创建/替换资源。- DELETE：用于删除资源。
例如，获取特定书籍信息的请求通过**HTTP GET**方法发起：

```
GET /books/9527

```

#### 3. 状态码

客户端的每一次请求，服务器都必须给出回应。回应包括 HTTP 状态码和数据两部分。

HTTP 状态码就是一个三位数，分成五个类别。
- 具体的还可以细分，看这里：
|状态码|含义
|------
|1xx|相关信息
|2xx|操作成功
|3xx|重定向
|4xx|客户端错误
|5xx|服务器错误

这些是一些常见的 HTTP 状态码，服务器通常使用这些状态码来指示请求的处理结果，以便客户端能够根据状态码采取适当的操作。

通过合适的状态码，API可以更清晰地传达操作结果。

#### 4. 服务器响应

**RESTful API**通常使用JSON（JavaScript Object Notation）作为数据格式，以便在不同应用之间进行数据交换。JSON是一种轻量级、易于读写的数据格式，适合在Web应用中传输数据。

API返回的数据格式，应该是一个 JSON 对象，因为这样才能返回标准的结构化数据。所以，服务器回应的 **HTTP** 头的 `Content-Type` 属性要设为`application/json`。

在 `Flask`中 `jsonify` 函数会自动将数据转换为 JSON 格式，并设置 `Content-Type` 头为 `application/json`。

```
GET /books/9527 HTTP/1.1
Accept: application/json

```

**成功返回：**

```
{<!-- -->
    "id": 9527,
    "title": "Sample Book",
    "author": "John Doe"
}

```

**失败返回：**

```
{<!-- -->
    'error': 'Book not found.'
}

```

#### 5. 汇总

这份代码已经包含了**RESTful API**的基本要素：
1.  **资源与URL**：每个API端点对应一个资源，如 `/books` 表示所有书籍资源，`/books/&lt;int:book_id&gt;` 表示特定书籍资源。 1.  **HTTP方法**：不同HTTP方法对应不同操作，如 `GET` 用于获取资源，`POST` 用于创建资源，`PUT` 用于更新资源，`DELETE` 用于删除资源。 1.  **数据格式**：API使用JSON格式来表示数据，例如使用 `jsonify` 来构建响应。 1.  **状态码**：合适的HTTP状态码，如 `200` 表示请求成功，`201` 表示资源创建成功，`404` 表示资源未找到，`204` 表示无内容响应。 
这些份代码遵循了**RESTful API**的设计原则，使API更易于理解、扩展和维护。

### 总结

本文详细介绍了**RESTful API**的设计原则，并通过一个 `Flask` 后端开发的图书管理系统示例，展示了如何在实际代码中应用这些原则。

文章从URL、HTTP方法、状态码和服务器响应四个角度，解析了示例代码中的**RESTful API**设计。
- 在**URL**设计中，每个API端点对应一个资源，使得URL的结构清晰、直观。- **HTTP**方法则用于表示对资源的不同操作，如GET用于获取资源，POST用于创建资源等；- 状态码用于表示请求的结果，如200表示请求成功，404表示请求的资源未找到等；- 服务器响应通常包含了请求的结果，当请求成功时或失败时候，服务器会返回对应的 **JSON** 对象。
总的来说，遵循**RESTful API**设计原则，可以使API的使用更加直观、易于理解，同时也使得API的维护和扩展更加方便。

通过本文的学习，小菜已经学会构建出易于维护和使用的API，为他开发后端平台**API** 打下了扎实的基础。
