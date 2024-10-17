
--- 
title:  cannal 启动异常(show master status‘ has an error pls check. you need (at least one of) the SUPER,REPLI) 
tags: []
categories: [] 

---
异常信息：‘show master status’ has an error! pls check. you need (at least one of) the SUPER,REPLICATI 详细信息： [destination = example , address = node03/192.168.8.120:3306 , EventParser] ERROR com.alibaba.otter.canal.common.alarm.LogAlarmHandler - destination:example[com.alibaba.otter.canal.parse.exception.CanalParseException: command : ‘show master status’ has an error! pls check. you need (at least one of) the SUPER,REPLICATION CLIENT privilege(s) for this operation <img src="https://img-blog.csdnimg.cn/4727b3e328f44ecea4fb9100dfe9ffde.png" alt="在这里插入图片描述"> 可能的原因：
1. 没有开启权限：
```
			CREATE USER canal IDENTIFIED BY 'canal';    
			GRANT ALL PRIVILEGES ON *.* TO 'canal'@'%' ;
			FLUSH PRIVILEGES;

```

<img src="https://img-blog.csdnimg.cn/5ca16afc732d491e8ed0a9a77c13e9ad.png" alt="在这里插入图片描述"> 2. 没有开启bin-log日志： vim /etc/my.cnf

```
log-bin=/var/lib/mysql/mysql-bin # 开启 binlog
binlog-format=ROW # 选择 ROW 模式
server_id=1 # 配置 MySQL replaction 需要定义，不要和 canal 的 slaveId 重复

```

<img src="https://img-blog.csdnimg.cn/edaaae2207fd4da0b82321946dbc1675.png" alt="在这里插入图片描述"> 经过排查，小编都配置好了，很奇怪！后来发现是配置完之后，没有重启mysql服务，尴尬！！！ 重启mysql 服务：

```
 systemctl restart mysqld

```

再参看日志： 成功 cat example.log <img src="https://img-blog.csdnimg.cn/fddabb47f25c4e9ea6678bdba7ba3bda.png" alt="在这里插入图片描述">
