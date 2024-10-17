
--- 
title:  0基础学习Mybatis系列数据库操作框架——最小Demo 
tags: []
categories: [] 

---


#### 大纲
- - - <ul><li>- <ul><li>- - - <ul><li>- - - <ul><li>- - - - <ul><li>- - 


在学习Java的过程中，一般都会学习到使用JDBC连接和操作数据库的知识。Mybatis则是JDBC的一个上层封装，它简化了驱动加载、创建连接等操作。我们只要按照规范配置几个文件、写几个Java类和按一定规则将这些配置文件通过代码的形式加以利用，即可完成数据库的相关操作。 这个系列我们将学习Mybatis以及基于它开发出的工具MybatisPlus。在这个探索的过程中，我们将依赖包的管理交给Maven去做，注意力主要集中在Mybatis相关技术的应用上。 这个案例将依赖于两个模块：
- 数据库- Mybatis
## 数据库

为了简单起见，我们使用部署的Mysql服务。然后使用下面指令创建包含各种类型字段的表

```
create database testdb;
use testdb;
create table all_type(
        info_int int(10) comment 'int',
        info_tint tinyint comment 'tinyint',
        info_sint smallint comment 'smallint',
        info_mint mediumint comment 'mediumint',
        info_bint bigint comment 'bigint',
        info_char varchar(100) comment 'char',
        info_ttext tinytext comment 'tinytext',
        info_text text comment 'text',
        info_mtext mediumtext comment 'mediumtext',
        info_ltext longtext comment 'longtext',
        info_blob blob comment 'blob',
        info_mblob mediumblob comment 'mediumblob',
        info_lblob longblob comment 'longblob',
        info_float float(8,1) comment 'float',
        info_double double(8,1) comment 'double',
        info_decimal decimal(10,2) comment 'decimal',
        info_date  date comment 'date',
        info_datetime datetime comment 'datetime',
        info_timestamp timestamp comment 'timestamp',
        info_time time comment 'time',
        info_year year(4) comment 'year'
        );

```

## Mybatis

我们需要按照Mybatis的规则来组织代码以及其结构。

### 目录结构

我们使用IntelliJ IDEA创建一个基于Maven的Java工程。 <img src="https://img-blog.csdnimg.cn/direct/fd2b29d26b3c4861a8ec911cec38306b.png#pic_center" alt="在这里插入图片描述"> 为了能使用Mybatis，我们需要对上述步骤创建的工程做如下的改进：

#### 配置
<li>新增配置。包含： 
  <ul>- 记录SQL的文件。这儿需要对Mybatis设计有一个初步认识——分离SQL语言和Java代码，即不要在Java代码中放置SQL语句，而在一个独立的配置文件中放置SQL。本例中该文件我们命名为AllTypeMapper.xml。- 包含数据库位置、用户名、密码以及指定SQL所在文件的文件名。本例中该文件我们命名为mybatis-config.xml。
#### 代码
- 新增代码。我们只要新增SQL结果映射的类即可，即Mybatis会将SQL返回的数据序列化为Java对象。本例中是com.all_type中的AlltType.java。- 修改代码。修改Main.java代码，利用上述配置以及Mybatis，达到查询数据库的效果。 <img src="https://img-blog.csdnimg.cn/direct/0019fb09772c4c33b6f5a29b4d743385.png#pic_center" alt="在这里插入图片描述">
### 代码/配置结构

#### 配置结构

##### 依赖库配置

在pom.xml中新增

```
    &lt;dependencies&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;com.mysql&lt;/groupId&gt;
            &lt;artifactId&gt;mysql-connector-j&lt;/artifactId&gt;
            &lt;version&gt;8.3.0&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.mybatis&lt;/groupId&gt;
            &lt;artifactId&gt;mybatis&lt;/artifactId&gt;
            &lt;version&gt;3.5.15&lt;/version&gt;
        &lt;/dependency&gt;
    &lt;/dependencies&gt;

```

