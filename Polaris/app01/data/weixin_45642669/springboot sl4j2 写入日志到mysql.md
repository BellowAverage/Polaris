
--- 
title:  springboot sl4j2 写入日志到mysql 
tags: []
categories: [] 

---
## 问题描述
- springboot初始化的时候，会先初始化日志然后再加载数据源- 如果用配置文件进行初始化，那么会出现数据源没有加载成功，导致空指针异常
报错排查如下：
- 搜索报错信息，OBjects.invoke is Null- 打断点发现。datasorce = null
## 解决方法
- 不使用文件配置数据源，而是使用ApplicationListener进行加载配置文件 这样的话就可以延迟database连接
实际方法如同链接： 

<img src="https://img-blog.csdnimg.cn/b0b74f016afb4f5c97d9fb77f9557b05.png" alt="在这里插入图片描述">

第二种方案：使用配置文件 <img src="https://img-blog.csdnimg.cn/877c86035346469a94630ae24a313ec0.png" alt="在这里插入图片描述"> 这样就可以不使用连接池

方案如下： 

第三种方式：单独初始化一个连接池。

但是定义两个连接池……有种代码的坏味道

文档如下： 
