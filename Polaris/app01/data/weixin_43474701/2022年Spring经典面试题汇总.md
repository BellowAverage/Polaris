
--- 
title:  2022年Spring经典面试题汇总 
tags: []
categories: [] 

---


#### 2022年Spring经典面试题大汇总
- <ul><li>- - - - - - - - - - - - - - - - - - - - - - - - - - 


> 

### 1、什么是Spring框架？Spring框架有哪些主要模块？

Spring框架是一个为Java应用程序的开发提供了综合、广泛的基础性支持的Java平台。Spring帮助开发者解决了开发中基础性的问题，使得开发人员可以专注于应用程序的开发。Spring框架本身亦是按照设计模式精心打造，这使得我们可以在开发环境中安心的集成Spring框架，不必担心Spring是如何在后台进行工作的。 Spring框架至今已集成了20多个模块。这些模块主要被分如下图所示的核心容器、数据访问/集成,、Web、AOP（面向切面编程）、工具、消息和测试模块。 <img src="https://img-blog.csdnimg.cn/5d062755f56240c095979eb4cff26040.png" alt="在这里插入图片描述">

### 2、使用Spring框架能带来哪些好处？

下面列举了一些使用Spring框架带来的主要好处： Dependency Injection(DI) 方法使得构造器和JavaBean properties文件中的依赖关系一目了然。 与EJB容器相比较，IoC容器更加趋向于轻量级。这样一来IoC容器在有限的内存和CPU资源的情况下进行应用程序的开发和发布就变得十分有利。 Spring并没有闭门造车，Spring利用了已有的技术比如ORM框架、logging框架、J2EE、Quartz和JDK Timer，以及其他视图技术。 Spring框架是按照模块的形式来组织的。由包和类的编号就可以看出其所属的模块，开发者仅仅需要选用他们需要的模块即可。 要测试一项用Spring开发的应用程序十分简单，因为测试相关的环境代码都已经囊括在框架中了。更加简单的是，利用JavaBean形式的POJO类，可以很方便的利用依赖注入来写入测试数据。 Spring的Web框架亦是一个精心设计的Web MVC框架，为开发者们在web框架的选择上提供了一个除了主流框架比如Struts、过度设计的、不流行web框架的以外的有力选项。 Spring提供了一个便捷的事务管理接口，适用于小型的本地事物处理（比如在单DB的环境下）和复杂的共同事物处理（比如利用JTA的复杂DB环境）。

### 3、什么是控制反转(IOC)？什么是依赖注入？

控制反转是应用于软件工程领域中的，在运行时被装配器对象来绑定耦合对象的一种编程技巧，对象之间耦合关系在编译时通常是未知的。在传统的编程方式中，业务逻辑的流程是由应用程序中的早已被设定好关联关系的对象来决定的。在使用控制反转的情况下，业务逻辑的流程是由对象关系图来决定的，该对象关系图由装配器负责实例化，这种实现方式还可以将对象之间的关联关系的定义抽象化。而绑定的过程是通过“依赖注入”实现的。 控制反转是一种以给予应用程序中目标组件更多控制为目的设计范式，并在我们的实际工作中起到了有效的作用。 依赖注入是在编译阶段尚未知所需的功能是来自哪个的类的情况下，将其他对象所依赖的功能对象实例化的模式。这就需要一种机制用来激活相应的组件以提供特定的功能，所以依赖注入是控制反转的基础。否则如果在组件不受框架控制的情况下，框架又怎么知道要创建哪个组件？ 在Java中依然注入有以下**三种实现方式**： 1.构造器注入 2.Setter方法注入 3.接口注入

### 4、请解释下Spring框架中的IoC？

Spring中的 org.springframework.beans 包和 org.springframework.context包构成了Spring框架IoC容器的基础。 BeanFactory 接口提供了一个先进的配置机制，使得任何类型的对象的配置成为可能。ApplicationContex接口对BeanFactory（是一个子接口）进行了扩展，在BeanFactory的基础上添加了其他功能，比如与Spring的AOP更容易集成，也提供了处理message resource的机制（用于国际化）、事件传播以及应用层的特别配置，比如针对Web应用的WebApplicationContext。 org.springframework.beans.factory.BeanFactory 是Spring IoC容器的具体实现，用来包装和管理前面提到的各种bean。BeanFactory接口是Spring IoC 容器的核心接口。

### 5、BeanFactory和ApplicationContext有什么区别？

