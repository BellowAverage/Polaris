
--- 
title:  KubeSphere 部署 rabbitmq 
tags: []
categories: [] 

---
### KubeSphere 部署 rabbitmq
1. 创建 rabbitmq 的pvc: rabbitmq-pvc <img src="https://img-blog.csdnimg.cn/bae9f19abc5a4b789f501278ece93410.png" alt="在这里插入图片描述">1. 基本信息配置， 点击下一步， 下一步， 创建 <img src="https://img-blog.csdnimg.cn/dc2caaf240ac416283621eeca12c447d.png" alt="在这里插入图片描述">1. 创建成功 <img src="https://img-blog.csdnimg.cn/992f300a8d9f42d2a478934ba452ef7b.png" alt="在这里插入图片描述">
### 创建 rabbitmq 的有状态服务： rabbitmq:management
1. 点击创建， 创建一个有状态的服务 <img src="https://img-blog.csdnimg.cn/eaf973f1afa24b9aabf705a697d5ae73.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/6db3e541835c4830878f56df8c437fea.png" alt="在这里插入图片描述">1. 基本信息配置 ： rabbitmq-management， 点击下一步 <img src="https://img-blog.csdnimg.cn/d04d966818d843659a3af22d9d844ed0.png" alt="在这里插入图片描述">1. 容器镜像配置： rabbitmq:management， 配置完了之后点击对号，点击下一步 <img src="https://img-blog.csdnimg.cn/d372c3ecdeb4449ba76212d90f90ddc5.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/a19ea58c15d14c9d8127ec8f658e9c37.png" alt="在这里插入图片描述">1. 挂载存储配置： /var/lib/rabbitmq 点击存储卷配置，配置好了之后，点击对号，点击下一步， 点击创建 <img src="https://img-blog.csdnimg.cn/1e62de125d314b4e9cd9b3ce7ccd18f7.png" alt="在这里插入图片描述">1. 创建成功 <img src="https://img-blog.csdnimg.cn/a64da91f847440afb734839b95740358.png" alt="在这里插入图片描述">