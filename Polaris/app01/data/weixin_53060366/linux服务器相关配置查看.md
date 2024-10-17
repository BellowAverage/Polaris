
--- 
title:  linux服务器相关配置查看 
tags: []
categories: [] 

---
## linux服务器相关配置查看

### 1、查看GPU信息和使用情况

>  
 #Linux查看显卡信息： 
 lspci是一个用来查看系统中所有PCI总线以及连接到该总线上的设备的工具。 
 `lspci | grep -i vga` 


>  
 #在CentOS使得lspci查看硬件信息。使用时，提示bash: lspci: command not found，大多使用/sbin/lspci即可，我发现我的系统中/sbin下也没有。使用yum install lspci显示没有这个包。 


>  
 查看指定显卡的详细信息用以下指令： 
 `lspci -v -s 00:0f.0` 
 查看nvidia显卡信息： 
 lspci | grep -i nvidia 
 Nvidia自带一个命令行工具可以查看显存的使用情况： 
 <pre><code class="prism language-shell">nvidia-smi
</code></pre> 


### 2、查看Linux服务器硬件信息

查看操作系统信息：

>  
 cat /etc/-release 


操作系统详细发行信息：

```
lsb_release -a
1

```

CPU信息：

```
lscpu
1

```

CPU 具体型号

```
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
1

```

CPU 个数：

```
cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l
1

```

CPU 每个里面的具体内核数量：

```
cat /proc/cpuinfo| grep "cpu cores"| uniq
1

```

CPU 逻辑个数：

```
cat /proc/cpuinfo| grep "processor"| wc -l
1

```

内核版本信息：

```
uname -r 或 uname -a

```

磁盘空间大小：

```
df -hT

```

内存大小：

```
free -mh
1
#内存使用的百分比
free -m | sed -n '2p' | awk '{print "used mem is "$3"M,total mem is "$2"M,used percent is "$3/$2*100"%"}'

```

内存硬件信息：

```
dmidecode -t memory
1

```

内存详细使用情况：

```
cat /proc/meminfo
1

```

进程：

```
#进程
ps -ef                 # 查看所有进程
top                    # 实时显示进程状态
lsof-d pid     #查看进程打开的文件句柄数
#查看端口占用情况：
netstat、ss、lsof

```

硬盘分区详情：

```
fdisk -l
1

```

分区挂载情况：

```
lsblk
mount

```

网卡信息：

```
lspci | grep -i 'eth'
1

```

显卡信息：

```
lspci | grep -i vga

```