com.mysql是数据库连接工具，org.mybatis是Mybatis。 完整配置如下，仅供参考

```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"&gt;
    &lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;

    &lt;groupId&gt;org.example&lt;/groupId&gt;
    &lt;artifactId&gt;mybatis_demo&lt;/artifactId&gt;
    &lt;version&gt;1.0-SNAPSHOT&lt;/version&gt;

    &lt;properties&gt;
        &lt;maven.compiler.source&gt;22&lt;/maven.compiler.source&gt;
        &lt;maven.compiler.target&gt;22&lt;/maven.compiler.target&gt;
        &lt;project.build.sourceEncoding&gt;UTF-8&lt;/project.build.sourceEncoding&gt;
    &lt;/properties&gt;

    &lt;dependencies&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;com.mysql&lt;/groupId&gt;
            &lt;artifactId&gt;mysql-connector-j&lt;/artifactId&gt;
            &lt;version&gt;8.3.0&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.mybatis&lt;/groupId&gt;
            &lt;artifactId&gt;mybatis&lt;/artifactId&gt;
            &lt;version&gt;3.5.15&lt;/version&gt;
        &lt;/dependency&gt;
    &lt;/dependencies&gt;

&lt;/project&gt;

```

使用Maven解析这个文件并把对应的库下载并部署，结果如下 <img src="https://img-blog.csdnimg.cn/direct/589f797e1d0d441cab129754dd793346.png" alt="在这里插入图片描述">

##### SQL配置

对应于本例中的AllTypeMapper.xml。 这个文件主要定义SQL语句以及其结果反射的Java类。

```
    &lt;select id="findAll" resultType="com.all_type.AllType"&gt;
        select * from all_type
    &lt;/select&gt;

```

id表示这个SQL的唯一标识；resultType是单个结果的类型（select返回的是一个数组，即多个该类型的结果集合）。 完整的配置如下

```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd"&gt;
&lt;mapper namespace="AllTypeMapper"&gt;
    &lt;select id="findAll" resultType="com.all_type.AllType"&gt;
        select * from all_type
    &lt;/select&gt;
&lt;/mapper&gt;

```

##### Mybatis配置

对应于本例中的mybatis-config.xml。 这个配置分为两部分。它们都定义在configuration下。

###### 数据库配置

数据库信息可以配置多个，用于表示不同的环境。所以最外层是environments标签。 单个的环境使用environment标签表示，并通过id来唯一标志。 transactionManager的type字段表示使用哪种事务管理器。可选项如下：
- JDBC。这个配置直接使用了 JDBC 的提交和回滚功能，它依赖从数据源获得的连接来管理事务作用域。默认情况下，为了与某些驱动程序兼容，它在关闭连接时启用自动提交。- MANAGED。这个配置几乎没做什么。它从不提交或回滚一个连接，而是让容器来管理事务的整个生命周期（比如 JEE 应用服务器的上下文）。 默认情况下它会关闭连接。
dataSource用于定义数据源。它的type也有两种类型，用于定义数据源的连接方式：
- UNPOOLED。这个数据源的实现会每次请求时打开和关闭连接。- POOLED。这种数据源的实现利用“池”的概念将 JDBC 连接对象组织起来，避免了创建新的连接实例时所必需的初始化和认证时间。
dataSource下的driver表示驱动程序名；url提供数据库连接信息；username和password分别表示数据库的用户名和密码。

```
    &lt;environments default="development"&gt;
        &lt;environment id="development"&gt;
            &lt;transactionManager type="JDBC"/&gt;
            &lt;dataSource type="POOLED"&gt;
                &lt;property name="driver" value="com.mysql.cj.jdbc.Driver"/&gt;
                &lt;property name="url" value="jdbc:mysql://localhost:3306/testdb?useSSL=true&amp;amp;useUnicode=true&amp;amp;characterEncoding=utf8"/&gt;
                &lt;property name="username" value="root"/&gt;
                &lt;property name="password" value="fangliang"/&gt;
            &lt;/dataSource&gt;
        &lt;/environment&gt;
    &lt;/environments&gt;

```

