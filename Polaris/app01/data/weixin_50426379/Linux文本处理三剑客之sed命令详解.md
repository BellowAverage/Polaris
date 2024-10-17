
--- 
title:  Linux|文本处理三剑客之sed命令详解 
tags: []
categories: [] 

---


#### 文章目录
- <ul><li>- <ul><li>- - - <ul><li>- - - 


### sed命令

主要对<mark>文本进行替换和修改</mark>等操作

```
[root@wh 0706]# man sed
	sed - stream editor for filtering and transforming text
	#文本字符串流的过滤和转换编编辑器

```

#### sed命令处理文本的过程：

文本处理主要在pattern space

<img src="https://img-blog.csdnimg.cn/img_convert/bbeb8db5f1fceed9ce53a67bd78e0412.png" alt="image.png">

#### sed的常用选项：

>  
 <mark>-n：只显示匹配处理的行</mark> 
 -e：执行多个编辑命令时（<mark>一般用 ; 代替</mark>） 
 <mark>-i：直接在原文件中进行修改，而不是输出到屏幕</mark> 
 <mark>-r：支持扩展正则表达式</mark> 
 -f：从脚本文件中读取内容并执行 


```
# -i 直接修改原文件
# /^fan/ 匹配正则 以fan开头
# s 替换 将fan替换为liu  g--》一行有多个的换全部替换
[root@wh 0706]# sed -i "/^fan/ s/fan/liu/g" fan.txt 
[root@wh 0706]# cat fan.txt 
wo ai chi fan ming you
liu ming you liu ming you

# 将you替换为空
[root@wh 0706]# sed -i 's/you//g' fan.txt 
[root@wh 0706]# cat fan.txt 
wo ai chi fan ming 
liu ming  liu ming 

# 不接-i选项，会标准输出到屏幕，不会修改原文件
[root@wh 0706]# cat sc.txt 
zhaojunjie changchuang
huangzian  changsha  male
duanyouxu  taohuadao daozhu
liuchang   dajiaoshi
zhangsan dajiaoshi 12345
[root@wh 0706]# cat sc.txt |sed '/liu/ s/chang/san/'
zhaojunjie changchuang
huangzian  changsha  male
duanyouxu  taohuadao daozhu
liusan   dajiaoshi
zhangsan dajiaoshi 12345
[root@wh 0706]# cat sc.txt 
zhaojunjie changchuang
huangzian  changsha  male
duanyouxu  taohuadao daozhu
liuchang   dajiaoshi
zhangsan dajiaoshi 12345

# -n：只显示匹配处理的行
[root@wh 0706]# sed -n '1,3p' /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin

# -r 支持扩展正则
[root@wh 0706]# sed -rn '/^#|^$/!p' /etc/login.defs 
MAIL_DIR	/var/spool/mail
PASS_MAX_DAYS	99999
PASS_MIN_DAYS	0
PASS_MIN_LEN	5
PASS_WARN_AGE	7 

```

#### sed的常用编辑命令：

sed操作：

​ 1.根据行号

​ 2.根据字符串（支持正则）

>  
 p：打印匹配行 print 
 d：删除指定行 delete 
 a：在匹配行后面追加append 
 i：在匹配行前面插入insert 
 c：整行替换 
 r：将文件的内容读入 read 
 w：将文本写入文件 write 
 s：字符串替换（匹配正则表达式） substitution 
 =：输出行号 


