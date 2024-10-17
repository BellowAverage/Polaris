
--- 
title:  Linux 用户管理相关命令 
tags: []
categories: [] 

---
### Linux 用户管理相关命令:
1.  添加用户: useradd test <img src="https://img-blog.csdnimg.cn/0146a68433544165ae46035447718739.png" alt="在这里插入图片描述"> 当创建用户成功后，Linux会在home目录下自动的创建和用户同名的目录 <img src="https://img-blog.csdnimg.cn/fb0d7b46c7a54e26969bed6228f73152.png" alt="在这里插入图片描述"> 1.  给用户设置密码： passwd test <img src="https://img-blog.csdnimg.cn/e5a9d04b4dca4a538f678d21fd20dd8c.png" alt="在这里插入图片描述"> 输入两次密码即可 1.  查询用户： id test <img src="https://img-blog.csdnimg.cn/84af2b1677554f6b8e875923e0f0c9e1.png" alt="在这里插入图片描述"> 1.  删除用户 userdel test <img src="https://img-blog.csdnimg.cn/3dfeb243bb8345f2969269f09c771e6c.png" alt="在这里插入图片描述"> 删除用户 ，但是会保留该用户的home目录 userdel -r test 删除用户，并删除该用户对应的home目录 
### 用户组的命令：
1.  增加一个新的用户组： groupadd testgroup <img src="https://img-blog.csdnimg.cn/5fd4786ad742415dad8439898071e055.png" alt="在这里插入图片描述"> 1.  删除一个用户组： groupdel testgroup <img src="https://img-blog.csdnimg.cn/a393dfada1324872bf097583b19557b8.png" alt="在这里插入图片描述"> 1.  查看用户组： cat /etc/group <img src="https://img-blog.csdnimg.cn/5c8cf954d32d49a9a0e4c7d5ecbb38d5.png" alt="在这里插入图片描述"> 1.  修改用户组的属性： usermod -g testgroup test <img src="https://img-blog.csdnimg.cn/8f4f91316e004940b46783c626d3cc7b.png" alt="在这里插入图片描述"> 