###### SQL映射配置

这儿可以定义一批SQL语句文件。

```
    &lt;mappers&gt;
        &lt;mapper resource="AllTypeMapper.xml"/&gt;
    &lt;/mappers&gt;

```

##### 完整配置

```
&lt;?xml version="1.0" encoding="UTF-8" ?&gt;
&lt;!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "https://mybatis.org/dtd/mybatis-3-config.dtd"&gt;
&lt;configuration&gt;
    &lt;environments default="development"&gt;
        &lt;environment id="development"&gt;
            &lt;transactionManager type="JDBC"/&gt;
            &lt;dataSource type="POOLED"&gt;
                &lt;property name="driver" value="com.mysql.cj.jdbc.Driver"/&gt;
                &lt;property name="url" value="jdbc:mysql://localhost:3306/testdb?useSSL=true&amp;amp;useUnicode=true&amp;amp;characterEncoding=utf8"/&gt;
                &lt;property name="username" value="root"/&gt;
                &lt;property name="password" value="fangliang"/&gt;
            &lt;/dataSource&gt;
        &lt;/environment&gt;
    &lt;/environments&gt;
    &lt;mappers&gt;
        &lt;mapper resource="AllTypeMapper.xml"/&gt;
    &lt;/mappers&gt;
&lt;/configuration&gt;

```

#### 代码结构

##### 映射类

对应于本例中的AllType.java。 为了简单起见，我们只定义了表中的第一个字段。注意字段名称一致。

>  
 info_int int(10) comment ‘int’, 


```
package com.all_type;

public class AllType {<!-- -->

    public int getInfo_int() {<!-- -->
        return info_int;
    }

    public void setInfo_int(int info_int) {<!-- -->
        this.info_int = info_int;
    }

    private int info_int;
}

```

这个映射类和SQL配置文件AllTypeMapper.xml的SQL语句块有关联，即resultType字段对应的值。

```
&lt;select id="findAll" resultType="com.all_type.AllType"&gt;
	select * from all_type
&lt;/select&gt;

```

##### Mybatis逻辑

这部分代码我们写在Main.java中。它需要按以下步骤执行：

###### 从 XML 中构建 SqlSessionFactory

```
InputStream in = Resources.getResourceAsStream("mybatis-config.xml");
SqlSessionFactory sqlSF = new SqlSessionFactoryBuilder().build(in);

```

###### 从 SqlSessionFactory 中获取 SqlSession

```
SqlSession s = sqlSF.openSession();

```

###### 通过mapper中的namespace和id执行SQL

```
List&lt;AllType&gt; all = s.selectList("AllTypeMapper.findAll");

```

##### 完整逻辑和代码

<img src="https://img-blog.csdnimg.cn/direct/e94b9df0627047978da8f61cb919a551.png" alt="在这里插入图片描述">

```
package org.example;

import com.all_type.AllType;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.*;

import java.io.InputStream;
import java.util.List;

public class Main {<!-- -->
    public static void main(String[] args) {<!-- -->
        try {<!-- -->
            InputStream in = Resources.getResourceAsStream("mybatis-config.xml");
            SqlSessionFactory sqlSF = new SqlSessionFactoryBuilder().build(in);
            List&lt;AllType&gt; all;
            try (SqlSession s = sqlSF.openSession()) {<!-- -->
                all = s.selectList("AllTypeMapper.findAll");
            }
            for (AllType a : all) {<!-- -->
                System.out.println(a.getInfo_int());
            }
        } catch (Exception e) {<!-- -->
            System.out.println(e.getMessage());
        }
    }
}

```

## 参考资料
- 