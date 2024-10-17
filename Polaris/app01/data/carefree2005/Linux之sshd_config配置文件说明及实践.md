
--- 
title:  Linux之sshd_config配置文件说明及实践 
tags: []
categories: [] 

---
## 一、sshd_config文件说明

  sshd_config 是 OpenSSH SSH 服务器守护进程配置文件，主要用于设置ssh server服务的相关参数，包括监听地址、监听端口、允许验证次数、是否允许root账户登录等等。sshd服务从/etc/ssh/sshd_config（或命令行中用-f指定的文件）读取配置数据。该文件包含关键字参数对，每行一对。以“#”开头的行和空行被解释为注释。参数可以用双引号（“）括起来，以表示包含空格的参数。改配置文件，只有root账户或者拥有root权限的账户可以配置和修改，配置文件修改后，重启sshd服务后参数生效。

## 二、使用实践

### 1、修改默认监听端口

  ssh server服务默认监听端口为22，为了系统安全，我们可以修改默认端口号。对应参数为Port，默认值为22，我们可以根据规划设置为指定端口。

>  
 [root@s142 ~]# cd /etc/ssh/ [root@s142 ssh]# vim sshd_config … Port 22222 … [root@s142 ssh]# systemctl restart sshd [root@s142 ssh]# netstat -tnpl Active Internet connections (only servers) Proto Recv-Q Send-Q Local Address Foreign Address State PID/Program name tcp 0 0 0.0.0.0:22222 0.0.0.0:* LISTEN 15808/sshd … <img src="https://img-blog.csdnimg.cn/d7e54acf794d46d7a4b1e0e50b593d22.png" alt="在这里插入图片描述"> 


### 2、指定监听地址

  如果服务器有多个网卡，我们只希望在某网卡提供sshd服务，则我们可以设置监听地址。

>  
 [root@s142 ssh]# vim sshd_config … ListenAddress 192.168.0.142 … [root@s142 ssh]# systemctl restart sshd [root@s142 ssh]# netstat -tnpl Active Internet connections (only servers) Proto Recv-Q Send-Q Local Address Foreign Address State PID/Program name tcp 0 0 192.168.0.142:22222 0.0.0.0:* LISTEN 15819/sshd … 


### 3、禁止root账户登录

  centos是默认运行root登录的，Ubuntu是默认禁止root登录的。如果我们需要禁止root账户登录，可以通过设置参数PermitRootLogin no，重启sshd服务后可以达到禁止root账户登录的目的。

>  
 [root@s142 ssh]# vim sshd_config … PermitRootLogin no … <img src="https://img-blog.csdnimg.cn/6c896c2f97c145049d112e45dde02820.png" alt="在这里插入图片描述"> 


### 4、设置每个连接最大允许的认证次数

  MaxAuthTries，指定每个连接最大允许的认证次数。默认值是 6 。如果失败认证的次数超过这个数值的一半，连接将被强制断开，且会生成额外的失败日志消息。

>  
 [root@s142 ssh]# vi sshd_config … MaxAuthTries 2 … …[root@s142 ssh]# ssh wuhs@192.168.0.142 -p 22222 wuhs@192.168.0.142’s password: Permission denied, please try again. wuhs@192.168.0.142’s password: Received disconnect from 192.168.0.142 port 22222:2: Too many authentication failures Authentication failed. <img src="https://img-blog.csdnimg.cn/4e6bfaf071aa414a87a491305e98ac38.png" alt="在这里插入图片描述"> 


### 5、设置Banner语

  设置登录前的横幅语，默认是空。Banner参数后参数值为路径及文件名。

>  
 [root@s142 ssh]# vi sshd_config … Banner /tmp/hi … [root@s142 ssh]# systemctl restart sshd [root@s142 ssh]# cat /tmp/hi 欢迎登陆s142 [root@s142 ssh]# systemctl restart sshd [root@s142 ssh]# ssh wuhs@192.168.0.142 -p 22222 欢迎登陆s142 wuhs@192.168.0.142’s password: 


