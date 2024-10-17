
--- 
title:  SpringBoot+SpringMVC+Mybatis+Swagger实现用户注册、登录功能 
tags: []
categories: [] 

---
>  
 SpringBoot+Mybatis+Swagger实现用户注册、登录功能 




#### 文章目录
- - - 


## 1.实现流程图

<img src="https://img-blog.csdnimg.cn/96710aaaecca4d8b9381a4dcad929298.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

## 2.后台业务开发
<li> 添加实体类（entity、beans、pojo） 
  <ul>- 使用`Easy Code`插件快速生成,参考：****（可自行修改生成模板）****
```
@ApiModel(value = "User实体类", description = "用户(Users)实体类")
@Data
public class Users implements Serializable{<!-- -->
	private static final longserialVersionUID = 624362698554707695L;
	/** 主键id */
	@ApiModelProperty(value = "主键id")
	private Integer userId;
	/** 用户名 */
	@ApiModelProperty(value = "用户名")
	private String username;
	/** 密码 */
	@ApiModelProperty(value = "密码")
	private String password;
	/** 头像 */
	@ApiModelProperty(value = "头像")
	private String userImg;
	/** 注册时间 */
	@ApiModelProperty(value = "注册时间")
	private Date userRegtime;
	/** 更新时间 */
	@ApiModelProperty(value = "更新时间")
	private Date userModtime;
}

```

完成DAO层
- 创建DAO接口、自定义操作方法
```
public interface UserDAO {<!-- -->
	// 添加用户
    int addUser(Users user);
    // 根据用户名查询用户
    Users getUserByName(String name);
}

```
- 创建DAO接口对应的Mapper.xml文件并完成配置
```
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPEmapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd"&gt;
&lt;mapper namespace="com.cy.dao.UserDAO"&gt;
    &lt;insert id="addUser"&gt;
		insert into users(username, password, user_img, user_regtime, user_modtime) values (#{username}, #{password}, #{userImg}, #{userRegtime}, #{userModtime})
	&lt;/insert&gt;

    &lt;select id="getUserByName" resultType="com.cy.entity.Users"&gt;
		SELECT 
			user_id as userId,
            username,
            password,
            user_img as userImg,
            user_regtime as userRegtime,
            user_modtime as userModtime
        FROM 
			users
        WHERE 
			username = #{name}
	&lt;/select&gt;
&lt;/mapper&gt;

```

完成Service层
- 创建Service接口、自定义操作方法
```
public interface UserService {<!-- -->
	// 添加用户
    ResultVo addUser(String name, String password);
    // 根据用户名查询用户
    ResultVo checkLogin(String name, String password);
}


```
- 创建Service接口对应的ServiceImpl实现类
```
@Service
public class UserServiceImpl implements UserService {<!-- -->

	@Resource
    private UserDAO userDAO;

    @Transactional
    public ResultVo addUser(String name, String password) {<!-- -->
		synchronized(this) {<!-- -->
	        // 1. 根据用户名查询用户是否存在
            Users user = userDAO.getUserByName(name);

            // 2. 如果用户不存在，则添加用户
            if(user == null) {<!-- -->
			    String pwd = MD5Utils.md5(password);
                user = new Users();
                user.setUsername(name);
                user.setPassword(pwd);
                user.setUserImg("img/default.jpg");
                user.setUserRegtime(new Date());
                user.setUserModtime(new Date());
                int addUser = userDAO.addUser(user);
                if(addUser &gt; 0) {<!-- -->
				    return new ResultVo(200, "注册成功", user);
			    }else{<!-- -->
					return new ResultVo(500, "注册失败", null);
				}
	        }else{<!-- -->
				// 3. 如果用户存在，则返回用户已存在
			    return new ResultVo(500, "用户已存在", null);
			}
		}
   }

	@Override
    public ResultVo checkLogin(String name, String password) {<!-- -->
		// 1. 根据用户名查询用户是否存在
        Users user = userDAO.getUserByName(name);
        if(user == null) {<!-- -->
			return new ResultVo(500, "用户不存在", null);
		} else {<!-- -->
			// 2. 如果用户存在，则校验密码是否正确
            String pwd = MD5Utils.md5(password);
            if(pwd.equals(user.getPassword())) {<!-- -->
				return new ResultVo(200, "登录成功", user);
			} else {<!-- -->
				return new ResultVo(500, "密码错误", null);
			}
        }
    }
}

```

完成Controller层
- 创建Controller类
```
@RestController
@RequestMapping("/user")
@Api(tags = "用户管理模块")
public class UserController{<!-- -->

	@Resource
    private UserService userService;

    @PostMapping("/register")
	@ApiOperation("用户注册")
	@ApiImplicitParams({<!-- -->
		@ApiImplicitParam(name = "username",value = "用户名",dataType = "String",required = true),
        @ApiImplicitParam(name = "password",value = "密码",dataType = "String",required = true)
    })
	public ResultVo register(@RequestParam("username")String username, @RequestParam("password")String password) {<!-- -->
		return userService.addUser(username, password);
	}
		
	@GetMapping("/login")
	@ApiOperation("用户登录")
	@ApiImplicitParams({<!-- -->
		@ApiImplicitParam(name = "username",value = "用户名",dataType = "String",required = true),
        @ApiImplicitParam(name = "password",value = "密码",dataType = "String",required = true)
    })
	public ResultVo login(@RequestParam("username")String username, @RequestParam("password")String password) {<!-- -->
		return userService.checkLogin(username, password);
	}
}

```