BeanFactory 可以理解为含有bean集合的工厂类。BeanFactory 包含了种bean的定义，以便在接收到客户端请求时将对应的bean实例化。 BeanFactory还能在实例化对象的时生成协作类之间的关系。此举将bean自身与bean客户端的配置中解放出来。BeanFactory还包含了bean生命周期的控制，调用客户端的初始化方法（initialization methods）和销毁方法（destruction methods）。 从表面上看，application context如同bean factory一样具有bean定义、bean关联关系的设置，根据请求分发bean的功能。但application context在此基础上还提供了其他的功能。 1.提供了支持国际化的文本消息 2.统一的资源文件读取方式 3.已在监听器中注册的bean的事件

以下是三种较常见的 ApplicationContext 实现方式： 1、ClassPathXmlApplicationContext：从classpath的XML配置文件中读取上下文，并生成上下文定义。应用程序上下文从程序环境变量中取得。 ApplicationContext context = new ClassPathXmlApplicationContext(“bean.xml”); 2、FileSystemXmlApplicationContext ：由文件系统中的XML配置文件读取上下文。

```
ApplicationContext context = new FileSystemXmlApplicationContext(“bean.xml”);

```

3、XmlWebApplicationContext：由Web应用的XML文件读取上下文。

### 6、Spring有几种配置方式？

将Spring配置到应用开发中有以下三种方式： 1.基于XML的配置 2.基于注解的配置 3.基于Java的配置

### 7、如何用基于XML配置的方式配置Spring？

在Spring框架中，依赖和服务需要在专门的配置文件来实现，我常用的XML格式的配置文件。这些配置文件的格式通常用开头，然后一系列的bean定义和专门的应用配置选项组成。 SpringXML配置的主要目的时候是使所有的Spring组件都可以用xml文件的形式来进行配置。这意味着不会出现其他的Spring配置类型（比如声明的方式或基于Java Class的配置方式） Spring的XML配置方式是使用被Spring命名空间的所支持的一系列的XML标签来实现的。Spring有以下主要的命名空间：context、beans、jdbc、tx、aop、mvc和aso。

```
&lt;beans&gt;

    &lt;!-- JSON Support --&gt;
    &lt;bean name="viewResolver" class="org.springframework.web.servlet.view.BeanNameViewResolver"/&gt;
    &lt;bean name="jsonTemplate" class="org.springframework.web.servlet.view.json.MappingJackson2JsonView"/&gt;

    &lt;bean id="restTemplate" class="org.springframework.web.client.RestTemplate"/&gt;

&lt;/beans&gt;

```

下面这个web.xml仅仅配置了DispatcherServlet，这件最简单的配置便能满足应用程序配置运行时组件的需求。

```
&lt;web-app&gt;
  &lt;display-name&gt;Archetype Created Web Application&lt;/display-name&gt;

  &lt;servlet&gt;
        &lt;servlet-name&gt;spring&lt;/servlet-name&gt;
            &lt;servlet-class&gt;
                org.springframework.web.servlet.DispatcherServlet
            &lt;/servlet-class&gt;
        &lt;load-on-startup&gt;1&lt;/load-on-startup&gt;
    &lt;/servlet&gt;

    &lt;servlet-mapping&gt;
        &lt;servlet-name&gt;spring&lt;/servlet-name&gt;
        &lt;url-pattern&gt;/&lt;/url-pattern&gt;
    &lt;/servlet-mapping&gt;

&lt;/web-app&gt;

```

### 8、如何用基于Java配置的方式配置Spring？

Spring对Java配置的支持是由@Configuration注解和@Bean注解来实现的。由@Bean注解的方法将会实例化、配置和初始化一个新对象，这个对象将由Spring的IoC容器来管理。@Bean声明所起到的作用与 元素类似。被@Configuration所注解的类则表示这个类的主要目的是作为bean定义的资源。被@Configuration声明的类可以通过在同一个类的内部调用@bean方法来设置嵌入bean的依赖关系。 最简单的@Configuration 声明类请参考下面的代码：

```
@Configuration
public class AppConfig
{<!-- -->
    @Bean
    public MyService myService() {<!-- -->
        return new MyServiceImpl();
    }
}

```

对于上面的@Beans配置文件相同的XML配置文件如下：

```
&lt;beans&gt;
    &lt;bean id="myService" class="com.howtodoinjava.services.MyServiceImpl"/&gt;
&lt;/beans&gt;

```

上述配置方式的实例化方式如下：利用AnnotationConfigApplicationContext 类进行实例化

```
public static void main(String[] args) {<!-- -->
    ApplicationContext ctx = new AnnotationConfigApplicationContext(AppConfig.class);
    MyService myService = ctx.getBean(MyService.class);
    myService.doStuff();
}

```

要使用组件组建扫描，仅需用@Configuration进行注解即可：

```
@Configuration
@ComponentScan(basePackages = "com.howtodoinjava")
public class AppConfig  {<!-- -->
    ...
}

```

