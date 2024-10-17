
--- 
title:  VMWare Workstation 17 Player虚拟机与Red Hat Linux子系统安装指南 
tags: []
categories: [] 

---
## VMWare Workstation 17 Player虚拟机与Linux子系统安装指南

>  
 常常有朋友在安装VMWare Workstation Pro 17时，出现种种问题，例如激活码失效，反复安装影响学习和项目，而又无法找到合适版本等，面临种种困惑。 
 其实，如果仅需要单个虚拟机安装，例如单个Red Hat Enterprise Linux(RHEL) 或者单个CentOS等发行版安装，那么VMWare Workstation 17 Player不失为一种合适的选择。 


本文简要介绍这个虚拟机软件安装以及Linux子系统安装使用步骤。

#### 1. 下载安装VMWare Workstation 17 Player

首先，访问该软件官网链接：， <img src="https://img-blog.csdnimg.cn/6b3d6f82a04b49d2bcff7e29d6a6e87b.png" alt="在这里插入图片描述"> 点击主页面**DOWNLOAD FOR FREE**按钮进行下载。

>  
 官网提示：由于学习和个人使用目的，可以用免费的Player软件; 因此，学生使用该版本的VMWare是再合适不过了。 


在Chrome浏览器下载完毕后，进入Windows的“下载‘文件夹，找到安装文件**VMware-player-full-17.0.0-20800274.exe**, 双击启动安装向导。

>  
 提示：如果先前安装了VMWare Workstation 17 Pro，必须先将其从Windows系统卸载，重新启动计算机后，再安装本软件版本。 卸载软件在控制面板 – 程序与功能 列表里，选择已安装的VMWare Workstation Pro 17, 然后点击“修改“，进入安装向导，进一步选择”卸载“完成软件卸载。 
 下图为安装向导正在删除VMWare Workstation Pro软件。 <img src="https://img-blog.csdnimg.cn/087e44c1ad4b41aaa104a5287cf79641.png" alt="在这里插入图片描述"> 


#### 2. 安装VMWare Workstation 17 Player

启动安装向导后，进入下图对话框。

<img src="https://img-blog.csdnimg.cn/d93865b05e834f0e8f6d1c172d37b320.png" alt="在这里插入图片描述"> 点击“下一步“继续。 <img src="https://img-blog.csdnimg.cn/0ee984c8a03c4c9ca71013275ea757b7.png" alt="在这里插入图片描述"> 选择**我接受许可协议中的条款**，点击”下一步“继续。

<img src="https://img-blog.csdnimg.cn/b3b882682eb84aa9ba216606324d7cf5.png" alt="在这里插入图片描述"> 点击“下一步“继续。 <img src="https://img-blog.csdnimg.cn/f23ce6dec35a4825a75285215fd12015.png" alt="在这里插入图片描述"> 保持默认复选项**将VMWare Workstation控制台工具添加到系统PATH**， 点击“下一步”继续。

<img src="https://img-blog.csdnimg.cn/93946fc7c7324cafac7646ea52b2a866.png" alt="在这里插入图片描述"> 同时，修改安装位置到除C:盘的其它分区。这里选择F:\VMWare\VMWare Player\作为安装目录。 点击“下一步”继续。 <img src="https://img-blog.csdnimg.cn/822a1eeabf5547fe855a5e11241e77bb.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/09f4646c87bf47ffa7bdb3d330b14888.png" alt="在这里插入图片描述"> 点击“下一步”开始安装向导。 <img src="https://img-blog.csdnimg.cn/358699eaa31d4382b3ca4d1a8f6ddc81.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ed06e95123f34891bfafc65f00152834.png" alt=""> <img src="https://img-blog.csdnimg.cn/e7b34fa08ae546438960c20a72315ed6.png" alt="在这里插入图片描述"> 安装结束，点击“完成”退出安装向导。

#### 3.启动VMWare Workstation 17 Player

右键单击桌面快捷方式“VMWare Workstation 17 Player”，选择**以管理员身份运行**。 <img src="https://img-blog.csdnimg.cn/6ec019f2df8a4b5f893288a3c8168cc4.png" alt="在这里插入图片描述"> 弹出程序对话框，保持默认选项**免费将VMWare Workstation Player用于非商业用途**，点击“继续”。 <img src="https://img-blog.csdnimg.cn/cede11ff6dd34b5995204097bdb90b20.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/fbf122c3da524eeeb5bf698acad95dc3.png" alt="在这里插入图片描述"> 出现欢迎画面，点击“完成”结束安装向导。 <img src="https://img-blog.csdnimg.cn/2252a541ec22489e85bb011347fd4e18.png" alt="在这里插入图片描述">

#### 4.创建Red Hat Enterprise Linux虚拟机

在VMWare Workstation Player对话框中，点击**创建虚拟机**。

>  
 注意：在启动虚拟机过程中，会触发软件更新。系统会提示升级到更高版本。如下图。 <img src="https://img-blog.csdnimg.cn/845407c4206741bb86f69806bd5c2849.png" alt="在这里插入图片描述"> 选择**跳过此版本**，以免影响正常加载虚拟机客户机操作系统。 


找到之前下载保存在硬盘相应位置的Red Hat Enterprise Linux 7.4镜像文件，如下图。点击“打开“，引入到虚拟机安装向导。

