
--- 
title:  SonarQube 创建 Token 
tags: []
categories: [] 

---
SonarQube 创建 Token Spring Boot项目构建流水线任务地址：https://v2-1.docs.kubesphere.io/docs/zh-CN/quick-start/devops-online/
1. 基于Spring Boot项目构建流水线任务时，遇到了SonarQube 创建 Token，因为官方文档不全，因此，在此记录一下创建过程1. 创建 SonarQube Token 地址：https://v2-1.docs.kubesphere.io/docs/zh-CN/devops/sonarqube/ 第一步：在服务器上输入：kubectl get svc --all-namespaces ，查看SonarQube 对外暴露的端口 <img src="https://img-blog.csdnimg.cn/5a884a3e15d9415eaed9d196eb92c86a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/140ab330b45e4d7f90feeaa00a9e5e73.png" alt="在这里插入图片描述"> 因此小编的访问地址： http://192.168.8.106:31933 <img src="https://img-blog.csdnimg.cn/2d3d0f29ed4f47e78a1d1df8525ea75a.jpeg" alt="在这里插入图片描述"> 点击登录：输入 admin/admin <img src="https://img-blog.csdnimg.cn/e29d713033364691a8ab7766041e1ba6.jpeg" alt="在这里插入图片描述"> 剩下的步骤，根据官方文档操作即可，地址：https://v2-1.docs.kubesphere.io/docs/zh-CN/devops/sonarqube/1. 创建的sonar-token： <img src="https://img-blog.csdnimg.cn/6836cc9f4c3645639911454c40c8b22e.png" alt="在这里插入图片描述">