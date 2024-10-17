
--- 
title:  python psutil模块详解以及编写监控脚本 
tags: []
categories: [] 

---
## psutil详解

### 一、介绍

用Python来编写脚本简化日常的运维工作是Python的一个重要用途。在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，如`ps`，`top`，`free`等等。要获取这些系统信息，Python可以通过`subprocess`模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。

在Python中获取系统信息的另一个好办法是使用`psutil`这个第三方模块。顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。

### 二.安装psutil模块

```
[root@master yum.repos.d]# yum  install gcc  python3-devel -y
[root@master yum.repos.d]# pip3  install psutil

```

### 三、模块的使用

#### 3.1 获取cpu信息

```
&gt;&gt;&gt; import psutil
&gt;&gt;&gt; psutil.cpu_
psutil.cpu_count(          psutil.cpu_percent(        psutil.cpu_times(
psutil.cpu_freq(           psutil.cpu_stats(          psutil.cpu_times_percent(

#默认返回逻辑CPU的个数,当设置logical的参数为False时，返回物理CPU的个数。
&gt;&gt;&gt; psutil.cpu_count()
2
#cpu的物理核心
&gt;&gt;&gt; psutil.cpu_count(logical=False)
2
#返回CPU的利用率,percpu为True时显示所有物理核心的利用率,interval不为0时,则阻塞时显示interval执行的时间内的平均利用率
&gt;&gt;&gt; psutil.cpu_percent()
0.1
#cpu用户／系统／空闲时间
&gt;&gt;&gt; psutil.cpu_times()
scputimes(user=2701.86, nice=2.3, system=1819.85, idle=1728893.15, iowait=172.23, irq=0.0, softirq=416.82, steal=0.0, guest=0.0, guest_nice=0.0)
#cpu频率
&gt;&gt;&gt; psutil.cpu_freq()
scpufreq(current=1800.004, min=0.0, max=0.0)
#以命名元组的形式返回CPU的统计信息，包括上下文切换，中断，软中断和系统调用次数。
&gt;&gt;&gt; psutil.cpu_stats()
scpustats(ctx_switches=107918325, interrupts=61923152, soft_interrupts=72724668, syscalls=0)
#cpu使用时间百分比
&gt;&gt;&gt; psutil.cpu_times_percent()
scputimes(user=0.0, nice=0.0, system=0.1, idle=99.9, iowait=0.0, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)

#实现类似top命令的CPU使用率，每秒刷新一次，累计10次
&gt;&gt;&gt; for x in range(10):
...     print(psutil.cpu_percent(interval=1,percpu=True)) #返回CPU的利用率,percpu为True时显示所有物理核心的利用率,interval不为0时,则阻塞时显示interval执行的时间内的平均利用率
... 
[0.0, 0.0]
[1.0, 0.0]
[0.0, 0.0]
[0.0, 0.0]
[0.0, 0.0]
[0.0, 0.0]
[0.0, 0.0]
[0.0, 1.0]
[0.0, 0.0]
[0.0, 0.0]

```

#### 3.2 获取内存信息

```
&gt;&gt;&gt; psutil.virtual_memory()
svmem(total=1907744768, available=1375522816, percent=27.9, used=346296320, free=225312768, active=592613376, inactive=835293184, buffers=0, cached=1336135680, shared=4149248, slab=134766592)
&gt;&gt;&gt; psutil.virtual_memory().percent
27.9

&gt;&gt;&gt; psutil.swap_memory()
sswap(total=2147479552, used=147595264, free=1999884288, percent=6.9, sin=7364608, sout=152559616)

```

返回的是字节为单位的整数，可以看到，总内存大小是1907744768=1.7G，已用346296320=0.3G，使用了27.9%。

而交换区大小是2147479552=2G。

#### 3.3 获取磁盘信息

可以通过psutil获取<mark>磁盘分区、磁盘使用率和磁盘IO信息</mark>

