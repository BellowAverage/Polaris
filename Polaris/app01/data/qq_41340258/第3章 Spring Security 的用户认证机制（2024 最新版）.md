
--- 
title:  第3章 Spring Security 的用户认证机制（2024 最新版） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/b53d9b63aa1c4086b4815cb789f24d15.png#pic_center" alt="在这里插入图片描述">



#### 文章目录
- - <ul><li>- <ul><li>- - - - - - <ul><li>- - - - - - - - <ul><li>- - - - - - - - 


## 3.1 认证流程

在 Spring Security 的世界里，认证流程是核心的安全机制，用于确认一个请求是否来自一个有效的用户。这个过程可以比作一道门槛，只有拥有正确钥匙的人才能进入。

### 3.1.1 基础知识详解

在深入探索用户认证机制之前，让我们首先建立一些基础知识，确保我们都在同一页面上。用户认证在应用安全中扮演着至关重要的角色，它就像是一道门槛，确保只有拥有正确密钥的人才能进入。

#### 认证流程的核心概念
<li> **认证（Authentication）**: 
  1. 这是确定某人是谁的过程。在网络安全中，它通常涉及用户名和密码，但也可以包括其他方法，如二因素认证、生物识别等。 </li><li> **授权（Authorization）**: 
  1. 一旦用户被认证，接下来就是确定他们有权访问的资源或执行的操作。简单来说，就是确定他们可以做什么。 </li><li> **凭证（Credentials）**: 
  1. 通常是指证明用户身份的信息，如用户名和密码、安全令牌等。 </li><li> **主体（Principal）**: 
  1. 在安全服务中，主体通常指可以在应用中执行操作的用户、设备或其他系统。 </li><li> **认证管理器（AuthenticationManager）**: 
  1. Spring Security 中的接口，负责协调认证过程。 </li><li> **用户详情服务（UserDetailsService）**: 
  1. 用于从指定的数据源（例如数据库、LDAP）加载用户信息的接口。 </li><li> **密码编码器（PasswordEncoder）**: 
  1. 负责密码加密和验证，以确保存储和比较密码的安全性。 </li>- 一旦用户被认证，接下来就是确定他们有权访问的资源或执行的操作。简单来说，就是确定他们可以做什么。- 在安全服务中，主体通常指可以在应用中执行操作的用户、设备或其他系统。- 用于从指定的数据源（例如数据库、LDAP）加载用户信息的接口。
#### 认证流程的步骤

用户认证流程通常包括以下步骤：
<li> **用户提交凭证**: 
  1. 用户通过登录表单或其他认证机制提交他们的凭证。 </li><li> **加载用户详情**: 
  1. 系统利用 `UserDetailsService` 根据提交的凭证（通常是用户名）加载用户的详细信息。 </li><li> **凭证验证**: 
  1. 使用 `PasswordEncoder` 等工具验证用户提交的凭证（如密码）是否与存储的凭证匹配。 </li><li> **创建认证令牌**: 
  1. 一旦用户被验证，系统会创建一个认证令牌（`Authentication` 对象），表示用户的认证状态。 </li><li> **设置安全上下文**: 
  1. 认证令牌被存储在安全上下文（`SecurityContextHolder`）中，以便在应用的后续处理中使用。 </li>- 系统利用 `UserDetailsService` 根据提交的凭证（通常是用户名）加载用户的详细信息。- 一旦用户被验证，系统会创建一个认证令牌（`Authentication` 对象），表示用户的认证状态。
通过理解这些基础知识，你现在应该对 Spring Security 中的用户认证流程有了一个清晰的概念。这为我们深入探索如何在实际应用中实现和测试不同类型的认证机制奠定了坚实的基础。

### 3.1.2 主要案例：内存用户认证

让我们通过一个实际的示例来演示如何在 Spring Boot 应用中实现基于内存的用户认证。这种方法非常适合开发和测试环境，让我们快速启动并运行，无需配置复杂的外部数据源。

#### 案例 Demo：快速启动你的 Spring Boot 守护程序

想象你正在创建一个神秘的守护程序，这个程序守护着一个包含古老知识的图书馆。为了进入图书馆，读者必须通过一个古老的仪式（也就是登录过程）。但在这个仪式中，我们将使用现代的 Spring Security 魔法来识别访客。

**步骤 1：准备你的魔法工具**

确保你的 `pom.xml` 中已经添加了 Spring Security 的依赖。

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-security&lt;/artifactId&gt;
&lt;/dependency&gt;

