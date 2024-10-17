
--- 
title:  Power Shell个人使用笔记 
tags: []
categories: [] 

---
### 运行脚本失败，被策略禁止

>  
 运行以下代码 


```
get-ExecutionPolicy
Set-ExecutionPolicy -Scope CurrentUser
RemoteSigned

```
