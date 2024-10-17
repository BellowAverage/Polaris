
--- 
title:  【Python语法实例】-6 九九乘法表 
tags: []
categories: [] 

---
```
#打印九九乘法表。
for i in range(1,10):   #[1,2,3,4,5,6,7,8,9]
    
    for j in range(1,i+1):#[1,2,3,4,5 ]
        print (i,'*',j,'=',i*j,'\t',end="")     #end=""作用是不换行
    print("")    

```