<img src="https://img-blog.csdnimg.cn/7d4edbbbb74e4db7839ed5f69ff736cb.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/bb03f9a32a94475c8fdd1426cb6c96d9.png" alt="在这里插入图片描述"> 因此，在对话框中间“安装程序光盘映像文件(iso)“中，出现了已选择镜像文件的路径。

>  
 提示：如果你的电脑有不同的位置存放该镜像文件，则要点击“浏览“重新找到镜像文件，并导入到安装向导。 


点击”下一步“继续。 <img src="https://img-blog.csdnimg.cn/5531c3c43caf41dfb54af42b61c20a14.png" alt="在这里插入图片描述"> 在上面对话框“新建虚拟机向导”中的“个性化Linux”选项中，输入全名、用户名和密码。这些信息靠使用者自行定义。 点击“下一步”继续。

>  
 提示：一定需要记住密码，以便启动虚拟机Linux客户机操作系统时，使用该用户和密码。 


<img src="https://img-blog.csdnimg.cn/d49155e50d8645e7a44d30a8888ffb4d.png" alt="在这里插入图片描述"> 点击“下一步”继续。

<img src="https://img-blog.csdnimg.cn/55fca5f6e811490389232d1e7d88c4af.png" alt="在这里插入图片描述"> 虚拟机名称可以保留不变，但是保存位置需要改变到F:盘相应目录，如F:\Virtual Machines\RedHatLinux, 点击“下一步”继续。 <img src="https://img-blog.csdnimg.cn/8fad16ff6a8049d0bba653b9a3288002.png" alt="在这里插入图片描述"> 保留默认选项“最大磁盘大小：20GB”（除非需要使用更大的虚拟空间，且硬盘足够大能够满足）；选择“将虚拟磁盘存储为单个文件“，点击”下一步“继续。

<img src="https://img-blog.csdnimg.cn/d7b7af9ae98349dd9cd2205174324a82.png" alt="在这里插入图片描述"> 出现对话框“已准备好创建虚拟机“，点击”完成“。此时，自动启动Red Hat Enterprise Linux安装向导。如下图： <img src="https://img-blog.csdnimg.cn/da566b28bd7b4e99bf45c809c3cae37f.png" alt="在这里插入图片描述"> 接下来，启动了红帽操作系统Red Hat Enterprise Linux 7(64位)。 该过程自动完成。以下是登录视图。

<img src="https://img-blog.csdnimg.cn/7c2dcdc4777349c39cb41d8f2cfedf42.png" alt="
">

用刚才创建的用户和密码，即可登录。 <img src="https://img-blog.csdnimg.cn/e2b189bb6d5146e2a774bb0d6f954a3b.png" alt="在这里插入图片描述"> 出现提示符如下，证明登录成功！

```
[jackson@localhost ~] $

```

如果需要用超级管理员登录，则使用以下命令：

```
# su root

```

执行完后，命令行提示符变为：

```
[root@localhost jackson] #

```

接下来，就可以在这个虚拟机上运行的Linux操作系统上完成各种命令操作了。

## # 远程登录该服务器

用以下命令查看安装好的Red Hat操作系统中，虚拟网络适配器（即虚拟IP）地址：

```
# ip addr

```

<img src="https://img-blog.csdnimg.cn/72e47026af064aca9be69f81125d1435.png" alt="在这里插入图片描述"> 查看得到虚拟网络适配器（虚拟网卡）绑定的IP地址：192.168.85.128.

#### 5.用终端访问程序XShell连接服务器

安装好Xshell，打开该软件，新建会话；输入主机IP地址，即上述的红帽Red Hat操作系统查出的虚拟网络适配器地址。

安装好Xshell，打开该软件，新建会话；输入主机IP地址，即上述的红帽Red Hat操作系统查出的虚拟网络适配器地址。

<img src="https://img-blog.csdnimg.cn/20144cccf6174606bf6b08e06ccca8b6.png" alt="在这里插入图片描述">输入会话名称：Red Hat Linux, 保留端口号22，点击“确定“。

在Xshell命令行，输入以下命令：

```
ssh 192.168.85.128

```

<img src="https://img-blog.csdnimg.cn/95bee81de6ad4309b397a853a43b2999.png" alt="在这里插入图片描述"> 弹出对话框，点击“接受并保存“继续。 <img src="https://img-blog.csdnimg.cn/d60199f9a53c49a6847266bc47314bfb.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5e405fe54c4f4d0ba6b74449f7af4fad.png" alt="在这里插入图片描述"> 输入root用户名和密码，点击“确定“。此时，连接到红帽操作系统主机成功！ <img src="https://img-blog.csdnimg.cn/91d9c5867452482398cf69d04d92a9b9.png" alt="在这里插入图片描述"> 进入到[root@localhost ~] #，这是root用户登录成功的标志，同时表明，当前位置在root用户目录。

这时候，就可以用XShell的强大功能，连接Red Hat Enterprise Linux进行学习和日常操作了。

请仔细查看，以下一系列命令，完成了哪些任务？

<img src="https://img-blog.csdnimg.cn/f5802e3118a845f89b034cdcc9f26938.png" alt="在这里插入图片描述">

相关有用的技术博文，会陆续推出。

喜欢就点赞哈，欢迎关注！😊
