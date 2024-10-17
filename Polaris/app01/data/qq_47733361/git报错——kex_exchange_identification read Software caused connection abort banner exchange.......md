
--- 
title:  git报错——kex_exchange_identification: read: Software caused connection abort banner exchange...... 
tags: []
categories: [] 

---
#### 1、问题：

在IDE推送的时候，出现了如下的问题，特此记录一下：

>  
 kex_exchange_identification: read: Software caused connection abort banner exchange: Connection to 175.24.250.178 port 22: Software caused connection abort fatal: Could not read from remote repository. Please make sure you have the correct access rights and the repository exists. 


<img src="https://img-blog.csdnimg.cn/e7c50276656045d59d209d42ff207068.png" alt="在这里插入图片描述"> 出现这个问题的原因呢，可能是因为当时通过 http 连接的路径或者端口号改变了，导致远程仓库与本地仓库不匹配。

#### 2、解决

在项目目录下输入如下命令，重新建立连接，这里会在次输入相关远程仓库的账号密码：

```
git remote set-url origin 路径

```

例如下面：

```
git remote set-url origin https://e.coding.net/lcc/yjwzDispatch/yjwzdispatch_front.git

```

此时在次推送就不会有问题了！
