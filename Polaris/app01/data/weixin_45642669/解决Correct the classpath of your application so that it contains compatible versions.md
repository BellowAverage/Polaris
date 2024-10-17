
--- 
title:  解决Correct the classpath of your application so that it contains compatible versions 
tags: []
categories: [] 

---- springboot启动失败- 报错Correct the classpath of your application so that it contains compatible versions of the classes org.springframework.web.servlet.handler.AbstractHandlerMethodMapping and org.springframework.web.method.HandlerMethod
排查发现：pom依赖同时引用了两个不同版本的web包。

<img src="https://img-blog.csdnimg.cn/4094a67c7b634a9f82c95d3c70675ae4.png" alt="在这里插入图片描述">

删掉一个web依赖重新构建以后问题直接解决。

Correct the classpath of your application so that it contains compatible versions of the classes org.springframework.web.servlet.handler.AbstractHandlerMethodMapping and org.springframework.web.method.HandlerMethod

某个类构建失败，删掉target重新构建
