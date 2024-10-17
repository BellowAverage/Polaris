
--- 
title:  【linux问题记录】 
tags: []
categories: [] 

---
Linux普通用户登录后，命令行提示：-bash-4.2$ ，原因分析及解决

有时候在使用用户登陆Linux系统时会发现，命令行提示符成了：-bash-4.2$，不显示用户名，路径信息。 <img src="https://img-blog.csdnimg.cn/direct/e598d11b09bb41e7a56b03e9dc5322e8.png" alt="在这里插入图片描述">

### 原因：

用户家目录里面与环境变量有关的文件被删除所导致的 也就是这俩文件： .bash_profile .bashrc 这两个文件被删除了，导致了这个错误

### 解决方法：

从/etc/skel把丢失的文件 复制回来就可以了 -bash-4.1$ cp /etc/skel/.bash* ~　　　　 -bash-4.1$ logout ##复制回来后，登出用户，然后在登陆用户查看是否已经解决 <img src="https://img-blog.csdnimg.cn/direct/15a6bbeb05a847bda22ababe5a38bc13.png" alt="在这里插入图片描述"> [root@rudy ~]# su - rudy 转自https://www.cnblogs.com/little-bin/p/16908482.html
