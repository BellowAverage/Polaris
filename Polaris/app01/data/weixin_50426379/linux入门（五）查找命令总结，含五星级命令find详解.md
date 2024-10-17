
--- 
title:  linux入门（五）查找命令总结，含五星级命令find详解 
tags: []
categories: [] 

---


#### 文章目录
- - <ul><li>- - <ul><li>- - - - - - - - - - <ul><li>


## 查找命令

### which bash ： 查看bash命令存放的路径

```
[root@localhost ~]# which  bash  #查看bash命令存放的路径
/usr/bin/bash

```

### whereis bash：查看bash命令存放的路径

```
[root@wh ~]# whereis bash  #不仅会显示命令存放的路径，还会显示该命令的man手册的路径
bash: /usr/bin/bash /usr/share/man/man1/bash.1.gz

```

#### PATH变量

<mark>which和whereis 都是到PATH变量里去查找命令的</mark>–&gt;不能查找非命令的文件

```
[root@wh lianxi]# which dengdeyong
/usr/bin/which: no dengdeyong in (/usr/local/mysql/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin)

```

PATH变量： <mark>存放linux系统里命令存放的路径</mark> --》命令藏宝图–》记录了命令存放在哪些文件夹里 PATH变量里都是<mark>文件夹的路径，中间使用冒号隔开</mark>

我们在linux系统里查找命令的时候，从<mark>PATH变量的最左边的文件夹里开始查找</mark>，如果找到就不往下查找了，如果没有找到就，继续往下找，以此类推，如果都没有找到就提醒没有找到这个命令

PATH变量是系统里<mark>预定义的变量</mark>，操作系统安装好就定义的变量 预定义变量–》环境变量–》全局变量 很多程序都可以使用，很多用户都可以使用的

>  
 <mark>/usr --》unix system resource</mark> --》linux里的所有的程序就是系统的资源 --》linux是山寨的unix linux is very like unix <mark>bin --》binary 二进制</mark> --》linux里的很多程序都是c语言编写–》编译成二进制程序，才可以运行 
 <mark>sbin --》super user binary</mark> --》有些命令必须是root用户才能使用的命令，就存放在sbin目录下–》御用（有权限的用户） sbin目录下的命令是需要高级权限的用户使用的，普通用户使用不了–》root可以使用，例如 useradd等命令 


```
[root@lb1 zhaojunjie]# which ip
/usr/sbin/ip
[root@lb1 zhaojunjie]# which useradd
/usr/sbin/useradd

[root@lb1 zhaojunjie]# useradd  li
[root@lb1 zhaojunjie]# su - li
[li@lb1 ~]$ useradd xiao
useradd: Permission denied.
useradd：无法锁定 /etc/passwd，请稍后再试。

```

```
[root@master ~]# PATH=/lianxi:$PAHT  #临时在当前终端里修改了PATH，只是影响当前终端

```

>  
 解决方法： 1.重新登录用户： su 发现不行 重新ssh远程连接，也会让root重新登录 --》可以的 2.重新定义PATH变量 


```
[root@master ~]# PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin

```

### locate：查找文件或目录（默认是模糊查找）

>  
 locate 是根据文件名到mlocate.db文件里去查找的 <mark>默认是模糊查找</mark>–》只要文件名里包含某个字符串就可以了 精确查找： 不能多也不能少 
 locate 不能查找到实时最新的数据，但是查找速度非常快，如果需要查找最新的数据，需要更新数据库–》<mark>updatedb</mark> 
 updatedb 背后其实可以理解为将我们整个linux系统里的文件或者文件夹创建了一个索引，存放在mlocate.db文件里 索引： index 相当于书本的目录，起到快速查找的内容的作用 --》帮助可以快速查询 


```
[root@master lianxi]# locate scfeng.py
locate: can not stat () `/var/lib/mlocate/mlocate.db': No such file or directory

