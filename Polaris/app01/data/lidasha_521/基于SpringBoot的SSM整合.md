
--- 
title:  基于SpringBoot的SSM整合 
tags: []
categories: [] 

---


#### 基于SpringBoot的SSM整合
- <ul><li>- - - 


>  
 开发系统：MAC 


>  
 开发工具：IntelliJ IDEA 2021.3.3 (Ultimate Edition) 


>  
 SpringBoot版本：2.5.12 


>  
 JDK版本：1.8 


### 1.创建SpringBoot项目
- 1.1.新建SpringBoot项目
<img src="https://img-blog.csdnimg.cn/04e68db43a8148bf9d9aea96421d4578.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">
- 1.2.选择SpringBoot版本和所需要的依赖
<img src="https://img-blog.csdnimg.cn/fdf76bdcc0da41b6a4b177e40a8d599f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">
- 1.3.项目创建成功结构
<img src="https://img-blog.csdnimg.cn/f24681c3e78647c7848cb803fcd4dd05.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">
- 1.4修改mysql驱动版本,默认生成的为8.x.x版本（可选）
默认生成的版本如下

<img src="https://img-blog.csdnimg.cn/1c58aba65e8c4e9790f6e1a4b78b81e6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

修改后的版本如下

<img src="https://img-blog.csdnimg.cn/54bc3c8460e54f51b9014a05617e8c14.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 2.进行Mybatis所需的配置
<li> 2.1.修改项目默认创建的的application.properties文件 
  <blockquote> 
   注：这个配置有以下两证方式可选，根据个人习惯选择 
  </blockquote> 
  <ul>- 2.1.1.使用  方式
```
# 配置数据源
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/数据库名?characterEncoding=utf-8&amp;useSSL=false
spring.datasource.username=数据库用户名
spring.datasource.password=数据库密码

# 配置映射文件路径及实体类包名
# 映射文件路径：在项目resources文件夹下创建mapper文件夹（此处可修改）
mybatis.mapper-locations=classpath:mapper/*Mapper.xml
# 实体类包路径
mybatis.type-aliases-package=com.example.ssm.demo.entity

```
- 2.1.2.使用 application.yml 方式
```
# 配置数据源
spring:
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/数据库名?characterEncoding=utf-8&amp;useSSL=false
    username: 数据量用户名
    password: 数据库密码

# 配置映射文件路径及实体类包名
mybatis:
  type-aliases-package: com.example.ssm.demo.entity
  mapper-locations: classpath:mapper/*Mapper.xml

```

2.2. 配置启动类，添加扫描包注解 `@MapperScan`

```
@SpringBootApplication
@MapperScan("com.example.ssm.demo.dao")
public class SsmDemoApplication{<!-- -->
		public static void main(String[]args) {<!-- -->
				SpringApplication.run(SsmDemoApplication.class, args);
		}
}

```

拓展，如果当前SpringBoot项目有个模块多个dao层，结构如下所示

<img src="https://img-blog.csdnimg.cn/088cf17c90a24b119ca4b24998fb3e65.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_13,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

此时启动类中的包扫描应该写成数组格式

```
@SpringBootApplication
@MapperScan({<!-- -->"com.example.ssm.demo.dao","com.example.ssm.demo.card.dao","com.example.ssm.demo.user.dao"})
public class SsmDemoApplication{<!-- -->
		public static void main(String[]args) {<!-- -->
				SpringApplication.run(SsmDemoApplication.class, args);
		}
}

```

### 3.整合数据库连接池Druid

>  
 在SpringBoot中整合Mybatis的时候，默认集成了Hikari连接池，Hikali的效率比Druid要高，但是得益于Druid提供了监控系统 

- 3.1.在项目的pom.xml中添加Druid的starter坐标（一个 starter = 依赖 + 配置）
```
&lt;!-- https://mvnrepository.com/artifact/com.alibaba/druid-spring-boot-starter --&gt;
&lt;dependency&gt;
    &lt;groupId&gt;com.alibaba&lt;/groupId&gt;
    &lt;artifactId&gt;druid-spring-boot-starter&lt;/artifactId&gt;
    &lt;version&gt;1.2.8&lt;/version&gt;
&lt;/dependency&gt;

```
- 3.2.修改 application.yml 配置文件
```
# 配置数据源
spring:
  datasource:
    druid:
      driver-class-name: com.mysql.jdbc.Driver
      url: jdbc:mysql://localhost:3306/数据库名?characterEncoding=utf-8&amp;useSSL=false
      username: 数据量用户名
      password: 数据量密码
      # 初始化容器大小
      initial-size: 1
      # 最小连接数
      min-idle: 1
      # 最大连接数
      max-active: 20

```
- 3.3.启动项目，查看结果
<img src="https://img-blog.csdnimg.cn/26ce778df1204f2fa0d8a2d548f76e50.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 4.整合完毕，手动撒花
