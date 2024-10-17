
--- 
title:  linux获取随机字符串（或数字）的3种方法 
tags: []
categories: [] 

---
#### 1. 获取随机8位字符串：

##### 方法1：

```
# echo $RANDOM |md5sum |cut -c 1-8

```

返回：

```
471b94f2

```

##### 方法2：

```
# openssl rand -base64 4

```

返回

```
vg3BEg==

```

##### 方法3：

```
# cat /proc/sys/kernel/random/uuid |cut -c 1-8

```

返回

```
】ed9e032c

```

#### 2.获取随机8位数字：

##### 方法1：

```
# echo $RANDOM |cksum |cut -c 1-8

```

返回

```
23648321

```

##### 方法2：

```
# openssl rand -base64 4 |cksum |cut -c 1-8

```

返回

```
38571131

```

##### 方法3：

```
# date +%N |cut -c 1-8

```

返回：

```
69024815

```
