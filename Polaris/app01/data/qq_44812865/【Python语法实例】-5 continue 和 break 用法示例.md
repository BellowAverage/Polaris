
--- 
title:  【Python语法实例】-5 continue 和 break 用法示例 
tags: []
categories: [] 

---
```
continue 和 break 用法示例。
# continue 和 break 用法
i = 1
while i &lt; 10:   
    i += 1
    if i%2 &gt; 0:      # 非双数时跳过输出
        continue
    print (i)         # 输出双数2、4、6、8、10

i = 1
while 1:             # 循环条件为1必定成立
    print (i)          # 输出1~10
    i += 1
    if i &gt; 10:         # 当i大于10时跳出循环
        break




```
