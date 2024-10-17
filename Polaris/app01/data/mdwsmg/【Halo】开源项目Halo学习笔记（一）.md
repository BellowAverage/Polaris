
--- 
title:  【Halo】开源项目Halo学习笔记（一） 
tags: []
categories: [] 

---
##### 开源项目Halo学习笔记（一）

Halo是GitHub上的开源项目，现代化的个人独立博客系统。  笔记为学习笔记，欢迎指出任何问题。本篇做到对Halo有一个大致的了解。希望自己能学完，少打两局游戏。



#### 目录
- <ul><li><ul><li><ul><li>- <ul><li>


#### (一):项目启动

###### 项目启动遇到的错误
- **JDK版本错误**
>  
 Execution failed for task ‘:compileJava’. Could not target platform: ‘Java SE 11’ using tool chain: ‘JDK 8 (1.8)’. 


修改Gradle JVM 为对应版本<img src="https://img-blog.csdnimg.cn/2021012811295649.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 修改运行设置，一定要记得，不然就会有下面第二个错误？

<img src="https://img-blog.csdnimg.cn/20210128115217835.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210128115221824.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">
- **@Deprecated 注释错误** <img src="https://img-blog.csdnimg.cn/20210128114113749.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 可以看到源码里名没有 since 、forRemoval，百度得知这两个元素为java 9新增。
>  
 @Documented @Retention(RetentionPolicy.RUNTIME) @Target(value={CONSTRUCTOR, FIELD, LOCAL_VARIABLE, METHOD, PACKAGE, PARAMETER, TYPE}) public @interface Deprecated {<!-- --> } 


项目启动了，嗯，还是报错，很气 <img src="https://img-blog.csdnimg.cn/20210128235656869.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 有看到前辈说要开启 h2的远程访问。没想明白，不开了，先启动

>  
 h2:  console:  settings:   web-allow-others: false #是否启用远程访问,说要改成true  path: /h2-console  enabled: false 


#### (二):项目配置学习
- **关于配置信息** 下面是大佬整理的**Halo配置文件详解**。好用，爱您。 
这是一份多此一举的注释版本

>  
 server:  port: 8090  forward-headers-strategy: native #处理X-Forwarded- For标头的策略  compression:   enabled: false #是否开启压缩功能，简单理解为将传输的json压小 spring:  mvc:   pathmatch:    use-suffix-pattern: true  jackson:   date-format: yyyy-MM-dd HH:mm:ss  devtools:   add-properties: false #是否启用开发属性默认值，生产环境是禁用的（部署后用户访问的环境）  output:   ansi:    enabled: always # 配置ANSI输出,控制字符样式，大可不必  datasource:   type: com.zaxxer.hikari.HikariDataSource   # H2 database configuration.   driver-class-name: org.h2.Driver   url: jdbc:h2:file:~/.halo/db/halo   username: admin   password: 123456  h2:   console:    settings:     web-allow-others: false #是否启用远程访问    path: /h2-console #浏览器地址栏输入对应路径，就可以访问h2数据库详细操作    enabled: false #是否启用控制台  jpa:   hibernate:    ddl-auto: update # 每次运行程序，没有表格会新建表格，表内有数据不会清空，只会更新（自动建表就是这个 ddl-auto 啦）   show-sql: false   open-in-view: false  flyway:   enabled: false #数据库版本管理，可同步数据库，resources下的migration就是，事务回滚只对DML有用  servlet:   multipart: #上载文件的中间位置。 也就是系统临时缓存目录。    max-file-size: 10240MB #档案大小上限。    max-request-size: 10240MB #最大请求大小 。    location: /tmp/run.halo.app management:  endpoints: #实行器特性 监控、管理   web:    base-path: /api/admin/actuator #Web端点的基本路径    exposure:     include: [ ‘httptrace’, ‘metrics’,‘env’,‘logfile’,‘health’ ] #应当包含的端点ID，或全部包含的（这样 /actuator/） logging:  level: #日志级别严重性映射   run.halo.app: INFO   org.eclipse.jetty.server.HttpChannel: ERROR  file: #日志存放位置   path: ${user.home}/.halo/logs springfox:  documentation: enabled: false #在生产环境下，我们需要关闭swagger配置，避免暴露接口的这种危险行为 halo:  download-timeout: 5m #资源下载超时设置,听说有状况，不关心，搁置了  cache: memory 

- **关于依赖信息** 简单梳理了一下各依赖作用，Markdown的 $ 符号已经声明了，所以**代码块里的$前后有空格**，不然会这样
>  
 <p>//githubAPI接口 implementation "org.kohsuke:github-api: 
      
       
        
        
          g 
         
        
          i 
         
        
          t 
         
        
          h 
         
        
          u 
         
        
          b 
         
        
          A 
         
        
          p 
         
        
          i 
         
        
          V 
         
        
          e 
         
        
          r 
         
        
          s 
         
        
          i 
         
        
          o 
         
        
          n 
         
        
          " 
         
        
          / 
         
        
          / 
         
        
          S 
         
        
          p 
         
        
          r 
         
        
          i 
         
        
          n 
         
        
          g 
         
        
          B 
         
        
          o 
         
        
          o 
         
        
          t 
         
        
       
         githubApiVersion" // SpringBoot 
        
       
     githubApiVersion"//SpringBoot  
      
       
        
        
          C 
         
        
          h 
         
        
          a 
         
        
          n 
         
        
          g 
         
        
          e 
         
        
          t 
         
        
          o 
         
        
          a 
         
        
          d 
         
        
          i 
         
        
          f 
         
        
          f 
         
        
          e 
         
        
          r 
         
        
          e 
         
        
          n 
         
        
          t 
         
        
          f 
         
        
          o 
         
        
          n 
         
        
          t 
         
        
       
         Change to a different font 
        
       
     Changetoadifferentfont</p> 


