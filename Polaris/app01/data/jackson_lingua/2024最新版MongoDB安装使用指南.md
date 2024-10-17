
--- 
title:  2024最新版MongoDB安装使用指南 
tags: []
categories: [] 

---
## 2024最新版MongoDB安装使用指南

### Installation and Usage Guide of the Latest MongoDB Community Edition in 2024

By Jackson@ML

>  
 MongoDB is a document database with the scalability and flexibility that you want with the querying and indexing that you need. – mongodb.com 


#### 1. 什么是MongoDB？

MongoDB是什么？确定含义是什么？

该软件官网给出了简洁的答案： **MongoDB是一个文档数据库，具有所需的查询和索引所需的可扩展性和灵活性。**

#### 2. MongoDB可以如何使用？

按照官网的介绍，MongoDB主要有以下两种方式供用户使用：

1） **MongoDB Atlas**，这是MongoDB的云应用，用户只需注册便可以登录使用，免费用户包含高达5GB的云存储空间，以及共享的RAM，永久免费的Sandbox，以及特定的一致性能，高安全性，无限可伸缩性； 2） **MongoDB Server**，MongoDB提供企业版和社区版，都是功能强大的分布式文档数据库。

MongoDB是领先的现代数据库平台，在其上构建应用程序数据平台简便且功能强大。它支持事务性、搜索、分析及移动使用项目，同时采用通用查询接口，便于开发人员进行数据模型构建及定制化数据库程序开发。

#### 3. MongoDB使开发更加容易

MongoDB 的文档模型易于开发人员学习和使用，同时仍提供满足任何规模最复杂需求所需的所有功能。该产品提供 10多种编程语言的驱动程序，并且，MongoDB社区也已经构建了数十种语言供用户查询使用。

#### 4. 下载最新版MongoDB社区版

打开Chrome浏览器，访问MongoDB官网链接：， 如下图：

<img src="https://img-blog.csdnimg.cn/direct/5a6c6252c77d4e91ba1bdc155bbe5dda.png" alt="在这里插入图片描述"> 在主页上方导航栏，点击 **Products** (产品)， 选择 **Try Community Edition**, 点击按钮 **Download**（下载），进入社区版下载页面，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/20393d1a346140d3968ee3cb7de3c6a2.png" alt="在这里插入图片描述"> 进入MongoDB Community （社区版）页面，将鼠标滚动向下，可以看到该社区版Community Server可供下载，点击**Select package** (选择包)，进入下一页。

<img src="https://img-blog.csdnimg.cn/direct/369ef7ba9e4e49da99a1ffcad311d26d.png" alt="在这里插入图片描述"> 鼠标滚轮向下滑动，看到MongoDB Community Edition的下载链接： <img src="https://img-blog.csdnimg.cn/direct/58fc822d93bf41a6be34a7f0c2c22b6e.png" alt="在这里插入图片描述">

出现默认的当前最新版本7.0.5，按照该默认选项（包含平台Windows x64，以及msi类型的安装包），点击Download开始下载。

Chrome浏览器随即进入下载进度，待下载完毕，可以到Windows的下载文件夹中去找该安装包文件。

#### 5. 安装MongoDB Community Edition

带下载完毕，在Windows下载文件夹内，找到 MongoDB安装包文件**mongodb-windows-x86_64-7.0.5-signed.msi**, 双击它启动安装向导。

<img src="https://img-blog.csdnimg.cn/direct/41be2b79d7284bf7a0b6ba72a053d12d.png" alt="在这里插入图片描述"> 点击 Next 进行下一步。

<img src="https://img-blog.csdnimg.cn/direct/93e7a17d2e3c4e9fbf723fdedd31fa1e.png" alt="在这里插入图片描述"> 选中 I accept the terms in the License Agreement (我接受许可证协议条款)， 点击Next进行下一步。 <img src="https://img-blog.csdnimg.cn/direct/dc09522e1e364545ba1d93b2391b29b3.png" alt="在这里插入图片描述"> 在Choose Setup Type （选择安装类型）对话框，点击默认选项 Complete (完整版)，如下图：

