
--- 
title:  Linux归档及压缩命令，含五星级命令tar详解 
tags: []
categories: [] 

---


#### 文章目录
- - <ul><li>- - - - - - - <ul><li>- - <ul><li>- - 


## 压缩命令

### 一、打包压缩的用途

>  
 1.为什么要打压缩包？ 备份的时候，能节约空间 网络传送的时候，能节约时间 
 2.打包压缩： 打包： 就是将很多文件放到一起，成一个文件 压缩： 减少占用磁盘空间的操作 
 3.windows里的.rar压缩文件传递到linux里，是否能打开？ zip windows和linux都支持 .rar文件在linux里默认是不能打开 linux里的所有的压缩文件，windows里的都能打开 windows里的压缩文件，在linux里不一定就可以打开 
 4.linux和windows之间的文件上传和下载的解决方法： 1.xftp: 在windows里安装 2.moba 在windows里安装 3.lrzsz 在windows里安装了xshell但是没有安装xftp，需要 在linux里安装lrzsz，速度没有使用xftp快 yum install lrzsz 
 rz linux里接受从windows里上传的文件 receive 
 sz playbook.sh 将linux里的playbook.sh文件传到windows里 sent 


### 二、命令

### 1.压缩：zip 解压：unzip 查看压缩文件里面的内容：zcat 后缀：.zip

zip只能给文件做成一个压缩包，不能对文件夹进行

```
[root@master 410]# yum  install zip unzip -y

[root@master 410]# zip  passwd.zip         passwd
                        #打包压缩文件         原文件
  adding: passwd (deflated 62%)
[root@master 410]# ls
passwd  passwd.zip

[root@master 410]# cp passwd.zip /backup
[root@master 410]# cd /backup/

```

>  
 Archive 附件： 一个压缩包或者压缩文件就称呼为一个附件 存档文件，归档文件 其实就是将一个文件压缩或者很多文件放到一个文件里，把很多东西放到一起–》这个过程就称呼归档，存档 deflated 泄气（压缩） inflat 解压 


### 2.压缩：gzip 解压：gunzip 查看压缩文件里面的内容：zcat 后缀：.gz

```
[root@master backup]# gzip passwd  #直接在原文件上进行压缩，添加后缀名.gz
[root@master backup]# zcat passwd.gz   #查看压缩文件里的内容
[root@master backup]# gunzip  passwd.gz   #解压文件

```

### 3.压缩：xz 解压：unxz 查看压缩文件里面的内容：xzcat 后缀：.xz

xz 也是linux系统默认安装的压缩工具

```
[root@master backup]# xz passwd
[root@master backup]# xzcat passwd.xz
[root@master backup]# unxz passwd.xz

```

例：https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.17.2.tar.xz

>  
 xz和gzip的区别 
 <mark>xz的压缩效果比gzip好</mark>，压缩后<mark>占用的空间比较少</mark>，压缩需要的<mark>时间长</mark> <mark>gzip 压缩速度快</mark>，但是<mark>效果一般</mark> 
 文件比较小，使用xz或者gzip都可以 如果<mark>文件比较大</mark>，<mark>建议使用xz压缩</mark>，可以<mark>节约更加多的磁盘空间</mark>，但是<mark>需要时间比较长</mark> 慢工出细活–》xz 


