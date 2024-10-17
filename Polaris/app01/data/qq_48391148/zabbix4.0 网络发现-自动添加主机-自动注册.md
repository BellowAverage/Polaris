
--- 
title:  zabbix4.0 网络发现-自动添加主机-自动注册 
tags: []
categories: [] 

---
>  
 **zabbix的网络发现** 
 **网络发现的好处：** 
 **        加快zabbix部署** 
 **        简化管理** 
 **        无需过多管理就能在快速变化的环境中使用zabbix** 


>  
 **zabbix网络发现给予以下信息** 
 **        IP范围** 
 **        可用的外部服务（FTP，SSH，WEB，POP3，IMAP，TCP等）** 
 **        来自zabbix agent的信息** 
 **        来自snmp agent的信息** 


**网络发现过程： **

<img alt="" height="119" src="https://img-blog.csdnimg.cn/fc1381cb8b1a4f38bab21278c98e3bea.png" width="811">

>  
 ** 实验环境：** 
 **准备两台未安装zabbix-agent 的centos7服务器** 


```
192.168.20.12
192.168.20.13
```

>  
 **在zabbix-server服务器上面安装ansible** 


```
yum install ansible -y
```

>  
 ** 准备安装zabbix-agent的yaml文件** 


```
[root@zabbix-server ~]# cat zabbix_agent.yml 
---
- hosts: webserver
  vars:
  - zabbix_server: 192.168.20.10
  tasks:
    - name: Install zabbix agent - CentOS6
      yum: name=http://repo.zabbix.com/zabbix/4.0/rhel/6/x86_64/zabbix-agent-4.0.0-2.el6.x86_64.rpm state=present
      when: ansible_distribution == "CentOS" and ansible_distribution_major_version == "6"
    - name: Install zabbix agent - CentOS7
      yum: name=http://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-agent-4.0.0-2.el7.x86_64.rpm state=present
      when: ansible_distribution == "CentOS" and ansible_distribution_major_version == "7"

    - name: Copy zabbix agent configuration file
      template: src=zabbix_agentd.conf.j2 dest=/etc/zabbix/zabbix_agentd.conf

    - name: Start zabbix agent
      service: name=zabbix-agent state=started enabled=true

```

>  
 **准备zabbix-agent的配置文件** 


```
[root@zabbix-server ~]# cat zabbix_agentd.conf.j2 
PidFile=/var/run/zabbix/zabbix_agentd.pid
LogFile=/var/log/zabbix/zabbix_agentd.log
DebugLevel=3
Server={<!-- -->{ zabbix_server }}
ListenPort=10050
ListenIP={<!-- -->{ ansible_default_ipv4.address }}
ServerActive={<!-- -->{ zabbix_server }}
Hostname={<!-- -->{ ansible_default_ipv4.address }} 
Include=/etc/zabbix/zabbix_agentd.d/*.conf
UserParameter=tcp.status[*],ss -antp |awk '{a[$$1]++}END{print a["'$1'"]}'
```

>  
 **执行ansible 剧本** 


<img alt="" height="604" src="https://img-blog.csdnimg.cn/ecf19f1dae20449e8f6bf316c685ce8c.png" width="1200">

** 配置网络自动发现**

<img alt="" height="599" src="https://img-blog.csdnimg.cn/0abd5f2d998c48b58a967ffc8a31fb7e.png" width="1200">

 <img alt="" height="435" src="https://img-blog.csdnimg.cn/bc736563632a42c48ad1d700a930ddb0.png" width="1200">

>  
 **进入监控-自动发现，可以看到已经自动发现了对应ip地址段内的三台机器 ** 


<img alt="" height="574" src="https://img-blog.csdnimg.cn/5eaf917ac0fd471399dfb78c6c6b7be5.png" width="1200">

>  
 **配置自动发现动作** 


<img alt="" height="399" src="https://img-blog.csdnimg.cn/ca4723dd3ae9485e96438a6e168c50b6.png" width="1200">

<img alt="" height="589" src="https://img-blog.csdnimg.cn/67a7fdfad8094e1f9054098970a309ed.png" width="989"> 

<img alt="" height="574" src="https://img-blog.csdnimg.cn/a0772a1afabc4bcd9e2f1f4c886da074.png" width="1200"> 

>  
 ** 配置好自动发现动作以后，过几分钟zabbix就会自动将发现的主机执行对应的操作，如图，主机自动添加成功。** 


<img alt="" height="554" src="https://img-blog.csdnimg.cn/d62a3edeed35461889b44a238f39f966.png" width="1200">

 

 

 
