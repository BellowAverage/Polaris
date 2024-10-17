
--- 
title:  sa账号密码在那个表里面 
tags: []
categories: [] 

---
sa账号密码在那个表里面，syslogins in master db, 不过是加密的，看不出是什么的。

SA管理帐户是放在视图下的、master数据库-视图-sys.sql_logins<img alt="" height="452" src="https://img-blog.csdnimg.cn/3dbf1dc87ca04e3bb92e3704e81bff3a.png" width="969">

 

sqlserver怎么查看sa密码？

查看sqlserver sa密码的方法与步骤：

1，改用windows身份登录系统，不需要密码<img alt="" height="207" src="https://img-blog.csdnimg.cn/892102ca70f34639a75d13eeb3c8a7fa.png" width="519">

2，进入sqlserver2005后，在服务名上单击右键选择属性，在安全性中选sql server和windows身份模式，单击确定<img alt="" height="242" src="https://img-blog.csdnimg.cn/4901f87eb89e443db712e329faa9eba9.png" width="520"> 

 

SQL Server2005中的新安全模式将用户和对象分开，提供fine-grainAccess存取、并允许对数据存取进行更大的控制。另外，所有系统表格将作为视图得到实施，对数据库系统对象进行了更大程度的控制。

SQL Server2005为开发可升级的数据库应用软件，提供了新的语言功能。这些增强的性能包括处理错误、递归查询功能、关系运算符PIVOT，APPLY，ROW_NUMBER和其他数据列排行功能。

使用SQL Server2005，开发人员将能够在数据库层开发Web服务，将SQL Server当作一个超文本传输协议(HTTP)侦听器，并且为网络服务中心应用软件提供一个新型的数据存取功能。  
