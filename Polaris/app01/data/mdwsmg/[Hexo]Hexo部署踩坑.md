
--- 
title:  [Hexo]Hexo部署踩坑 
tags: []
categories: [] 

---
>  
 记录一下hexo部署遇到的坑 


### 部署遇到的坑——git
- git key 使用命令生成ssh后，需要确认生成成功，且文件是新的
```
ssh-keygen -t rsa -C "yourGitMail"

```
-  git token github 2021年8月下旬 开始，不能直接使用password进行认证，需要生成token代替密码进行认证 -  git SSL SSL_read: Connection was aborted, errno 10053 解决方法，禁用SSL验证 
```
git config http.sslVerify "false"

```