```
[root@master ~]# ll -h  bigfile.txt 
-rw-r--r--. 1 root root 76M 3月  28 16:32 bigfile.txt
[root@master ~]# time xz bigfile.txt  #查看gzip命令的执行消耗时间
real	0m4.384s
user	0m3.545s
sys	0m0.801s
[root@master ~]# ll -h bigfile.*
-rw-r--r--. 1 root root 132 3月  28 16:31 bigfile.sh
-rw-r--r--  1 root root 12K 3月  28 16:32 bigfile.txt.xz
[root@master ~]# unxz bigfile.txt.xz 
[root@master ~]# ls
anaconda-ks.cfg    bigfile.txt 

[root@master ~]# ll -h bigfile.*
-rw-r--r--. 1 root root 132 3月  28 16:31 bigfile.sh
-rw-r--r--  1 root root 76M 3月  28 16:32 bigfile.txt
[root@master ~]# time gzip  bigfile.txt  #查看gzip命令的执行消耗时间
real	0m0.987s
user	0m0.913s
sys	0m0.073s
[root@master ~]# ll -h bigfile.*
-rw-r--r--. 1 root root  132 3月  28 16:31 bigfile.sh
-rw-r--r--  1 root root 262K 3月  28 16:32 bigfile.txt.gz
[root@master ~]# gunzip bigfile.txt.gz 

```

### 4.压缩：bzip2 解压：bunzip2 查看压缩文件里面的内容：bzcat 后缀：.bz2

```
[root@master lianxi]# yum  install bzip2 -y
[root@master lianxi]# bzip2 feng.yaml 
[root@master lianxi]# ls feng.yaml.bz2 
feng.yaml.bz2
[root@master lianxi]# bzcat  feng.yaml.bz2 
[root@master lianxi]# bunzip2 feng.yaml.bz2 

```

### 5.tar命令（五星级命令）

#### 1.tar包的后缀

>  
 使用tar命令打的压缩包叫tarball --》tar包–&gt;归档文件：将很多个文件或者文件夹打包到一个文件里，然后可以对归档文件进行压缩 
 .tar —》其实只是归档，不进行压缩 .tar.gz --》先归档，然后再调用gzip进行压缩–》.tar.gz --》速度快 .tar.xz --》先归档，然后再调用xz进行压缩–》.tar.xz --&gt;压缩效果好 .tar.bz2 --》先归档，然后再调用bzip2进行压缩–》.tar.bz2 


#### 2.tar命令的语法

用途：制作归档文件、释放归档文件 格式：<mark>压缩：tar [选项]… 归档文件名 源文件或目录</mark> <mark>解压：tar [选项]… 归档文件名 [-C 目标目录]</mark> 常用命令选项 -c：创建 .tar 格式的包文件 create -x：解开.tar格式的包文件 -v：输出详细信息 -f：表示使用归档文件 file -t：列表查看包内的文件 list -p：保持原文件的原来属性 -P：保持原文件的绝对路径 -z 调用gzip去压缩 -J 调用xz去压缩 -j 调用bzip2去压缩

##### 1.打压缩包

常用选项： ​ <mark>tar -czf --&gt;.tar.gz ​ tar czf（加不加 - 效果一样） ​ tar cjf --&gt;.tar.bz2 ​ tar cJf --&gt;.tar.xz</mark>

```
[root@master luoyawei]# cp  /etc/passwd .
[root@master luoyawei]# cp /boot  . -r
[root@master luoyawei]# ls
boot  passwd
[root@master luoyawei]# tar  czf  passwd.tar.gz   passwd   
#  passwd.tar.gz为压缩文件，passwd为源文件
#将当前目录下的passwd文件打包成passwd.tar.gz压缩包 

#后面打包的文件会覆盖原来的文件，如果文件名一样
[root@master luoyawei]# ls
boot  passwd  passwd.tar.gz
[root@master luoyawei]# tar  czf  passwd.tar.gz  passwd 
[root@master luoyawei]# ls
boot  passwd  passwd.tar.gz

# 用gzip打包成.xz后缀的文件，发现文件还是gzip压缩文件
[root@master luoyawei]# tar  czf  passwd.tar.xz  passwd 
[root@master luoyawei]# ls
boot  passwd  passwd.tar.gz  passwd.tar.xz
[root@master luoyawei]# file passwd.tar.gz
passwd.tar.gz: gzip compressed data, from Unix, last modified: Tue Apr 12 19:55:59 2022
[root@master luoyawei]# file passwd.tar.xz
passwd.tar.xz: gzip compressed data, from Unix, last modified: Tue Apr 12 19:57:08 2022

[root@master luoyawei]# tar cjf passwd.tar.bz2 passwd 
[root@master luoyawei]# tar cJf passwd.tar.xz passwd  
[root@master luoyawei]# ls
boot  passwd  passwd.tar.bz2  passwd.tar.gz  passwd.tar.xz
[root@master luoyawei]# file passwd.tar.xz
passwd.tar.xz: XZ compressed data
#总结： 后面打包的文件会覆盖原来的文件，如果文件名一样

#出现提示信息，是因为我们使用的是绝对路径
[root@master luoyawei]# tar czf  /lianxi/luoyawei/hosts.tar.gz   /etc/hosts
tar: 从成员名中删除开头的“/”
[root@master luoyawei]# ls
boot  hosts.tar.gz  passwd  passwd.tar.bz2  passwd.tar.gz  passwd.tar.xz

```

