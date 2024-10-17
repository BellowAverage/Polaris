
--- 
title:  kingbase客户端工具安装和使用 
tags: []
categories: [] 

---
## 一、kingbase客户端工具简介

  kingbase客户端工具是人大金仓提供的连接KES数据库的图形化客户端工具。它是基于JAVA语言开发的能运行在不同操作系统平台上的图形工具，用于访问、配置、控制和管理 KingbaseES 数据库服务器。它不仅可以用于开发工程师进行数据库项目开发，还为DBA提供了丰富的运维功能，其中包括：
- 管理和配置KingbaseES数据库服务器。- 管理各种KingbaseES数据库对象。- 进行KingbaseES数据库的安全管理。- 调用查询分析器执行和测试SQL语句。
## 二、客户端工具下载及安装

### 1、下载软件包

  登录https://www.kingbase.com.cn/rjcxxz/index.htm下载安装包，实际上客户端工具和数据库软件包是同一个软件包，就是我们在安装的时候可以选择只安装客户端及完成客户端工具的安装。客户端工具一般用于window客户端，我们这里选择x86架构的window版本进行下载。 <img src="https://img-blog.csdnimg.cn/ddbe74af18e04d38adf82a4b986ed799.png" alt="在这里插入图片描述">

### 2、安装软件包

  将ISO软件包使用UltraISO这类的工具打开，加载到光驱中。然后双机exe程序开始安装。 <img src="https://img-blog.csdnimg.cn/c65bf262d1bf49638b0e553785a61a3b.png" alt="在这里插入图片描述">

### 3、选择语言

  默认是简体中文，只支持英文和简体中文语言。 <img src="https://img-blog.csdnimg.cn/95d48c4b0e5e4f4cb524ffb864824eb8.png" alt="在这里插入图片描述">

### 4、选择客户端安装

  kingbase数据库安装和客户端安装步骤基本上是一致的，就是在选择安装集的时候的选择后有所区别。虽然是客户端安装，所需磁盘空间还是需要3G+，所以如果安装在C盘我们需要预留足够的磁盘空间。 <img src="https://img-blog.csdnimg.cn/b74f688a068c49c198b89bd9d1fb6e6b.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2ae08dd9c7e948acaf81e5ba2e29c099.png" alt="在这里插入图片描述">

### 5、完成安装

  看到如下界面就说明安装完成了。 <img src="https://img-blog.csdnimg.cn/7cc61287e8dc46bfac1a108a2a5fbff6.png" alt="在这里插入图片描述">

### 5、启动工具

  启动项中选择数据库开发管理工具，点击启动。实际上这3个都是kingbase的客户端工具，这里我们只介绍数据库开发管理工具。 <img src="https://img-blog.csdnimg.cn/d7f43e6c516c4b1ba480d066022be9e7.png" alt="在这里插入图片描述">

## 三、使用简介

  kingbase客户端主要有数据库、表空间、安全性、管理、备份五大功能：

<th align="left">类别</th><th align="left">常用功能</th>
|------
<td align="left">数据库</td><td align="left">1)、查看数据库、模式、表和相关PL/SQL对象的定义2)、对象的创建、修改、删除3)、表数据的查看和导入导出</td>
<td align="left">表空间</td><td align="left">1)、创建表空间2)、修改表空间3)、删除表空间</td>
<td align="left">安全性</td><td align="left">1)、创建用户和角色2)、修改用户和角色3)、为用户和角色分配权限</td>
<td align="left">管理</td><td align="left">1)、查看和修改数据库参数2)、查看和断开连接到数据库的会话3)、查看数据库资源占用</td>
<td align="left">备份</td><td align="left">1)、整库逻辑备份和还原2)、对象级逻辑备份和还原</td>

### 1、工具主页展示

<img src="https://img-blog.csdnimg.cn/d0445bd5d1664bb7a8706e432ad4d6fe.png" alt="在这里插入图片描述">

