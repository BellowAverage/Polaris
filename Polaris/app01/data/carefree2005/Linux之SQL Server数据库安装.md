
--- 
title:  Linux之SQL Server数据库安装 
tags: []
categories: [] 

---
## 一、SQL Server简介

  SQL Server 是一个关系数据库管理系统。它最初是由Microsoft Sybase 和Ashton-Tate三家公司共同开发的，于1988 年推出了第一个OS/2 版本。在Windows NT 推出后，Microsoft与Sybase 在SQL Server 的开发上就分道扬镳了，Microsoft 将SQL Server 移植到Windows NT系统上，专注于开发推广SQL Server 的Windows NT 版本。Sybase 则较专注于SQL Server在UNIX 操作系统上的应用。SQL Server数据库是Microsoft开发设计的一个关系数据库智能管理系统(RDBMS)，现在是全世界主流数据库之一。博文将介绍在linux环境下安装SQL Server数据库及客户端工具，博文实验环境如下：
- 操作系统：centos7.6- SQL Server版本：SQL Server2019
## 二、安装SQL Server

### 1、下载SqlServer的yum源文件

>  
 [root@s142 opt]# curl -o /etc/yum.repos.d/mssql-server.repo https://packages.microsoft.com/config/rhel/7/mssql-server-2019.repo % Total % Received % Xferd Average Speed Time Time Time Current Dload Upload Total Spent Left Speed 100 231 100 231 0 0 196 0 0:00:01 0:00:01 --:–:-- 196 


### 2、查看repo文件

  我们可以看到就是从微软官网链接完成下载，SQLServer虽然是微软开发的，目前已经支持windows、linux、MACOS等。

>  
 [root@s142 opt]# cat /etc/yum.repos.d/mssql-server.repo [packages-microsoft-com-mssql-server-2019] name=packages-microsoft-com-mssql-server-2019 baseurl=https://packages.microsoft.com/rhel/7/mssql-server-2019/ enabled=1 gpgcheck=1 gpgkey=https://packages.microsoft.com/keys/microsoft.asc 


### 3、yum安装SQL Server

>  
 [root@s142 opt]# yum install -y mssql-server … Installed: mssql-server.x86_64 0:15.0.4261.1-2 … Dependency Updated: cyrus-sasl-lib.x86_64 0:2.1.26-24.el7_9 … Complete! 


### 4、执行SQL Server初始化

>  
 [root@s142 opt]# /opt/mssql/bin/mssql-conf setup 


### 5、选择版本

<img src="https://img-blog.csdnimg.cn/f2976acd355245c2b61a9baca5e31b78.png" alt="在这里插入图片描述">

### 6、设置数据库管理员密码

  输入Yes接受软件试用协议，输入两次数据库管理员密码完成DBA账户设置。然后就完成了SQL Server的安装，非常简单。 <img src="https://img-blog.csdnimg.cn/1eff199a28c34095b128e11a70d63865.png" alt="在这里插入图片描述">

### 7、检查SQL Server服务

  监控监听端口，可以看到sqlserver默认的1433端口已经监听，查看SQL Server服务状态，已经是active状态。说明sqlserver我们已经安装就绪，可以使用了。 <img src="https://img-blog.csdnimg.cn/282ca4d618c64402b8acdc5e62d71e4d.png" alt="在这里插入图片描述">

## 三、安装SQL Server客户端工具

### 1、下载客户端工具yum源文件

>  
 [root@s142 opt]# curl -o /etc/yum.repos.d/msprod.repo https://packages.microsoft.com/config/rhel/7/prod.repo % Total % Received % Xferd Average Speed Time Time Time Current Dload Upload Total Spent Left Speed 100 193 100 193 0 0 268 0 --:–:-- --:–:-- --:–:-- 268 


### 2、安装sqlserver客户端工具

>  
 [root@s142 opt]# yum install -y mssql-tools unixODBC-devel … Do you accept the license terms? (Enter YES or NO) YES … Do you accept the license terms? (Enter YES or NO) YES … Installed: mssql-tools.x86_64 0:17.10.1.1-1 unixODBC-devel.x86_64 0:2.3.7-1.rh 


### 3、添加环境变量

  客户端工具默认安装路径/opt/mssql-tools/bin/，为了方便使用我们可以把命令路径写入环境变量中，这样可以任意路径下发起sqlcmd本地连接。

>  
 [root@s142 opt]# echo ‘export PATH=“$PATH:/opt/mssql-tools/bin”’ &gt;&gt; ~/.bash_profile [root@s142 opt]# echo ‘export PATH=“$PATH:/opt/mssql-tools/bin”’ &gt;&gt; ~/.bashrc [root@s142 opt]# source ~/.bashrc [root@s142 opt]# which sqlcmd /opt/mssql-tools/bin/sqlcmd 


## 四、连接测试

### 1、本地连接
- 本地登录 本地登录使用-S指定IP地址，-U指定用户，-P指定输入密码，不带-P则会进入输入密码交互模式。登录成功显示1&gt;，如果需要退出则可以使用quit和:exit，此模式下除了go命令直接输入，其他命令则需要使用冒号开头，例如输入:help获取帮助。
>  
 [root@s142 opt]# sqlcmd -S 127.0.0.1 -U sa Password: 1&gt; 

- 查看版本 本地连接状态下输入select @@version和go可以查看到版本信息。 <img src="https://img-blog.csdnimg.cn/3ba4f407b81741d494041893256fff12.png" alt="在这里插入图片描述">- 获取帮助 <img src="https://img-blog.csdnimg.cn/31893f0c573642bfa6adb69d12044a95.png" alt="在这里插入图片描述">
### 2、远程连接
- 新建sqlserver连接 使用数据库连接客户端连接sqlserver，输入数据库IP地址，账户密码，sqlserver管理员默认账户名sa。 <img src="https://img-blog.csdnimg.cn/a6e098cf090741ea9ae8a15bc4da1178.png" alt="在这里插入图片描述">- 查询版本 输入select @@version查询语句，执行sql语句后可以看到数据库的版本信息。 <img src="https://img-blog.csdnimg.cn/ff54d662a65b4e408eb839ee08d1d737.png" alt="在这里插入图片描述">