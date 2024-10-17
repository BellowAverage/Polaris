
--- 
title:  rsync 远程同步 
tags: []
categories: [] 

---
## 详解rsync远程同步



#### 文章目录
- - <ul><li>- - - - - 


### 1、关于rsync

**remote sync ，远程同步；**

是一个开源的快速备份工具，可以在不同主机之间镜像同步整个目录树，支持增量备份，并保持链接和权限，且采用优化的同步算法，传输前执行压缩，因此非常适用于异地备份、镜像服务器等应用。

在远程同步任务中，负责发起rsync同步操作的客户机称为发起端，而负责响应来自客户机的rsync同步操作的服务器称为同步源。在同步过程中，同步源负责提供文件的原始位置，发起端应对该位置具有读取权限。

**在下行同步（下载）中**，同步源负责提供文档的原始位置，发起端应对该位置有读取权限。

**在上行同步（上传）中**，同步源负责提供文档的目标位置，发起端应对该位置具有写入权限。

<img src="https://img-blog.csdnimg.cn/049e057612704192a4c45bbeace90cdf.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LyK5rKz5paw5p2R,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/fa418894e5864565b168ffe2130032ae.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LyK5rKz5paw5p2R,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

基本思路：
- 建立rsyncd.conf配置文件、独立的账号文件- 启用rsync的–daemon模式
应用示例：
- 用户backuper，允许下行同步- 操作的目录为/var/www/html/
rsync账号文件：
- 采用 账号：密码 的记录格式，每行一个用户记录。- 独立的账号数据，不依赖与系统账号。
### 2、rsync 使用语法及参数详解：

rsync [选项] 原始位置 目标位置

**常用选项**： -a：归档模式，递归并保留对象属性，等同于-rlptgoD

-v：显示同步过程的详细(verbose)信息 -z∶在传输文件时进行压缩(compress)

-H：保留硬连接文件 -A：保留ACL属性信息 –delete：删除目标位置有而原始位置没有的文件

–checksum：根据对象的校验和来决定是否跳过文件

–配置源的两种格式–
1. 用户名@主机地址::共享模块名 或<li> 
  <ol start="2">1. rsync://用户名@主机地址/共享模块名
### 3、rsync配置流程：

```
1.基本思路
- 建立rsyncd.conf配置文件、独立的账号文件
- 启用rsync的 --daemon模式

----

2.配置文件 rsyncd.conf
- 认证配置 auth users、secrets file，不加则为匿名

----

3.独立的账号文件
- 用户名:密码
- 每行一个用户记录
- 独立的账号数据，不依赖系统账号

----

4.启用 rsync 服务
- 通过"--daemon"独自提供服务（rsync --daemon）
- 执行"kill $(cat /var/run/rsyncd.pid)"关闭服务

```

### 4、实际操作

```
#关闭防火墙和SELinux
systemctl stop firewalld
setenforce 0
#查看rsync rpm包
[root@localhost ~]#rpm -q rsync 
rsync-3.0.9-18.el7.x86_64

[root@localhost ~]#vim /etc/rsyncd.conf 
uid = nobody
gid = nobody
use chroot = yes
pid file = /var/run/rsyncd.pid
dont compress   = *.gz *.tgz *.zip *.z *.Z *.rpm *.deb *.bz2
address = 192.168.111.10
port = 873
log file = /var/log/rsycd.log
hosts allow = 192.168.111.0/24
[swl]
path = /var/www/html
comment = web service
read only = yes
auth users = bak
secrets file = /root/rsyncd_users.db


uid = nobody
gid = nobody
use chroot = yes
#禁锢在源目录
address = 192.168.111.10
#监听地址
port 873
#监听端口号 tcp/udp 873
log file = /var/log/rsyncd.log
#日志地址
pid file = /var/run/rsyncd.pid
#存放进程ID的文件位置
hosts allow = 192.168.111.0/24
#允许访问的客户机地址

[swl]
#共享模块名称
path = /home/swl
#原目录实际路径
comment = ftp export area
#备注
read only = yes
#是否只读
dont comperss = *.gz *.bz2 *.tgz *.zip *.rar *.z
#同步时不再压缩的文件类型
auth users = backuper
#授权账户，多个账号以空格分隔
secrets file = /etc/rsyncd_users.db
#存放账户信息的数据文件

```

