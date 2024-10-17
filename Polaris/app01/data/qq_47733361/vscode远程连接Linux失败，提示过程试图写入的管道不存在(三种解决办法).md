
--- 
title:  vscode远程连接Linux失败，提示过程试图写入的管道不存在(三种解决办法) 
tags: []
categories: [] 

---
vscode报错如下： <img src="https://img-blog.csdnimg.cn/225b8322072e4808b067202ce8bd9f6b.png" alt="在这里插入图片描述">

#### 一、第一种情况

原因是本地的known_hosts文件记录服务器信息与现服务器的信息冲突了，导致连接失败。 解决方案就是把本地的known_hosts的原服务器信息全部删掉，然后重新连接。 <img src="https://img-blog.csdnimg.cn/1e6674fc4ea2409fbb62fea69dae9c05.png" alt="在这里插入图片描述">

#### 二、第二种情况

在编写配置文件config时，有些机器比较奇怪，要求必须添加端口号，才能成功，即

```
Port 22

```

#### 三、第三种情况

这也是我出现的问题，这里我把秘钥文件路径IdentityFile 初始写成了相对路径，即

```
IdentityFile ./id_rsa

```

<img src="https://img-blog.csdnimg.cn/225b8322072e4808b067202ce8bd9f6b.png" alt="在这里插入图片描述"> 出现了没有这个文件或目录的提示。

下面是一份完整配置：使用这份配置，在配置方面基本不会出问题

```
Host 120.46.83.82
     HostName 120.46.83.82
     User root
     Port 22
     PreferredAuthentications publickey
     IdentityFile ~/.ssh/id_rsa

```
