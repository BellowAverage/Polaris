
--- 
title:  Spring Boot(四)——web开发 
tags: []
categories: [] 

---
**目录**









































































## 一、简介

### 1.1步骤

1）、新建SpringBoot应用，选中需要的模块；

2）、SpringBoot已经默认将这些场景配置好了，只需要在配置文件中指定少量配置就可以运行；

3）、自己编写业务代码；

### 1.2SpringBoot帮我们配置了什么？

```
******AutoConfiguration： 帮我们给容器中自动配置组件
******Properties：        配置类来封装配置文件的内容
```

## 二、SpringBoot对静态资源的映射规则

可以看WebMvcAutoConfiguration里

```
 public void addResourceHandlers(ResourceHandlerRegistry registry) {
            if (!this.resourceProperties.isAddMappings()) {
                logger.debug("Default resource handling disabled");
            } else {
                Duration cachePeriod = this.resourceProperties.getCache().getPeriod();
                CacheControl cacheControl = this.resourceProperties.getCache().getCachecontrol().toHttpCacheControl();
                if (!registry.hasMappingForPattern("/webjars/**")) {
                    this.customizeResourceHandlerRegistration(registry.addResourceHandler(new String[]{"/webjars/**"}).addResourceLocations(new String[]{"classpath:/META-INF/resources/webjars/"}).setCachePeriod(this.getSeconds(cachePeriod)).setCacheControl(cacheControl));
                }

                String staticPathPattern = this.mvcProperties.getStaticPathPattern();
                if (!registry.hasMappingForPattern(staticPathPattern)) {
                    this.customizeResourceHandlerRegistration(registry.addResourceHandler(new String[]{staticPathPattern}).addResourceLocations(WebMvcAutoConfiguration.getResourceLocations(this.resourceProperties.getStaticLocations())).setCachePeriod(this.getSeconds(cachePeriod)).setCacheControl(cacheControl));
                }

            }
        }
```

### 2.1** /webjars/****

都去 **classpath:/META-INF/resources/webjars/找资源；**

**其中：**webjars：以jar包的方式引入静态资源；官网:（springboot是通过webjars管理静态资源）

比如访问:Jquery

        1）、添加依赖:

```
&lt;!--引入jquery的webjar--&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.webjars&lt;/groupId&gt;
            &lt;artifactId&gt;jquery&lt;/artifactId&gt;
            &lt;version&gt;3.1.1&lt;/version&gt;
        &lt;/dependency&gt;
```

     2）、就可以看见:

<img alt="" class="has" height="208" src="https://img-blog.csdnimg.cn/20200121211159178.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="464">

    3）、访问:

### 2.2 /**  如果访问的资源未知，会去以下文件夹里面找

```
"classpath:/META-INF/resources/"
"classpath:/resources/"
"classpath:/static/"
"classpath:/public/"
```

### 2.3欢迎页 映射配置

<img alt="" class="has" height="270" src="https://img-blog.csdnimg.cn/20200121215519938.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="971">

### 2.4图标修改 favicon.ico

 （当然可通过 spring.resources.static-location = 来修改资源文件路径）

## 三、模板引擎

### 3.1背景

以前开发，我们需要将HTML转换为jsp页面，转jsp的好处就是，我们可以用&lt;c:foreach&gt;等，也能写java代码。

而springboot首先以jar包的方式，不是war包方式，其次，我们使用的是嵌入式的tomcat，默认是不支持jsp。

因此呢，springboot推荐使用模板引擎。

模板引擎的作用就是:页面上的某些值是动态的，我们用一些表达式表示，这些值从哪来呢？我们组装一些数据，然后把页面模板和数据交给模板引擎，模板引擎将数据填充到对应位置，生成一个最终内容，显示出来。

### 3.2springboot推荐的Thymeleaf

语法简单、功能强大

### 3.3引入Thymeleaf

```
&lt;dependency&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-starter-thymeleaf&lt;/artifactId&gt;
&lt;/dependency&gt;
```

### 3.4Thymeleaf使用&amp;语法

