
--- 
title:  ubuntu从零开始安装mxnet--安装NVIDIA驱动 
tags: []
categories: [] 

---
### 基础设置
- 操作系统：ubuntu 16.04 LTS Desktop- 显卡：NVIDIA GEFORCE GTX 950M
### 安装步骤

#### 下载驱动

首先，我们到下载对应版本的nvidia显卡驱动

<img src="https://img-blog.csdn.net/20171012150600081?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">

下载的结果是runfile内容，我们把它存放的不含有非ASCII字符的路径下。

#### 卸载驱动（可选）

`sudo apt-get remove --purge nvidia*`  根据一些参考的说法，如果是runfile安装的话，是可以不用卸载的，因为runfile会自动卸载之前安装的驱动。

#### 禁用nouveau
1. 编辑配置文件  `sudo vim /etc/modprobe.d/blacklist.conf`1. 在最后面添加  `blacklist nouveau`1. 保存后执行  `sudo update-initramfs -u`1. 重启电脑1. 执行`lsmod | grep nouveau`，如果没有输出则代表这部分步骤成功。
#### 关闭桌面(X-Server)
1. 进入命令行模式 ctrl + alt + f1，输入对应的帐号密码。1. 执行`service lightdm stop`关闭X-server
#### 运行安装文件
1. 进入刚才下载的runfile文件的目录  `cd /下载目录`1. 运行文件  `./NVIDIA-Linux-x86_64-384.90.run --no-opengl-files`1. 安装过程  期间遇到任何需要同意，接受，继续的字眼请点击进行。
#### 安装成功

到最后会说一段话表示complete

#### 检查安装

数据`nvidia-smi`查看是否有内容存在。  <img src="https://img-blog.csdn.net/20171012172150094?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">

### 参考内容：

  该链接包含了部分疑难杂症解决，在此由衷的感谢。