```

**步骤 2：铸造你的魔法咒语**

创建一个配置类 `SecurityConfig` 来定义你的安全配置。在这个咒语中，我们将定义哪些用户有权访问我们神秘的图书馆。

```
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
        auth.inMemoryAuthentication()
            .withUser("wizard").password(passwordEncoder().encode("ancientSecret")).roles("WIZARD")
            .and()
            .withUser("apprentice").password(passwordEncoder().encode("learning")).roles("APPRENTICE");
    }

    @Bean
    public PasswordEncoder passwordEncoder() {<!-- -->
        return new BCryptPasswordEncoder();
    }
}

```

在这段咒语中，我们定义了两个用户：“wizard” 和 “apprentice”，他们分别拥有不同的秘密和角色。

**步骤 3：守护你的图书馆入口**

现在，让我们创建一个简单的控制器 `LibraryController`，来守护我们的图书馆入口。

```
@RestController
public class LibraryController {<!-- -->

    @GetMapping("/")
    public String welcome() {<!-- -->
        return "Welcome to the Ancient Library!";
    }

    @GetMapping("/secret")
    public String secret() {<!-- -->
        return "Behold the Ancient Secrets!";
    }
}

```

这里，任何人都可以被欢迎进入图书馆，但只有通过了认证的访客才能看到古老的秘密。

**步骤 4：召唤你的应用守护程序**

现在，运行你的 Spring Boot 应用。访问 `http://localhost:8080/` 将显示欢迎信息。尝试访问 `http://localhost:8080/secret`，如果未登录，你将被重定向到登录页面。

恭喜你，你已经成功实现了基于内存的用户认证，保护了你神秘图书馆的秘密！通过这个简单的案例，你学会了如何使用 Spring Security 进行基本的安全配置，现在你的应用已经有了一个强大的守护者。

### 3.1.3 拓展案例 1：数据库用户认证

现在，让我们的守护程序升级，使它能够通过一个神秘的图书管理员名单（也就是数据库）来识别进入图书馆的访客。这个名单记录着每位图书管理员的名字和他们守护的秘密（用户名和密码）。

#### 案例 Demo：让数据库守护你的秘密

假设我们的应用已经有了一些基本的用户认证机制，现在我们要将用户信息存储在数据库中，而不是静静地躺在内存里。

**步骤 1：添加你的数据库和 JPA 魔法工具**

首先，确保你的 `pom.xml` 包含了对 Spring Data JPA 和数据库（这里使用 H2 作为例子）的支持。

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-data-jpa&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;com.h2database&lt;/groupId&gt;
    &lt;artifactId&gt;h2&lt;/artifactId&gt;
    &lt;scope&gt;runtime&lt;/scope&gt;
&lt;/dependency&gt;

```

**步骤 2：设计你的图书管理员名单**

创建一个 `Librarian` 实体来代表你的用户，并设计一个 `LibrarianRepository` 来访问数据库中的用户信息。

```
@Entity
public class Librarian {<!-- -->
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String username;
    private String password;

    // Standard getters and setters
}

public interface LibrarianRepository extends JpaRepository&lt;Librarian, Long&gt; {<!-- -->
    Optional&lt;Librarian&gt; findByUsername(String username);
}

```

**步骤 3：告诉你的守护程序如何读取名单**

实现 `UserDetailsService` 接口，让 Spring Security 知道如何通过 `LibrarianRepository` 从数据库中查找用户。

```
@Service
public class CustomUserDetailsService implements UserDetailsService {<!-- -->

    @Autowired
    private LibrarianRepository librarianRepository;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {<!-- -->
        Librarian librarian = librarianRepository.findByUsername(username)
                .orElseThrow(() -&gt; new UsernameNotFoundException("Librarian not found: " + username));

        return new User(librarian.getUsername(), librarian.getPassword(), new ArrayList&lt;&gt;());
    }
}

```

**步骤 4：配置你的保安来使用这个名单**

在你的 `SecurityConfig` 中，配置 `AuthenticationManagerBuilder` 以使用你的 `CustomUserDetailsService`。

```
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

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
}

