
--- 
title:  运维工具之MobaXterm工具安装和使用 
tags: []
categories: [] 

---
## 一、MobaXterm工具简介

  MobaXterm是远程计算的终极工具箱。在一个Windows应用程序中，它提供了大量的功能，这些功能是为程序员、网站管理员、it管理员以及几乎所有需要以更简单的方式处理远程工作的用户量身定制的。MobaXterm在一个开箱即用的可移植exe文件中为Windows桌面提供了所有重要的远程网络工具（SSH、X11、RDP、VNC、FTP、MOSH…）和Unix命令（bash、ls、cat、sed、grep、awk、rsync…）。   为我们远程任务提供All-In-One网络应用程序有很多优点，例如，当您使用SSH连接到远程服务器时，会自动弹出一个图形SFTP浏览器，以便直接编辑您的远程文件。您的远程应用程序也将使用嵌入式X服务器在Windows桌面上无缝显示。MobaXterm时专注于一个简单的目标：提出一个直观的用户界面，以便通过不同的网络或系统高效地访问远程服务器。

## 二、MobaXterm下载和安装

### 1、访问官网

  访问官网地址https://mobaxterm.mobatek.net/download.html，选择下载家庭版，家庭版是免费的，只是有会话数限制。点击Download now按钮进入下载链接。 <img src="https://img-blog.csdnimg.cn/80d43c8627c14f7dbc8198e118de5e1a.png" alt="在这里插入图片描述">

### 2、下载便携版

  官网提供便携版和安装版下载，这里我们选择便携版，下载后启动即可使用。 <img src="https://img-blog.csdnimg.cn/1c4b4202034141eab86ba93e540f7404.png" alt="在这里插入图片描述">

### 3、启动MobaXterm

  将下载的软件包解压到文件夹，双机启动exe程序，启动后可以直接使用，不需要安装，非常方便。整个软件包只有三十多M，非常的精简方便。 <img src="https://img-blog.csdnimg.cn/6bb6ba7eac124af7bb791c2c3de9fbb9.png" alt="在这里插入图片描述">

## 三、MobaXterm ssh远程使用简介

### 1、新建会话

  MobaXterm支持的远程方式非常丰富，基本上一个工具涵盖了日常所需的所有远程需要。最常用的莫过于ssh远程连接linux服务器了。输入IP地址后即可开启一个会话，如果需要指定登录用户可以勾选Specify username，输入对应的用户名。如果非默认的22端口，我们在port输入口输入对应的端口号。 <img src="https://img-blog.csdnimg.cn/fb5518355c0544d0b771bb8fed692c86.png" alt="在这里插入图片描述">

### 2、设置主密码

  首次使用会弹窗要求设置master password，即打开会话的密码。这个工具是便携版，我们可以放在U盘，随时更换终端使用，当切换window终端的时候我们需要输入主密码验证保证会话安全。 <img src="https://img-blog.csdnimg.cn/dd77044b0a0c4f409c79c57726d6311d.png" alt="在这里插入图片描述">

### 3、sftp文件上传下载

  ssh远程登录服务器后默认开启一个sftp会话窗口，默认路径为登录用户的家目录，我们可以在输入框输入路径进行切换。点击上面的按钮可以上传、下载文件。也可以执行创建文件夹、删除等操作。 <img src="https://img-blog.csdnimg.cn/147dd02ad1f5480abe7f5503712ec51d.png" alt="在这里插入图片描述">

### 4、录制宏指令

  点击record new macro即可开始宏指令录制，所有操作命令都将被记录下来。 <img src="https://img-blog.csdnimg.cn/e05cddf839d44a2fb9c21e45e051d566.png" alt="在这里插入图片描述">

### 5、保存宏指令

  录制完成后，点击stop按钮，会弹窗保存宏指令，默认名称为输入的第一条命令，我们可以根据需要自定义名称。 <img src="https://img-blog.csdnimg.cn/da0ce682a5e041db8fbe66ea7eb82d57.png" alt="在这里插入图片描述">

### 6、执行宏指令

  录制好的宏指令，我们可以在任何的会话窗口点击执行。所以我们可以把日常巡检命令录制为宏指令，点击后批量执行。 <img src="https://img-blog.csdnimg.cn/358e2c56ead44b95a9be9e3aeeec65e9.png" alt="在这里插入图片描述">

