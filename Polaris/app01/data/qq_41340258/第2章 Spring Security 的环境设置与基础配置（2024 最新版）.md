
--- 
title:  第2章 Spring Security 的环境设置与基础配置（2024 最新版） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/f9ae5ada61e74f4cb7d13049a338b6bc.png#pic_center" alt="在这里插入图片描述">



#### 文章目录
- - <ul><li>- <ul><li>- - - - - - - - - <ul><li>- - - - - - <ul><li>- - - - 


## 2.1 安装和配置 Spring Boot

### 2.1.1 基础知识详解

在深入 Spring Boot 的世界之前，让我们先了解一些基础知识，这就像是在开始一场激动人心的旅行前查看地图一样。

#### Spring Boot 的核心概念
1.  **自动配置**: Spring Boot 的自动配置机制旨在根据添加的依赖自动配置你的应用程序。这就像有一个智能助手，根据你的需求自动为你准备一切。 1.  **起步依赖（Starters）**: 这些特殊的依赖项是预设的模板，它们为你提供了一切必需的依赖组合，帮助你快速启动一个特定类型的项目。比如，`spring-boot-starter-web` 就包含了构建 web 应用所需的所有基础设施。 1.  **内嵌服务器**: Spring Boot 应用通常会内嵌一个 Tomcat、Jetty 或 Undertow 服务器，这意味着你不需要单独安装一个服务器就可以运行你的应用。 1.  **无代码生成和 XML 配置**: 与传统的 Spring 框架相比，Spring Boot 允许你使用极少甚至无需任何 XML 配置来启动一个应用，让你的代码库更加整洁。 1.  **应用监控**: Spring Boot Actuator 提供了一套现成的应用监控和管理功能，可以帮助你监视应用的运行状态和各种指标。 
#### 安装步骤
1.  **访问 Spring Initializr**: 打开 ，这是一个在线工具，可以帮助你快速生成 Spring Boot 项目结构。 <li> **选择项目设置**: 
  1. **项目类型**: Maven 或 Gradle。Maven 是传统选择，而 Gradle 提供了更现代的构建工具体验。1. **Spring Boot 版本**: 通常选择最新稳定版本。1. **项目元数据**: 如 Group、Artifact 等，这些将成为你的项目唯一标识。 </li><li> **添加起步依赖**: 
  1. 选择你所需的起步依赖，例如 `spring-boot-starter-web` 用于创建 web 应用。 </li><li> **生成项目**: 
  1. 生成并下载项目压缩文件。1. 解压缩并使用你喜欢的 IDE（如 IntelliJ IDEA、Eclipse）打开。 </li>- 选择你所需的起步依赖，例如 `spring-boot-starter-web` 用于创建 web 应用。
#### 配置和运行
<li> **配置应用属性**: 
  1. 在 `application.properties` 或 `application.yml` 文件中设置应用的配置，如端口号、数据库配置等。 </li><li> **编写业务逻辑**: 
  1. 创建模型（Model）、视图（View）和控制器（Controller）等组件。 </li><li> **运行应用**: 
  1. 直接在 IDE 中运行应用，或者在命令行中使用 `mvn spring-boot:run` 或 `gradle bootRun` 命令启动应用。 </li>- 创建模型（Model）、视图（View）和控制器（Controller）等组件。
通过掌握这些基础知识，你就能够顺利地开始你的 Spring Boot 旅程，并为集成 Spring Security 做好准备。这就像是为你的软件开发之旅装上了一个涡轮增压器！接下来的章节将带你深入到更具挑战性的 Spring Security 领域，准备好了吗？让我们开始吧！

### 2.1.2 主要案例：创建基本的 Spring Boot 应用

在这个案例中，我们将一步步创建一个基本的 Spring Boot 应用程序。这就像是在建造你自己的数字王国的第一块砖。

#### 案例 Demo

假设我们正在开发一个简单的博客应用，它将有一个页面来显示一条欢迎信息。

