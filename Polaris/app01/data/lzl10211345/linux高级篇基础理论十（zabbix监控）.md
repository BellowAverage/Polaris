
--- 
title:  linux高级篇基础理论十（zabbix监控） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**不能因为人生的道路坎坷,就使自己的身躯变得弯曲;不能因为生活的历程漫长,就使求索的 脚步迟缓。** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 ♥️**感谢CSDN让你我相遇！** 


**目录**

























### zabbix是什么？

Zabbix是一个基于Wb界面的企业级开源监控套件，提供分布式系统监控与网络监视功能。具 备主机的性能监控，网络设备性能监控，数据库性能监控，多种告警方式，详细报表、图表的绘制等功能。监测的对象可以是Linux或Vindows服务器，也可以是路由器、交换机等网络设备，通过SNMP(Simple Network Management Protocol,简单网络管理协议)、Zabbix Agent、PNG.端口监视等方法提供对远程网络服务器等监控、数据收集等功能，并提供通知机制使系统管理员可以快速定位、解决系统中存在的各种问题

### zabbix三种架构图

<img alt="" height="356" src="https://img-blog.csdnimg.cn/direct/b028d6e75c604a18b3f125ac1d14134c.png" width="705">

#### zabbix重要组件

zabbix主要由以下几个重要组件构成，具体作用如下。
- Zabbix Server：负责接收Agent发送报告信息的核心组件，所有的配置、数据统计、数据操作都由它组织进行。- Database storage：负责存储所有的配置信息以及收集的数据- Web interface:是zabbix的GU接口，通常情况下与Zabbix Server运行在同一台主机上- Pxory:属于可选组件，常用于分布式监控环境中，代理Server收集部分数据，然后转发Server，可以减轻Server的压力，- Aget:部署在被监控的主机（客户端）上，负责收集被监控端主机的数据，如CPU、内存<li>数据库等数据，然后发送到Server端或Proxy端。 
  <hr></li>
## 理论

#### 1、zabbix的具备功能

主机的性能监控、网络设备性能监控、数据库性能监控、多种告警方式、详细报表图表绘制

#### 2、zabbix的监测对象

linux服务器，window服务器，交换机，路由器等网络设备。

#### 3、zabbix的监控架构

server-client架构：适用于网络比较简单，设备比较少的监控环境。 master-node-client架构：适用于跨网络，跨机房，设备较多的环境 server-proxy-client架构：适用于跨网络，跨机房的中型网络环境。

#### 4、zabbix服务端口：

#### zabbix-server的端口：tcp   10051 zabbix-agent的端口：tcp    10050   5、测试命令：

cat      /dev/zero      &gt;      /dev/null     &amp; 查看CPU的动态进程信息：     top

#### 6、SNMP：简单网络管理协议

### zabbix安装引导

访问网页以后默认界面

<img alt="" height="571" src="https://img-blog.csdnimg.cn/direct/51397a6c1536447ba8dac3b3fa245bd8.png" width="834">

单击“Next step”按钮，进入系统环境检测界面，需要确保所有的软件都符合要求才能继 续，

<img alt="" height="381" src="https://img-blog.csdnimg.cn/direct/45fc9064783240eb95a7fd03877f6e47.png" width="629">

单击“Next step”按钮，进入数据库连接配置界面。根据之前创建好的zabbix数据库填写 授权信息

<img alt="" height="376" src="https://img-blog.csdnimg.cn/direct/67b746aaf85047eaa1d8b446aa3c891f.png" width="681">

数据库连接配置完成后，还需要填写连接Zbb×服务信息，如图11.5所示。

<img alt="" height="356" src="https://img-blog.csdnimg.cn/direct/877f0e6923c74cb3942604d27330c396.png" width="713">

返回一个汇总的配置信息

<img alt="" height="345" src="https://img-blog.csdnimg.cn/direct/0522613b0fa54b29aa0709ecd77c3eb6.png" width="727">

安装完成

<img alt="" height="353" src="https://img-blog.csdnimg.cn/direct/97b33d6a2b6149e58a33138b295eac9d.png" width="660">

在登录界面输入默认的用户名Admin,密码zabbix,即可登录到Zabbix服务器

<img alt="" height="338" src="https://img-blog.csdnimg.cn/direct/613e0e5150b84c2dbbca974075c0b19e.png" width="330">

到此就完成啦，zabbix的图形界面还是很好操作的。

<img alt="" height="1189" src="https://img-blog.csdnimg.cn/direct/ae606060516d4e45b929613af8f8ae54.png" width="1200">

人生要尽全力度过每一关,不管遇到什么困难不可轻言放弃！！！
