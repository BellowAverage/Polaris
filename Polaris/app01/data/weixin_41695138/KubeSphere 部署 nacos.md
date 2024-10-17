
--- 
title:  KubeSphere 部署 nacos 
tags: []
categories: [] 

---
### KubeSphere 部署 nacos

### 创建nacos的pvc
1. 点击创建 <img src="https://img-blog.csdnimg.cn/1ea3d00b3d9640d8b663fb977d355d05.png" alt="在这里插入图片描述">1. 基本信息配置 <img src="https://img-blog.csdnimg.cn/44d2a8ce519b483fbea33ff6a0c1a9fc.png" alt="在这里插入图片描述">1. 点击下一步 下一步 创建，创建成功 <img src="https://img-blog.csdnimg.cn/3ffca8fa79354bb79f3718a5fbba2f64.png" alt="在这里插入图片描述">
### 创建 nacos 的服务： nacos
1. 点击创建 <img src="https://img-blog.csdnimg.cn/1d32d439f2bf4680ab2fdd36667a40d3.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d9f1dcea250f428fa8d5cc3305c46383.png" alt="在这里插入图片描述">1. 基本信息配置：nacos <img src="https://img-blog.csdnimg.cn/47c2f136555f45be83296d8b9a651240.png" alt="在这里插入图片描述">1. 容器镜像配置： nacos/nacos-server:1.1.4 <img src="https://img-blog.csdnimg.cn/7b194ec525b94481be261aa99eb19ee0.png" alt="在这里插入图片描述"> 配置环境变量， 配置环境变量后，点击对号，点击下一步 <img src="https://img-blog.csdnimg.cn/3894d205c2f547488fd191021d176370.png" alt="在这里插入图片描述">1. 挂载存储配置： /home/nacos/data, 点击对号，点击下一步， 点击创建 <img src="https://img-blog.csdnimg.cn/e07dcc8ff5b245ee90bfa8eed2364946.png" alt="在这里插入图片描述">1. 创建成功 <img src="https://img-blog.csdnimg.cn/2aad1fa7a879411ea61142cbb7c17556.png" alt="在这里插入图片描述">
### 删除nacos服务
1. 删除该有状态的nacos服务， **但是不要删除该服务对应的容器组** <img src="https://img-blog.csdnimg.cn/0409941ec3af4506a666226b7520d1af.jpeg" alt="在这里插入图片描述">
### 创建一个对外暴露端口的nacos， 前提是要先删除nacos服务，请参考（上一步的删除nacos服务）
1. 点击创建， 点击指定工作负载 <img src="https://img-blog.csdnimg.cn/db3bc63b58be4b748dd6914273cbf713.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/88f4c41cbcd8459289220371ff30a3c1.png" alt="在这里插入图片描述">1. 基本信息配置 nacos-foreign， 点击下一步 <img src="https://img-blog.csdnimg.cn/599007cec5f84824a03a09a2fbe295b0.png" alt="在这里插入图片描述">1. 服务配置 <img src="https://img-blog.csdnimg.cn/15328e9e0712408ca6c2ac5e0c1668fa.png" alt="在这里插入图片描述"> 指定访问类型与端口 <img src="https://img-blog.csdnimg.cn/07b62f1e4aea489f8252a670a5e7ca91.png" alt="在这里插入图片描述">1. 高级设置，配置外网访问， 点击创建 <img src="https://img-blog.csdnimg.cn/149090018cec425bbb18a6451da03a6d.png" alt="在这里插入图片描述">1. 创建成功 <img src="https://img-blog.csdnimg.cn/c883ecf7531d4387800eaad067b6c68b.png" alt="在这里插入图片描述">1. 访问地址： <img src="https://img-blog.csdnimg.cn/18061a5476b74a848ac56bbc629c9329.png" alt="在这里插入图片描述">1. 默认用户名密码（nacos nacos） <img src="https://img-blog.csdnimg.cn/276ffc5a76fd4639810060c5004d3a5a.png" alt="在这里插入图片描述">