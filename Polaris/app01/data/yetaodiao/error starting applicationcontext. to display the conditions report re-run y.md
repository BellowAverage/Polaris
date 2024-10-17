
--- 
title:  error starting applicationcontext. to display the conditions report re-run y 
tags: []
categories: [] 

---
出现主要错误：

>  
 Failed to configure a DataSource: 'url' attribute is not specified and no embedded datasource could be configured. 


未能配置数据源:未指定“url”属性，也无法配置嵌入式数据源。

复制代码如下：

```
Error starting ApplicationContext. To display the conditions report re-run your application with 'debug' enabled.
2019-06-03 09:47:45.300 ERROR 23160 --- [           main] o.s.b.d.LoggingFailureAnalysisReporter   : 
 
***************************
APPLICATION FAILED TO START
***************************
 
Description:
 
Failed to configure a DataSource: 'url' attribute is not specified and no embedded datasource could be configured.
 
Reason: Failed to determine a suitable driver class
 
 
Action:
 
Consider the following:
    If you want an embedded database (H2, HSQL or Derby), please put it on the classpath.
    If you have database settings to be loaded from a particular profile you may nee
```
