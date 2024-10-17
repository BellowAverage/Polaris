
--- 
title:  Python获取当前时间 
tags: []
categories: [] 

---
## 一、使用datetime模块

```
import datetime
i = datetime.datetime.now()  #获取当前时间
print('今天是{}月{}日{}点{}分{}秒'.format(i.month,i.day,i.hour,i.minute,i.second))

```

打印结果：

```
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
```

打印结果： 

```
import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
```

打印结果：

2022-12-03 18:01:04 

 
