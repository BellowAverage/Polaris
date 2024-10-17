
--- 
title:  PowerBI - 匹配并从另一个表中获取值 
tags: []
categories: [] 

---
我有 2 个表通过列 A 相互连接。我想将列 C 与列 A 匹配并获得列 B 的值。 <img src="https://img-blog.csdnimg.cn/842a654708e44b8f820d5c42b909fda5.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ce0827caf5d94bb591b70a823447c273.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/10e9ba13f6454f9d98a2e64c6b39a056.png" alt="在这里插入图片描述">

DAX 函数是 LOOKUPVALUE .

```
MatchedOutput = LOOKUPVALUE(Table2[ColB],Table2[ColA],Table1[ColC])

```

**这将查找 Table2[ColB] 中的值哪里Table2[ColA]匹配 Table1[ColC] .**