**步骤 1：项目初始化**
1. 访问 。1. 选择你的项目设置，例如 Maven 作为构建工具和 Java 作为编程语言。1. 选择 Spring Boot 的最新稳定版本。1. 在依赖中添加 `spring-boot-starter-web`。1. 点击“生成”，下载项目压缩包。
**步骤 2：项目结构**
1. 解压缩下载的文件。1. 使用你喜欢的 IDE（例如 IntelliJ IDEA 或 Eclipse）打开项目。<li>查看项目结构，主要关注以下目录： 
  1. `src/main/java`: 存放 Java 源代码。1. `src/main/resources`: 存放资源文件，如配置文件。 </li>
**步骤 3：编写 Hello World 控制器**
1.  在 `src/main/java` 下，找到主应用程序类（通常命名为 `Application` 或与你的项目名称相同）。 1.  创建一个新的包，例如 `com.example.blog`。 <li> 在该包中创建一个新的 Java 类 `HelloController`。 <pre><code class="prism language-java">package com.example.blog;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {<!-- -->

    @GetMapping("/")
    public String hello() {<!-- -->
        return "Welcome to the Blog!";
    }
}
</code></pre> </li>
**步骤 4：运行应用程序**
1. 回到主应用程序类，并运行应用。1. 打开浏览器，访问 `http://localhost:8080`。1. 你应该看到页面上显示“Welcome to the Blog!”。
#### 再添加一个简单的服务

假设我们想要在应用中添加一个服务来处理一些业务逻辑。

**案例 Demo**:
<li> **创建服务类**: 
  1. 在 `com.example.blog` 包下创建一个新的类 `BlogService`。 <pre><code class="prism language-java">package com.example.blog;

import org.springframework.stereotype.Service;

@Service
public class BlogService {<!-- -->

    public String getWelcomeMessage() {<!-- -->
        return "Welcome to the Blog!";
    }
}
</code></pre> </li><li> **修改控制器以使用服务**: 
  1. 注入 `BlogService` 到 `HelloController` 并使用它。 <pre><code class="prism language-java">@RestController
public class HelloController {<!-- -->

    private final BlogService blogService;

    public HelloController(BlogService blogService) {<!-- -->
        this.blogService = blogService;
    }

    @GetMapping("/")
    public String hello() {<!-- -->
        return blogService.getWelcomeMessage();
    }
}
</code></pre> </li><li> **运行并测试**: 
  1. 再次运行应用程序，并验证服务是否正确返回消息。 </li>- 注入 `BlogService` 到 `HelloController` 并使用它。
#### 还可以整合数据库

让我们进一步扩展应用，通过整合数据库来存储和检索数据。

**案例 Demo**:
<li> **添加数据库依赖**: 
  1. 在 `pom.xml` 中添加 `spring-boot-starter-data-jpa` 和内嵌数据库（如 H2）的依赖。 </li><li> **配置数据库**: 
  1. 在 `application.properties` 中配置数据库。 </li><li> **创建实体和仓库**: 
  1. 定义一个实体类 `BlogPost` 和一个仓库接口 `BlogPostRepository`。 </li><li> **修改服务以使用数据库**: 
  1. 更新 `BlogService` 以使用 `BlogPostRepository`。 </li><li> **运行并测试**: 
  1. 测试应用能否正确地存取数据。 </li>- 在 `application.properties` 中配置数据库。- 更新 `BlogService` 以使用 `BlogPostRepository`。
通过这个案例，你将了解到如何从零开始创建一个 Spring Boot 应用，并逐步扩展其功能，从一个简单的 “Hello World” 到集成服务和数据库。这将为你打下坚实的基础，为进一步探索 Spring Security 的世界做好准备。

### 2.1.3 拓展案例 1：添加数据库支持

在这个案例中，我们将在 Spring Boot 应用中添加数据库支持，以增强其数据持久化能力。我们将构建一个简单的博客应用，其中包括保存和检索博客文章的功能。

#### 案例 Demo

假设我们的博客应用需要保存博客文章到数据库，并能够从数据库中检索这些文章。

**步骤 1：添加数据库依赖**
<li> 在 `pom.xml` 中添加 `spring-boot-starter-data-jpa` 依赖和一个数据库连接池依赖，例如 H2。 <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-data-jpa&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;com.h2database&lt;/groupId&gt;
    &lt;artifactId&gt;h2&lt;/artifactId&gt;
    &lt;scope&gt;runtime&lt;/scope&gt;
