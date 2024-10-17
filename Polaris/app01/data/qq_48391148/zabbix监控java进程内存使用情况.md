
--- 
title:  zabbix监控java进程内存使用情况 
tags: []
categories: [] 

---
###  需求：监控集群里面所有Java进程的内存使用情况。

>  
 **查看linux系统里面有哪些java进程在运行：jps命令** 


```
[root@localhost zabbix]# jps
26490 YarnTaskExecutorRunner
12012 NodeManager
14047 YarnTaskExecutorRunner
25007 Jps

```

>  
 **查看java进程的内存使用情况：jstat命令  -gc  -gcutil** 


```
[root@node035 zabbix]# jstat -gc 12012
 S0C    S1C    S0U    S1U      EC       EU        OC         OU       MC     MU    CCSC   CCSU   YGC     YGCT    FGC    FGCT     GCT   
2560.0 2560.0  0.0   2208.0 335872.0 180374.6  338432.0   57522.0   51624.0 50525.8 5808.0 5542.1 104079  881.980   3      0.384  882.364

```

```
[root@node035 zabbix]# jstat -gcutil 12012
  S0     S1     E      O      M     CCS    YGC     YGCT    FGC    FGCT     GCT   
  0.00  86.25  89.43  17.00  97.87  95.42 104079  881.980     3    0.384  882.364

```

 **####################################################################### **

>  
 **采集数据脚本：** 
 **        ****这里最好用grep命令过滤出所有你要监控的所有java进程，不要用grep -v排除法** 
 **        ****因为有些进程可能从产生到销毁的过程比你使用jps命令还快，例如jps，jstat，jmap等命令，所以可能使用jps | grep 只能获取一个进程pid号，无法获取进程名等信息，** 
 **        ****导致你的脚本会出现偶尔卡顿的情况，然后数据获取也会出现一系列的问题** 
 **        对于可能出现的同一个进程名有多个进程存在的情况，例如父子进程等。** 
 **        这里脚本采用的是给相同进程名进行标记的方法，例如 kafka，kafka1，kafka2.....** 
 **        因为zabbix采用的是自动发现的方式来获取进程名，曾经尝试过使用进程名+pid的方式来获取，但是pid会发生变化，** 
 **        所以目前还没有好的方法来分离两个相同进程名的方法** 
 **        不过监控的意义在于观察监控项的趋势变化，如果看到一个进程内存状态有异常，根据进程名再到我们脚本的数据文件里面来获取pid** 


```
[root@node031 monitor]# cat getJavaMemoryStatus.sh
#!/bin/bash
# Final output
output=""

# Variables
flag=1
last_name=""
currnet_name=""	

# JPS Command
result=`/usr/local/jdk/bin/jps | egrep  "QuorumPeerMain|Kafka|CanalAdminApplication|CanalLauncher|JournalNode|DFSZKFailoverController|NameNode|DataNode|ResourceManager|NodeManager|YarnJobClusterEntrypoint|YarnTaskExecutorRunner|HMaster|HRegion" | sort -k2 -k1`

# Main Loop
#echo "$result" | while read -r pid name ; do
while read -r pid name ; do
    #echo "${pid},${name},${last_name}"

	# Add num to same process name, for example: Process1, Process2 ...
	if [ x"$name" = x"$last_name" ]; then
		currnet_name="$name$flag"
		flag=$(( $flag + 1 ))	
	else
	    currnet_name="$name"	
		flag=1
	fi
	last_name="$name"

	# Get GC Status
	res_gc=`/usr/local/jdk/bin/jstat -gc $pid 2&gt;/dev/null | awk 'NR==2{print $1, $2, $3, $4, $5, $6, $7, $8}'`
	res_gcutil=`/usr/local/jdk/bin/jstat -gcutil $pid 2&gt;/dev/null | awk 'NR==2{print $1, $2, $3, $4, $7, $8, $9, $10}'`

	# Combime output
	if [ x"$output" = x"" ]; then 
		output="${currnet_name} $pid ${res_gc} ${res_gcutil}"
	else
		output+=$'\n'"${currnet_name} $pid ${res_gc} ${res_gcutil}"
	fi
	#echo "$output"

done &lt;&lt;&lt; "$result"

# Output
echo "$output" &gt; /tmp/java_memory_status.txt

```

