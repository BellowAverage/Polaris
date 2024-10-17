
--- 
title:  KubeSphere 部署 elasticsearch kibana 
tags: []
categories: [] 

---
### KubeSphere 部署 elasticsearch

### 创建 elasticsearch 的配置
1. 创建1. 基本配置 <img src="https://img-blog.csdnimg.cn/fe6b314e54854d3fa57e01fd58c5a79a.png" alt="在这里插入图片描述">1. 配置设置 ： http.host: 0.0.0.0 discovery.type:single-node ES_JAVA_OPTS=“-Xms300m -Xmx300m” <img src="https://img-blog.csdnimg.cn/0ea8e6d9d8074fb6a475ea98ead57319.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c0ac30dbc2604922af8d569a28f515b0.png" alt="在这里插入图片描述">
<img src="https://img-blog.csdnimg.cn/a27ebf7000994bba97ee87febf9a34d5.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/cff5f8fa27c0489fba40d75484911709.png" alt="在这里插入图片描述"> 4. 点击对号 – 创建 <img src="https://img-blog.csdnimg.cn/0af9a1b7382448cc887232aca6da78c4.png" alt="在这里插入图片描述">

### 创建 elasticsearch 的存储卷
1. 点击创建 <img src="https://img-blog.csdnimg.cn/d5ce02bb2f204934a6aefc3ba5ab07b5.png" alt="在这里插入图片描述">1. 基本信息： elasticsearch-pvc， 点击下一步， 存储卷设置和高级设置都是默认的，下一步 下一步 创建即可 **<img src="https://img-blog.csdnimg.cn/1c8478273df941f5af68990de1614120.png" alt="加粗样式"> **1. 创建成功 <img src="https://img-blog.csdnimg.cn/5472149a384344a392b43fee6b056d32.png" alt="在这里插入图片描述">
### 创建 elasticsearch 服务
1. 创建 <img src="https://img-blog.csdnimg.cn/38f554410886434eaf0ca39c40420527.png" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/1847403867e5471db3c094d64bd1423c.png" alt="在这里插入图片描述">1. 基本信息配置 <img src="https://img-blog.csdnimg.cn/f46688ad15474fbca73cf62631082d84.png" alt="在这里插入图片描述">1. 容器镜像 <img src="https://img-blog.csdnimg.cn/2196e66e2c564576a122a905e6c90774.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/9a97abd835cf441aac7737da0f32b73a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/25a8208e695c4ef190224d299ba218ee.png" alt="在这里插入图片描述">1. 挂载储存配置， 配置存储卷 <img src="https://img-blog.csdnimg.cn/55225d736a05417cace4c50f1f8e1d92.png" alt="在这里插入图片描述">1. 下一步 创建 <img src="https://img-blog.csdnimg.cn/9546495141ec45ed99a400acca6d576e.png" alt="在这里插入图片描述">
### kubesphere 部署 kibana
1. 创建 无状态的 kibana <img src="https://img-blog.csdnimg.cn/60ee673f2fea451cab096c5999902c8a.png" alt="在这里插入图片描述">1. 拉取 kibana:7.4.2 的镜像 <img src="https://img-blog.csdnimg.cn/4a43b308f7b04980814cad1d86e5cc2a.png" alt="在这里插入图片描述">_配置环境： ELASTICSEARCH_HOSTS： http://elasticsearch.demo-project:9200 <img src="https://img-blog.csdnimg.cn/1e74d6a24fa64988b5bcc4ac6d15df94.png" alt="在这里插入图片描述">1. 配置外网访问 <img src="https://img-blog.csdnimg.cn/6ba61982afa94ae080188b00b14eda08.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e4e4ecc6ef9b434583020f7ab8bc03c9.png" alt="在这里插入图片描述">1. 访问 kibana 服务： http://192.168.8.106:30070/ <img src="https://img-blog.csdnimg.cn/95293260a57e4c2289f7dcbab8753cce.png" alt="在这里插入图片描述">