```
# p 打印匹配行
# 显示文件的第一行和最后一行，$ 最后
[root@wh 0706]# sed -n '1p;$p' /etc/passwd
root:x:0:0:root:/root:/bin/bash
mengmeng2:x:12431:12431::/home/mengmeng2:/bin/bash
--------------------
# d 删除
[root@wh 0706]# cat fan.txt 
zhaojunjie wangshenghu zhengyang
liuchang zhangchang
wo ai chi fan ming 
yangyongjie lijunlin

[root@wh 0706]# sed -i '$d' fan.txt  #删除最后一行
[root@wh 0706]# cat fan.txt 
zhaojunjie wangshenghu zhengyang
liuchang zhangchang
wo ai chi fan ming 
yangyongjie lijunlin
# 删除包含wo的那行
[root@wh 0706]# sed -i '/wo/d' fan.txt 
[root@wh 0706]# cat fan.txt 
zhaojunjie wangshenghu zhengyang
liuchang zhangchang
yangyongjie lijunlin
--------------------
# a 在...后面追加
[root@wh 0706]# cat fan.txt 
wo ai chi fan ming 
# 在第1行后面追加shenjiemi
[root@wh 0706]# sed -i '1a shenjiemi' fan.txt 
[root@wh 0706]# cat fan.txt 
wo ai chi fan ming 
shenjiemi
--------------------
# i 在...前面插入
# 在第1行前面插入
[root@wh 0706]# sed -i '1i zhaojunjie wangshenghu zhengyang' fan.txt 
[root@wh 0706]# cat fan.txt 
zhaojunjie wangshenghu zhengyang
wo ai chi fan ming 
shenjiemi
# 在包含fan这行的前面插入
[root@wh 0706]# sed -i '/fan/i chenxiongwei zhouyiwei' fan.txt 
[root@wh 0706]# cat fan.txt 
zhaojunjie wangshenghu zhengyang
chenxiongwei zhouyiwei
wo ai chi fan ming 
shenjiemi
--------------------
# c 整行替换
# 将包含shenjiemi的整行替换成yangyongjie lijunlin
[root@wh 0706]# sed -i '/shenjiemi/c yangyongjie lijunlin' fan.txt 
[root@wh 0706]# cat fan.txt 
zhaojunjie wangshenghu zhengyang
chenxiongwei zhouyiwei
wo ai chi fan ming 
yangyongjie lijunlin
#将第2行替换
[root@wh 0706]# sed -i '2c liuchang zhangchang' fan.txt 
[root@wh 0706]# cat fan.txt 
zhaojunjie wangshenghu zhengyang
liuchang zhangchang
wo ai chi fan ming 
yangyongjie lijunlin
--------------------
# s 替换
# 将以ONBOOT开头的行中的yes替换成no
[root@wh 0706]# sed -i '/^ONBOOT/ s/yes/no/' ifcfg-ens33 
[root@wh 0706]# cat ifcfg-ens33 
BOOTPROTO="none"
NAME="ens33"
DEVICE="ens33"
ONBOOT="no"
IPADDR=192.168.72.129
PREFIX=24
GATEWAY=192.168.72.2
DNS1=114.114.114.114

# 在1到8行前面添加#
[root@wh 0706]# sed -i '1,8 s/^/#/' ifcfg-ens33 
[root@wh 0706]# cat ifcfg-ens33 
#BOOTPROTO="none"
#NAME="ens33"
#DEVICE="ens33"
#ONBOOT="no"
#IPADDR=192.168.72.129
#PREFIX=24
#GATEWAY=192.168.72.2
#DNS1=114.114.114.114

# 在1到8行后面添加sanchuang
[root@wh 0706]# sed -i '1,8 s/$/sanchuang/' ifcfg-ens33 
[root@wh 0706]# cat ifcfg-ens33 
#BOOTPROTO="none"sanchuang
#NAME="ens33"sanchuang
#DEVICE="ens33"sanchuang
#ONBOOT="no"sanchuang
#IPADDR=192.168.72.129sanchuang
#PREFIX=24sanchuang
#GATEWAY=192.168.72.2sanchuang
#DNS1=114.114.114.114sanchuang

# s 替换
# 不接，默认只替换每行的第一个
# 接数字n，替换每行的第n个
# 接g，都替换
[root@wh 0706]# cat sc.txt 
zhaojunjie changchuang
huangzian  changsha  male
duanyouxu  taohuadao daozhu
liuchang   dajiaoshi
zhangchang dajiaoshi 12345 zhangchang123 zhangchang 456 zhangchang
zhangchang dajiaoshi 12345 zhangchang123 zhangchang 456 zhangchang
zhangchang dajiaoshi 12345 zhangchang123 zhangchang 456 zhangchang
# 默认替换每行的第一个
[root@wh 0706]# sed -i '/zhangchang/ s/zhangchang/tiannannan/' sc.txt 
[root@wh 0706]# cat sc.txt 
zhaojunjie changchuang
huangzian  changsha  male
duanyouxu  taohuadao daozhu
liuchang   dajiaoshi
tiannannan dajiaoshi 12345 zhangchang123 zhangchang 456 zhangchang
tiannannan dajiaoshi 12345 zhangchang123 zhangchang 456 zhangchang
tiannannan dajiaoshi 12345 zhangchang123 zhangchang 456 zhangchang
# 替换每行的第二个
[root@wh 0706]# sed -i '/zhangchang/ s/zhangchang/tiannannan/2' sc.txt 
[root@wh 0706]# cat sc.txt 
zhaojunjie changchuang
huangzian  changsha  male
duanyouxu  taohuadao daozhu
liuchang   dajiaoshi
tiannannan dajiaoshi 12345 zhangchang123 tiannannan 456 zhangchang
tiannannan dajiaoshi 12345 zhangchang123 tiannannan 456 zhangchang
tiannannan dajiaoshi 12345 zhangchang123 tiannannan 456 zhangchang
# 都替换
[root@wh 0706]# sed -i '/zhangchang/ s/zhangchang/wangxiao/g' sc.txt 
[root@wh 0706]# cat sc.txt 
zhaojunjie changchuang
huangzian  changsha  male
duanyouxu  taohuadao daozhu
liuchang   dajiaoshi
tiannannan dajiaoshi 12345 wangxiao123 tiannannan 456 wangxiao
tiannannan dajiaoshi 12345 wangxiao123 tiannannan 456 wangxiao
tiannannan dajiaoshi 12345 wangxiao123 tiannannan 456 wangxiao
# 指定替换模式的分隔符，这样里面的字符串就可以不用转义
[root@wh 0706]# sed -i '/mengmeng/ s#/bin/bash#/sbin/nologin#' /etc/passwd
[root@wh 0706]# grep 'mengmeng' /etc/passwd
mengmeng:x:12429:12429::/home/mengmeng:/sbin/nologin
mengmeng1:x:12430:12430::/home/mengmeng1:/sbin/nologin
mengmeng2:x:12431:12431::/home/mengmeng2:/sbin/nologin
------------
# r 读取文件内容到文件
[root@wh 0706]# cat fan.txt 
zhaojunjie wangshenghu zhengyang
liuchang zhangchang
yangyongjie lijunlin
[root@wh 0706]# sed -i '$r /etc/hosts' fan.txt 
[root@wh 0706]# cat fan.txt 
zhaojunjie wangshenghu zhengyang
liuchang zhangchang
yangyongjie lijunlin
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
[root@wh 0706]# cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
[root@wh 0706]# 
-------------
# w 把文件内容写入到文件
[root@wh 0706]# sed -i '1,3w wangdan.txt' fan.txt 
[root@wh 0706]# ls
access.log  fan.txt  ifcfg-ens33  sc.txt  wangdan.txt
[root@wh 0706]# cat wangdan.txt 
zhaojunjie wangshenghu zhengyang
liuchang zhangchang
yangyongjie lijunlin
[root@wh 0706]# cat fan.txt 
zhaojunjie wangshenghu zhengyang
liuchang zhangchang
yangyongjie lijunlin
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
# 会覆盖
[root@wh 0706]# sed -i '4w wangdan.txt' fan.txt 
[root@wh 0706]# cat wangdan.txt 
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4

```