<mark>**–exclude** 排除</mark>

将/boot目录下的除grub2目录以外的所有文件都备份到/bak目录下叫no-grub.tar.gz

```
[root@fengdeyong bak]# tar --exclude=/boot/grub2 -czf  /bak/no-grub.tar.gz  /boot

# 排除多个文件或者文件夹
[root@fengdeyong bak]# tar --exclude=/boot/grub2 --exclude=/boot/loader -czf  /bak/no-grub.tar.gz  /boot
[root@master luoyawei]# tar --exclude=/boot/{grub2,grub,efi}  -czf /lianxi/luoyawei/no_grub2_boot.tar.gz  /boot

```

<mark>**打包文件时嵌入日期**</mark>

打包压缩某个文件–》本质上就是备份，一般备份都会添加备份时候的时间

>  
 date 是linux里查看时间的命令 
 格式化输出日期 
 <mark>+%Y year 年 %m month 月 %d day 日 %H hour 小时 %M minute 分钟 %S seconde 秒</mark> 


```
[root@hunan-wangzhe-5 lianxi]# date +%Y%m%d
20211027
[root@hunan-wangzhe-5 lianxi]# date +%Y-%m-%d
2021-10-27
[root@hunan-wangzhe-5 lianxi]# date +%Y_%m_%d
2021_10_27
[root@hunan-wangzhe-5 lianxi]# date +%Y%m%d%H%M%S
20211027162146
[root@hunan-wangzhe-5 lianxi]# w_time=$(date +%Y%m%d%H%M%S)
#将date +%Y%m%d%H%M%S命令的执行结果赋值给w_time这个变量
#变量名=$( 命令)  优先执行$()里的命令，然后将命令的执行结果赋值给变量名
$( 命令) ---》命令替换

[root@hunan-wangzhe-5 lianxi]# echo $w_time   
20211027162311
#引用w_time变量的值      $变量名   --》引用变量名的值

#获得日期给变量，然后调用变量
[root@master luoyawei]# ctime=$(date +%Y%m%d)
[root@master luoyawei]# echo $ctime
20220412
[root@master luoyawei]# tar  czf  boot-$ctime.tar.gz /boot 
[root@master luoyawei]# tar  czf  boot-$(date +%Y%m%d).tar.gz /boot 

```

>  
 在工作中经常需要备份的东西： 日志文件会记录程序发生的事情 web服务器的日志记录哪些人从哪些地方访问了哪些网址–》大数据分析的 日志非常消耗磁盘空间 服务器上只是保存最近30天 nginx的日志，mysql的日志文件等 思考：京东，淘宝 1亿用户–》app和网站–》10个网址–》一条日志： 99**100000000**10 美团： 一天有多少外卖订单 


##### 2.查看压缩文件里的内容（.tar.gz .tar.xz .tar.bz2都用tf选项）

-f：表示使用归档文件 file -t：列表查看<mark>包内的文件</mark> list

