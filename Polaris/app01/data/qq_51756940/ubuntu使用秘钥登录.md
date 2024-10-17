
--- 
title:  ubuntu使用秘钥登录 
tags: []
categories: [] 

---


1.生成SSH密钥对

```
ssh-keygen

```

该命令将提示您输入要在其中保存密钥对的文件名以及一个密码（如果需要）。默认情况下，它将在~/.ssh目录中生成密钥对。

2.将公钥添加到授权密钥文件

```
cat ~/.ssh/id_rsa.pub &gt;&gt; ~/.ssh/authorized_keys

```

这将将公钥添加到授权密钥文件中，以便可以使用SSH密钥对进行身份验证。

3.更改权限

```
chmod 600 ~/.ssh/authorized_keys
```

<img alt="" height="120" src="https://img-blog.csdnimg.cn/73f13099851443d8bf9d7821f6f35501.png" width="681">

**id_rsa就是私钥，用这个登录，拷贝到本地就可以删除服务器上的了。 **

4.禁用密码登录

```
sudo vim /etc/ssh/sshd_config

```

编辑SSH配置文件来禁用密码登录。

在该文件中找到以下行

PasswordAuthentication yes

#PubkeyAuthentication yes

将其修改为

PasswordAuthentication no

PubkeyAuthentication yes

以上意思为启用秘钥登录，禁用密码登录。

<img alt="" height="45" src="https://img-blog.csdnimg.cn/9df52df0b69a4f958a9b23b05594f205.png" width="235">

 <img alt="" height="45" src="https://img-blog.csdnimg.cn/edd65036264542aabd0e8403b93992c3.png" width="214">

 5.重启SSH服务

```
sudo systemctl restart sshd

```

现在，需要使用SSH密钥对进行身份验证才能登录到服务器上。
