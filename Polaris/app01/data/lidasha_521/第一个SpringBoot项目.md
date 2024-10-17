
--- 
title:  第一个SpringBoot项目 
tags: []
categories: [] 

---


#### 文章目录
- - - <ul><li>- - - <ul><li>- - - - <ul><li>- - - 


## SpringBoot应用

`提示：以下是本篇文章正文内容，下面案例可供参考`

## 一、SpringBoot简介

### 1.概念
<li>随着动态语言的流行，Java语言的开发就显得格外的笨重： 
  <ul>- 配置繁琐- 开发效率低- 项目部署复杂- 集成第三方难度大
### 2.SpringBoot的优缺点
<li>SpringBoot优点： 
  <ul>- 能够快速搭建项目- 对主流的开发框架提供了无配置集成（SpringBoot内置了配置）- 项目可以独立运行，无需单独配置Servlet容器（内置了Tomcat)- 极大提高了开发、部署效率- 提供运行时监控系统（日志等）- 由于配置都是内置的，报错时定位比较困难- 版本迭代速度比较快，版本改动大会增加学习成本
## 二、第一个SpringBoot应用项目

```
开发系统：MAC

开发工具：IntelliJ IDEA 2021.3.3 (Ultimate Edition)

SpringBoot版本：2.5.12

JDK版本：1.8

```

### 1.基于SpringBoot整合SpringMVC

#### 1.1.新建项目，如下图

<img src="https://img-blog.csdnimg.cn/1882e80c81444d4b8ea6d6cb46488f57.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

注：SpringBoot应用需要依赖远程服务器进行创建,远程服务器有两种：
1. Spring官方：https://start.spring.io1. ali（阿里）：https://start.aliyun.com
#### 1.2.选择SpringBoot版本和所需要的依赖

<img src="https://img-blog.csdnimg.cn/175865b21f5f4035adfddd37a8275064.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

#### 1.3.项目创建成功结构

<img src="https://img-blog.csdnimg.cn/358852ad68ae462d81512ef285c2186b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 2.SpringBoot配置

#### 2.1.自定义配置

>  
 SpringBoot帮助我们完成通用性配置，但是数据库连接账号密码等还是需要手动配置 


##### 2.1.1.在SpringBoot项目的application.properties文件中配置数据源及路径

<img src="https://img-blog.csdnimg.cn/42a444241d55431b83b0ed38134b29eb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

```
# 配置数据源
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/xxxx?characterEncoding=utf-8&amp;useSSL=false
spring.datasource.username=root
spring.datasource.password=1qaz!QAZ

# 配置映射文件路径及实体类包名
mybatis.mapper-locations=classpath:mapper/*Mapper.xml
mybatis.type-aliases-package=com.example.springboot_demo.entity

```

##### 2.1.2.在SpringBoot启动类通过@MapperScan注解指定DAO接口的包名

```
@SpringBootApplication
@MapperScan("com.example.springboot_demo.dao")
public class SpringbootDemoApplication{<!-- -->
public static void main(String[]args) {<!-- -->
	SpringApplication.run(SpringbootDemoApplication.class, args);
	}
}

```

##### 2.1.3.第一个SpringBoot项目最终结构及代码

<img src="https://img-blog.csdnimg.cn/ef799efd97cb40648ac2d089c9cbd63b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_19,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

UserController类代码：

```
@RestController
@RequestMapping("/user")
public class UserController {<!-- -->

    @Resource
    private UserService userService;

    @RequestMapping("/insertUser")
    @ResponseBody
    public User insertUser(User user){<!-- -->
        User user1 = userService.insertUser(user);
        return user1;
    }
}

```

UserDao接口代码：

```
public interface UserDao{<!-- -->
	int insertUser(User user);
}

```

User类代码：

```
@Data
public class User{<!-- -->
	private String userName;
    private String passWord;
}

```

UserService接口代码：

```
public interface UserService{<!-- -->
	User insertUser(User user);
}

```

UserServiceImpl接口实现代码：

```
@Service
public class UserServiceImpl implements UserService{<!-- -->

	@Resource
    private UserDao userDao;

    @Override
    public User insertUser(User user) {<!-- -->
		int i = userDao.insertUser(user);
        if(i &gt; 0) {<!-- -->
			return user;
		}else{<!-- -->
			return null;
		}
	 }
}

```

UserMapper.xml代码

```
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPEmapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd"&gt;
&lt;mapper namespace="com.example.springboot_demo.dao.UserDao"&gt;
    &lt;insert id="insertUser"&gt;
		insert into user values(#{userName},#{passWord})
	&lt;/insert&gt;
&lt;/mapper&gt;

```

##### 2.1.4.启动SpringbootDemoApplication服务，测试项目

<img src="https://img-blog.csdnimg.cn/399518fcd0d04301811dd8d845c5c02b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/82af3814ddac4b39951c7fc2058500fd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/a2c8f71d0aa14ab2800adb876635ec8d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

## 总结

好了，以上就是我的第一个SpringBoot应用
