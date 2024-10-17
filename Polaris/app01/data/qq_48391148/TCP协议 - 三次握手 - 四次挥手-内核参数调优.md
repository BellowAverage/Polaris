
--- 
title:  TCP协议 - 三次握手 - 四次挥手-内核参数调优 
tags: []
categories: [] 

---
## 一、什么是TCP协议？

>  
 **TCP协议：传输控制协议（TCP，Transmission Control Protocol）是一种面向连接的、可靠的、基于字节流的传输层通信协议。** 


>  
 **tcp协议和udp协议一样，都是位于传输层的协议** 


**什么是网络通信四元组？**

>  
 **        源ip，目的ip，源端口，目的端口** 


**什么是网络通信五元组？**

>  
 **        源ip，目的ip，源端口，目的端口，协议** 


**################################################**

## 二、TCP报文头部信息

TCP报文头部信息组成：

TCP 头部由两部分组成：头部（20字节） + 选项（60字节）

<img alt="" src="https://img-blog.csdnimg.cn/03e3303e944643b4a4ab6c8e6dfd6d68.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAV2FuZ3NoQA==,size_20,color_FFFFFF,t_70,g_se,x_16">

>  
 **16位的源端口号** 
 **        16位源端口号，占2个字节** 
 **        一台机器上面可以开启的最大端口数为65535** 
 **        为什么？** 
 **        2 ^ 16 = 65535** 
 **        所以端口范围一般为 0-65535** 


>  
 **16位的目标端口号** 
 **        16位的目标端口号，占2个字节** 


>  
 **32位的序列号（Sequence Number）** 
 **        32位的序列号，占4个字节** 
 **        序列号和确认号是tcp协议实现可靠传输服务的关键所在，tcp协议是基于字节流的协议，当报文被分为多个报文段时，序列号就是该报文段首字节在整个报文的偏移量，每发送一次数据，每增加一次，就会增加一次该数据字节的大小，并且序列号不会从0开始，而是随机生成一个数，由SYN包传给接收端主机，这是为了安全性考虑，随机生成让黑客不会那么容易地猜到序列号，从而伪造一些确认序列号对服务器发起攻击。** 
 **        假设主机A和主机B进行通信，那么在主机A发送给B的第一个TCP报文段中，此时系统会随机生成一个随机值ISN（Initial Sequence Number ， 初始序号值），那么在A - B传输方向上面，后续的TCP报文段里面序号值就是ISN加上该报文段所携带的数据在整个字节流中的偏移量，例如：某个TCP报文段里面传送的数据是整个字节流中的1025~2048字节，那么该报文段的序号值就是ISN + 1025，B - A传输方向上面的序号值也是如此。** 
 **        序列号回绕** 
 **                尽管序列号是由32位保存的，但是也是会有尽头的，到达尽头后，序列号又会从0开始使用，所以这个时候接收方怎么判断出哪个是之前的报文段，哪个又是之后的报文段呢？其实我们可以在tcp头部里面的选项里面加入timestamp时间戳，如果出现之前的请求突然断了，B没有收到，A又会发送新的序列号，B会查看时间戳，如果新的序列号时间戳比之前收到的序列号新，就会丢弃。** 


>  
 **32位的确认号（Acknowledge Number）** 
 **        32位确认号，占4个字节** 
 **        确认号是用来表示接收方B期待收到的下一个报文段的第一个字节，并且告诉主机A之前发送的报文包已经收到，因此，确认号应该是上次收到的数据字节序列号加1，收到确认号的主机A就知道之前的报文已经收到，确认号只有ACK标志位1时候才生效。** 


>  
 **4位的首部长度和保留的6位** 
 **        4位首部长度：首部长度也叫数据偏移量，因为首部长度实际上指示了数据区在报文段中的起始偏移值** 


**6个标志位：**  **URG、 ACK、PSH 、 RST 、 SYN、 FIN**

>  
 **URG：表示紧急指针（urgent pointer）是否有效。** 


>  
 **ACk：表示确认号是否有效。我们称携带ACK标识的TCP报文段为确认报文段。** 


>  
 **PSH：** 
 **提示接收端应用程序应该立即从TCP接收缓冲区中读走数据，为接收后续数据腾出空间（如果应用程序不将接收** 
 **        到的数据读走，它们就会一直停留在TCP接收缓冲区中）。** 


>  
 **RST：** 
 **        表示要求对方重新建立连接。我们称携带RST标志的TCP报文段为复位报文段。** 


>  
 **SYN：** 
 **        表示请求建立一个连接。我们称携带SYN标志的TCP报文段为同步报文段。** 


>  
 **FIN：** 
 **        表示通知对方本端要关闭连接了。我们称携带FIN标志的TCP报文段为结束报文段** 


