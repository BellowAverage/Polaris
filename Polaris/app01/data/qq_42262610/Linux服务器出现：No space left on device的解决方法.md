
--- 
title:  Linux服务器出现：No space left on device的解决方法 
tags: []
categories: [] 

---
安装任意东西都会出现No space left on device，原因是服务器中的空间用完了。

df -lh查看系统的磁盘使用情况，

在我的 /dev/sda2 下占用率已经达到100%，在根目录下。

cd / 

sudo du -sh * # 查看到根目录下各个文件夹得大小

我的原因是home下占用了太多的空间，

cd /home

sudo du -sh *

将各自用户中多余的东西删除

OK，空间出现剩余。
