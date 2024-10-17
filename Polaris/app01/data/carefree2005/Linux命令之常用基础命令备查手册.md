
--- 
title:  Linux命令之常用基础命令备查手册 
tags: []
categories: [] 

---
## 一、前言

  家里领导因公司系统部署国产化发展趋势，需要学习Linux。作为Linux初学者，希望能有一篇博文提供学习快速学习和掌握Linux系统的常用基础命令。为了满足领导要求，特编写此博文，尽量将常用Linux命令囊括进来，以示例的方式介绍命令的使用。为了更加贴近需求，博文介绍将以银行麒麟V10操作系统环境为例进行示例介绍。

## 二、常用命令示例

### 1、网络管理
- 查看IP地址，ip address命令或者ifconfig命令
>  
 [root@qlv10 ~]# ip address [root@qlv10 etc]# ifconfig ens18: flags=4163&lt;UP,BROADCAST,RUNNING,MULTICAST&gt; mtu 1500 inet 192.168.0.150 netmask 255.255.255.0 broadcast 192.168.0.255 

- 配置网卡IP、掩码、网关，其中ens18为网卡名称，通过上一个命令可以看到
>  
 [root@qlv10 etc]# vim /etc/sysconfig/network-scripts/ifcfg-ens18 

- 重启网络服务，systemctl restart network
>  
 [root@qlv10 etc]# systemctl restart network 

- 查看路由，使用route -n命令
>  
 [root@qlv10 etc]# route -n 

- 配置DNS，编辑/etc/resolv.conf文件，格式参照下面示例
>  
 [root@qlv10 etc]# vim /etc/resolv.conf nameserver 114.114.114.114 

- 查看监听端口，使用netstat -tnpl查看TCP端口监听情况
>  
 [root@qlv10 etc]# netstat -tnpl 

- 查看防火墙状态，systemctl status firewalld查看防火墙状态，status是查看状态，start可以启动防火墙，stop可以关闭防火墙
>  
 [root@qlv10 etc]# systemctl status firewalld 

- 开通一个端口权限，以开通80端口为例
>  
 [root@qlv10 etc]# firewall-cmd --zone=public --add-port=“80”/tcp --permanent success [root@qlv10 etc]# firewall-cmd --reload success 

- 查看防火墙开放的端口列表
>  
 [root@qlv10 etc]# firewall-cmd --list-all 

- 添加一条静态路由，使用route add命令添加一条静态路由，使用route del命令删除路由
>  
 [root@qlv10 etc]# route add -net 100.1.1.0 netmask 255.255.255.0 gw 192.168.0.186 

- 查看网卡是否连接，Link detected: yes表示已连接，no表示未连接
>  
 [root@qlv10 yhxx]# ethtool ens18 


### 2、系统信息
- 查看系统架构，一般都是x86架构，常见国产服务器为aarch架构
>  
 [root@qlv10 etc]# arch x86_64 

- 查看系统内核版本，uname命令也可以查看系统架构信息，cat /proc/version文件也可以看到内核版本信息
>  
 [root@qlv10 etc]# uname -a Linux qlv10 4.19.90-24.4.v2101.ky10.x86_64 #1 SMP Mon May 24 12:14:55 CST 2021 x86_64 x86_64 x86_64 GNU/Linux [root@qlv10 etc]# cat /proc/version 

- 查看系统版本，国产服务器一般是
>  
 [root@qlv10 etc]# cat /etc/os-release [root@qlv10 etc]# cat /etc/system-release 

- 查看内存大小，free命令可以查看内存及swap的大小及使用情况
>  
 [root@qlv10 etc]# free -h [root@qlv10 etc]# cat /proc/meminfo 

- 查看CPU数量
>  
 [root@qlv10 etc]# cat /proc/cpuinfo 

- 查看系统时间，date命令查看的是系统时钟，clock命令查看的是硬件时钟
>  
 [root@qlv10 etc]# date 2022年 11月 24日 星期四 11:18:10 CST [root@qlv10 etc]# clock 2022-11-24 11:18:21.155292+08:00 

- 查看系统负载
>  
 [root@qlv10 etc]# top 


### 3、进程管理
- 过滤查看某进程，使用ps -ef与grep命令结合，查看指定进程，也可以与netstat -tnpl命令综合一起确认监听端口的进程
>  
 [root@qlv10 etc]# ps -ef |grep ssh 

- 获取指定关键字进程ID，可以与xargs kill命令结合使用杀死指定进程，新手建议使用关键字为可以确定唯一进程的关键字
>  
 [root@qlv10 etc]# pgrep -f tomcat [root@qlv10 etc]# pgrep -f tomcat |xargs kill 

- 查看进程工作路径，3107为进程ID，cdw执行的就是进程服务所在路径
>  
 [root@qlv10 etc]# ll /proc/3107 |grep cwd 