&lt;/dependency&gt;
</code></pre> </li>
**步骤 2：配置数据库**
<li> 在 `application.properties` 中配置 H2 数据库。 <pre><code class="prism language-properties">spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.h2.console.enabled=true
</code></pre> </li>
**步骤 3：创建实体和仓库**
<li> 创建一个实体类 `BlogPost`。 <pre><code class="prism language-java">package com.example.blog;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;

@Entity
public class BlogPost {<!-- -->
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String title;
    private String content;
    // 省略 getter 和 setter
}
</code></pre> </li><li> 创建一个继承自 `JpaRepository` 的仓库接口 `BlogPostRepository`。 <pre><code class="prism language-java">package com.example.blog;

import org.springframework.data.jpa.repository.JpaRepository;

public interface BlogPostRepository extends JpaRepository&lt;BlogPost, Long&gt; {<!-- -->
}
</code></pre> </li>
**步骤 4：创建服务类和控制器**
<li> 创建一个服务类 `BlogService` 来处理业务逻辑。 <pre><code class="prism language-java">package com.example.blog;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class BlogService {<!-- -->
    private final BlogPostRepository repository;

    @Autowired
    public BlogService(BlogPostRepository repository) {<!-- -->
        this.repository = repository;
    }

    public BlogPost saveBlogPost(BlogPost post) {<!-- -->
        return repository.save(post);
    }

    public List&lt;BlogPost&gt; getAllBlogPosts() {<!-- -->
        return repository.findAll();
    }
}
</code></pre> </li><li> 在 `HelloController` 中添加新的端点。 <pre><code class="prism language-java">package com.example.blog;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class BlogController {<!-- -->
    private final BlogService blogService;

    @Autowired
    public BlogController(BlogService blogService) {<!-- -->
        this.blogService = blogService;
    }

    @PostMapping("/posts")
    public BlogPost addBlogPost(@RequestBody BlogPost post) {<!-- -->
        return blogService.saveBlogPost(post);
    }

    @GetMapping("/posts")
    public List&lt;BlogPost&gt; getAllBlogPosts() {<!-- -->
        return blogService.getAllBlogPosts();
    }
}
</code></pre> </li>
**步骤 5：运行和测试**
1. 运行应用程序。1. 使用 REST 客户端或浏览器访问 `http://localhost:8080/posts` 来查看所有博客文章，或通过 POST 请求向 `/posts` 添加新的博客文章。
通过这个案例，你将学会如何在 Spring Boot 应用中添加和配置数据库支持，创建实体和仓库，并通过服务类和控制器与数据库交互。这些步骤为构建具有数据持久化功能的应用提供了基础，使你的 Spring Boot 之旅更加丰富多彩。

### 2.1.4 拓展案例 2：整合外部服务

在这个案例中，我们将演示如何将外部服务整合到 Spring Boot 应用中。我们将以集成一个简单的邮件发送服务为例。

#### 案例 Demo

假设我们的 Spring Boot 应用需要发送欢迎邮件给新注册的用户。

**步骤 1：添加邮件服务依赖**
<li> 在 `pom.xml` 中添加 `spring-boot-starter-mail` 依赖。 <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-mail&lt;/artifactId&gt;
&lt;/dependency&gt;
</code></pre> </li>
**步骤 2：配置邮件服务器**
<li> 在 `application.properties` 中配置邮件服务器的属性。这里我们以 Gmail 为例： <pre><code class="prism language-properties">spring.mail.host=smtp.gmail.com
spring.mail.port=587
spring.mail.username=your-email@gmail.com
spring.mail.password=your-password
spring.mail.properties.mail.smtp.auth=true
spring.mail.properties.mail.smtp.starttls.enable=true
</code></pre> </li>
**步骤 3：创建邮件服务类**
<li> 创建一个 `EmailService` 类来封装邮件发送逻辑。 <pre><code class="prism language-java">package com.example.blog;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.stereotype.Service;

@Service
public class EmailService {<!-- -->

    @Autowired
    private JavaMailSender mailSender;

    public void sendWelcomeEmail(String to, String username) {<!-- -->
        SimpleMailMessage message = new SimpleMailMessage();
        message.setFrom("noreply@example.com");
        message.setTo(to);
        message.setSubject("Welcome to the Blog!");
        message.setText("Hello " + username + ",\nWelcome to our blog!");
        mailSender.send(message);
    }
}
</code></pre> </li>
**步骤 4：在应用中使用邮件服务**
<li> 创建一个控制器来使用 `EmailService` 发送邮件。 <pre><code class="prism language-java">package com.example.blog;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/users")
public class UserController {<!-- -->