[root@master lianxi]# cd /var/lib/mlocate/
[root@master mlocate]# ls
[root@master mlocate]#
#mlocate.db  这个文件是locate命令去查找文件的数据库文件--》这个文件里存放了很多文件的路径   db --》database 数据库

#dba --》database administrator 数据库管理员 --》IT岗位，就是负责维护公司里的所有的数据库的，数据库有哪些数据库？（MySQL，redis，MongoDB，oracle，MSSQL等）

#/var/lib/mlocate/mlocate.db 如何得到这个mlocate.db文件呢？
#updatedb  会帮助我们去创建mlocate.db这个文件

[root@master mlocate]# updatedb  
[root@master mlocate]# pwd
/var/lib/mlocate
[root@master mlocate]# ls
mlocate.db

#模糊查找
[root@master mlocate]# locate scfeng.py
/lianxi/scfeng.py
[root@master mlocate]# locate scfeng
/lianxi/scfeng.py
[root@master mlocate]# 

#精确查找
[root@master mlocate]# locate -b '\scfeng'

#locate 不能查找到实时最新的数据，但是查找速度非常快
[root@master mlocate]# touch xiejiaxin.txt
[root@master mlocate]# locate xiejiaxin
[root@master mlocate]# ls
mlocate.db  xiejiaxin.txt
[root@master mlocate]# updatedb 
[root@master mlocate]# locate xiejiaxin
/var/lib/mlocate/xiejiaxin.txt

```

### find:用于查找文件或目录（默认是精确查找）

>  
 <mark>格式：find [查找范围] [查找条件] [动作]</mark> 常用查找条件 <mark>-name：按文件名称查找</mark> <mark>-iname：按文件名称查找,不区分大小写</mark> <mark>-size： 按文件大小查找</mark> -user： 按文件属主查找 -type： 按文件类型查找 -perm ：按文件权限查找 <mark>-mtime ：按文件更改时间查找</mark> -newer：按比某个文件更新的查找 


>  
 -o ：逻辑或 or ，只要所给的条件中有一个满足，寻找条件就算满足 -not :逻辑非 not ，在命令中可用“!”表示。该运算符表示查找不满足所给条件的文件 --&gt;取反 -a： 逻辑与 and ，<mark>系统默认是与，可不加</mark>，表示只有当所给的条件都满足时，寻找条件才算满足。 
 改变优先级：使用小括号,需用\进行转义，且括号与表达式之间需要有空格 


```
[root@master back]# find  /home  -user root -type f   \(  -size +2k -o -name "*cali*"  \)

```

#### -name

<mark>/ 查找的位置</mark>，不知道哪里有，就在根目录下，默认所有的文件都在根目录下

-<mark>name 查找的条件，是根据文件名, 默认是精确查找</mark>

<mark>“*.jpg” 文件名以.jpg结尾 * 代表任意的字符串（通配符）</mark>

```
[root@localhost lianxi]# find   /   -name  "*.jpg"
/root/feng.jpg
/usr/share/backgrounds/morning.jpg
/usr/share/backgrounds/night.jpg
/usr/share/backgrounds/day.jpg
/usr/share/backgrounds/default.jpg
/usr/share/kde4/apps/ksplash/Themes/CentOS7/2560x1600/background.jpg
/usr/share/wallpapers/CentOS7/contents/images/2560x1600.jpg
/usr/share/nginx/html/test/zs.jpg
/lianxi/zhangjian.jpg

```

```
[root@master mlocate]# find   /  -name  "scfeng"  #默认是精确查找
[root@master mlocate]# find   /  -name  "scfeng.py"
/lianxi/scfeng.py
#可使用通配符进行模糊查找
[root@master mlocate]# find  /boot   -name "*linuz*"
/boot/.vmlinuz-3.10.0-1160.el7.x86_64.hmac
/boot/vmlinuz-3.10.0-1160.el7.x86_64
/boot/vmlinuz-0-rescue-d0bc6df5a0e74d248da1b6d460cd2ded

