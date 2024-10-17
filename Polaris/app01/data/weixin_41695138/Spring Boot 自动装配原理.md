
--- 
title:  Spring Boot 自动装配原理 
tags: []
categories: [] 

---
引用：  

### Spring Boot 自动装配原理

启动类的@SpringBootApplication注解由@SpringBootConfiguration，@EnableAutoConfiguration，@ComponentScan三个注解组成，三个注解共同完成自动装配； @SpringBootConfiguration 注解标记启动类为配置类 @ComponentScan 注解实现启动时扫描启动类所在的包以及子包下所有标记为bean的类由IOC容器注册为bean @EnableAutoConfiguration通过 @Import 注解导入 AutoConfigurationImportSelector类，然后通过AutoConfigurationImportSelector 类的 selectImports 方法去读取需要被自动装配的组件依赖下的spring.factories文件配置的组件的类全名，并按照一定的规则过滤掉不符合要求的组件的类全名，将剩余读取到的各个组件的类全名集合返回给IOC容器并将这些组件注册为bean

### SpringBoot 是如何实现自动装配的？
1. 判断自动装配开关是否打开。默认spring.boot.enableautoconfiguration=true，可在 application.properties 或 application.yml 中设置1. 用于获取EnableAutoConfiguration注解中的 exclude 和 excludeName。1. 获取需要自动装配的所有配置类，读取META-INF/spring.factories 并加载之
### 如何实现一个 Starter


