
--- 
title:  Linux /dev/sda1磁盘满了，清理办法 
tags: []
categories: [] 

---
两种情况比较多

1.查看/tmp　所占的内存，不想重启，可以手动清理

2./var/log/syslog.1 所占的内存,清空

可以使用下面指令删除30天钱的文件

sudo find /var/log/ -type f -mtime +30 -exec rm -f {} \;

３.

清理linux系统垃圾还有以下命令

sudo apt-get autoclean 清理旧版本的软件缓存

sudo apt-get clean 清理所有软件缓存

sudo apt-get autoremove 删除系统不再使用的孤立软件
