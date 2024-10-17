
--- 
title:  spring boot 使用笔记 
tags: []
categories: [] 

---
### 一、配置视图解析
1.  在resources文件夹下新建static文件夹（用来储存静态资源） <li> 配置application.yml <pre><code>spring:
	  mvc:
		view:
  			prefix: /
  			suffix: .html
</code></pre> </li>1.  将html页面存放在static文件夹下 
### Spring Boot：拦截器与过滤器

**一、拦截器与过滤器** 在讲Spring boot之前，我们先了解一下过滤器和拦截器。这两者在功能方面很类似，但是在具体技术实现方面，差距还是比较大的。在分析两者的区别之前，我们先理解一下AOP的概念，AOP不是一种具体的技术，而是一种编程思想。在面向对象编程的过程中，我们很容易通过继承、多态来解决纵向扩展。 但是对于横向的功能，比如，在所有的service方法中开启事务，或者统一记录日志等功能，面向对象的是无法解决的。所以AOP——面向切面编程其实是面向对象编程思想的一个补充。而我们今天讲的过滤器和拦截器都属于面向切面编程的具体实现。而两者的主要区别包括以下几个方面：

1.Filter的执行由Servlet容器回调完成，而拦截器通常通过动态代理的方式来执行。 2. Filter的执行由Servlet容器回调完成，而拦截器通常通过动态代理的方式来执行。 3. Filter的生命周期由Servlet容器管理，而拦截器则可以通过IoC容器来管理，因此可以通过注入等方式来获取其他Bean的实例，因此使用会更方便。

**二、过滤器的配置** 现在我们通过过滤器来实现记录请求执行时间的功能，其实现如下：

```
public class LogCostFilter implements Filter {
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
 
    }
 
    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        long start = System.currentTimeMillis();
        filterChain.doFilter(servletRequest,servletResponse);
        System.out.println("Execute cost="+(System.currentTimeMillis()-start));
    }
 
    @Override
    public void destroy() {
 
    }
}

```

这段代码的逻辑比较简单，就是在方法执行前先记录时间戳，然后通过过滤器链完成请求的执行，在返回结果之间计算执行的时间。这里需要主要，这个类必须继承Filter类，这个是Servlet的规范，这个跟以前的Web项目没区别。但是，有了过滤器类以后，以前的web项目可以在web.xml中进行配置，但是spring boot项目并没有web.xml这个文件，那怎么配置？在Spring boot中，我们需要FilterRegistrationBean来完成配置。其实现过程如下：

```
@Configuration
public class FilterConfig {
 
    @Bean
    public FilterRegistrationBean registFilter() {
        FilterRegistrationBean registration = new FilterRegistrationBean();
        registration.setFilter(new LogCostFilter());
        registration.addUrlPatterns("/*");
        registration.setName("LogCostFilter");
        registration.setOrder(1);
        return registration;
    }
 
}

```

这样配置就完成了，需要配置的选项主要包括实例化Filter类，然后指定url的匹配模式，设置过滤器名称和执行顺序，这个过程和在web.xml中配置其实没什么区别，只是形式不同而已。现在我们可以启动服务器访问任意URL： 　<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWFnZXMyMDE3LmNuYmxvZ3MuY29tL2Jsb2cvODIwNDA2LzIwMTgwMS84MjA0MDYtMjAxODAxMjkyMzExNTAzMTItNDY1NjkzNzE1LnBuZw?x-oss-process=image/format,png" alt="在这里插入图片描述"> 　大家可以看到上面的配置已经生效了。除了通过 FilterRegistrationBean 来配置以外，还有一种更直接的办法，直接通过注解就可以完成了：

```
@WebFilter(urlPatterns = "/*", filterName = "logFilter2")
public class LogCostFilter2 implements Filter {
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
 
    }
 
    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        long start = System.currentTimeMillis();
        filterChain.doFilter(servletRequest, servletResponse);
        System.out.println("LogFilter2 Execute cost=" + (System.currentTimeMillis() - start));
    }
 
    @Override
    public void destroy() {
 
    }
}

```

这里直接用@WebFilter就可以进行配置，同样，可以设置url匹配模式，过滤器名称等。这里需要注意一点的是@WebFilter这个注解是Servlet3.0的规范，并不是Spring boot提供的。除了这个注解以外，我们还需在配置类中加另外一个注解：@ServletComponetScan，指定扫描的包。

```
@SpringBootApplication
@MapperScan("com.pandy.blog.dao")
@ServletComponentScan("com.pandy.blog.filters")
public class Application {
    public static void main(String[] args) throws Exception {
        SpringApplication.run(Application.class, args);
    }
}

```

