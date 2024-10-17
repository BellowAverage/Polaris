
--- 
title:  打开目录报错：Stale file handle 
tags: []
categories: [] 

---


**报错原因**：

```
cd AIRecord
-bash: cd: AIRecord: Stale file handle
```

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/ff89952d68dd63bacecdf71f6b5f229e.png">

查看目录详情，显示d?????????

可能是NFS在挂载时，后面不用了，没有解挂载掉，所以这个目录没用了。

解决：
- 如果此目录不在用了， 直接解挂载这个目录即可。- 如果还有数据需要使用，就重新挂载下。
```
解决:
umount -f /directory

后重新挂载：
/bin/mount -t nfs 192.168.6.31:/web/share /web/share/
```

 