####       3.4.1源码，原理

```
public class ThymeleafProperties {
    private static final Charset DEFAULT_ENCODING;
    public static final String DEFAULT_PREFIX = "classpath:/templates/";
    public static final String DEFAULT_SUFFIX = ".html";
    private boolean checkTemplate = true;
    private boolean checkTemplateLocation = true;
    private String prefix = "classpath:/templates/";  //只要放在这个路径下就能自动渲染了
    private String suffix = ".html";
    private String mode = "HTML";

```

      官网：

####  3.4.2使用

  1）导入thymeleaf的名称空间

```
&lt;html lang="en" xmlns:th="http://www.thymeleaf.org"&gt;
```

2）放数据

<img alt="" class="has" height="122" src="https://img-blog.csdnimg.cn/20200122122959391.png" width="610">

3）显示

<img alt="" class="has" height="57" src="https://img-blog.csdnimg.cn/20200122123043962.png" width="313">

#### 3.4.3语法规则

<img alt="" class="has" height="456" src="https://img-blog.csdnimg.cn/20200122174313418.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="721">

表达式:     4 Standard Expression Syntax

```
Simple expressions:   //表达式语法
        Variable Expressions: ${...}   //获取值  OGNL
            //1.获取对象的属性、调用方法
            //2.使用内置的基本对象
                //#ctx : the context object.
                //#vars: the context variables.
                //#locale : the context locale.
                //#request : (only in Web Contexts) the HttpServletRequest object. ${session.foo}
                //#response : (only in Web Contexts) the HttpServletResponse object.
                //#session : (only in Web Contexts) the HttpSession object.
                //#servletContext : (only in Web Contexts) the ServletContext object.
            //3.内置的工具对象
                //#execInfo : information about the template being processed.
                //#messages : methods for obtaining externalized messages inside variables expressions, in the same way as they
                would be obtained using #{…} syntax.
                //#uris : methods for escaping parts of URLs/URIs
                //#conversions : methods for executing the configured conversion service (if any).
                //#dates : methods for java.util.Date objects: formatting, component extraction, etc.
                //#calendars : analogous to #dates , but for java.util.Calendar objects.
                //#numbers : methods for formatting numeric objects.
                //#strings : methods for String objects: contains, startsWith, prepending/appending, etc.
                //#objects : methods for objects in general.
                //#bools : methods for boolean evaluation.
                //#arrays : methods for arrays.
                //#lists : methods for lists.
                //#sets : methods for sets.
                //#maps : methods for maps.
                //#aggregates : methods for creating aggregates on arrays or collections.
                //#ids : methods for dealing with id attributes that might be repeated (for example, as a result of an iteration).

        Selection Variable Expressions: *{...}   //选择表达式，和${}一样，
        //补充：配合th:Object 使用
        Message Expressions: #{...}     //获取国际化内容
        Link URL Expressions: @{...}     //定义url
        //&lt;!-- Will produce '/gtvg/order/details?orderId=3' (plus rewriting) --&gt;
        //    &lt;a href="details.html" th:href="@{/order/details(orderId=${o.id})}"&gt;view&lt;/a&gt;
        Fragment Expressions: ~{...}    //片段表达式
Literals    //字面量
        Text literals: 'one text' , 'Another one!' ,…
        Number literals: 0 , 34 , 3.0 , 12.3 ,…
        Boolean literals: true , false
        Null literal: null
        Literal tokens: one , sometext , main ,…
Text operations:   //文本操作
        String concatenation: +
        Literal substitutions: |The name is ${name}|
Arithmetic operations:  //数字运算
        Binary operators: + , - , * , / , %
        Minus sign (unary operator): -
Boolean operations:  //布尔运算
        Binary operators: and , or
        Boolean negation (unary operator): ! , not
Comparisons and equality:  //比较运算
        Comparators: &gt; , &lt; , &gt;= , &lt;= ( gt , lt , ge , le )
        Equality operators: == , != ( eq , ne )
Conditional operators:     //条件运算   （三元运算符）
        If-then: (if) ? (then)
        If-then-else: (if) ? (then) : (else)
        Default: (value) ?: (defaultvalue)
Special tokens:   //不操作写 -
    No-Operation: _
```

