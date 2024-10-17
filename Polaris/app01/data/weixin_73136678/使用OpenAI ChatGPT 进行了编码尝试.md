
--- 
title:  使用OpenAI ChatGPT 进行了编码尝试 
tags: []
categories: [] 

---
<img alt="" src="https://img-blog.csdnimg.cn/img_convert/368416be21b9cc4720468a18c5ceab21.webp?x-oss-process=image/format,png">

ChatGPT 是一种以类似聊天的方式进行交互的人工智能网络，从名字上看起来像是另一个“聊天机器人”，但实际上已经远超聊天的范畴了，当要求它编写一些代码时，结果相等震撼，它可以写出一些意想不到的连贯代码，而这些代码对于开发者很有启发。

开始要求它使用 JavaScript 编写一个散列（HASH）密码的函数。具体一点就是编写一个 JavaScript 函数，它接受密码的字符串输入并输出散列（HASH）密码。

```
function hashPassword(password) {
    return crypto.createHash("sha256").update(password).digest("hex");
}
复制代码
```

然后逐步提高编码的难度，实现一些更加符合项目开发的需求，于是输入：

>  
 编写一个在请求正文中包含用户名和密码的 Express 路由处理程序，对密码进行哈希处理，在 MySQL 数据库中查找现有用户并检查哈希后的密码是否匹配。 


```
const express = require("express");
const bcrypt = require("bcrypt");
const mysql = require("mysql");

// 创建 MySQL 数据库连接
const db = mysql.creat
```