```

**步骤 5：召唤并测试你的守护程序**

运行你的 Spring Boot 应用，并尝试使用存储在数据库中的用户信息进行登录。你可以通过 H2 Console 或其他数据库管理工具添加用户到你的 `Librarian` 表中来测试。

通过这个案例，你已经让你的应用升级，现在它可以通过数据库来认证用户了。这为保护你神秘的图书馆添加了一层额外的安全措施，确保只有真正的图书管理员能够进入。

### 3.1.4 拓展案例 2：集成 OAuth2 认证

在这个案例中，我们将通过集成 Lightweight Directory Access Protocol (LDAP) 认证来实现企业级的用户管理和认证机制。LDAP 是广泛用于企业环境中的用户和组织信息的目录服务协议，它允许应用以统一的方式查询和管理用户信息。

#### 案例 Demo

假设你正在开发一个需要对接企业LDAP服务器进行用户认证的Spring Boot应用。以下是如何实现LDAP认证的步骤：

**步骤 1：添加 LDAP 依赖**
<li> 在 `pom.xml` 中添加 Spring LDAP 的依赖。 <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-data-ldap&lt;/artifactId&gt;
&lt;/dependency&gt;
</code></pre> </li>
**步骤 2：配置 LDAP**
<li> 在 `application.properties` 或 `application.yml` 中配置 LDAP 连接信息，包括URL、用户DN（Distinguished Name）模式等。 <pre><code class="prism language-properties">spring.ldap.urls=ldap://localhost:8389
spring.ldap.base=dc=example,dc=com
spring.ldap.username=cn=admin,dc=example,dc=com
spring.ldap.password=admin
spring.ldap.user.dn-pattern=uid={0},ou=people
</code></pre> </li>
这些配置指定了LDAP服务器的地址、基础搜索路径、用于绑定（登录）的管理员用户名和密码，以及用于搜索用户的DN模式。

**步骤 3：实现 LDAP 认证**
<li> 创建一个安全配置类 `WebSecurityConfig`，使用LDAP进行认证。 <pre><code class="prism language-java">import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
        auth
            .ldapAuthentication()
            .userDnPatterns("uid={0},ou=people")
            .groupSearchBase("ou=groups")
            .contextSource()
            .url("ldap://localhost:8389/dc=example,dc=com")
            .and()
            .passwordCompare()
            .passwordEncoder(new BCryptPasswordEncoder())
            .passwordAttribute("userPassword");
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .authorizeRequests()
            .anyRequest().fullyAuthenticated()
            .and()
            .formLogin();
    }
}
</code></pre> </li>
这里我们配置了LDAP认证，指定用户和组的搜索基础，以及密码比对的策略。

**步骤 4：运行和测试**
1. 启动你的 Spring Boot 应用。1. 访问应用中的受保护资源，例如 `http://localhost:8080/`。1. 系统应该会重定向到登录页面。尝试使用 LDAP 服务器中的用户凭证进行登录。
通过整合 LDAP 认证，你的应用现在可以利用现有的企业级用户目录进行安全的用户认证，从而实现统一的身份管理和访问控制。这种方法特别适用于大型企业应用，能够大大简化用户管理和应用部署的复杂性。

## 3.2 配置用户详细信息服务

在 Spring Security 中，用户详细信息服务（`UserDetailsService`）是一个核心接口，用于从你选择的数据源加载用户信息。通过实现这个接口，Spring Security 可以在进行认证时获取到用户的详细信息，如用户名、密码和授权。

### 3.2.1 基础知识详解

在 Spring Security 中，用户详细信息服务（`UserDetailsService`）扮演着至关重要的角色。它负责从指定的数据源中加载用户的详细信息，这些信息随后被用于在认证过程中验证用户的身份。理解并正确配置用户详细信息服务对于建立一个安全的 Spring 应用来说是必不可少的。

#### 用户详细信息服务 (`UserDetailsService`)

`UserDetailsService` 是一个核心接口，定义了一个方法 `loadUserByUsername(String username)`，该方法接收一个用户名作为参数，并返回一个 `UserDetails` 实例，其中包含了用户的详细信息。如果指定用户名的用户不存在，则抛出一个 `UsernameNotFoundException`。

#### 密码编码 (`PasswordEncoder`)

为了安全地存储用户密码，Spring Security 提供了密码编码器的概念。`PasswordEncoder` 接口定义了密码编码（加密）和匹配（验证）方法。最常用的实现是 `BCryptPasswordEncoder`，它使用 BCrypt 强哈希算法来加密密码。使用密码编码器可以确保即使数据被泄露，攻击者也无法轻易地解码用户密码。

#### 认证管理器 (`AuthenticationManager`)

