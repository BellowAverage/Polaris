
--- 
title:  Js里面无法调用contains 
tags: []
categories: [] 

---
## 问题描述：
- 标准的字符串类型，检查发现是的，不是undefined或者其他类型- 无法调用contains，报错contains方法不存在- 火狐浏览器
## 原因

火狐不支持contains方法，而chrome支持

为了兼容性，用标准的indexOf() &gt;= 0 进行代替
