
--- 
title:  springboot项目热部署 
tags: []
categories: [] 

---
快捷键Ctrl + Alt + Shift + / 选Registry 勾选下面这个 <img src="https://img-blog.csdnimg.cn/5079471a8c9a4436b2cbf1846688e1a5.png" alt="在这里插入图片描述"> 然后 <img src="https://img-blog.csdnimg.cn/f23f8351c832456c8a85f7f1884c8bee.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/884a726385134b8cbd29a2814bf0e30a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/3c9b556042e44d00bfd26dd69dd9d652.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d76fa9bea308489eb816547650d1cb45.png" alt="在这里插入图片描述"> apply一下

pom.xml

```
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-devtools&lt;/artifactId&gt;
            &lt;version&gt;2.5.1&lt;/version&gt;
        &lt;/dependency&gt;

```

application.properties(yml,yaml)

```
#springdevtools
spring.devtools.restart.enabled=true

```
