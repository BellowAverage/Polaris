
--- 
title:  spring Boot(七)——数据库(JDBC、Druid、MyBatis、JPA) 
tags: []
categories: [] 

---
## 一、JDBC

导入依赖：

```
&lt;!--jdbc--&gt;
        &lt;!-- https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-jdbc --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-jdbc&lt;/artifactId&gt;
        &lt;/dependency&gt;
        &lt;!-- https://mvnrepository.com/artifact/mysql/mysql-connector-java --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;mysql&lt;/groupId&gt;
            &lt;artifactId&gt;mysql-connector-java&lt;/artifactId&gt;
            &lt;!--&lt;scope&gt;runtime&lt;/scope&gt;--&gt;
        &lt;/dependency&gt;
```

数据源：

```
spring.datasource.username=root
spring.datasource.password=123456
spring.datasource.url=jdbc:mysql://ip:端口/test1?characterEncoding=utf8&amp;useSSL=false&amp;serverTimezone=UTC&amp;rewriteBatchedStatements=true
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
```

参数：

```
#指定
spring.datasource.schema = 建表sql
spring.datasource.data  = 表数据
#不指定  默认只需将文件命名为：
schema-*.sql
data-*.sql
```

使用：

```
spring.datasource.initialization-mode=always
spring.datasource.schema=classpath:sql/schema-ddl.sql
```

操作数据库：

```
@Autowired
    private JdbcTemplate jdbcTemplate;
    @ResponseBody
    @GetMapping(value = "/hello")
    public Map&lt;String, Object&gt; hel() {
        List&lt;Map&lt;String, Object&gt;&gt; list = jdbcTemplate.queryForList("select * from login");
        return list.get(0);
    }
```

<img alt="" class="has" height="107" src="https://img-blog.csdnimg.cn/20200204213152900.png" width="382">

## 二、Druid

### 2.1引入依赖

```
&lt;!--引入druid --&gt;
&lt;dependency&gt;
         &lt;groupId&gt;com.alibaba&lt;/groupId&gt;
         &lt;artifactId&gt;druid-spring-boot-starter&lt;/artifactId&gt;
         &lt;version&gt;1.1.10&lt;/version&gt; 
&lt;/dependency&gt;
```

### 2.2配置

```
# 初始化大小，最小，最大
spring.datasource.druid.initial-size=5
spring.datasource.druid.min-idle=5
spring.datasource.druid.max-active=20
# 配置间隔多久才进行一次检测，检测需要关闭的空闲连接，单位是毫秒
spring.datasource.druid.time-between-eviction-runs-millis=60000
# 配置一个连接在池中最小生存的时间，单位是毫秒
spring.datasource.druid.min-evictable-idle-time-millis=300000
spring.datasource.druid.validation-query: SELECT 1 FROM DUAL
spring.datasource.druid.test-while-idle: true
spring.datasource.druid.test-on-borrow: false
spring.datasource.druid.test-on-return: false
# 打开PSCache，并且指定每个连接上PSCache的大小
spring.datasource.druid.pool-prepared-statements=true
# 配置监控统计拦截的filters，去掉后监控界面sql无法统计，'wall'用于防火墙
spring.datasource.druid.max-pool-prepared-statement-per-connection-size: 20
spring.datasource.druid.filters: stat,wall
spring.datasource.druid.use-global-data-source-stat: true
# 打开mergeSql功能；慢SQL记录
spring.datasource.druid.filter.stat.merge-sql=true
spring.datasource.druid.filter.stat.slow-sql-millis=500
# 配置监控服务器
spring.datasource.druid.stat-view-servlet.enabled=true
# 登录名
spring.datasource.druid.stat-view-servlet.login-username=tchuhu
# 登录密码
spring.datasource.druid.stat-view-servlet.login-password=tchuhu
spring.datasource.druid.stat-view-servlet.reset-enable=false
spring.datasource.druid.stat-view-servlet.url-pattern=/druid/*
# 添加IP白名单
#spring.datasource.druid.stat-view-servlet.allow=127.0.0.1
# 添加IP黑名单，当白名单和黑名单重复时，黑名单优先级更高
#spring.datasource.druid.stat-view-servlet.deny=127.0.0.1
# 添加过滤规则
spring.datasource.druid.web-stat-filter.enabled=true
spring.datasource.druid.web-stat-filter.url-pattern=/*
# 忽略过滤格式
spring.datasource.druid.web-stat-filter.exclusions= "*.js,*.gif,*.jpg,*.png,*.css,*.ico,/druid/*"

```

