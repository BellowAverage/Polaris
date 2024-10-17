
--- 
title:  0基础学习Mybatis系列数据库操作框架——目录结构 
tags: []
categories: [] 

---


#### 大纲
- - - <ul><li>- <ul><li>- 


在一文中，我们用最简单的方法组织出一个Mybatis应用项目。为了后续构建更符合日常开发环境的项目，我们对项目的目录结构做了调整，并引入了单元测试组件JUnit。 <img src="https://img-blog.csdnimg.cn/direct/4a85d0d2b9634334a9d9ae2be488c819.png" alt="在这里插入图片描述">

## 配置的修改

在resources目录下，将mybatis相关的配置聚合到名字叫mybatis的目录下，这样会方便后续管理。因为实际开发中，我们还会使用到很多其他组件的配置。如果散乱在resources这个目录下，将不利于后期维护。 mybatis的配置由两部分组成：
- 数据库连接和mapper文件路径。这个配置叫mybatis-config.xml，我们把它放在config目录下。
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
        &lt;mapper resource="mybatis/mapper/AllTypeMapper.xml"/&gt;
    &lt;/mappers&gt;
&lt;/configuration&gt;

```
<li>mapper文件。可能是多个mapper文件，我们把它们放到mapper目录下。本例我们只设计了一个mapper，但是含有两条SQL。 
  <ul>- findAll用查询表中所有数据。- find会**根据传入的参数**返回多条数据。
需要注意的是mapper的namespace，**它与后续我们定义的SQL映射器（mapper）接口的包(org.example.mapper)和名称(AllTypeMapper)组合一致**。否则我们在后续的Java代码中不能创建SQL映射器对象。

```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd"&gt;
&lt;mapper namespace="org.example.mapper.AllTypeMapper"&gt;
    &lt;select id="findAll" resultType="org.example.model.AllType"&gt;
        select * from all_type
    &lt;/select&gt;
    &lt;select id="find" resultType="org.example.model.AllType"&gt;
        select * from all_type where info_int = #{info_int}
    &lt;/select&gt;
&lt;/mapper&gt;

```

## 代码的修改

主要修改分为两部分

### Main.java文件所在包下

#### 新增org.example.model包

用于保存SQL结果映射的Java对象类。

```
package org.example.model;

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

#### 新增org.example.mapper包

用于保存SQL语句映射器类（Mapper Class）的接口定义（Interface）。这个概念我们并没有在中涉及，因为之前我们直接通过全限定名“AllTypeMapper.findAll”访问了SQL方法。而本文我们将使用映射机器来访问。 注意映射器接口中的find方法名，在之前写好的SQL XML文件中看到过。后续我们还将在单元测试代码中见到它。 **这个接口的定义连接了SQL XML和Java代码。**

```
package org.example.mapper;

import org.example.model.AllType;
import java.util.List;

public interface AllTypeMapper {<!-- -->
    List&lt;AllType&gt; find(int info_int);
}

```

### 单元测试

和main目录对等，建立相似的目录结构和包。 <img src="https://img-blog.csdnimg.cn/direct/868963083f644afaa2d3834f061d961e.png" alt="在这里插入图片描述"> 我们并不打算针对main下的model和mapper包做单元测试，而是在单元测试中测试mybatis相关特性，所以test目录下的org.example包下只有一个测试文件AllTypeTest.java。 不同于中查询所有数据的写法

```
            try (SqlSession s = sqlSF.openSession()) {<!-- -->
                all = s.selectList("org.example.mapper.AllTypeMapper.findAll");
            }
            for (AllType a : all) {<!-- -->
                System.out.println(a.getInfo_int());
            }

```

本文要根据根据传入的参数，动态修改SQL语句。注意下面的写法：
- 通过connection的getMapper方法获取映射器类（传入的是接口）。- 通过映射器类的方法（继承自映射器接口），修改SQL语句并获得返回结果。
```
            try (SqlSession s = sqlSF.openSession()) {<!-- -->
                AllTypeMapper all_type_mapper = s.getMapper(AllTypeMapper.class);
                List&lt;AllType&gt; all = all_type_mapper.find(1);
                for (AllType a : Objects.requireNonNull(all)) {<!-- -->
                	System.out.println(a.getInfo_int());
            	}
            }

```

完整代码如下：

```
package org.example;

import org.example.model.AllType;
import org.example.mapper.AllTypeMapper;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class AllTypeTest {<!-- -->
    private static SqlSessionFactory sqlSF;

    @BeforeAll
    static void CreateSessionFactory() throws IOException {<!-- -->
        InputStream in = Resources.getResourceAsStream("mybatis/config/mybatis-config.xml");
        sqlSF = new SqlSessionFactoryBuilder().build(in);
    }
    
    @Test
    void testFindAll() {<!-- -->
        List&lt;AllType&gt; all = null;
        try (SqlSession s = sqlSF.openSession()) {<!-- -->
            all = s.selectList("org.example.mapper.AllTypeMapper.findAll");
        } catch (Exception e) {<!-- -->
            System.out.println(e.getMessage());
        }
        for (AllType a : Objects.requireNonNull(all)) {<!-- -->
            System.out.println(a.getInfo_int());
        }
    }

    @Test
    void testFind() {<!-- -->
        try (SqlSession s = sqlSF.openSession()) {<!-- -->
            AllTypeMapper all_type_mapper = s.getMapper(AllTypeMapper.class);
            List&lt;AllType&gt; all = all_type_mapper.find(1);
            for (AllType a : Objects.requireNonNull(all)) {<!-- -->
                System.out.println(a.getInfo_int());
            }
        } catch (Exception e) {<!-- -->
            System.out.println(e.getMessage());
        }
    }
}

```

经过优化后的目录结构，将有利于后续我们的设计和探索。 代码样例见：
