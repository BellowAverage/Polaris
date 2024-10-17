
--- 
title:  kettle连接mysql8 异常 
tags: []
categories: [] 

---1. 错误1： <img src="https://img-blog.csdnimg.cn/7075193a011147f79f47972082c85972.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/656ddd0f8d5e473d9731659698adf93f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 错误连接数据库 [mysql_kettle_demo] : org.pentaho.di.core.exception.KettleDatabaseException: Error occurred while trying to connect to the database
Driver class ‘org.gjt.mm.mysql.Driver’ could not be found, make sure the ‘MySQL’ driver (jar file) is installed. org.gjt.mm.mysql.Driver 分析原因是缺少jar包，因此把jar放入了lib中，小编的数据库版本是：8.0.20 <img src="https://img-blog.csdnimg.cn/570c6de67f54464f984976cc2d8b6fa6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 2. 重启 kettle, 再测试连接 <img src="https://img-blog.csdnimg.cn/daa5cdb3bc3f48ff87cfd294425e00e9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 异常信息： Driver class ‘org.gjt.mm.mysql.Driver’ could not be found, make sure the ‘MySQL’ driver (jar file) is installed. org.gjt.mm.mysql.Driver 3. 后来参考  修改data-integration\simple-jndi路径下的jdbc.properties配置文件

```
MYSQL8_DB/type=javax.sql.DataSource
MYSQL8_DB/driver=com.mysql.cj.jdbc.Driver
MYSQL8_DB/url=jdbc:mysql://192.168.8.171:3306/kettle?useUnicode=true&amp;characterEncoding=utf8&amp;useSSL=false&amp;serverTimezone=GMT
MYSQL8_DB/user=root
MYSQL8_DB/password=root

```

<img src="https://img-blog.csdnimg.cn/2224a367d23d4dd9bc40081ebbd5e8e3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 重启kettle,继续测试之,连接成功 <img src="https://img-blog.csdnimg.cn/6d07f6f68e014c96918da88c399380df.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
