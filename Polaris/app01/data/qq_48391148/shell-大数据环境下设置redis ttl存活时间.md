
--- 
title:  shell-大数据环境下设置redis ttl存活时间 
tags: []
categories: [] 

---
>  
 **情况：** 
 **最近项目无用代码造成堆积，要把redis数据库中的以form_开头的key都设置一个ttl** 


>  
 **在测试环境下的redis服务器上面插入10w个key，然后进行测试** 


```
[root@vm01 lianxi]# cat 100_keys.sh 
#!/bin/bash

for ((i=0;i&lt;100000;i++))
do
{
echo $i |redis-cli -n 7 -x set form_$i
}&amp;
done
wait
```

>  
 **使用 redis-cli -n 7 keys *查看已经产生的keys** 


<img alt="" height="405" src="https://img-blog.csdnimg.cn/277d84f78cf9457c9c498ab3f7092f52.png" width="508"> 

>  
 **设置ttl脚本： ** 


```
[root@vm01 lianxi]# cat set-ttl.sh 
#!/bin/bash

keys=`/usr/local/redis/bin/redis-cli -n 7 keys form_* | head -10000`
for i in $keys

do
{
    /usr/local/redis/bin/redis-cli -n 7 &lt;&lt;EOF
    expire $i 1800
EOF
}&amp;
done
wait

```

>  
 **脚步运行测试：使用pstree命令查看一瞬间产生的线程，应该开启了近万个线程来执行。** 


<img alt="" height="675" src="https://img-blog.csdnimg.cn/a50f2513d507459686c614ca835af639.png" width="1003">

<img alt="" height="49" src="https://img-blog.csdnimg.cn/0919556436714d4d9e14b3db0cf37ddc.png" width="491">

>  
 ** 然后在再写一个计划任务，设置每30分钟执行一次，ttl设置的时间是1800s** 
 **实现给所有form_开头的key值设置一个1800s的ttl** 





