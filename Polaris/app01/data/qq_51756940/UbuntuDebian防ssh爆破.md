
--- 
title:  Ubuntu/Debian防ssh爆破 
tags: []
categories: [] 

---
**目录**











输入 lastb 指令查看尝试登录的ip，可以看到有个ip一直尝试爆破。<img alt="" height="295" src="https://img-blog.csdnimg.cn/direct/6f09719b6fab4fce940d663adcc156db.png" width="899">

##### 1、安装fail2ban

```
sudo apt-get update
sudo apt-get install fail2ban
```

##### 2、**配置 Fail2ban**

复制默认配置文件以创建一个可编辑的配置文件

```
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

```

编辑 `jail.local` 文件来配置 SSH 的保护规则。

```
sudo vim /etc/fail2ban/jail.local
```

在 `jail.local` 文件中，找到与 SSH 相关的部分（通常是 `[sshd]` 或 `[ssh]`），并配置相关参数

```
port    = 22222
logpath = %(sshd_log)s
backend = %(sshd_backend)s
maxretry = 3
bantime = 3600
```

其中port是ssh端口， `maxretry` 是尝试次数限制，`bantime` 是封禁时长（秒）

<img alt="" height="193" src="https://img-blog.csdnimg.cn/direct/a381ba8ca1c34e1988f4e9cd6205de57.png" width="622">

##### 3、**重启 Fail2ban 服务**

修改配置后，重启 `fail2ban` 服务以应用更改

```
sudo systemctl restart fail2ban

```

##### 4、**检查 Fail2ban 状态**

检查 `fail2ban` 的状态和封禁的 IP 列表

```
sudo fail2ban-client status sshd

```

<img alt="" height="238" src="https://img-blog.csdnimg.cn/direct/f83b157a380349e5bbf8d8a3ac33eea2.png" width="515">


