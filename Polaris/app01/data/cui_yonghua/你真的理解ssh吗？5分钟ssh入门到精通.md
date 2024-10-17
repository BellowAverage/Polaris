
--- 
title:  你真的理解ssh吗？5分钟ssh入门到精通 
tags: []
categories: [] 

---
SSH 为 <mark>Secure Shell</mark> 的缩写，`它是建立在应用层基础上的安全协议。SSH 是较可靠，专为远程登录会话和其他网络服务提供安全性的协议`。利用 SSH 协议可以有效防止远程管理过程中的信息泄露问题。SSH最初是UNIX系统上的一个程序，后来又迅速扩展到其他操作平台，目前SSH在几乎所有 UNIX 平台上受到支持。

SSH 协议存在以下特征：
- 有效防止远程管理过程中的信息泄漏- 传输数据加密，能够防止DNS和IP欺骗- 传输数据压缩，加快传输速度
### 一. 基础使用

<mark>OpenSSH</mark> 是 SSH协议的流行的免费开源实现。OpenSSH提供了服务端程序(openssh-server)和客户端工具(openssh-client)。

UNIX 平台系统（Linux/MacOS）等一般都默认安装了 SSH 客户端，直接在终端中使用SSH命令即可，Windows 等其它平台则需要手动安装 SSH 客户端，较常用的Windows SSH客户端有Putty和XShell等。

Ubuntu/Debian的安装方式如下：

```
# 安装服务端/客户端(Ubuntu/Debian)
$ sudo apt install openssh-server/openssh-client

# 查看ssh服务是否开启
$ netstat -tlp | grep ssh

# 启动/停止/重启 ssh服务
$ sudo /etc/init.d/ssh start/stop/restart

```

SSH服务端配置文件默认为/etc/ssh/sshd_config，可以按需修改默认22端口等配置。

```
# 命令格式
# user远程服务器登录的用户名，默认为当前用户
# hostname远程服务器地址。可以是IP/域名/别名
# exit或logout命令均可退出当前登录
$ ssh [-options] [user@hostname]

```

|options|含义
|------
|-p|指定ssh端口号,默认端口为22
|-i|使用指定私钥文件连接服务器免密登录

样例如下：

```
# 以root用户登录192.168.1.196的到ssh服务器
$ ssh root@192.168.1.196

# 以root用户登录到192.168.1.198的ssh服务器，使用2222端口
$ ssh -p 2222 root@192.168.1.198


```

### 二. SSH高级配置

SSH配置信息一般保存在 `~/.ssh` 目录下。

|配置文件|作用
|------
|known_hosts|作为客户端。记录曾连接服务器授权。SSH第一次连接一台服务器会有一个授权提示，确认授权后会记录在此文件中，下次连接记录中的服务器时则不再需要进行授权确认提示
|authorized_keys|作为服务端。客户端的免密连接公钥文件
|config|作为客户端。记录连接服务器配置的别名

#### 2.1 服务器别名

远程管理命令(如ssh,scp等)连接一台服务器时一般都需要提供 服务器地址、端口、用户名 ，每次输入比较繁琐，我们可以把经常使用的服务器连接参数打包记录到配置文件中并为其设置一个简单易记的别名。这样我们就可以通过别名方便的访问服务器，而不需要提供地址、端口、用户名等信息了。

配置方法如下：

创建或打开 `~/.ssh/config`，在文件追加服务器配置信息 一台服务器配置格式如下：（以下配置中只有HostName是必选项，其他都可按需省略。）

```
Host ColinMac
  HostName 192.168.1.196
  User colin
  Port 22

```

配置完成后远程管理命令中就可以直接使用别名访问了。

```
$ ssh ColinMac
$ scp abc.txt ColinMac:Desktop

```

#### 2.2 免密登录

```
# 命令格式
$ ssh-keygen [-options]

```

|options|含义
|------
|-t|指定加密类型,默认为非对称加密(rsa), 所有可选项[dsa,ecdsa,ed25519,rsa]
|-f|密钥文件名。
|-C|注释，将附加在密钥文件尾部

远程管理命令(如ssh,scp等)每次都需要提供用户密码保证安全。除此之外，我们也可配置使指定加密算法验证密钥文件的方式，避免每次输入密码 配置免密登录后，ssh连接和scp等远程管理命令都不需要再输密码 生成密钥时若指定了文件名，连接服务器时需要通过-i指定要验证的密钥文件,形如：`ssh -i file user@host`。默认文件名则可省略 默认配置只需以下两步：

```
# 客户端生成密钥对
$ ssh-keygen

# 上传公钥到服务器
$ ssh-copy-id user@hostname   # 文件会自动上传为服务器特定文件 ～/.ssh/authorized_keys


```

完成以上步骤后直接使用`ssh ColinUbuntu`即可登录，服务器地址和密码均不用录入。

#### 2.3 免密钥文件登录

出于安全考虑，大部分服务器提供商如要求使用密钥文件进行远程登录，如GCP和AWS。下面我们以GCP为例来看如何简化连接操作,这搞起来吧…

##### 2.3.1 生成密钥对

```
$ ssh-keygen -t rsa -f ~/.ssh/[KEY_FILENAME] -C [USERNAME]
$ chmod 400 ~/.ssh/[KEY_FILENAME]


```



##### 2.3.2 上传公钥

在Compute Engine页面左侧菜单找到元数据,将上一步生成的公钥文件(KEY_FILENAME_pub)内容添加到SSH密钥中即可。 <img src="https://img-blog.csdnimg.cn/direct/9a37de79624c450e81cfe32cb7ee010b.png" alt="在这里插入图片描述">

##### 2.3.3 连接GCP

使用以下命令登录即可

```
$ ssh -i ~/.ssh/KEY_FILENAME [USERNAME]@[IP_ADDRESS]

```

##### 2.3.4 简化登录

以上是GCP官方步骤，使用IdentityFile方式进行登录，每次登录都要通过-i选项指定私钥路径比较繁琐，我们可以将密钥文件添加到ssh客户端config中以简化连接命令。

```
Host *
 AddKeysToAgent yes
 UseKeychain yes  # only for mac

Host tu
   HostName IP_ADDRESS
   Port 22
   User USERNAME
   IdentityFile ~/.ssh/gcp


```

按照以上配置添加到`～/.ssh/config`中

```
# 后台运行ssh-agent
$ eval "$(ssh-agent -s)"
# 添加密钥到ssh-agent
$ ssh-add -K ~/.ssh/gcp


```

完成以上配置后，连接服务器只需使用 `ssh tu` 即可。

除了连接云服务器，GitHub等服务也可是通过以上方式连接
