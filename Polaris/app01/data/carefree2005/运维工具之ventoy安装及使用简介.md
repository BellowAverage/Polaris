
--- 
title:  运维工具之ventoy安装及使用简介 
tags: []
categories: [] 

---
## 一、Ventoy简介

  简单来说，Ventoy是一个制作可启动U盘的开源工具。有了Ventoy你就无需反复地格式化U盘，你只需要把 ISO/WIM/IMG/VHD(x)/EFI 等类型的文件直接拷贝到U盘里面就可以启动了，无需其他操作。你可以一次性拷贝很多个不同类型的镜像文件，Ventoy 会在启动时显示一个菜单来供你进行选择。你还可以在 Ventoy 的界面中直接浏览并启动本地硬盘中的 ISO/WIM/IMG/VHD(x)/EFI 等类型的文件。Ventoy 安装之后，同一个U盘可以同时支持 x86 Legacy BIOS、IA32 UEFI、x86_64 UEFI、ARM64 UEFI 和 MIPS64EL UEFI 模式，同时还不影响U盘的日常使用。Ventoy 支持大部分常见类型的操作系统 （Windows/WinPE/Linux/ChromeOS/Unix/VMware/Xen …），只需要下载ventory安装到U盘中即可，同时支持window和linux系统下安装。

## 二、安装步骤

### 1、通过官网下载最新软件包

  登录，下载ventory最新版本软件包，博主这是window环境下安装选择第一个。 <img src="https://img-blog.csdnimg.cn/direct/16b07e58291c46b2acf6b17a56bae679.png" alt="在这里插入图片描述">

### 2、校验下载文件hash值

  校验下载的文件hash值，确保文件无损坏和篡改。 <img src="https://img-blog.csdnimg.cn/direct/79b24ffc43264c8fada0cec43d9bc924.png" alt="在这里插入图片描述">

### 3、解压后开始安装

  将压缩包解压，进入解压目录，双机Ventoy2Ddisk.exe开始安装。记得先插入需要用来做启动盘的U盘。点击安装按钮开始安装。 <img src="https://img-blog.csdnimg.cn/direct/58b66dce4a2a40348509d1bcfcb1770d.png" alt="在这里插入图片描述">

### 4、格式化U盘

  格式化U盘，需要进行二次确认，这一点还是比较人性化涉及，避免误点击导致U盘数据丢失。 <img src="https://img-blog.csdnimg.cn/direct/16c3be933e9c42bda5553ea26674729d.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/059505ad3fc142f9a1fe015e70f7816a.png" alt="在这里插入图片描述">

### 5、安装完成

  看到如下提示就说明安装完成啦。 <img src="https://img-blog.csdnimg.cn/direct/aa17514ebc734bd2b86dae2123b6932b.png" alt="在这里插入图片描述">

## 三、使用简介

### 1、将系统镜像iso文件上传到U盘

  将系统镜像上传到U盘下。 <img src="https://img-blog.csdnimg.cn/direct/562108ff27b64ca0a0abeb965d93e5a0.png" alt="在这里插入图片描述">

### 2、修改服务器boot参数

  legacy等模式下安装完系统本地磁盘启动是第一选项，插上U盘重启并不会进入U盘系统安装界面，我们修改启动顺序，将USB调整到第一启动位置。 <img src="https://img-blog.csdnimg.cn/direct/0693d816ec6a4bb4ba54e26168f14553.png" alt="在这里插入图片描述">

### 3、选择需要安装的系统iso文件

  插上ventoy U盘，重启机器，进入如下界面，选择我们需要安装的操作系统。 <img src="https://img-blog.csdnimg.cn/direct/9737b61144ff4c838507d51670022754.png" alt="在这里插入图片描述">

### 4、选择启动模式

  为了兼容一些特殊的ISO文件和电脑主板，Ventoy 提供了几种特殊的启动模式。比如： WIMBOOT 模式、GRUB2 模式、 MEMDISK 模式。在之前的版本中只能通过快捷键来启用这些特殊模式。比如按 Ctrl+w 使用 WIMBOOT 模式，按 Ctrl+r 使用 GRUB2 模式等。为了方便使用，从 1.0.80 版本开始，Ventoy 提供了一个二级启动菜单。可以直接选择使用正常模式还是上述特殊模式启动。快捷键的方式仍然有效，而且如果提前按了相关快捷键，或者镜像文件名中有特殊的标识，则不会再显示此菜单。这里我们选择grub2 mode。   normal模式和grub2模式的主要区别：
- 启动模式：normal模式是救援模式，在此模式下只能使用非常少的命令，而Grub2则支持更多命令。- 配置文件：Grub的配置文件为grub.conf，而Grub2的配置文件为grub.cfg。- 语法支持：Grub2增添了许多语法，更接近于脚本语言，例如支持变量、条件判断、循环等，而normal模式则不具备这些功能。- 设备分区命名：Grub2中设备分区名称从1开始，而normal模式以及Grub中是从0开始。- 交互界面：Grub2中无法进入交互式界面，且不能使用查找命令find，这是与normal模式的主要区别。 <img src="https://img-blog.csdnimg.cn/direct/4a2c7c51b9b747b49f2741dafd16523d.png" alt="在这里插入图片描述">
### 5、开始安装系统

  接下来的步骤就跟正常U盘安装系统或者光盘安装系统没有多少区别了。我们按照自己的安装要求和习惯点击下一步和设置即可完成安装。 <img src="https://img-blog.csdnimg.cn/direct/1e3eb94a380542a3bf54af9dc6d1bd08.png" alt="在这里插入图片描述">

### 6、选择系统安装磁盘

  需要注意的是选择安装目标位置的时候本地硬盘和U盘都在识别范围内，这里我们要注意标识不要选错了，尤其是U盘容量比较大的时候。 <img src="https://img-blog.csdnimg.cn/direct/30eebbe69e504ed3bc50a669fe13b011.png" alt="在这里插入图片描述">

### 7、安装完成

  剩下的步骤我们一步步按照提示完成安装，安装完成后重启系统，重启前我们拔除U盘。完成配置IP地址、设置主机名就可以使用了。Ventoy 除了可以启动U盘中的文件以外，还可以浏览、启动本地硬盘、移动硬盘中的 ISO/WIM/IMG/VHD(x)/EFI 等类型的文件。从 Ventoy 1.0.67 版本开始，在 Ventoy 界面上按 F2 可以直接浏览并启动本地硬盘中的镜像文件。总之ventoy是一个非常nice的多系统装机工具。 <img src="https://img-blog.csdnimg.cn/direct/a25f1ddb70794fa7bd4c28d73eeabeb6.png" alt="在这里插入图片描述">