在上面的例子中，com.acme包首先会被扫到，然后再容器内查找被@Component 声明的类，找到后将这些类按照Sring bean定义进行注册。 如果你要在你的web应用开发中选用上述的配置的方式的话，需要用AnnotationConfigWebApplicationContext 类来读取配置文件，可以用来配置Spring的Servlet监听器ContrextLoaderListener或者Spring MVC的DispatcherServlet。

```
&lt;web-app&gt;
    &lt;!-- Configure ContextLoaderListener to use AnnotationConfigWebApplicationContext
        instead of the default XmlWebApplicationContext --&gt;
    &lt;context-param&gt;
        &lt;param-name&gt;contextClass&lt;/param-name&gt;
        &lt;param-value&gt;
            org.springframework.web.context.support.AnnotationConfigWebApplicationContext
        &lt;/param-value&gt;
    &lt;/context-param&gt;

    &lt;!-- Configuration locations must consist of one or more comma- or space-delimited
        fully-qualified @Configuration classes. Fully-qualified packages may also be
        specified for component-scanning --&gt;
    &lt;context-param&gt;
        &lt;param-name&gt;contextConfigLocation&lt;/param-name&gt;
        &lt;param-value&gt;com.howtodoinjava.AppConfig&lt;/param-value&gt;
    &lt;/context-param&gt;

    &lt;!-- Bootstrap the root application context as usual using ContextLoaderListener --&gt;
    &lt;listener&gt;
        &lt;listener-class&gt;org.springframework.web.context.ContextLoaderListener&lt;/listener-class&gt;
    &lt;/listener&gt;

    &lt;!-- Declare a Spring MVC DispatcherServlet as usual --&gt;
    &lt;servlet&gt;
        &lt;servlet-name&gt;dispatcher&lt;/servlet-name&gt;
        &lt;servlet-class&gt;org.springframework.web.servlet.DispatcherServlet&lt;/servlet-class&gt;
        &lt;!-- Configure DispatcherServlet to use AnnotationConfigWebApplicationContext
            instead of the default XmlWebApplicationContext --&gt;
        &lt;init-param&gt;
            &lt;param-name&gt;contextClass&lt;/param-name&gt;
            &lt;param-value&gt;
                org.springframework.web.context.support.AnnotationConfigWebApplicationContext
            &lt;/param-value&gt;
        &lt;/init-param&gt;
        &lt;!-- Again, config locations must consist of one or more comma- or space-delimited
            and fully-qualified @Configuration classes --&gt;
        &lt;init-param&gt;
            &lt;param-name&gt;contextConfigLocation&lt;/param-name&gt;
            &lt;param-value&gt;com.howtodoinjava.web.MvcConfig&lt;/param-value&gt;
        &lt;/init-param&gt;
    &lt;/servlet&gt;

    &lt;!-- map all requests for /app/* to the dispatcher servlet --&gt;
    &lt;servlet-mapping&gt;
        &lt;servlet-name&gt;dispatcher&lt;/servlet-name&gt;
        &lt;url-pattern&gt;/app/*&lt;/url-pattern&gt;
    &lt;/servlet-mapping&gt;
&lt;/web-app&gt;

```

### 9、怎样用注解的方式配置Spring？

Spring在2.5版本以后开始支持用注解的方式来配置依赖注入。可以用注解的方式来替代XML方式的bean描述，可以将bean描述转移到组件类的内部，只需要在相关类上、方法上或者字段声明上使用注解即可。注解注入将会被容器在XML注入之前被处理，所以后者会覆盖掉前者对于同一个属性的处理结果。 注解装配在Spring中是默认关闭的。所以需要在Spring文件中配置一下才能使用基于注解的装配模式。如果你想要在你的应用程序中使用关于注解的方法的话，请参考如下的配置。

```
&lt;beans&gt;

   &lt;context:annotation-config/&gt;
   &lt;!-- bean definitions go here --&gt;

&lt;/beans&gt;

```

在 context:annotation-config/标签配置完成以后，就可以用注解的方式在Spring中向属性、方法和构造方法中自动装配变量。 下面是几种比较重要的注解类型： 1.@Required：该注解应用于设值方法。 2.@Autowired：该注解应用于有值设值方法、非设值方法、构造方法和变量。 3.@Qualifier：该注解和@Autowired注解搭配使用，用于消除特定bean自动装配的歧义。 4.JSR-250 Annotations：Spring支持基于JSR-250 注解的以下注解，@Resource、@PostConstruct 和 @PreDestroy。

### 10、请解释Spring Bean的生命周期？