演示:

<img alt="" class="has" height="130" src="https://img-blog.csdnimg.cn/20200122205515468.png" width="668">

<img alt="" class="has" height="472" src="https://img-blog.csdnimg.cn/20200122205304869.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="687"><img alt="" class="has" height="417" src="https://img-blog.csdnimg.cn/20200122205434416.png" width="196">

## 四、Spring MVC auto-configuration



<img alt="" class="has" height="256" src="https://img-blog.csdnimg.cn/2020012221285558.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

## 五、如何修改SpringBoot的默认配置

模式:

<img alt="" class="has" height="155" src="https://img-blog.csdnimg.cn/2020012221370244.png" width="1200">

1)、SpringBoot在自动化配置很多组件的时候，先看容器中有没有用户自己配置的(@Bean @Component)如果有就用用户自己配置的，如果没有，才自动配置，如果有些组件可以有多个(ViewResolver）将用户配置的和自己默认的组合起来

## 六、扩展SpringMvc

编写一个配置类(@Configuration)，是WebMvcConfigurerAdapter类型，不能标注@EnableWebMvc

即保留了自动配置，也可以使用自定义的配置。

<img alt="" class="has" height="181" src="https://img-blog.csdnimg.cn/20200122214645483.png" width="651">

原理:

      1)、WebMvcAutoConfiguration是SpringMvc自动配置类；

      2)、在做其他自动配置时会导入:@Import(EnableWebMvcConfiguration.class)；

      3)、容器中所有的WebMvcConfiguration会一起起作用；

      4)、我们的配置类也会被调用。

## 七、全面接管SpringMvc

springboot对springmvc的自动配置就不需要了，所有都是我们自己配，那么在配置类中加@EnableWebMvc即可。

原理:

```
@Import({DelegatingWebMvcConfiguration.class})
public @interface EnableWebMvc {
}
```

```
@Configuration(
    proxyBeanMethods = false
)
public class DelegatingWebMvcConfiguration extends WebMvcConfigurationSupport {<!-- -->
```

```
@Configuration(
    proxyBeanMethods = false
)
@ConditionalOnWebApplication(
    type = Type.SERVLET
)
@ConditionalOnClass({Servlet.class, DispatcherServlet.class, WebMvcConfigurer.class})
@ConditionalOnMissingBean({WebMvcConfigurationSupport.class}) //容器中没有这个组件的时候，这个自动配置类才生效
@AutoConfigureOrder(-2147483638)
@AutoConfigureAfter({DispatcherServletAutoConfiguration.class, TaskExecutionAutoConfiguration.class, ValidationAutoConfiguration.class})
public class WebMvcAutoConfiguration {<!-- -->
```

@EnableWebMvc将WebMvcConfigurationSupport组件导入进来；

导入的WebMvcConfigurationSupport只是Springmvc最基本的功能；

## 八、实际使用

### 8.1引入依赖

```
&lt;!--引入BootStarp的webjar--&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.webjars&lt;/groupId&gt;
            &lt;artifactId&gt;bootstrap&lt;/artifactId&gt;
            &lt;version&gt;4.4.1&lt;/version&gt;
        &lt;/dependency&gt;
```

### 8.2页面引用

```
&lt;html lang="en"  xmlns:th="http://www.thymeleaf.org"&gt;     &lt;!--引入 --&gt;
	&lt;head&gt;
		&lt;meta http-equiv="Content-Type" content="text/html; charset=UTF-8"&gt;
		&lt;meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"&gt;
		&lt;meta name="description" content=""&gt;
		&lt;meta name="author" content=""&gt;
		&lt;title&gt;Signin Template for Bootstrap&lt;/title&gt;
		&lt;!-- Bootstrap core CSS    --&gt; &lt;!--引用 --&gt;
		&lt;link th:href="@{/webjars/bootstrap/4.4.1/css/bootstrap.css}" rel="stylesheet"&gt;
		&lt;!-- Custom styles for thiss template --&gt;&lt;!-- 自定义css文件  任意一个方式都行--&gt;
		&lt;link href="asserts/css/signin.css" th:href="@{/asserts/css/signin.css}" rel="stylesheet"&gt;    
	&lt;/head&gt;
```

