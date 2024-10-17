
--- 
title:  Dockerfile-个人笔记 
tags: []
categories: [] 

---
### 设置时区

```
#定义时区参数
ENV TZ=Asia/Shanghai

#设置时区
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime &amp;&amp; echo '$TZ' &gt; /etc/timezone


```

### 指定使用utf-8编码运行

```
# 设置编码
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

```