```

#### -iname

>  
 -iname pattern 
 Like -name, but the match is case insensitive. 大小写不敏感，<mark>不区分大小写</mark> 


>  
 <mark>2&gt; 表示错误输出重定向</mark> <mark>/dev/null 是linux系统里的黑洞文件</mark>，任何的内容往这个文件里输入都不保存，直接删除 


```
[root@master mlocate]# find / -iname "xiejiaxin.txt" 2&gt;/dev/null
/var/lib/mlocate/xiejiaxin.txt
/var/lib/mlocate/XIEJIAXIN.TXT

```

#### -size

>  
 -size 单位 k–&gt;M–&gt;G–&gt;T +10M 大于10M --&gt;推荐 -10M 小于10M 10M 等于10M 


```
[root@master mlocate]# find  /boot  -size +1M
/boot/grub2/fonts/unicode.pf2
/boot/System.map-3.10.0-1160.el7.x86_64
/boot/vmlinuz-3.10.0-1160.el7.x86_64
/boot/initramfs-0-rescue-d0bc6df5a0e74d248da1b6d460cd2ded.img
/boot/vmlinuz-0-rescue-d0bc6df5a0e74d248da1b6d460cd2ded
/boot/initramfs-3.10.0-1160.el7.x86_64.img
/boot/initramfs-3.10.0-1160.el7.x86_64kdump.img

```

```
[root@master boot]# find  /boot -size +1M  -o  -name "*sanchuang*"
/boot/grub2/fonts/unicode.pf2
/boot/System.map-3.10.0-1160.el7.x86_64
/boot/vmlinuz-3.10.0-1160.el7.x86_64
/boot/initramfs-0-rescue-d0bc6df5a0e74d248da1b6d460cd2ded.img
/boot/vmlinuz-0-rescue-d0bc6df5a0e74d248da1b6d460cd2ded
/boot/initramfs-3.10.0-1160.el7.x86_64.img
/boot/initramfs-3.10.0-1160.el7.x86_64kdump.img
/boot/sanchuang.txt
 
[root@master boot]# find  /boot ! -size +1M 
[root@master boot]# find  /boot ! -name "sanchuang.txt"

```

优先级的问题： 与的优先级高于或

```
#前面2个条件组合      
[root@master boot]# find  /boot  -name "*.txt" -size +1k  -o -name "*.img"
/boot/grub2/i386-pc/core.img
/boot/grub2/i386-pc/boot.img
/boot/initramfs-0-rescue-d0bc6df5a0e74d248da1b6d460cd2ded.img
/boot/initramfs-3.10.0-1160.el7.x86_64.img
/boot/initramfs-3.10.0-1160.el7.x86_64kdump.img

```

#### -user

<mark>普通用户只能在自己的家目录下 (例/home/yao) 新建文件或文件夹</mark>，在别的地方新建会没有权限

```
[root@master duanyouxu]# useradd yao
[root@master duanyouxu]# su - yao
[yao@master ~]$ pwd
/home/yao
[yao@master ~]$ ls
#普通用户只能在自己的家目录下新建文件或文件夹，在别的地方新建会没有权限
[yao@master ~]$ touch yao.txt dayao.txt
[yao@master ~]$ mkdir sanchuang
[yao@master ~]$ ll
总用量 0
-rw-rw-r-- 1 yao yao 0 4月  10 11:26 dayao.txt
drwxrwxr-x 2 yao yao 6 4月  10 11:27 sanchuang
-rw-rw-r-- 1 yao yao 0 4月  10 11:26 yao.txt
[yao@master ~]$ pwd
/home/yao
[yao@master ~]$ cd /
[yao@master /]$ mkdir dayao
mkdir: 无法创建目录"dayao": 权限不够
[yao@master /]$ cd /find
[yao@master find]$ ls
boot  daydayup  duan.txt  duanyouxu.jpg  hn  hunantv  liu  liu.txt  meinv.jpg  passwd  三创就业信息.jpg
[yao@master find]$ mkdir xiaoyao
mkdir: 无法创建目录"xiaoyao": 权限不够
[yao@master find]$ exit
登出