    private final EmailService emailService;

    @Autowired
    public UserController(EmailService emailService) {<!-- -->
        this.emailService = emailService;
    }

    @PostMapping("/register")
    public String registerUser(@RequestParam String email, @RequestParam String username) {<!-- -->
        // 注册用户的逻辑...
        emailService.sendWelcomeEmail(email, username);
        return "User registered successfully!";
    }
}
</code></pre> </li>
**步骤 5：运行和测试**
1. 运行你的 Spring Boot 应用。1. 使用 POST 请求向 `/users/register` 发送一个包含邮件地址和用户名的请求。1. 检查指定的邮箱，确认是否收到了欢迎邮件。
通过这个案例，你将学会如何在 Spring Boot 应用中集成外部服务，如邮件服务。这不仅增强了你的应用功能，还提高了用户体验。整合外部服务是构建现代应用的关键步骤，它能让你的应用更加丰富和动态。

## 2.2 集成 Spring Security

### 2.2.1 基础知识详解

集成 Spring Security 到你的 Spring Boot 应用中是一项关键任务，它保障了应用的安全性和数据保护。在此过程中，你将了解到 Spring Security 的核心概念和实现方法。

#### Spring Security 的核心组件
<li> **过滤器链（Filter Chains）**: 
  1. Spring Security 使用一系列过滤器来处理不同的安全考虑。这些过滤器负责执行认证、授权等安全操作。 </li><li> **认证（Authentication）**: 
  1. 认证是确认用户身份的过程。Spring Security 提供多种认证方式，如内存认证、数据库认证、LDAP 认证等。 </li><li> **授权（Authorization）**: 
  1. 授权是控制已认证用户访问应用程序资源的过程。Spring Security 支持基于角色的访问控制（RBAC）和基于表达式的访问控制。 </li><li> **用户详情服务（UserDetailsService）**: 
  1. `UserDetailsService` 接口用于根据用户名加载用户的数据。它通常用于从数据库中加载用户信息。 </li><li> **密码编码器（PasswordEncoder）**: 
  1. Spring Security 强调对密码进行加密存储。`PasswordEncoder` 接口用于定义密码的加密方式。 </li>- 认证是确认用户身份的过程。Spring Security 提供多种认证方式，如内存认证、数据库认证、LDAP 认证等。- `UserDetailsService` 接口用于根据用户名加载用户的数据。它通常用于从数据库中加载用户信息。
#### Spring Security 的配置
<li> **创建 SecurityConfig 类**: 
  1. 通过扩展 `WebSecurityConfigurerAdapter` 类并覆写其方法，你可以自定义应用程序的安全配置。 </li><li> **定义认证规则**: 
  1. 在 `configure(AuthenticationManagerBuilder auth)` 方法中定义认证规则。 </li><li> **定义授权规则**: 
  1. 在 `configure(HttpSecurity http)` 方法中定义哪些路径应该受保护，哪些路径应该公开访问。 </li><li> **自定义登录和注销**: 
  1. Spring Security 允许自定义登录和注销行为，你可以指定登录页面、默认成功登录跳转路径等。 </li>- 在 `configure(AuthenticationManagerBuilder auth)` 方法中定义认证规则。- Spring Security 允许自定义登录和注销行为，你可以指定登录页面、默认成功登录跳转路径等。
通过理解这些基础概念和配置步骤，你将能够为你的应用添加一个强大而灵活的安全层。这不仅保护了你的应用免受未经授权的访问，还为用户提供了安全的交互环境。

### 2.2.2 主要案例：基本的安全配置

在这个案例中，我们将通过一个实际的示例来展示如何在 Spring Boot 应用中实现基本的安全配置。

#### 案例 Demo

我们将构建一个简单的博客应用，它允许用户查看文章列表，但只有注册用户才能查看文章详情。

