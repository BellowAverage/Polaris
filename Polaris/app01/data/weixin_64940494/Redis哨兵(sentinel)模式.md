
--- 
title:  Redis哨兵(sentinel)模式 
tags: []
categories: [] 

---
        Redis的的主从模式中我们了解到当master服务器宕机后slave服务器并不会自动接管master服务器而是继续等待master服务器的开启，或者需要手工将slave服务器通过执行slaveof no one 命令才能转变为master服务器，而Redis的哨兵模式就可以解决这个问题。

        哨兵模式就是监控所有master和slave服务器，当master服务器异常则会从slave服务器中选举一台作为master服务器同时其他salve服务器也将会被重新挂在到新的master服务器上，而当原来的master服务器恢复后也将作为slave服务器挂载在新的master服务器下。client客户端在首次访问Redis服务时其实访问的是Redis哨兵(sentinel),sentinel会将自己监控的Redis实例的master节点信息返回给client客户端，后续客户端就会直接访问master节点。

**哨兵模式的选举规则**

        1. 选择优先级最高的服务器，在redis.conf配置文件中 slave-priority 值越小优先级越高。

        2. 当优先级一样时，获取原主机的数据量最全的服务器。

        3. 当1和2都一样时选择redis实例启动时runid最小的服务器。

**Redis哨兵模式配置**

这里我用的是一台服务器以不同的端口作为多台服务器。

1. 在Redis配置文件目录下创建一个 sentinel.conf 文件，在配置文件中添加下列配置。

>  
 sentinel monitor myredis 127.0.0.1 6379 1    


>  
 myredis为自己对哨兵取名   
 127.0.0.1 6379 哨兵需要监控的主服务器 
 1 代表当主服务器宕机，选举时需要几台服务器通过选举，一般这个值需大于主从服务器数量的一半 ，这里我们只有3台服务器(1主2从的架构) 


2. 开启哨兵

>  
 redis-sentinel  sentinel.conf 


3. 把6379这台master服务器 shutdown后，sentinel出现以下结果。

<img alt="" height="326" src="https://img-blog.csdnimg.cn/f635ac9bc3664952b0eeb8090773c48b.png" width="893">

 如图可以看出sentinel的执行过程，监控到6379宕机后，选举了6380作为master服务器，并将6381挂在到了6380上。

4. 查看6380和6381这两台服务器的信息。

<img alt="" height="243" src="https://img-blog.csdnimg.cn/0e66992c983f42a9b0138363cdcf6482.png" width="539">

<img alt="" height="392" src="https://img-blog.csdnimg.cn/774f83aa82b44559b748103ff0fca641.png" width="671">

5. 将原6379重新启动，发现6379挂载在了6380上。

<img alt="" height="370" src="https://img-blog.csdnimg.cn/f463c2c52fbb4e798a60e4cfd1ed3344.png" width="743">

以上演示了Redis哨兵模式的过程，在实际应用中一般都是多台服务器(一主n从的架构），同时sentinel也可以部署集群以确保哨兵的绝对有效。 


