
--- 
title:  springcloud整合sentinel 
tags: []
categories: [] 

---
springcloud整合sentinel
1. 启动 sentinel： java -jar sentinel-dashboard-1.6.3.jar --server.port=8888 <img src="https://img-blog.csdnimg.cn/996d7d336410494c8dcee270341c0810.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/877a59fccaf54a18908fa17dad4bd621.png" alt="在这里插入图片描述"> 指定了sentinel 控制台的端口为88881. 访问： http://127.0.0.1:8888/#/login 用户名 密码 ：sentinel sentinel <img src="https://img-blog.csdnimg.cn/dc2ad4afe28e4afaafb5fda606ad28ef.png" alt="在这里插入图片描述">1. 项目中引入依赖
```
    &lt;dependencyManagement&gt;
        &lt;dependencies&gt;

            &lt;dependency&gt;
                &lt;groupId&gt;com.alibaba.cloud&lt;/groupId&gt;
                &lt;artifactId&gt;spring-cloud-alibaba-dependencies&lt;/artifactId&gt;
                &lt;version&gt;2021.0.1.0&lt;/version&gt;
                &lt;type&gt;pom&lt;/type&gt;
                &lt;scope&gt;import&lt;/scope&gt;
            &lt;/dependency&gt;
        &lt;/dependencies&gt;
    &lt;/dependencyManagement&gt;
       
        &lt;!-- SpringCloud Alibaba Sentinel --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;com.alibaba.cloud&lt;/groupId&gt;
            &lt;artifactId&gt;spring-cloud-starter-alibaba-sentinel&lt;/artifactId&gt;
        &lt;/dependency&gt;

```
1. 添加配置：
```
spring:
  cloud:
    sentinel:
      # 取消控制台懒加载
      eager: true
      transport:
        # 控制台地址
        dashboard: 127.0.0.1:8888

```

<img src="https://img-blog.csdnimg.cn/8efbe378c60d40d8a386f6499159a92a.png" alt="在这里插入图片描述">
