
--- 
title:  zabbix4.0 Web页面配置 - 聚合图形的实现 
tags: []
categories: [] 

---
**目录**





















### 1、主机组Host groups配置

>  
 **什么是主机组？** 
 ** **主机的逻辑组；可能包含主机和模板。一个主机组里的主机和模板之间并没有任何直接的关联。通常在给不同用户组的主机分配权限时候使用主机组。****   


#### 创建主机组

#### <img alt="" height="253" src="https://img-blog.csdnimg.cn/395ba63cbf6e47e8a0a8d1dd45403abd.png" width="1200"> 将一个主机添加至刚才创建的主机里面

<img alt="" height="431" src="https://img-blog.csdnimg.cn/e7fd553d467f4c4680edf14cf4b0f99c.png" width="935">

>  
 ** 可以看到，新添加的主机显示在Wordpress主机组里面** 


<img alt="" height="131" src="https://img-blog.csdnimg.cn/925e789b14694314b82ef87210d937b1.png" width="853">

**########################################################################## **

###  2、用户参数UserParameter设置

>  
 **用户定义参数可以用来帮助用户实现通过Zabbix agent执行非Zabbix原生的 agent check。** 
 **你可以编写一个命令来检索所需的数据，并将其包含在用户自定义参数中 ('UserParameter' 参数配置)。** 
 **一条用户自定义参数配置应当使用以下语法：** 


```
UserParameter=&lt;key&gt;,&lt;command&gt;
```

```
语法：
UserParameter=&lt;key&gt;,&lt;command&gt;
```

#### 示例： 添加一个参数：show.host.messages

<img alt="" height="328" src="https://img-blog.csdnimg.cn/8bef7ea27bd74618b6eaacdce66473e5.png" width="836">

>  
 **更改配置文件以后重启zabbix-agent 服务，然后再zabbix-server服务器上使用zabbix_get 获取这个参数的值** 


```
[root@zabbix-agent zabbix]# service zabbix-agent restart
Redirecting to /bin/systemctl restart zabbix-agent.service

```

```
[root@zabbix-server ~]# /usr/bin/zabbix_get  -s 192.168.20.11 -p 10050 -k "show.host.messages"
this is host 192.168.20.11

```

**########################################################################## ** 

####  模拟zabbix模板里面的参数再添加一个userparameter

<img alt="" height="67" src="https://img-blog.csdnimg.cn/53f6eb320b8941d0a29fb928f1aa6b65.png" width="706">

 <img alt="" height="42" src="https://img-blog.csdnimg.cn/de37439e2ed64739894e9eef45b82703.png" width="342">

 <img alt="" height="403" src="https://img-blog.csdnimg.cn/a9c88df068384f299e8e40f80b0ca2a4.png" width="1017">

 脚本：

<img alt="" height="215" src="https://img-blog.csdnimg.cn/fc5866fb04904106b444cca33e5077a6.png" width="554">

>  
 ** 给与可执行权限** 


```
[root@zabbix-agent tmp]# chmod +x get_messages.sh 
[root@zabbix-agent tmp]# ll
总用量 8
-rwxr-xr-x. 1 root root 118 2月  25 10:27 get_messages.sh
-rwx------. 1 root root 836 2月  23 09:03 ks-script-J20yaP
drwx------. 3 root root  17 2月  24 14:24 systemd-private-39ebc6e16749408bbee2a6246245a24e-chronyd.service-cwMIWA
drwx------. 2 root root   6 2月  24 14:19 vmware-root_708-2998936538
drwx------. 2 root root   6 2月  23 09:03 vmware-root_738-2999591909
-rw-------. 1 root root   0 2月  23 09:01 yum.log
[root@zabbix-agent tmp]# 

```

>  
 ** 重启zabbix-agent服务，然后再zabbix-server上执行zabbix_get** 


```
[root@zabbix-agent tmp]# service zabbix-agent restart
Redirecting to /bin/systemctl restart zabbix-agent.service

```

<img alt="" height="215" src="https://img-blog.csdnimg.cn/bec482b8c9364963aafdb4b1ef026a0f.png" width="1184">

**########################################################################## ** 

### 3、触发器设置

监控项表达式的格式：

```
{&lt;server&gt;:&lt;key&gt;.&lt;function&gt;(&lt;parameter&gt;)}&lt;operator&gt;&lt;constant&gt;
```

当你不知道某个监控项的key怎么写的时候，可以参考模板里的key是怎么写的

>  
  <img alt="" height="1160" src="https://img-blog.csdnimg.cn/c7b1f417fe504fadadfa1386bdda244c.png" width="1185"> 


**########################################################################## ** 

####  示例：

 

>  
 **来自192.168.20.11主机可用内村小于20M的时候进入PROBLEM状态** 


```
{192.168.20.11:vm.memory.size[available].last()}&lt;20M
```

>  
 **来自www.zabbix.com主机最后一个负载值大于5的时候进入PROBLEM状态** 


```
{www.zabbix.com:system.cpu.load[all,avg1].last()}&gt;5
```

>  
 **在5分钟内CPU iowait平均负载大于20的时候进入PROBLEM状态** 


```
{www.zabbix.com:system.cpu.util[,iowail].avg(5m)}&gt;20
```

**当网卡"ens33"在5分钟内接受的字节大于100kb的时候进入PROBLEM状态**

```
{www.zabbix.com:net.if.in[ens33,bytes].min(5m)}&gt;100k
```

>  
 **在30分钟内超过5次ping不可达的时候进入PROBLEM状态** 


```
{www.babbix.com:icmpping.count[30m,0]}&gt;5
```

**########################################################################## ** 

### 4、Screens聚合图形设置

>  
 **可以通过创建聚合图形，将想看的图形都放在同一个页面** 


<img alt="" height="446" src="https://img-blog.csdnimg.cn/9c4ff12e7a424eba8940afeaeff50a59.png" width="1200">

<img alt="" height="433" src="https://img-blog.csdnimg.cn/6237dbea8da14362b11903cdc0d03b7e.png" width="889">

 <img alt="" height="581" src="https://img-blog.csdnimg.cn/01eec17e1e1b4785aa1709654d5f0d41.png" width="1006">

 <img alt="" height="483" src="https://img-blog.csdnimg.cn/746f66ad5fe346cf88276ee7c25d67b9.png" width="1200">

按照自己的需求，添加需要聚合的图形

<img alt="" height="1053" src="https://img-blog.csdnimg.cn/bc0775ddde1241ab982171f8b2aa2610.png" width="1200"> 

 还可以选择不同的主机组的图形来聚合到一起

<img alt="" height="900" src="https://img-blog.csdnimg.cn/daa1fd1fc5b4456f9c929666c2284c8f.png" width="1067">

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/3bf25c7c65e3486fb8e0b4c780ffe581.png" width="1200">

添加完了以后，可以看到Screens里面已经有了刚才 设置的聚合图形test-screens了。

<img alt="" height="423" src="https://img-blog.csdnimg.cn/d653bf252c3842ac8ec038ff30a1d4d1.png" width="1188">

 点击test-screens查看聚合图形

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/88344f7398c04c8d8fe2e6c70d0f1731.png" width="1200">

 
