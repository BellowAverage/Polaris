
--- 
title:  git 添加公钥以后仍然失效的bug的一个解决方案 
tags: []
categories: [] 

---
#### 遇见的问题：
- git失效。- 故障和没有添加公钥一模一样- 重新新增公钥也无法解决，还是提示没有该公钥- 查询公钥存在
#### debug发现：

排查bug来源如下： https://zhuanlan.zhihu.com/p/440267789 https://www.linuxquestions.org/questions/linux-security-4/no-matching-host-key-type-found-their-offer-ssh-rsa-ssh-dss-4175701155/

在.ssh路径下添加一个config文件（无扩展名） 写入：

```
HostKeyAlgorithms ssh-rsa
PubkeyAcceptedKeyTypes ssh-rsa

```

问题立刻解决。

#### 原因

没有使用ssh-rsa算法来进行匹配。  
