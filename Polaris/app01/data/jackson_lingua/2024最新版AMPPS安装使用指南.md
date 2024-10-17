
--- 
title:  2024最新版AMPPS安装使用指南 
tags: []
categories: [] 

---
## 2024最新版AMPPS安装使用指南

### Installation and Usage Guide to the Latest AMPPS in 2024

By Jackson@ML

#### 1. 部署开发服务器的必要性

在网络应用程序开发过程中，常常需要将代码在服务器端测试；只有这样，才能评估该程序到底是否符合用户需求，是否能够达到预定的开发目标。

当今时代，宽带已经遍布办公室和家庭，但是，即便是无处不在的互联网连接，不断发生的上传及更新也会极大地影响开发效率和进度。

同时，网站应用的展现，需要不断地测试、修改及再测试等，这种频繁发生的动作，如果一开始就出现在互联网，那么，就会带来诸多问题。因此，相对独立的测试站点部署，也就是本地开发服务器的搭建，就显得至关重要。

前文所指的服务器端，可以是用户喜欢的浏览器，比如Google Chrome, Microsoft Edge, Mozilla Firefox, Opera, 或者Safari。 用户发布产品之前，需要在所有浏览器和平台中一一测试，以确保Web应用功能达到预期，同时运行稳定。

#### 2. WAMP与LAMP

**WAMP**是 **Windows, Apache, MySQL和PHP**的缩写，意思是运行于Windows系统的，用PHP作为WEB开发语言，搭建可用的Apache Web Server同时能够运行MySQL数据库服务等Web应用开发平台。

LAMP则是Linux, Apache, MySQL和PHP的缩写，与上述web开发平台类似，只是运行于Linux操作系统之上。

此外，还有个缩写名词叫MAMP，是Mac/macOS, Apache, MySQL和PHP的缩写，意思是运行于Mac/macOS操作系统的Web应用开发平台。

#### 3. 安装AMPPS

##### 1) 获取AMPPS

WAMP服务器在现实中有好几个，其功能一致，但配置略有不同。在免费的开源选项中，AMPPS也许是最好的选择之一。

打开Chrome浏览器，访问AMPPS官网链接： 如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/70257204fccc4570972b6c4be008078b.png" alt="在这里插入图片描述"> 点击页面中央的Download，进入下载页面。

<img src="https://img-blog.csdnimg.cn/direct/56748110408d4db0ad7525fd32cfa6d4.png" alt="在这里插入图片描述"> 由于在Windows系统实战，因此点击页面右侧Windows下方的Download按钮。

<img src="https://img-blog.csdnimg.cn/direct/f2e5e57ad8a64c41a0e6cf1b689998e6.png" alt="在这里插入图片描述">

此时，弹出一个Download AMPPS对话框，要求输入Email，或者在Twitter上推荐。

可以输入Email以便后续收到相关邮件，也可以不予理会（因为这不是必须的）。

稍后，Chrome浏览器开始下载。

##### 2) 安装AMPPS

下载完毕，在Windows下载文件夹，找到安装包文件 **AMPPS-4.3-x86_64.exe**, 双击它开始安装。

安装向导启动，出现欢迎画面，如下图。

<img src="https://img-blog.csdnimg.cn/direct/ac5d70384ac1417b8d14321f8a1f2660.png" alt="在这里插入图片描述"> 点击Next继续。

<img src="https://img-blog.csdnimg.cn/direct/56f156d442e6426b8ade5079ec581d60.png" alt="在这里插入图片描述"> 选择 **I Accept the agreement**, 点击Next继续。

<img src="https://img-blog.csdnimg.cn/direct/544d8d1c400b44b491c1d360d6c20c24.png" alt="在这里插入图片描述"> 按照默认信息，点击Next进行下一步。

<img src="https://img-blog.csdnimg.cn/direct/f0787233164b4dc7ae4b25742adae54e.png" alt="在这里插入图片描述"> 选择目的安装位置，按照默认安装路径即可，点击Next继续下一步。

<img src="https://img-blog.csdnimg.cn/direct/769c8702b1174c7cba55d6a075ec5a55.png" alt="在这里插入图片描述"> 设置启动文件夹，也按照默认名称Ampps，点击Next继续下一步。

