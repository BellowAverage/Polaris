
--- 
title:  MongoDB实战 – 用Python访问MongoDB数据库 
tags: []
categories: [] 

---
## MongoDB实战 – 用Python访问MongoDB数据库

### MongoDB in Action – Access MongoDB Databases with Python

By Jackson@ML

>  
 Python语言功能强大众所周知，在数据库管理领域也无所不能。MongoDB是文档数据库，属于NoSQL数据库的一种，在业界也非常有名。 


本文简要介绍用Python如何实现连接和访问MongoDB数据库，希望对广大读者有所帮助。

首先，Python可用于数据库应用程序。由于MongoDB为最受欢迎的NoSQL数据库之一，因此，如何使用及访问它，也备受关注。

#### 1. 获取MongoDB

MongoDB将数据存储在类似JSON的文档中，这使得数据库访问变得异常灵活，它还具备很好的可扩展性。

##### 1）获取途径

用户可以在 https://www.mongodb.com 下载免费的 MongoDB 数据库。或者，注册登录，以开始使用 MongoDB 云服务，https://www.mongodb.com/cloud/atlas。

##### 2）下载安装MongoDB

获取并安装MongoDB数据库，请参看笔者文章：****。本文不再赘述。

本文提供了典型的示例代码，便于通过实验来访问 MongoDB 数据库。

#### 2. 获取PyMongo

使用Python语言访问MongoDB数据库，必须具备PyMongo这个外挂库，这是Python操作MongoDB的driver(驱动)。

为了实现这一目的，需要先下载和安装Python最新版3.12.2。安装步骤参考文章：****。 本文亦不再赘述。

安装好最新版Python 3.12.2后，就具备了Python包管理器pip, 可以用它来安装外挂库PyMongo。

以管理员身份运行命令行提示符(cmd), 如下图：

<img src="https://img-blog.csdnimg.cn/direct/77ad2142a1ee4f24938372c11f260fd3.png" alt="在这里插入图片描述"> 在命令行中运行以下命令：

```
pip install pymongo

```

执行结果如下图所示: <img src="https://img-blog.csdnimg.cn/direct/7734ba703139436bab125f3c72b48f52.png" alt="在这里插入图片描述"> 成功完成安装，所安装的最新版本为PyMongo 4.6.2。

这样一来，MongoDB的驱动就安装好了。

#### 3. 验证PyMongo

打开IDLE交互式命令行，运行以下命令：

```
import pymongo

```

如下图所示： <img src="https://img-blog.csdnimg.cn/direct/c4f9b57f00994e598867382c9a6b18cb.png" alt="在这里插入图片描述"> 说明PyMongo库导入成功！

#### 4. 创建MongoDB数据库

为了在 MongoDB 中创建新的数据库，首先需要创建一个 MongoClient 对象，创建完毕赋值给变量theClient，这就是新的MongoClient对象，然后使用正确的 IP 地址和要创建的数据库的名称(theDatabase)指定连接 URL。

本地主机默认名称为localhost, MongoDB的默认端口号为27107,因此，编写代码如下： （如果数据库不存在，MongoDB将创建数据库，并与之建立连接。）

```
theClient = pymongo.MongoClient("mongodb://localhost:27107/")
theDB = theClient["theDatabase"]

```

运行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/f1ae6e4e06b7400187942589ea152c75.png" alt="在这里插入图片描述"> 没有报错，说明执行成功！

接下来，验证数据库是否存在（即验证新创建的数据库）：

```
print(theClient.list_database_names( ))

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/60b1c6ede3364f7f8c03872ac0a0d069.png" alt="在这里插入图片描述"> 打印输出的结果是出现了四个内置数据库，分别为admin, config, local和test。

#### 5. 验证数据库

上面例子中，print()函数并未得到打印输出结果。

如果需要验证，myDatabase是否存在，则可以使用条件表达式来判断，代码如下：

```
DBList = myClient.list_database_names()
if "myDatabase" in DBList:
print("The database {} exists.".format(myDatabase))

```

#### 6. 建立连接

如果为了简便，在导入pymongo库的时候，将其子模块MongoClient导入，则可以节省代码段长度，简洁引用，从而连接到数据库。

代码示例如下：

```
from pymongo import MongoClient

client = MongoClient()
print(client)

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/4b7d7f7550864498a549d90cd7323076.png" alt="在这里插入图片描述"> 如上例所示，要建立与数据库的连接，
- 首先，需要创建一个 MongoClient 实例。此类为 MongoDB 实例或服务器提供客户端。每个客户端对象都有一个内置连接池，默认情况下，该连接池最多可处理与服务器的一百个连接。
返回到 Python 交互式会话并从 pymongo 导入 MongoClient。
- 然后创建一个客户端对象，以便与当前运行的 MongoDB 实例进行通信。
上述代码建立了与默认本地主机(localhost)端口27107之间的连接。MongoClient采用一系列参数来指定自定义主机、端口号以及其它参数。

如果需要自定义主机和端口号，示例代码如下：

```
client = MongoClient(host="localhost", port=27107)

```

当用户需要与MongoDB默认设置不同的主机和端口号时，这样写代码很方便；当然，还可以使用MongoDB URI格式，代码如下：

```
client = MongoClient(“mongodb://localhost:27107”)

```

以上示例都可以提供相同的客户端设置来连接当前的MongoDB实例。选择哪个取决于用户的具体需求。

将MongoClient实例化后，就可以使用其实例来引用对特定数据库的连接。

技术好文陆续推出，敬请关注。

您的认可，我的动力！ 😃