现在，我们再来访问一下任意URL： 　<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWFnZXMyMDE3LmNuYmxvZ3MuY29tL2Jsb2cvODIwNDA2LzIwMTgwMS84MjA0MDYtMjAxODAxMjkyMzIxMzAwNDYtMTkwNTIzOTMwNi5wbmc?x-oss-process=image/format,png" alt="在这里插入图片描述"> 　可以看到，我们配置的两个过滤器都生效了。细心的读者会发现，第二个Filter我们并没有指定执行的顺序，但是却在第一个Filter之前执行。这里需要解释一下，@WebFilter这个注解并没有指定执行顺序的属性，其执行顺序依赖于Filter的名称，是根据Filter类名（注意不是配置的filter的名字）的字母顺序倒序排列，并且@WebFilter指定的过滤器优先级都高于FilterRegistrationBean配置的过滤器。有兴趣的朋友可以自己实验一下。

**三、拦截器的配置** 上面我们已经介绍了过滤器的配置方法，接下来我们再来看看如何配置一个拦截器。我们使用拦截器来实现上面同样的功能，记录请求的执行时间。首先我们实现拦截器类：

```
public class LogCostInterceptor implements HandlerInterceptor {
    long start = System.currentTimeMillis();
    @Override
    public boolean preHandle(HttpServletRequest httpServletRequest, HttpServletResponse httpServletResponse, Object o) throws Exception {
        start = System.currentTimeMillis();
        return true;
    }
 
    @Override
    public void postHandle(HttpServletRequest httpServletRequest, HttpServletResponse httpServletResponse, Object o, ModelAndView modelAndView) throws Exception {
        System.out.println("Interceptor cost="+(System.currentTimeMillis()-start));
    }
 
    @Override
    public void afterCompletion(HttpServletRequest httpServletRequest, HttpServletResponse httpServletResponse, Object o, Exception e) throws Exception {
    }
}

```

这里我们需要实现HandlerInterceptor这个接口，这个接口包括三个方法，preHandle是请求执行前执行的，postHandler是请求结束执行的，但只有preHandle方法返回true的时候才会执行，afterCompletion是视图渲染完成后才执行，同样需要preHandle返回true，该方法通常用于清理资源等工作。除了实现上面的接口外，我们还需对其进行配置：

```
@Configuration
public class InterceptorConfig extends WebMvcConfigurerAdapter {
 
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new LogCostInterceptor()).addPathPatterns("/**");
        super.addInterceptors(registry);
    }
}

```

这里我们继承了WebMVCConfigurerAdapter，看过前面的文章的朋友应该已经见过这个类了，在进行静态资源目录配置的时候我们用到过这个类。这里我们重写了addInterceptors这个方法，进行拦截器的配置，主要配置项就两个，一个是指定拦截器，第二个是指定拦截的URL。现在我们再启动系统访问任意一个URL： <img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWFnZXMyMDE3LmNuYmxvZ3MuY29tL2Jsb2cvODIwNDA2LzIwMTgwMS84MjA0MDYtMjAxODAxMzAwMDM4NTE4NTktMjE0MDI1NzA3My5wbmc?x-oss-process=image/format,png" alt="在这里插入图片描述">

可以看到，我们通过拦截器实现了同样的功能。不过这里还要说明一点的是，其实这个实现是有问题的，因为preHandle和postHandle是两个方法，所以我们这里不得不设置一个共享变量start来存储开始值，但是这样就会存在线程安全问题。当然，我们可以通过其他方法来解决，比如通过ThreadLocal就可以很好的解决这个问题，有兴趣的同学可以自己实现。不过通过这一点我们其实可以看到，虽然拦截器在很多场景下优于过滤器，但是在这种场景下，过滤器比拦截器实现起来更简单。

**四、总结** 拦截器这一段主要对基于Spring boot对过滤器和拦截器的配置进行的讲解。无论是过滤器还是拦截器都属于AOP（面向切面编程）思想的具体实现。除了这两种实现我们还见过另一种更灵活的AOP实现技术，即Aspect，我们可以通过Aspect来完成更多更强大的功能。这个后续再给大家分享。

### 实例类注解

**时间注解**

```
@DateTimeFormat(pattern = "时间格式")

yml文件配置
spring: 
	jackson:
    	date-format: yyyy-MM-dd
    	joda-date-time-format: yyyy-MM-dd HH:mm:ss

```

### SpringBoot 参数校验的方法
- @AssertFalse 所注解的元素必须是Boolean类型，且值为false- @AssertTrue 所注解的元素必须是Boolean类型，且值为true- @DecimalMax 所注解的元素必须是数字，且值小于等于给定的值- @DecimalMin 所注解的元素必须是数字，且值大于等于给定的值- @Digits 所注解的元素必须是数字，且值必须是指定的位数- @Future 所注解的元素必须是将来某个日期- @Max 所注解的元素必须是数字，且值小于等于给定的值- @Min 所注解的元素必须是数字，且值小于等于给定的值- @Range 所注解的元素需在指定范围区间内- @NotNull 所注解的元素值不能为null- @NotBlank 所注解的元素值有内容- @Null 所注解的元素值为null- @Past 所注解的元素必须是某个过去的日期- @PastOrPresent 所注解的元素必须是过去某个或现在日期- @Pattern 所注解的元素必须满足给定的正则表达式- @Size 所注解的元素必须是String、集合或数组，且长度大小需保证在给定范围之内- @Email 所注解的元素需满足Email格式
**在controller层的参数校验可以分为两种场景：**
1. 单个参数校验1. 实体类参数校验
### 单个参数校验

