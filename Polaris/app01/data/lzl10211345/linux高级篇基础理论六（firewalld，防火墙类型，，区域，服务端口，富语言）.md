
--- 
title:  linux高级篇基础理论六（firewalld，防火墙类型，，区域，服务端口，富语言） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**不能因为人生的道路坎坷,就使自己的身躯变得弯曲;不能因为生活的历程漫长,就使求索的 脚步迟缓。** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 ♥️**感谢CSDN让你我相遇！** 


运维人员辛苦和汗水总结的干货理论希望对你有所帮助

<img alt="" height="80" src="https://img-blog.csdnimg.cn/fd3fee85df1d4cffba97164ba01cdf81.gif" width="640">

**目录**































### 防火墙基础概念与底层

#### 1、防火墙的技术上分类

包过滤：firewalld属于这种 应用代理：360，金山毒霸，鲁大师 状态检测：ASA

#### 2、firewalld的两种配置模式：

运行时配置：    立即生效 永久配置：    重新加载服务生效

#### 3、常用的区域：

trusted：    信任区域，用于连接内部网络 public:    公共区域，是默认区域 internal：内部区域，用于连接内部网络 external：外部区域，用于连接互联网，次区域有地址位置nat功能 dmz:    非军事化区域，用于连接内部服务器

#### 4、防火墙的配置方法：

firewall-config图形工具 firewall-cmd命令行工具（常用） /etc/firewalld/中的配置文件

#### 5、firewalld-cmd命令工具相关选项：

--reload：重新加载防火墙规则 --permanent：用于设置永久性规则，需要重新加载防火墙才会生效 --runtime-to-permanent：将运行时的配置进行保存

#### 6、开启路由转发

vim         /etc/sysctl.conf net.ipv4.ip_forward = 1

### firewlld支持两种类型的网络地址转换

（1）IP地址伪装（masquerade）解决了内部访问互联网的问题 可以实现局域网多个地址共享单一公网地址上网 IP地址伪装仅支持IPV4，不支持IPV6 （2）端口转发（firewalld-port）：解决了内部服务器发布到互联网的问题，端口转发，指定IP地址及端口的流量将被转发到相同计算机上的不同端口，或者转发到不同计算机的端口

#### ip地址伪装工作原理

>  
 地址伪装(masquerade)：通过地址伪装，NAT设备将经过设备的包转发到指定接收方，同时将通过的数据包的源地址更改为其自己的接口地址。当返回的数据包到达时，会将目的地址修改为原始主机的地址并做路由。地址伪装可以实现局域网多个地址共享单一公网地址上网。类似于NAT技术中的端口多路复用(PAT)。P地址伪装仅支持Pv4,不支持Pv6。 


#### 端口转发原理

>  
 端口转发(Forward-port)：也称为目的地址转换或端口映射。通过端口转发，将指定P地址及 端口的流量转发到相同计算机上的不同端口，或不同计算机上的端口。企业内网的服务器一般都采用私网地址，可以通过端口转发将使用私网地址的服务器发布到公网，以便让互联网用户访问。例如，当接收互联网用户的HTTP请求时，网关服务器判断数据包的目标地址与目标端口，一旦匹配指定规则，则将其目标地址修改为内网真正的服务器地址，从而建立有效连接。 


### 常见服务端口：

http (apache):    tcp    80

https：tcp    443

mysq：tcp    3306

squid:  tcp    3128

rsync：tcp    873

ssh：tcp        22

ftp：tcp        21和20

telnet:  tcp    23

DNS:    tcp/udp  53

DHCP:  udp   67

### 防火墙补充命令

1.重新加载防火墙配置： firewall-cmd  --reload

2.防火墙操作例子： 移除tcp12345端口： firewall-cmd --zone=external --add-port=12345/tcp --permanent

3.配置external区域移除ssh服务： firewall-cmd --zone=external --remove-service=ssh --permanent

4.设置默认区域为external： firewall-cmd --set-default-zone=external

5.因为预定义的SSH服务已经更改默认端口，所以将预定义SSH服务移除： firewall-cmd --zone=dmz --remove-service=ssh --permanent

6.禁止ping： firewall-cmd --add-icmp-block=echo-request --zone=dmz --permanent                

### firewalld富语言

富语言是与直接语言对比的差距就是可以更加丰富的来表示条件，更详细来描述规则，富规则可用于表达基本的允许/拒绝规则，也可以用于配置记录（面向syslog和auditd),以及端口转发、伪装和速率限制。下面是表达富规则的基本语法：

<img alt="" height="234" src="https://img-blog.csdnimg.cn/8b839bebbd8247638903ad6f1e61bf0a.png" width="889">

规则的每个单一元素都能够以option=value的形式来采用附加参数。

##### 理解富规则命令

firewal-cmd有四个选项可以用于处理富规则，所有这些选项都可以同常规的--permanent或 --zone=&lt;ZONE&gt;选项组合使用：

--add-rich-rule='RULE' 向指定区域中添加RULE,如果没有指定区域，则为默认区域 --remove-rich-rule='RULE' 从指定区域中删除RULE,如果没有指定区域，则为默认区域 --query-rich-rule='RULE' 查询RULE是否已添加到指定区域，如果未指定区域，则为默认区域。规则 存在，则返回0，否则返回1 --list-rich-rules 输出指定区域的所有富规则，如果未指定区域，则为默认区域

>  
 人生要尽全力度过每一关,不管遇到什么困难不可轻言放弃！！！ 

