
--- 
title:  TinyDB-- 一个纯Python编写的轻量级数据库 
tags: []
categories: [] 

---
TinyDB 是一个纯 Python 编写的轻量级数据库，一共只有1800行代码，没有外部依赖项。

TinyDB的目标是降低小型 Python 应用程序使用数据库的难度，对于一些简单程序而言与其用 SQL 数据库，不如就用TinyDB， 因为它有如下特点：

轻便：当前源代码有 1800 行代码（大约 40% 的文档）和 1600 行测试代码。

可随意迁移：在当前文件夹下生成数据库文件，不需要任何服务，可以随意迁移。

简单：TinyDB 通过提供简单干净的 API 使得用户易于使用。

用纯 Python 编写：TinyDB 既不需要外部服务器，也不需要任何来自 PyPI 的依赖项。

适用于 Python 3.6+ 和 PyPy3：TinyDB 适用于所有现代版本的 Python 和 PyPy。

强大的可扩展性：您可以通过编写中间件修改存储的行为来轻松扩展 TinyDB。

100% 测试覆盖率：无需解释。

**1.准备**

开始之前，需要先安装它

pip install tinydb

**2.简单的增删改查示例**

初始化一个DB文件：

from tinydb import TinyDB db = TinyDB('db.json') 这样就在当前文件夹下生成了一个名为 `db.json` 的数据库文件。

**往里面插入数据：**

from tinydb import TinyDB db = TinyDB('db.json') db