```
@RestController
@Validated
public class PingController {

    @GetMapping("/getUser")
    public String getUserStr(@NotNull(message = "name 不能为空") String name,
                             @Max(value = 99, message = "不能大于99岁") Integer age) {
        return "name: " + name + " ,age:" + age;
    }
}

```

当处理**GET**请求时或只传入少量参数的时候，我们可能不会建一个bean来接收这些参数，就可以像上面这样直接在**controller**方法的参数中进行校验。

>  
 注意：这里一定要在方法所在的controller类上加入@Validated注解，不然没有任何效果。 这时候在**postman**输入请求： 


```
http://localhost:8080/getUser?name=Allan&amp;age=101

```

调用方会收到springboot默认的格式报错：

```
{
    "timestamp": "2019-06-01T04:30:26.882+0000",
    "status": 500,
    "error": "Internal Server Error",
    "message": "getUserStr.age: 不能大于99岁",
    "path": "/getUser"
}

```

```
javax.validation.ConstraintViolationException: getUserStr.age: 不能大于99岁
   at org.springframework.validation.beanvalidation.MethodValidationInterceptor.invoke(MethodValidationInterceptor.java:116)
   at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:185)
   at org.springframework.aop.framework.CglibAopProxy$DynamicAdvisedInterceptor.intercept(CglibAopProxy.java:688)
   at io.shopee.bigdata.penalty.server.controller.PingController$$EnhancerBySpringCGLIB$$232cfd51.getUserStr(&lt;generated&gt;)
   ...

```

具体详情参考：

### 项目报错 统一处理 （刘俊秦是本人，请忽略）

>  
 当我们开发项目，经常需要捕获很多异常时，几乎每个接口都需要重写很多捕获代码。（本人就很烦，所有写了一个统一处理的方法） 怎么处理呢，我们可以扫码包下全部的Controller 的异常。捕获它，进行我们的异常处理。springboot 就提供了一个注解 


```
/*
 * 功能描述: 
 * 〈统一异常处理〉
 * 
 * @param null 1
 * @return : 
 * @author : ljq-刘俊秦
 * @date : 2020/5/16 0016 下午 5:05
 */

@ControllerAdvice(
        //指定拦截包的控制器
        basePackages = {<!-- -->"com.*.*.controller.*"},
        //限定被标注为@Controller或者@RestController的类才被拦截
        annotations = {<!-- -->Controller.class, RestController.class}
)
public class ControllerExHandler {<!-- -->

    //异常处理，可以定义异常类型进行拦截处理
    @ExceptionHandler(value = BaseException.class)
    @ResponseBody
    //定义为服务器错误状态码
    @ResponseStatus(HttpStatus.OK)
    public ServiceResult baseException(BaseException e) {<!-- -->
        return ServiceResult.failure(e.getCode(), e.getMessage());
    }

    //ex异常处理，可以定义异常类型进行拦截处理
    @ExceptionHandler(value = Exception.class)
    @ResponseBody
    //定义为服务器错误状态码
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ServiceResult exception(Exception e) {<!-- -->
        LogPrintUtil.logRunTimeError(e);
        return ServiceResult.failure(ReturnCode.FAILURE);
    }

    //io异常处理，可以定义异常类型进行拦截处理
    @ExceptionHandler(value = IOException.class)
    @ResponseBody
    //定义为服务器错误状态码
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ServiceResult ioException(IOException e) {<!-- -->
        LogPrintUtil.logRunTimeError(e);
        return ServiceResult.failure(ReturnCode.JAVA_IO);
    }

}

```

### Springboot用@PathVariable传参，最后一个参数会丢失小数点后面的部分

>  
 当使用@PathVariable传递路径参数时，竟然神奇的发现，后面一位参数的小数点后面部分竟然不见啦，如下代码： 


**Controller方法注解如下：**

```
@RequestMapping(value = "/user/findPassword/{email}", method = RequestMethod.GET, produces="application/json")

```

>  
 我这里是想传递个邮箱过来的，然后就发现了没有邮箱后缀。 百思不得其解，遂百度之，解决方法如下： 


```
@RequestMapping(value = "/user/findPassword/{email:.+}", method = RequestMethod.GET, produces="application/json")

```

### get请求对象参数的接收方式

>  
 可以使用@ModelAttribute注解 


```
    @GetMapping("/page")
    public ApiResult&lt;IPage&lt;OutboundResp&gt;&gt; page(@ModelAttribute OutboundPageSearchReq searchReq) {<!-- -->
        searchReq.setTenantId(ContextHolder.getContext().getTenantId());
        return ApiResult.success(weftYarnOutboundService.findPage(searchReq));
    }

```
