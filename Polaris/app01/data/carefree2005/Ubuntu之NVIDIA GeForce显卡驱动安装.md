
--- 
title:  Ubuntu之NVIDIA GeForce显卡驱动安装 
tags: []
categories: [] 

---
## 一、NVIDIA简介

  NVIDIA是一家人工智能计算公司 [1] 。公司创立于1993年，总部位于美国加利福尼亚州圣克拉拉市。美籍华人Jensen Huang（黄仁勋）是创始人兼CEO。1999年，NVIDIA定义了GPU，这极大地推动了PC游戏市场的发展，重新定义了现代计算机图形技术，并彻底改变了并行计算。 2017年6月，入选《麻省理工科技评论》“2017 年度全球50大最聪明公司”榜单。当前世界上机器学习、深度学习都离不开GPU的支持。GeForce是一款显卡产品的英文商标。GeForce显卡是NVIDIA（英伟达）的核心产品系列之一。博主安装的时的实验软件如下：
- 操作系统：Ubuntu20.04 LTS- 驱动程序版本：525.89.02
## 二、NVIDIA显卡驱动安装步骤

### 0、多用户模式启动

  将系统设置为多用户模式启动，图形化启动状态下安装显卡驱动会提示正在使用。当然如果是已经部署生产程序的主机，多用户模式下安装可能也会提示x-server已启动，我们只需要查看/var/log/nvidia-installer.log可以看到x-server进程，关闭进程重新执行安装即可。

>  
 wuhs@jqxxpc:~$ sudo systemctl set-default multi-user.target Removed /etc/systemd/system/default.target. Created symlink /etc/systemd/system/default.target → /lib/systemd/system/multi-user.target. <img src="https://img-blog.csdnimg.cn/9149feaee6e74496acd2eab7ac59ab83.png" alt="在这里插入图片描述"> 


### 1、查看nouveau状态

  如下命令如下如果没有任何输出说明nouveau为禁用状态，如果有输出说明是启用状态。nouveau状态Ubuntu16.04和18.04版本均为禁用，20.04以上版本为启用状态，所以如果是Ubuntu18.04操作系统可以从第3步骤开始。

>  
 wuhs@jqxxpc:~$ lsmod |grep nouveau nouveau 1949696 0 mxm_wmi 16384 1 nouveau ttm 106496 1 nouveau i2c_algo_bit 16384 2 i915,nouveau drm_kms_helper 184320 2 i915,nouveau drm 495616 5 drm_kms_helper,i915,ttm,nouveau wmi 32768 5 intel_wmi_thunderbolt,asus_wmi,wmi_bmof,mxm_wmi,nouveau video 57344 3 asus_wmi,i915,nouveau 


### 2、禁用nouveau

  禁用nouveau，这是ubuntu默认使用的开源显卡驱动，和nvidia驱动一起使用可能导致黑屏，所以禁掉。配置完成后重启，重启后再次执行步骤1命令，无任何输出说明禁用成功。

>  
 wuhs@jqxxpc:~$ sudo vim /etc/modprobe.d/blacklist-nouveau.conf #编辑并插入如下两行后保存 blacklist nouveau options nouveau modeset=0 wuhs@jqxxpc:~$ sudo update-initramfs -u wuhs@jqxxpc:~$ sudo reboot … wuhs@jqxxpc:~$ lsmod |grep nouveau wuhs@jqxxpc:~$ 


### 3、安装gcc

  GeForce显卡驱动的安装需要gcc支持，提前安装，否则在安装显卡驱动的时候会报错，无法继续安装。

>  
 wuhs@jqxxpc:~$ sudo apt-get install -y gcc 


### 4、安装make

  GeForce显卡驱动的安装需要用到make命令，所以提前安装make命令，否则在安装显卡驱动的时候会报错。

>  
 wuhs@jqxxpc:~$ sudo apt-get install -y make 


### 5、下载显卡驱动

  访问NVIDIA官网，根据型号搜索驱动程序，复制链接后使用wget命令下载。

>  
 wuhs@jqxxpc:~$ wget https://us.download.nvidia.com/XFree86/Linux-x86_64/525.89.02/NVIDIA-Linux-x86_64-525.89.02.run 


### 6、添加执行权限

>  
 wuhs@jqxxpc:~$ chmod u+x NVIDIA-Linux-x86_64-525.89.02.run 


### 7、执行安装脚本

>  
 wuhs@jqxxpc:~$ sudo sh NVIDIA-Linux-x86_64-525.89.02.run 


### 8、选择继续安装

<img src="https://img-blog.csdnimg.cn/9024c33f2be8497eabbd1f40654eb7d4.png" alt="在这里插入图片描述">

### 9、安装32位兼容库

<img src="https://img-blog.csdnimg.cn/3159fa20544542429b3741d69e6ba57c.png" alt="在这里插入图片描述">

### 10、回车继续

  libglvnd是与供应商无关的调度层，用于仲裁多个供应商之间的OpenGL API调用。它允许来自不同供应商的多个驱动程序共存于同一文件系统上，并确定在运行时将每个API调用分派给哪个供应商。这里只是一个警告，不影响程序的后续安装。 <img src="https://img-blog.csdnimg.cn/a3e9e0f7e1cc4fb887791f714b30df6c.png" alt="在这里插入图片描述">

### 11、是否运行xconfig

  是否运行xconfig这里选择yes。这是将新驱动程序应用到x server上，如果是开启了桌面环境下安装显卡驱动的时候就会提示需要先关闭x server进程，这里应该是将新版驱动的xconfig应用到xserver。点击yes回车后会有successful弹窗。 <img src="https://img-blog.csdnimg.cn/cea41d136a364073bab10d9a87f8b4bf.png" alt="在这里插入图片描述">

### 12、检查驱动版本

  使用nvidia-smi命令可以看到驱动程序的版本，显存大小，当前使用了GPU的程序等等。也可以看到支持的CUDA最高版本为12.0，这个不是当前安装的CUDA版本，cuda软件包还需要另行安装。nvidia-smi -L命令可以查看GPU的型号。 <img src="https://img-blog.csdnimg.cn/cf3b48820c7a45f59c120c46223b8214.png" alt="在这里插入图片描述">

## 三、Ubuntu20.04网卡IP地址配置步骤

  Ubuntu 20.04系统和Ubuntu18.04网卡IP命令行配置方式是不一样的，Ubuntu18.04是编辑/etc/networks/interfaces配置网卡IP地址。Ubuntu20.04 LTS的网卡IP命令行配置方式如下。

### 1、编辑00-installer-config.yaml配置文件

>  
 wuhs@jqxxpc:~$ sudo vim /etc/netplan/00-installer-config.yaml <img src="https://img-blog.csdnimg.cn/fc5ecdfb09434800a96f0ff7f6d71eab.png" alt="在这里插入图片描述"> 


### 2、应用网络配置

>  
 wuhs@jqxxpc:~$ sudo netplan apply 

