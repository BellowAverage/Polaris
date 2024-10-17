
--- 
title:  Ubuntu系统升级16.04升级18.04 
tags: []
categories: [] 

---
## 一、需求说明

  作为Linux发行版中的后起之秀，Ubuntu 在短短几年时间里便迅速成长为从Linux初学者到实验室用计算机/服务器都适合使用的发行版，目前官网最新版本是22.04。Ubuntu16.04是2016年4月发行的版本，于2019年4月停止更新维护。很多软件支持的Ubuntu最早版本也是18.04，所以考虑对现有的Ubuntu16.04操作系统进行更新，升级至Ubuntu18.04版本。如下升级步骤不仅仅可以Ubuntu16.04升级到Ubuntu18.04版本，也可以Ubuntu18.04升级到Ubuntu20.04版本。 <img src="https://img-blog.csdnimg.cn/e9682c21044944ab940e45cb46bbd1ee.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d628a9f65bef433c920f3f871e3a2229.png" alt="在这里插入图片描述">

## 二、Ubuntu升级步骤

### 1、查看系统版本

  查看当前操作系统版本，现在是Ubuntu16.04.7 LTS版本。Ubuntu系统建议安装LTS版本，是官方长期支持的版本。 <img src="https://img-blog.csdnimg.cn/cbc47a01fdfa45bcaa175b51a14f166d.png" alt="在这里插入图片描述">

### 2、更新软件包的索引

  更新系统前，首先需要更新软件包的索引。

>  
 wuhs@s169:~$ sudo apt-get update [sudo] password for wuhs: … Fetched 1,146 kB in 5s (203 kB/s) Reading package lists… Done 


### 3、更新软件包

  将当前系统的软件包更新到最新。

>  
 wuhs@s169:~$ sudo apt-get dist-upgrade -y … update-initramfs: Generating /boot/initrd.img-4.15.0-142-generic Processing triggers for libc-bin (2.23-0ubuntu11.3) … 


### 4、安装update-manager-core

>  
 wuhs@s169:~$ sudo apt-get install -y update-manager-core 


### 5、确认版本为LTS版本

  需要确认update-manager参数，默认是lts。设置为lts表示从当前lts版本升级到下一个lts版本。设置为normal则是升级到下一个公开发行版本，如从16.04升级到16.10版本。

>  
 ~$ sudo nano /etc/update-manager/release-upgrades <img src="https://img-blog.csdnimg.cn/7c896ecc0aea491caa64fcb4611e42ab.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ccaf751ea6a54b99b9d19cb6e7c2c19a.png" alt="在这里插入图片描述"> 


### 6、升级系统

  使用do-release-upgrade命令开始升级，我们也可以直接带参数y执行，则省略了中间的确认过程。如果第一次升级则建议查验观察下整个升级过程需要经历的步骤，整个升级国产可能需要持续数小时，博主实测是花费时间2小时+。

>  
 wuhs@s169:~$ sudo do-release-upgrade … If you continue, an additional ssh daemon will be started at port ‘1022’. Do you want to continue?  Continue [yN] y … <img src="https://img-blog.csdnimg.cn/0621d521fc3940d19898329dd87d5a19.png" alt="在这里插入图片描述"> … <img src="https://img-blog.csdnimg.cn/e89c430178594e66ad5f3c69ba688e3d.png" alt="在这里插入图片描述"> … <img src="https://img-blog.csdnimg.cn/844697cc6028446db910306ed8efc61f.png" alt="在这里插入图片描述"> … <img src="https://img-blog.csdnimg.cn/19c24f8006af4f1aa8d3a1e102585c8f.png" alt="在这里插入图片描述"> … 


### 7、重启系统

  升级到此位置，说明升级完成，待重启后生效。 <img src="https://img-blog.csdnimg.cn/03871b868c8445878bfd52d116bc78c4.png" alt="在这里插入图片描述">

### 8、版本验证

  重启系统查看版本我们可以看到已经升级到Ubuntu18.04的版本，如果继续升级，可以升级到下一个LTS版本Ubuntu20.04。 <img src="https://img-blog.csdnimg.cn/5b3ee2c950fe4d75bb75309b5ef36138.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5cea45a6458b45f096b36e25aa7f7584.png" alt="在这里插入图片描述">

## 三、附录

### 1、DNS配置

  Ubuntu和centos配置DNS的方式略有不同，Ubuntu在编辑/etc/resolv.conf配置文件的时候提示这个文件在重启的时候会被覆盖，所以就会出现在这里配置了DNS地址，重启后系统无法访问网站的情况。 <img src="https://img-blog.csdnimg.cn/ad996c420d9d4451b05beef209bcc359.png" alt="在这里插入图片描述">   Ubuntu系统DNS配置方式一：与其他系统一样可以在网卡配置中添加DNS信息，如下所示。

>  
 #dns-nameservers 114.114.114.114 8.8.8.8 


  Ubuntu系统DNS配置方式二：编辑/etc/resolvconf/resolv.conf.d/base配置文件，往其中写入DNS配置信息，然后使用命令resolvconf -u是DNS配置生效。此时再去查看/etc/resolv.conf配置文件可以看到我们刚才添加的DNS配置信息。

>  
 ~$ sudo vim /etc/resolvconf/resolv.conf.d/base nameserver 114.114.114.114 ~$ sudo resolvconf -u 


### 2、ssh服务安装和启用

  Ubuntu16.04默认是未安装和启用SSH服务的。我们可以apt-get安装并启用。

>  
 ~$ sudo apt-get install -y openssh-server ~$ sudo systemctl start ssh 