>  
 **16位窗口大小（Window Size）** 


>  
 **16位效验和（TCP Check Sum）** 


>  
 **16位紧急指针（Urgent Point）** 


>  
 **选项** 
 **        tcp头部的最后一个选项字段是可变长的，可选的，这部分最多包含40字节，因为TCP头部的最大长度是60字节（其中还包括前面20个字节的固定部分，也就是说TCP头部长度在20字节-60字节）** 
 **        选项里面的MSS（Maximum Segment Size），最大报文大小，它表示本段所能接受的最大报文段的长度，（不包含头部字段）选项长度不一定是32位的整数倍，所以要加填充为，即在这个字段中添加额外的0，来保证TCP头是整数倍** 
 **        因为传输层的MTU最大传输单元最大是1500，所以 1500 - ip包头（20字节） - tcp头（20字节） = 1460字节，所以因为有了MSS，tcp包一般来说在网络层是不需要分片的。** 
 **        ****选项 ： timestamp时间戳 - - 计算往返时间，确认数据包的先后顺序。** 


>  
 **数据部分** 
 **        TCP 报文段中的数据部分是可选的。在一个连接建立和一个连接终止时，双方交换的报文段仅有 TCP 首部。如果一方没有数据要发送，也使用没有任何数据的首部来确认收到的数据。在处理超时的许多情况中，也会发送不带任何数据的报文段。** 


** ##################################################**

## 三、 三次握手

**TCP连接建立**

<img alt="" height="538" src="https://img-blog.csdnimg.cn/4a30ac7606cf4a7fa5bdb3a6d3e10cc0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAV2FuZ3NoQA==,size_20,color_FFFFFF,t_70,g_se,x_16" width="1167">

>  
 **第一次握手：** 
 **在建立TCP连接时，客户机A向服务器B发出连接请求报文,其中同步位SYN=1，同时选择一个初始序号seq=x，这时候客户机A进入SYN-SENT（同步已发送）状态，** 


>  
 **第二次握手：** 
 **服务器B收到报文段后，如果同意建立连接，则向A发送确认，在确认报文段中应把SYN位和ACK为都置为1，确认号ack=x+1，同时也为自己选择一个初始序列号seq=y，这时服务器B处于SYN-RCVD（同步收到）状态，** 


>  
 **第三次握手：** 
 **客户机A收到B的确认以后，还要给B给出确认，确认报文ACK=1，确认号ack=y+1，自己的序号seq=x+1，这时TCP连接已经建立，A进入ESTABLISHED（已建立连接）状态，当B收到A的确认以后，也进入ESTABLISHED状态。** 


** ##################################################**

## 四、四次挥手

**TCP连接释放**

<img alt="" height="709" src="https://img-blog.csdnimg.cn/8926b0f13cfa4af0ab114a91dda717b7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAV2FuZ3NoQA==,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

>  
 **1.客户机A发送连接释放报文，并且停止发送数据，主动关闭TCP连接，A把连接释放报文段首部的终止控制位FIN=1其序号seq=u（等于前面已经传送过的数据的最后一个字节的序号加1），这时候A进入FIN-WAIT-1（终止等待1）状态，等待B的确认，注意，TCP规定，FIN报文段即时不携带数据，他也会消耗掉一个序号。** 


>  
 **2.服务器B收到连接释放报文，发出确认报文，确认号ack=u+1，这个报文段自己的序号是v，等于B前面已经传送过的数据的最后一个字节的序号加1，然后B就进入了CLOSED-WAIT（关闭等待）状态，TCP服务器进程这时候通知高层应用进程，客户机A到服务器B这个方向的连接就释放了，这时TCP连接处于半关闭（half-close）状态，即A已经没有数据要发送的了，但是B若发送数据，A仍然要接收，也就是说，从B到A这个方向的连接并没有关闭，这个状态可能会持续一段时间，** 


>  
 **3.A收到来自B的确认后，就进入FIN-WAIT-2（终止等待2）状态，等待B发出的连接释放报文段** 


>  
 **4.若B已经没有要向A发送的数据，其应用进程就通知TCP释放连接，这时B发出的连接释放报文段FIN=1，ACK=1，假定B的序号seq=w（在这半关闭状态B可能又发送一些数据），B还要重复上次已经发送过的确认号ack=u+1，这时B就进入LAST-ACK（等待确认）状态，等待A的确认** 


>  
 **5.A在收到B的连接释放报文段后，必须对此发出确认，在确认报文中把ACK=1，确认号ack=w+1，自己的序号是seq=u+1，然后进入TIME-WAIT（时间等待）状态，注意此时TCP连接还没有释放掉，必须经过时间等待计时器（TIME-WAIT timer）设置的时间2MSL后，A才能进入CLOSED状态** 


