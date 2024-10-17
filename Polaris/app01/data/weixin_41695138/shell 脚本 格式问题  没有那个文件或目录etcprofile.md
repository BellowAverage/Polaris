
--- 
title:  shell 脚本 格式问题 : 没有那个文件或目录etc/profile 
tags: []
categories: [] 

---
### 异常信息：

```
increment.sh:行2: $'\r': 未找到命令
increment.sh:行9: $'\r': 未找到命令
increment.sh:行11: $'\r': 未找到命令
: 没有那个文件或目录etc/profile

```

<img src="https://img-blog.csdnimg.cn/546aaa7e0f8747f3ad94b9839c0ae8bd.png" alt="在这里插入图片描述"> 原因是： 我在windows环境下写的 shell 脚本上传至centos7下， 出现了格式问题，因此报错 解决办法： 查看格式：:set ff

```
vim increment.sh 
:set ff

```

<img src="https://img-blog.csdnimg.cn/44bab52ad24945428bb844b8849a0a57.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/210224606f4645c08ed91f426a66dc97.png" alt="在这里插入图片描述"> dos是换成unix格式， :set ff=unix <img src="https://img-blog.csdnimg.cn/c1444ffee4b74b128b2dc1b5b766876e.png" alt="在这里插入图片描述"> 设置后保存文件即可，重新执行，成功 <img src="https://img-blog.csdnimg.cn/30c146874d0c4d05b3c6cb11bb2bc355.png" alt="在这里插入图片描述">