```

```
[root@master duanyouxu]# find  / -user yao -type  f  2&gt;/dev/null  
/var/spool/mail/yao
/home/yao/.bash_logout
/home/yao/.bash_profile
/home/yao/.bashrc
/home/yao/yao.txt
/home/yao/dayao.txt
/home/yao/.bash_history
[root@master duanyouxu]# 

```

#### -type

>  
 文件类型： <mark>普通文件 f</mark> file <mark>目录 d</mark> directory <mark>链接文件 l</mark> link <mark>块设备文件 b</mark> block ： 用来存放数据的文件–》是**磁盘（硬盘）对应的文件**–》一切皆文件 <mark>字符设备文件 c</mark> character 用来**与字符的显示**相关–》字符输入和输出相关的 <mark>管道文件 p</mark> pipe ：实现**进程和进程之间通信的**–》是内存里的文件 <mark>socket文件 s</mark> socket 套接字文件 是**实现进程和进程之间通信的方式，socket文件可以在磁盘里** --》槽、插线板 、套接字： 将2边的东西连接起来 
 (mysql是一个数据库服务，用来存放数据的) **文件socket**： /data/mysql/mysql.sock ： 实现是同一台机器上的不同进程之间通信 **网络socket**： 不同的机器上的不同的进程之间通信的 表现形式： ip+port 192.168.2.1.30:3306 


```
[root@master dev]# ll sda
brw-rw---- 1 root disk 8, 0 4月   8 09:26 sda
[root@master dev]# ll tty1
crw--w---- 1 root tty 4, 1 4月   8 09:26 tty1
[root@master find]# ll /run/dmeventd-client
prw------- 1 root root 0 4月   8 09:26 /run/dmeventd-client
[root@wh mysql]# ll
srwxrwxrwx  1 mysql mysql        0 4月   8 08:32 mysql.sock

```

#### -mtime

>  
 Measure times (for -amin, -atime, -cmin, -ctime, -mmin, and -mtime -mmin n File’s data was last modified n minutes ago. -mtime n File’s data was last modified n*24 hours ago. 
 -mtime +2 2天前的 -mtime -2 2天内的 
 -mmin +10 10分钟之前的 -mmin -10 10分钟之内的 


以当前的时间作为参照对象

```
[root@master find]# date
2022年 04月 10日 星期日 11:19:52 CST

[root@master find]# find  . -mmin -5 -type f
./liu.txt

```

#### -newer

```
[root@master find]# find .  -newer liu.txt
.
./liu
./duan.txt

[root@master find]# find .  -newer liu.txt  -type f
./duan.txt

```

#### -maxdepth

>  
 需要是接在find后面的<mark>第一个选项</mark> 
 查找文件的时候，目录的深度 1 代表当前 2 代表下一级目录 3 下一级的下一级目录，以此类推 


```
[root@master china]# ls
aa  sc.txt
[root@master china]# find  /china  -maxdepth 1 -name sc.txt
/china/sc.txt
[root@master china]# find  /china  -maxdepth 2 -name sc.txt
/china/sc.txt
/china/aa/sc.txt
[root@master china]# find  /china  -maxdepth 3 -name sc.txt
/china/sc.txt
/china/aa/sc.txt
/china/aa/bb/sc.txt
/china/aa/cc/sc.txt

```

#### -exec

是一个执行选项

```
[root@master duanyouxu]# find /root  -name hello.c -type f  -exec  cp  {} /find  \;
#复制过去会覆盖原来的文件的里内容

