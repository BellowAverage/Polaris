
--- 
title:  【实战Flask API项目指南】之六 数据库集成 SQLAlchemy 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/b9ed9b5029e8ee68a2fcf0592b634527.png" alt="">

## 实战Flask API项目指南之 数据库集成

本系列文章将带你深入探索**实战Flask API项目指南**，通过跟随小菜的学习之旅，你将逐步掌握 `Flask` 在实际项目中的应用。让我们一起踏上这个精彩的学习之旅吧！

## 前言

在上一篇文章中，我们实现了一个 图书馆里系统API的后端，小菜觉得美中不足的是它使用一个 **Python**的列表用于存储图书的信息，是一个 **本地版图书管理系统后端API**。重新启动程序图书的数据就会丢失了。所以这节，我们将用上数据库来帮助小菜解决这一痛点，实现持久化数据存储。

当小菜踏入`Flask`后端开发的世界时，数据库是存储和管理数据的关键。

`Flask`并没有内置数据库功能，但是提供了扩展机制，可以方便地集成第三方数据库库。本文将介绍如何在 `Flask` 项目中集成**SQLAlchemy**，这是一个流行的**Python ORM**库。 我们将会在上一节课的基础上改写，让读者朋友们了解如何在 `Flask`应用中集成数据库。

<font color="red" size="3">注意：本文直接直接上代码，干货满满。</font>

## SQLAlchemy

### 1. 安装依赖

在`Flask` 中，可以使用各种数据库，如SQLite、MySQL、PostgreSQL等。首先，需要安装所需的数据库驱动库，例如`flask-sqlalchemy`用于集成 **SQLAlchemy**。

在使用 **SQLAlchemy** 进行数据库操作时，大部分操作是相似的，无论使用哪种数据库类型。(本文使用的是 **MYSQL**)

首先我们需要安装对应的依赖库，使用以下命令。

```
pip install flask-sqlalchemy flask-mysqldb

```

### 2. 配置数据库

在 `Flask` 应用中配置数据库连接信息。在应用的配置中，添加数据库的连接字符串。
- 确保将`username`、`password`、`localhost`和`flask`替换为自己的**MySQL**数据库的用户名、密码、主机和数据库名称。
```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# mysql示例
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/database'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/flask'


db = SQLAlchemy(app)

```

### 3. 定义数据模型

使用**SQLAlchemy**，可以定义数据模型作为 **Python** 类。每个类对应一个表，类的属性对应表中的列。数据模型是数据库中表格的抽象表示，它定义了表格的结构和字段。

在下面代码中，定义了一个名为`Book`的数据模型，它有三列
-  `book_id` 字段作为主键，用作主键（**primary key**）,唯一的，不允许为空 -  `title` 字段表示书籍的标题，字符串类型，最大长度为100字符，不允许为空 -  `author` 字段表示书籍的作者，字符串类型，最大长度为50字符，不允许为空 -  因为在我们的案例中，数据表只需要这三列。 
```
class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)

```

附上**SQLAlchemy**中常用的列设置选项：

|选项|描述
|------
|`primary_key=True`|将列标记为主键，用于唯一标识每行数据。
|`nullable=False`|指定列不允许为空值。
|`unique=True`|确保列中的值是唯一的，不允许重复值。
|`default=&lt;value&gt;`|为列设置默认值，如果插入数据时未提供值，则使用默认值。
|`index=True`|创建列的索引，以提高检索性能。
|`autoincrement=True`|自动生成递增的值（通常与主键一起使用）。
|`onupdate=&lt;value&gt;`|在更新行时设置列的值为指定的值。
|`server_default=&lt;value&gt;`|设置列的服务器默认值，通常在数据库层面实现。

### 4. 常用数据库操作

当使用**SQLAlchemy**时，有许多常用的数据库操作方法，用于执行CRUD（创建、读取、更新、删除）操作。以下是一些常用的**SQLAlchemy**操作方法示例：

请注意，这些示例假定你已经正确配置了SQLAlchemy和数据库连接。
<li> **创建数据（Create）**： <pre><code class="prism language-python"># 创建一个新对象并将其添加到数据库中
new_book = Book(title="Sample Book", author="John Doe")
db.session.add(new_book)
db.session.commit()
</code></pre> </li><li> **读取数据（Read）**： <pre><code class="prism language-python"># 查询所有书籍
books = Book.query.all()

# 根据条件查询书籍
specific_book = Book.query.filter_by(title="Sample Book").first()
</code></pre> </li><li> **更新数据（Update）**： <pre><code class="prism language-python"># 查询要更新的对象
book_to_update = Book.query.filter_by(title="Sample Book").first()

# 更新对象的属性
book_to_update.author = "New Author"
db.session.commit()
</code></pre> </li><li> **删除数据（Delete）**： <pre><code class="prism language-python"># 查询要删除的对象
book_to_delete = Book.query.filter_by(title="Sample Book").first()

# 从数据库中删除对象
db.session.delete(book_to_delete)
db.session.commit()
</code></pre> </li><li> **过滤和排序（Filter and Sort）**： <pre><code class="prism language-python"># 查询所有作者是"John Doe"的书籍
johns_books = Book.query.filter_by(author="John Doe").all()