>  
 **6.服务器B收到了A发出的确认，就会进入CLOSED状态，同样B在撤销相应的传输控制块TCB后，就结束了这次的TCP连接，我们注意到，B结束TCP连接的时间比客户机A要早一点。** 




** ##################################################**

## 五、内核参数调优

>  
 **Linux系统里面存放内核参数的目录：/proc/sys/net/ipv4/** 


```
[root@network ipv4]# pwd
/proc/sys/net/ipv4
[root@network ipv4]# ls
cipso_cache_bucket_size            ip_forward_use_pmtu               tcp_fack                tcp_retries1
cipso_cache_enable                 ipfrag_high_thresh                tcp_fastopen            tcp_retries2
cipso_rbm_optfmt                   ipfrag_low_thresh                 tcp_fastopen_key        tcp_rfc1337
cipso_rbm_strictvalid              ipfrag_max_dist                   tcp_fin_timeout         tcp_rmem
conf                               ipfrag_secret_interval            tcp_frto                tcp_sack
fib_multipath_hash_policy          ipfrag_time                       tcp_invalid_ratelimit   tcp_slow_start_after_idle
fwmark_reflect                     ip_local_port_range               tcp_keepalive_intvl     tcp_stdurg
icmp_echo_ignore_all               ip_local_reserved_ports           tcp_keepalive_probes    tcp_synack_retries
icmp_echo_ignore_broadcasts        ip_nonlocal_bind                  tcp_keepalive_time      tcp_syncookies
icmp_errors_use_inbound_ifaddr     ip_no_pmtu_disc                   tcp_limit_output_bytes  tcp_syn_retries
icmp_ignore_bogus_error_responses  neigh                             tcp_low_latency         tcp_thin_dupack
icmp_msgs_burst                    ping_group_range                  tcp_max_orphans         tcp_thin_linear_timeouts
icmp_msgs_per_sec                  route                             tcp_max_ssthresh        tcp_timestamps
icmp_ratelimit                     tcp_abort_on_overflow             tcp_max_syn_backlog     tcp_tso_win_divisor
icmp_ratemask                      tcp_adv_win_scale                 tcp_max_tw_buckets      tcp_tw_recycle
igmp_max_memberships               tcp_allowed_congestion_control    tcp_mem                 tcp_tw_reuse
igmp_max_msf                       tcp_app_win                       tcp_min_snd_mss         tcp_window_scaling
igmp_qrv                           tcp_autocorking                   tcp_min_tso_segs        tcp_wmem
inet_peer_maxttl                   tcp_available_congestion_control  tcp_moderate_rcvbuf     tcp_workaround_signed_windows
inet_peer_minttl                   tcp_base_mss                      tcp_mtu_probing         udp_mem
inet_peer_threshold                tcp_challenge_ack_limit           tcp_no_metrics_save     udp_rmem_min
ip_default_ttl                     tcp_congestion_control            tcp_notsent_lowat       udp_wmem_min
ip_dynaddr                         tcp_dsack                         tcp_orphan_retries      xfrm4_gc_thresh
ip_early_demux                     tcp_early_retrans                 tcp_reordering
ip_forward                         tcp_ecn                           tcp_retrans_collapse

```

**示例：查看ack重传参数：**

```
[root@network ipv4]# cat tcp_synack_retries 
7
[root@network ipv4]# cat tcp_syn_retries 
6
[root@network ipv4]# 

```

**示例：查看半传输队列最大值**

```
[root@network ipv4]# cat tcp_max_syn_backlog
128
```

>  
 **永久修改参数可以在/etc/sysctl.conf文件里面添加指定的参数值** 


```
[root@network ipv4]# vim /etc/sysctl.conf 

# sysctl settings are defined through files in
# /usr/lib/sysctl.d/, /run/sysctl.d/, and /etc/sysctl.d/.
#
# Vendors settings live in /usr/lib/sysctl.d/.
# To override a whole file, create a new file with the same in
# /etc/sysctl.d/ and put new settings there. To override
# only specific settings, add a file with a lexically later
# name in /etc/sysctl.d/ and put new settings there.
#
# For more information, see sysctl.conf(5) and sysctl.d(5).
#
# ack重传次数  ：/proc/sys/net/ipv4/tcp_synack_retries  
net.ipv4.tcp_synack_retries=7

```

>  
 **然后使用 sysctl -p 命令让它生效（否则需要重启）** 


```
[root@network ipv4]# sysctl -p
net.ipv4.tcp_synack_retries = 7

```

**示例：查看当前内核参数**

```
[root@network ipv4]# sysctl -a

```


