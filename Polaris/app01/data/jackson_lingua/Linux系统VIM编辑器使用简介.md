
--- 
title:  Linux系统VIM编辑器使用简介 
tags: []
categories: [] 

---
## Linux系统VIM编辑器使用简介

### A Brief Introduction to VIM Editor on Linux Operating System

<img src="https://img-blog.csdnimg.cn/90684b0e46df4942875b91e7bb5613f5.png" alt="在这里插入图片描述">

>  
 Vi和Vim 均是 Linux 用户中广受欢迎的文本编辑器之一。与其他编辑器相比，Linux 系统管理员通常更喜欢它们。 Vim看似相同，但跟Vi略有不同。 


本文将简要介绍关于 Vim 的知识，并了解如何以开发人员的角色快速启用和熟悉 Vim。

#### 1. 什么是Vim？

**Vim** 是 **Vi IMproven** 的首字母缩写。它是一个开源的跨平台文本编辑器，使用它是免费的。Vim于 **1991 年**加粗样式由 **Bram Moolenaar** 首次发布，用于 UNIX 变体，例如：Linux发行版等。

Vim 基于最初的 **Vi 编辑器**，该编辑器由 **Bill Joy** 于 **1976 年**创建。在1990’s 年代，与 Emacs 编辑器相比，Vi 在某些功能上有所欠缺。因此，Bram 实现了许多缺失的功能，并以 Vim 的名义发布。

#### 2. 安装Vim

Vim 可在 Windows、Linux 和 Mac 等各种平台上运行。Red Hat Enterprise Linux操作系统预装了Vim，无须自己安装。

访问Vim官网： ，看到以下页面。

<img src="https://img-blog.csdnimg.cn/c6994e04ec064458b5e963c7a1425aa6.png" alt="在这里插入图片描述">

官网页面提示，Vim新的官网将于2023年9月24日迁移，目的网站IP地址为： IP 31.172.117.18. 笔者尚未能够打开新的Vim官网。

下面仅以目前下载的Vim作简要介绍。

##### 1) 要在 Windows 上安装 Vim，请从 Vim 站点下载可执行文件并运行该文件。按照屏幕上显示的说明进行操作，您就可以开始了。

Vim 预装在绝大多数Unix, Linux操作系统上。但是，如果它安装在您的系统上，则可以使用您选择的包管理器进行安装。

##### 2) 在Linux发行版安装

###### a. 在基于 Debian 的操作系统的安装命令：

```
sudo apt-get update
sudo apt-get install vim

```

###### b. 在基于Red Hat Linux操作系统的安装命令：

```
dnf install vim

```

#### 3. 验证Vim

安装好Vim后，当我们需要查找它的位置，运行以下命令：

```
which vim

```

<img src="https://img-blog.csdnimg.cn/70542a0334b94ef5bf91007af55ca44f.png" alt="在这里插入图片描述">

#### 4. 用Vim编辑器创建一个新的文本文件sample.txt

直接执行命令：

```
vim

```

于是，打开一个空的文件，欢迎画面如下图：

<img src="https://img-blog.csdnimg.cn/302db4d1bd7844f9bae90eee884f9b03.png" alt="在这里插入图片描述"> 点击键盘的“i”键，进入**INSERT**（插入字符）模式，现在可以编辑文档了。

如果没有对新文件起名，可以用以下命令：

```
:edit sample.txt

```

将新文件命名为sample.txt的文本文件。编辑时输入相应文本，如下图：

<img src="https://img-blog.csdnimg.cn/62f99ebc33904e01b01884930b38b77b.png" alt="在这里插入图片描述"> 编辑完毕后，按以下命令退出插入编辑模式，

```
ESC

```

然后输入以下命令，保存并推出，

```
：wq

```

###### *注：创建新文件，也可以执行以下命令（如果有名字的话，可以直接命名新文件）

```
vim sample.txt

```

创建完毕文本文件后，我们查看一下该文件内容，执行以下命令：

```
cat sample.txt

```

<img src="https://img-blog.csdnimg.cn/5efed8cdcb6e4fd3bef70f4a5a1275e4.png" alt="在这里插入图片描述"> 看到了该文本文件内容（欢迎词如上图）。

#### 5. 创建一个Shell脚本文件（*.sh）

既然Vim集成到Unix, Linux系统中，那么创建一个Shell脚本文件就太容易了，因为Bash Shell也集成到了类Unix系统，如：Linux发行版，macOS等中。

**示例：用Vim编辑器创建file.sh脚本文件**

```
vim file.sh

```

##### 1） 在/root目录创建一个新的子目录，执行命令：

```
mkdir sh

```

##### 2） 转换目录到/root/sh

```
cd sh

```

##### 3） 在此目录下创建一个file.sh的Shell脚本文件

```
vim file.sh

```

<img src="https://img-blog.csdnimg.cn/36f93a13263b4f339a8fe0bc457e1018.png" alt="在这里插入图片描述"> 这里进行输入输出操作：

###### 1） 输出问候语”Hello, world!”， 询问 “What is your name?”

###### 2） 要求用户输入name(姓名)；

###### 3） 打印返回屏幕“Welcome，XX先生。“

执行Shell命令如下：

```
sh file.sh

```

执行完毕，输出效果如下图： <img src="https://img-blog.csdnimg.cn/c77e0fe042f048578577d74360f6c892.png" alt="在这里插入图片描述"> 至此，Vim在Linux系统的安装使用介绍完毕。

如果您感兴趣，请给予支持。喜欢就点赞哈。😊

技术好文陆续推出，敬请关注。

>  
 All rights reserved. @2023, 版权所有，侵权必究。 

