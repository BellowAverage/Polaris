
--- 
title:  [项目排错]SpringBoot项目 application.yml文件不生效 
tags: []
categories: [] 

---


#### SpringBoot配置文件
- - 


## 修改配置文件后项目未识别——添加指定配置

**前情提要**：因为网上抄作业的原因（懒），需要在存在application.properties的情况下再创建一个application.yml。结果**项目没有识别出yml文件**

>  
 yml与properties同时存在，yml先加载，properties后加载并覆盖yml中相同配置。 


讲道理，spring-boot-starter依赖中有SnakeYAML库作为YAML格式文件的解析器。这不应该。不知道为什么。但是快速解决，选择项目——&gt;右键——&gt;F4(open module settings)—&gt;Customize,自己手动添加一个。 <img src="https://img-blog.csdnimg.cn/20210225110349263.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210322114525991.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 搞定。 当然，只是练手的小项目，实际工作应该不可以这样瞎搞。不好环境管理与配置查找吧

>  
 PS：win10, idea版本2020 


## 配置文件ICON为“A”

可能是被解析成 Ansible 文件了，在Setting——&gt;File types 中，yaml项添加相应匹配。 <img src="https://img-blog.csdnimg.cn/2b90856232eb4673ac156df55fc0bad3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2g5aW977yM5pG45LqG5LmI,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 而后再指定配置即可。