**步骤 1：配置安全依赖**
<li> 在你的 Spring Boot 项目的 `pom.xml` 中添加 Spring Security 依赖： <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-security&lt;/artifactId&gt;
&lt;/dependency&gt;
</code></pre> </li>
**步骤 2：创建安全配置类**
<li> 创建一个新的 Java 类 `SecurityConfig` 并扩展 `WebSecurityConfigurerAdapter`。 <pre><code class="prism language-java">import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .authorizeRequests()
            .antMatchers("/", "/posts").permitAll()
            .antMatchers("/post/*").authenticated()
            .and()
            .formLogin()
            .loginPage("/login")
            .permitAll()
            .and()
            .logout()
            .permitAll();
    }
}
</code></pre> 在这里，我们配置了 URL 模式的安全性。任何人都可以访问主页 (`/`) 和文章列表 (`/posts`)，但只有认证用户可以访问文章详情（例如 `/post/1`）。 </li>
**步骤 3：创建控制器**
<li> 创建一个控制器 `BlogController` 来处理 HTTP 请求。 <pre><code class="prism language-java">import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class BlogController {<!-- -->

    @GetMapping("/")
    public String home() {<!-- -->
        return "home";
    }

    @GetMapping("/posts")
    public String posts() {<!-- -->
        return "posts";
    }

    @GetMapping("/post/{id}")
    public String postDetails() {<!-- -->
        return "post-details";
    }

    @GetMapping("/login")
    public String login() {<!-- -->
        return "login";
    }
}
</code></pre> 这里，我们定义了不同的路由和它们对应的视图。 </li>
**步骤 4：创建视图**
1. 创建相应的 HTML 文件（如 `home.html`, `posts.html`, `post-details.html`, `login.html`）在 `src/main/resources/templates` 目录下。
**步骤 5：运行应用程序**
1. 运行你的 Spring Boot 应用。1. 在浏览器中访问 `http://localhost:8080`，尝试点击不同的链接，并观察安全配置的效果。
通过这个案例，你将学会如何在 Spring Boot 应用中添加基本的 Spring Security 配置。这样做不仅提高了应用的安全性，还为今后添加更复杂的安全功能奠定了基础。

### 2.2.3 拓展案例 1：数据库用户存储

在这个案例中，我们将展示如何在 Spring Boot 应用中使用数据库进行用户认证，这是实际生产环境中非常常见的场景。

#### 案例 Demo

我们将创建一个简单的 Spring Boot 应用，其中用户信息存储在数据库中，并用于认证。

**步骤 1：添加依赖**
<li> 在 `pom.xml` 文件中添加 `spring-boot-starter-data-jpa` 和数据库依赖（这里我们使用 H2 数据库作为示例）。 <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-data-jpa&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;com.h2database&lt;/groupId&gt;
    &lt;artifactId&gt;h2&lt;/artifactId&gt;
    &lt;scope&gt;runtime&lt;/scope&gt;
&lt;/dependency&gt;
</code></pre> </li>
**步骤 2：配置数据源**
<li> 在 `application.properties` 文件中配置 H2 数据库。 <pre><code class="prism language-properties">spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.h2.console.enabled=true
</code></pre> </li>
**步骤 3：创建用户实体和仓库**
<li> 创建用户实体 `User`。 <pre><code class="prism language-java">package com.example.demo;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class User {<!-- -->

    @Id
    private String username;
    private String password;
    private String role;

    // Getters and Setters
}
</code></pre> </li><li> 创建用户仓库接口 `UserRepository`。 <pre><code class="prism language-java">package com.example.demo;

import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository&lt;User, String&gt; {<!-- -->
}
</code></pre> </li>
**步骤 4：实现 UserDetailsService**
<li> 创建服务 `CustomUserDetailsService` 实现 `UserDetailsService`。 <pre><code class="prism language-java">package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class CustomUserDetailsService implements UserDetailsService {<!-- -->

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Override
    public User loadUserByUsername(String username) throws UsernameNotFoundException {<!-- -->
        User user = userRepository.findById(username)
            .orElseThrow(() -&gt; new UsernameNotFoundException("User not found"));
        return new User(user.getUsername(), passwordEncoder.encode(user.getPassword()), 
                       Collections.singletonList(new SimpleGrantedAuthority(user.getRole())));
    }
}
</code></pre> </li>
**步骤 5：配置 Spring Security**
<li> 修改 `SecurityConfig` 类，使用自定义的 `UserDetailsService` 和密码编码器。 <pre><code class="prism language-java">import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

