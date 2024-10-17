
--- 
title:  勇敢牛牛yum版MySQL搭建MHA 
tags: []
categories: [] 

---
## 超牛yum版MySQL，搭建MHA



#### 文章目录
- - <ul><li>- - - - - <ul><li>- - - - - - - 


<img src="https://img-blog.csdnimg.cn/e5016cbcb2b04f0b9844c8c9d7dfba87.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 1、服务器安装mysql：

没有安装MySQL的同学，可以看这篇博客，这里详细展示了MySQL的三种安装方式，包括yum安装MySQL。

https://blog.csdn.net/weixin_53060366/article/details/121623206?spm=1001.2014.3001.5501

这些安装教程都是针对MySQL7版本的，大家多注意一下。

```
#准备四台虚拟机,关闭防火墙及selinux
master：192.168.111.100
slave1：192.168.111.122
slave2：192.168.111.130
mha：192.168.111.128

#关闭防火墙
systemctl stop firewalld
systemctl disable firewalld
setenforce 0

```

### 2、免密操作：

在实验前对所有服务器进行免密登入操作：（master，slave1，slave2，mha）

```
#在所有服务器上配置无密码认证
#mha服务器
ssh-keygen
ssh-copy-id 192.168.111.100
ssh-copy-id 192.168.111.122
ssh-copy-id 192.168.111.130

#master服务器
ssh-keygen
ssh-copy-id 192.168.111.122
ssh-copy-id 192.168.111.130

#slave1服务器
ssh-keygen
ssh-copy-id 192.168.111.100
ssh-copy-id 192.168.111.130

#slave2服务器
ssh-keygen
ssh-copy-id 192.168.111.100
ssh-copy-id 192.168.111.122

```

这里的步骤相同，只演示一个操作，其他的只需要注意一下ssh要免密登入的服务器IP地址即可；

<img src="https://img-blog.csdnimg.cn/498d2cdb62aa48798ea86a04e44def76.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/78e4fce5a3ef4b908a8a0ac57af40dd4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 3、MySQL配置文件的重铸：

这里主要是修改3台主从服务器的配置文件；

配置文件的位置：/etc/my.cnf

注意三台服务器的 server-id 不能一样

```
#修改 master 服务器
[root@localhost ~]#vim /etc/my.cnf
[mysqld]
server-id = 1
log_bin = master-bin
log-slave-updates = true

#修改 slave1 服务器
server-id = 2
log_bin = master-bin
relay-log = relay-log-bin
relay-log-index = slave-relay-bin.index

#修改 slave2 服务器
server-id = 3 
log_bin = master-bin
relay-log = relay-log-bin
relay-log-index = slave-relay-bin.index

#最后重启三台服务器，三台都要重启MySQL；
systemctl restart mysqld

```

<img src="https://img-blog.csdnimg.cn/fb5640c291084426948924ed2653a79e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/3ef2cabc710b43f28ef0fa15974a2d8c.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/1dd26ed1c5bb45f989c8b30ed24fd42c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/802a49ed39b244eebad59f7a387549ea.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 4、MySQL主从复制：

这里MySQL主从复制，在master 服务器上设置权限；

```
# master 节点
#登录数据库，设置权限
[root@localhost ~]# mysql -u root -p
mysql&gt; grant all on *.* to 'tom'@'192.168.111.%' identified by 'TikS@123';
mysql&gt; show master status;

```

<img src="https://img-blog.csdnimg.cn/4501ad273b274cc28bf471b1dfdc4158.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

两个从服务器设置：（slave1，slave2）

```
#登入数据库
[root@localhost ~]# mysql -u root -p
#从节点配置
mysql&gt; change master to master_host='192.168.111.100',master_user='tom',master_password='TikS@123',master_log_file='master-bin.000001',master_log_pos=445;

mysql&gt; start slave;
Query OK, 0 rows affected (0.00 sec)

mysql&gt; show slave status\G

#设置两个从节点 只读模式
set global read_only=1;

```

<img src="https://img-blog.csdnimg.cn/baca2b973e134c0c82fd462d7a370f61.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

**验证一下：**

在master服务器上创建一个用户，用两个slave服务器查看是否创建；

<img src="https://img-blog.csdnimg.cn/31d2c1b5fbbc41a7b5030ad614765668.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/00d580018c934faea976e4ef7aaabfa2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/4e5410107af34590812e745db819fc19.png#pic_center" alt="在这里插入图片描述">

这里主从都需要授权一个 mha 时用到的用户；

```
mysql&gt; grant all privileges on *.* to 'tom'@'192.168.111.%' identified by 'TikS@123';

```