```
&gt;&gt;&gt; psutil.disk_
psutil.disk_io_counters(  psutil.disk_partitions(   psutil.disk_usage(

#disk_io_counters([perdisk])：以命名元组的形式返回磁盘io统计信息(汇总的)，包括读、写的次数，读、写的字节数等。
#当perdisk的值为True，则分别列出单个磁盘的统计信息(字典：key为磁盘名称，value为统计的namedtuple)。
&gt;&gt;&gt; psutil.disk_io_counters()
sdiskio(read_count=34398, write_count=294425, read_bytes=4553839616, write_bytes=32097749504, read_time=3360863, write_time=20864691, read_merged_count=1118, write_merged_count=42832, busy_time=3063547)

#disk_partitions([all=False])：以命名元组的形式返回所有已挂载的磁盘，包含磁盘名称，挂载点，文件系统类型等信息。
#当all等于True时，返回包含/proc等特殊文件系统的挂载信息
&gt;&gt;&gt; psutil.disk_partitions()
[sdiskpart(device='/dev/mapper/centos-root', mountpoint='/', fstype='xfs', opts='rw,relatime,attr2,inode64,noquota', maxfile=255, maxpath=4096), sdiskpart(device='/dev/sda1', mountpoint='/boot', fstype='xfs', opts='rw,relatime,attr2,inode64,noquota', maxfile=255, maxpath=4096)]

#disk_usage(path)：以命名元组的形式返回path所在磁盘的使用情况，包括磁盘的容量、已经使用的磁盘容量、磁盘的空间利用率等。
&gt;&gt;&gt; psutil.disk_usage('/')
sdiskusage(total=18238930944, used=10811842560, free=7427088384, percent=59.3)
&gt;&gt;&gt; psutil.disk_usage('/boot')
sdiskusage(total=1063256064, used=157560832, free=905695232, percent=14.8)
&gt;&gt;&gt; psutil.disk_usage('/').percent
59.3
&gt;&gt;&gt; psutil.disk_usage('/boot').percent
14.8

```

#### 3.4 获取网络信息

psutil可以获取<mark>网络接口和网络连接信息</mark>

```
&gt;&gt;&gt; psutil.net_
psutil.net_connections(  psutil.net_if_stats(     
psutil.net_if_addrs(     psutil.net_io_counters(  

```

```
&gt;&gt;&gt; psutil.net_connections()
[sconn(fd=3, family=&lt;AddressFamily.AF_INET: 2&gt;, type=&lt;SocketKind.SOCK_STREAM: 1&gt;, laddr=addr(ip='192.168.72.129', port=22), raddr=addr(ip='192.168.72.1', port=59959), status='ESTABLISHED', pid=117509), sconn(fd=41, family=&lt;AddressFamily.AF_INET6: 10&gt;, type=&lt;SocketKind.SOCK_STREAM: 1&gt;, laddr=addr(ip='::', port=3306), raddr=(), status='LISTEN', pid=1053), sconn(fd=14, family=&lt;AddressFamily.AF_INET6: 10&gt;, type=&lt;SocketKind.SOCK_STREAM: 1&gt;, laddr=addr(ip='::1', port=25), raddr=(), status='LISTEN', pid=1107), sconn(fd=5, family=&lt;AddressFamily.AF_INET: 2&gt;, type=&lt;SocketKind.SOCK_DGRAM: 2&gt;, laddr=addr(ip='127.0.0.1', port=323), raddr=(), status='NONE', pid=699), sconn(fd=13, family=&lt;AddressFamily.AF_INET: 2&gt;, type=&lt;SocketKind.SOCK_STREAM: 1&gt;, laddr=addr(ip='127.0.0.1', port=25), raddr=(), status='LISTEN', pid=1107), sconn(fd=6, family=&lt;AddressFamily.AF_INET6: 10&gt;, type=&lt;SocketKind.SOCK_DGRAM: 2&gt;, laddr=addr(ip='::1', port=323), raddr=(), status='NONE', pid=699), sconn(fd=3, family=&lt;AddressFamily.AF_INET: 2&gt;, type=&lt;SocketKind.SOCK_STREAM: 1&gt;, laddr=addr(ip='0.0.0.0', port=22), raddr=(), status='LISTEN', pid=674), sconn(fd=3, family=&lt;AddressFamily.AF_INET: 2&gt;, type=&lt;SocketKind.SOCK_STREAM: 1&gt;, laddr=addr(ip='192.168.72.129', port=22), raddr=addr(ip='192.168.72.1', port=50421), status='ESTABLISHED', pid=122369), sconn(fd=3, family=&lt;AddressFamily.AF_INET: 2&gt;, type=&lt;SocketKind.SOCK_STREAM: 1&gt;, laddr=addr(ip='192.168.72.129', port=22), raddr=addr(ip='192.168.72.1', port=50793), status='ESTABLISHED', pid=122934), sconn(fd=4, family=&lt;AddressFamily.AF_INET6: 10&gt;, type=&lt;SocketKind.SOCK_STREAM: 1&gt;, laddr=addr(ip='::', port=22), raddr=(), status='LISTEN', pid=674)]

[root@wh ~]# netstat -anplut
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      674/sshd            
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      1107/master         
tcp        0      0 192.168.72.129:22       192.168.72.1:50793      ESTABLISHED 122934/sshd: root@p 
tcp        0      0 192.168.72.129:22       192.168.72.1:59959      ESTABLISHED 117509/sshd: root@p 
tcp        0      0 192.168.72.129:22       192.168.72.1:50421      ESTABLISHED 122369/sshd: root@p 
tcp6       0      0 :::3306                 :::*                    LISTEN      1053/mysqld         
tcp6       0      0 :::22                   :::*                    LISTEN      674/sshd            
tcp6       0      0 ::1:25                  :::*                    LISTEN      1107/master         
udp        0      0 127.0.0.1:323           0.0.0.0:*                           699/chronyd         
udp6       0      0 ::1:323                 :::*                                699/chronyd  

```

