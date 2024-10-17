
--- 
title:  Linux - sed命令详解 
tags: []
categories: [] 

---
**目录**



























## sed命令

### 01.sed是什么？

sed全称是：Stream EDitor（流编辑器），是对文本字符串流进行过滤和转换（替换和删除）的编辑器。

### 02.sed的模式空间和保留空间

<img alt="" height="294" src="https://img-blog.csdnimg.cn/3e013eaf811c40878dd410dac1270c6d.png" width="638">

### 03.sed语法格式

>  
 1、sed [选项] sed编辑命令 输入文件 2、shell 命令 | sed [选项] sed编辑命令 3、sed [选项] -f sed脚本文件 输入文件 


### 04.sed常用选项

>  
 -n：只显示匹配处理的行（否则会输出所有的行） 
 -e：执行多个编辑命令时（一般用;代替） 
 -r：直接在文件进行修改，而不是输出到屏幕 
 -i：支持扩展正则 


#### -n选项

```
# 输出第一行
[root@localhost 7.6]# sed -n '1p' passwd 
root:x:0:0:root:/root:/bin/bash
# 输出最后一行
[root@localhost 7.6]# sed -n '$p' passwd 
mengmeng3:x:9943:9944::/home/mengmeng3:/bin/bash
# 输出第一行和第五行
[root@localhost 7.6]# sed -n '1p;5p' passwd 
root:x:0:0:root:/root:/bin/bash
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin


```

示例：查看以liu开头的行

```
[root@localhost 7.6]# sed -n '/^liu/p' passwd 
liudehua:x:1022:1022::/home/liudehua:/bin/bash

```

#### -i选项

-i选项会直接在原文进行修改，不会输出到屏幕

原文本：

```
[root@localhost 7.6]# cat fan.txt
wo ai chi fan ming you
fan ming you  fan ming you

```

将以fan开头的替换为liu

```
[root@localhost 7.6]# sed -i '/^fan/ s/fan/liu/g' fan.txt 
[root@localhost 7.6]# cat fan.txt 
wo ai chi fan ming you
liu ming you  liu ming you

```

将ai替换为111

```
[root@localhost 7.6]# sed -i 's/ai/111/g' fan.txt 
[root@localhost 7.6]# cat fan.txt 
wo 111 chi fan ming you
liu ming you  liu ming you

```

### 05.sed常用编辑命令

>  
 p：打印匹配行 print 
 d：删除指定行 delete 
 a：在匹配行后面追加 append 
 i：在匹配行前面插入insert 
 c：整行替换 
  r：将文件的内容读入 read 
 w：将文本写入文件 write 
 s：字符串替换（匹配正则表达式）substitution 
 =：输出行号 


#### p命令：

不连续的输出多行， ；是命令连接符

```
[root@localhost 7.6]# sed -n '1p;3p;5p' passwd 
root:x:0:0:root:/root:/bin/bash
daemon:x:2:2:daemon:/sbin:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin

```

 连续输出多行

```
[root@localhost 7.6]# sed -n '1,5p' passwd 
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin

```

 1~2p，从第一行开始，步长为2，每次间隔2行输出

```
[root@localhost 7.6]# cat -n passwd | sed -n '1~2p' | head -10
     1	root:x:0:0:root:/root:/bin/bash
     3	daemon:x:2:2:daemon:/sbin:/sbin/nologin
     5	lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
     7	shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
     9	mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
    11	games:x:12:100:games:/usr/games:/sbin/nologin
    13	nobody:x:99:99:Nobody:/:/sbin/nologin
    15	dbus:x:81:81:System message bus:/:/sbin/nologin
    17	sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
    19	chrony:x:998:996::/var/lib/chrony:/sbin/nologin

```

####  c命令

1.修改主机名/etc/hostname里的内容为你自己的名字

```
[root@localhost 7.6]# cat /etc/hostname 
lcoalhost.localdomain
[root@localhost 7.6]# sed -i '1c wangsh' /etc/hostname
[root@localhost 7.6]# cat /etc/hostname 
wangsh

```

#### s命令

** 2.修改selinux策略/etc/selinux/config里的SELINUX=enforcing修改为SELINUX=disabled**

```
[root@localhost 7.6]# sed -i '/^SELINUX=/ s/enforcing/disabled' /etc/selinux/config

```

**   3.禁用网卡 /etc/sysconfig/network-scripts/ifcfg-ens33的ONBOOT="yes"修改为ONBOOT="on"**

```
[root@localhost network-scripts]# sed -i '/^ONBOOT=/s/yes/no/' ifcfg-ens33 
[root@localhost network-scripts]# cat ifcfg-ens33 
BOOTPROTO="none" # 指定获得ip地址的引导协议，dhcp说明是动态获得，none是静态
NAME="ens33" # 网卡名字
UUID="20641fea-634f-424c-b9ea-3e2c6db49ea3" # 设备的唯一标识符
DEVICE="ens33" # 设备的名字
ONBOOT="no" # 系统启动的时候激活网卡，yes标识激活，no禁用
IPADDR=192.168.44.132 # 建议ip地址不能和别人冲突
NETMASK=255.255.255.0  # 指定子网掩码
GATEWAY=192.168.44.2  # 指定网关
DNS1=114.114.114.114 # 首选dns服务器
#DNS1=192.168.44.0 # 备用dns服务器

```

练习：

练习： 1.sed取出/etc/passwd文件的第一列 2.sed将PATH环境变量中的冒号换成换行  -&gt;可以将PATH变量的内容重定向到一个文件里，例如path.txt 3.sed将PATH环境变量斜杠/换成斜杠\ 4.sed修改SELINUX配置文件从开启(enforcing)变成禁用(disabled) /etc/sysconfig/selinux 5.去掉/etc/passwd文件中第二个字段的x 6.将/etc/sysconfig/network-scripts/ifcfg-ens33里的ONBOOT=no修改为yes或者修改下IPADDR后面的ip地址，具体ip自己定义 7.只显示ip add的ip地址 8.复制/etc/ssh/sshd_config到当前目录下，修改里面的端口号修改为8899 将#Port 22 配置修改为Port 8899 要求去掉前面的#号，将22修改为8899   9.给下列含有大写字母的行，在大写字母后追加数字2022  --》sed    abcdSdddde    islHishbxld    goBkefji    daanshXxge 不要直接对上面的源文件进行操作，建议复制到当前文件夹里进行  



 
