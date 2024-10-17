
--- 
title:  CentOS7 克隆机 网络重启失败 网络无法使用 
tags: []
categories: [] 

---
1.ifconfig 查看网络

发现 网卡变成 了ens-33

2、修改网卡名

 

### 克隆后的Centos7配置

执行`ifconfig`命令后会发现网卡名称是`ens33`,但是网络配置文件仍为`/etc/sysconfig/network-scripts/ifcfg-eno16777736` 。如果现在执行`systemctl restart network` 会出现`Job for network.service failed because the control process exited with error code.`
- 将原来的网络配置文件名`ifcfg-eno16777736`改为查询到的网卡名称(我的是ens33): `mv ifcfg-eno16777736 ifcfg-ens33`。- 修改ifcfg-ens33内容，将`DEVICE`和`NAME`的值都修改为`ens33`。**注意我这里没有设置mac地址**。修改ip地址为192.168.140.12。 <img src="https://img-blog.csdnimg.cn/img_convert/8d8ed9b735adf9532cf389e2e7b035e6.jpeg" alt="8d8ed9b735adf9532cf389e2e7b035e6.jpeg"> - 重新启动网络，`systemctl restart network`，发现启动成功。ping以下百度–成功。 <img src="https://img-blog.csdnimg.cn/img_convert/8d9d847ab9bacd9156f1478a92d0189f.jpeg" alt="8d9d847ab9bacd9156f1478a92d0189f.jpeg"> 
 
