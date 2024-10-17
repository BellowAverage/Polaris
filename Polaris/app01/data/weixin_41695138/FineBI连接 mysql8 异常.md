
--- 
title:  FineBI连接 mysql8 异常 
tags: []
categories: [] 

---
转载FineBI的文档 
1. 异常信息
<img src="https://img-blog.csdnimg.cn/64a362f2bfe6477786a305324174a7ae.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/fa19be04363b46cf8c83a7ffd73529dc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
java.sql.SQLException: Unable to load authentication plugin 'caching_sha2_password'.
at com.mysql.jdbc.SQLError.createSQLException(SQLError.java:868)
at com.mysql.jdbc.SQLError.createSQLException(SQLError.java:864)
at com.mysql.jdbc.MysqlIO.proceedHandshakeWithPluggableAuthentication(MysqlIO.java:1746)
at com.mysql.jdbc.MysqlIO.doHandshake(MysqlIO.java:1226)
at com.mysql.jdbc.ConnectionImpl.coreConnect(ConnectionImpl.java:2191)
at com.mysql.jdbc.ConnectionImpl.connectOneTryOnly(ConnectionImpl.java:2222)
at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2017)
at com.mysql.jdbc.ConnectionImpl.&lt;init&gt;(ConnectionImpl.java:779)
at com.mysql.jdbc.JDBC4Connection.&lt;init&gt;(JDBC4Connection.java:47)
at sun.reflect.GeneratedConstructorAccessor215.newInstance(Unknown Source)
at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
at java.lang.reflect.Constructor.newInstance(Constructor.java:423)
at com.mysql.jdbc.Util.handleNewInstance(Util.java:425)
at com.mysql.jdbc.ConnectionImpl.getInstance(ConnectionImpl.java:389)
at com.mysql.jdbc.NonRegisteringDriver.connect(NonRegisteringDriver.java:330)
at com.fr.third.alibaba.druid.pool.DruidAbstractDataSource.createPhysicalConnection(DruidAbstractDataSource.java:1461)
at com.fr.third.alibaba.druid.pool.DruidAbstractDataSource.createPhysicalConnection(DruidAbstractDataSource.java:1525)
at com.fr.third.alibaba.druid.pool.DruidDataSource$CreateConnectionThread.run(DruidDataSource.java:2153)	

```

连接信息： 数据连接名称：mysql_test 数据库名称：jdbc:mysql://localhost:3306/qinenqi?useUnicode=true&amp;characterEncoding=utf8 主机：localhost 端口: 3306 用户名：root 密码：root 数据连接URL：jdbc:mysql://localhost:3306/qinenqi?useUnicode=true&amp;characterEncoding=utf8
1. 解决方法， 替换成mysql8 的驱动 <img src="https://img-blog.csdnimg.cn/8f53b3b797f14ebfb0c0341c44646c53.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 找到jar 所在的目录； D:\tool\FineBI\fineBI\FineBI5.1\webapps\webroot\WEB-INF\lib 把mysql8的驱动复制至此 <img src="https://img-blog.csdnimg.cn/9800beb089d248f2b1c46989703e22b1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c673f7fdf085428a84a0afbab5231f5d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 把 com.mysql.cj.jdbc.Driver 复制到驱动上，数据库连接URL更改为 jdbc:mysql://localhost:3306/qinenqi?useUnicode=true&amp;characterEncoding=UTF-8&amp;useSSL=false&amp;serverTimezone=Asia/Shanghai&amp;allowPublicKeyRetrieval=true <img src="https://img-blog.csdnimg.cn/f7f167b4473a4ecdb9a97dba89bf1a98.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">