@Autowired
private CustomUserDetailsService userDetailsService;

@Override
protected void configure(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
    auth.userDetailsService(userDetailsService)
        .passwordEncoder(passwordEncoder());
}

@Bean
public PasswordEncoder passwordEncoder() {<!-- -->
    return new BCryptPasswordEncoder();
}
</code></pre> </li>
**步骤 6：运行和测试**
1. 启动 Spring Boot 应用。1. 通过 H2 Console 或其他方式添加用户数据到数据库。1. 尝试登录，验证用户认证是否工作正常。
通过此案例，你可以学习到如何在 Spring Boot 应用中结合数据库进行用户认证。这为你提供了一个更接近真实世界应用的安全配置方案。

### 2.2.4 拓展案例 2：OAuth2 集成

在这个案例中，我们将在 Spring Boot 应用中集成 OAuth2，允许用户使用第三方服务（如 Google, Facebook）进行登录，这是现代应用中常见的一种用户认证方式。

#### 案例 Demo

我们的目标是创建一个 Spring Boot 应用，其中用户可以通过 Google 账户登录。

**步骤 1：添加 OAuth2 客户端依赖**
<li> 在 `pom.xml` 中添加 `spring-boot-starter-oauth2-client` 依赖。 <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-oauth2-client&lt;/artifactId&gt;
&lt;/dependency&gt;
</code></pre> </li>
**步骤 2：配置 OAuth2 客户端**
<li> 在 `application.properties` 或 `application.yml` 文件中配置 Google OAuth2 客户端信息。 <pre><code class="prism language-properties">spring.security.oauth2.client.registration.google.client-id=your-google-client-id
spring.security.oauth2.client.registration.google.client-secret=your-google-client-secret
spring.security.oauth2.client.registration.google.scope=profile,email
</code></pre> 您需要在 Google Cloud Console 中创建 OAuth2.0 客户端 ID，以获取客户端 ID 和秘密。 </li>
**步骤 3：安全配置**
<li> 修改 `SecurityConfig` 类，以支持 OAuth2 登录。 <pre><code class="prism language-java">import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Override
protected void configure(HttpSecurity http) throws Exception {<!-- -->
    http
        .authorizeRequests()
            .anyRequest().authenticated()
            .and()
        .oauth2Login();
}
</code></pre> </li>
**步骤 4：创建控制器来处理登录后的操作**
<li> 创建一个控制器来展示用户信息。 <pre><code class="prism language-java">import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {<!-- -->

    @GetMapping("/user")
    public String user(@AuthenticationPrincipal OAuth2User principal) {<!-- -->
        return "Welcome, " + principal.getAttribute("name");
    }
}
</code></pre> </li>
**步骤 5：运行和测试**
1. 启动 Spring Boot 应用。1. 访问 `http://localhost:8080/user`。1. 应用将重定向到 Google 的登录页面。使用 Google 账户登录。1. 登录成功后，应显示欢迎消息和用户信息。
通过这个案例，您可以了解到如何在 Spring Boot 应用中实现 OAuth2 集成，使用户可以通过第三方服务进行身份验证，从而提供更加流畅和安全的用户体验。这种认证方式广泛应用于现代网页和移动应用中。

## 2.3 测试你的配置

在集成了 Spring Security 后，测试你的配置是确保一切按预期工作的重要步骤。这不仅关乎安全性，也关乎功能的正确实现。

### 2.3.1 基础知识详解

在集成了 Spring Security 后，测试你的配置是确保一切按预期工作的重要步骤。这部分不仅关乎安全性，也涉及到功能性的正确实现。

