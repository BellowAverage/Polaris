
--- 
title:  win的Windows PowerShell 
tags: []
categories: [] 

---
### 解决脚本运行不了的问题

**打开管理员的运行窗口**

>  
 `win+x` 选择管理员Windows PowerShell 


**设置执行策略**

```
Set-ExecutionPolicy RemoteSigned

```

运行完选 Y

还没同步到其他地方

**同步一下策略**

```
Set-ExecutionPolicy -Scope CurrentUser
//选择RemoteSigned
RemoteSigned

```