### 2、新建数据库连接

  点击连接按钮，弹窗选择kingbase数据库类型后进入连接设置窗口，填写我们需要连接的数据库的IP地址、端口号、用户名、密码、连接名等信息。填写完成后我们可以先点击测试链接进行验证，验证通过点击完成即可。 <img src="https://img-blog.csdnimg.cn/ed175af7e93f48c5bb1a3abe4921d0e4.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/1185e8cc6bcb440db2cc06947c13160f.png" alt="在这里插入图片描述">

### 3、创建数据库

  选择导航栏中的数据库，右键可以新建数据库。输入数据库名称、属主、编码这些基本参数后即可，可以查看DDL项，这就是界面操作转换为sql语句的内存，我们在数据库命令行界面实际上执行的sql语句。点击确定后就完成了数据库的创建。 <img src="https://img-blog.csdnimg.cn/c767d94469c14b22ba217aa120d77f52.png" alt="在这里插入图片描述">   创建后的数据库我们可以通过右键进行编辑，右键编辑的内容只有属主这一项。 <img src="https://img-blog.csdnimg.cn/fbb20a8574cd4f11bab91743fa9e7bba.png" alt="在这里插入图片描述">

### 4、新建表空间

  在表空间项下可以创建表空间，默认存在sys_default、sys_global、sysaudit三个表空间。后续我们可以通过右键编辑表空间的属主，当前我们创建普通用户，临时设置表空间属主是system用户。

>  
 [root@s166 v8]# mkdir wuhsdata [root@s166 v8]# chown -R kingbase.kingbase wuhsdata/ 


<img src="https://img-blog.csdnimg.cn/934058a0202041a6b78a1f4cf5c45955.png" alt="在这里插入图片描述">

### 5、新建用户

  新建一个用户我们需要完成基本属性、系统权限、对象权限的设置，当然基本属性是必须设置的，权限这些如果没有设置则表示没有相关权限。系统权限设置中如果是作为普通用户使用我们赋予其login权限即可，如果是作为DBA账户使用则还需要赋予创建数据库、创建角色、超级权限等相关权限。对象权限是针对数据库和表权限的设置，可以在数据库、模式、表这些不同层级单独设置。 <img src="https://img-blog.csdnimg.cn/eb60c0eaf01b43b4a9ac445a9af33215.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f6e7078140534dfdb32ac7754d58a0a2.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/908a5bfee238452681b1a8d321731ead.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c0d9a0e383b34e3ab4bcd642c2fc51e1.png" alt="在这里插入图片描述">

### 6、创建表

  依次点击数据库–&gt;模式–&gt;public–&gt;表，右键新建表。在基本属性中设置表的名称、所属表空间、字段信息等。在约束菜单下设置主键、唯一键；如果还需要设置外键、索引都在对应属性窗口设置。 <img src="https://img-blog.csdnimg.cn/8fce3cac69ef4785ba53311523312694.png" alt="在这里插入图片描述">

### 7、数据库管理

  数据库管理主要是配置数据库参数、会话管理、锁管理，这个需要连接账户具有系统权限才可以操作。 <img src="https://img-blog.csdnimg.cn/0cb931fcdfdf45cabf641204fd2700fb.png" alt="在这里插入图片描述">

### 8、新建查询

  新建查询实际上是开启了一个命令行窗口栏，我们不仅可以执行查询，也可以其他任何的DDL SQL语句。如下示例我们使用新建查询往表bookname中插入了2条数据。

<img src="https://img-blog.csdnimg.cn/a28930e20c55451bb2a0791c67a96cc4.png" alt="在这里插入图片描述">

### 9、系统备份和还原

  工具里的备份功能包括逻辑备份和还原，逻辑备份时勾选我们需要备份的数据库，选择备份类型备份即可，这里的备份支持备份包括二进制和sql文件。逻辑还原要求是备份的二进制文件，如果是sql文件需要使用ksql命令工具进行还原。还原的时候支持全部还原和部分还原。逻辑备份和还原实际上执行的是sys_dump和sys_restore命令。 <img src="https://img-blog.csdnimg.cn/4202fee69a744964a42ed5221d8fd3be.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/fb3ad05a40be435693b0d8430cc33d4f.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/8b6fff390b30465ba7b1db36f0850792.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/04209d3613d24e5e9f601623862ab038.png" alt="在这里插入图片描述">
