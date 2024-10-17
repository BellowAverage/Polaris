
--- 
title:  Zabbix4.0架构理解-zabbix的工作方式 
tags: []
categories: [] 

---
**目录**





























### 1.1、zabbix4.0架构图

<img alt="" height="882" src="https://img-blog.csdnimg.cn/5045f73893fc4320b67bf7f964363330.png" width="851">

 

**##########################################################################################** 

###  1.2、zabbix的进程

#### 1、  zabbix server

>  
 **        Zabbix server 是整个 Zabbix 软件的核心程序。         Zabbix server 进程以守护进程（Deamon）运行** 
 **        Zabbix Server 负责执行数据的主动轮询和被动获取，计算触发器条件，向用户发送通知。它是 Zabbix Agent 和 Proxy 报告系统可用性和完整性数据的核心组件。Server 自身可以通过简单服务远程检查网络服务（如Web服务器和邮件服务器）。** 
 **        Zabbix Server是所有配置、统计和操作数据的中央存储中心，也是Zabbix监控系统的告警中心。在监控的系统中出现任何异常，将被发出通知给管理员。** 
 **        基本的 Zabbix Server 的功能分解成为三个不同的组件。他们是：Zabbix server、Web前端和数据库。** 
 **        Zabbix 的所有配置信息都存储在 Server 和web前段进行交互的数据库中  ,例如，当你通过Web前端（或者API）新增一个监控项时，它会被添加到数据库的监控项表里。然后，Zabbix server 以每分钟一次的频率查询监控项表中的有效项，接着将它存储在 Zabbix server 中的缓存里。这就是为什么 Zabbix 前端所做的任何更改需要花费两分钟左右才能显示在最新的数据段的原因。** 


>  
 **   可以通过执行以下命令来启动zabbix server** 


```
shell&gt; service zabbix-server start
```

>  
    **     上述命令在大多数的 GNU/Linux 系统下都可以正常完成。如果是其他系统，你可能要尝试以下命令来运行：** 


```
 shell&gt; /etc/init.d/zabbix-server start
```

        类似的，停止、重启、查看状态，则需要执行以下命令：

```
            shell&gt; service zabbix-server stop
            shell&gt; service zabbix-server restart
            shell&gt; service zabbix-server status
```

>  
 **        手动启动** 
 **            如果以上操作均无效，您可能需要手动启动，找到 Zabbix Server 二进制文件的路径并且执行：** 


>  
 **        zabbix server 的命令行参数** 


```
            -c --config &lt;file&gt;              配置文件路径（默认的是 /usr/local/etc/zabbix_server.conf）
            -R --runtime-control &lt;option&gt;   执行管理功能
            -h --help                       帮助
            -V --version                    显示版本号
```

**##########################################################################################** 

####  2、zabbix agent

>  
 **        zabbix agent 部署在被监控目标上，以主动监控本地资源和应用程序 （硬盘，内存，处理器统计信息等）。         Zabbix agent 进程以守护进程（Deamon）运行。** 
 **        zabbix agent 收集本地的操作信息并将数据报告给zabbix server 用于进一步处理，一旦出现异常（例如硬盘空间已满或者有崩溃的服务进程）         zabbix server会主动警告管理员指定机器上的异常** 
 **        zabbix agents的极高效率缘于它可以利用本地系统调用来完成统计数据的采集** 
 **        zabbix agent可以运行被动检查和主动检查         在被动检查模式中 agent应答数据请求，zabbix server（或proxy） 询求数据，例如cpu load，然后zabbix agent返还结果         主动检查处理过程将相对复杂，agent必须首先从zabbix server索取监控项列表以进行独立处理，然后会定期发送采集到的新值给zabbix server** 
 **        是否执行被动或主动检查是通过选择相应的监控项类型来配置的。zabbix agent 处理 zabbix agent 或 zabbix agent（active） 类型的监控项** 


>  
 **        zabbix agent 的启动可以通过执行以下命令来完成** 


```
 shell&gt; service zabbix-agent start
```

>  
 **        上述命令在大多数的 GNU/Linux 系统下都可以正常完成。如果是其他系统，你可能要尝试以下命令来运行：** 


```
            shell&gt; /etc/init.d/zabbix-agent start
```

>  
 **        类似的，停止、重启、查看状态，则需要执行以下命令：** 


```
            shell&gt; service zabbix-agent stop
            shell&gt; service zabbix-agent restart
            shell&gt; service zabbix-agent status
```

>  
 **        手动启动         如果以上操作均无效，您可能需要手动启动，找到 Zabbix agent 二进制文件的路径并且执行：** 


```
        shell&gt; zabbix_agentd

```

 **##########################################################################################**

####     3、  zabbix proxy

