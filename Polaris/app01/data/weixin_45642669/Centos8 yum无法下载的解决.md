
--- 
title:  Centos8 yum无法下载的解决 
tags: []
categories: [] 

---
原因：sentos官方库移动了yum源的位置，导致yum无法获取列表。

操作：

```
cd /etc/yum.repos.d/
rm - r 
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo
yum clear all
yum makecache

```
