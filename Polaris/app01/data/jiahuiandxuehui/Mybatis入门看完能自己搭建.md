
--- 
title:  Mybatis入门看完能自己搭建 
tags: []
categories: [] 

---


#### 目录标题
- - - <ul><li><ul><li>- <ul><li>- - - - <ul><li>- - 


## Mybatis是什么
- mybatis是一个优秀的基于java的持久层框架，它内部封装了jdbc，使开发者只需要关注sql语句本身，而不需要花费精力去处理加载驱动、创建连接、创建statement等繁杂的过程。- mybatis通过xml主解的方式将要执行的各种statement配置起来。并通过java对象和statement中sql的动态参数进行映射生成最终执行的sql语句。- 最后mybatis框架执行sq并将结果映射为java对象并返回。采用ORM思想解决了实体和数据库映射的问题。对jdbc进行了封装。屏蔽了jdbc api底层访问细节,使我们不用与jdbc api打交道。就可以完成对数据库的持久化操作。
orm：对象关系映射是基于对象和数据表关系得映射

## 基本配置

<img src="https://img-blog.csdnimg.cn/1f003261eae14bf89b6ccd759d1cb877.png" alt="在这里插入图片描述">

#### 数据源环境配置

```
&lt;?xml version="1.0" encoding="UTF-8" ?&gt;
&lt;!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN" "http://mybatis.org/dtd/mybatis-3-config.dtd"&gt;
&lt;configuration&gt;


    &lt;properties resource="jdbc.properties"/&gt;
    
&lt;!--    自定义别名--&gt;
    &lt;typeAliases&gt;
        &lt;typeAlias type="com.wxh.domain.User" alias="user"/&gt;
    &lt;/typeAliases&gt;
    
&lt;!--    数据源环境--&gt;
    &lt;environments default="developement"&gt;
        &lt;environment id="developement"&gt;
            &lt;transactionManager type="JDBC"&gt;&lt;/transactionManager&gt;

            &lt;dataSource type="POOLED"&gt;
                &lt;property name="driver" value="${jdbc.drive}"/&gt;
                &lt;property name="url" value="${jdbc.url}"/&gt;
                &lt;property name="username" value="${jdbc.username}"/&gt;
                &lt;property name="password" value="${jdbc.password}"/&gt;
            &lt;/dataSource&gt;
        &lt;/environment&gt;
    &lt;/environments&gt;
    &lt;mappers&gt;
        &lt;mapper resource="com\whx\mapper\UserMapper.xml"/&gt;
    &lt;/mappers&gt;
&lt;/configuration&gt;

```

##### environments标签

```

其中，事务管理器(transactionManager）类型有两种:

.JDBC:这个配置就是直接使用了JDBC的提交和回滚设置，它依赖于从数据源得到的连接来管理事务作用域。

MANAGED:这个配置几乎没做什么。它从来不提交或回滚一个连接，而是让容器来管理事务的整个生命周期（比如JEE应用服务器的上下文)。默认情况下它会关闭连接，然而一些容器并不希望这样，因此需要将closeConnection属性设置为false来阻止它默认的关闭行为。心
其中，数据源(dataSource)类型有三种:

. UNPOOLED:这个数据源的实现只是每次被请求时打开和关闭连接。

. POOLED:这种数据源的实现利用“池”的概念将JDBC连接对象组织起来。

·JNDI:这个数据源的实现是为了能在如EJB或应用服务器这类容器中使用，容器可以集中或在外部配置数据源，然后放置一个JNDI上下文的引用。

```

##### mapper标签

```
该标签的作用是加载映射的，加载方式有如下几种:
·使用相对于类路径的资源引用，例如: &lt;mapper resource="org/mybatis/builder/AuthorMapper.xml"/&gt;

·使用完全限定资源起位符(URL)，例如:&lt;mapper url="file:///var/mappers/AuthorMapper.xml"/&gt;

·使用映射器接口实现类的完全限定类名，例如: &lt;mapper class="org.mybatis.builder.AuthorMapper"/&gt;

·将包内的映射器接口实现全部主册为映射器，例如: &lt;package name="org.mybatis.builder" /&gt;

```

##### Properties标签

实际开发中，习惯将数据源的配置信息单独抽取成一个properties文件，该标签可以加载额外配置的properties文件 <img src="https://img-blog.csdnimg.cn/b3ad16bac27244b59359c992d58859a4.png" alt="在这里插入图片描述">

##### typeAliases

自定义别名 <img src="https://img-blog.csdnimg.cn/252c9afb10a741b0a0535ee9dd8206ca.png" alt="在这里插入图片描述">

## MyBatis的API