Spring Bean的生命周期简单易懂。在一个bean实例被初始化时，需要执行一系列的初始化操作以达到可用的状态。同样的，当一个bean不在被调用时需要进行相关的析构操作，并从bean容器中移除。 Spring bean factory 负责管理在spring容器中被创建的bean的生命周期。Bean的生命周期由两组回调（call back）方法组成。 1.初始化之后调用的回调方法。 2.销毁之前调用的回调方法。 Spring框架提供了以下四种方式来管理bean的生命周期事件： InitializingBean和DisposableBean回调接口 针对特殊行为的其他Aware接口 Bean配置文件中的Custom init()方法和destroy()方法 @PostConstruct和@PreDestroy注解方式 使用customInit()和 customDestroy()方法管理bean生命周期的代码样例如下：

```
&lt;beans&gt;
    &lt;bean id="demoBean" class="com.howtodoinjava.task.DemoBean"
            init-method="customInit" destroy-method="customDestroy"&gt;&lt;/bean&gt;
&lt;/beans&gt;

```

更多内容请参考：Spring生命周期Spring Bean Life Cycle。

### 11、Spring Bean的作用域之间有什么区别？

Spring容器中的bean可以分为5个范围。所有范围的名称都是自说明的，但是为了避免混淆，还是让我们来解释一下： 1.singleton：这种bean范围是默认的，这种范围确保不管接受到多少个请求，每个容器中只有一个bean的实例，单例的模式由bean factory自身来维护。 2.prototype：原形范围与单例范围相反，为每一个bean请求提供一个实例。 3.request：在请求bean范围内会每一个来自客户端的网络请求创建一个实例，在请求完成以后，bean会失效并被垃圾回收器回收。 4.Session：与请求范围类似，确保每个session中有一个bean的实例，在session过期后，bean会随之失效。 5.global-session：global-session和Portlet应用相关。当你的应用部署在Portlet容器中工作时，它包含很多portlet。如果你想要声明让所有的portlet共用全局的存储变量的话，那么这全局变量需要存储在global-session中。 全局作用域与Servlet中的session作用域效果相同。

### 12、什么是Spring inner beans？

在Spring框架中，无论何时bean被使用时，当仅被调用了一个属性。一个明智的做法是将这个bean声明为内部bean。内部bean可以用setter注入“属性”和构造方法注入“构造参数”的方式来实现。 比如，在我们的应用程序中，一个Customer类引用了一个Person类，我们的要做的是创建一个Person的实例，然后在Customer内部使用。

```
public class Customer
{<!-- -->
    private Person person;

    //Setters and Getters
}
public class Person
{<!-- -->
    private String name;
    private String address;
    private int age;

    //Setters and Getters
}

```

内部bean的声明方式如下：

```
&lt;bean id="CustomerBean" class="com.howtodoinjava.common.Customer"&gt;
    &lt;property name="person"&gt;
        &lt;!-- This is inner bean --&gt;
        &lt;bean class="com.howtodoinjava.common.Person"&gt;
            &lt;property name="name" value="lokesh" /&gt;
            &lt;property name="address" value="India" /&gt;
            &lt;property name="age" value="34" /&gt;
        &lt;/bean&gt;
    &lt;/property&gt;
&lt;/bean&gt;

```

### 13、Spring框架中的单例Beans是线程安全的么？

Spring框架并没有对单例bean进行任何多线程的封装处理。关于单例bean的线程安全和并发问题需要开发者自行去搞定。但实际上，大部分的Spring bean并没有可变的状态(比如Serview类和DAO类)，所以在某种程度上说Spring的单例bean是线程安全的。如果你的bean有多种状态的话（比如 View Model 对象），就需要自行保证线程安全。 最浅显的解决办法就是将多态bean的作用域由“singleton”变更为“prototype”。

### 14、请举例说明如何在Spring中注入一个Java Collection？

Spring提供了以下四种集合类的配置元素：  : 该标签用来装配可重复的list值。  : 该标签用来装配没有重复的set值。 <map>: 该标签可用来注入键和值可以为任何类型的键值对。  : 该标签支持注入键和值都是字符串类型的键值对。 下面看一下具体的例子：</map>

