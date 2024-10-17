
--- 
title:  用Xshell远程登陆Red Hat Enterprise Linux (RHEL)虚拟机子系统 
tags: []
categories: [] 

---
## 用Xshell远程登陆Red Hat Enterprise Linux (RHEL)虚拟机子系统

#### 前言

>  
 安装好VMWare Workstation Player/Pro之后，就可以在VMWare Workstation平台新建Red Hat Enperprise Linux虚拟机；由于VMWare Workstation 17 Player可以在学习时用作非商业用途，因此免费且无须Lincense. 该安装和启动过程，已经在前面发布的文章中介绍过。 


今天，本文要分享给诸位的是，如何用XShell远程登陆创建好的红帽Linux虚拟机子系统。

XShell何许物也？要是看到她官网首页的一句话，你就明白了，”The Industry’s Most Powerful SSH Client” (行业最强大的SSH客户端)。

#### 1. 下载安装XShell 7

访问XShell官网：https://www.xshell.com/，打开主页后，看到下载选项。 <img src="https://img-blog.csdnimg.cn/082f86cddfae41c2a7347593b2dc56ff.png" alt="在这里插入图片描述"> 点击**DOWNLOAD**进行下载，于是跳转到下载页面。 <img src="https://img-blog.csdnimg.cn/bb6a048cdb5e456aa72155186e4f24d3.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/da608849d1284d00a86399b032c3a887.png" alt="在这里插入图片描述"> 选择试用版后，需要填写用户名，邮箱进行注册；之后就进入下载过程。 下载完毕，进行安装；安装完毕后，点击退出安装向导。

#### 2. 获取红帽Linux虚拟机子系统IP地址

启动VMWare Workstation Player，新建Red Hat Enterprise Linux成功后，进入Shell控制台。 <img src="https://img-blog.csdnimg.cn/e4177a8170df433b9ab42b17ca64907c.png" alt="在这里插入图片描述"> 点击“播放虚拟机“，于是开始启动安装在VMWare Workstation Player平台的Red Hat Enterprise Linux虚拟子系统。 <img src="https://img-blog.csdnimg.cn/80f1af395282491ab4fe0b2490868b0f.png" alt="在这里插入图片描述"> 以安装向导注册的用户登录，如下图： <img src="https://img-blog.csdnimg.cn/107f73f426e04bd7a8256d44f7c936d2.png" alt="在这里插入图片描述"> 用以下命令，获取IP地址：

```
ip addr

```

看到待访问主机IP地址为：**192.168.85.138**. 记下这个地址。

#### 3. 启动和使用XShell

在Windows 10搜索关键字“XShell”, 选择**以管理员身份运行**，如下图： <img src="https://img-blog.csdnimg.cn/7413b6247a1545db8a80838423df22a5.png" alt="在这里插入图片描述">

#### 4. 新建会话<img src="https://img-blog.csdnimg.cn/69e797abd34c4b62a896b67a31a1bbf0.png" alt="">

运行后，随即新建会话； 输入主机，点击确定进入终端界面，输入以下命令：

```
ssh 192.168.85.130

```

<img src="https://img-blog.csdnimg.cn/b63387bf24064785816cbb3a11f2b426.png" alt="在这里插入图片描述"> 弹出对话框，要求输入登录的用户名，即输入root, 和相应的密码。 <img src="https://img-blog.csdnimg.cn/d4aab18d4a6948338859f474fa3022bf.png" alt="在这里插入图片描述"> 点击**确定**。 <img src="https://img-blog.csdnimg.cn/5f78bced254048d59badc3f065b01c1f.png" alt="在这里插入图片描述"> 然后，在SSH客户端验证相应Linux命令：

```
ls

```

显示当前目录的文件列表。创建一个脚本文件file.sch:

```
touch file.sh

```

接着输入以下命令：

```
cat file.sh

```

在该文件中，因刚刚创建，内容为空白。 随后，用VIM编辑器编写内容到file.sh文件：

```
vim file.sh

```

加入输出语句：

```
echo "Welcome to Shell Scripting!"
echo "Hello, world!"

```

按**ESC**键退出VIM编辑器，并用 :wq 保存退出。

接下来，用sh命令运行该shell文件：

```
sh file.sh

```

得到如下结果：

<img src="https://img-blog.csdnimg.cn/f84df2966a9a4068b934061285861c9e.png" alt="在这里插入图片描述"> 看到Shell脚本运行成功！

接下来，就可以持续使用XShell的ssh通道，来访问新建的红帽Linux主机了。

后续美文不断推出。 喜欢请点赞，感谢关注！😊
