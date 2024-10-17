
--- 
title:  python篇--- python list分割 
tags: []
categories: [] 

---
## python list 分割

### 用Python将一个列表分割成小列表的实例讲解

```
l = [i for i in range(15)]

n = 3  # 大列表中几个数据组成一个小列表

print([l[i:i + n] for i in range(0, len(l), n)])

```

### 结果如下：

<img src="https://img-blog.csdnimg.cn/11264382ecce4379bd73ff615c5907a1.png" alt="在这里插入图片描述">