### 2.3监控

<img alt="" height="359" src="https://img-blog.csdnimg.cn/20200224173229680.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="825">

<img alt="" height="321" src="https://img-blog.csdnimg.cn/20200224173359696.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

## 三、整合MyBatis

mybatis参考文档:

### 3.1引入依赖

```
&lt;!--引入mybatis --&gt;
&lt;dependency&gt;
            &lt;groupId&gt;org.mybatis.spring.boot&lt;/groupId&gt;
            &lt;artifactId&gt;mybatis-spring-boot-starter&lt;/artifactId&gt;
            &lt;version&gt;1.3.2&lt;/version&gt;
&lt;/dependency&gt;
```

### 3.2注解版

```
public interface UserMapper {

    @Select("select * from login where id = #{id}")
    public User getUserById(Integer id);

    @Delete("delete from login where id =#{id}")
    public int deleteById(Integer id);

    @Options(useGeneratedKeys = true,keyProperty = "id")//会返回自增的id
    @Insert("insert into login(name,pwd) values(#{name},#{pwd})")
    public int insertLogin(User user);

    @Update("update login set name =#{name} where id = #{id}")
    public int updateById(User user);

    @Select("select * from login")
    public List&lt;User&gt; getUsers();
}
```

### 3.2.1mapper扫描

```
//mapper包扫描
@MapperScan("com.mapper")

@SpringBootApplication
public class SpringBootWebApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringBootWebApplication.class, args);
    }

}
```

### 3.3配置版

配置文件

<img alt="" height="131" src="https://img-blog.csdnimg.cn/20200225220927391.png" width="244">

#### 3.3.1配置文件配置

```
#mybatis配置
mybatis.config-location=classpath:mybatis/mybatis_config.xml
mybatis.mapper-locations=classpath:mybatis/mapper/*.xml

```

#### 3.3.2mapper扫描

```
@MapperScan("com.mapper")
@SpringBootApplication
public class SpringBootWebApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringBootWebApplication.class, args);
    }

}
```

## 四、整合JPA

Java Persistence Api（Java持久化API）

### 4.0Spring Data JPA

<img alt="" height="389" src="https://img-blog.csdnimg.cn/20200228222940707.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="758">

**JAP与Hibernate的关系**

<img alt="" height="86" src="https://img-blog.csdnimg.cn/20200228223044683.png" width="865">

**JPA的优势**

<img alt="" height="76" src="https://img-blog.csdnimg.cn/20200228223121182.png" width="862">

**JPA包含的技术**

<img alt="" height="71" src="https://img-blog.csdnimg.cn/20200228223201820.png" width="858">

### 4.1实现

引入依赖:

```
 &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-data-jpa&lt;/artifactId&gt;
&lt;/dependency&gt;
```

### 4.2映射

#### 4.2.1一对一

比如一个丈夫只能有一个老婆，数据库分别为men表和women表

<img alt="" height="94" src="https://img-blog.csdnimg.cn/20200229164249115.png" width="435">          <img alt="" height="98" src="https://img-blog.csdnimg.cn/20200229164322545.png" width="249">

接下来，编写实体类：

```
@Entity
@Table(name = "men")
public class Men { //老公类
    @Id    //主键
    /*
        @GeneratedValue(generator =GenerationType.IDENTITY )  //自增ID
            -AUTO主键由程序控制, 是默认选项 ,不设置就是这个
            -IDENTITY 主键由数据库生成, 采用数据库自增长, Oracle不支持这种方式
            -SEQUENCE 通过数据库的序列产生主键, MYSQL  不支持
            -Table 提供特定的数据库产生主键, 该方式更有利于数据库的移植
    */
    @Column(name = "menId")
    private String id;
    @Column(name = "menName")
    private String name;
    @OneToOne(optional = false) //woMen的id 可以为空
    @JoinColumn(name = "womenId",unique = true)//当前表对应表的列名， 唯一外键
    private Women women;

    public Men() {
    }
    //省略setter getter
}
```

```
@Entity
@Table(name = "women")
public class Women {  //老婆类
    @Id
    @Column(name = "womenId")
    private String id;
    @Column(name = "womenName")
    private String name;
    @OneToOne(fetch = FetchType.LAZY,mappedBy = "women") //这里放弃关系维护，交给men表来维护
    private Men men;

    public Women() {
    }
    //省略setter getter
}
```

#### 4.2一对多

#### 4.3多对一

#### 4.4多对多

参考


