
--- 
title:  Swagger 
tags: []
categories: [] 

---
## 一、引入依赖 

```
        &lt;dependency&gt;
            &lt;groupId&gt;io.springfox&lt;/groupId&gt;
            &lt;artifactId&gt;springfox-swagger2&lt;/artifactId&gt;
            &lt;version&gt;2.9.2&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;io.springfox&lt;/groupId&gt;
            &lt;artifactId&gt;springfox-swagger-ui&lt;/artifactId&gt;
            &lt;version&gt;2.9.2&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
        &lt;/dependency&gt;
```

## 二、配置

```
@Configuration
@EnableSwagger2
public class SwaggerConfig {
    @Bean
    public Docket createRestApi() {
        return new Docket(DocumentationType.SWAGGER_2)
                .pathMapping("/")
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.example.photo.controller"))
                .paths(PathSelectors.any())
                .build().apiInfo(new ApiInfoBuilder()
                        .title("证件照相关文档")
                        .description("证件照切换背景色，查询相关图片")
                        .version("1.0")
                        .contact(
                                new Contact("证件照",
                                "https://market.aliyun.com/products/57124001/cmapi030523.html?spm=5176.730005.productlist.d_cmapi030523.15783524Ns28FE&amp;innerSource=search_证件照制作#sku=yuncode2452300008",
                                        "aaa@gmail.com"))
                        .license("详细信息")
                        .licenseUrl("http://www.baidu.com")
                        .build());
    }
```

>  
 访问地址： 


<img alt="" height="359" src="https://img-blog.csdnimg.cn/20210226164511717.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

##  三、相关注解

>  
 @Api() 用于类；表示标识这个类是swagger的资源 tags–表示说明 value–也是说明，可以使用tags替代 但是tags如果有多个值，会生成多个list 


>  
  @ApiOperation() 用于方法；表示一个http请求的操作 value用于方法描述 notes用于提示内容 tags可以重新分组（视情况而用） 


>  
  @ApiParam() 用于方法，参数，字段说明；表示对参数的添加元数据（说明或是否必填等） name–参数名 value–参数说明 required–是否必填 


>  
 @ApiModel()用于类 ；表示对类进行说明，用于参数用实体类接收 value–表示对象名 description–描述 都可省略 


>  
 @ApiModelProperty()用于方法，字段； 表示对model属性的说明或者数据操作更改 value–字段说明 name–重写属性名字 dataType–重写属性类型 required–是否必填 example–举例说明 hidden–隐藏 


>  
 @ApiIgnore()用于类或者方法上，可以不被swagger显示在页面上 比较简单, 这里不做举例 


>  
 @ApiImplicitParam() 用于方法 表示单独的请求参数 


>  
 @ApiImplicitParams() 用于方法，包含多个 @ApiImplicitParam name–参数ming value–参数说明 dataType–数据类型 paramType–参数类型 example–举例说明 


```
 @ApiOperation("查询测试")
  @GetMapping("select")
  //@ApiImplicitParam(name="name",value="用户名",dataType="String", paramType = "query")
  @ApiImplicitParams({
  @ApiImplicitParam(name="name",value="用户名",dataType="string", paramType = "query",example="xingguo"),
  @ApiImplicitParam(name="id",value="用户id",dataType="long", paramType = "query")})
  public void select(){
  }

```

 

 
