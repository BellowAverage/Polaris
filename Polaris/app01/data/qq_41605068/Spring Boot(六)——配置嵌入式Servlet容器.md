
--- 
title:  Spring Boot(六)——配置嵌入式Servlet容器 
tags: []
categories: [] 

---
## 一、SpringBoot默认使用Tomcat作为嵌入式的Servlet容器

### 1.1如何定制和修改Servlet容器的相关配置

    修改和server有关的配置（ServerProperties）

<img alt="" class="has" height="116" src="https://img-blog.csdnimg.cn/20200201181755965.png" width="454">

### 1.2编写一个WebServerFactoryCustomizer嵌入式的Servlet容器的定制器

```
@Bean
    public WebServerFactoryCustomizer webServerFactoryCustomizer(){
        return new WebServerFactoryCustomizer&lt;ConfigurableServletWebServerFactory&gt;() {
            @Override
            public void customize(ConfigurableServletWebServerFactory factory) {
                factory.setPort(8080);
            }
        };
    }
```

## 二、注册Servlet、Filter、Listener

由于SpringBoot默认使用的是以jar包的方式启动嵌入式的Servlet容器来启动SpringBoot的web应用，没有web.xml文件

注册三大组件用以下：

ServletRegistrationBean

```
public class MyServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        super.doPost(req, resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("***--999");
        resp.getWriter().write("hello Hello!");
    }
}
```

 

```
//注册三大组件
    @Bean
    public ServletRegistrationBean myServlet(){
        ServletRegistrationBean registrationBean = new ServletRegistrationBean(new MyServlet(), "/hello");
        return registrationBean;
    }
```

FilterRegistionBean

```
public class MyFilter implements Filter {
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {

    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {

    }

    @Override
    public void destroy() {

    }
}
```

```
@Bean
    public FilterRegistrationBean myFilter(){
        FilterRegistrationBean&lt;MyFilter&gt; registrationBean = new FilterRegistrationBean&lt;&gt;();
        registrationBean.setFilter(new MyFilter());
        registrationBean.setUrlPatterns(Arrays.asList("/hello"));
        return  registrationBean;
    } 
```

ServletListenerRegistrationBean

```
public class MyListener implements ServletContextListener {
    @Override
    public void contextInitialized(ServletContextEvent sce) {

    }

    @Override
    public void contextDestroyed(ServletContextEvent sce) {

    }
}
```

```
 @Bean
    public ServletListenerRegistrationBean myListener(){
        ServletListenerRegistrationBean&lt;MyListener&gt; registrationBean = new ServletListenerRegistrationBean&lt;&gt;();
        return  registrationBean;
    }
```

## 三、嵌入式Servlet容器启动原理

什么时候创建嵌入式的Servlet容器工厂？什么时候获取嵌入式的Servlet容器并启动Tomcat?

获取嵌入式的Servlet容器工厂：

1）、SpringBoot应用启动运行run方法；

2）、refreshContext(context)

   SpringBoot刷新IOC容器【创建IOC容器对象，并初始化容器，创建容器中的每一个组件】，如果是web应用创建AnnotationConfigEmbeddedWebApplicationContext，否则：AnnotationConfigApplicationContext

3)、refresh(context);刷新刚才创建好的IOC容器；

4）、onRefresh();web的IOC容器重写了onRefresh方法

5)、web IOC容器会创建嵌入式的Servlet容器；createEmbeddedServletContainer();

6)、获取嵌入式的servlet容器工厂：

EmbeddedServletContainerFactory con = getEmbeddedServletContainerFactory();

从IOC容器中获取EmbeddedServletContainerFactory组件，TomcatEmbeddedServletContainerFactory创建对象，后置处理器是这个对象，就会获取所有的定制器来定制Servlet容器的相关配置

7)、使用容器工厂获取嵌入式的Servlet容器：

this.embeddedServletContainer = containerFactory.getEmbeddedServletContainer(getSerlfitializer())

8)、嵌入式的servlet容器创建对象并启动Servlet容器；

先启动嵌入式的servlet容器，再将IOC容器剩下没有创建出的对象获取出来，IOC容器启动创建嵌入式的servlet容器。

## 四、优缺点

嵌入式Servlet容器：应用为可执行的jar包

优点：简单、便携

缺点：默认不支持jsp，优化定制比较复杂（使用定制器【ServerProperties、自定义EmbeddedServletContainerCustomizer】，自己编写嵌入式servlet容器的创建工厂）

## 五、使用外置servlet容器

步骤：

1）、必须创建一个war项目；

2）、将嵌入式的tomcat指定为provided;

3）、必须编写一个SpringBootServletInitializer的子类，并调用configure方法；

4）、启动服务器就可以使用；
