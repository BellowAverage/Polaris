
--- 
title:  指定ssh的默认启动目录 
tags: []
categories: [] 

---
ssh 有一个默认的参数 -t。

```
ssh -t root@127.0.0.1 "cd /home/work &amp;&amp; bash"

```

问题：
- 首先，连接符必须是 &amp;&amp; 而不是分号，不然会出现目录指定失败的情况- 如果后面不接bash而是其他的命令，那么当这个命令执行结束以后，整个ssh会自动断开