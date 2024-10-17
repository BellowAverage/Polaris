
--- 
title:  开源防火墙pfSense的安装及初始化 
tags: []
categories: [] 

---
## 一、pfSense简介

  pfSense是一个基于FreeBSD，专为防火墙和路由器功能定制的开源版本。它被安装在计算机上作为网络中的防火墙和路由器存在，并以可靠性著称，且提供往往只存在于昂贵商业防火墙才具有的特性。它可以通过WEB页面进行配置，升级和管理而不需要使用者具备FreeBSD底层知识。pfSense通常被部署作为边界防火墙，路由器，无线接入点，DHCP服务器，DNS服务器和VPN端点。通常一个硬件防火墙少则几万元，多则几十万，而我们通过pfSense这个开源防火墙软件，就可以体验大部分硬件防火墙才有的功能。pfSense最新的稳定版本是2.6。博文实验环境说明：
- 虚拟化平台：Proxmox7.0.8- pfSense版本：2.6.0
## 二、安装步骤

### 1、官网下载iso软件包

  登录官网https://www.pfsense.org/download/，下载iso软件包。 <img src="https://img-blog.csdnimg.cn/44254a61c6f843d3bae1245d3bbeddff.jpeg" alt="在这里插入图片描述">

### 2、解压软件包

  下载完成后是pfSense-CE-2.6.0-RELEASE-amd64.iso.gz压缩包，使用解压工具得到镜像软件包pfSense-CE-2.6.0-RELEASE-amd64.iso。

### 3、将软件上传到promox平台

  将iso包上传到Proxmox虚拟化平台。 <img src="https://img-blog.csdnimg.cn/ee43cef1410c46499a79f2b31d059b33.png" alt="在这里插入图片描述">

### 4、新建一个虚拟机

  新建一个虚拟机，pfSense对配置要求不高，我们配置一个2c,2G内存,40G硬盘资源的虚拟机即可，为了模拟防火墙我们需要两个网卡，所以配置完虚拟机后我们编辑硬件，添加一个网络设备，即添加一块网卡。 <img src="https://img-blog.csdnimg.cn/10ac9c58c87e41e8891bab27476ac4fe.png" alt="在这里插入图片描述">

### 5、接受协议

  接受软件安装协议。 <img src="https://img-blog.csdnimg.cn/a450af31f5f549f2a54c7a4d81c49a2d.png" alt="在这里插入图片描述">

### 6、选择Install pfSense

  默认选择项，点击回车继续即可。 <img src="https://img-blog.csdnimg.cn/23c929b786c84129806bec57da79b780.png" alt="在这里插入图片描述">

### 7、选择键盘类型

  选择默认键盘类型即可，默认会进入测试模式，输入回车键完成选择。 <img src="https://img-blog.csdnimg.cn/c0b99b5ede934c6c82c676908a5ca9f8.png" alt="在这里插入图片描述">

### 8、选择文件系统格式

  我们选择UFS文件系统格式，如果是物理服务器，且配置有raid阵列卡的我们可以选择ZFS格式安装。 <img src="https://img-blog.csdnimg.cn/c626a27f738548f68f03c9ea3581832d.png" alt="在这里插入图片描述">

### 9、安装完成

  安装完成后提示是否需要进入shell模式修改，选择no即可，然后选择reboot重启。 <img src="https://img-blog.csdnimg.cn/1b998b7713b24f07966b587700698566.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/9576854542db4af691fd56b5a9e68d8b.png" alt="在这里插入图片描述">

### 10、重启后进入接口配置任务

  这里我们要选择y，至少配置1个wan/lan一个接口地址，接口地址配置完成我们才可以管理防火墙。 <img src="https://img-blog.csdnimg.cn/45260e00f9a6491bae7d7707ec897505.png" alt="在这里插入图片描述">

### 11、映射wan口

  虚拟机开始配置了两块网卡，我们将WAN口映射到vtnet0网卡。这个配置需要大约1-2分钟，耐心等待。 <img src="https://img-blog.csdnimg.cn/9d15f6c0541044cf859729f6de81735a.png" alt="在这里插入图片描述">

### 12、配置IP地址

  WAN口自动配置任务完成后，进入如下界面，我们选择2，配置wan口的IP地址。配置过程中根据提示配置IP地址、掩码、网关，以及启用http服务。 <img src="https://img-blog.csdnimg.cn/9efa1f2852e0427aa5ec2237d300a6e8.png" alt="在这里插入图片描述">

### 13、登录防火墙

  完成IP地址配置后我们可以重启防火墙，重启后还是进入如上界面。我们可以通过浏览器登录(http://ip)并管理防火墙。ip地址为我们上一步手动配置。输入默认账户admin/pfsense完成登录。 <img src="https://img-blog.csdnimg.cn/8f1b3cc4a8c3472db616200e1f2da10e.png" alt="在这里插入图片描述">

### 14、修改admin密码

  初始登录后界面如下，会有告警提示，需要修改admin账户密码，点击提示处，我们修改admin账户密码。 <img src="https://img-blog.csdnimg.cn/5a6914e68cb9450d9a46d2c8fb76f502.png" alt="在这里插入图片描述">

### 15、密码修改完成

  输入两次密码，点击save后完成账户密码修改。 <img src="https://img-blog.csdnimg.cn/3248c204f0334c81acf175aebc923b19.png" alt="在这里插入图片描述">

### 16、设置防火墙系统语言

  依次点击System–》General Setup进入基本设置页面。 <img src="https://img-blog.csdnimg.cn/4f1f504e71b545dc82fb634464ff5f57.png" alt="在这里插入图片描述">   拉下到localization位置，将时钟设置为上海时钟，语言设置为简体中文。设置完成后单击save保存。 <img src="https://img-blog.csdnimg.cn/b4897679e1bb4eeb98fb77e0c0cf163e.png" alt="在这里插入图片描述">

### 17、可以使用啦

  设置完成后，自动刷新了界面，系统管理语言切换为了我们熟悉的中文，可以看到系统、接口、防火墙、服务、VPN等功能模块。现在我们就可以像配置物理防火墙一样配置我们的防火墙啦，是不是很酷呀。 <img src="https://img-blog.csdnimg.cn/75ef8f44bdca48f6b49d0916d8a79011.png" alt="在这里插入图片描述">