# 查询前5本书籍并按书名升序排列
top_books = Book.query.order_by(Book.title).limit(5).all()
</code></pre> </li><li> **聚合和统计（Aggregate and Count）**： <pre><code class="prism language-python"># 计算书籍总数
book_count = Book.query.count()

# 计算不同作者的书籍数量
author_book_count = db.session.query(Book.author, db.func.count(Book.book_id)).group_by(Book.author).all()
</code></pre> </li>
在**SQLAlchemy**中常用的操作及其描述：

|操作|描述
|------
|定义数据模型|使用`db.Model`定义数据模型，并定义字段及其属性。
|创建数据表|使用`db.create_all()`创建定义的数据模型对应的数据表。
|查询数据|使用`db.session.query()`创建查询对象，并添加查询条件。
|插入数据|使用`db.session.add()`添加新数据对象，并提交更改。
|更新数据|获取数据对象，修改属性后使用`db.session.commit()`提交更改。
|删除数据|使用`db.session.delete()`添加要删除的数据对象，并提交更改。
|过滤条件|在查询中使用`filter`、`filter_by`等方法添加过滤条件。
|排序|使用`order_by`方法指定查询结果的排序方式。
|限制数量|使用`limit`和`offset`限制查询结果的数量和偏移量。
|聚合和统计|使用`func`函数进行聚合和统计操作，如`func.count()`。
|关联表查询|使用`relationship`定义关联关系，使用`join`进行关联查询。
|事务管理|使用`db.session.begin()`开始事务，使用`commit`提交更改，或`rollback`回滚更改。
|批量操作|使用`db.session.bulk_insert_mappings()`进行批量插入，使用`db.session.bulk_update_mappings()`进行批量更新。
|连接查询|使用`join`进行多表连接查询，使用`select_from`、`outerjoin`等方法进行不同类型的连接。
|原始SQL查询|使用`db.session.execute()`执行原始的SQL查询。

### 5. 创建数据表

在`app.py`的末尾，添加以下代码来创建数据表：

在**Flask-SQLAlchemy**中，可以使用`db.create_all()`来创建所有定义的数据模型对应的数据表。在`app.py`的末尾，添加以下代码：

```
db.create_all()

```

但有时候会抛出一个 `RuntimeError` 的异常，

<img src="https://img-blog.csdnimg.cn/img_convert/611fa2c35105c1be86cbb8ac9c99e7ba.png" alt="">

提示说在应用程序上下文之外工作，所以在前面添加 `with app.app_context()`，如下所示：

```
# 创建数据表
with app.app_context():
    db.create_all()  # 或其他需要应用上下文的操作

```

### 6. 持久化数据存储的图书管理系统

这里将会在上一节课 **本地版图书管理系统** 的基础上，使用**SQLAlchemy** 改写成持久化数据存储的图书管理系统。

**上代码**

```
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask import (Flask, jsonify, request)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/flask'  # 替换为你的数据库 URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 定义Book模型类
class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)


# 获取所有书籍
@app.route("/books", methods=["GET"])
def get_all_books():
    books = Book.query.all()
    book_list = [{<!-- -->"id": book.book_id, "title": book.title, "author": book.author} for book in books]
    return jsonify(book_list), 200


# 获取特定书籍
@app.route("/books/&lt;int:book_id&gt;", methods=["GET"])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify({<!-- -->"id": book.book_id, "title": book.title, "author": book.author}), 200
    return jsonify({<!-- -->"error": "Book not found."}), 404


# 创建新书籍
@app.route("/books", methods=["POST"])
def create_book():
    data = request.json
    new_book = Book(title=data["title"], author=data["author"])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({<!-- -->"id": new_book.book_id, "title": new_book.title, "author": new_book.author}), 201


# 更新书籍信息
@app.route("/books/&lt;int:book_id&gt;", methods=["PUT"])
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

现在，小菜可以使用GET、POST、PUT和DELETE请求来访问API端点，并对图书数据进行操作。这个例子演示了如何在 `Flask` 应用中集成数据库、定义数据模型、执行数据库操作以及使用API端点来操作数据。这将帮助小菜更好地理解 `Flask` 中的数据库集成。

### 总结

这篇文章深入探讨了在`Flask`应用中集成数据库的关键步骤，通过引入**SQLAlchemy**这一流行的**Python ORM**库，实现了数据的持久化存储。文章首先介绍了安装依赖以及配置数据库的过程，然细讲解了如何定义数据模型以及常见的数据库操作方法。重点强调了如何使用**Flask-SQLAlchemy**扩展来简化数据库交互的过程。

通过以上步骤，小菜已经成功地在 `Flask` 应用中集成了**MySQL**数据库，并实现了图书的增删改查等操作。小菜获得了以下知识：
- 如何配置`Flask`应用以连接数据库。- 如何使用**SQLAlchemy**定义数据模型和表格结构。- 如何执行常见的数据库操作，包括创建、读取、更新和删除数据。- 如何使用**Flask-SQLAlchemy**扩展简化数据库交互。
通过本文的学习，小菜已经理解了`Flask`中数据库集成和操作，这为后面小菜需要实现后端API平台打下了扎实的基础！
