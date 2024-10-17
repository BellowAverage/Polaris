
--- 
title:  springboot整合mybatis（idea） 
tags: []
categories: [] 

---
#### 从idea新建项目

选择spring启动<img src="https://img-blog.csdnimg.cn/76e374f6a13a43e2b878a30e5fcc824e.png" alt="在这里插入图片描述">* help、mvnw 文件可以删除
- springBoot3.0需要的最小JDK是JDK17，当低于17的时候会报错。 改成2.7.6
#### 新建控制层Controller、Mapper层和Model文件夹
- 必须在springBoot启动项下面新建，不然无法识别。
##### 允许XML进入target

在pom.xml里面写入

```
&lt;build&gt;
        &lt;resources&gt;
            &lt;resource&gt;
                &lt;directory&gt;src/main/java&lt;/directory&gt;
                &lt;includes&gt;
                    &lt;include&gt;**/*.properties&lt;/include&gt;
                    &lt;include&gt;**/*.xml&lt;/include&gt;
                &lt;/includes&gt;
                &lt;filtering&gt;false&lt;/filtering&gt;
            &lt;/resource&gt;
        &lt;/resources&gt;
&lt;/build&gt;

```

##### 引入必要的依赖包

```
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter&lt;/artifactId&gt;
        &lt;/dependency&gt;


        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-jdbc&lt;/artifactId&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;org.projectlombok&lt;/groupId&gt;
            &lt;artifactId&gt;lombok&lt;/artifactId&gt;
            &lt;optional&gt;true&lt;/optional&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;mysql&lt;/groupId&gt;
            &lt;artifactId&gt;mysql-connector-java&lt;/artifactId&gt;
            &lt;version&gt;8.0.28&lt;/version&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
            &lt;scope&gt;test&lt;/scope&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-validation&lt;/artifactId&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.xmlunit&lt;/groupId&gt;
            &lt;artifactId&gt;xmlunit-core&lt;/artifactId&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;org.mybatis.spring.boot&lt;/groupId&gt;
            &lt;artifactId&gt;mybatis-spring-boot-starter&lt;/artifactId&gt;
            &lt;version&gt;2.0.1&lt;/version&gt;
        &lt;/dependency&gt;

```

#### 配置数据库账号密码

application.properties

```
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/test01?useUnicode=true&amp;characterEncoding=utf8&amp;useSSL=false
spring.datasource.username=testUser
spring.datasource.password=testnlp#123

```

#### 在model导入一个新的类

和数据库对应，构建一个类 <img src="https://img-blog.csdnimg.cn/9052761491ab40ebab8f27484d2e833b.png" alt="在这里插入图片描述">

实现GetSet方法、各种有参构造、无参构造。 通过@value实现默认值设定

```
@Data
@Component
@AllArgsConstructor
@NoArgsConstructor
public class Cat {<!-- -->
    @NotNull(message="必须为空")
    Integer age;
    @Value("dog01")
    String name;
    @Value("1")
    Integer id;
}

```

#### 写入mapper文件

在mapper文件夹下写入一个接口

```
@Mapper
public interface CatMapper {<!-- -->
    @Insert("insert into cat(id, name, age) values(#{id}, #{name}, #{age})")
    void addOneCat(Cat cat);
}

```
- 加入@mapper注解或者在主类加入@MapperScan(“com/example/test02/test02/mapper”)- 可以在接口上写注释实现简单的SQL查询
#### 写入一个控制层
- 类上加入控制注解- 将mapper注入这个类- 实现控制类方法
```
@RestController
public class testController {<!-- -->
    @Resource
    CatMapper catMapper;

    @RequestMapping(value = "/cat", method = RequestMethod.POST)
    @ResponseBody
    Cat addCat(Cat cat) {<!-- -->
        catMapper.addOneCat(cat);
        return cat;
    }
}

```

#### 测试接口

启动SpringBoot服务 <img src="https://img-blog.csdnimg.cn/62533672f776402ca09c51b51ad7ba5e.png" alt="在这里插入图片描述"> 使用postman发送对应的请求，检查返回值 <img src="https://img-blog.csdnimg.cn/3c4db09c7e5c4077b097d50476e046b1.png" alt="在这里插入图片描述">

检查数据库是否有新增的数据： <img src="https://img-blog.csdnimg.cn/65e7aeadf1f6457b9c6c65b6a987d39c.png" alt="在这里插入图片描述"> 成功写入数据。
