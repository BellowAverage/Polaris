
--- 
title:  mysql5升级mysql8无法通过jdbc连接的几个原因 
tags: []
categories: [] 

---
#### mysql8 jdbc加了一个必选的参数：

```
jdbc:mysql://127.0.0.1:3306/test?characterEncoding=utf8&amp;useSSL=false

```

useSSL=true或者useSSL=false，而且必须要指定。 当数据库从低版本迁移到高版本的时候会因为没有这个参数而报错。 这个参数的默认值是false。  

#### mysql8必须指时区。不然会报错有多个时区无法连接。加上下面参数才能够进行JDBC连接

```
serverTimezone=Asia/Shanghai

```

 

#### 如果是Java的话，导入的第三方依赖里面有：

```
        &lt;dependency&gt;
            &lt;groupId&gt;mysql&lt;/groupId&gt;
            &lt;artifactId&gt;mysql-connector-java&lt;/artifactId&gt;
            &lt;version&gt;8.0.11&lt;/version&gt;
        &lt;/dependency&gt;

```

这个版本可能过老会导致数据无法连接。  

#### 新老版本Driver路径不同

在老版本使用JDBC用的是com.mysql.jdbc.Driver这个包。 但是新版本（5以后的版本）是用的com.mysql.cj.jdbc.Driver。 需要将Driver进行修改，才能够实现连接
