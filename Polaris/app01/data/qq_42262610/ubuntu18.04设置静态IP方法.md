
--- 
title:  ubuntu18.04设置静态IP方法 
tags: []
categories: [] 

---
** 1. 查找netplan目录下默认的网络配置文件，文件后缀为.yaml。** cd /etc/netplan ls

显示01-network-manager-all.yaml  # 如果有的.yaml文件 如果没有可以使用sudo gedit 01-network-manager-all.yaml自己创建。

cd /etc sudo mkdir netpaln sudo gedit 01-network-manager-all.yaml

**2.编辑文件**

sudo vim** **01-network-manager-all.yaml 

# Let NetworkManager manage all devices on this system network:   version: 2   renderer: NetworkManager   ethernets:      eth0: #配置的网卡名称,使用ifconfig -a查看得到        dhcp4: no #dhcp4关闭        addresses: [192.168.1.114/24] #设置要修改的IP及掩码        gateway4: 192.168.1.1 #设置网关        nameservers:          addresses: [192.168.137.1, 192.168.1.1 ] #设置DNS

注：特别要注意的是这里的每一行的空格一定要有的，否则会报错误而设置失败！ 网关、DNS可以在"设置-Network"中查看。

**3.使用命令，来重启网络服务，使静态ip生效** sudo netplan apply 如果出现sudo:netplan命令不存在

使用命令安装netplan sudo apt-get install netplan.io 再使用命令，使静态ip生效 sudo netplan apply

**4.此时如何出现不能上网，出现the system network services are not compatible with this version**, 使用命令 sudo service network-manger start

**5.使用ifconfig命令查看配置情况，如果配置成功，ip会变成自己设置的ip。**
