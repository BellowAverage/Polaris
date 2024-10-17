
--- 
title:  KubeSphere安装redis 
tags: []
categories: [] 

---
### 安装

<img src="https://img-blog.csdnimg.cn/7479f2a5b37e4a54bf1037d031c43895.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/799f964bc39c40aba03b7396e3572c9d.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/105b1988e95e4916b9af7da0f3f0d573.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/9686c399366540f5b96303e66f8a0154.png" alt="在这里插入图片描述">

### 配置字典

<img src="https://img-blog.csdnimg.cn/e2fc2a0755364a208f7fb984c6d977af.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d5c2ddfcd13c49da9a1f56397d8ef518.png" alt="在这里插入图片描述">

```
redis.conf

```

<img src="https://img-blog.csdnimg.cn/38c8c02e0b9a407f9f312146cb12a0ff.png" alt="在这里插入图片描述">

```
appendonly yes
port 6379
bind 0.0.0.0

```

**挂载字典** <img src="https://img-blog.csdnimg.cn/97bcaf10ad6341efb9a64df96b4fab7b.png" alt="在这里插入图片描述">

```
/etc/redis/redis.conf

redis.conf

```

### 配置存储

<img src="https://img-blog.csdnimg.cn/0609db1f03c54fd986dcaf120d019193.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/a4ad53e7c442498aac2eb50e6993e4dd.png" alt="在这里插入图片描述">

```
/data

```

### 完整配置图

<img src="https://img-blog.csdnimg.cn/ea94d53cef0a43eaaf2c7e05d9b44681.png" alt="在这里插入图片描述">

### 启动效果

<img src="https://img-blog.csdnimg.cn/27472f9e79454734be28f3f864a3b4e8.png" alt="在这里插入图片描述">