`AuthenticationManager` 是 Spring Security 认证架构的入口点。它定义了一个 `authenticate(Authentication authentication)` 方法，用于尝试对输入的认证信息进行认证。在配置 `WebSecurityConfigurerAdapter` 时，通过覆写 `configure(AuthenticationManagerBuilder auth)` 方法来设置应用的认证管理器，包括指定用户详细信息服务和密码编码器。

#### 自定义用户详细信息服务

虽然 Spring Security 提供了基于内存和基于JDBC的用户详细信息服务实现，但在许多情况下，你可能需要从不同的数据源加载用户信息，如使用 JPA 从关系型数据库或者连接到 LDAP 服务器。在这种情况下，你可以通过实现 `UserDetailsService` 接口来提供自定义的用户详细信息服务。

自定义实现通常会涉及到以下步骤：
1.  **实现 `UserDetailsService` 接口**：创建一个类来实现 `UserDetailsService` 接口，提供 `loadUserByUsername` 方法的具体实现，用于从你选择的数据源中加载用户信息。 1.  **配置认证管理器**：在你的安全配置中（一个扩展自 `WebSecurityConfigurerAdapter` 的类），通过覆写 `configure(AuthenticationManagerBuilder auth)` 方法来使用你的自定义 `UserDetailsService`。 1.  **使用密码编码器**：为了安全地处理密码，你应该在 `configure(AuthenticationManagerBuilder auth)` 方法中配置一个密码编码器（如 `BCryptPasswordEncoder`）。 
通过深入了解和配置用户详细信息服务，你可以确保你的 Spring 应用在处理用户认证时既灵活又安全。

### 3.2.2 主要案例：自定义数据库用户详细信息服务

在这个案例中，我们将通过自定义 `UserDetailsService` 实现，从数据库加载用户信息以进行认证。这对于需要动态管理用户信息的应用尤其重要。

#### 案例 Demo

假设我们正在开发一个需要用户认证的 Spring Boot 应用，并且希望用户信息存储在关系型数据库中。

**步骤 1**: 添加依赖
<li> 在 `pom.xml` 文件中添加 `spring-boot-starter-data-jpa` 和数据库相关依赖（这里以 H2 数据库为例）。 <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-data-jpa&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;com.h2database&lt;/groupId&gt;
    &lt;artifactId&gt;h2&lt;/artifactId&gt;
    &lt;scope&gt;runtime&lt;/scope&gt;
&lt;/dependency&gt;
</code></pre> </li>
**步骤 2**: 配置数据源
<li> 在 `application.properties` 中配置数据库连接。 <pre><code class="prism language-properties">spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
</code></pre> </li>
**步骤 3**: 创建用户实体和仓库
<li> 定义一个 `User` 实体类。 <pre><code class="prism language-java">@Entity
public class User {<!-- -->
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String username;
    private String password;
    // Constructors, Getters, and Setters
}
</code></pre> </li><li> 创建 `UserRepository` 接口。 <pre><code class="prism language-java">public interface UserRepository extends JpaRepository&lt;User, Long&gt; {<!-- -->
    Optional&lt;User&gt; findByUsername(String username);
}
</code></pre> </li>
**步骤 4**: 实现 `UserDetailsService`
<li> 创建 `CustomUserDetailsService` 类。 <pre><code class="prism language-java">@Service
public class CustomUserDetailsService implements UserDetailsService {<!-- -->
    @Autowired
    private UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {<!-- -->
        User user = userRepository.findByUsername(username)
            .orElseThrow(() -&gt; new UsernameNotFoundException("User not found with username: " + username));
        return new org.springframework.security.core.userdetails.User(user.getUsername(), user.getPassword(), new ArrayList&lt;&gt;());
    }
}
</code></pre> </li>
**步骤 5**: 配置安全性
<li> 创建 `SecurityConfig` 类，配置自定义的 `UserDetailsService` 和密码编码器。 <pre><code class="prism language-java">@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->
    @Autowired
    private CustomUserDetailsService userDetailsService;

    @Bean
    public PasswordEncoder passwordEncoder() {<!-- -->
        return new BCryptPasswordEncoder();
    }

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
        auth.userDetailsService(userDetailsService)
            .passwordEncoder(passwordEncoder());
    }
}
</code></pre> </li>
通过这个案例，你将学会如何自定义 `UserDetailsService` 以从数据库加载用户信息，并在 Spring Security 中使用这些信息进行认证。这种方法为你提供了灵活性来管理用户信息，并且能够确保你的应用安全性。