```
&lt;beans&gt;

   &lt;!-- Definition for javaCollection --&gt;
   &lt;bean id="javaCollection" class="com.howtodoinjava.JavaCollection"&gt;

      &lt;!-- java.util.List --&gt;
      &lt;property name="customList"&gt;
        &lt;list&gt;
           &lt;value&gt;INDIA&lt;/value&gt;
           &lt;value&gt;Pakistan&lt;/value&gt;
           &lt;value&gt;USA&lt;/value&gt;
           &lt;value&gt;UK&lt;/value&gt;
        &lt;/list&gt;
      &lt;/property&gt;

     &lt;!-- java.util.Set --&gt;
     &lt;property name="customSet"&gt;
        &lt;set&gt;
           &lt;value&gt;INDIA&lt;/value&gt;
           &lt;value&gt;Pakistan&lt;/value&gt;
           &lt;value&gt;USA&lt;/value&gt;
           &lt;value&gt;UK&lt;/value&gt;
        &lt;/set&gt;
      &lt;/property&gt;

     &lt;!-- java.util.Map --&gt;
     &lt;property name="customMap"&gt;
        &lt;map&gt;
           &lt;entry key="1" value="INDIA"/&gt;
           &lt;entry key="2" value="Pakistan"/&gt;
           &lt;entry key="3" value="USA"/&gt;
           &lt;entry key="4" value="UK"/&gt;
        &lt;/map&gt;
      &lt;/property&gt;

      &lt;!-- java.util.Properties --&gt;
    &lt;property name="customProperies"&gt;
        &lt;props&gt;
            &lt;prop key="admin"&gt;admin@nospam.com&lt;/prop&gt;
            &lt;prop key="support"&gt;support@nospam.com&lt;/prop&gt;
        &lt;/props&gt;
    &lt;/property&gt;

   &lt;/bean&gt;

&lt;/beans&gt;

```

### 15、如何向Spring Bean中注入一个Java.util.Properties？

第一种方法是使用如下面代码所示的 标签：

```
&lt;bean id="adminUser" class="com.howtodoinjava.common.Customer"&gt;

    &lt;!-- java.util.Properties --&gt;
    &lt;property name="emails"&gt;
        &lt;props&gt;
            &lt;prop key="admin"&gt;admin@nospam.com&lt;/prop&gt;
            &lt;prop key="support"&gt;support@nospam.com&lt;/prop&gt;
        &lt;/props&gt;
    &lt;/property&gt;

&lt;/bean&gt;

```

也可用”util:”命名空间来从properties文件中创建出一个propertiesbean，然后利用setter方法注入bean的引用。

### 16、请解释Spring Bean的自动装配？

在Spring框架中，在配置文件中设定bean的依赖关系是一个很好的机制，Spring容器还可以自动装配合作关系bean之间的关联关系。这意味着Spring可以通过向Bean Factory中注入的方式自动搞定bean之间的依赖关系。自动装配可以设置在每个bean上，也可以设定在特定的bean上。 下面的XML配置文件表明了如何根据名称将一个bean设置为自动装配：

```
&lt;bean id="employeeDAO" class="com.howtodoinjava.EmployeeDAOImpl" autowire="byName" /&gt;

```

除了bean配置文件中提供的自动装配模式，还可以使用@Autowired注解来自动装配指定的bean。在使用@Autowired注解之前需要在按照如下的配置方式在Spring配置文件进行配置才可以使用。 &lt;context:annotation-config /&gt; 也可以通过在配置文件中配置AutowiredAnnotationBeanPostProcessor 达到相同的效果。

```
&lt;bean class ="org.springframework.beans.factory.annotation.AutowiredAnnotationBeanPostProcessor"/&gt;

```

配置好以后就可以使用@Autowired来标注了。 @Autowired public EmployeeDAOImpl ( EmployeeManager manager ) {<!-- --> this.manager = manager; }

### 17、请解释自动装配模式的区别？

在Spring框架中共有5种自动装配，让我们逐一分析。 1.no：这是Spring框架的默认设置，在该设置下自动装配是关闭的，开发者需要自行在bean定义中用标签明确的设置依赖关系。 2.byName：该选项可以根据bean名称设置依赖关系。当向一个bean中自动装配一个属性时，容器将根据bean的名称自动在在配置文件中查询一个匹配的bean。如果找到的话，就装配这个属性，如果没找到的话就报错。 3.byType：该选项可以根据bean类型设置依赖关系。当向一个bean中自动装配一个属性时，容器将根据bean的类型自动在在配置文件中查询一个匹配的bean。如果找到的话，就装配这个属性，如果没找到的话就报错。 4.constructor：造器的自动装配和byType模式类似，但是仅仅适用于与有构造器相同参数的bean，如果在容器中没有找到与构造器参数类型一致的bean，那么将会抛出异常。 5.autodetect：该模式自动探测使用构造器自动装配或者byType自动装配。首先，首先会尝试找合适的带参数的构造器，如果找到的话就是用构造器自动装配，如果在bean内部没有找到相应的构造器或者是无参构造器，容器就会自动选择byTpe的自动装配方式。

### 18、如何开启基于注解的自动装配？

要使用 @Autowired，需要注册 AutowiredAnnotationBeanPostProcessor，可以有以下两种方式来实现： 1、引入配置文件中的下引入 context:annotation-config

```
&lt;beans&gt;
    &lt;context:annotation-config /&gt;
&lt;/beans&gt;

```

2、在bean配置文件中直接引入AutowiredAnnotationBeanPostProcessor

```
&lt;beans&gt;
    &lt;bean class="org.springframework.beans.factory.annotation.AutowiredAnnotationBeanPostProcessor"/&gt;
&lt;/beans&gt;

```

