
--- 
title:  rsync 将本地文件传输到远程机器 
tags: []
categories: [] 

---
要使用rsync向远程机器传输文件，需要先在本地机器上安装rsync，并确保远程机器能够通过ssh登录。

以下是具体步骤：
1. 在本地机器上安装rsync：
```
yum install rsync

```
1. 然后使用以下命令**将本地文件**传输到**远程**机器：
```
rsync -avz /local/path/to/file username@remote:/remote/path/to/destination

```

其中，/local/path/to/file是要传输的本地文件路径，username是远程机器的用户名，remote是远程机器的IP地址或域名，/remote/path/to/destination是文件在远程机器上的存储路径。
1. 如果需要通过ssh登录远程机器，请确保已经在本地机器上配置了ssh公钥，并且远程机器允许ssh公钥登录。如果还没有配置，请参考以下步骤：- 生成ssh密钥对
```
ssh-keygen

```
- 将公钥传输到远程机器
```
ssh-copy-id username@remote

```
1. 如果需要定期自动备份文件，可以使用crontab来设置定时任务。例如，每天凌晨3点备份一次文件：
```
0 3 * * * rsync -avz /local/path/to/file username@remote:/remote/path/to/destination

```

这样就可以实现在CentOS 7下使用rsync向远程机器传输文件了。
