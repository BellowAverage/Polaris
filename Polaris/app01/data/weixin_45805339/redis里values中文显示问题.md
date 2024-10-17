
--- 
title:  redis里values中文显示问题 
tags: []
categories: [] 

---
## redis里values中文显示问题

```
lpush name 张无忌 赵敏

```

<img src="https://img-blog.csdnimg.cn/20200102194512755.png" alt="在这里插入图片描述"> 解决方法： 在启动redis客户端时，添加–raw

```
redis-cli --raw

```

<img src="https://img-blog.csdnimg.cn/20200102194844161.png" alt="在这里插入图片描述">
