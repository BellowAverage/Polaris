
--- 
title:  zabbix agent端 TIME_WAIT过多解决 
tags: []
categories: [] 

---
>  
 **最近查看zabbix agent端发现有很多 处于TIME_WAIT状态的tcp连接** 


<img alt="" height="1007" src="https://img-blog.csdnimg.cn/11af7a68a0a64a08abc4758609ff6389.png" width="900">

>  
 ** 目前zabbix采用的是被动模式，passive** 
 **即zabbix-server主动来向zabbix-agent来获取数据，** 


**被动模式工作流程 **

>  
 **工作流程：** 
 - **Zabbix-Server打开一个TCP连接。**- **Zabbix-Server发送一个key为agent.ping\n的请求。**- **Zabbix-Agent接受这个请求，然后响应数据＜HEADER&gt;＜DATALEN&gt;。**- **Zabbix-Server对接收到的数据进行处理。**- **Zabbix-Server对接收到的数据进行处理** 


**四次回收过程：**

<img alt="" height="450" src="https://img-blog.csdnimg.cn/bc30fe3f4e9845e5b1c532cdda8d0848.png" width="620">

>  
 **根据四次挥手，zabbix-server 收到 zabbix-agent发送的FIN报文以后，应该再给zabbix-agent发送一个ACK报文确认关闭连接，****然后zabbix-server进入TIME_WAIT状态，等待关闭连接，但是这里有一个巨坑：zabbix passive模式没有最后一次挥手！并且zabbix passive模式不支持长连接，****即zabbix-agent发完最后一次FIN报文以后会进入2MSL的一个TIME_WAIT状态，这个连接在两分钟内是不可重用的，这意味着你的服务器上面会出现大量的TIME_WAIT的tcp连接！** 


** 解决办法：**

>  
 **将zabbix模式换成主动模式：** 
 **或者开启linux内核的TIME_WAIT回收。** 


**主动模式工作流程：**

>  
 **（1）Zabbix-Agent向Zabbix-Server建立一个TCP连接** 
 **（2）Zabbix-Agent请求需要监测的数据列表** 
 **（3）Zabbix-Server响应Zabbix-Agent，发送一个item列表** 
 **（4）Zabbix-Agent响应请求 ** 
 **（5）完成本次会话后关闭TCP连接** 
 **（6）Zabbix-Agent开始周期性的采集数据** 


>  
 ** 将服务器的监控项都设置为主动模式，并且模板换成主动模式的模板** 


<img alt="" height="102" src="https://img-blog.csdnimg.cn/52cf0760b40d43a682f6c4dd5a7d0948.png" width="662">

** 问题解决：**

<img alt="" height="139" src="https://img-blog.csdnimg.cn/ecd2857672f249549f171c03ea030d92.png" width="1048">

```
[root@zabbix ipv4]# netstat -anplut| grep 10050|wc -l
4

```