<img src="https://img-blog.csdnimg.cn/direct/a4408bc268ae4d329e7c74fae47a8b6a.png" alt="在这里插入图片描述"> 接下来，选择额外任务，按照默认选项，分别创建桌面快捷方式，快速启动图标，以及开始菜单图标。

点击Next继续下一步。

<img src="https://img-blog.csdnimg.cn/direct/ef49223c2f3249dd8df7fc573fa5e377.png" alt="在这里插入图片描述"> 此时，基本就绪，点击Install开始安装。

<img src="https://img-blog.csdnimg.cn/direct/d944dba12e4d4d5cb267fc925fcec1f5.png" alt="在这里插入图片描述"> 安装向导开始复制文件，很快结束。

<img src="https://img-blog.csdnimg.cn/direct/65bfb6dabd644b5297f95c1b9454791e.png" alt="在这里插入图片描述">

弹出Microsoft Visual C++库安装，点击安装按钮。

<img src="https://img-blog.csdnimg.cn/direct/a0f790e41ae04552a7574342dc9df897.png" alt="在这里插入图片描述">

接下来，安装向导完成，点击Finish退出。

#### 4. 启动AMPPS

在Windows搜索栏，键入关键字AMPPS, 点击启动该软件界面，点击Install， 安装相关套件，完成后，出现以下对话框，提示是否用于专用或者公用网络。

为了安全，选择点击专用网络，并点击允许访问，以启动Apache HTTP Server。

<img src="https://img-blog.csdnimg.cn/direct/6b13695724084c85ba817e15fd8bedbd.png" alt="在这里插入图片描述">

完成后，屏幕右下方弹出对话框，并选择服务启动和停止，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/669e6528df14452cb8753a8d3d493f53.png" alt="在这里插入图片描述"> 看到Apache服务开启，状态时Running(运行中)；且PHP 7.4已安装，状态同样是Running(运行中)。

#### 5. 测试Apache HTTP服务器

为了测试AMPPS安装结果，最重要的是测试Apache HTTP服务器是否运行正常。

此时，从上述安装步骤，了解到Apache，PHP服务已经启动；因此，打开Chrome浏览器，在url里输入本地主机：localhost， 或者IP地址：127.0.0.1， 如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/428c78f38f4643968550c7abf1a83316.png" alt="在这里插入图片描述"> 显示树形目录结构，说明AMPPS安装完成，并且Apache HTTP服务器安装成功！

由于本次安装的集成服务为AMPPS，所以访问该主控界面，需要访问本地主机地址下的服务地址 **https://localhost/ampps**, 如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/007c28ebeba142048b54d94e7c5caae4.png" alt="在这里插入图片描述">

而上面localhost显示的页面，则是文档根目录。

AMPPS使用的以下默认地址作为文档根目录： C:\Program files\ampps\www, 在文件资源管理器中，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/7d984521d78f4a7b9fef399ee1308a46.png" alt="在这里插入图片描述">

#### 6. 创建和访问HTML文件

为了显示新建的HTTP服务器，作为Web服务器预览页面的功能，现在创建一个HTML文件，放到文件根目录中。

新建文件index.html, 使用Visual Studio Code编辑标记和代码如下：

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Apache HTTP Server&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Hello, world!&lt;/h1&gt;
    &lt;p&gt;This is an Apache HTTP Server Sample.&lt;/p&gt;
    &lt;h4&gt;2024 All rights reserved. Powered by Jackson@ML&lt;/p&gt;
    &lt;style&gt;
        h1 {<!-- -->color: red;}
        p {<!-- -->
            color: brown;
            font-size: 1.5em;
        }
        h4 {<!-- -->
            color: lightgreen;
            font-size: 1.0em;
        }
    &lt;/style&gt;    
&lt;/body&gt;
&lt;/html&gt;

```

可以看到，笔者在Body部分添加了h1标题，p段落和h4标题，并且设置了简单的CSS样式。

重新打开Chrome浏览器，键入该页面地址, https;//localhose/index.html, 如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/e10c85a85331453981457aaee658f3a2.png" alt="在这里插入图片描述"> 这说明搭建的Apache HTTP服务器工作正常，也就是说AMPPS全栈包安装完成！

技术好文陆续推出，敬请关注。 您的鼓励，我的动力！ 😊

#### 相关阅读
1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 