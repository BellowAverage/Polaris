
--- 
title:  Mybatis配置第一个sql和一些细节 
tags: []
categories: [] 

---
今天第一次配置成功Mybatis，配置的吐血。用了大概4个小时。 我百分百过了几个小时以后忘了，直接记录一下备查。

#### 登陆Mybatis

官网：https://mybatis.org/mybatis-3/

官网有中文，说的是比较简略的。

除了mybatis以外需要下载链接器和测试。

#### 导入POM依赖

在pom.xml里面写入依赖并刷新，即可导入需要的内容，我用的是：

```
		&lt;dependency&gt;
            &lt;groupId&gt;mysql&lt;/groupId&gt;
            &lt;artifactId&gt;mysql-connector-java&lt;/artifactId&gt;
            &lt;version&gt;5.1.46&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;junit&lt;/groupId&gt;
            &lt;artifactId&gt;junit&lt;/artifactId&gt;
            &lt;version&gt;4.12&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
            &lt;scope&gt;test&lt;/scope&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.mybatis&lt;/groupId&gt;
            &lt;artifactId&gt;mybatis&lt;/artifactId&gt;
            &lt;version&gt;3.5.9&lt;/version&gt;
        &lt;/dependency&gt;

```

刷新以后，测试连接数据库。

#### 修改pom中对于xml的过滤规则

默认情况下，只有resource里面的文件才能够对代码进行构建，不然代码无法注入。

有两个选择：
1. 所有的mapper.xml文件都写入到resource里面。1. 修改系统配置pom.xml文件，加入这么一行
```
&lt;resources&gt;
            &lt;resource&gt;
                &lt;includes&gt;
                    &lt;include&gt;**/*.xml&lt;/include&gt;
                &lt;/includes&gt;
            &lt;/resource&gt;
&lt;/resources&gt;

```

这个意思是：所有xml格式的文件通过过滤。

#### 新建mybatis config文件

我是直接用的：https://blog.csdn.net/banmingi/article/details/90407700这篇文章的，这篇文章很正。

mysql5以后的版本可能需要时区、SSL和其他详细的配置才能够连接，普通的jdbc:mysql://localhost:3306会连接失败。

新建一个配置文件，文件名随意（我指定的是Mybatis-config.xml）直接输入jdbc、用户和密码即可。

```
&lt;?xml version="1.0" encoding="UTF-8" ?&gt;
&lt;!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd"&gt;
&lt;configuration&gt;
    &lt;environments default="text"&gt;
        &lt;environment id="text"&gt;
            &lt;transactionManager type="JDBC"/&gt;
            &lt;dataSource type="POOLED"&gt;
                &lt;property name="driver" value="com.mysql.jdbc.Driver"/&gt;
                &lt;property name="url" value="jdbc:mysql://localhost:3306/s1?characterEncoding=utf8&amp;amp;useSSL=false&amp;amp;serverTimezone=UTC&amp;amp;rewriteBatchedStatements=true"/&gt;
                &lt;property name="username" value="root"/&gt;
                &lt;property name="password" value="123456"/&gt;
            &lt;/dataSource&gt;
        &lt;/environment&gt;
    &lt;/environments&gt;
&lt;/configuration&gt;

```

****由于在XML里面会对&amp;进行转义，所以修改&amp;为转义以后的****。

需要加入时区。jdbc中的s1即为数据库类型。

#### 开启工厂函数

```
public class Main {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        String resource = "Mybatis-config.xml";
        InputStream inputStream = Resources.getResourceAsStream(resource);
        SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
        SqlSession sqlSession = sqlSessionFactory.openSession();
    }
}

```

按照官方的说法：只需要构造一次，而且只定义一次。工厂函数会解决这个问题，不要定义多次。

第二个问题：要保证xml文件在target存在。不然会报错。

#### 构造返回类（实际类）

比如说：

```
CREATE TABLE `t1` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `grade` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8

```

写入测试数据：

```
insert into s1.t1 values(1, 1, 1);

```

为了储存这个数据，需要构造一个类。（我用的是pojo，组件类）,实现get、set方法和toString。

```
package com.demo3.pojo;

public class t1 {
    int id;
    String name;
    int grade;

    public int getId() {
        return id;
    }

    @Override
    public String toString() {
        return "select1{" +
                "id=" + id +
                ", name=" + name +
                ", grade=" + grade +
                '}';
    }

    public String getName() {
        return name;
    }

    public int getGrade() {
        return grade;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setGrade(int grade) {
        this.grade = grade;
    }

    public t1(int id, String name, int grade) {
        this.id = id;
        this.name = name;
        this.grade = grade;
    }
}


```

#### 构造接口。

按照网上的说法，如果是mapper方法实现的话，那么需要在一个包下。但是底层逻辑相差不大：都是实现一个接口然后重写接口。

所以需要写一个接口。

```
import java.util.List;

public interface t1Mapper {<!-- -->
    public List&lt;t1&gt; getT1Mapper();
}


```

官方提供的并不是无参的，也可以提供参数，不过一样的：可以注入参数。

#### 构造一个mapper

```
&lt;?xml version="1.0" encoding="UTF-8" ?&gt;
&lt;!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd"&gt;

&lt;mapper namespace="com.demo3.Dao.t1Mapper"&gt;
    &lt;select id="getT1Mapper" resultType="com.demo3.pojo.t1"&gt;
        select * from s1.t1 limit 1
    &lt;/select&gt;

&lt;/mapper&gt;

```

按照官方文档的说法，需要在接口的旁边实现一个mapper，为了可读性考虑可以同名（似乎没有硬性规定）
1. 需要指定namespace。1. 确认实现的方法是select还是其他。1. 指定要实现的接口1. 需要指定返回的类型1. 由于是全局的xml，所以包要使用全名。
#### 注册mapper

在mapper的config里面写入mapper。

```
    &lt;mappers&gt;
        &lt;mapper resource="com/demo3/Dao/t1Mapper.xml"/&gt;
    &lt;/mappers&gt;

```

所有的mapper都需要在对应的文件中进行写入，不然扫描不到。

#### 执行查询
1. 获取接口的反射：
```
t1Mapper mapper = sqlSession.getMapper(t1Mapper.class);

```

2.将查询的结果返回；

```
List&lt;t1&gt; t1Mapper = mapper.getT1Mapper();

```
1. 打印下返回结果
```
        System.out.println(t1Mapper);

```

获得返回：

```
[select1{id=1, name=1, grade=1}, select1{id=2, name=1, grade=1}, select1{id=3, name=1, grade=1}]

```

成功实现第一个sql。