- 杀死进程，使用kill pid命令杀死指定进程，如果无法杀死可以使用kill -9 pid强制杀死进程
>  
 [root@qlv10 etc]# kill 11111 

- 查看在线会话，使用w或者who都可以连接会话，行中有IP地址的为远程连接会话
>  
 [root@qlv10 etc]# who yhxx tty1 2022-11-23 17:57 (:0) root pts/0 2022-11-24 10:44 (192.168.0.186) [root@qlv10 etc]# w 

- 断开会话连接，使用pkill -kill -t ttyid断开指定会话，ttyid为如上的tty1,pts/0
>  
 [root@qlv10 etc]# pkill -kill -t tty1 


### 4、目录和文件管理
- 查看当前路径，使用pwd命令
>  
 [root@qlv10 yhxx]# pwd /home/yhxx 

- 切换目录，使用cd命令，~表示用户家目录，.表示当前目录，…表示上一层目录
>  
 [root@qlv10 ~]# cd /home/yhxx/ 

- 查看目录及文件列表，使用ls -l命令可以看到目录下的文件及目录信息，包括属主、权限等，默认不包括隐藏文件，如果需要查看隐藏文件使用-a参数，如ls -al
>  
 [root@qlv10 yhxx]# ls -l 

- 创建一个文件，使用touch命令
>  
 [root@qlv10 yhxx]# touch a.txt 

- 创建一个目录，使用mkdir命令
>  
 [root@qlv10 yhxx]# mkdir test 

- 创建一个软连接，使用ln命令，创建软连接文件b.txt
>  
 [root@qlv10 yhxx]# ln -s a.txt b.txt 

- 移动目录或者文件，使用mv命令，相当于重命名
>  
 [root@qlv10 yhxx]# mv test/ tt 

- 拷贝文件或者目录，使用cp命令，如果目标路径后跟了文件名则表示拷贝并重命名，如果是递归拷贝可以使用-R参数
>  
 [root@qlv10 yhxx]# cp a.txt tt/c.txt [root@qlv10 yhxx]# cp -R tt test #如上如果test不存在，命令等价于将tt复制为test，如果test存在表示将tt拷贝到test目录下，所以注意查看结果 


### 5、权限管理
- 给文件添加执行权限，使用chmod命令，u+x表示给属主用户添加执行权限，a+x表示给所有用户添加执行权限，如果是需要减少权限则使用u-x，x,r,w分别表示执行，读，写
>  
 [root@qlv10 yhxx]# chmod u+x a.txt 

- 修改文件或目录属主，使用chown user:group命令修改文件或者目录属主，如果需要递归修改目录则需要加上-R参数
>  
 [root@qlv10 yhxx]# chown root.root a.txt [root@qlv10 yhxx]# chown -R root:root tt 

- 添加一个用户
>  
 [root@qlv10 yhxx]# useradd test 

- 修改用户密码，root账户可以使用passwd user修改指定user的密码，不需要输入旧密码，普通用户可以使用passwd修改自己密码，需要输入旧密码确认
>  
 [root@qlv10 yhxx]# passwd yhxx 


### 6、磁盘管理
- 挂载磁盘，使用mount命令挂载磁盘，如果是特殊文件类型还需要加上指定参数，比如挂载iso文件：mount -o loop xx.iso /mnt/cdrom，要求挂载的目录存在
>  
 [root@qlv10 ~]# mount /dev/sr0 /mnt mount: /mnt: WARNING: source write-protected, mounted read-only. 

- 取消挂载
>  
 [root@qlv10 ~]# umount /mnt 

- 查看磁盘利用率
>  
 [root@qlv10 yhxx]# df -hT 

- 查看目录下各文件大小，*表示当前目录下所有文件及目录，使用/dir也可以查看指定目录的大小
>  
 [root@qlv10 yhxx]# du -sh * [root@qlv10 yhxx]# du -sh /tmp 


### 7、文件查看、打包、搜索
- 查看文件，可以使用cat、head、tail命令查看文件。cat可以结合more,less命令翻页查看，more只可以向后翻页，less可以用翻页键上下翻页
>  
 [root@qlv10 yhxx]# cat a.txt 士兵是个好人，很坚强 将军是个好人，很威武 

- 查看前n行
>  
 [root@qlv10 yhxx]# head -n 1 a.txt 士兵是个好人，很坚强 

- 查看后n行，我们常用tail -fn查看应用日志后面的n行，动态更新的最后N行日志：tail -fn 100 tomcat.out
>  
 [root@qlv10 yhxx]# tail -n 1 a.txt 将军是个好人，很威武 