```

>  
 find /root -name hello.c -type f 查找到文件类型是文件 名字是hello.c 在/root目录下查找 -exec 执行的动作，动作一般都是命令 cp {} /find 源文件 目的地 {} 相当于一个容器，里面存放的是前面的find命令查找到的内容 
 ; 是-exec 执行动作的结束符号 --》不接find命令不知道需要执行的命令，是否输入完成 


\; 和 ; 的区别？

转义字符串 \ ,让有特殊作用的元字符回归到字符本身的意思

; 命令连接符号，无论前面的命令执行成功还是失败都会执行后面的命令 command1 ; command2

```
[root@master duanyouxu]# mkdir shenjiemi  ; ls 
mkdir: 无法创建目录"shenjiemi": 文件已存在
duan.txt  hello.c  shenjiemi

[root@master duanyouxu]# mkdir shenjiemi\;ls 
[root@master duanyouxu]# ls
duan.txt  hello.c  shenjiemi  shenjiemi;ls

```

>  
 command1 &amp;&amp; command2 如果command1执行成功，就执行command2，不成功不执行 command1 || command2 如果command1执行不成功，就执行command2，成功不执行 command1 &amp;&amp; command2 || command3 如果command1执行成功，就执行command2，不成功执行command3 


```
[root@master find]# mkdir  sc123 &amp;&amp; echo "ok"
ok
[root@master find]# ls
boot      duan.txt       feng.txt  hn       liu      meinv.jpg  sc123
daydayup  duanyouxu.jpg  hello.c   hunantv  liu.txt  passwd 
[root@master find]# mkdir  sc123 &amp;&amp; echo "ok"
mkdir: 无法创建目录"sc123": 文件已存在
[root@master find]# useradd  root
useradd：用户“root”已存在
[root@master find]# useradd  root || echo "failed"
useradd：用户“root”已存在
failed
[root@master find]# useradd  root &amp;&amp; echo "ok" || echo "no"
useradd：用户“root”已存在
no
[root@master find]# useradd  root123 &amp;&amp; echo "ok" || echo "no"
ok
[root@master find]#

```

##### 练习：

查找出daydayup的文件然后删除它

```
[root@master find]# find  / -name daydayup  -exec rm -rf  {} \;

```

将最近3小时内/lianxi目录下文件大小大于10K的文件 移动到/back目录下

```
[root@master back]# find /lianxi -type f -size +10k -mmin -180 -exec  mv {} /back  \;

```

新建用户califeng、cali123、然后复制/boot/vmlinuz开头的文件到/home目录下，再复制/var/log/messages到/home目录下改名为cali789，然后查找/home目录下用户是root，文件类型是f，这2个条件必须满足，然后再满足大小大于2k或者文件名包含cali的文件中的一个条件，查找出来后，复制到/lianxi目录下。

```
[root@master back]# find  /home  -user root -type f   \(   -size +2k -o -name "*cali*"    \)

```

1.将/etc/目录下的所有的.conf结尾的文件，不管深度，大小小于5k的，复制到/back目录下

```
mkdir -p /back
[root@master back]# find /etc/ -name "*.conf" -size -5k -exec cp {} /back \;

```

2.新建一个目录/sc，复制/boot目录到/sc目录下，然后查找/sc目录下的大小大于2M文件名里包含vm的文件，移动到/tmp目录下

```
[root@master back]# find  /sc  -size +2M -name "*vm*" -exec mv {}  /tmp  \;

```

3.查找/sc目录下20分钟内修改过的文件，并且文件名以.txt结尾

```
[root@master back]# find /sc  -mmin -20  -type f  -name "*.txt"

```

4.查找比/etc/passwd文件更加新的文件，要求这个文件要大于10k，并且用户是root

```
[root@master back]# find  /  -newer /etc/passwd  -type f   -size +10k  -user root

```

5.将/etc/目录下的所有的.conf结尾的文件，深度为2层（例如：/etc/aa止，/etc/aa/bb不查询了），大小小于5k的，复制到/back目录下

```
[root@master back]# find /etc/ -maxdepth 2 -name "*.conf" -size -5k -exec cp {} /back \;

```