#### 重要的测试概念
<li> **安全性测试**: 
  1. 确认认证（Authentication）和授权（Authorization）机制按预期工作。1. 验证不同用户角色的访问权限是否正确实现。 </li><li> **端点测试**: 
  1. 测试不同的 API 端点以确保安全配置正确，例如，某些端点应仅对认证用户开放。 </li><li> **测试类型**: 
  1. **单元测试**: 测试单个方法或类的功能。1. **集成测试**: 测试多个组件协同工作的情况。1. **端到端测试**: 测试整个应用程序的工作流程。 </li><li> **测试工具**: 
  1. **JUnit**: Java 程序员最常用的单元测试框架。1. **MockMvc**: 用于模拟 MVC 测试，可以模拟发送 HTTP 请求并验证结果。1. **Spring Security Test**: 提供了一系列用于测试 Spring Security 配置的工具。 </li>- 测试不同的 API 端点以确保安全配置正确，例如，某些端点应仅对认证用户开放。- **JUnit**: Java 程序员最常用的单元测试框架。- **MockMvc**: 用于模拟 MVC 测试，可以模拟发送 HTTP 请求并验证结果。- **Spring Security Test**: 提供了一系列用于测试 Spring Security 配置的工具。
#### 如何进行有效的安全性测试
1. **模拟认证用户**: 使用测试工具模拟不同角色的用户，以测试他们的访问权限。1. **测试受保护的资源**: 验证受保护的资源（如 API 端点）是否仅对具有适当权限的用户开放。1. **测试登录流程**: 确保登录流程按预期工作，包括错误处理。1. **CSRF 防护测试**: 如果应用启用了 CSRF 防护，应进行相应的测试以确保其有效性。
通过这些测试，你可以保证你的 Spring Security 配置既安全又高效，为用户提供了必要的保护，同时不会干扰应用程序的正常功能。测试是任何安全配置不可或缺的一部分，它确保了安全措施的有效性和应用的健壮性。

### 2.3.2 主要案例：测试基本的安全配置

在这个案例中，我们将通过一个实际的示例来测试在 Spring Boot 应用中集成的基本 Spring Security 配置。

#### 案例 Demo

假设我们的 Spring Boot 应用有两个主要端点：一个公开的主页 (`/`) 和一个受保护的用户页面 (`/user`)。我们将编写测试来验证安全配置是否按预期工作。

**步骤 1：添加测试依赖**
<li> 在 `pom.xml` 文件中添加以下依赖，以支持测试： <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
    &lt;scope&gt;test&lt;/scope&gt;
&lt;/dependency&gt;
</code></pre> </li>
**步骤 2：编写测试类**
<li> 创建一个测试类 `WebSecurityConfigTest`。 <pre><code class="prism language-java">package com.example.demo;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
public class WebSecurityConfigTest {<!-- -->

    @Autowired
    private MockMvc mockMvc;

    @Test
    public void accessPublic() throws Exception {<!-- -->
        mockMvc.perform(get("/"))
                .andExpect(status().isOk());
    }

    @Test
    public void accessPrivateUnauthenticated() throws Exception {<!-- -->
        mockMvc.perform(get("/user"))
                .andExpect(status().isUnauthorized());
    }
}
</code></pre> 在这里，我们使用 `MockMvc` 来模拟发送 HTTP 请求到不同的端点，并验证响应的状态码。我们期望公开页面返回 `200 OK` 状态，而未经认证的访问受保护的 `/user` 端点应返回 `401 Unauthorized` 状态。 </li>
**步骤 3：运行测试**
1. 在 IDE 中运行测试类或使用 Maven/Gradle 命令行工具来执行测试。1. 检查测试结果，确认安全配置是否按预期工作。
通过这个案例，你可以验证你的 Spring Security 配置是否正确实现了基本的认证和授权。这种测试是确保应用安全性的重要步骤，能帮助你捕获潜在的安全问题和配置错误。

2.3.3 ### 拓展案例 1：测试数据库用户存储

在这个案例中，我们将测试 Spring Boot 应用中使用数据库进行用户认证的配置。假设我们的应用使用数据库来存储用户信息，并基于这些信息进行认证。

#### 案例 Demo

假设我们已经有一个集成了数据库用户存储的 Spring Boot 应用，现在我们需要编写测试来验证用户认证功能。

**步骤 1：配置测试数据库**
<li> 在 `src/test/resources` 目录下创建一个 `application.properties` 文件，配置用于测试的数据库信息（使用 H2 数据库作为示例）。 <pre><code class="prism language-properties">spring.datasource.url=jdbc:h2:mem:testdb;DB_CLOSE_DELAY=-1
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.h2.console.enabled=true
</code></pre> </li>
**步骤 2：添加测试依赖**
<li> 确保在 `pom.xml` 中已经添加了 `spring-boot-starter-test` 和 `h2` 数据库的依赖。 <pre><code class="prism language-xml">&lt;!-- Test dependencies --&gt;
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
    &lt;scope&gt;test&lt;/scope&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;com.h2database&lt;/groupId&gt;
    &lt;artifactId&gt;h2&lt;/artifactId&gt;
    &lt;scope&gt;test&lt;/scope&gt;