依赖梳理

>  
 //githubAPI接口 implementation “org.kohsuke:github-api: $ githubApiVersion” // SpringBoot implementation “org.springframework.boot:spring-boot-starter-actuator” implementation “org.springframework.boot:spring-boot-starter-data-jpa” implementation “org.springframework.boot:spring-boot-starter-web” // jetty代替tomcat implementation “org.springframework.boot:spring-boot-starter-jetty” implementation “org.springframework.boot:spring-boot-starter-freemarker” implementation ‘org.springframework.boot:spring-boot-starter-validation’ // java邮件发送 implementation “com.sun.mail:jakarta.mail” // hutool implementation “cn.hutool:hutool-core: $ hutoolVersion” implementation “cn.hutool:hutool-crypto: $ hutoolVersion” implementation “cn.hutool:hutool-extra: $ hutoolVersion” // 又拍云 implementation “com.upyun:java-sdk: $ upyunSdkVersion” // 七牛云 implementation “com.qiniu:qiniu-java-sdk: $ qiniuSdkVersion” // 阿里云 对象存储OSS implementation “com.aliyun.oss:aliyun-sdk-oss: $ aliyunSdkVersion” // 百度智能云 implementation “com.baidubce:bce-java-sdk: $ baiduSdkVersion” // 腾讯云 对象存储COS implementation “com.qcloud:cos_api: $ qcloudSdkVersion” // 华为云 implementation “com.huaweicloud:esdk-obs-java: $ huaweiObsVersion” // 基于Apache License v2.0开源协议的对象存储服务 implementation “io.minio:minio:$minioSdkVersion” // swagger文档 implementation “io.springfox:springfox-boot-starter: $ swaggerVersion” // 文件上传 implementation “commons-fileupload:commons-fileupload: $ commonsFileUploadVersion” // 各种类型文件的 Utils处理包 implementation “org.apache.commons:commons-lang3: $ commonsLangVersion” // http 服务调用 implementation “org.apache.httpcomponents:httpclient: $ httpclientVersion” // Jackson implementation “com.fasterxml.jackson.dataformat:jackson-dataformat-yaml: $ dataformatYamlVersion” // Java程序中使用Git implementation “org.eclipse.jgit:org.eclipse.jgit: $ jgitVersion” // Java代码Bug分析 implementation “com.google.code.findbugs:annotations: $ annotationsVersion” // flexmark 将MarkDown转为HTML 等功能 implementation “com.vladsch.flexmark:flexmark: $ flexmarkVersion” implementation “com.vladsch.flexmark:flexmark-ext-attributes: $ flexmarkVersion” implementation “com.vladsch.flexmark:flexmark-ext-autolink: $ flexmarkVersion” implementation “com.vladsch.flexmark:flexmark-ext-emoji: $ flexmarkVersion” implementation “com.vladsch.flexmark:flexmark-ext-escaped-character: $ flexmarkVersion” implementation “com.vladsch.flexmark:flexmark-ext-gfm-strikethrough: $ flexmarkVersion” implementation “com.vladsch.flexmark:flexmark-ext-gfm-tasklist: $ flexmarkVersion” implementation “com.vladsch.flexmark:flexmark-ext-ins: $ flexmarkVersion” implementation “com.vladsch.flexmark:flexmark-ext-media-tags: $ flexmarkVersion” implementation “com.vladsch.flexmark:flexmark-ext-tables: $ flexmarkVersion” implementation “com.vladsch.flexmark:flexmark-ext-toc: $ flexmarkVersion” implementation “com.vladsch.flexmark:flexmark-ext-superscript: $ flexmarkVersion” implementation “com.vladsch.flexmark:flexmark-ext-yaml-front-matter: $ flexmarkVersion” implementation “com.vladsch.flexmark:flexmark-ext-gitlab: $ flexmarkVersion” // 生成缩略图 implementation “net.coobird:thumbnailator: $ thumbnailatorVersion” // image4j 主要用于bmp文件生成，bmp转ico，ico转bmp implementation “net.sf.image4j:image4j: $ image4jVersion” // flyway 数据库版本管理 implementation “org.flywaydb:flyway-core: $ flywayVersion” // 用Java实现的一维/二维条码图像处理库，支持在图像中解码和生成条形码 implementation “com.google.zxing:core: $ zxingVersion” // Leveldb是一个google实现的非常高效的key-value数据库 implementation “org.iq80.leveldb:leveldb: $ levelDbVersion” // Java编写的数据库，支持嵌入式数据库、内存数据库、只读数据库 runtimeOnly “com.h2database:h2: $ h2Version” // Mysql runtimeOnly “mysql:mysql-connector-java” // lombok compileOnly “org.projectlombok:lombok” annotationProcessor “org.projectlombok:lombok” testCompileOnly “org.projectlombok:lombok” testAnnotationProcessor “org.projectlombok:lombok” // junit testImplementation(“org.springframework.boot:spring-boot-starter-test”) {<!-- --> exclude group: ‘org.junit.vintage’, module: ‘junit-vintage-engine’ } // devtools developmentOnly “org.springframework.boot:spring-boot-devtools” 