### 6、登录后显示上次登录信息

  PrintLastLog参数控制是否显示上一次登录信息，默认是yes，即显示。通过登录信息我们可以了解上一次是否登录成功或者失败，会显示上一次登录的IP地址。这个信息有利有弊，利是可以显示上一次登录信息记录，如果显示陌生地址登录失败，说明有人在尝试登录服务器。弊端自然就是会暴露一些你实际的使用源地址信息。

>  
 Last failed login: Mon Sep 19 16:38:42 CST 2022 from s142 on ssh:notty There was 1 failed login attempt since the last successful login. Last login: Mon Sep 19 16:38:25 2022 from 192.168.0.32 <img src="https://img-blog.csdnimg.cn/d49a32ea428341afa80cdf046b899407.png" alt="在这里插入图片描述"> 


## 三、sshd_config配置文件参数说明

### 1、常见参数说明

  实际上sshd_config参数除了如下表格中，还有很多，只是我们大部分我们都使用默认值即可。如果想了解每个参数的用途和说明，我们可以使用man sshd_config命令进行查看。

<th align="left">参数</th><th align="left">默认值</th><th align="left">参数说明</th>
|------
<td align="left">Port</td><td align="left">22</td><td align="left">sshd服务默认的端口22，为了安全考虑建议修改成其它端口</td>
<td align="left">AddressFamily</td><td align="left">any</td><td align="left">设置协议簇，默认支持IPV4和IPV6</td>
<td align="left">ListenAddress</td><td align="left">0.0.0.0</td><td align="left">默认监听网卡所有的IP地址</td>
<td align="left">PermitRootLogin</td><td align="left">yes</td><td align="left">是否允许root登陆，默认是允许的，建议设置成no</td>
<td align="left">StrictModes</td><td align="left">yes</td><td align="left">当使用者的host key改变之后，server就不接受其联机</td>
<td align="left">MaxAuthTries</td><td align="left">6</td><td align="left">最多root尝试6次连接</td>
<td align="left">MaxSessions</td><td align="left">10</td><td align="left">最大允许保持多少个未认证的连接。默认值是 10 到达限制后，将不再接受新连接，除非先前的连接认证成功或超出 LoginGraceTime 的限制。</td>
<td align="left">PrintMotd</td><td align="left">yes</td><td align="left">登陆后是否显示一些默认信息</td>
<td align="left">PrintLastLog</td><td align="left">yes</td><td align="left">显示上次登录的信息</td>
<td align="left">TCPKeepAlive</td><td align="left">yes</td><td align="left">ssh server会传keepalive信息给client以此确保两者的联机正常，任何一端死后，马上断开</td>
<td align="left">PasswordAuthentication</td><td align="left">yes</td><td align="left">是否允许使用基于密码的认证。默认为”yes”。</td>
<td align="left">PermitEmptyPasswords</td><td align="left">no</td><td align="left">是否允许密码为空的用户远程登录。默认为”no”。</td>

### 2、相关重要文件说明
- ~/.ssh/known_hosts文件 ssh 会把每个你访问过的计算机的公钥（public key）都记录到~/.ssh/known_hosts文件中，当你下次访问该计算机时，openss会核对公钥。如果公钥不同，那openssh就会发出警告，避免你收到DNSHijack等攻.- /etc/host.allow和/etc/hosts.deny 这两个文件时控制远程访问设置的，通过该设置可以允许或者拒绝某个ip或者ip段访问linux的某项服务。我们可以用于限制访问服务器sshd服务的源地址，host.allow文件对应白名单，hosts.deny文件对应黑名单。
### 3、sshd_config配置文件验证

  我们可以使用sshd -t命令验证配置文件语法是否正确，如果配置文件中语法错误会有提示，我们根据提示修改配置文件即可。

>  
 [root@s142 ~]# sshd -t /etc/ssh/sshd_config: line 15: Bad configuration option: semanage /etc/ssh/sshd_config: terminating, 1 bad configuration options 