### 3.2.3 拓展案例 1：内存中的用户存储

对于开发环境或小型应用，可能你只需要一个简单的用户存储而不想引入外部数据库的复杂性。在这种情况下，Spring Security 允许你在内存中定义用户列表，这是一个快速启动和测试安全配置的好方法。

#### 案例 Demo

让我们创建一个 Spring Boot 应用，其中用户认证信息存储在内存中，以简化认证流程。

**步骤 1**: 添加 Spring Security 依赖

首先，确保你的 `pom.xml` 包含了 Spring Security 的起步依赖。

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-security&lt;/artifactId&gt;
&lt;/dependency&gt;

```

**步骤 2**: 配置内存中的用户存储

创建一个安全配置类 `SecurityConfig`，在这个类中，你将定义用户的认证信息。

```
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.password.NoOpPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
        auth.inMemoryAuthentication()
            .withUser("user").password("password").roles("USER")
            .and()
            .withUser("admin").password("admin").roles("ADMIN");
    }

    @SuppressWarnings("deprecation")
    @Bean
    public PasswordEncoder passwordEncoder() {<!-- -->
        // WARNING: This is only for demonstration purposes and should not be used in production
        return NoOpPasswordEncoder.getInstance();
    }
}

```

在这个配置中，我们定义了两个用户，一个是普通用户，另一个是管理员，都使用了不安全的密码编码器 `NoOpPasswordEncoder` 来避免密码加密。**注意**：`NoOpPasswordEncoder` 已被弃用，仅用于演示目的，生产环境中应使用强密码编码器如 `BCryptPasswordEncoder`。

**步骤 3**: 测试认证

运行你的 Spring Boot 应用，并尝试访问任何受保护的资源。你将被重定向到登录页面，此时可以使用上面定义的用户凭证进行登录。

通过这个简单的案例，你可以快速地在 Spring Boot 应用中实现用户认证功能，而不需要配置外部数据源。这对于原型开发或小型应用来说是一个理想的选择。

### 3.2.4 拓展案例 2：使用 JdbcUserDetailsManager

当你的应用需要从关系型数据库中加载用户信息进行认证时，Spring Security 提供了一个方便的方式来实现这一需求——使用 `JdbcUserDetailsManager`。这个方法不仅支持用户信息的加载，还支持通过 JDBC 进行用户的增加、删除和修改操作。

#### 案例 Demo

我们将构建一个 Spring Boot 应用，使用 `JdbcUserDetailsManager` 从数据库加载用户信息进行认证。

**步骤 1**: 添加依赖

在你的 `pom.xml` 文件中添加 Spring Boot 的数据 JPA 起步依赖和数据库驱动依赖（以 H2 数据库为例）。

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-data-jpa&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;com.h2database&lt;/groupId&gt;
    &lt;artifactId&gt;h2&lt;/artifactId&gt;
    &lt;scope&gt;runtime&lt;/scope&gt;
&lt;/dependency&gt;

```

**步骤 2**: 配置数据源和安全配置

在 `application.properties` 文件中配置你的数据库连接，以及启用 H2 控制台。

```
spring.datasource.url=jdbc:h2:mem:testdb;DB_CLOSE_DELAY=-1
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password
spring.h2.console.enabled=true
spring.sql.init.platform=h2

```

创建安全配置类 `SecurityConfig`，配置 `JdbcUserDetailsManager`。

```
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.provisioning.JdbcUserDetailsManager;

import javax.sql.DataSource;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Bean
    public UserDetailsService userDetailsService(DataSource dataSource) {<!-- -->
        return new JdbcUserDetailsManager(dataSource);
    }

    @Bean
    public PasswordEncoder passwordEncoder() {<!-- -->
        return new BCryptPasswordEncoder();
    }

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
        auth
            .jdbcAuthentication()
            .dataSource(dataSource())
            .usersByUsernameQuery("select username, password, enabled from users where username=?")
            .authoritiesByUsernameQuery("select username, authority from authorities where username=?")
            .passwordEncoder(passwordEncoder());
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .authorizeRequests()
            .anyRequest().authenticated()
            .and()
            .formLogin()
            .and()
            .httpBasic();
    }
}

```

**步骤 3**: 初始化用户数据

通常，你需要预先在数据库中创建 `users` 和 `authorities` 表，并插入一些测试用户。你可以使用 Spring SQL 初始化特性来自动完成这一步骤。

在 `src/main/resources/schema.sql` 中定义表结构：

