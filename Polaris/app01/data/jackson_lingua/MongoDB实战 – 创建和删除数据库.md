
--- 
title:  MongoDB实战 – 创建和删除数据库 
tags: []
categories: [] 

---
## MongoDB实战 – 创建和删除数据库

### MongoDB In Action - Create and Drop Databases

By Jackson@ML

根据前文介绍，MongoDB安装完毕后，可以有不同方法进行访问。

本文简要介绍在Windows操作系统中，如何使用MongoDB Shell进行文档数据库的基本操作，并以实例加以说明。

#### 1. 访问MongoDB的途径

我们一道启动MongoDB的实战应用吧。

无论是否由MongoDB Atlas预配置MongoDB数据库，都可以尝试使用这类文档型数据库。

根据用户的首选项，对于如何创建数据库并与之交互，有以下各种途径（或者叫选项）：

1） 通过**MonngoDB Compass**， 这是官方跨平台图形用户界面（GUI）; 2） 通过Web浏览器和**MongoDB Atlas Web用户界面**。此接口与MongoDB Compass非常相似； 3） 通过命令行工具**MongoDB Shell**，可以进行快捷的命令行操作； 4） 通过**编程语言（例如：Node.js, Python, Java）、API或IDE**（即Visual Studio Code的extension, Python MongoDB驱动程序、node.js MongoDB驱动程序、Java MongoDB驱动程序）

#### 2. 创建集合

前述的各种交互选项，用户可以自由选择。

本文就MongoDB Shell进行介绍。

创建集合是数据库的根本，用Shell命令执行简易直观。例如在默认数据库test中创建集合（collection）:

```
test&gt; db.createCollection('JacksonCollection')
{
   <!-- --> ok: 1 }

```

在此基础上，增加