### 19、请举例解释@Required annotation？

在产品级别的应用中，IoC容器可能声明了数十万了bean，bean与bean之间有着复杂的依赖关系。设值注解方法的短板之一就是验证所有的属性是否被注解是一项十分困难的操作。可以通过在中设置“dependency-check”来解决这个问题。 在应用程序的生命周期中，你可能不大愿意花时间在验证所有bean的属性是否按照上下文文件正确配置。或者你宁可验证某个bean的特定属性是否被正确的设置。即使是用“dependency-check”属性也不能很好的解决这个问题，在这种情况下，你需要使用@Required 注解。 需要用如下的方式使用来标明bean的设值方法。

```
public class EmployeeFactoryBean extends AbstractFactoryBean&lt;Object&gt;
{<!-- -->
    private String designation;

    public String getDesignation() {<!-- -->
        return designation;
    }

    @Required
    public void setDesignation(String designation) {<!-- -->
        this.designation = designation;
    }

    //more code here
}

```

RequiredAnnotationBeanPostProcessor是Spring中的后置处理用来验证被@Required 注解的bean属性是否被正确的设置了。在使用RequiredAnnotationBeanPostProcesso来验证bean属性之前，首先要在IoC容器中对其进行注册：

```
&lt;bean class="org.springframework.beans.factory.annotation.RequiredAnnotationBeanPostProcessor" /&gt;

```

但是如果没有属性被用 @Required 注解过的话，后置处理器会抛出一个BeanInitializationException 异常。

### 20、请举例解释@Autowired注解？

@Autowired注解对自动装配何时何处被实现提供了更多细粒度的控制。@Autowired注解可以像@Required注解、构造器一样被用于在bean的设值方法上自动装配bean的属性，一个参数或者带有任意名称或带有多个参数的方法。 比如，可以在设值方法上使用@Autowired注解来替代配置文件中的 元素。当Spring容器在setter方法上找到@Autowired注解时，会尝试用byType 自动装配。 当然我们也可以在构造方法上使用@Autowired 注解。带有@Autowired 注解的构造方法意味着在创建一个bean时将会被自动装配，即便在配置文件中使用 元素。

```
public class TextEditor {<!-- -->
   private SpellChecker spellChecker;

   @Autowired
   public TextEditor(SpellChecker spellChecker){<!-- -->
      System.out.println("Inside TextEditor constructor." );
      this.spellChecker = spellChecker;
   }

   public void spellCheck(){<!-- -->
      spellChecker.checkSpelling();
   }
}

```

下面是没有构造参数的配置方式：

```
&lt;beans&gt;

   &lt;context:annotation-config /&gt;

   &lt;!-- Definition for textEditor bean without constructor-arg  --&gt;
   &lt;bean id="textEditor" class="com.howtodoinjava.TextEditor"&gt;
   &lt;/bean&gt;

   &lt;!-- Definition for spellChecker bean --&gt;
   &lt;bean id="spellChecker" class="com.howtodoinjava.SpellChecker"&gt;
   &lt;/bean&gt;

&lt;/beans&gt;

```

### 21、请举例说明@Qualifier注解？

@Qualifier注解意味着可以在被标注bean的字段上可以自动装配。Qualifier注解可以用来取消Spring不能取消的bean应用。 下面的示例将会在Customer的person属性中自动装配person的值。

```
public class Customer
{<!-- -->
    @Autowired
    private Person person;
}

```

下面我们要在配置文件中来配置Person类。

```
&lt;bean id="customer" class="com.howtodoinjava.common.Customer" /&gt;

&lt;bean id="personA" class="com.howtodoinjava.common.Person" &gt;
    &lt;property name="name" value="lokesh" /&gt;
&lt;/bean&gt;

&lt;bean id="personB" class="com.howtodoinjava.common.Person" &gt;
    &lt;property name="name" value="alex" /&gt;
&lt;/bean&gt;

```

Spring会知道要自动装配哪个person bean么？不会的，但是运行上面的示例时，会抛出下面的异常： Caused by: org.springframework.beans.factory.NoSuchBeanDefinitionException: No unique bean of type [com.howtodoinjava.common.Person] is defined: expected single matching bean but found 2: [personA, personB] 要解决上面的问题，需要使用 @Quanlifier注解来告诉Spring容器要装配哪个

```
bean：
public class Customer
{<!-- -->
    @Autowired
    @Qualifier("personA")
    private Person person;
}

```

### 22、构造方法注入和设值注入有什么区别？

