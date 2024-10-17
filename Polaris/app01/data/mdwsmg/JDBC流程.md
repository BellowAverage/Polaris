
--- 
title:  JDBC流程 
tags: []
categories: [] 

---
**JDBC 使用要求加载相应jar包，所有语句自动commit** 推荐一篇超详细的JDBC原理和开发步骤  **具体流程** **1、加载驱动（注册驱动）** 这里推荐使用Class.forName()反射方法载入驱动，这样不会对详细驱动类产生依赖 连接Oracle

```
Class.forName("oracle.jdbc.driver.OracleDriver");

```

连接MySQL

```
Class.forName("com.mysql.jdbc.Driver");

```

**2、建立连接+创建连接对象** ****Connection**** 连接对象，用于与数据库取得连接 ****Driver**** 用于创建 Connection对象 getConnection(url,user,password); URL格式为 “子协议：自名称：//主机名：port/数据库名”

```
Connection coon=DriverManager.getConnection
("jdbc:mysql://localhost:3306/数据库名称","用户名称"，"密码");//mysql
("jdbc:mysql://127.0.0.1:3306/sms?characterEncoding=UTF-8", "root", "root");//我的
("jdbc:oracle:thin:@127.0.0.1:1521:orcl","scott","tiger");//oracle

```

**ps**:在句柄前，获得连接对象后，可以通过 conn.setAutoCommit(false);取消自动提交 //里面参数为boolean 配合conn.commit();conn.rollback()使用,以防止脏数据 

**3、执行SQL语句（对数据库发出请求/创建运行对象）** ****Statement/PreparedStatement**** 语句对象，用于执行sql语句

```
preparedStatement pstm = conn.prepareStatement(sql);//预编译

```

配合 pstm.setType(index,value);//设置预处理的sql语句的值

不知道具体类型是，用pstm.setObject(); 执行效率PreparedStatement&gt;Statement

```
Statement sta = conn.createStatement();

```

**ps:** CallableStatement接口实现了preparedStatement CallableStatement 储存过程语句对象，用于调用执行存储过程

**4、返回查询结果 **ResultSet 结果集****

```
ResultSet rs = pstm.executeQuery();||sta.executeQuery(sql);

```

executeQuery()用于查询功能的sql语句； executeUpdate()用于增、删、改；返回结果为Int execute();适用于所有情况，返回boolean

ps: ResultSetMetaData rsmd = rs.getMetaData(); 返回结果集的表结构对象

下面链接为三者区别 

**5、处理运行结果**

```
while(rs.next()){//rs.next()指向结果第一条
    rs.getType(index);||rs.getType("attributeName");
}

```

注意日期型数据，下面链接是日期型数据的处理 

**6、关闭连接** 顺序为 rs pstm conn

-----20210330 update----- 最近在做对接，发现一个很坑的地方。

需要在一个接口获取一些数据，然后需要在某一个时刻，根据这些数据获取其他数据。好办，给这些**要用到的数据**存起来就好了,然后就想到了csv文件

>  
 诶嘿，我先存起来，然后确定用不到了再删除。我简直是个天才。 


后来发现，尼玛，这不就是数据库的底层么……数据库文件。
