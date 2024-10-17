
--- 
title:  vmvare ubuntu 拖拽复制 
tags: []
categories: [] 

---
**目录**







在VMware中安装新版Ubuntu后，无法跨虚拟机复制粘贴和拖拽文件的解决方法



### 先是弹框报错：

Ubuntu 22.04 drag and drop is not supported



解决方法：执行命令：

dconf reset -f /org/gnome/desktop/peripherals/mouse/



### 但是拖拽到文件夹还是红色的禁止符号，解决方法

解决方法，感谢：





首先确保已经安装了VMware Tools：

sudo apt install open-vm-tools sudo apt install open-vm-tools-desktop 然后发现还是不能复制粘贴和拖拽文件？原因是Ubuntu（22.04，20.04等）默认启用了新版的窗口系统Wayland而非原来的X11。而VMware Tools尚未支持这个特性（见https://github.com/vmware/open-vm-tools/issues/592）。

所以我们需要禁用Wayland（见https://linuxconfig.org/how-to-enable-disable-wayland-on-ubuntu-22-04-desktop）：



sudo gedit /etc/gdm3/custom.conf 删掉WaylandEnable=false这一行最开始的#号以解开注释，然后保存文件。

 接着重启虚拟机系统即可，或者：

sudo systemctl restart gdm3 然后在虚拟机和主机之间的文件复制粘贴和拖拽就可以用了！
