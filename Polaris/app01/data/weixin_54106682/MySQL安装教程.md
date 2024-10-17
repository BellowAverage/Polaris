
--- 
title:  MySQL安装教程 
tags: []
categories: [] 

---
**目录**







### 下载地址

官方下载地址：

### 安装步骤

①双击msi安装程序，进入如下界面，点击custom，点击next

<img alt="" height="1186" src="https://img-blog.csdnimg.cn/30924a1dcdc14da5b6270f91ec385124.png" width="1200">

②选择自己要安装的组件 MySQL Server：是数据库服务，要安装这个 。 MySQL Workbench：一款MySQL的ER/数据库建模工具。 MySQL for Visual Studio：你要是使用VS编程，并且要用VS来连接数据库进行表管理就需要装这个。 MySQL for Excel：是一个Excel插件，能让我们在Microsoft excel中处理MySQL数据。 MySQL Notifier ：是一款 MySQL 数据库的辅助工具。它可以在系统任务栏通知区域（系统托盘）处驻留图标，用于快捷监视、更改服务器实例（服务）的状态。同时，也可以与一些图形化管理工具（如 MySQL Workbench）集成使用。一般用不到。 MySQL Shell：是MySQL Server的高级客户端和代码编辑器。 MySQL Router：一般用不到。 MySQL Connector ：一些连接mysql的驱动包。 MySQL Documentation ：一些mysql的官方文档。

windows x64和x86最主要的区别：windows x64是指64位的操作系统，windows x86是指32位的操作系统。所以如果你电脑拥有超过4G的内存，则建议安装64位的操作系统，这是这两者最大的区别.<img alt="" height="1186" src="https://img-blog.csdnimg.cn/24c00b2f0b884524991ace9c9ffc9ce0.png" width="1200">

③自定义安装路径

√首先点击MySQL Server--&gt;advanced option--&gt;设置MySQL Server安装路径

<img alt="" height="1186" src="https://img-blog.csdnimg.cn/0dcc80d507f84c7783a0bf17d419ad35.png" width="1200">

 √之后点击Connector/Python--&gt;advanced option--&gt;设置Connector/Python安装路径

<img alt="" height="1186" src="https://img-blog.csdnimg.cn/6526d750f34c4dfca8b17fa4a8d3b512.png" width="1200">

√ 之后点击MySQL Shell--&gt;advanced option--&gt;设置MySQL Shell安装路径

<img alt="" height="1186" src="https://img-blog.csdnimg.cn/b56af93f3c124c95873e54df63bab934.png" width="1200">

④ready to download

<img alt="" height="1186" src="https://img-blog.csdnimg.cn/ebac60aa31d94fc383a00e40a9292a11.png" width="1200">

⑤ready to install

<img alt="" height="1186" src="https://img-blog.csdnimg.cn/63fed19d453e41e1a34d0a6f3fc19f90.png" width="1200">

⑥之后一直点击next即可，直至出现如下界面，需要设置数据库的密码（友情提示：最好找个地方记下来~）

<img alt="" height="1186" src="https://img-blog.csdnimg.cn/75321f1df1074d6f82332f6c85d6b785.png" width="1200">

⑦next即可【可根据个人意愿对服务名称进行修改】

<img alt="" height="1186" src="https://img-blog.csdnimg.cn/4f930954833244f699cafb851d453750.png" width="1200"> ⑧点击execute

<img alt="" height="1186" src="https://img-blog.csdnimg.cn/22ab4b4036e0419289202aab41f17e52.png" width="1200">

⑨完成

### <img alt="" height="1186" src="https://img-blog.csdnimg.cn/650fcbb7a1f548ba99179bc6d2a58a14.png" width="1200">配置环境变量

#### **为什么需要配置环境变量？**
- 环境变量，代表系统的一个全局搜索路径。- 当你没有配置环境变量的时候，你想要执行某个目录下的某个程序，就必须找到它的具体位置，才能够执行它。- 当不配置环境变量，想要执行某个程序可以吗？当然也是可以的，就拿启动mysql来说，你如果不配置环境变量，就必须在CMD黑窗口中，使用cd命令切换到mysql server下的bin目录下，才可以执行启动。你每次这样启动是不是觉得很麻烦，当你需要经常使用mysql，需要经常执行mysql启动。这就是为什么我们需要配置环境变量的原因。- 当配置了某个环境变量，如果你想要执行某个程序，你可以在任何路径下，执行这个程序。首先，系统会在当前目录下，搜索是否存在想要执行的某个程序，假如没有，系统会再去系统环境变量中的目录进行一个个搜索，当搜索到了该程序，便会立即执行。
 将MySQL Server安装路径中的bin目录加入path即可。注意：结尾是英文封号<img alt="" height="335" src="https://img-blog.csdnimg.cn/53aac7a4c8b94b56ae59dee26b7a0ad2.png" width="1200">

打开CMD，输入mysql -u root -p ，之后输入密码（123456），出现如下界面，与数据库连接成功

<img alt="" height="505" src="https://img-blog.csdnimg.cn/b616af8e6bce4ad0ab6b0dcc02ce69ef.png" width="1200">
