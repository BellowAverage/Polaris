
--- 
title:  SpringBoot集成Mybatis插件tkMapper的使用 
tags: []
categories: [] 

---
>  
 SpringBoot集成通用Mapper 




#### 文章目录
- - - - - - 


## 1.通用 MAPPER 3简介

文档地址：
- **通用Mapper都可以极大的方便开发人员。可以随意的按照自己的需要选择通用方法，还可以很方便的开发自己的通用方法。**- **极其方便的使用MyBatis单表的增删改查。**- **支持单表操作，不支持通用的多表联合查询。**- **支持 Mybatis-3.2.4 及以上版本**- **不是表中字段的属性必须加 `@Transient` 注解,这样通用Mapper在处理单表操作时就不会将标注的属性当成表字段处理！**- **通用 Mapper 不支持 devtools 热加载**，devtools 排除实体类包即可，配置方式参考：
## 2.集成通用 MAPPER
- **<strong>添加 Maven 依赖或引入 Jar 包**</strong>
```
&lt;!-- https://mvnrepository.com/artifact/tk.mybatis/mapper --&gt;
&lt;dependency&gt;
    &lt;groupId&gt;tk.mybatis&lt;/groupId&gt;
    &lt;artifactId&gt;mapper&lt;/artifactId&gt;
    &lt;version&gt;4.2.1&lt;/version&gt;
&lt;/dependency&gt;

```

## 3.使用通用 MAPPER
- **继承通用的`Mapper&lt;T&gt;`,必须指定泛型`&lt;T&gt;`**
```
// 一旦继承了Mapper&lt;T&gt;,继承的Mapper就拥有了Mapper&lt;T&gt;所有的通用方法。
public interface UserMapper extends Mapper&lt;User&gt; {<!-- -->
		//其他必须手写的接口...
}

```
- **泛型(实体类)`&lt;T&gt;`的类型必须符合要求**
```
1. 表名默认使用类名,驼峰转下划线(只对大写字母进行处理),如`User`默认对应的表名为`user`。
2. 表名可以使用`@Table(name = "tableName")`进行指定,对不符合第一条默认规则的可以通过这种方式指定表名.如：数据库表明为users,实体类为User此时就需要使用@Table(name = "users")
3. 字段默认和`@Column`一样,都会作为表字段,表字段默认为Java对象的`Field`名字驼峰转下划线形式.
4. 可以使用`@Column(name = "fieldName")`指定不符合第3条规则的字段名
5. 使用`@Transient`注解可以忽略字段,添加该注解的字段不会作为表字段使用.
6. **建议一定是有一个`@Id`注解作为主键的字段,可以有多个`@Id`注解的字段作为联合主键.**
7. **默认情况下,实体类中如果不存在包含`@Id`注解的字段,所有的字段都会作为主键字段进行使用(这种效率极低).**
8. 实体类可以继承使用,可以参考测试代码中的`tk.mybatis.mapper.model.UserLogin2`类.
9. 由于基本类型,如int作为实体类字段时会有默认值0,而且无法消除,所以实体类中建议不要使用基本类型.
10. `@NameStyle`注解，用来配置对象名/字段和表名/字段之间的转换方式，该注解优先于全局配置`style`，可选值：
    - `normal`:使用实体类名/属性名作为表名/字段名
    - `camelhump`:**这是默认值**，驼峰转换为下划线形式
    - `uppercase`:转换为大写
    - `lowercase`:转换为小写

```
<li> **<strong>主键策略(仅用于insert方法)**</strong> 
  <ul>- @GeneratedValue(generator = “JDBC”)
```
@Id
@GeneratedValue(generator = "JDBC")
private Integer id;

```
- @GeneratedValue(strategy = GenerationType.IDENTITY)
```
//不限于@Id注解的字段,但是一个实体类中只能存在一个(继承关系中也只能存在一个)
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Integer id;

```
- @GeneratedValue(generator = “UUID”)
```
//可以用于任意字符串类型长度超过32位的字段
@GeneratedValue(generator = "UUID")
private String username;

```