```
# 查看网卡配置信息，以字典的形式返回网卡的配置信息，包括IP地址和mac地址、子网掩码和广播地址。
&gt;&gt;&gt; psutil.net_if_addrs()
{<!-- -->'lo': [snicaddr(family=&lt;AddressFamily.AF_INET: 2&gt;, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None), snicaddr(family=&lt;AddressFamily.AF_INET6: 10&gt;, address='::1', netmask='ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', broadcast=None, ptp=None), snicaddr(family=&lt;AddressFamily.AF_PACKET: 17&gt;, address='00:00:00:00:00:00', netmask=None, broadcast=None, ptp=None)], 'ens33': [snicaddr(family=&lt;AddressFamily.AF_INET: 2&gt;, address='192.168.72.129', netmask='255.255.255.0', broadcast='192.168.72.255', ptp=None), snicaddr(family=&lt;AddressFamily.AF_INET6: 10&gt;, address='fe80::20c:29ff:fef7:d944%ens33', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None), snicaddr(family=&lt;AddressFamily.AF_PACKET: 17&gt;, address='00:0c:29:f7:d9:44', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)]}

&gt;&gt;&gt; psutil.net_if_addrs()['ens33'][0].address
'192.168.72.129'

[root@wh ~]# ip add
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:f7:d9:44 brd ff:ff:ff:ff:ff:ff
    inet 192.168.72.129/24 brd 192.168.72.255 scope global ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::20c:29ff:fef7:d944/64 scope link 
       valid_lft forever preferred_lft forever

```

```
#返回网卡的详细信息，包括是否启动、通信类型、传输速度与mtu。
&gt;&gt;&gt; psutil.net_if_stats()
{<!-- -->'lo': snicstats(isup=True, duplex=&lt;NicDuplex.NIC_DUPLEX_UNKNOWN: 0&gt;, speed=0, mtu=65536), 'ens33': snicstats(isup=True, duplex=&lt;NicDuplex.NIC_DUPLEX_FULL: 2&gt;, speed=1000, mtu=1500)}

```

```
#以命名元组的形式返回当前系统中每块网卡的网络io统计信息，包括收发字节数，收发包的数量、出错的情况和删包情况。当pernic为True时，则列出所有网卡的统计信息。
&gt;&gt;&gt; psutil.net_io_counters()
snetio(bytes_sent=18304876, bytes_recv=72909709, packets_sent=196237, packets_recv=175782, errin=0, errout=0, dropin=0, dropout=0)
&gt;&gt;&gt; psutil.net_io_counters(pernic=True)
{<!-- -->'lo': snetio(bytes_sent=2508888, bytes_recv=2508888, packets_sent=28366, packets_recv=28366, errin=0, errout=0, dropin=0, dropout=0), 'ens33': snetio(bytes_sent=15799288, bytes_recv=70404039, packets_sent=167913, packets_recv=147458, errin=0, errout=0, dropin=0, dropout=0)}



```

练习：监控磁盘/ /boot分区的使用率

