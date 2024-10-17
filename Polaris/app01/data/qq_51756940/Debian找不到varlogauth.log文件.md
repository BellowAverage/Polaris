
--- 
title:  Debian找不到/var/log/auth.log文件 
tags: []
categories: [] 

---
#### 检查rsyslog是否正常运行

```
 ps -aux | grep rsyslog
```

<img alt="" height="147" src="https://img-blog.csdnimg.cn/direct/9b720761c14d491da5b94d86ffe5c435.png" width="1148">

**通常情况下，`rsyslog` 负责处理和转发系统日志，包括 SSH 日志。**

#### **安装 rsyslog**

```
sudo apt-get install rsyslog
```

#### **启动和启用 rsyslog 服务**

```
sudo systemctl start rsyslog
sudo systemctl enable rsyslog
```

**确认 rsyslog 服务运行**

```
systemctl status rsyslog
```

#### <img alt="" height="293" src="https://img-blog.csdnimg.cn/direct/fba153980b2745b3975086906d94e59f.png" width="983">

#### 重启ssh服务

```
sudo systemctl restart sshd
```

<img alt="" height="161" src="https://img-blog.csdnimg.cn/direct/218a0b88d43d48a9bea9b61190740d11.png" width="653">