好处:会自动修改引用路径!

### 8.3国际化

#### 8.3.1编写国际化配置文件

<img alt="" class="has" height="113" src="https://img-blog.csdnimg.cn/2020012413491087.png" width="601">

<img alt="" class="has" height="217" src="https://img-blog.csdnimg.cn/20200124135108835.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="793">

<img alt="" class="has" height="249" src="https://img-blog.csdnimg.cn/20200124135203371.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="503">

<img alt="" class="has" height="613" src="https://img-blog.csdnimg.cn/20200124135411596.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="655">

结果：

<img alt="" class="has" height="195" src="https://img-blog.csdnimg.cn/2020012414014948.png" width="652">

### 8.3.2使用ResourceBundleMessageSource管理国际化资源文件

```
@Configuration(
    proxyBeanMethods = false
)
@ConditionalOnMissingBean(
    name = {"messageSource"},
    search = SearchStrategy.CURRENT
)
@AutoConfigureOrder(-2147483648)
@Conditional({MessageSourceAutoConfiguration.ResourceBundleCondition.class})
@EnableConfigurationProperties
public class MessageSourceAutoConfiguration {
    private static final Resource[] NO_RESOURCES = new Resource[0];

    public MessageSourceAutoConfiguration() {
    }

    @Bean
    @ConfigurationProperties(
        prefix = "spring.messages"
    )
    public MessageSourceProperties messageSourceProperties() {
        return new MessageSourceProperties();
    }

    @Bean
    public MessageSource messageSource(MessageSourceProperties properties) {
        ResourceBundleMessageSource messageSource = new ResourceBundleMessageSource();
        if (StringUtils.hasText(properties.getBasename())) {
//设置国际化资源文件的基础名(去掉语言国家代码的)
            messageSource.setBasenames(StringUtils.commaDelimitedListToStringArray(StringUtils.trimAllWhitespace(properties.getBasename())));
        }

        if (properties.getEncoding() != null) {
            messageSource.setDefaultEncoding(properties.getEncoding().name());
        }

        messageSource.setFallbackToSystemLocale(properties.isFallbackToSystemLocale());
        Duration cacheDuration = properties.getCacheDuration();
        if (cacheDuration != null) {
            messageSource.setCacheMillis(cacheDuration.toMillis());
        }

        messageSource.setAlwaysUseMessageFormat(properties.isAlwaysUseMessageFormat());
        messageSource.setUseCodeAsDefaultMessage(properties.isUseCodeAsDefaultMessage());
        return messageSource;
    }

    protected static class ResourceBundleCondition extends SpringBootCondition {
        private static ConcurrentReferenceHashMap&lt;String, ConditionOutcome&gt; cache = new ConcurrentReferenceHashMap();

        protected ResourceBundleCondition() {
        }

        public ConditionOutcome getMatchOutcome(ConditionContext context, AnnotatedTypeMetadata metadata) {
//通过 spring.messages.basename 指定文件
            String basename = context.getEnvironment().getProperty("spring.messages.basename", "messages");
            ConditionOutcome outcome = (ConditionOutcome)cache.get(basename);
            if (outcome == null) {
                outcome = this.getMatchOutcomeForBasename(context, basename);
                cache.put(basename, outcome);
            }

            return outcome;
        }
```

#### 8.3.3在页面使用国际化内容

看参考**3.4.3**知：#{}来获取

国际化Locale（区域信息对象），LocaleResolver（获取区域信息对象）

原理：