##### sed的p命令示例：

>  
 1,5p ：1-5行 
 10p ：第10行 
 $p ：最后一行 
 1~2p ：从第一行开始，间隔2行 
 2,+2p ：第2行开始，往后显示2行 
 3,100!p ：显示除了3-100的行 
 /模式/p : 支持正则，如果是扩展正则，需要接-r选项 
 查找日志文件中两个时间段的内容 


```
# -n：只显示匹配显示的行
# 1,5p 1-5行
[root@wh 0706]# sed -n '1,5p' /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
[root@wh 0706]# sed  '1,5p' /etc/passwd
# 会显示所有行，1到5行会显示2遍

# 显示130行
[root@wh 0706]# nl /etc/passwd|sed -n '130p'|head -10
   130	mengmeng2:x:12431:12431::/home/mengmeng2:/bin/bash
# 显示第8行
[root@wh 0706]# head -8 /etc/passwd|tail -1
halt:x:7:0:halt:/sbin:/sbin/halt
[root@wh 0706]# sed -n '8p' /etc/passwd
halt:x:7:0:halt:/sbin:/sbin/halt
[root@wh 0706]# awk 'NR==8{print $0}' /etc/passwd
halt:x:7:0:halt:/sbin:/sbin/halt
# 显示文件第一行和最后一行
[root@wh 0706]# head -1 /etc/passwd;tail -1 /etc/passwd
root:x:0:0:root:/root:/bin/bash
mengmeng2:x:12431:12431::/home/mengmeng2:/bin/bash
[root@wh 0706]# sed -n '1p;$p' /etc/passwd
root:x:0:0:root:/root:/bin/bash
mengmeng2:x:12431:12431::/home/mengmeng2:/bin/bash
[root@wh 0706]# awk 'NR==1{print $0}END{print $0}' /etc/passwd
root:x:0:0:root:/root:/bin/bash
mengmeng2:x:12431:12431::/home/mengmeng2:/bin/bash


# 显示最后一行
[root@wh 0706]# nl /etc/passwd|sed -n '$p'|head -10
   130	mengmeng2:x:12431:12431::/home/mengmeng2:/bin/bash
   
# 1~2p：从第一行开始，间隔2行显示
[root@wh 0706]# nl /etc/passwd |sed -n '1~2p' |head -10
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
# 2~2p：从第2行开始，间隔2行显示
[root@wh 0706]# nl /etc/passwd |sed -n '2~2p' |head -10
     2	bin:x:1:1:bin:/bin:/sbin/nologin
     4	adm:x:3:4:adm:/var/adm:/sbin/nologin
     6	sync:x:5:0:sync:/sbin:/bin/sync
     8	halt:x:7:0:halt:/sbin:/sbin/halt
    10	operator:x:11:0:operator:/root:/sbin/nologin
    12	ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
    14	systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
    16	polkitd:x:999:998:User for polkitd:/:/sbin/nologin
    18	postfix:x:89:89::/var/spool/postfix:/sbin/nologin
    20	weihong:x:1000:1000::/home/weihong:/bin/bash

# 2,+2p ：第2行开始，往后显示2行
[root@wh 0706]# nl /etc/passwd|sed -n '2,+2p'|head -10
     2	bin:x:1:1:bin:/bin:/sbin/nologin
     3	daemon:x:2:2:daemon:/sbin:/sbin/nologin
     4	adm:x:3:4:adm:/var/adm:/sbin/nologin

# 3,100!p ：显示除了3-100的行
[root@wh 0706]# nl /etc/passwd|sed -n '3,100!p'|head -10
     1	root:x:0:0:root:/root:/bin/bash
     2	bin:x:1:1:bin:/bin:/sbin/nologin
   101	user11:x:12402:12402::/home/user11:/bin/bash
   102	user12:x:12403:12403::/home/user12:/bin/bash
   103	user13:x:12404:12404::/home/user13:/bin/bash
   104	user14:x:12405:12405::/home/user14:/bin/bash
   105	user15:x:12406:12406::/home/user15:/bin/bash
   106	user16:x:12407:12407::/home/user16:/bin/bash
   107	user17:x:12408:12408::/home/user17:/bin/bash
   108	user18:x:12409:12409::/home/user18:/bin/bash

# 时间段的匹配
[root@wh 0706]# sed -n '/01\/Jul\/2022:23:40/,/01\/Jul\/2022:23:57/p' access.log
类似 sed -n '1,7p' access.log 的用法

```

