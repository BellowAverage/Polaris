
--- 
title:  ubuntu下使用filezilla上传文件权限问题 
tags: []
categories: [] 

---
今天在使用filezilla连接中的ubuntu的时候出现上次出错，错误详情为：命令:    put "E:\All 

 <img alt="" src="https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTcxMjA3MTYwMzMyMTU0?x-oss-process=image/format,png">

看完错误大概知道和权限有问题，再次查看虚拟机，我们使用以下命令给我们需要放入的目标文件权限：

sudo chmod 777 /usr/local/

再次尝试上传，上传成功！

/usr/local/的文件路径可以根据你的情况调整，比如你想放在/home/yaoming/下

1. sudo su

2. 输入普通用户下的密码，进入root账号下

sudo chmod 777 /home/yaoming/

再次尝试上传，上传成功！