&lt;/dependency&gt;
</code></pre> </li>
**步骤 3：编写测试类**
<li> 创建一个测试类 `UserAuthenticationTest`。 <pre><code class="prism language-java">package com.example.demo;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
public class UserAuthenticationTest {<!-- -->

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @BeforeEach
    public void setup() {<!-- -->
        User user = new User();
        user.setUsername("testuser");
        user.setPassword(passwordEncoder.encode("password"));
        user.setRole("USER");
        userRepository.save(user);
    }

    @Test
    public void authenticateWithValidUser() throws Exception {<!-- -->
        mockMvc.perform(post("/login")
                .param("username", "testuser")
                .param("password", "password"))
                .andExpect(status().isOk());
    }

    @Test
    public void authenticateWithInvalidUser() throws Exception {<!-- -->
        mockMvc.perform(post("/login")
                .param("username", "invaliduser")
                .param("password", "password"))
                .andExpect(status().isUnauthorized());
    }
}
</code></pre> 在这里，我们使用 `MockMvc` 来模拟登录请求，并验证不同用户（有效和无效）的认证结果。 </li>
**步骤 4：运行测试**
1. 在 IDE 中运行测试类或使用 Maven/Gradle 命令行工具来执行测试。1. 检查测试结果，确认数据库用户存储和认证是否按预期工作。
通过这个案例，你可以确保你的 Spring Boot 应用中的用户认证机制（基于数据库存储）按预期运行，从而提高应用的安全性和可靠性。

### 2.3.4 拓展案例 2：测试 OAuth2 集成

在这个案例中，我们将演示如何测试 Spring Boot 应用中的 OAuth2 集成，确保第三方登录（如 Google OAuth2）按预期工作。

#### 案例 Demo

假设我们的 Spring Boot 应用已经集成了 Google OAuth2 登录。我们需要编写测试来验证 OAuth2 流程。

**步骤 1：添加测试依赖**
<li> 确保在 `pom.xml` 中添加了 `spring-boot-starter-test` 依赖。 <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
    &lt;scope&gt;test&lt;/scope&gt;
&lt;/dependency&gt;
</code></pre> </li>
**步骤 2：配置 OAuth2 测试**
<li> 在测试配置中（`src/test/resources/application.properties`），添加用于测试的 OAuth2 配置。 <pre><code class="prism language-properties">spring.security.oauth2.client.registration.google.client-id=test-client-id
spring.security.oauth2.client.registration.google.client-secret=test-client-secret
</code></pre> </li>
**步骤 3：编写测试类**
<li> 创建一个测试类 `OAuth2LoginTest`。 <pre><code class="prism language-java">package com.example.demo;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.security.test.context.support.WithMockUser;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.redirectedUrlPattern;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
public class OAuth2LoginTest {<!-- -->

    @Autowired
    private MockMvc mockMvc;

    @Test
    @WithMockUser
    public void requestProtectedUrlWithUser() throws Exception {<!-- -->
        mockMvc.perform(get("/user"))
                .andExpect(status().isOk());
    }

    @Test
    public void requestProtectedUrlWithoutUser() throws Exception {<!-- -->
        mockMvc.perform(get("/user"))
                .andExpect(status().is3xxRedirection())
                .andExpect(redirectedUrlPattern("**/oauth2/authorization/google"));
    }
}
</code></pre> 这里我们使用 `WithMockUser` 来模拟一个已认证的用户，以测试受保护的 URL 访问。同时，我们测试未认证用户访问受保护 URL 时的重定向行为。 </li>
**步骤 4：运行测试**
1. 在 IDE 中运行测试类或使用 Maven/Gradle 命令行工具来执行测试。1. 检查测试结果，确认 OAuth2 集成是否按预期工作。
通过这个案例，你可以确保你的应用中的 OAuth2 集成正确实现了第三方登录流程，提供了有效的用户认证机制。这对于提供一个安全、便捷的用户登录体验至关重要。
