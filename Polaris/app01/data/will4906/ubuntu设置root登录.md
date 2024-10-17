
--- 
title:  ubuntu设置root登录 
tags: []
categories: [] 

---
简单做个笔记  由于ubuntu默认关掉了ssh的root登录，所以需要做如下处理开放root登录

### 设置root密码

在终端执行

```
sudo passwd root
```

<img src="https://img-blog.csdn.net/20170507015141479?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">

### 简单测试

```
su -
```

<img src="https://img-blog.csdn.net/20170507015407685?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">

### 修改配置文件

```
vi /etc/ssh/sshd_config
```
- 将PermitRootLogin后面改为yes  <img src="https://img-blog.csdn.net/20170507015751565?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">
### 重启机器