```
###如果采用匿名的方式，只要将其中的“auth users” 和“secrets file” 配置项去掉即可
#为备份账户创建数据文件
#建立同步用户
[root@localhost ~]#vim /root/rsyncd_users.db
backuper:123456

#一定要600 权限
[root@localhost ~]#chmod 600 /root/rsyncd_users.db

[root@localhost ~]#chmod +r /var/www/html
[root@localhost ~]#rsync --daemon
#守护进程后台运行
[root@localhost ~]# netstat -anpt |grep rsync
[root@localhost ~]# kill `cat /var/run/rsyncd.pid`

################发起端（客户端）####################
客户端： rsync [选项] 原始位置 目标位置
常用选项###
-r:递归模式,包含目录及子目录中的所有文件。
-l:对于符号链接文件仍然复制为符号链接文件。
-V:显示同步过程的详细（verbose）信息。
-z：在传输文件时进行压缩（compress）
-a：归档模式，递归并保留对象属性，等同于 -rlptgoD
-p:保留文件的权限标记。
-t:保留文件的时间标记
-g:保留文件的属组标记（仅超级用户使用）。
-o:保留文件的属主标记（仅超级用户使用）
-H：保留硬连接文件
-A：保留ACL属性信息
-D:保留设备文件及其他特殊文件。
--delete：删除目标位置有而原始位置没有的文件
--checksum：根据对象的校验和来决定是否跳过文件

[root@localhost mnt]#rsync -avz bak@192.168.111.20::swl /opt/test
[root@localhost mnt]#rsync -avz rsync://backuper@192.168.111.10/ky15 /mnt


免交互配置：
echo "123123" &gt; /etc/server.pass
chmod 600 /etc/server.pass

crontab -e
30 22 * * * /usr/bin/rsync -az --delete --password-file=/etc/server.pass backuper@192.168.111.10::ky15 /mnt/


[root@localhost mnt]#echo "123123" &gt;server.pass
[root@localhost mnt]#chmod 600 server.pass
[root@localhost mnt]#rsync -avz --password-file=/mnt/server.pass backuper@192.168.91.100::ky15 /mnt/

[root@localhost mnt]#crontab -e
30 23 * * * /usr/bin/rsync -az --password-file=/mnt/server.pass backuper@192.168.111.20::swl /opt/test
[root@localhost mnt]#crontab -l


```

### 5、rsync实时同步

使用inotify通知接口，可以用来监控文件系统的各种变化情况，如文件存取、删除、移动、修改等。利用这一机制，可以非常方便地实现文件异动告警、增量备份，并针对目录或文件的变化及时作出响应。

将inotify机制与rsync相结合，可以实现**触发式备份（实时同步)**，即只要原始位置的文档发生变化，则立即启动增量备份操作；否则处于静默等待状态。这样，就避免了按固定周期备份时存在的延迟性、周期过密等问题。

因为inotify通知机制由 Linux内核提供，因此主要做本机监控，在触发式备份中，应用时更适合上行同步。

```
[root@localhost ~]#vim /etc/rsyncd.conf 
read only = no
#修改只读模式为no
[root@localhost ~]#ss -ntap |grep rsync
[root@localhost ~]#kill 进程号
[root@localhost ~]#chmod 777 /var/www/html/
[root@localhost ~]#ll -d /var/www/html/
drwxrwxrwx. 3 root root 68 12月 12 23:22 /var/www/html/

#调整inotify内核参数
max_queue_events：监控队列大小 默认16384
max_user_instances：最多监控实例数 默认 128
max_user_watches：每个实例最多监控文件数 默认8192

[root@localhost ~]#cat /proc/sys/fs/inotify/max_queued_events 
16384
[root@localhost ~]#cat /proc/sys/fs/inotify/max_user_instances 
128
[root@localhost ~]#cat /proc/sys/fs/inotify/max_user_watches 
8192

[root@localhost ~]# vim /etc/sysctl.conf
fs.inotify.max_queued_events = 32768
fs.inotify.max_user_instances = 1024
fs.inotify.max_user_watches = 1048576
#刷新一下
[root@localhost ~]# sysctl -p

#####安装inotify#####
安装inotify-tools辅助工具
inotifywait：用于持续监控，实时输出结果（增删改属性修改）
inotifywatch：用于短期监控，任务完成后再出汇总结果

[root@localhost opt]#tar xf inotify-tools-3.14.tar.gz 
[root@localhost opt]#cd inotify-tools-3.14/
[root@localhost inotify-tools-3.14]#./configure
#编译安装
[root@localhost inotify-tools-3.14]#make &amp;&amp; make install

##开启客户端
[root@localhost inotify-tools-3.14]#mkdir /var/www/html -p
[root@localhost inotify-tools-3.14]#cd /var/www/html/
##可以先执行“inotifywait”命令，然后另外再开启一个新的终端向 /var/www/html 目录下添加文件、移动文件，在原来的终端中跟踪屏幕输出结果。
[root@localhost ~]# inotifywait -mrq -e modify,create,move,delete  /var/www/html
-e 用来指定要监控哪些事情
-m 表示持续监控
-r 表示递归整个目录
-q 简化输出信息

[root@localhost ~]# chmod 777 /var/www/html/
#在另外一个终端编写触发式同步脚本
[root@localhost html]#vim /opt/inotify.sh
#!/bin/bash
INOTIFY_CMD="inotifywait -mrq -e create,delete,move,modify,attrib /var/www/html"
RSYNC_CMD="rsync -azH --delete --password-file=/root/server.pass /var/www/html bak@192.168.111.20::swl"

$INOTIFY_CMD | while read DIRECTORY EVENT FILE
do
    if [ $(pgrep rsync | wc -l) -le 0 ] ; then
        $RSYNC_CMD
#       echo "${FILE} was rsynced" &gt;&gt;/opt/inotify_rsync.log

    fi
done
#给脚本赋权并在后台执行
[root@localhost html]#chmod +x /opt/inotify

###去主节点
[root@localhost html]#rm -rf *


rsync可以快速删除大量文件
在主节点上  创建文件
[root@localhost html]#touch file{1..1000}.txt
[root@localhost opt]#rsync --delete-before -aHv --progress -stats /opt/ /var/www/html/
#找个空文件

```

### 总结：
- rsync 为下行同步，即源端同步到发送端；- 但rsync+inotify正好相反，是发送端同步到源端；