<img src="https://img-blog.csdnimg.cn/0107b3676d5f441b8630d480d204c9a2.png#pic_center" alt="在这里插入图片描述">

### 5、安装和配置MHA：

#### （1）node 节点安装：

先在所有服务器上必须先安装 node 组件。（master，slave1，slave2，mha）

```
#先安装工具包
yum -y install perl-ExtUtils-CBuilder perl-ExtUtils-MakeMaker perl-DBD-MySQL perl-devel perl-CPAN

#上传mha的node压缩包
mha4mysql-node-0.57.tar.gz （可自行去官网下载）
#创建压缩包放置目录，将压缩包拖进该目录
mkdir /etc/mha
cd /etc/mha/
[root@localhost mha]#tar -zxf mha4mysql-node-0.57.tar.gz 
[root@localhost mha]#ls
mha4mysql-node-0.57  mha4mysql-node-0.57.tar.gz
[root@localhost mha]#mv mha4mysql-node-0.57 node
[root@localhost mha]#ls
mha4mysql-node-0.57.tar.gz  node
[root@localhost mha]#cd node
[root@localhost node]#ls
AUTHORS  bin  COPYING  debian  inc  lib  Makefile.PL  MANIFEST  META.yml  README  rpm  t
[root@localhost node]#perl Makefile.PL 
[root@localhost node]#make &amp;&amp; make install

```

<img src="https://img-blog.csdnimg.cn/e1427157ce6e4fcd93b0b3bccbdd2a01.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/321ba6789214455086e3f44fdb50e73e.png#pic_center" alt="在这里插入图片描述">

#### （2）manager节点安装：（mha）

这个只需要在mha服务器上安装，在 MHA-manager 节点上安装 manager 组件，因为 manager 依赖 node 组件。

```
yum -y install epel-release --nogpgcheck
yum -y install perl-Config-Tiny perl-Log-Dispatch perl-Parallel-ForkManager perl-Time-HiRes

#上传mha的manager的源码包
#mha4mysql-manager-0.57.tar.gz (可自行去官网下载)
#创建压缩包放置目录，将压缩包拖进该目录
[root@linux mha]#ls
mha4mysql-manager-0.57.tar.gz  mha4mysql-node-0.57.tar.gz  node
[root@linux mha]#tar zxf mha4mysql-manager-0.57.tar.gz 
[root@linux mha]#ls
mha4mysql-manager-0.57  mha4mysql-manager-0.57.tar.gz  mha4mysql-node-0.57.tar.gz  node
[root@linux mha]#mv mha4mysql-manager-0.57 manager
[root@linux mha]#ls
manager  mha4mysql-manager-0.57.tar.gz  mha4mysql-node-0.57.tar.gz  node
[root@linux mha]#cd manager/
[root@linux manager]#ls
AUTHORS  bin  COPYING  debian  inc  lib  Makefile.PL  MANIFEST  META.yml  README  rpm  samples  t  tests
[root@linux manager]#perl Makefile.PL 
[root@linux manager]#make &amp;&amp; make install

```

<img src="https://img-blog.csdnimg.cn/05be3e260d5e447db9ee180b77e38193.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/9d8dab67d24f4e95bee27d6cc8a1e806.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/fa6bb728f1894c31b05c12479e26cee8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/27c68cb2ea564d8f93a78f99ce234fb0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

#### （3）修改manager的配置文件：

```
#创建工作存放文件，
[root@linux manager]#mkdir /etc/mha/app1
[root@linux manager]#cp samples/conf/app1.cnf ../
[root@linux manager]#cd ../
[root@linux mha]#ls
app1  app1.cnf  manager  mha4mysql-manager-0.57.tar.gz  mha4mysql-node-0.57.tar.gz  node

[root@linux mha]#vim app1.cnf 
[server default]
manager_workdir=/etc/mha/app1
manager_log=/etc/mha/app1/manager.log
master_binlog_dir="/var/lib/mysql"
remote_workdir=/etc/mha/app1
master_ip_failover_script=/etc/mha/master_ip_failover
master_ip_online_change_script=/etc/mha/master_ip_online_change
report_script=/etc/mha/send_report
user=tom
password=TikS@123
repl_user=tom
repl_password=TikS@123
ping_interval=1
secondary_check_script= masterha_secondary_check -s 192.168.111.122 -s 192.168.111.130

[server1]
hostname=192.168.111.100
port=3306
ssh_port=22

[server2]
hostname=192.168.111.122
port=3306
ssh_port=22
candidate_master=1
check_repl_delay=0

[server3]
hostname=192.168.111.130
port=3306
no_master=1
ssh_port=22

```