>  
         ** zabbix proxy 是一个可以从一个或多个受监控设备采集监控数据并将信息发送到zabbix server的进程         Zabbix proxy 进程以守护进程（Deamon）运行。** 
 **        主要是代表zabbix server 工作，所有收集的数据都在本地缓存，然后传输到proxy所属的 zabbix server** 
 **        部署zabbix proxy是可选的，但可能非常有利于分担单个zabbix server 的负载，如果只有代理采集数据，则zabbix server会减少cpu和磁盘io的开销** 
 **        zabbix proxy是无需本地管理员即可集中监控远程位置，分支机构和网络的理想解决方案         zabbix proxy 需要使用独立的数据库** 


>  
 **        Zabbix proxy 的启动可以通过执行以下命令来完成：** 


```
            shell&gt; service zabbix-proxy start
```

>  
 **        上述命令在大多数的 GNU/Linux 系统下都可以正常完成。如果是其他系统，你可能要尝试以下命令来运行：** 


```
            shell&gt; /etc/init.d/zabbix-proxy start
```

>  
 **        类似的，Zabbix proxy 的停止、重启、查看状态，则需要执行以下命令：** 


```
            shell&gt; service zabbix-proxy stop
            shell&gt; service zabbix-proxy restart
            shell&gt; service zabbix-proxy status
```

>  
 **        手动启动         如果以上操作均无效，您可能需要手动启动，找到 Zabbix proxy 二进制文件的路径并且执行：** 


```
            shell&gt; zabbix_proxy
```

 **##########################################################################################**

####  4、 java gateway

>  
 **从 Zabbix 2.0 开始，以 Zabbix 守护进程方式原生支持监控 JMX 应用程序就存在了，称之为“Zabbix Java gateway”。Zabbix Java gateway 的守护进程是用 Java 编写。为了在特定主机上找到 JMX 计数器的值，Zabbix server 向 Zabbix Java gateway 发送请求，** 
  
  
 **当必须通过 Java gateway 更新监控项时，Zabbix server 或 proxy 将连接到 Java gateway 并请求该值，Java gateway 将检索该值并将其传递回 Zabbix server 或 Zabbix proxy。 因此，Java gateway 不会缓存任何值。** 


 **##########################################################################################** 

#### 5、zabbix get

>  
 **Zabbix get 是一个命令行应用，它可以用于与 Zabbix agent 进行通信，并从 Zabbix agent 那里获取所需的信息。 ** 


>  
 ** 该应用通常被用于 Zabbix agent 故障排错。** 


>  
 **运行 Zabbix get** 
 **一个在 UNIX 下运行 Zabbix get 以从 Zabbix agent 获取 processor load 的值的例子。** 


```
shell&gt; cd bin
shell&gt; ./zabbix_get -s 127.0.0.1 -p 10050 -k system.cpu.load[all,avg1]
```

>  
 **请注意，此处的监控项键值包含空格，因此引号用于将监控项键值标记为 shell。 引号不是监控项键值的一部分；它们将被 shell 修剪，不会被传递给Zabbix agent。****Zabbix get 接受以下命令行参数：** 




```
  -s --host &lt;host name or IP&gt;      指定目标主机名或IP地址
         -p --port &lt;port number&gt;          指定主机上运行 Zabbix agent 的端口号。默认端口10050
         -I --source-address &lt;IP address&gt; 指定源 IP 地址
         -k --key &lt;item key&gt;              指定要从监控项键值检索的值
         -h --help                        获得帮助
         -V --version                     显示版本号
```

**##########################################################################################**

### 1.3、zabbix的几种工作方式

#### 1、通过zabbix agent

>  
 **通过zabbix agent，获取机器的硬件利用率，应用，数据库，设备等情况，然后通过主动或者被动的模式，将数据发送给zabbix server，zabbix server收集到数据后，存储到 DB（数据库）里面，最后Zabbix Web，前端页面将数据库里的数据进行展示。** 


#### 2、通过zabbix proxy

>  
 **zabbix proxy就相当于一个代理，代替zabbix server 向zabbix agent获取数据，zabbix agent 直接与zabbix proxy交互，zabbix proxy分担zabbix server的压力，收集好数据以后就直接发送给zabbix server，这也是zabbix 分布式的一种实现。** 


#### 3、通过 zabbix java gateway

>  
 **zabbix java gateway就相当于一个“体育老师”的角色，专门收集java应用的数据，java gateway收集了所有java应用的数据以后，再发送给zabbix server。** 


#### 4、其他

>  
 **zabbix server 自身还能实现一些简单的检查，例如snmp端，server可以直接从snmp协议收集数据，可以直接去监控web，也可以直接监控tcp/udp端口是否开启，****这些功能不需要再部署zabbix agent了，zabbix server自身就可以实现。** 


###  1.3、zabbix 数据走向

<img alt="" height="136" src="https://img-blog.csdnimg.cn/1119e8b0b42047bf9df98a0be0092df8.png" width="840">