请注意以下明显的区别： 1.在设值注入方法支持大部分的依赖注入，如果我们仅需要注入int、string和long型的变量，我们不要用设值的方法注入。对于基本类型，如果我们没有注入的话，可以为基本类型设置默认值。在构造方法注入不支持大部分的依赖注入，因为在调用构造方法中必须传入正确的构造参数，否则的话为报错。 2.设值注入不会重写构造方法的值。如果我们对同一个变量同时使用了构造方法注入又使用了设置方法注入的话，那么构造方法将不能覆盖由设值方法注入的值。很明显，因为构造方法尽在对象被创建时调用。 3.在使用设值注入时有可能还不能保证某种依赖是否已经被注入，也就是说这时对象的依赖关系有可能是不完整的。而在另一种情况下，构造器注入则不允许生成依赖关系不完整的对象。 4.在设值注入时如果对象A和对象B互相依赖，在创建对象A时Spring会抛出sObjectCurrentlyInCreationException异常，因为在B对象被创建之前A对象是不能被创建的，反之亦然。所以Spring用设值注入的方法解决了循环依赖的问题，因对象的设值方法是在对象被创建之前被调用的。

### 23、Spring框架中有哪些不同类型的事件？

Spring的ApplicationContext 提供了支持事件和代码中监听器的功能。 我们可以创建bean用来监听在ApplicationContext 中发布的事件。ApplicationEvent类和在ApplicationContext接口中处理的事件，如果一个bean实现了ApplicationListener接口，当一个ApplicationEvent 被发布以后，bean会自动被通知。

```
public class AllApplicationEventListener implements ApplicationListener &lt; ApplicationEvent &gt;
{<!-- -->
    @Override
    public void onApplicationEvent(ApplicationEvent applicationEvent)
    {<!-- -->
        //process event
    }
}

```

Spring 提供了以下5中标准的事件： 1.上下文更新事件（ContextRefreshedEvent）：该事件会在ApplicationContext被初始化或者更新时发布。也可以在调用ConfigurableApplicationContext 接口中的refresh()方法时被触发。 2.上下文开始事件（ContextStartedEvent）：当容器调用ConfigurableApplicationContext的Start()方法开始/重新开始容器时触发该事件。 3.上下文停止事件（ContextStoppedEvent）：当容器调用ConfigurableApplicationContext的Stop()方法停止容器时触发该事件。 4.上下文关闭事件（ContextClosedEvent）：当ApplicationContext被关闭时触发该事件。容器被关闭时，其管理的所有单例Bean都被销毁。 5.请求处理事件（RequestHandledEvent）：在Web应用中，当一个http请求（request）结束触发该事件。 除了上面介绍的事件以外，还可以通过扩展ApplicationEvent 类来开发自定义的事件。

```
public class CustomApplicationEvent extends ApplicationEvent
{<!-- -->
    public CustomApplicationEvent ( Object source, final String msg )
    {<!-- -->
        super(source);
        System.out.println("Created a Custom event");
    }
}
为了监听这个事件，还需要创建一个监听器：
public class CustomEventListener implements ApplicationListener &lt; CustomApplicationEvent &gt;
{<!-- -->
    @Override
    public void onApplicationEvent(CustomApplicationEvent applicationEvent) {<!-- -->
        //handle event
    }
}

```

之后通过applicationContext接口的publishEvent()方法来发布自定义事件。 CustomApplicationEvent customEvent = new CustomApplicationEvent(applicationContext, “Test message”); applicationContext.publishEvent(customEvent);

### 24、FileSystemResource和ClassPathResource有何区别？

在FileSystemResource 中需要给出spring-config.xml文件在你项目中的相对路径或者绝对路径。在ClassPathResource中spring会在ClassPath中自动搜寻配置文件，所以要把ClassPathResource 文件放在ClassPath下。 如果将spring-config.xml保存在了src文件夹下的话，只需给出配置文件的名称即可，因为src文件夹是默认。 简而言之，ClassPathResource在环境变量中读取配置文件，FileSystemResource在配置文件中读取配置文件。

### 25、Spring 框架中都用到了哪些设计模式？

Spring框架中使用到了大量的设计模式，下面列举了比较有代表性的： 代理模式—在AOP和remoting中被用的比较多。 单例模式—在spring配置文件中定义的bean默认为单例模式。 模板方法—用来解决代码重复的问题。 比如. RestTemplate, JmsTemplate, JpaTemplate。 前端控制器—Srping提供了DispatcherServlet来对请求进行分发。 视图帮助(View Helper )—Spring提供了一系列的JSP标签，高效宏来辅助将分散的代码整合在视图里。 依赖注入—贯穿于BeanFactory / ApplicationContext接口的核心理念。 工厂模式—BeanFactory用来创建对象的实例。