```
CREATE TABLE users (
  username VARCHAR(50) NOT NULL PRIMARY KEY,
  password VARCHAR(100) NOT NULL,
  enabled BOOLEAN NOT NULL
);

CREATE TABLE authorities (
  username VARCHAR(50) NOT NULL,
  authority VARCHAR(50) NOT NULL,
  FOREIGN KEY (username) REFERENCES users(username)
);

```

在 `src/main/resources/data.sql` 中插入测试数据：

```
INSERT INTO users (username, password, enabled) VALUES ('user', '{bcrypt}加密后的密码', true);
INSERT INTO authorities (username, authority) VALUES ('user', 'ROLE_USER');

```

确保将 `{bcrypt}加密后的密码` 替换为使用 `BCryptPasswordEncoder` 加密的密码。

**步骤 4**: 测试认证

启动应用并访问任何受保护的 URL，系统应重定向你到登录页面。使用步骤 3 中定义的用户凭证进行登录，验证认证流程是否按预期工作。

通过使用 `JdbcUserDetailsManager`，你可以轻松地将 Spring Security 与数据库用户存储集成，实现复杂的认证和用户管理功能。这种方式适合需要持久化用户信息的中大型应用。

## 3.3 自定义认证逻辑

在 Spring Security 中，定制认证逻辑可以让你实现更加复杂和安全的认证机制，比如添加验证码校验、实现多因素认证等。Spring Security 提供了灵活的扩展点，使得定制认证过程变得可行。

### 3.3.1 基础知识详解

#### 认证管理器 (`AuthenticationManager`)
- `AuthenticationManager` 是 Spring Security 认证机制的中心接口，负责协调认证过程。- 它定义了一个 `authenticate(Authentication authentication)` 方法，用于尝试对输入的认证信息进行认证。
#### 认证提供者 (`AuthenticationProvider`)
- `AuthenticationProvider` 接口定义了实际执行认证逻辑的方法。- 每个 `AuthenticationProvider` 都能处理特定类型的认证请求。例如，你可以有一个专门处理用户名和密码认证的提供者，另一个处理基于短信验证码的认证。
#### 用户详细信息服务 (`UserDetailsService`)
- `UserDetailsService` 是一个用于加载用户特定数据的核心接口。它只有一个方法 `loadUserByUsername(String username)`，用于根据用户名查找 `UserDetails` 对象。- `UserDetails` 对象包含了一些基本的用户信息，如用户名、密码、权限等。
#### 密码编码 (`PasswordEncoder`)
- 在认证过程中，用户提交的密码需要与存储在系统中的密码进行比对。为了安全起见，存储的密码通常是加密过的。- `PasswordEncoder` 接口定义了加密和匹配用户密码的方法。使用强加密算法（如 BCrypt）可以有效防止密码被破解。
#### 自定义认证逻辑的意义
- **安全性提升**：通过自定义认证逻辑，开发者可以引入额外的安全措施，如验证码验证、多因素认证等，进一步增强应用的安全性。- **灵活性和扩展性**：每个应用的安全需求都是独特的。Spring Security 的可扩展性允许开发者根据自己的需求定制认证过程。- **集成第三方服务**：在现代的应用中，常常需要集成第三方认证服务（如社交登录）。自定义认证逻辑使得这种集成变得可行。
通过深入理解和应用上述基础知识，开发者可以充分利用 Spring Security 提供的强大功能，实现既安全又符合业务需求的认证机制。

### 3.3.2 主要案例：添加验证码校验

在这个案例中，我们将实现一个包含验证码校验的自定义认证流程，以增强登录过程的安全性。验证码校验是一种常见的防止自动化攻击（如暴力破解、机器人登录）的手段。

#### 案例 Demo

假设我们的 Spring Boot 应用有一个登录表单，我们想在用户提交表单时验证一个验证码字段。

**步骤 1**: 集成验证码服务

首先，假设你有一个服务来生成和验证验证码，我们将其称为 `CaptchaService`。

```
@Service
public class CaptchaService {<!-- -->

    public boolean validateCaptcha(String sessionId, String captcha) {<!-- -->
        // 模拟验证码校验逻辑
        // 在实际应用中，应该根据 sessionId 查找预先存储的验证码，并与用户输入的 captcha 进行比对
        return "expectedCaptcha".equals(captcha);
    }
}

```

**步骤 2**: 自定义认证过滤器

