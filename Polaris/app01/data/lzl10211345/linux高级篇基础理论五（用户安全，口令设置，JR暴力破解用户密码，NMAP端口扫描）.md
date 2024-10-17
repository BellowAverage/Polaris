
--- 
title:  linux高级篇基础理论五（用户安全，口令设置，JR暴力破解用户密码，NMAP端口扫描） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**不能因为人生的道路坎坷,就使自己的身躯变得弯曲;不能因为生活的历程漫长,就使求索的 脚步迟缓。** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 ♥️**感谢CSDN让你我相遇！** 


运维人员辛苦和汗水总结的干货理论希望对你有所帮助

<img alt="" height="80" src="https://img-blog.csdnimg.cn/fd3fee85df1d4cffba97164ba01cdf81.gif" width="640">

**目录**



































### 用户安全

#### 1、系统账户清理

（1）将非登录用户的shell设为/sbin/nologin     useradd  -s   /sbin/nologin 用户名     usermod -s   /sbin/nologin 用户名 （2）锁定长期不使用的账户     usermod  -L   用户名     passwd   -l   用户名     解锁：    usermod    -U   用户名             passwd    -u    用户名 （3）删除无用的账户     userdel     -r    用户 （4）锁定账号文件passwd，shadow     锁定：chattr    +i    /etc/passwd  /etc/shadow     查看:   lsattr     /etc/passwd   /etc/shadow     解锁：chattr    -i    /etc/passwd   /etc/shadow

#### 2、密码的安全控制：

（1）设置密码有效期： 修改/etc/login.defs文件：适用于新建用户 PASS_MAX_DAYS  9999                 //修改本行后数字 chage  -M   数字  用户：    适用于已有用户 （2）用户下次登录修改密码 chage   -d     0    用户

#### 3、命令历史限制：

减少记录的命令条数：/etc/profile HISTSIZE=1000              // 最后执行脚本   . /etc/profile 清空命令历史：history     -c

#### 4、字符终端自动注销：

修改 vim   ~/.bash_profile export    TMOUT=600                           //(秒)

#### 5、su命令：

用于切换用户 语法: su - 用户名 密码验证规则：         root用户切换到任意用户，不验证密码         普通用户切换到任意其他用户，验证目标用户的密码 su的日志文件：/var/log/secure

####  6、suod命令：

提示权限（以root用户身份执行授权命令） 语法：sudo   授权命令 配置sudo授权：     visudo   或  vi   /etc/sudoers     语法格式：   用户名      主机名列表=命令程序；列表 查看sudo所给用户的权限：sudo    -l sudo的日志文件：/var/log/sudo

#### 7、限制root用户只能在安全终端登录

    vim   /etc/securetty

tty1--表示图形终端（Ctrl+alt+f1） tty2--tty6表示字符终端（Ctrl+alt+f2-f6）

#### 8、禁止普通用户登录

禁止：touch  /etc/nologin 取消：rm  -rf  /etc/nologin

### JR软件：

###### 1.下载并安装John the Ripper

是一款密码分析工具，支持暴力破解，将检测密码强度。John the Ripper的官方网站是http:/www.openwall.com/john/,通过该网站可以获取稳定版源码包，如john-1.8.0.tar.gz。 以源码包john-1.8.0.tr.gz为例，解压后可看到三个子目录一doc、run、src,分别表示手册 文档、运行程序、源码文件，除此之外还有一个链接的说明文件README。其中，doc目录下包括 README、INSTALL、EXAMPLES等多个文档，提供了较全面的使用指导。

<img alt="" height="287" src="https://img-blog.csdnimg.cn/436efbaf347d4d729554d4f50c014337.png" width="720">

切换到src子目录并执行“make clean linux--x86-64”命令，即可执行编译过程。若单独执行 mke命令，将列出可用的编译操作、支持的系统类型。编译完成以后，run子目录下会生成一个名为john的可执行程序。

<img alt="" height="151" src="https://img-blog.csdnimg.cn/c77af0fa3b7640f0b7deffbf377250e4.png" width="500">

John the Ripper不需要特别的安装操作，编译完成后的run子目录中包括可执行程序john及相关 的配置文件、字典文件等，可以复制到任何位置使用。

###### 2.检测弱口令账号

在安装有John the Ripper的服务器中，可以直接对/etc/shadow文件进行检测。对于其他Linux服务器，可以对shadow文件进行复制，并传递给john程序进行检测。只需执行run目录下的john程 序，将待检测的shadow文件作为命令行参数，就可以开始弱口令分析了。

<img alt="" height="342" src="https://img-blog.csdnimg.cn/1ad383eddcbf4f49b3b8951bff10a623.png" width="871">

在执行过程中，分析出来的弱口令账号将即时输出，第一列为密码字串，第二列的括号内为相 应的用户名（如用户kadmin的密码为“123456"）。默认情况下，john将针对常见的弱口令设置特点， 尝试破解已识别的所有密文字串，如果检测的时间太长，可以按C+C组合键强行终止。破解出的 密码信息自动保存到john.pot文件中，可以结合“--show”选项进行查看。

<img alt="" height="202" src="https://img-blog.csdnimg.cn/65646f9bc3d740dd9f404837a26f1bf0.png" width="830">

###### 3.使用密码字典文件

对于密码的暴力破解，字典文件的选择很关键。只要字典文件足够完整，密码破解只是时间上 的问题。因此，“什么样的密码才足够强壮”取决于用户的承受能力，有人认为超过72小时仍无法 破解的密码才算安全，也可能有人认为至少暴力分析一个月仍无法破解的密码才足够安全。 John the Ripper默认提供的字典文件为password.lst,其列出了3OO0多个常见的弱口令。如果有 必要，用户可以在字典文件中添加更多的密码组合，也可以直接使用更加完整的其他字典文件。执 行john程序时，可以结合“--wordlist==”选项来指定字典文件的位置，以便对指定的密码文件进行 暴力分析。

<img alt="" height="319" src="https://img-blog.csdnimg.cn/7a4e9acc7bd44eeab4ecf4a7430a00c7.png" width="872">

从上述结果可以看出，由于字典文件中的密码组合较少，因此仅破解出其中四个账号的口令。 也不难看出，像“123456”   “iloveyou”之类的密码有多脆弱了。

### NMAP软件：

是一款强大的网络扫描，安全检测 VB你们不能

###### NMAP扫描类型：

-sS,TCP SYN扫描（半开扫描）：只向目标发出SYN数据包，如果收到SYN/ACK响应包 就认为目标端口正在监听，并立即断开连接；否则认为目标端口并未开放

-sT,TCP连接扫描：这是完整的TCP扫描方式，用来建立一个TCP连接，如果成功则认为 目标端口正在监听服务，否则认为目标端口并未开放。

-sF,TCP FIN扫描：开放的端口会忽略这种数据包，关闭的端口会回应RST数据包。许多 防火墙只对SYN数据包进行简单过滤，而忽略了其他形式的TCP攻击包。这种类型的扫描 可间接检测防火墙的健壮性。

-sU,UDP扫描：探测目标主机提供哪些UDP服务，UDP扫描的速度会比较慢。

-sP,ICP扫描：类似于pig检测，快速判断目标主机是否存活，不做其他扫描。

-P0,跳过pig检测：这种方式认为所有的目标主机是存活的，当对方不响应CP请求时， 使用这种方式可以避免因无法pig通而放弃扫描。


