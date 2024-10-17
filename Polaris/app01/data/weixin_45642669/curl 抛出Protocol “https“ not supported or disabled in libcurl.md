
--- 
title:  curl 抛出Protocol “https“ not supported or disabled in libcurl 
tags: []
categories: [] 

---
## 故障描述

使用curl的时候抛出： Protocol “https” not supported or disabled in libcurl

## 故障原因
- linux自带的发行版是支持https的- 其他软件安装的时候，替代了linux自带的版本
## 解决

除非丧心病狂，不然一般不会直接删除默认的curl。一般是写入一个新位置，然后软连接到curl

执行命令

```
find / -name curl

```

然后，如果/usr/bin/curl存在的话，可以直接执行

```
/usr/bin/curl https:XXX

```

可以查询是否支持https协议