<img src="https://img-blog.csdnimg.cn/0fe848870b7646a5918d055d957c3a38.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/7905c42b0aac4dc992a218599f299d37.png#pic_center" alt="在这里插入图片描述">

#### （4）编写脚本：（slave1，slave2）

```
设置日志清洗
[root@localhost ~]# mysql -u root -p
mysql&gt; set global relay_log_purge=0;
Query OK, 0 rows affected (0.00 sec)

```

<img src="https://img-blog.csdnimg.cn/62a87ca2e7bd40e280aa4a07182b20e2.png#pic_center" alt="在这里插入图片描述">

```
#创建软连接
[root@localhost ~]# mkdir /var/lib/mysql/log1
[root@localhost ~]# ln -s /var/lib/mysql/relay-log* /var/lib/mysql/log1/
[root@localhost ~]# vim /etc/mha/purge_relay_log.sh
#!/bin/bash
user=root
passwd=TikS@821
port=3306
log_dir=’/var/lib/mysql/’
work_dir=’/var/lib/mysql/logs1’
purge=’/usr/local/bin/purge_relay_logs’
if [ ! -d $log_dir ]
then
mkdir $log_dir -p
fi
$purge --user=$user --password=$passwd --disable_relay_log_purge --port= $port --host=localhost --workdir=$work_dir &gt;&gt; $log_dir/purge_relay_logs.log 2&gt;&amp;1

```

<img src="https://img-blog.csdnimg.cn/4138d14db4b6435f9e85e0d7a41495eb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

测试一下：

```
purge_relay_logs --user=root --host=localhost --port=3306 --password=TikS@821 -disable_relay_log_purge --workdir=/var/lib/mysql/

```

<img src="https://img-blog.csdnimg.cn/43abe779168c43efb9e0bf864f7f5c90.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

做个定时任务，每周自动清理日志文件：

```
[root@localhost ~]# crontab -e
0 0 */5 * * bash /etc/auto_clean_relay_log.sh

```

#### （5）自动切换脚本：（master，slave1，slave2，mha）

首先编写自动切换脚本：

```
vim /etc/mha/master_ip_failover
#!/usr/bin/env perl
use strict;
use warnings FATAL =&gt; 'all';
use Getopt::Long;
my (
$command, $ssh_user, $orig_master_host, $orig_master_ip,
$orig_master_port, $new_master_host, $new_master_ip, 			$new_master_port
);
my $vip = '192.168.111.188/24';
my $key = '0';
my $ssh_start_vip = "/sbin/ifconfig ens33:$key $vip";
my $ssh_stop_vip = "/sbin/ifconfig ens33:$key down";
GetOptions(
'command=s' =&gt; \$command,
'ssh_user=s' =&gt; \$ssh_user,
'orig_master_host=s' =&gt; \$orig_master_host,
'orig_master_ip=s' =&gt; \$orig_master_ip,
'orig_master_port=i' =&gt; \$orig_master_port,
'new_master_host=s' =&gt; \$new_master_host,               'new_master_ip=s' =&gt; \$new_master_ip,
'new_master_port=i' =&gt; \$new_master_port,
 );
exit &amp;main();
sub main {<!-- -->
print "\n\nIN SCRIPT TEST====$ssh_stop_vip==$ssh_start_vip===\n\n";
if ( $command eq "stop" || $command eq "stopssh" ) {<!-- -->
my $exit_code = 1;
eval {<!-- -->
print "Disabling the VIP on old master: $orig_master_host \n";
&amp;stop_vip();
$exit_code = 0;
};
if ($@) {<!-- -->
warn "Got Error: $@\n";
exit $exit_code;
}
exit $exit_code;
}
elsif ( $command eq "start" ) {<!-- -->
my $exit_code = 10;
eval {<!-- -->
print "Enabling the VIP - $vip on the new master - $new_master_host \n";
&amp;start_vip();
$exit_code = 0;
};
if ($@) {<!-- -->
warn $@;
exit $exit_code;
}
exit $exit_code;
}
elsif ( $command eq "status" ) {<!-- -->
print "Checking the Status of the script.. OK \n";
exit 0;
}
else {<!-- -->
&amp;usage();
exit 1;
}
}
sub start_vip() {<!-- -->
`ssh $ssh_user\@$new_master_host \" $ssh_start_vip \"`;
}
sub stop_vip() {<!-- -->
return 0 unless ($ssh_user);
`ssh $ssh_user\@$orig_master_host \" $ssh_stop_vip \"`;
}
sub usage {<!-- -->
print
"Usage: master_ip_failover --command=start|stop|stopssh|status --orig_master_host=host --orig_master_ip=ip
--orig_master_port=port --new_master_host=host --new_master_ip=ip --new_master_port=port\n";
}