```
[root@wh 507]# cat monitor.py
#!/usr/bin/python3
import psutil,datetime

root_num=psutil.disk_usage('/').percent
boot_num=psutil.disk_usage('/boot').percent
ctime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
if root_num&gt;60:
    print(f"root partition is not enough   usage:{root_num}%")
    with open("/var/log/root_boot_partition.txt",'a+',encoding='utf-8') as fp:
        fp.write(f"{ctime} / used {root_num}%")
else:
    print(f"root partition is enough   usage:{root_num}%")

if boot_num&gt;50:
    print(f"boot partition is not enough   usage:{boot_num}%")
    with open("/var/log/root_boot_partition.txt",'a+',encoding='utf-8') as fp:
        fp.write(f"{ctime} /boot used {boot_num}%\n")
else:
    print(f"boot partition is enough   usage:{boot_num}%")

[root@wh 507]# python3 monitor.py
root partition is enough   usage:59.3%
boot partition is enough   usage:14.8%

```

#### 使用psutil模块监控系统磁盘，cpu，内存的使用率以及网络情况

```
[root@wh python-test]# cat monitor.py 
import psutil
import datetime
import time
def disk_usage():
    root_num=psutil.disk_usage('/').percent
    boot_num=psutil.disk_usage('/boot').percent
    ctime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if root_num&gt;60:
        print(f"root partition is not enough   usage:{root_num}%")
        with open("/var/log/root_boot_partition.txt",'a+',encoding='utf-8') as fp:
            fp.write(f"{ctime} / used {root_num}%")
    else:
        print(f"root partition is enough   usage:{root_num}%")
    if boot_num&gt;50:
        print(f"boot partition is not enough   usage:{boot_num}%")
        with open("/var/log/root_boot_partition.txt",'a+',encoding='utf-8') as fp:
            fp.write(f"{ctime} /boot used {boot_num}%\n")
    else:
        print(f"boot partition is enough   usage:{boot_num}%")
disk_usage()

def cpu_percent():
    cpu_per = psutil.cpu_percent()
    if cpu_per &gt; 50:
        print(f"cpu使用率：{cpu_per}%,已超过50%")
        with open("/var/log/cpu_percent.txt",'a+',encoding='utf-8') as fp:
            fp.write(f"cpu used {cpu_per}%\n")
    else:
        print(f"cpu used: {cpu_per}%")
cpu_percent()

def memory_percent():
    memory_per = psutil.virtual_memory().percent
    if memory_per &gt; 50:
        print(f"内存使用率：{memory_per}%,已超过50%")
        with open("/var/log/memory_percent.txt",'a+',encoding='utf-8') as fp:
            fp.write(f"memory used {memory_per}%\n")
    else:
        print(f"memory used：{memory_per}%")
memory_percent()

def get_net_speed(interval):
	net_msg = psutil.net_io_counters()
	bytes_sent, bytes_recv = net_msg.bytes_sent, net_msg.bytes_recv
	time.sleep(interval)
	net_msg = psutil.net_io_counters()
	bytes_sent2, bytes_recv2 = net_msg.bytes_sent, net_msg.bytes_recv
	sent_speed = (bytes_sent2 - bytes_sent) / interval
	sent_speed = str(round((sent_speed / 1048576), 2)) + " MB/s" if sent_speed &gt;= 1048576 else str(
		round((sent_speed / 1024), 2)) + " KB/s"
	recv_speed = (bytes_recv2 - bytes_recv) / interval
	recv_speed = str(round((recv_speed / 1048576), 2)) + " MB/s" if recv_speed &gt;= 1048576 else str(
		round(recv_speed / 1024, 2)) + " KB/s"

	return sent_speed, recv_speed
	
sent_speed, recv_speed = get_net_speed(3)
print(f"网络实时IO（3s内）\n上传速度:{sent_speed}\n下载速度:{recv_speed}")
net = psutil.net_io_counters()
sent_bytes = net.bytes_recv / 1024 / 1024
recv_bytes = net.bytes_sent / 1024 / 1024

sent_bytes = str(round(sent_bytes, 2)) + "MB" if sent_bytes &lt; 1024 else str(round(sent_bytes / 1024, 2)) + "GB"
recv_bytes = str(round(recv_bytes, 2)) + "MB" if recv_bytes &lt; 1024 else str(round(recv_bytes / 1024, 2)) + "GB"

print(f"网卡总接收流量{recv_bytes}\n总发送流量{sent_bytes}")


```
