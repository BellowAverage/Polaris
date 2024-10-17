
--- 
title:  Linux之sqlserver客户端安装和使用简介 
tags: []
categories: [] 

---
## 一、前言

  测试环境需要与外部联调，外部数据库为sql server，需要通过VPN连接，而连接源地址限制只能通过VPN地址进行连接。我们在linux服务器上部署了测试环境，并安装了inodeclient，见博文。调试的还是开发人员还需要查询对方数据库的数据与接口调用进行比对，则需要在linux服务器上安装sql server客户端，通过客户端查询sql server库里的数据。博文实验环境说明：
- 操作系统：centos 7.6- mssql版本：17.10.1.1
## 二、sqlserver客户端安装

### 1、下载sqlserver yum源文件

>  
 [root@s146 ~]# curl https://packages.microsoft.com/config/rhel/7/prod.repo &gt; /etc/yum.repos.d/msprod.repo 


### 2、安装mssql-tools

  安装mssql-tools需要依赖unixODBC，虽然我们yum安装的时候使用了-y参数，但是在安装过程中还需要输入两次YES，需要接受许可证协议才能完成安装。

>  
 [root@s146 ~]# yum install -y ‘mssql-tools’ … Installed: mssql-tools.x86_64 0:17.10.1.1-1  Dependency Installed: msodbcsql17.x86_64 0:17.10.1.1-1 unixODBC.x86_64 0:2.3.7-1.rh  Complete! <img src="https://img-blog.csdnimg.cn/59e80458ced24ad2947ee647182dcf33.png" alt="在这里插入图片描述"> 


### 3、设置环境变量

  mssql-tools默认安装在/opt/mssql-tools/bin/路径下，要想使用sqlcmd、bcp命令，还需要我们将路径写入环境变量。

>  
 [root@s146 ~]# echo “export PATH=$PATH:/opt/mssql-tools/bin/” &gt;&gt; /etc/profile [root@s146 ~]# source /etc/profile 


### 4、验证命令是否安装成功

>  
 [root@s146 ~]# which sqlcmd /opt/mssql-tools/bin/sqlcmd [root@s146 ~]# which bcp /opt/mssql-tools/bin/bcp 


## 三、sqlcmd命令使用示例

### 1、获取命令帮助

>  
 [root@s146 ~]# sqlcmd -? <img src="https://img-blog.csdnimg.cn/5a78c44151b04e7d868fcfa2e13feb3e.png" alt="在这里插入图片描述"> 


### 2、登录远程sql server

  使远程登录sql server的语法为：****sqlcmd -S serverip -U 用户名 -P 密码****

>  
 [root@s146 ~]# sqlcmd -S x.x.x.x -U user-P ‘passwod’ 


### 3、查询实例下有哪些库

  使用如下命令可以查询sql server数据库实例下有哪些库，记住重要的一点，需要执行的命令输入结束后需要换行输入go命令哦，输入go命令sql语句才会正式执行。其中前4个库为sql server自带库。

>  
 &gt;select name from sys.databases go <img src="https://img-blog.csdnimg.cn/b478e7f504324ab2aeadae4aa5cc5110.png" alt="在这里插入图片描述"> 


### 4、查询表数据

  查询表的top n，即前N行数据。 <img src="https://img-blog.csdnimg.cn/ba068e6aa0e5451fade3e02516ef7e46.png" alt="在这里插入图片描述">
