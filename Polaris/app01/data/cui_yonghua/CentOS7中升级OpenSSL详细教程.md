
--- 
title:  CentOS7中升级OpenSSL详细教程 
tags: []
categories: [] 

---


#### 文章目录
- <ul><li>- - <ul><li>- - 


### 一. 引言

**OpenSSL**: <mark>是用于保护数据安全的重要工具。它能提供加密，解密等多项功能。</mark> 然而，随着技术的发展和新的安全漏洞的出现，使用最新版本的 OpenSSL 成为了重要的需求。

想了解更多可进入官网：

有些较新的应用只能安装在openssl3上，所以不更换centos7只能升级。

本文记录如何在 CentOS 7 上升级 OpenSSL。会逐步介绍所需步骤，包括备份，下载和安装，以及配置等。

注意：安装的时候，必须 <mark>有方式可以直接操作到系统</mark>，而不是通过xshell等工具，因为在一开始备份旧的openssl后，如果系统刷新后就断开连接，所以需要在能直接操作系统前提下进行安装升级

### 二. 升级前的准备

#### 1.备份现有配置

执行查找命令 `find /usr -name openssl`,例如查找出来的是 <mark>/usr/bin/openssl</mark> 和 <mark>/usr/lib64/openssl</mark> 则执行拷贝命令:

```
[root@localhost ~]# find /usr -name openssl
/usr/bin/openssl
/usr/lib64/openssl
[root@localhost ~]# cp -r /usr/bin/openssl /usr/bin/openssl_backup
[root@localhost ~]# cp -r /usr/lib64/openssl /usr/lib64/openssl_backup

```

#### 2. 检查系统版本

我们需要确认当前的 CentOS 和 OpenSSL 的版本，以确定升级的需求。例如，我们可以使用命令 `cat /etc/centos-release` 和 `openssl version` 来检查。

```
[root@localhost ~]# cat /etc/centos-release
CentOS Linux release 7.6.1810 (Core) 
[root@localhost ~]# openssl version
OpenSSL 1.0.2k-fips  26 Oct 2023
[root@localhost ~]# 

```

#### 3. 安装依赖

安装所需的依赖

```
yum -y install gcc perl make zlib-devel perl-CPAN

```

然后安装 IPC::Cmd模块：`cpan IPC::Cmd`，此过程会有几次交互，直接按y即可

### 三. OpenSSL安装

```
# 下载包
wget https://github.com/openssl/openssl/releases/download/openssl-3.1.1/openssl-3.1.1.tar.gz

# 解压
tar -zxvf openssl-3.1.1.tar.gz

# 进入解压后的文件夹，执行配置
./config --prefix=/usr/local/ssl --openssldir=/usr/local/ssl shared zlib

# 执行编译命令
make

# 执行安装命令
make install

# 配置动态库链接
echo "/usr/local/ssl/lib64" &gt; /etc/ld.so.conf.d/openssl.conf

# 更新系统的库缓存
ldconfig

# 替换旧版的目录
cp /usr/local/ssl/bin/openssl /usr/bin/openssl

# 使用新的OpenSSL版本
ldconfig -v

```

### 四. 验证

执行：`openssl version` 命令打印当前的版本:

```
# openssl version
OpenSSL 3.1.1 30 May 2023 (Library: OpenSSL 3.1.1 30 May 2023)

```
