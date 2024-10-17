
--- 
title:  grep无法使用完整的正则表达式 
tags: []
categories: [] 

---
## 问题描述

grep无法使用完整的正则表达式，比如前置断言、后置断言、\d和\t、\n等

## 问题原因

使用了扩展正则，而不是perl正则。规则和perl正则不同

从文档上讲得很清楚： -E PATTERN is an extended regular expression 他是扩展表达式，而不是正则表达式……

链接如下： https://blog.51cto.com/linux2015/1576889

扩展正则并不支持很多正则表达式语法：
- 前置断言（?=123）- 后置断言- \d+也并不支持- \t也不支持
<img src="https://img-blog.csdnimg.cn/direct/42fa6a1404f342ddbeebd24eec31365a.png" alt="在这里插入图片描述"> 比如下面123，使用\d+匹配失败 <img src="https://img-blog.csdnimg.cn/direct/d31ad55c384a489ba1f05d9e574af142.png" alt="在这里插入图片描述">

作为平替，扩展正则 -E扩展了其他的语法： <img src="https://img-blog.csdnimg.cn/direct/aa4671574c58491c88faabdc59c04dcf.png" alt="在这里插入图片描述">**-E 并不等于perl正则。虽然perl正则大部分语法都类似**

## 解决方案

而想要支持全部的正则表达式，需要使用-P：perl正则

测试发现符合perl规则 <img src="https://img-blog.csdnimg.cn/direct/802cc73845974d67a41d769ebf5d05f2.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/direct/00cfb9bdd0064d6188d8ca073e17b177.png" alt="在这里插入图片描述">
