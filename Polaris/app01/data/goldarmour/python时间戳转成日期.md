
--- 
title:  python时间戳转成日期 
tags: []
categories: [] 

---
#### 时间戳转日期

代码如下：

```
import time

def st_to_date(ts):
    # 先转成年月日时分秒的数组，然后转成字符串格式
    date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts)) 
    return date

now=time.time() #获取当前时戳
date=st_to_date(now)
print(date)
```