### 26、Spring事务的隔离级别
1. ISOLATION_DEFAULT： 这是一个PlatfromTransactionManager默认的隔离级别，使用数据库默认的事务隔离级别. 另外四个与JDBC的隔离级别相对应1. ISOLATION_READ_UNCOMMITTED： 这是事务最低的隔离级别，它充许令外一个事务可以看到这个事务未提交的数据。 这种隔离级别会产生脏读，不可重复读和幻像读。1. ISOLATION_READ_COMMITTED： 保证一个事务修改的数据提交后才能被另外一个事务读取。另外一个事务不能读取该事务未提交的数据1. ISOLATION_REPEATABLE_READ： 这种事务隔离级别可以防止脏读，不可重复读。但是可能出现幻像读。 它除了保证一个事务不能读取另一个事务未提交的数据外，还保证了避免下面的情况产生(不可重复读)。1. ISOLATION_SERIALIZABLE 这是花费最高代价但是最可靠的事务隔离级别。事务被处理为顺序执行。 除了防止脏读，不可重复读外，还避免了幻像读。
其中的一些概念的说明： 脏读: 指当一个事务正在访问数据，并且对数据进行了修改，而这种修改还没有提交到数据库中，这时，另外一个事务也访问这个数据，然后使用了这个数据。因为这个数据是还没有提交的数据， 那么另外一 个事务读到的这个数据是脏数据，依据脏数据所做的操作可能是不正确的。 不可重复读: 指在一个事务内，多次读同一数据。在这个事务还没有结束时，另外一个事务也访问该同一数据。 那么，在第一个事务中的两次读数据之间，由于第二个事务的修改，那么第一个事务两次读到的数据可能是不一样的。这样就发生了在一个事务内两次读到的数据是不一样的，因此称为是不可重复读。 幻觉读: 指当事务不是独立执行时发生的一种现象，例如第一个事务对一个表中的数据进行了修改，这种修改涉及 到表中的全部数据行。同时，第二个事务也修改这个表中的数据，这种修改是向表中插入一行新数据。那么，以后就会发生操作第一个事务的用户发现表中还有没有修改的数据行，就好象发生了幻觉一样。

### 27、你对 Spring 的理解。

1.Spring 实现了工厂模式的工厂类（在这里有必要解释清楚什么是工厂模式），这个类名为 BeanFactory（实际上是一个接口），在程序中通常 BeanFactory 的子类 ApplicationContext。 Spring 相当于一个大的工厂类，在其配置文件中通过元素配置用于创建实例对象的 类名和实例对象的属性。 2. Spring 提供了对 IOC 良好支持，IOC 是一种编程思想，是一种架构艺术，利用这种思想 可以很好地实现模块之间的解耦。IOC 也称为 DI（Depency Injection），什么叫依赖注入呢？ 譬如，

```
Class Programmer
{<!-- --> 
 Computer computer =null;
 public void code()
 {<!-- --> 
 //Computercomputer = new IBMComputer();
 //Computercomputer = beanfacotry.getComputer();
 computer.write();
 } 
 public voidsetComputer(Computer computer)
 {<!-- --> 
 this.computer= computer;
 } 
} 

```

另外两种方式都由依赖，第一个直接依赖于目标类，第二个把依赖转移到工厂上，第三个彻 底与目标和工厂解耦了。在 spring 的配置文件中配置片段如下：

```
&lt;bean id=”computer” class=”cn.itcast.interview.Computer”&gt; 
&lt;/bean&gt;
 
&lt;bean id=”programmer” class=”cn.itcast.interview.Programmer”&gt; 
 &lt;property name=”computer” ref=”computer”&gt;&lt;/property&gt;
&lt;/bean&gt;

```
1. Spring 提供了对 AOP 技术的良好封装， AOP 称为面向切面编程，就是系统中有很多各 不相干的类的方法，在这些众多方法中要加入某种系统功能的代码，例如，加入日志，加入 权限判断，加入异常处理，这种应用称为 AOP。实现 AOP 功能采用的是代理技术，客户端 程序不再调用目标，而调用代理类，代理类与目标类对外具有相同的方法声明，有两种方式 可以实现相同的方法声明，一是实现相同的接口，二是作为目标的子类在，JDK 中采用 Proxy 类产生动态代理的方式为某个接口生成实现类，如果要为某个类生成子类，则可以用 CGLI B。在生成的代理类的方法中加入系统功能和调用目标类的相应方法，系统功能的代理以 Advice 对象进行提供，显然要创建出代理对象，至少需要目标类和 Advice 类。spring 提供 了这种支持，只需要在 spring 配置文件中配置这两个元素即可实现代理和 aop 功能，例如，
```
&lt;bean id=”proxy” type=”org.spring.framework.aop.ProxyBeanFactory”&gt; 
 &lt;property name=”target”ref=””&gt;&lt;/property&gt;
 &lt;property name=”advisor”ref=””&gt;&lt;/property&gt;
 
&lt;/bean&gt;

```
