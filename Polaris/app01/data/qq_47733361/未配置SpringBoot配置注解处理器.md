
--- 
title:  未配置SpringBoot配置注解处理器 
tags: []
categories: [] 

---
如果出现了下面图片中的问题，那可能是你没有引入相关依赖。 <img src="https://img-blog.csdnimg.cn/7554f282c75e4582b9c505f6b64d6d6a.png" alt="在这里插入图片描述"> 在 pom.xml 文件中添加如下依赖项：

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-configuration-processor&lt;/artifactId&gt;
    &lt;optional&gt;true&lt;/optional&gt;
&lt;/dependency&gt;

```

解决问题！！！！