创建一个自定义的认证过滤器 `CustomAuthenticationFilter`，在尝试认证之前校验验证码。

```
public class CustomAuthenticationFilter extends UsernamePasswordAuthenticationFilter {<!-- -->

    @Autowired
    private CaptchaService captchaService;

    @Override
    public Authentication attemptAuthentication(HttpServletRequest request, HttpServletResponse response)
            throws AuthenticationException {<!-- -->
        String captcha = request.getParameter("captcha");
        String sessionId = request.getSession().getId();

        if (!captchaService.validateCaptcha(sessionId, captcha)) {<!-- -->
            throw new AuthenticationServiceException("验证码错误");
        }

        return super.attemptAuthentication(request, response);
    }
}

```

**步骤 3**: 配置自定义过滤器

在你的安全配置类中，注册自定义的认证过滤器并设置其在 `UsernamePasswordAuthenticationFilter` 之前执行。

```
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Autowired
    private CustomAuthenticationFilter customAuthenticationFilter;

    @Autowired
    public void configureGlobal(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
        // 配置用户认证逻辑，例如使用 inMemoryAuthentication 或其他
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            // 其他配置...
            .addFilterBefore(customAuthenticationFilter, UsernamePasswordAuthenticationFilter.class);
    }

    @Bean
    @Override
    public AuthenticationManager authenticationManagerBean() throws Exception {<!-- -->
        return super.authenticationManagerBean();
    }
    
    @Bean
    public CustomAuthenticationFilter customAuthenticationFilter() throws Exception {<!-- -->
      CustomAuthenticationFilter filter = new CustomAuthenticationFilter();
      filter.setAuthenticationManager(authenticationManagerBean());
      return filter;
    }
}

```

**步骤 4**: 测试验证码功能

启动应用并访问登录页面。尝试不输入验证码或输入错误的验证码提交登录表单，应该被阻止并提示验证码错误。

通过实现这个案例，你将学会如何在 Spring Security 的认证过程中加入额外的校验步骤，如验证码校验，以增强应用的安全性。这种方法为防止自动化攻击提供了一层额外的保护。

### 3.3.3 拓展案例 1：实现基于短信的认证

在这个案例中，我们将通过实现基于短信验证码的认证流程来增强应用的安全性。这种方法适合于需要额外安全措施的场景，例如金融应用或敏感数据的访问控制。

#### 案例 Demo

**步骤 1**: 创建短信验证码服务

首先，创建一个服务来发送和验证短信验证码，这里我们称之为 `SmsCodeService`。

```
@Service
public class SmsCodeService {<!-- -->

    private final Map&lt;String, String&gt; smsCodeStorage = new ConcurrentHashMap&lt;&gt;();

    public void sendSmsCode(String mobile, String code) {<!-- -->
        // 实际项目中应调用短信服务提供商的API发送短信
        // 这里仅做模拟
        smsCodeStorage.put(mobile, code);
        System.out.println("Sending SMS code " + code + " to " + mobile);
    }

    public boolean validateSmsCode(String mobile, String code) {<!-- -->
        String validCode = smsCodeStorage.get(mobile);
        return code.equals(validCode);
    }
}

```

**步骤 2**: 定义短信认证令牌

创建一个 `SmsAuthenticationToken` 类来表示短信认证的令牌。

```
public class SmsAuthenticationToken extends AbstractAuthenticationToken {<!-- -->

    private final Object principal;
    private String code;

    public SmsAuthenticationToken(String mobile, String code) {<!-- -->
        super(null);
        this.principal = mobile;
        this.code = code;
        setAuthenticated(false);
    }

    public SmsAuthenticationToken(String mobile, Collection&lt;? extends GrantedAuthority&gt; authorities) {<!-- -->
        super(authorities);
        this.principal = mobile;
        this.code = null;
        super.setAuthenticated(true); // must use super, as we override
    }

    @Override
    public Object getCredentials() {<!-- -->
        return code;
    }

    @Override
    public Object getPrincipal() {<!-- -->
        return this.principal;
    }
}

```

**步骤 3**: 实现短信认证提供者

创建一个 `SmsAuthenticationProvider` 类来实现短信验证码的认证逻辑。