<img src="https://img-blog.csdnimg.cn/direct/29f7dc4a61894ce7ad693175fcb98b98.png" alt="在这里插入图片描述"> 由于没有特定需求，因此按照默认选项，点击Next进行下一步。 接下来，提示安装MongoDB Compass， 如下图：

<img src="https://img-blog.csdnimg.cn/direct/56481defd4ab40d585e82425f9323486.png" alt="在这里插入图片描述"> 点击Next继续安装。 <img src="https://img-blog.csdnimg.cn/direct/d4a7fd63ef3d45f7b8ae8e2142d12876.png" alt="在这里插入图片描述"> 点击Install开始安装。 <img src="https://img-blog.csdnimg.cn/direct/f85581887cc94cd98ec2f884c8429225.png" alt="在这里插入图片描述"> 很快安装会结束。

<img src="https://img-blog.csdnimg.cn/direct/2779923fece04af2970d42d4a52994e7.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/direct/3dc2cca0993440489f65bfcfa17b6f57.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/direct/f60bfe584cd648b18a3ea882802c8253.png" alt="在这里插入图片描述"> 安装结束，点击 Finish 结束安装向导。

#### 6. 下载安装MongoDB Shell

MongoDB Shell用来连接和使用MongoDB，是最快捷的方式。

MongoDB是交互式的JavaScript接口，您可以使用Mongo Shell查询和更新数据以及执行管理操作。 Mongo Shell作为MongoDB Server安装的一部分包含在内。

MongoDB还提供mongo shell作为独立软件包。使用这个现代、可扩展的命令行界面轻松查询数据、配置设置和执行其他操作 - 充满了语法突出显示、智能自动完成、上下文帮助和错误消息。

##### 1） 下载MongoDB Shell

打开Chrome浏览器，访问MongoDB Shell官方下载链接： ，如下图所示： <img src="https://img-blog.csdnimg.cn/direct/7327e104a1ea4c2cb9af3dd817c9d6e1.png" alt="在这里插入图片描述"> 鼠标向下滚动，得到MongoDB Shell Download下载链接：

<img src="https://img-blog.csdnimg.cn/direct/6f52a0b776c946e197552512024030e3.png" alt="在这里插入图片描述"> 选择默认版本不2.1.3，选择Package为msi格式（Windows安装包），点击Download进行下载。

##### 2）安装MongoDB Shell

下载完毕，在Windows下载文件夹，找到该安装可执行文件 **mongosh-2.1.3-x64.msi**, 双击启动安装向导。

<img src="https://img-blog.csdnimg.cn/direct/7463f2d9b1dd4601ac2cc90bb8b68aea.png" alt="在这里插入图片描述">

点击Next进行下一步。 <img src="https://img-blog.csdnimg.cn/direct/8449d342c5e2470e90c1fec44ceae831.png" alt="在这里插入图片描述"> 按照默认选项Install just for you(Administrator)（仅为你（管理员）安装），选择默认路径，点击Next进行下一步。

<img src="https://img-blog.csdnimg.cn/direct/4c6a28e6a70c4b1a95fe4e905680a269.png" alt="在这里插入图片描述"> 点击Install进行安装。

<img src="https://img-blog.csdnimg.cn/direct/dd9fad62ef3546ebbd56919a978b89d4.png" alt="在这里插入图片描述"> 很快安装结束，点击Finish退出安装向导。

##### 3）启动MongoDB Shell

打开Windows命令行提示符(cmd), 执行以下命令，运行MongoDB Shell：

```
mongosh

```

出现test&gt;提示符，证明MongoDB Shell运行正常。 <img src="https://img-blog.csdnimg.cn/direct/5dd319994f53458f9bf33d5a1d214aa0.png" alt="在这里插入图片描述"> 当前启动数据库，是默认的test。

使用以下命令，来验证已安装的db列表：

```
test&gt; show dbs
admin   40.00 KiB
config  60.00 KiB
local   40.00 KiB
test    40.00 KiB

```

至此，MongoDB已安装完成，我们也可以使用MongoDB Shell来进行交互式管理了。

技术好文陆续推出，敬请关注。

您的认可，我的动力！ 😃

#### 相关阅读
1. 1. 1. 1. 1. 1. 1. 1. 