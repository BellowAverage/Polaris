
--- 
title:  [Java]SpringBoot配置参数 
tags: []
categories: [] 

---
偶尔忘记怎么获取配置的参数，备忘一下。
- Spring Boot会自动识别正确的配置文件（.properties或.yml）并加载其中的属性。 例如：application.properties与application.yml- 读取机制为 Environment ，它将配置抽象为Properties和Profiles，并提供了一个接口来访问配置。SpringBoot中，Environment默认使用的Environment实现类是StandardServletEnvironment
## 1、参数注入

### 1.1、@PropertySource配置文件引入+@Configuration注入

使用下列注解引入配置文件

|注解|用途
|------
|@PropertySource(“classpath:/datasource.properties”)|在任意被注入的类、方法使用。提供了一种方便的声明性机制，用于将 PropertySource 添加到 Spring 的环境中。与@Configuration类结合使用。一般用于引入不会被默认加载的自定义配置文件

例如下面的代码，加载了resources下自定义的baidu-secret.properties文件，在其他类使用的时候，注入BaiduProperties 即可获取baidu-secret.properties配置文件中的参数。

@PropertySource只是将自定义的配置文件引入，具体值还需要适用 @Value注解配置

```

import lombok.Data;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Data
@Configuration
@PropertySource("classpath:baidu-secret.properties")
public class BaiduProperties {<!-- -->

    @Value("{baidu.ocr.client_id}")
    private String clientId;

    @Value("${baidu.ocr.client_secret}")
    private String clientSecret;


    @Value("${baidu.trans.appid}")
    private String appId;

    @Value("${baidu.trans.key}")
    private String key;

    @Value("${baidu.trans.url}")
    private String url;
}

```

另外还有一个注解，可以指定参数前缀。不用也可以，没什么必要，感觉通常情况参数在一处写完整比较易读

|注解|用途
|------
|@ConfigurationProperties|可以指定前缀外部化配置的注释。如果要绑定和验证某些外部属性（例如，从 .properties 文件），请将其添加到类定义或 @Configuration 类中的 @Bean 方法中。

### 1.2、@ImportResource

使用下列注解兼容Spring配置文件，使用位置为**启动类**(一般情况)

|注解|用途
|------
|@ImportResource(“classpath:/applicationContext.xml”)|在启动类使用，引入Spring配置文件

## 2、使用Environment

除了使用@Value注解，还可以使用SpringBoot的 Environment来动态的获取程序加载的参数。 demo如下，可以获取参数 hello.world：

```
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.core.env.Environment;
import org.springframework.stereotype.Component;

@Component
public class DemoEnvironment implements CommandLineRunner {<!-- -->

    @Autowired
    private Environment environment;

    @Override
    public void run(String... args) throws Exception {<!-- -->
        String property = environment.getProperty("hello.world");
        System.out.println("Hello world: " + property);
    }
}

```