其他类和配置
- 公用返回结果Vo
```
@ApiModel(value = "ResultVo", description = "公用返回结果Vo")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class ResultVo{<!-- -->

	@ApiModelProperty(value = "状态码", example = "200")
	private Integer code;

    @ApiModelProperty(value = "返回信息", example = "success")
	private String msg;

    @ApiModelProperty(value = "返回数据", example = "data")
	private Object data;
}

```
- MD5Utils工具类
```
public class MD5Utils{<!-- -->
	public static String md5(String password) {<!-- -->
		//生成一个md5加密器
	    try{<!-- -->
			MessageDigest md = MessageDigest.getInstance("MD5");
	        //计算MD5 的值
	        md.update(password.getBytes());
	        //BigInteger 将8位的字符串 转成16位的字符串 得到的字符串形式是哈希码值
	        //BigInteger(参数1,参数2) 参数1 是 1为正数 0为0 -1为负数
	        return new BigInteger(1, md.digest()).toString(16);
		} catch (NoSuchAlgorithmException e) {<!-- -->
				e.printStackTrace();
		}
		return null;
	}
}

```
- 配置数据源
```
# 配置数据源
spring:
  datasource:
    druid:
      driver-class-name: com.mysql.jdbc.Driver
      url: jdbc:mysql://localhost:3306/数据库?characterEncoding=utf-8&amp;useSSL=false
      username: 数据库用户名
      password: 数据库密码
      # 初始化容器大小
      initial-size: 1
      # 最小连接数
      min-idle: 1
      # 最大连接数
      max-active: 20

# 配置映射文件路径及实体类包名
mybatis:
  type-aliases-package: com.cy.entity
  mapper-locations: classpath:mapper/*Mapper.xml

```
- 启动类
```
@SpringBootApplication
@MapperScan("com.cy.dao")
@ComponentScan(basePackages ={<!-- -->"com.cy"})
public class ApiApplication{<!-- -->
	public static void main(String[]args) {<!-- -->
		SpringApplication.run(ApiApplication.class, args);
	}
}

```
- pom.xml
```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"&gt;
   &lt;parent&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-starter-parent&lt;/artifactId&gt;
        &lt;version&gt;2.5.12&lt;/version&gt;
        &lt;relativePath/&gt; &lt;!-- lookup parent from repository --&gt;
    &lt;/parent&gt;
    &lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;
    &lt;artifactId&gt;mapper&lt;/artifactId&gt;
    &lt;packaging&gt;jar&lt;/packaging&gt;

    &lt;properties&gt;
        &lt;java.version&gt;1.8&lt;/java.version&gt;
        &lt;mysql.version&gt;5.1.47&lt;/mysql.version&gt;
    &lt;/properties&gt;

    &lt;dependencies&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;mysql&lt;/groupId&gt;
            &lt;artifactId&gt;mysql-connector-java&lt;/artifactId&gt;
            &lt;version&gt;${mysql.version}&lt;/version&gt;
            &lt;scope&gt;runtime&lt;/scope&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;com.alibaba&lt;/groupId&gt;
            &lt;artifactId&gt;druid-spring-boot-starter&lt;/artifactId&gt;
            &lt;version&gt;1.1.10&lt;/version&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;org.mybatis.spring.boot&lt;/groupId&gt;
            &lt;artifactId&gt;mybatis-spring-boot-starter&lt;/artifactId&gt;
            &lt;version&gt;2.2.2&lt;/version&gt;
        &lt;/dependency&gt;
				
				&lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
            &lt;scope&gt;test&lt;/scope&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;io.springfox&lt;/groupId&gt;
            &lt;artifactId&gt;springfox-swagger2&lt;/artifactId&gt;
            &lt;version&gt;3.0.0&lt;/version&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;com.github.xiaoymin&lt;/groupId&gt;
            &lt;artifactId&gt;knife4j-spring-boot-starter&lt;/artifactId&gt;
            &lt;version&gt;3.0.3&lt;/version&gt;
        &lt;/dependency&gt;
    &lt;/dependencies&gt;
&lt;/project&gt;

```
- SwaggerConfig配置类
```
/**
 * 创建Swagger2的配置类
 * @Configuration 注解：表示配置类
 * @EnableSwagger2 注解：启用Swagger2
 * 1：配置生成的文档信息
 * 2：配置生成规则
 */
@Configuration
@EnableSwagger2
public class SwaggerConfig {<!-- -->
    @Bean
    public Docket getDocket() {<!-- -->

        // 创建API信息构建器
        ApiInfoBuilder apiInfoBuilder = new ApiInfoBuilder();
        // 创建标题
        apiInfoBuilder.title("接口文档说明")
                // 创建描述
                .description("SpringBoot整合Swagger2")
                // 创建版本
                .version("1.0")
                // 创建联系人
                .contact(new Contact("测试", "http://www.baidu.com", "123@qq.com"));

        // 创建ApiInfo对象
        ApiInfo apiInfo = apiInfoBuilder.build();

        // 返回指定生成的文档类型
        return new Docket(DocumentationType.SWAGGER_2)
                // 生成文档的封面信息：标题、描述、版本、联系方式
                .apiInfo(apiInfo)
                // 选择需要生成文档的接口
                .select()
                // 指定生成文档的接口范围
                .apis(RequestHandlerSelectors.basePackage("com.cy.api.controller"))
                // 对哪些请求路径生成文档：any：所有
                .paths(PathSelectors.any())
                .build();
    }
}

```

## 3.启动项目,测试结果
- swagger接口文档地址：
<img src="https://img-blog.csdnimg.cn/f6295f9fbd924ac3baf2203650f50ba0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/807953015d0f44ddb89e74de265ebe45.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">