>  
 **脚本优化：** 
 **        获取数据命令尽量只运行一次，减少服务器压力** 
 **        取数据的时候尽量不要读文件，减少IO** 


>  
 **进程自动发现脚本：** 


```
[root@localhost parameter_script]# cat java_discovery.sh 
#!/bin/bash
javaProcessList=`cat /tmp/java_memory_status.txt|awk '{print $2"#"$1}'`
echo "{\"data\":["
first=1
for javaProcess in $javaProcessList;
do
    IFS='#' read -r -a items &lt;&lt;&lt; "$javaProcess";
    if [ $first == 1 ]; then
        echo "{\"{#JAVAPSNAME}\":\"${items[1]}\",\"{#JAVAPSPID}\":\"${items[0]}\"}";
        first=0
    else
        echo ",{\"{#JAVAPSNAME}\":\"${items[1]}\",\"{#JAVAPSPID}\":\"${items[0]}\"}";
    fi
done;

echo "]}";

```

**####################################################################### **

>  
 **获取java进程内存数据脚本：** 


```
[root@node031 parameter_script]# cat getjavastatus.sh 
#!/bin/bash
pid=`cat /tmp/java_memory_status.txt | awk '{print $2}'`
case $2 in
# S0总大小
S0C)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $3}'|bc
	;;
# S1总大小
S1C)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $4}'|bc
	;;
# S0使用大小
S0U)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $5}'|bc
	;;
# S1使用大小
S1U)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $6}'|bc
	;;
# Eden总大小
EC)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $7}'|bc
	;;
# Eden使用大小
EU)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $8}'|bc
	;;
#old大小
OC)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $9}'|bc
	;;
#old使用大小
OU)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $10}'|bc
	;;
# S0使用率
S0Util)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $11}'|bc
	;;
# S1使用率
S1Util)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $12}'|bc
	;;
# Eden使用率
EUtil)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $13}'|bc
	;;
#old使用率
OUtil)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $14}'|bc
	;;
# 年轻代垃圾回收次数
YGC)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $15}'|bc
	;;
# 年轻代垃圾回收消耗时间
YGCT)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $16}'|bc
	;;
# 老年代垃圾回收次数
FGC)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $17}'|bc
	;;
# 老年代垃圾回收消耗时间
FGCT)
	grep -w $1 /tmp/java_memory_status.txt |awk '{print $18}'|bc
	;;
esac	
```

>  
 **添加配置文件，自定义监控项** 


```
UserParameter=javaps,/etc/zabbix/parameter_script/java_discovery.sh
UserParameter=javastat[*],/etc/zabbix/parameter_script/getjavastatus.sh $1 $2

```

>  
 **重启zabbix-agent2进程** 


```
service zabbix-agent2 restart
```

>  
 **配置计划任务** 


```
*/1 * * * * sh /data/script/monitor/getJavaMemoryStatus.sh

```

>  
 **配置java进程自动发现** 


>  
 **创建一个模板组：JavaProcess** 


<img alt="" height="144" src="https://img-blog.csdnimg.cn/c0843ee1f66347208f598546af241a9b.png" width="1200">

>  
 ** 创建一个模板 JavaProcess** 


<img alt="" height="373" src="https://img-blog.csdnimg.cn/6948511fcf224d72946f241737d867fd.png" width="1200">

>  
 **在 JavaProcess模板里面创建自动发现规则** 


 <img alt="" height="680" src="https://img-blog.csdnimg.cn/b4ec2aa160f644e1acfec273ced9b282.png" width="1099">

>  
 ** 添加要监控的监控项原型** 


<img alt="" height="688" src="https://img-blog.csdnimg.cn/1cad5b42a9ab42098384dbc37a268b0d.png" width="1200">

>  
  **给要监控的主机添加JavaProcess模板** 


 <img alt="" height="224" src="https://img-blog.csdnimg.cn/415ac49a33fa46ea82ac9a48b68e2b34.png" width="733">

>  
 **zabbix会自动将发现的进程添加到对应主机,然后根据监控项原型创建出对应的监控项，采集到数据以后grafana就会产生图形** 


<img alt="" height="1165" src="https://img-blog.csdnimg.cn/132f5fcb23df47328d73999ffbb6d1af.png" width="1200">