```
[root@master luoyawei]# tar  tf  hosts.tar.gz 
etc/hosts

[root@wh 415]# tar czf boot.tar.gz /boot
tar: 从成员名中删除开头的“/”
[root@wh 415]# ls
boot.tar.gz  
[root@wh 415]# tar xf boot.tar.gz 
[root@wh 415]# ls
boot  boot.tar.gz 
[root@wh 415]# tar tf boot.tar.gz 
boot/
boot/efi/
boot/efi/EFI/
boot/efi/EFI/centos/
boot/grub2/
boot/grub2/device.map
boot/grub2/i386-pc/
boot/grub2/i386-pc/gcry_rmd160.mod
boot/grub2/i386-pc/acpi.mod
boot/grub2/i386-pc/gcry_rsa.mod
boot/grub2/i386-pc/adler32.mod
boot/grub2/i386-pc/gcry_seed.mod
boot/grub2/i386-pc/affs.mod
boot/grub2/i386-pc/gcry_serpent.mod
boot/grub2/i386-pc/afs.mod
boot/grub2/i386-pc/gcry_sha1.mod
boot/grub2/i386-pc/ahci.mod
......


```

##### 3.解压

>  
 xf 
 Extract all files from archive.tar. 
 Extract 提取，解压 ===》x 


<mark>1. 默认压缩路径为当前，如果压缩的时候用的是绝对路径，那么解压的时候，会去除/，产生后面对应的目录，如果压缩的时候是相对路径，那么默认解压到当前</mark>

```
#绝对路径
[root@master luoyawei]# tar czf hosts.tar.gz /etc/host
tar: 从成员名中删除开头的“/”
[root@master luoyawei]# tar xf hosts.tar.gz 
[root@master luoyawei]# ls
boot  etc  hosts.tar.gz  passwd  passwd.tar.bz2  passwd.tar.gz  passwd.tar.xz
[root@master luoyawei]# ls etc
hosts

[root@wh 415]# ls
[root@wh 415]# tar czf passwd.tar.gz /etc/passwd
tar: 从成员名中删除开头的“/”
[root@wh 415]# ls
passwd.tar.gz
[root@wh 415]# tar xf passwd.tar.gz  #会在当前目录下产生etc目录，把解压后的passwd放在etc目录下
[root@wh 415]# ls
etc  passwd.tar.gz
[root@wh 415]# tar tf passwd.tar.gz 
etc/passwd

#相对路径
[root@wh 415]# cp /etc/hosts .
[root@wh 415]# ls
hosts
[root@wh 415]# tar czf hosts.tar.gz hosts
[root@wh 415]# ls
hosts  hosts.tar.gz
[root@wh 415]# rm -rf hosts
[root@wh 415]# ls
hosts.tar.gz
[root@wh 415]# tar xf hosts.tar.gz 
[root@wh 415]# ls
hosts  hosts.tar.gz

```

产生提示信息是因为使用的是绝对路径保存压缩包

```
[root@master luoyawei]# mkdir /weihong
[root@master luoyawei]# pwd
/lianxi/luoyawei
[root@master luoyawei]# tar czf  /weihong/passwd.tar.gz   /etc/passwd
tar: 从成员名中删除开头的“/”
[root@master luoyawei]# ls /weihong
passwd.tar.gz

```

<mark>2. -C 指定解压文件存放的路径</mark>

```
[root@master luoyawei]# ls /nongda_weihong/
[root@master luoyawei]# tar xf /weihong/passwd.tar.gz   -C /nongda_weihong/
[root@master luoyawei]# ls /nongda_weihong/
etc

```

<mark>文件和文件夹</mark>可以一起打包到一个压缩文件里

```
[root@master luoyawei]# tar  czf   /lianxi/luoyawei/boot_passwd.tar.gz   /boot   /etc/passwd
tar: 从成员名中删除开头的“/”
[root@master luoyawei]# tar  czf   /lianxi/luoyawei/boot_passwd_log.tar.gz   /boot   /etc/passwd  /var/log
tar: 从成员名中删除开头的“/”
#/boot,/var/log是文件夹 /etc/passwd是文件

```
