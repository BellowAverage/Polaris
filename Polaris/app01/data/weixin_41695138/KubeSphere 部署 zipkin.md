
--- 
title:  KubeSphere 部署 zipkin 
tags: []
categories: [] 

---
### KubeSphere 部署 zipkin
1. 创建无状态服务 zipkin <img src="https://img-blog.csdnimg.cn/eceb76d90a57487a934265a3cc4fe8ef.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/396b745ad8d54cc38b1891006ab554df.png" alt="在这里插入图片描述">1. 基本信息配置， 点击下一步 <img src="https://img-blog.csdnimg.cn/a2eba95107de49bf82eb278cda93f7a4.png" alt="在这里插入图片描述">1. 容器镜像配置： openzipkin/zipkin <img src="https://img-blog.csdnimg.cn/a5bdd683d8b64ea7b69490ab92a12bba.png" alt="在这里插入图片描述"> 配置环境变量： STORAGE_TYPE=elasticsearch ES_HOSTS=elasticsearch.demo-project:9200， 配置之后，点击对号，点击下一步 <img src="https://img-blog.csdnimg.cn/49ec2fc3cdda4ed9a0dbd609ac0cb8db.png" alt="在这里插入图片描述"> 4， 点击下一步。设置外网访问， 点击创建 <img src="https://img-blog.csdnimg.cn/fe8fa84f7c8c4ccca2d8a17bf2e88636.png" alt="在这里插入图片描述">1. 创建成功 <img src="https://img-blog.csdnimg.cn/e887f7db621143e6825eb0150a543e5e.png" alt="在这里插入图片描述">1. 外网访问： http://192.168.8.106:31290 <img src="https://img-blog.csdnimg.cn/e93550d0d35346c0bec0d35657f3a4c5.png" alt="在这里插入图片描述">