## 4.SpringBoot项目主要实现代码
- 创建users表
```
CREATE TABLE `users` (
  `user_id` int(64) NOT NULL AUTO_INCREMENT COMMENT '主键id ',
  `username` varchar(32) NOT NULL COMMENT '用户名',
  `password` varchar(64) NOT NULL COMMENT '密码 ',
  `user_img` varchar(1024) NOT NULL COMMENT '头像',
  `user_regtime` datetime NOT NULL COMMENT '注册时间',
  `user_modtime` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='用户 ';

```
- User实体类
```
@Table(name = "users")
@Data
public class User implements Serializable{<!-- -->
	private static final longserialVersionUID= 624362698554707695L;
	/** 主键id */
	@Id
   	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer userId;
	/** 用户名 */
	private String username;
	/** 密码 */
	private String password;
	/** 头像 */
	private String userImg;
	/** 注册时间 */
	private Date userRegtime;
	/** 更新时间 */
	private Date userModtime;
}

```
- UserDAO接口
```
import com.example.tkmapper.demo.entity.User;
import tk.mybatis.mapper.common.Mapper;

// 一旦继承了Mapper&lt;T&gt;,继承的Mapper就拥有了Mapper&lt;T&gt;所有的通用方法。
public interface UserDAO extends Mapper&lt;User&gt; {<!-- -->
	//其他必须手写的接口...
}


```
- 启动类
```
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import tk.mybatis.spring.annotation.MapperScan;

@MapperScan("com.example.tkmapper.demo.dao")
@SpringBootApplication
public class TkmapperDemoApplication {<!-- -->
    public static void main(String[] args) {<!-- -->
        SpringApplication.run(TkmapperDemoApplication.class, args);
    }
}

```
- application.properties配置数据源
```
# 配置数据源
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/数据库?characterEncoding=utf-8
spring.datasource.username=数据库用户名
spring.datasource.password=数据库密码

# 配置映射文件路径及实体类包名
mybatis.mapper-locations=classpath:mapper/*Mapper.xml
mybatis.type-aliases-package=com.example.tkmapper.demo.entity

```
- 测试类
```
import com.example.tkmapper.demo.dao.UserDAO;
import com.example.tkmapper.demo.entity.User;
import org.apache.ibatis.session.RowBounds;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import tk.mybatis.mapper.entity.Example;
import javax.annotation.Resource;
import java.util.Date;
import java.util.List;
import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest
class TkmapperDemoApplicationTests {<!-- -->

    @Resource
    private UserDAO userDAO;

    @Test
    void test1() {<!-- -->
        // 测试插入
        User user = new User();
        user.setUsername("test12");
        user.setPassword("123456");
        user.setUserImg("test.jpg");
        user.setUserRegtime(new Date());
        user.setUserModtime(new Date());
        int status = userDAO.insert(user);
        assertEquals(1, status);
    }

    @Test
    void test2() {<!-- -->
        // 测试删除
        int status = userDAO.deleteByPrimaryKey(13);
        assertEquals(1, status);
    }

    @Test
    void test3() {<!-- -->
        // 测试修改
        int status = userDAO.updateByPrimaryKey(new User(12, "xixi", "123456", "test.jpg", new Date(), new Date()));
        assertEquals(1, status);
    }

    @Test
    void test4() {<!-- -->
        // 测试查询所有
        userDAO.selectAll().forEach(System.out::println);
    }

    @Test
    void test5() {<!-- -->
        // 测试根据主键查询
        User user = userDAO.selectByPrimaryKey(12);
        System.out.println("user = " + user);
    }

    @Test
    void test6() {<!-- -->
        // 测试根据条件查询
        Example example = new Example(User.class);
        example.createCriteria().andEqualTo("username", "xixi")
                .andLike("password", "%123%");
        List&lt;User&gt; users = userDAO.selectByExample(example);
        users.forEach(System.out::println);
    }

    @Test
    void test7() {<!-- -->
        // 测试分页查询
        int pageNum = 1;
        int pageSize = 5;
        int offset = (pageNum - 1) * pageSize;
        userDAO.selectByRowBounds(new User(), new RowBounds(offset, pageSize)).forEach(System.out::println);

        //查询总记录数用于分页
        int count = userDAO.selectCount(new User());
        System.out.println("count = " + count);
    }

    @Test
    void test8() {<!-- -->
        // 测试带条件的分页查询
        Example example = new Example(User.class);
        example.createCriteria().andEqualTo("password", "123456");

        int pageNum = 1;
        int pageSize = 5;
        int offset = (pageNum - 1) * pageSize;

        userDAO.selectByExampleAndRowBounds(example, new RowBounds(offset, pageSize)).forEach(System.out::println);

        //查询总记录数用于分页
        int count = userDAO.selectCountByExample(example);
        System.out.println("count = " + count);
    }
}

```

## 5.Mapper接口大全
- 链接地址：
## 6.使用通用Mapper进行关联查询
<li>**根据条件进行多次单表查询** 
  <ul>- 如先查询用户信息，再根据用户id查询订单信息- 也就是在DAO接口中自定义接口，在**Mapper.xml中进行SQL编写