```

<img src="https://img-blog.csdnimg.cn/e41e5d45fee14478ba03c45b207a3455.png#pic_center" alt="在这里插入图片描述">

对刚才的脚本文件授权：（所有服务器）

```
[root@localhost node]#chmod +x /etc/mha/master_ip_failover

```

#### （6）manager检测及开启：（mha）

**ssh免密检测：**

```
/etc/mha/manager/bin/masterha_check_ssh --conf=/etc/mha/app1.cnf

```

<img src="https://img-blog.csdnimg.cn/4af7a96a904b46fa95f1278625eaad1f.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b0122b0e3fd945a2a76d0e7eabf5d3ec.png#pic_center" alt="在这里插入图片描述">

**检测mysql主从是否正常：**

```
/etc/mha/manager/bin/masterha_check_repl --conf=/etc/mha/app1.cnf

```

<img src="https://img-blog.csdnimg.cn/d5a16188a1784fe5b63bdc34da98c322.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/a60b327e9fc649478851e64d85a0669a.png#pic_center" alt="在这里插入图片描述">

#### （7）对 master 节点设置虚拟网卡：

```
ifconfig ens33:0 192.168.111.188 netmask 255.255.255.0

```

<img src="https://img-blog.csdnimg.cn/16c78f2f0ea94a9c87f1e6a0d2f5d4a5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5c3bcc832fb04125ab021cc99e856a40.png#pic_center" alt="在这里插入图片描述">

在mha 服务器上：

```
#启动manager
nohup /etc/mha/manager/bin/masterha_manager --conf=/etc/mha/app1.cnf --ignore_last_failover &gt;/tmp/mha_manager.log &lt; /dev/null 2&gt;&amp;1 &amp;

#查看主的状态
/etc/mha/manager/bin/masterha_check_status --conf=/etc/mha/app1.cnf

```

<img src="https://img-blog.csdnimg.cn/d57013fcfab440cb8a505c4d3062e629.png#pic_center" alt="在这里插入图片描述">

#### （8）测试:

**关闭 master 的mysql：**

systemctl stop mysqld.service

**在 mha 上查看manager的日志** tail -f /etc/mha/app1/manager.log

<img src="https://img-blog.csdnimg.cn/fdf4fe42f14f41a3b29941493e0ddf6a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/efbb0bd7139b4eebaa4fdd0bfb22d1bc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/0ee862a2164d4c56bf4c2d3aa60c7cb3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

Vip漂移到 slave1(122) 服务器，成为了新主，然后启动旧主 100 的mysql，为122和100做mysql主从；

```
#进入新主122的mysql，查看节点
[root@localhost node]#mysql -uroot -p
mysql&gt; show master status;

#启动100的mysql
[root@localhost node]#systemctl start mysqld
[root@localhost node]#mysql -uroot -p
change master to master_host='192.168.111.122',master_user='tom',master_password='TikS@123',master_log_file='master-bin.000001',master_log_pos=445;
start slave;
show slave status\G

```

<img src="https://img-blog.csdnimg.cn/b57d212ecb2d4e6789fac6419bd85eb9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d8dddb9bfd5547e9a9afa63600be3fd7.png#pic_center" alt="在这里插入图片描述">

```
#修改 mha（128）的配置文件
[root@linux mha]#vim /etc/mha/app1.cnf

```

<img src="https://img-blog.csdnimg.cn/93ecf7016a284af6a3f4e6ca84a7452c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

**启动manager**

nohup /etc/mha/manager/bin/masterha_manager --conf=/etc/mha/app1.cnf --ignore_last_failover &gt;/tmp/mha_manager.log &lt; /dev/null 2&gt;&amp;1 &amp;

**查看状态，此时主为122**

/etc/mha/manager/bin/masterha_check_status --conf=/etc/mha/app1.cnf

<img src="https://img-blog.csdnimg.cn/5fa078e08c31443d897b634e2b533fc1.png#pic_center" alt="在这里插入图片描述">

此时再去关闭122的mysql，去100的服务器上查看ip，就可以看到VIP又回到了100，100又变回了主，

之后再去开,122的mysql，与100做主从，重复以上步骤，看vip是否漂移就欧克啦！

<img src="https://img-blog.csdnimg.cn/50d1159420254496994221618b5c7ef7.png#pic_center" alt="在这里插入图片描述">
