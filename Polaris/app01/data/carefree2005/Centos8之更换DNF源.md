
--- 
title:  Centos8之更换DNF源 
tags: []
categories: [] 

---
## 一、DNF包管理器简介

  DNF（Dandified Yum）是一个用于Fedora、CentOS和RHEL等Linux发行版的包管理器。它是Yum（Yellowdog Updater, Modified）的下一代版本，旨在提供更快、更可靠的软件包管理体验。以下是一些DNF包管理器的特点和功能：
1.  依赖解决：DNF能够智能地解决软件包之间的依赖关系。当您安装或升级软件包时，DNF会自动处理所需的依赖关系，确保所有依赖的软件包都被正确安装。 1.  插件系统：DNF具有一个灵活的插件系统，可以通过插件扩展其功能。这些插件可以提供额外的功能，如自动清理缓存、启用软件仓库优先级等。 1.  事务支持：DNF支持事务操作，这意味着您可以在多个软件包之间进行原子操作。如果某个操作失败，DNF将会回滚到之前的状态，确保系统的稳定性。 1.  快速和并行：相比于Yum，DNF具有更快的执行速度。它使用了并行下载和解析的技术，以提高软件包的安装和更新速度。 1.  配置管理：DNF使用简单的文本配置文件来管理软件仓库和其他设置。您可以编辑这些配置文件来添加、删除或修改软件仓库，以及调整DNF的行为。 1.  软件仓库：DNF使用软件仓库来存储和管理软件包。您可以通过配置文件或命令行参数来添加、启用或禁用不同的软件仓库。DNF默认使用Fedora官方的软件仓库，但您也可以添加其他第三方的软件仓库。 
  总体而言，DNF是一个功能强大、易于使用的包管理器，它提供了依赖解决、事务支持、快速执行等功能，使您能够轻松地安装、更新和删除软件包，并管理系统的软件环境。centos系统从centos8之后默认使用dnf包管理器来存储和管理软件包。

## 二、需求说明

  centos8系统默认使用的dnf源是centos官网的，中国内地访问境外网站速度比较慢，博主在安装lrzsz命令的时候明显感觉到下载速度慢，所以准备切换为国内网站镜像源。实验环境如下：
- 操作系统：CentOS Stream release 8- 旧源：http://mirrorlist.centos.org/- 新源：http://mirrors.aliyun.com/ <img src="https://img-blog.csdnimg.cn/direct/a1cbb5e7b2104836b7895c49857082dc.png" alt="在这里插入图片描述">
## 三、更换步骤

### 1、备份当前的DNF源配置文件

>  
 [root@s181 /]# cd /etc/yum.repos.d/ [root@s181 yum.repos.d]# mv CentOS-Stream-BaseOS.repo CentOS-Stream-BaseOS.repo.bak 


### 2、下载新的DNF源配置文件

>  
 [root@s181 yum.repos.d]# wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-8.repo 


### 3、清除DNF缓存

>  
 [root@s181 yum.repos.d]# dnf clean all Repository extras is listed more than once in the configuration 39 files removed 


### 4、更新DNF缓存

>  
 [root@s181 yum.repos.d]# dnf makecache <img src="https://img-blog.csdnimg.cn/direct/67e00877c9e0489082ebcae490df6fcf.png" alt="在这里插入图片描述"> 


### 5、重新安装lrzsz软件包验证

  卸载lrzsz软件包并重新安装，可以看到下载速度明显提升。

>  
 [root@s181 yum.repos.d]# dnf remove lrzsz [root@s181 yum.repos.d]# dnf install lrzsz <img src="https://img-blog.csdnimg.cn/direct/f12b7abfd11d4689904157d41c4cd5e9.png" alt="在这里插入图片描述"> 


## 四、切换其他源：

### 1、切换为网易源

  我们也可以备份源镜像文件后，编辑CentOS-Base.repo文件，写入如下内容，然后执行清除缓存和更新缓存，就可以使用网易163镜像源了。

```
[root@s181 yum.repos.d]# cat CentOS-Base.repo
[base]
name=CentOS-$releasever - Base - 163.com
baseurl=http://mirrors.163.com/centos/8-stream/BaseOS/x86_64/os/
gpgcheck=1
gpgkey=http://mirrors.163.com/centos/RPM-GPG-KEY-CentOS-7
[updates]
name=CentOS-$releasever - Updates - 163.com
baseurl=http://mirrors.163.com/centos/8-stream/BaseOS/x86_64/os/
gpgcheck=1
gpgkey=http://mirrors.163.com/centos/RPM-GPG-KEY-CentOS-7
[extras]
name=CentOS-$releasever - Extras - 163.com
baseurl=http://mirrors.163.com/centos/8-stream/extras/x86_64/os/
gpgcheck=1
gpgkey=http://mirrors.163.com/centos/RPM-GPG-KEY-CentOS-7
[centosplus]
name=CentOS-$releasever - Plus - 163.com
baseurl=http://mirrors.163.com/centos/8-stream/centosplus/x86_64/os/
gpgcheck=1
enabled=0
gpgkey=http://mirrors.163.com/centos/RPM-GPG-KEY-CentOS-7

```

### 2、切换为清华大学镜像源

  清华大学镜像源也是国内镜像源不错的站点，可以使用命令一步完成替换，更多信息可以参考官网。。

>  
 [root@s181 yum.repos.d]# sed -e ‘s|^mirrorlist=|#mirrorlist=|g’ -e ‘s|^#baseurl=http://mirror.centos.org/$contentdir|baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos|g’ -i.bak /etc/yum.repos.d/CentOS-Stream-*.repo <img src="https://img-blog.csdnimg.cn/direct/20f7ae9168cc44e0b46c5ee142994349.png" alt="在这里插入图片描述"> 


### 3、查看BaseOS源repo信息

>  
 [root@s181 yum.repos.d]# dnf repoinfo BaseOS Last metadata expiration check: 0:06:09 ago on Tue 12 Dec 2023 01:56:43 PM CST. Repo-id : baseos Repo-name : CentOS Stream 8 - BaseOS Repo-status : enabled Repo-revision : 8-stream Repo-distro-tags : [cpe:/o:centos-stream:centos-stream:8]: , , 8, C, O, S, S, a, e, e, m, n, r, t, t Repo-updated : Tue 12 Dec 2023 02:30:57 AM CST Repo-pkgs : 18,931 Repo-available-pkgs: 18,926 Repo-size : 33 G Repo-baseurl : https://mirrors.tuna.tsinghua.edu.cn/centos/8-stream/BaseOS/x86_64/os/ Repo-expire : 172,800 second(s) (last: Tue 12 Dec 2023 01:56:31 PM CST) Repo-filename : /etc/yum.repos.d/CentOS-Stream-BaseOS.repo Total packages: 18,931 