```
package com.wxh.test;

import com.wxh.domain.User;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.junit.Test;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class testTser {<!-- -->

    public static SqlSession getMysqlSession(){<!-- -->
        //get配置文件
        InputStream resourceAsStream= null;
        try {<!-- -->
            resourceAsStream = Resources.getResourceAsStream("sqlMapperConfig.xml");
        } catch (IOException e) {<!-- -->
            e.printStackTrace();
        }

        //get sql session factory object
        SqlSessionFactory sqlSessionFactory=new SqlSessionFactoryBuilder().build(resourceAsStream);
        //get session conmmunicate object
        SqlSession sqlSession=sqlSessionFactory.openSession();
        return sqlSession;
    }

    @Test
    //查询
    public void test1()  {<!-- -->

        //execute
        List&lt;User&gt; userList=getMysqlSession().selectList("userMapper.findAll");
        System.out.println(userList);
        getMysqlSession().close();

    }
    @Test
    //插入
    public void test2(){<!-- -->
        User u=new User();
        u.setName("凡凡");
        u.setPassword("12345");
        getMysqlSession().insert("userMapper.save",u);
        getMysqlSession().commit();
        getMysqlSession().close();
    }

    @Test
    //修改
    public void test3(){<!-- -->
        User u=new User();
        u.setId(2);
        u.setPassword("12345");
        getMysqlSession().update("userMapper.revise",u);
        getMysqlSession().commit();
        getMysqlSession().close();
    }
    @Test
    //删除
    public void test4(){<!-- -->
        getMysqlSession().delete("userMapper.deleteUser",6);
        getMysqlSession().commit();
        getMysqlSession().close();
    }
}


```

#### SqlSession工厂构建器SqlSessionFactoryBuilder

```
常用API: SqlSessionFactory build(InputStream inputStream)

通过加载mybatis的核心文件的输入流的形式构建一个SqlSessionFactory对象

string resource = "org/mybatis/builder/mybatis-config.xaml";

Inputstream inputstream = Resources.getResourceasstream (resource) ;

sqlsessionFactoryBuilder builder = new sqlsessionFactoryBuilder() ;

sqlsessionFactory factory = builder. build(inputstream) ;


其中，Resources 工具类，这个类在org.apache.ibats.io包中。Resources类帮助你从类路径下、文件系统或一个web URL 中加载资源文件。

```

#### SqlSession工厂对象SqlSessionFactory

SqlSessionFactory有多个个方法创建SqlSession实例。常用的有如下两个:

```
openSession0
会默认开启一个事务，但事务不会自动提交，也就意味着需要手动提交该事务，更新操作数据才会持久化到数据库中

openSession(boolean autoCommit)
参数为是否自动提交，如果设置为true，那么不需要手动提交事务


```

到这里大家就应该能自己手动实现简单配置了，我们称这种配置的方法为传统方式实现。

#### 接口代理方式实现dao层配置

这种方法与传统方法相比省略了对接口的实现（不理解的话可以往下看），但是要注意在配置这种方式的时候要注意一下几个地方。 <img src="https://img-blog.csdnimg.cn/c4eaf3d0b1d54ae1b9c112a229aa6d43.png" alt="在这里插入图片描述"> 具体实现为：
- 对于接口
```
package com.wxh.dao;

import com.wxh.domain.User;

import java.util.List;

public interface UserMapper {<!-- -->
    public List&lt;User&gt; findAll();
    public void revise();
}


```

对于userMapper.xml

```
&lt;?xml version="1.0" encoding="UTF-8" ?&gt;
&lt;!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd"&gt;
&lt;mapper namespace="com.wxh.dao.UserMapper"&gt;
    &lt;select id="findAll" resultType="com.wxh.domain.User"&gt;
        select * from USER
    &lt;/select&gt;

    &lt;update id="revise" parameterType="com.wxh.domain.User"&gt;
        update user set password=#{<!-- -->password} where id=#{<!-- -->id}
    &lt;/update&gt;
&lt;/mapper&gt;


```

测试代码：

```
package com.wxh.test;

import com.wxh.dao.UserMapper;
import com.wxh.domain.User;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.junit.Test;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class test2 {<!-- -->
    public static UserMapper getUserMapper() throws IOException {<!-- -->

        InputStream inputStream=Resources.getResourceAsStream("sqlMapperConfig.xml");
        SqlSessionFactory sqlSessionFactory=new SqlSessionFactoryBuilder().build(inputStream);
        SqlSession sqlSession=sqlSessionFactory.openSession();
        UserMapper userMapper=sqlSession.getMapper(UserMapper.class);
        return userMapper;

    }
    @Test
    public void FindAll() throws IOException {<!-- -->

        List&lt;User&gt; userList=getUserMapper().findAll();
        System.out.println(userList);
    }
}


```
