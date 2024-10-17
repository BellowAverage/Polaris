
--- 
title:  @RestController注入为空的排查方法 
tags: []
categories: [] 

---
我介绍一下我的思路：

1·如果你是注解开发可以看看引入注解是否是dubbo的别引错了

2·看看配置文件是否正常配置，比如注册中心地址、包扫描等。

3·检查调用的服务是否配置dubbo的Service

4·如果都正确可以切换一下方法比如使用注解的可以试一下xml配置。

5·因为spring的初始化问题经常导致@RestController注入为空大家可以参考一下下面的解释。

https://blog.csdn.net/zhou_java_hui/article/details/53039491