```
@Bean
        @ConditionalOnMissingBean
        @ConditionalOnProperty(
            prefix = "spring.mvc",
            name = {"locale"}
        )
        public LocaleResolver localeResolver() {
            if (this.mvcProperties.getLocaleResolver() == org.springframework.boot.autoconfigure.web.servlet.WebMvcProperties.LocaleResolver.FIXED) {
                return new FixedLocaleResolver(this.mvcProperties.getLocale());
            } else {
                AcceptHeaderLocaleResolver localeResolver = new AcceptHeaderLocaleResolver();
                localeResolver.setDefaultLocale(this.mvcProperties.getLocale());
                return localeResolver;
            }
        }

//默认的就是根据request带来的区域信息获取Local进行国际化
```

定义自己的Locale：

<img alt="" class="has" height="344" src="https://img-blog.csdnimg.cn/20200124151937870.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1039">

加入到容器：

<img alt="" class="has" height="105" src="https://img-blog.csdnimg.cn/20200124152030565.png" width="489">

#### 8.3.4html代码：

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"  xmlns:th="http://www.thymeleaf.org"&gt;
	&lt;head&gt;
		&lt;meta http-equiv="Content-Type" content="text/html; charset=UTF-8"&gt;
		&lt;meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"&gt;
		&lt;meta name="description" content=""&gt;
		&lt;meta name="author" content=""&gt;
		&lt;title&gt;Signin Template for Bootstrap&lt;/title&gt;
		&lt;!-- Bootstrap core CSS --&gt;
		&lt;link th:href="@{/webjars/bootstrap/4.4.1/css/bootstrap.css}" rel="stylesheet"&gt;
		&lt;!-- Custom styles for thiss template --&gt;
		&lt;link th:href="@{/asserts/css/signin.css}" rel="stylesheet"&gt;
	&lt;/head&gt;
	&lt;body class="text-center"&gt;
		&lt;form class="form-signin" action="dashboard.html" method="post"&gt;
			&lt;img class="mb-4" th:src="@{/asserts/img/bootstrap-solid.svg}"  alt="" width="72" height="72"&gt;
			&lt;h1 class="h3 mb-3 font-weight-normal" th:text="#{login.tip}" &gt;Please sign in&lt;/h1&gt;
			&lt;label class="sr-only" th:text="#{login.username}"&gt;Username&lt;/label&gt;
			&lt;input type="text"  name="username" class="form-control" placeholder="Username" th:placeholder="#{login.username}" required="" autofocus=""&gt;
			&lt;label class="sr-only" th:text="#{login.password}" &gt;Password&lt;/label&gt;
			&lt;input type="password" name="password" class="form-control" placeholder="Password" th:placeholder="#{login.password}"  required=""&gt;
			&lt;div class="checkbox mb-3"&gt;
				&lt;label&gt;
					&lt;!--行内 表达式--&gt;
          			&lt;input type="checkbox" value="remember-me"/&gt; [[#{login.remember}]]
        		&lt;/label&gt;
			&lt;/div&gt;
			&lt;button class="btn btn-lg btn-primary btn-block" type="submit" th:text="#{login.btn}" &gt;Sign in&lt;/button&gt;
			&lt;p class="mt-5 mb-3 text-muted"&gt;© 2017-2018&lt;/p&gt;
			&lt;a class="btn btn-sm" th:href="@{/login.html(l='zh_CN')}" &gt;中文&lt;/a&gt;
			&lt;a class="btn btn-sm" th:href="@{/login.html(l='en_US')}"&gt;English&lt;/a&gt;
		&lt;/form&gt;
	&lt;/body&gt;

&lt;/html&gt;
```

#### 8.3.5效果

<img alt="" class="has" height="494" src="https://img-blog.csdnimg.cn/20200124152255724.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="372"><img alt="" class="has" height="479" src="https://img-blog.csdnimg.cn/20200124152421352.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="338">

## 九、模板引擎实时生效

### 9.1禁用缓存

```
spring.thymeleaf.cache=false
```

### 9.2重新编译: Ctrl + F9

### 9.3登录错误信息提示

```
&lt;p style="color: red" th:text="${msg}" th:if="${not #strings.isEmpty(msg)}"&gt;&lt;/p&gt;
```

### 9.4拦截器进行登录检查

```
/*
*登录检查
 *  */
public class LoginHandlerInterceptor implements HandlerInterceptor {
    //目标方法执行之前
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        Object user = request.getSession().getAttribute("loginUser");
        if(user == null){
            request.setAttribute("msg","没有权限请先登录!");
            request.getRequestDispatcher("/index.html").forward(request,response);
            return false;
        }
        return true;
    }

    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {

    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {

    }
}

```

```
@Bean
    public WebMvcConfigurer webMvcConfigurerAdapter(){
        return new WebMvcConfigurer(){
            @Override
            public void addViewControllers(ViewControllerRegistry registry) {
                registry.addViewController("/").setViewName("login");
                registry.addViewController("/index.html").setViewName("login");
                registry.addViewController("/main.html").setViewName("dashboard");
            }

            @Override
            public void addInterceptors(InterceptorRegistry registry) {
                registry.addInterceptor(new LoginHandlerInterceptor()).addPathPatterns("/**")
                        .excludePathPatterns("/","/index.html","/asserts/**","/webjars/**","/user/login");
            }
        };
    }
```

## 十、SpringBoot参数验证

Controller：

```
@GetMapping(value = "/page")
    public Result&lt;Order&gt;  list(@RequestBody @Valid Order order, BindingResult results) throws Exception {
       	if(results.hasErrors(){
       		return results.getFieldError().getDefaultMessage();
       	}
        return "success";
    }
```

```
​@Null  //被注释的元素必须为null
@NotNull  //被注释的元素不能为null
@AssertTrue  //被注释的元素必须为true
@AssertFalse  //被注释的元素必须为false
@Min(value)  //被注释的元素必须是一个数字，其值必须大于等于指定的最小值
@Max(value)  //被注释的元素必须是一个数字，其值必须小于等于指定的最大值
@DecimalMin(value)  //被注释的元素必须是一个数字，其值必须大于等于指定的最小值
@DecimalMax(value)  //被注释的元素必须是一个数字，其值必须小于等于指定的最大值
@Size(max,min)  //被注释的元素的大小必须在指定的范围内。
@Digits(integer,fraction)  //被注释的元素必须是一个数字，其值必须在可接受的范围内
@Past  //被注释的元素必须是一个过去的日期
@Future  //被注释的元素必须是一个将来的日期
@Pattern(value) //被注释的元素必须符合指定的正则表达式。
@Email //被注释的元素必须是电子邮件地址
@Length //被注释的字符串的大小必须在指定的范围内
@NotEmpty  //被注释的字符串必须非空
@Range  //被注释的元素必须在合适的范围内

```

```
@NotNull：不能为null，但可以为empty

@NotEmpty：不能为null，而且长度必须大于0

@NotBlank：只能作用在String上，不能为null，而且调用trim()后，长度必须大于0
```

## 十一、开发热部署

引入依赖：

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-devtools&lt;/artifactId&gt;
    &lt;scope&gt;runtime&lt;/scope&gt;
    &lt;optional&gt;true&lt;/optional&gt;
&lt;/dependency&gt;
```

添加maven插件

```
&lt;build&gt;
    &lt;plugins&gt;
      &lt;plugin&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-maven-plugin&lt;/artifactId&gt;
        &lt;configuration&gt;
          &lt;fork&gt;true&lt;/fork&gt;
          &lt;addResources&gt;true&lt;/addResources&gt;
        &lt;/configuration&gt;
      &lt;/plugin&gt;
    &lt;/plugins&gt;
  &lt;/build&gt;
```

开启自动编译的权限

<img alt="" height="567" src="https://img-blog.csdnimg.cn/20200715204625548.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

使用快捷键：ctrl+shift+alt+/，选择：

<img alt="" height="392" src="https://img-blog.csdnimg.cn/20200715204842867.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="960">

<img alt="" height="317" src="https://img-blog.csdnimg.cn/20200715204925615.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

<img alt="" height="85" src="https://img-blog.csdnimg.cn/20200715205001603.png" width="900">

重启IDEA，当修改完成后 ctrl+s后，便可自动运行。
