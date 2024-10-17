
--- 
title:  docker login 命令行登录失败，页面登录成功 
tags: []
categories: [] 

---1. docker login 命令行登录失败 <img src="https://img-blog.csdnimg.cn/083da5a026284facb448fa2b4c51e9f6.png" alt="在这里插入图片描述">
```
Error response from daemon: Get "https://registry-1.docker.io/v2/": unauthorized: incorrect username or password

```
1. 页面登录成功（url：https://login.docker.com/u/login/identifier?state=hKFo2SBzQnVQZTNXWm05ZHFHZXljMGtRT2ExNXRldkJ6TnIxU6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIER2NVo4RjlyX0RFTEhJcTdJS2x6NmVBOWk1MjItQWwxo2NpZNkgbHZlOUdHbDhKdFNVcm5lUTFFVnVDMGxiakhkaTluYjk） <img src="https://img-blog.csdnimg.cn/f927da8c204d4dd18aa7f8fb380b9f66.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">1. 后来发现命令行登录的时候，用户名不是邮箱而是账户名称（qinenqi）1. 重新登录 成功 <img src="https://img-blog.csdnimg.cn/6ef8bc099a634af4943d7511d5c9d56c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">