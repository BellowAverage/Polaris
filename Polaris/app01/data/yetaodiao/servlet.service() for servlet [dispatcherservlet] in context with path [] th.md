
--- 
title:  servlet.service() for servlet [dispatcherservlet] in context with path [] th 
tags: []
categories: [] 

---
.Servlet.service() for servlet [dispatcherServlet] in context with path [] threw exception [Request processing failed; nested exception is org.springframework.web.client.ResourceAccessException: I/O error on GET request for "http://localhost/8081:user/1": Connection refused: connect; nested exception is java.net.ConnectException: Connection refused: connect] with root cause java.net.ConnectException: Connection refused: connect

是因为：Servlet.service服务（对于路径为[]的上下文中的servlet[dispatcherServlet]，引发了异常[请求处理失败；嵌套异常为java.lang.NullPointerException]有根本原因

<img alt="" height="179" src="https://img-blog.csdnimg.cn/65cacde6ade94bb29aa9ce694e2344bc.png" width="932">

 

原因：

说明是上面url引发的错误（可能url不存在，所跳转的url可能与web项目的root路径（一般是项目名）冲突）；

所以检查自己的url是否配对噢。 另外一个**解决办法：启动类配置包扫描使能够扫描到common包下的bean即可。**
