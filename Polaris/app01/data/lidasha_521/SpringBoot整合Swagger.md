
--- 
title:  SpringBoot整合Swagger 
tags: []
categories: [] 

---


#### 文章目录
- - <ul><li>- - - - 


## SpringBoot整合Swagger

>  
 **前后端分离,接口需要及时协同** 


>  
 swagger是一个用于生成服务器接口的规范性文档、并且能够对接口进行测试的工具 


### 1.Swagger的作用
- 生成接口说明文档- 对接口进行测试
### 2.SpringBoot整合Swagger
- 2.1.添加依赖（Swagger2 \ Swagger UI )
```
&lt;!-- https://mvnrepository.com/artifact/io.springfox/springfox-swagger2 --&gt;
&lt;dependency&gt;
    &lt;groupId&gt;io.springfox&lt;/groupId&gt;
    &lt;artifactId&gt;springfox-swagger2&lt;/artifactId&gt;
    &lt;version&gt;2.9.2&lt;/version&gt;
&lt;/dependency&gt;

&lt;!-- https://mvnrepository.com/artifact/io.springfox/springfox-swagger-ui --&gt;
&lt;dependency&gt;
    &lt;groupId&gt;io.springfox&lt;/groupId&gt;
    &lt;artifactId&gt;springfox-swagger-ui&lt;/artifactId&gt;
    &lt;version&gt;2.9.2&lt;/version&gt;
&lt;/dependency&gt;

```
- 2.2.新建`config`文件夹添加`SwaggerConfig`类，如图
<img src="https://img-blog.csdnimg.cn/ef5c95cb6c5b435f8fcc00e95e09073c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

```
package com.example.api.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

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
                .apis(RequestHandlerSelectors.basePackage("com.example.api.controller"))
                // 对哪些请求路径生成文档：any：所有
                .paths(PathSelectors.any())
                .build();
    }
}

```

### 3.查看/测试生成的接口说明文档
-  3.1.启动SpringBoot项目，访问： <img src="https://img-blog.csdnimg.cn/43fc46b969da418d8f2d2abc24afc786.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <li> 3.2.对接口进行测试 
  <ul>-  3.2.1.找到想要测试接口,点击 `Try out` 按钮 <img src="https://img-blog.csdnimg.cn/51282d6e258d4f9b967c67135f31adeb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> -  3.2.2.输入参数，点击`Execute`执行 <img src="https://img-blog.csdnimg.cn/1a2b7d8dde1647f38f9870c18f8c9fb3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> -  3.2.3.发送请求返回的响应结果 <img src="https://img-blog.csdnimg.cn/47ccd45e884f4de1b748b80a2ca7a7b9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 
### 4.Swagger常用注解说明
- `@API`：请求类的说明 —&gt; 用于`controller`类上- `@ApiOperation`：方法的说明 —&gt; 用于`方法`的上面- `@ApiImplicitParams`：用在请求的方法上, 包含一组参数说明 —&gt; 用于`方法`的上面<li>`@ApiImplicitParam`：对单个参数的说明，包含以下属性 
  <ul>- `name`：参数名- `value`：参数的汉字说明, 解释- `required`：参数是否必须传- `paramType`：参数放在哪个地方- `dataType`： 参数类型, 默认 String, 其它值 dataType="Integer”- `defaultValue`：参数的默认值- `code`：状态码，如200、400、401等- `message`：信息，例如"请求成功”- `response`：抛出异常的类
```
@RestController
@Api(tags = "用户管理模块" ,value = "该参数没什么意义, 所以不需要配置")
public class UserController{<!-- -->

	@Resource
    private UserDAO userDAO;

    @PostMapping("getUserInfo")
	@ApiOperation(value = "根据用户名获取用户信息接口")
	@ApiImplicitParams({<!-- -->
       	@ApiImplicitParam(name = "userName", value = "用户名", required = true, dataType = "String", paramType = "query", defaultValue = "Tony")
  		})
	@ApiResponses({<!-- -->
		@ApiResponse(code = 200, message = "成功"),
       	@ApiResponse(code = 500, message = "失败")
   	})
	public User getUserInfo(String userName){<!-- -->
			return userDAO.getUserInfo(userName);
	}
}

```
- `@ApiModel`：用在 JavaBean 类上，说明 JavaBean 的 用途- `@ApiModelProperty`：用在 JavaBean 类的属性上面，说明此属性的的含议
```
@ApiModel(value = "User", description = "用户实体类")
public class User implements Serializable{<!-- -->
	@ApiModelProperty(value = "用户名")
	private String userName;
    @ApiModelProperty(value = "密码")
	private String passWord;
}

```
- `@ApiIgnore`：忽略某个接口，不生成在Swagger的接口说明文档中- 整体结果展示
<img src="https://img-blog.csdnimg.cn/349d6c3059c940afac372ea7df09ae0a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 5.原始页面太丑，换个页面
- springfox-swagger-ui 的界面长这个样子，说实话，确实略显丑陋。- 改成改良后的 Knife4j 不仅在界面上更加优雅、炫酷，功能上也更加强大：后端 Java 代码和前端 UI 模块分离了出来，在微服务场景下更加灵活；更提供了专注于 Swagger 的增强解决方案.
```
&lt;!-- 将原来的springfox-swagger2版本改成3.0.0，解决以下版本兼容性问题 --&gt;
&lt;dependency&gt;
    &lt;groupId&gt;io.springfox&lt;/groupId&gt;
    &lt;artifactId&gt;springfox-swagger2&lt;/artifactId&gt;
    &lt;version&gt;3.0.0&lt;/version&gt;
&lt;/dependency&gt;

&lt;!-- 将原来的springfox-swagger-ui版本改成knife4j-spring-boot-starter --&gt;
&lt;dependency&gt;
    &lt;groupId&gt;com.github.xiaoymin&lt;/groupId&gt;
    &lt;artifactId&gt;knife4j-spring-boot-starter&lt;/artifactId&gt;
    &lt;version&gt;3.0.3&lt;/version&gt;
&lt;/dependency&gt;

```
- 再来看一下效果，访问： 是不是好了很多啊，完毕撒花
<img src="https://img-blog.csdnimg.cn/0b02646983244c36a739f67872a734bd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">
