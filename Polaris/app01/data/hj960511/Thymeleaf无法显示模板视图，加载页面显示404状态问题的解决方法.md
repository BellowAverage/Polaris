
--- 
title:  Thymeleaf无法显示模板视图，加载页面显示404状态问题的解决方法 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解：Thymeleaf无法显示模板视图，加载页面显示404状态问题的解决方法 日期：2024年2月23日 作者：任聪聪 


## 现象说明：

### 1.只返回输出模板的名称，如图：

<img src="https://img-blog.csdnimg.cn/direct/9122fec7b84243f09b4fb95014373e26.png" alt="在这里插入图片描述">

### 2.显示报错信息：

```
Whitelabel Error Page
This application has no explicit mapping for /error, so you are seeing this as a fallback.

Fri Feb 23 23:00:32 CST 2024
There was an unexpected error (type=Not Found, status=404).

```

## 问题原因：

1.依赖没有安装正确 2.没有正确填写Thymeleaf的模板文件内容。 3.没有正确填写Controller的生命和配置。 4.缺少核心配置文件参数。 5.路径不对。

## 解决方法：

### 排查步骤一、自审相关安装情况

#### 1.依赖信息是否是如下配置：

```
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-thymeleaf&lt;/artifactId&gt;
        &lt;/dependency&gt;

```

注意：位置是在`&lt;dependencies&gt;....&lt;/dependencies&gt;`之间

#### 2.检查是否配置，application.properties文件：

```
spring.thymeleaf.prefix=classpath:/templates/
spring.thymeleaf.encoding=UTF-8
spring.thymeleaf.cache=false
spring.thymeleaf.suffix=.html
spring.thymeleaf.servlet.content-type=text/html

```

#### 3.检查templates文件路径是否在，\src\main\resources\templates下：

<img src="https://img-blog.csdnimg.cn/direct/42936392f9624e6a870e6d76f488908c.png" alt="在这里插入图片描述">

#### 4.检查模板文件是否存在th头，如果没有则也会报错：

```
&lt;!DOCTYPE html&gt;
&lt;html xmlns:th="http://www.thymeleaf.org"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;距离成功又近了一步~&lt;/title&gt;
    &lt;style&gt;
        body {<!-- -->
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 20px;
        }
        h1 {<!-- -->
            color: #007bff;
        }
        p {<!-- -->
            font-size: 18px;
            color: #6c757d;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;欢迎使用Thymeleaf模板&lt;/h1&gt;
&lt;p th:text="${<!-- -->message?:'is null'}"&gt;默认文本信息演示~~&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;

```

#### 5.检查controller的注解是否是RustController：

说明：如果是controller那么建议改为RustController。

### 排查步骤二、检查Controller

说明：如果你的controller没有进行ModelAndView的声明那么也会不显示界面，正确的配置如下：

```
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

@RestController
public class HomeController {<!-- -->
    @GetMapping("/")
    public ModelAndView index(ModelAndView model){<!-- -->
        model.addObject("message", "Hello, Thymeleaf!");
        model.setViewName("index");
        return model;
    }
}

```

## 引入Thymeleaf成功后效果：

<img src="https://img-blog.csdnimg.cn/direct/73d73aed8d8a49d39b516de4a69bf025.png" alt="在这里插入图片描述"> end：大功告成~
