
--- 
title:  服务器发送了一个意外的数据包。received:3,expected:20 
tags: []
categories: [] 

---
<img alt="" height="203" src="https://img-blog.csdnimg.cn/20210304185508416.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RvbW9ycm93QW5kVHV0dXJl,size_16,color_FFFFFF,t_70" width="336">

一般出现这个问题是由于新版的 sshd 可能与 XShell 存在兼容性问题（最近刚好 XShell 连接机器的时候出现了这个问题，根据自己的解决方法，稍微写一下）。

解决方法：在 XShell 连不上的那个机子上的 /etc/ssh/sshd_config 最后增加以下一行：

```
KexAlgorithms curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group14-sha1
```

然后：

```
systemctl restart sshd
```

当然，你可能会比较疑问？我都登录不上去，怎么才能进去设置呢？

其实这个时候，在其他的机子上是可以 ssh 过去的，像下面这样的格式**（或者先使用 MobaXterm 之类的工具登录进去也是不错的选择）**：

```
[root@master ~]# ssh -p xxxxx root@xxx.xxx.xx.xx

Authorized users only. All activities may be monitored and reported.
root@xxx.xxx.xx.xx's password: 

[root@localhost ~]# vim /etc/ssh/sshd_config 
```

如果 /etc/ssh/sshd_config 最后一行已经有 KexAlgorithms curve25519-sha256, *** 这些东东的话，你就不要再重复写一遍 KexAlgorithms 关键字了。

**错误操作（我最开始死脑筋一样重复写了，结果碰了一鼻子灰）：**

<img alt="" height="80" src="https://img-blog.csdnimg.cn/20210304190923968.png" width="1158">

**正确操作：**

你直接把要增加的内容追加到原有内容后边就好了**（还有一点，千万不要在逗号后边加一个空格，不然你 sshd 没法正常重启的）**。

**<img alt="" height="88" src="https://img-blog.csdnimg.cn/20210304190447662.png" width="1152">**

当然，修改以后，记得：

```
systemctl restart sshd
```

一般上面命令敲了之后没啥报错的话基本上就正常重启了，当再次 XShell 连接，应该就会正常提示你输入用户密码之类的了。 