##### 引用shell变量：双引号 、花括号括变量名

```
[root@wh 0706]# num1=5
[root@wh 0706]# num2=15
[root@wh 0706]# sed -n "${num1}p;${num2}p" /etc/passwd
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin

```

##### &amp;的用法

```
[root@wh 0706]# cat cat.txt 
i have a fat big cat
i have a fat big cat
i have a fat big cat
# 将fat和cat用双引号引起来
[root@wh 0706]# sed -i 's/.at/"&amp;"/g' cat.txt 
[root@wh 0706]# cat cat.txt 
i have a ""fat"" big "cat"
i have a ""fat"" big "cat"
i have a ""fat"" big "cat"

[root@wh 0706]# cat cat.txt 
7878i have a ""fat"" big "cat"456
i have8989 a ""fat"" big "cat" 123
i have a ""fat"" big "cat" 789
# 在三位数的数字后面加0
[root@wh 0706]# sed -r 's/\b[0-9]{3}\b/&amp;0/g' cat.txt 
7878i have a ""fat"" big "cat"4560
i have8989 a ""fat"" big "cat" 1230
i have a ""fat"" big "cat" 7890

```

##### 标签的用法（分组思想）

```
[root@wh 0706]# echo aaa bbb 1234|sed -r  's/([a-z]+) ([a-z]+) ([0-9]+)/\3/'
1234
[root@wh 0706]# echo aaa bbb 1234|sed -r  's/([a-z]+) ([a-z]+) ([0-9]+)/\1/'
aaa
[root@wh 0706]# echo aaa bbb 1234|sed -r  's/([a-z]+) ([a-z]+) ([0-9]+)/\3 \2 \1/'
1234 bbb aaa

```
