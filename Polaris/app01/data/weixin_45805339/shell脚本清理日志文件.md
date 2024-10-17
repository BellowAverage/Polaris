
--- 
title:  shell脚本清理日志文件 
tags: []
categories: [] 

---
```
#!/bin/bash

clearDayNum=1 #数据保留天数

echo "开始清理.out或.in数据,保留$clearDayNum内数据......"
workdir="/var/userdata/workload"


logFiles=(`find $workdir -mtime +$clearDayNum -name "*.in" -o -mtime +$clearDayNum -name "*.out" | xargs`)

i=0
j=0
for logFile in ${logFiles[@]}
do
	
	rm $logFile
	if [ $? -eq 0 ];then
		i=$((${i} + 1))
		echo -e "\033[32m 清理$logFile文件成功！ \033[0m"
	else
		echo -e "\033[31m 清理$logFile文件失败！ \033[0m"
		j=$((${i} + 1))
	fi

done
#echo -e "\033[34m 本次清理数据：${logFiles[@]} \033[0m"

echo -e "\033[5;33m 本次共清理文件${<!-- -->#logFiles[@]}个，成功$i个，失败$j个 \033[0m"


```