- 将目录tar包为一个文件，可以将1个或者多个文件tar包为1个文件
>  
 [root@qlv10 yhxx]# tar -cvf test.tar test/ tt/ test/ test/c.txt test/tt/ test/tt/c.txt tt/ tt/c.txt 

- 解开tar包文件，如果是解开压缩的tar包文件，使用tar -zxvf
>  
 [root@qlv10 yhxx]# tar -xvf test.tar 

- tar包并压缩文件，tar包时还可以使用–exclude=log，排除指定文件或者目录
>  
 [root@qlv10 yhxx]# tar -zcvf test.tar.gz test/ tt/ test/ test/c.txt test/tt/ test/tt/c.txt tt/ tt/c.txt 

- zip压缩文件，可以将多个文件或目录压缩为1个文件，使用unzip命令解压，如果是需要将文件打包下载到window环境，建议使用zip命令，一般window环境都可以解压
>  
 [root@qlv10 yhxx]# zip -r test.zip test tt adding: test/ (stored 0%) adding: test/tt/ (stored 0%) adding: test/tt/c.txt (stored 0%) adding: test/c.txt (stored 0%) adding: tt/ (stored 0%) adding: tt/c.txt (stored 0%) 

- 搜索指定文件，搜索当前目录下的txt文件
>  
 [root@qlv10 yhxx]# find . -name “*.txt” 

- 查询二进制文件存储路径
>  
 [root@qlv10 yhxx]# which java /usr/bin/java 


### 8、系统关机和重启
- 重启系统，如下命令都可以重启系统，重启或者关机需要root账户或者具有sudo权限的普通账户才可以执行
>  
 [root@qlv10 yhxx]# reboot [root@qlv10 yhxx]# halt --reboot [root@qlv10 yhxx]# poweroff --reboot [root@qlv10 yhxx]# shutdown -r [root@qlv10 ~]# init 6 

- 关机，如下命令都可以关机
>  
 [root@qlv10 ~]# poweroff [root@qlv10 ~]# shutdown -P [root@qlv10 ~]# halt -p [root@qlv10 ~]# init 0 

- 定时重启系统，在晚上10点重启系统
>  
 [root@qlv10 ~]# shutdown -r 22:00:00 &amp; 

- 定时关机，在晚上10点关闭操作系统
>  
 [root@qlv10 ~]# shutdown -h 22:00:00 &amp; 


### 9、文件的上传下载
- 单个文件的下载，使用CRT终端工具连接可以使用sz file命令下载指定文件，默认下载到CRT配置好的目录，如果目录不存在则会要求弹窗选择
>  
 [root@qlv10 yhxx]# sz a.txt 

- 上传单个文件，使用rz命令上传，-y表示文件如果存在则覆盖
>  
 [root@qlv10 yhxx]# rz -y 

- scp方式上传本地文件到远端，如果是上传下载目录加上-r参数，需要输入远端服务器密码后开始上传
>  
 [root@qlv10 yhxx]# scp -r test 192.168.0.142:/tmp/ 

- scp方式将远端文件或者目录下载到本地，示例将远端的test.tar下载到当前目录，需要输入远端服务器密码后开始下载
>  
 [root@qlv10 yhxx]# scp 192.168.0.142:/tmp/test.tar ./ 


### 10、依赖软件的安装和卸载
- YUM安装软件，可以自动查找并安装依赖包
>  
 [root@qlv10 yhxx]# yum install -y vim 

- YUM卸载软件
>  
 [root@qlv10 yhxx]# yum remove vim 

- 查询是否安装指定包，可以使用rpm -qa查询
>  
 [root@qlv10 yhxx]# rpm -qa |grep ssh 

- 安装rpm包，使用-ivh可以安装指定包
>  
 [root@qlv10 yhxx]# rpm -ivh epel-release-latest-7.noarch.rpm 

- 卸载rpm包，使用-e卸载指定包，–nodeps类似强制卸载
>  
 [root@qlv10 yhxx]# rpm -e --nodeps mariadb-server-10.3.9-9.p02.ky10.x86_64 


### 11、查看硬件信息

  查看系统硬件信息可以使用dmidecode命令，关于此命令详解可以参考博文：
- 查看主板信息
>  
 [root@qlv10 yhxx]# dmidecode -t 2 

- 查看内存信息
>  
 [root@qlv10 yhxx]# dmidecode -t 16 

- 查看CPU信息
>  
 [root@qlv10 yhxx]# dmidecode -t 4 


### 12、shell脚本执行

  关于shell脚本执行的四种方式见博文：

### 13、其他

  其他更多关于Linux命令详解及示例见我的博客专栏：，也可以访问我的博客主页，在搜索框输入Linux命令或者待查询的命令。 <img src="https://img-blog.csdnimg.cn/ec5ff8ed68b6401bbfe26c4be37410ef.png" alt="在这里插入图片描述">