```
@Component
public class SmsAuthenticationProvider implements AuthenticationProvider {<!-- -->

    @Autowired
    private SmsCodeService smsCodeService;

    @Autowired
    private MyUserDetailsService myUserDetailsService; // 自定义的UserDetailsService实现

    @Override
    public Authentication authenticate(Authentication authentication) throws AuthenticationException {<!-- -->
        SmsAuthenticationToken authenticationToken = (SmsAuthenticationToken) authentication;
        String mobile = (String) authenticationToken.getPrincipal();
        String code = (String) authenticationToken.getCredentials();

        if (!smsCodeService.validateSmsCode(mobile, code)) {<!-- -->
            throw new BadCredentialsException("短信验证码错误");
        }

        UserDetails userDetails = myUserDetailsService.loadUserByMobile(mobile);
        if (userDetails == null) {<!-- -->
            throw new UsernameNotFoundException("用户不存在");
        }

        SmsAuthenticationToken authenticationResult = new SmsAuthenticationToken(userDetails, userDetails.getAuthorities());
        authenticationResult.setDetails(authenticationToken.getDetails());

        return authenticationResult;
    }

    @Override
    public boolean supports(Class&lt;?&gt; authentication) {<!-- -->
        return (SmsAuthenticationToken.class.isAssignableFrom(authentication));
    }
}

```

**步骤 4**: 配置短信认证

在安全配置类中注册 `SmsAuthenticationProvider`。

```
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Autowired
    private SmsAuthenticationProvider smsAuthenticationProvider;

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
        auth.authenticationProvider(smsAuthenticationProvider);
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        // 配置安全规则
    }
}

```

**步骤 5**: 测试短信认证

启动应用并尝试使用短信验证码登录。你可以创建一个简单的登录页面，用于输入手机号和验证码，然后通过后端接口验证。

通过实现这个案例，你将能够为你的应用添加基于短信验证码的二次认证流程，提高安全性。这种认证方式在需要额外验证用户身份的场景中非常有用，尤其是在移动应用中。

### 3.3.4 拓展案例 2：集成第三方认证服务

在这个案例中，我们将演示如何将第三方认证服务（例如 OAuth2 提供商，如 Google 或 Facebook）集成到 Spring Boot 应用中，为用户提供更多便捷的登录选项。

#### 案例 Demo

假设我们希望用户可以通过 Google 账户登录我们的应用。

**步骤 1**: 添加依赖

首先，确保你的 `pom.xml` 包含了 Spring Security OAuth2 客户端的起步依赖。

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-oauth2-client&lt;/artifactId&gt;
&lt;/dependency&gt;

```

**步骤 2**: 配置 OAuth2 客户端

在 `application.yml` 或 `application.properties` 文件中配置 OAuth2 客户端信息。以下是使用 Google 作为 OAuth2 提供商的一个例子：

```
spring.security.oauth2.client.registration.google.client-id=your-google-client-id
spring.security.oauth2.client.registration.google.client-secret=your-google-client-secret
spring.security.oauth2.client.registration.google.scope=profile,email

```

你需要替换 `your-google-client-id` 和 `your-google-client-secret` 为你在 Google Cloud Platform 创建 OAuth2 客户端时获得的客户端 ID 和密钥。

**步骤 3**: 创建安全配置

创建一个安全配置类 `SecurityConfig`，配置使用 OAuth2 登录：

```
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .authorizeRequests()
            .anyRequest().authenticated()
            .and()
            .oauth2Login();
    }
}

```

这个配置确保了所有请求都需要认证，并启用了 OAuth2 登录。

**步骤 4**: 测试 OAuth2 登录

启动应用并尝试访问任何受保护的资源。系统应该会重定向你到 Google 的登录页面。使用你的 Google 账户登录后，你将被重定向回应用，并成功访问受保护的资源。

#### 拓展：自定义 OAuth2 登录行为

Spring Security 允许你自定义 OAuth2 登录行为，例如自定义登录成功或失败后的处理逻辑：

```
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.oauth2.client.oidc.userinfo.OidcUserService;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .authorizeRequests()
            .anyRequest().authenticated()
            .and()
            .oauth2Login()
                .userInfoEndpoint()
                .oidcUserService(this.oidcUserService());
    }

    private OidcUserService oidcUserService() {<!-- -->
        OidcUserService service = new OidcUserService();
        service.setUserinfoCustomizer((userRequest, user) -&gt; {<!-- -->
            // 自定义用户信息处理逻辑
        });
        return service;
    }
}

```

通过实现这个案例，你可以向你的应用添加更多的登录选项，提供更便捷的用户体验，并利用第三方服务提供的安全性。这种方法尤其适用于希望简化登录过程或提供社交登录选项的现代应用。
