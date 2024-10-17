
--- 
title:  Spring Boot(一)——入门 
tags: []
categories: [] 

---
**目录**























## 一、简介

Spring Boot来简化Spring应用开发，约定大于配置，去繁从简，just run就能创建一个独立的，产品级别的应用。

       Spring Boot -&gt;J2EE一站式解决方案        Spring Cloud -&gt;分布式整体解决方案

优点:

 -快速创建独立运行的Spring项目以及与主流框架集成；

 -使用嵌入式的Servlet容器，应用无需打成WAR包；

 -starters自动依赖与版本控制；(场景启动器)

 -大量的自动配置，简化开发，也可修改默认值；

 -无需配置xml，无代码生成，开箱即用；

 -准生产环境的运行时应用监控；

 -与云计算的天然集成；

## 二、微服务

2014 年 Martin Fowler 发的一篇博客。一个应用应该是一组小型服务，可以通过HTTP的方式进行互通。

微服务:架构风格(服务微化)

每一个功能单元最终都是一个可独立替换的独立升级的软件单元，形成应用网(和神经元相似)

#### （Hello World!）

<img alt="" class="has" height="132" src="https://img-blog.csdnimg.cn/20200119213232970.png" width="255">

<img alt="" class="has" height="186" src="https://img-blog.csdnimg.cn/20200119213255653.png" width="355">

<img alt="" class="has" height="144" src="https://img-blog.csdnimg.cn/20200119213317603.png" width="930">

## 三、深究

### 3.1@SpringBootApplication

 Spring Boot应用标注在某个类上说明这个类是SpringBoot的主配置类，SpringBoot就应该运行这个类的main方法来启动SpringBoot应用

```
/*
@SpringBootApplication 来标注一个主程序类，说明这是一个spring boot应用
 */
@SpringBootApplication
public class AppMain {
    public static void main(String[] args) {
        //Spring 应用启动起来
        SpringApplication.run(AppMain.class,args);
    }
}
```

          @SpringBootApplication内部:

```
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@SpringBootConfiguration
@EnableAutoConfiguration
@ComponentScan(
    excludeFilters = {@Filter(
    type = FilterType.CUSTOM,
    classes = {TypeExcludeFilter.class}
), @Filter(
    type = FilterType.CUSTOM,
    classes = {AutoConfigurationExcludeFilter.class}
)}
)
```

### 3.1.1@SpringBootConfiguration：Spring Boot的配置类:

标注在某个类上，表示这是一个Spring Boot的配置类；

### 3.1.2@Configuration：配置类上标注这个注解

     配置类也就是配置文件，也是容器中的一个组件:@Component

### 3.1.3@EnableAutoConfiguration：开启自动配置功能

以前我们需要配置的东西，Spring Boot帮我们自动配置，@EnableAutoConfiguration告诉SpringBoot开启自动配置功能；这样自动配置才能生效；

内部如下:

```
@AutoConfigurationPackage
@Import({AutoConfigurationImportSelector.class})
public @interface EnableAutoConfiguration {<!-- -->
```

### 3.1.3.1@AutoConfigurationPackage：自动配置包

 Spring的底层注解@Import，给容器中导入一个组件的选择器；

#### 将主配置类(@SpringBootApplication标注的类)的所在包及下面所有子包里面的所有组件扫描到spring容器；

会给容器导入非常多的自动配置类(***AutoConfiguration)，就是给容器中导入这个场景需要的所有组件，并配置好这些组件

有了自动配置类，免去了我们手动编写配置注入功能组件等工作，spring boot在启动的时候从类路径下的META-INF/spring.factories中获取EnableAutoConfiguration指定的值，将这些值作为自动配置类导入到容器中，自动配置类就生效，帮我们进行自动配置工作。

在  **<u>**spring-boot-autoconfigure-2.1.3.RELEASE.jar**</u>** 里给我们配置好了

## 四、使用Spring Initializer快速创建Spring Boot项目

<img alt="" class="has" height="102" src="https://img-blog.csdnimg.cn/20200119212212579.png" width="270">

static:保存所有的静态资源:js css images

templates：保存所有的模板页面；（spring boot默认jar包使用嵌入式的Tomcat，默认不支持jsp页面），可以使用模板引擎(freemarker、thymeleaf)；

application.properties：Spring Boot应用的配置文件。   比如:server.port=8081
