
--- 
title:  KubeSphere 部署 redis 
tags: []
categories: [] 

---
KubeSphere 部署 redis

### 创建redis配置
1. 点击创建按钮 <img src="https://img-blog.csdnimg.cn/4dded79aeac24649bf85e6637bc1ecaf.png" alt="在这里插入图片描述">1. redis的基本信息配置 <img src="https://img-blog.csdnimg.cn/04eb200b54b64afda142692a8f79bfdc.png" alt="在这里插入图片描述">1. redis 的配置设置， 点击对号，点击创建 <img src="https://img-blog.csdnimg.cn/cd8b867b64d9491dac0990ecaad8f06f.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/820ec085d08f4427bfa073c45975d11f.png" alt="在这里插入图片描述">1. redis配置创建成功 <img src="https://img-blog.csdnimg.cn/1d560284d92a49888e4128e881696f6a.png" alt="在这里插入图片描述">
### 创建redis的pvc
1. 点击创建 <img src="https://img-blog.csdnimg.cn/dd3a687cb1984100b205b2b8a10eadc7.png" alt="在这里插入图片描述">1. 基本信息配置 <img src="https://img-blog.csdnimg.cn/232ac62f01df4d0abded1c5ab1bf53c7.png" alt="在这里插入图片描述">1. 存储卷设置， 点击下一步—&gt; 创建 <img src="https://img-blog.csdnimg.cn/bebcca34c3f54543a3c2c8a4bb98818f.png" alt="在这里插入图片描述">1. 创建成功 <img src="https://img-blog.csdnimg.cn/a16c588d479341998fb7ceea88f27993.png" alt="在这里插入图片描述">
### 创建redis有状态服务
1. 点击创建按钮 <img src="https://img-blog.csdnimg.cn/ddac2144e3594a19baf9c3946a031176.png" alt="在这里插入图片描述">1. 选择有状态服务， 配置基本信息 <img src="https://img-blog.csdnimg.cn/04bf6c9b7aea4f6cb64af75ba0a4c6d7.png" alt="在这里插入图片描述">1. 容器镜像配置：redis:5.0.7， 点击使用默认端口 <img src="https://img-blog.csdnimg.cn/ab00aec9264b41a6ae4cfc9cae378c5f.png" alt="在这里插入图片描述"> redis的启动命令： redis-server redis的参数为：/etc/redis/redis.conf <img src="https://img-blog.csdnimg.cn/cc20fdc7cae940ca8fc30a6a1801ab9e.png" alt="在这里插入图片描述">1. 挂载存储 <img src="https://img-blog.csdnimg.cn/a1372917a6b043bc8a9fc4358e18711a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d5cdeee9cd56498ca6f586f5e13447bf.png" alt="在这里插入图片描述"> 挂载文件配置 <img src="https://img-blog.csdnimg.cn/36efc968454647a58dd187d682231c55.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/9ea92fc9cfb24a6eb0e265a89dbe9e01.png" alt="在这里插入图片描述">1. 点击下一步，创建 —&gt; 创建成功 <img src="https://img-blog.csdnimg.cn/e25a3e3271394a02b8659d5f5be0415d.png" alt="在这里插入图片描述">