
--- 
title:  用Visual Studio Code搭建C/C++语言开发环境 
tags: []
categories: [] 

---
## 用Visual Studio Code搭建C/C++语言开发环境

### Build a C/C++ Development Environment with Visua Studio Code

>  
 Visual Studio Code（简称VS Code）是一款非常流行且广泛使用的开源代码编辑器和IDE（集成开发环境）。它不但支持多语言，而且可以使用大量Extension,从而使VS Code本身变得 非常强大和易用。 


本文简要介绍如何在Visual Studio Code(以下简称VS Code）平台搭建C语言和C++语言开发环境，从而有效发挥VS Code的强大功能，来支持C/C++敏捷开发项目。

在启动 Visual Studio Code 并运行第一个 C 或 C++ 代码的过程之前，我们做一些准备。

#### 1. 安装C/C++的编译器

要运行 C 或 C++ 代码，您只需要在计算机上安装有效的 C/C++ 编译器。除非是Linux 操作系统，它很有可能已经预先安装在您的系统上。否则，在Window系统里，我们需要首先确保C编译器正确安装。

要检查您的系统上是否安装了编译器 （GCC/G++/MinGW），您必须先检查编译器版本。 只需打开终端并使用 以下命令：

```
gcc --version 

```

和

```
g++ --version

```

如果获得版本号，则编译器已安装在系统上。如下图所示： <img src="https://img-blog.csdnimg.cn/c12c3935c4114e2985bf6343d2882495.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/60a85444cf4f41c78df92bfdbe053ca6.png" alt="在这里插入图片描述"> 分别显示gcc版本号为6.3.0, 而g++版本号为6.3.0, 上图证明，笔者电脑已经安装了gcc编译器，和g++编译器。

您可以在任何操作系统上使用相同的命令检查版本，无论是 Windows、Linux 还是基于 macOS 的操作系统。

如果你在终端上得到反馈，说它对 GCC 或 G++ 一无所知，那么你必须正确安装编译器。

#### 2. 安装Visual Studio Code Insiders

若进行Visual Studio Code开发，必须直接从官方网站下载 Visual Studio Code：。

如果需要，还可以安装 **VS Code Insiders**，安装过程类似。

Visual Studio Code Insiders 实际上是 Visual Studio Code 的“Insiders”版本，其中包含每天发布的所有最新功能。可以将 VS Code 视为稳定版本，将 VS Code Insiders 视为 Insiders 版本。

如果想立即体验最新的更新，那么也可以尝试 Visual Studio Code Insiders（我自己使用它）。要下载 VS Code Insiders，您可以在此处访问 VS Code Insiders 的官方网站： 

以下就逐步介绍如何用Visual Studio Code Insiders软件进行C程序开发的例子。

<img src="https://img-blog.csdnimg.cn/db98ad637b1a40608c5329a7c114f000.png" alt="在这里插入图片描述"> 选择x64(即64位)的User Installer，点击Download for Windows下载Visual Studio Code Insiders，如下图：

<img src="https://img-blog.csdnimg.cn/6aafb79368c845c9962f55db6f8cc22f.png" alt="在这里插入图片描述"> 随后，Visual Studio Code Insider自动下载；待下载完毕，在Windows的下载文件夹，找到该可执行文件**VSCodeUserSetup-x64-1.85.0-insider.exe**，双击开始安装。

<img src="https://img-blog.csdnimg.cn/418239cb69a349fc8da561e58ae362ed.png" alt="在这里插入图片描述"> 点击选择**我同意此协议**，然后点击**下一步**继续。 <img src="https://img-blog.csdnimg.cn/b09f1a0a2ef440c694620d202a520976.png" alt="在这里插入图片描述"> 按照默认安装路径，点击下一步继续。 <img src="https://img-blog.csdnimg.cn/d4e85802785c40029a4a9412bf6dbc06.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ceb2c72ae6dc45628900f9386540c7c7.png" alt="在这里插入图片描述"> 默认选择**添加到PATH**（PATH是环境变量），点击**下一步**继续。

<img src="https://img-blog.csdnimg.cn/1ff2ded293b8416795a3937919e6f6af.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/739cae51d74a41e2a900328474ceabce.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/a8ed9db9449742fb84814674d98e4537.png" alt="在这里插入图片描述"> 安装完毕，点击完成退出安装向导。

#### 3. 安装必要的Extension

##### 1) C/C++ Extension

安装完毕后，自动启动Visual Studio Code Insiders。此时，需要在marketplace搜索C/C++的Extension并安装完成, 如下图所示：

<img src="https://img-blog.csdnimg.cn/7adca11b070b4d619ef64aef8c19379e.png" alt="在这里插入图片描述">

##### 2) C/C++ Extension Pack

同样，C/C++ Extension Pack也是一个extension, 需搜索并完成安装，如下图： <img src="https://img-blog.csdnimg.cn/05948769ee294c769acfc847915f2a28.png" alt="在这里插入图片描述">

##### 3) Code Runner

同时，还需要搜索Code Runner进行安装，这也是不可或缺的，如下图： <img src="https://img-blog.csdnimg.cn/4facec45cfa7497497c81b9400000410.png" alt="在这里插入图片描述"> 当Code Runner这项Extension安装完毕后，接下来，需要对它进行简要配置。

选择**Manage**(管理) &gt; **Setting**(设置) &gt; **User**(用户) &gt; 搜索**Run Code Configuration**(运行代码配置)后，在Extension里看到Run Code Configuration选项。

滚动右侧配置选项，找到**Code Runner: Run in Terminal**, 复选该项**Whether to run code in Integrated Terminal**(是否在集成终端运行代码)。这意味着，使之能够在终端输出代码结果。

<img src="https://img-blog.csdnimg.cn/ca1fe7daa1ed43e6a025733e72c6db9c.png" alt="在这里插入图片描述">

##### 4) IntelliCode

为了实现代码高亮显示和代码补全，利于高效开发程序，需要安装IntelliCode这个extension.

<img src="https://img-blog.csdnimg.cn/16dba8700dc744a6932f9f5fc03ede26.png" alt="在这里插入图片描述"> 之后，开始编写第一个C语言程序，如下所示： <img src="https://img-blog.csdnimg.cn/dd051ad7b3f64a9bb04dba532f55d9f7.png" alt="在这里插入图片描述"> 最后，在右上角，选择点击Run Code(运行代码)， 快捷键位Ctrl + Alt + N，此时看到下方Terminal(终端)窗口已经出现Hello, world!的运行结果。 <img src="https://img-blog.csdnimg.cn/2afda1c6745d4e77a659227e2f6e5a4e.png" alt="在这里插入图片描述"> 恭喜！运行成功！

从现在开始，就可以用Visual Studio Code Insider全面开发C语言应用程序了。

喜欢就点赞哈。😊

技术好文陆续推出，欢迎关注。

**All rights reserved. @2023, 版权所有，侵权必究。**
