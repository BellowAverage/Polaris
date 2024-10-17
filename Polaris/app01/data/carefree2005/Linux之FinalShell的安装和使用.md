
--- 
title:  Linux之FinalShell的安装和使用 
tags: []
categories: [] 

---
## 一、FinalShell简介

  FinalShell是一体化的的服务器、网络管理软件，不仅是ssh客户端，还是功能强大的开发、运维工具，充分满足开发，运维需求，支持Windows、macOS、Linux，开源免费，还是一款国产软件。它还有一些特色功能：云端同步，免费海外服务器远程桌面加速，ssh加速，本地化命令输入框，支持自动补全，命令历史，自定义命令参数等。主要特性:
- 1、多平台支持Windows，macOS，Linux。- 2、多标签，批量服务器管理。- 3、支持登录ssh和Windows远程桌面。- 4、漂亮的平滑字体显示，内置100多个配色方案。- 5、终端，sftp同屏显示，同步切换目录。- 6、命令自动提示，智能匹配，输入更快捷，方便。- 7、sftp支持，通过各种优化技术，加载更快，切换，打开目录无需等待。- 8、服务器网络，性能实时监控，无需安装服务器插件。- 9、内置海外服务器加速，加速远程桌面和ssh连接，操作流畅无卡顿。- 10、内存，Cpu性能监控，Ping延迟丢包，Trace路由监控。
## 二、FinalShell下载和安装

### 1、下载一键安装脚本

>  
 [root@s146 opt]# wget www.hostbuf.com/downloads/finalshell_install_linux.sh 


### 2、给脚本添加执行权限

>  
 [root@s146 opt]# chmod u+x finalshell_install_linux.sh 


### 3、执行安装脚本

>  
 [root@s146 opt]# ./finalshell_install_linux.sh centos 正在安装FinalShell… –2022-10-19 10:30:50-- http://dl.hostbuf.com/finalshell2/finalshell_linux.zip?v=27069 … inflating: /usr/lib/FinalShell/lib/runtime/release FinalShell安装完成 


### 4、启动FinalShell

  安装完成后我们进入/usr/lib/FinalShell/目录，双机软件图标启动软件。 <img src="https://img-blog.csdnimg.cn/529874a4b3f345d78b855a44eae8455d.png" alt="在这里插入图片描述">

### 5、FinalShell启动界面

<img src="https://img-blog.csdnimg.cn/8af128b7dddf4df3b6bac3bfdf8a31d0.png" alt="finalshell启动界面">

### 9、其他功能

  FinalShell还有些其他功能，有些是需要收费版才可以使用的，比如云同步、多网卡流量监控等。

## 三、FinalShell使用简介

### 1、新建连接

  点击文件夹图标后，点击新建连接，填写好主机名称、IP地址、端口、用户名密码等信息后完成新建连接。我们也可以新建文件夹，使用文件夹进行分类管理，然后再新建连接。略显不足的地方是无法通过拖拽的方式将已创建连接进行位置调整。 <img src="https://img-blog.csdnimg.cn/b4b8cf82d0d34e2693d075a6ea434e8c.png" alt="在这里插入图片描述">

### 2、多标签页

  可以多标签页，同时管理多个远程终端，略显不足的是点击+新起标签页后只能选择已经创建的连接开启，也就是说所有的连接必须先在参考第一步创建好连接。 <img src="https://img-blog.csdnimg.cn/7df19d360b234d918e4930bc0e6e0ec5.png" alt="在这里插入图片描述">

### 3、系统监控

  连接上系统后左侧的监控栏就自动刷新数据了，主要包括了系统负载、网卡流量、磁盘使用率等信息。 <img src="https://img-blog.csdnimg.cn/fac04e3c9bbc4ea390c851e888c995ea.png" alt="在这里插入图片描述">

### 4、文件下载

  可视化的文件下载，选中远程服务器上的文件后点击下载按钮即可完成下载，默认下载到/home/user/fsdownload目录下。 <img src="https://img-blog.csdnimg.cn/f3e636eace9f42d981d95140d80c8d2d.png" alt="在这里插入图片描述">

### 5、文件上传

  可视化的文件上传，选择需要上传到的远程服务器的目录位置，然后点击上传按钮，选择本机上的文件，选中后双机完成文件上传任务。 <img src="https://img-blog.csdnimg.cn/2510fee8bf074bd1b67dfd962b1fc07f.png" alt="在这里插入图片描述">

### 6、全部会话命令执行

  多标签页的好处就是我们可以同时往这多个会话发送同样的命令，类似批量执行。在批量巡检，查看服务器uptime时间，查看文件路径等场景下非常有用。 <img src="https://img-blog.csdnimg.cn/34155a1baade48bb9e621577404ae734.png" alt="在这里插入图片描述">

### 7、历史命令

  如果是使用命令行终端进行操作，我们查看历史执行的命令需要使用history命令，通过此工具可以可视化选择，我们可以选择再次执行，也可以复制，然后去其他终端黏贴执行。 <img src="https://img-blog.csdnimg.cn/2e96741c0ca34a89897e1f5a3b5b0ce8.png" alt="在这里插入图片描述">

### 8、内容搜索

  点击搜索，输入需要搜索的内容，可以搜索命令窗口屏幕中的字符内容。 <img src="https://img-blog.csdnimg.cn/6989901415dd4beab5cb930ef10d4b2a.png" alt="在这里插入图片描述">

## 四、写在结尾

  根据官网介绍，该软件未来还将支持远程桌面功能（目前该功能在window版本已经是支持的），也就是说我们可以通过linux终端远程管理linux和window终端，一个软件搞定，非常的nice和期待。 <img src="https://img-blog.csdnimg.cn/2ccd3dfbc1104b7b9995e041c9fa0d87.png" alt="在这里插入图片描述">