### 7、查看服务器监测信息

   <img src="https://img-blog.csdnimg.cn/c402b8fbc7df47c98b92e90c7677d454.png" alt="在这里插入图片描述">

## 四、MobaXterm telnet远程使用简介

  交换机、路由器常用telnet远程管理方式，使用MobaXterm也可以满足要求。

### 1、新建telnet会话

  新建会话，选择telnet，输入IP地址和用户名，username不输入也可以，telnet连接连接的时候还是会要求输入username。 <img src="https://img-blog.csdnimg.cn/d7ed6d6fa8fe4d25aa236389f6e7391e.png" alt="在这里插入图片描述">

### 2、远程操作

  telnet登录后就是正常的shell操作窗口，跟其他的没有啥区别。正常使用即可。 <img src="https://img-blog.csdnimg.cn/e4012722137d4c038a2dac2490110c07.png" alt="在这里插入图片描述">

## 五、MobaXterm RDP远程使用简介

### 1、新建RDP会话

  新建一个RDP会话，跟我们使用windows自带的mstsc.exe远程登录window客户端效果是一样的，这里不再过多赘述。 <img src="https://img-blog.csdnimg.cn/e2d5387ef3c14d4898fdb6e168110d4c.png" alt="在这里插入图片描述">

### 2、远程操作window桌面

<img src="https://img-blog.csdnimg.cn/bb2e77f734114b02a5c5585d512e0d1a.png" alt="在这里插入图片描述">

## 六、MobaXterm其他功能使用简介

### 1、MobaXterm server功能

  MobaXterm server功能非常有用，可以通过此功能启用TFTP、FTP、HTTP、SSH、等服务。主要有两个用途，一是比如我们可以启用TFTP server，用于交换机升级时文件上传下载；二是我们可以使用HTTP server自定义服务端口，用于验证网络策略的开通与否。不过免费版本启用的服务会在6分钟后停止，对于验证网络策略需要完全够用，上传小文件也满足需求了。 <img src="https://img-blog.csdnimg.cn/88b29af416c54cfc95812eec8234ad8e.png" alt="在这里插入图片描述">

### 2、工具集

  工具间集包括了系统工具、办公工具、网络工具。List hardware devices（查看本机硬件信息）、Wake on Lan(网络唤醒)、Ports scanner（端口扫描）等工具都非常实用。 <img src="https://img-blog.csdnimg.cn/59a885dce91147689fca0c41866b4e9c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/1bb8ce0407924aabb1a200d5a3b46145.png" alt="在这里插入图片描述">

### 3、Games功能

  工作累了还可以玩会小游戏，娱乐一下，有数独、蜘蛛扑克等。 <img src="https://img-blog.csdnimg.cn/0fe1ced59e404bdda72c382768f7c71f.png" alt="在这里插入图片描述">

### 4、分屏

  支持分屏2个窗口或者四个窗口。俩屏可以是左右分或者上下分。 <img src="https://img-blog.csdnimg.cn/0c978b9d91e74bbd81a5df706f91a496.png" alt="在这里插入图片描述">

### 5、MultiExec多屏同时执行

  使用MultiExec功能可以同时在多屏执行同一个命令，这个功能通常用于需要执行相同命令，对命令结果进行对比时。 <img src="https://img-blog.csdnimg.cn/7d647f7209014befb505a7d004af16bb.png" alt="在这里插入图片描述">

### 6、SSHTunneling配置

  SSHTunneling功能实际上就是自动登录跳板机环境。比如我们需要登录服务器A，但是根据安全管理要求，所有登录必须先登录跳板机B，通过跳板机B才可以登录A。这个时候我们就可以配置一条SSHTunneling通道。如下图所示，配置好通道之后，启动隧道，这个时候就会监听1080端口，新建session 127.0.0.1:1080,实际上登录的服务器是s152。免费版有限制，只可以配置2条隧道。 <img src="https://img-blog.csdnimg.cn/1c290c946d624f74a9aedae458e6211b.png" alt="在这里插入图片描述">

### 7、串口连接

  作为一名网络工程师console线必备，毕竟很多交换机路由器都需要靠console线连接，完成初始化配置之后才可以远程连接。 <img src="https://img-blog.csdnimg.cn/de8cc107564b4c0497fe59f08891383e.png" alt="在这里插入图片描述">
