
--- 
title:  第1章 Spring Security 概述（2024 最新版） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/a4fd0eb490094e48934987c2ef0f7986.png#pic_center" alt="在这里插入图片描述"> 

#### 文章目录
- - <ul><li>- - - - - - - - - - - 


## 1.1 Spring Security 的重要性

在这一节中，我们将首先深入探讨 Spring Security 的基础知识，然后通过三个实际案例，展示其在现实生产环境中的应用。这些案例将以 Java 为核心，展现 Spring Security 在保护应用程序方面的实用性。

### 1.1.1 基础知识详解

**Spring Security 的重要性**

在深入探讨 Spring Security 之前，让我们先了解为什么这个框架在现代 Web 应用开发中如此重要。
1.  **安全性的核心需求**： 在数字时代，安全性是任何 Web 应用的基石。Spring Security 提供了一个健壮的安全框架，帮助开发者保护他们的应用免受各种网络攻击和安全威胁。 1.  **广泛的应用场景**： 无论是小型企业应用还是大型企业级系统，Spring Security 都能灵活适应。它不仅支持传统的 Web 应用，还能很好地与微服务架构和云服务集成。 1.  **社区和支持**： 作为 Spring 生态系统的一部分，Spring Security 拥有一个活跃的开发者社区和丰富的文档资源。这意味着它不断更新，能够应对新出现的安全挑战。 
**Spring Security 的核心概念**
<li> **认证（Authentication）**： 
  1. 认证是确认某个实体的身份。在 Spring Security 中，这通常指验证用户名和密码，但也可以扩展到更复杂的方法，如多因素认证。1. Spring Security 支持多种认证方式，如表单登录、LDAP、OAuth2 等。 </li><li> **授权（Authorization）**： 
  1. 授权涉及决定认证通过的实体可以访问哪些资源。简单来说，就是决定谁能做什么。1. Spring Security 通过角色和权限来管理授权。它允许细粒度控制，比如基于方法的安全性。 </li><li> **防护措施**： 
  1. Spring Security 提供了多种防护措施来保护应用免受常见的网络攻击，例如跨站请求伪造（CSRF）和会话固定攻击。1. 它还提供了其他高级功能，如安全通道（HTTPS 强制使用）和内容安全策略（CSP）。 </li><li> **过滤器链**： 
  1. Spring Security 使用一系列过滤器来处理安全相关的任务。这些过滤器在请求进入应用之前拦截请求，执行例如认证和授权的操作。1. 了解这些过滤器及其顺序对于深入理解 Spring Security 的工作原理至关重要。 </li>- 授权涉及决定认证通过的实体可以访问哪些资源。简单来说，就是决定谁能做什么。- Spring Security 通过角色和权限来管理授权。它允许细粒度控制，比如基于方法的安全性。- Spring Security 使用一系列过滤器来处理安全相关的任务。这些过滤器在请求进入应用之前拦截请求，执行例如认证和授权的操作。- 了解这些过滤器及其顺序对于深入理解 Spring Security 的工作原理至关重要。
通过理解这些基础概念，开发者能够更好地利用 Spring Security 为他们的应用提供坚固的安全基础。下一步，我们将深入探讨如何在实际应用中实现这些概念，并通过具体案例加以展示。

### 1.1.2 主要案例：用户认证与授权

在这个案例中，我们将展示如何在一个 Spring Boot 应用程序中实现基本的用户认证和授权。这个案例将重点介绍如何配置 Spring Security 来管理用户登录，并根据用户角色授权访问特定资源。

**案例 Demo**

假设我们正在开发一个小型网站，该网站有两种类型的用户：普通用户和管理员。我们需要确保普通用户只能访问主页，而管理员则可以访问管理面板。

**步骤 1：创建 Spring Boot 应用程序**

首先，我们需要创建一个基本的 Spring Boot 应用程序。您可以使用 Spring Initializr（https://start.spring.io/）快速生成项目结构。

添加以下依赖：
- Spring Web- Spring Security
**步骤 2：配置 Spring Security**

在我们的 Spring Boot 应用程序中，我们需要配置 Spring Security 来处理用户认证和授权。创建一个类继承自 `WebSecurityConfigurerAdapter` 并覆盖相应的方法。

```
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
        auth.inMemoryAuthentication()
            .withUser("user").password("{noop}password").roles("USER")
            .and()
            .withUser("admin").password("{noop}adminpass").roles("ADMIN");
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .authorizeRequests()
                .antMatchers("/admin").hasRole("ADMIN")
                .antMatchers("/").hasAnyRole("USER", "ADMIN")
                .and()
            .formLogin();
    }
}

```

在这个配置中，我们定义了两个用户：一个普通用户和一个管理员，以及它们的权限。我们还启用了表单登录。

**步骤 3：创建控制器**

现在，我们需要创建一个简单的控制器来管理不同的页面。

```
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class MainController {<!-- -->

    @GetMapping("/")
    public String home() {<!-- -->
        return "home";
    }

    @GetMapping("/admin")
    public String admin() {<!-- -->
        return "admin";
    }
}

```

**步骤 4：创建视图**

为了完整性，我们还需要创建两个简单的 HTML 页面（`home.html` 和 `admin.html`）来表示主页和管理页面。

**步骤 5：运行和测试**

运行您的 Spring Boot 应用程序，并访问 `http://localhost:8080/`。您应该会看到一个登录表单。使用不同的用户登录，并验证它们是否能正确访问对应的页面。

通过这个案例，您不仅能够了解如何在 Spring Security 中实现基本的认证和授权机制，还能够看到这些概念在实际应用中是如何工作的。这为您提供了一个坚实的基础，让您可以根据自己的需要进一步扩展和定制安全性配置。

### 1.1.3 拓展案例 1：OAuth2 社交登录

在这个案例中，我们将展示如何在 Spring Boot 应用中集成 OAuth2 社交登录，允许用户通过 Google 账户登录。这种方式提供了一种更便捷、安全的用户认证方法，同时提高了用户体验。

**案例 Demo**

假设我们的 Spring Boot 应用需要提供用户通过 Google 账户登录的功能。我们将使用 Spring Security 的 OAuth2 客户端支持来实现这一点。

**步骤 1：添加相关依赖**

首先，在你的 `pom.xml` 文件中添加以下依赖：

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-oauth2-client&lt;/artifactId&gt;
&lt;/dependency&gt;

```

**步骤 2：配置 OAuth2 登录**

在 `application.properties` 或 `application.yml` 文件中，添加 Google OAuth2 客户端配置：

```
spring.security.oauth2.client.registration.google.client-id=YOUR_GOOGLE_CLIENT_ID
spring.security.oauth2.client.registration.google.client-secret=YOUR_GOOGLE_CLIENT_SECRET
spring.security.oauth2.client.registration.google.scope=profile,email

```

你需要替换 `YOUR_GOOGLE_CLIENT_ID` 和 `YOUR_GOOGLE_CLIENT_SECRET` 为你从 Google Cloud Console 获得的实际值。

**步骤 3：安全配置**

更新你的 `SecurityConfig` 类，以支持 OAuth2 登录：

```
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.context.annotation.Configuration;

@Configuration
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

这里我们配置了所有请求都需要认证，并且启用了 OAuth2 登录。

**步骤 4：用户信息获取和处理**

当用户通过 Google 登录后，你可能需要获取并处理用户信息。你可以通过实现 `OAuth2UserService` 来完成这一步：

```
import org.springframework.security.oauth2.client.userinfo.DefaultOAuth2UserService;
import org.springframework.security.oauth2.client.userinfo.OAuth2UserRequest;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.stereotype.Service;

@Service
public class CustomOAuth2UserService extends DefaultOAuth2UserService {<!-- -->

    @Override
    public OAuth2User loadUser(OAuth2UserRequest userRequest) throws OAuth2AuthenticationException {<!-- -->
        OAuth2User user = super.loadUser(userRequest);
        // 处理用户信息逻辑
        return user;
    }
}

```

**步骤 5：运行和测试**

启动应用程序并访问 `http://localhost:8080/`。现在，你应该能看到一个通过 Google 登录的选项。使用你的 Google 账户登录，并验证登录流程是否正常工作。

通过这个案例，你可以看到如何在 Spring Boot 应用中轻松集成 OAuth2 社交登录。这个功能不仅提高了用户体验，还增强了应用的安全性。

### 1.1.4 拓展案例 2：JWT 认证

在这个案例中，我们将演示如何在 Spring Boot 应用中实现基于 JSON Web Token (JWT) 的认证。JWT 是一种广泛使用的技术，用于在客户端和服务器之间安全地传输信息。

**案例 Demo**

假设我们正在开发一个 RESTful API，我们希望通过 JWT 来认证和授权用户。

**步骤 1：添加 JWT 相关依赖**

首先，在你的 `pom.xml` 文件中添加 JWT 的依赖。我们将使用 `java-jwt` 库：

```
&lt;dependency&gt;
    &lt;groupId&gt;com.auth0&lt;/groupId&gt;
    &lt;artifactId&gt;java-jwt&lt;/artifactId&gt;
    &lt;version&gt;3.10.3&lt;/version&gt;
&lt;/dependency&gt;

```

**步骤 2：实现 JWT 工具类**

创建一个 JWT 工具类来生成和解析 JWT。这个类将负责创建令牌、验证令牌以及解析令牌：

```
import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.exceptions.JWTVerificationException;
import com.auth0.jwt.interfaces.DecodedJWT;
import com.auth0.jwt.interfaces.JWTVerifier;

import java.util.Date;

public class JwtUtil {<!-- -->
    private static final String SECRET_KEY = "your_secret_key";

    public static String createToken(String username) {<!-- -->
        return JWT.create()
                .withSubject(username)
                .withExpiresAt(new Date(System.currentTimeMillis() + 864000000)) // 设置过期时间
                .sign(Algorithm.HMAC256(SECRET_KEY));
    }

    public static String validateTokenAndRetrieveSubject(String token) {<!-- -->
        try {<!-- -->
            JWTVerifier verifier = JWT.require(Algorithm.HMAC256(SECRET_KEY)).build();
            DecodedJWT jwt = verifier.verify(token);
            return jwt.getSubject();
        } catch (JWTVerificationException exception) {<!-- -->
            //Invalid signature/claims
            return null;
        }
    }
}

```

**步骤 3：配置 Spring Security**

在 Spring Security 配置中，我们需要添加一个过滤器来检查传入的请求中的 JWT。

创建一个 JWT 过滤器类：

```
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.FilterChain;
import java.io.IOException;
import java.util.Collections;

public class JwtFilter extends UsernamePasswordAuthenticationFilter {<!-- -->

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain chain)
            throws IOException, ServletException {<!-- -->
        String token = request.getHeader("Authorization");
        if (token != null &amp;&amp; token.startsWith("Bearer ")) {<!-- -->
            token = token.substring(7);
            String username = JwtUtil.validateTokenAndRetrieveSubject(token);

            if (username != null) {<!-- -->
                UsernamePasswordAuthenticationToken auth = new UsernamePasswordAuthenticationToken(
                        username, null, Collections.singletonList(new SimpleGrantedAuthority("USER")));
                SecurityContextHolder.getContext().setAuthentication(auth);
            }
        }
        chain.doFilter(request, response);
    }
}

```

然后，在 `SecurityConfig` 类中注册这个过滤器：

```
@Override
protected void configure(HttpSecurity http) throws Exception {<!-- -->
    http.addFilterBefore(new JwtFilter(), UsernamePasswordAuthenticationFilter.class);
    // 其他配置...
}

```

**步骤 4：创建认证端点**

在你的控制器中，创建一个端点用于生成 JWT：

```
@PostMapping("/authenticate")
public ResponseEntity&lt;?&gt; createAuthToken(@RequestParam String username) {<!-- -->
    String token = JwtUtil.createToken(username);
    return ResponseEntity.ok(token);
}

```

**步骤 5：运行和测试**

启动你的应用程序，然后向 `/authenticate` 端点发送一个请求，携带用户名。你应该会收到一个 JWT。然后，你可以使用这个 JWT 来访问受保护的资源。

通过这个案例，你可以看到如何在 Spring Boot 应用中使用 JWT 进行认证。JWT 认证在开发现代 Web 应用和微服务架构时非常有用，尤其是在处理跨域请求和轻量级认证时。

## 1.2 Spring Security 的核心特性

### 1.2.1 基础知识详解

**Spring Security 的核心特性**
<li> **认证和授权**： 
  1. **认证** 是验证用户身份的过程。Spring Security 支持多种认证方式，包括但不限于用户名和密码验证、LDAP 认证、OAuth2、JWT 等。1. **授权** 则是决定已认证用户可以访问哪些资源的过程。Spring Security 允许你基于角色或更细粒度的权限来控制访问。 </li><li> **CSRF 防护**： 
  1. CSRF 攻击是一种常见的网络攻击方式，它试图利用用户的登录状态执行未经授权的操作。Spring Security 提供了 CSRF 防护机制，默认情况下在所有的 POST 请求上启用。 </li><li> **会话管理**： 
  1. 会话管理涉及用户的登录会话和会话过期。Spring Security 提供了丰富的会话管理功能，包括会话固定保护和并发会话控制。 </li><li> **密码存储**： 
  1. Spring Security 支持多种密码存储格式，包括明文、哈希、PBKDF2、SCrypt 等，并且鼓励开发者使用强密码编码方式。 </li><li> **方法级安全**： 
  1. 除了 URL 级别的安全控制外，Spring Security 还支持方法级别的安全控制。这允许开发者直接在 Java 方法上应用安全注解，实现更细粒度的控制。 </li><li> **LDAP 集成**： 
  1. 对于需要与 LDAP 目录服务集成的应用程序，Spring Security 提供了简便的集成方式。这使得在企业环境中实现认证和授权变得容易。 </li><li> **OAuth2 和 OpenID Connect**： 
  1. Spring Security 支持现代认证和授权协议，如 OAuth2 和 OpenID Connect，使得它可以与第三方认证提供者（如 Google、Facebook 等）轻松集成。 </li><li> **跨域资源共享（CORS）支持**： 
  1. 在开发 SPA（单页面应用程序）或调用跨域 API 时，CORS 是一个常见的问题。Spring Security 提供了 CORS 支持，允许开发者配置跨域请求的处理。 </li>- CSRF 攻击是一种常见的网络攻击方式，它试图利用用户的登录状态执行未经授权的操作。Spring Security 提供了 CSRF 防护机制，默认情况下在所有的 POST 请求上启用。- Spring Security 支持多种密码存储格式，包括明文、哈希、PBKDF2、SCrypt 等，并且鼓励开发者使用强密码编码方式。- 对于需要与 LDAP 目录服务集成的应用程序，Spring Security 提供了简便的集成方式。这使得在企业环境中实现认证和授权变得容易。- 在开发 SPA（单页面应用程序）或调用跨域 API 时，CORS 是一个常见的问题。Spring Security 提供了 CORS 支持，允许开发者配置跨域请求的处理。
通过掌握这些基础知识，开发者可以利用 Spring Security 为他们的应用程序构建一个强大且灵活的安全系统。接下来的案例将更具体地展示如何将这些特性应用于实际开发中。

### 1.2.2 主要案例：基于角色的访问控制

在这个案例中，我们将演示如何在 Spring Boot 应用中实现基于角色的访问控制（RBAC）。我们假设有两种角色：“USER” 和 “ADMIN”，每种角色都有不同的访问权限。

**案例 Demo**

我们将创建一个简单的 Spring Boot 应用程序，其中包含两个受保护的页面：一个仅对普通用户开放，另一个仅对管理员开放。

**实现步骤**:
1.  **创建 Spring Boot 应用程序**: 使用 Spring Initializr 创建一个新的 Spring Boot 项目，并添加 `spring-boot-starter-web` 和 `spring-boot-starter-security` 依赖。 <li> **配置安全性**: 创建一个继承自 `WebSecurityConfigurerAdapter` 的配置类来定义安全规则。 <pre><code class="prism language-java">import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;

@Configuration
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
        auth.inMemoryAuthentication()
            .withUser("user").password("{noop}password").roles("USER")
            .and()
            .withUser("admin").password("{noop}adminpass").roles("ADMIN");
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .authorizeRequests()
            .antMatchers("/user").hasRole("USER")
            .antMatchers("/admin").hasRole("ADMIN")
            .anyRequest().authenticated()
            .and()
            .formLogin()
            .and()
            .logout();
    }
}
</code></pre> 在这个配置中，我们定义了两个用户和他们的角色。同时，我们设置了 `/user` 只能被 USER 角色访问，`/admin` 只能被 ADMIN 角色访问。 </li><li> **创建控制器**: 创建一个控制器来管理不同的页面。 <pre><code class="prism language-java">import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class MainController {<!-- -->

    @GetMapping("/user")
    public String user() {<!-- -->
        return "user";
    }

    @GetMapping("/admin")
    public String admin() {<!-- -->
        return "admin";
    }
}
</code></pre> </li>1.  **创建视图**: 为 `user` 和 `admin` 路径分别创建视图文件，例如 `user.html` 和 `admin.html`。 1.  **运行和测试**: 运行应用程序并访问 `http://localhost:8080/user` 和 `http://localhost:8080/admin`。尝试使用不同的用户登录并验证它们是否能访问正确的页面。 
通过这个案例，您将看到 Spring Security 如何实现基于角色的访问控制，这是构建安全 Web 应用程序的基础。这种方法可以确保用户只能访问他们被授权的资源。

### 1.2.3 拓展案例 1：表单登录与数据库用户存储

在这个案例中，我们将演示如何结合表单登录和数据库用户存储在 Spring Boot 应用中实现用户认证。这将涉及从数据库中加载用户信息，并根据这些信息进行认证。

**案例 Demo**

假设我们有一个应用程序，其中用户信息存储在数据库中。我们需要实现一个表单登录页面，用户可以使用其数据库中的凭据进行登录。

**实现步骤**:
<li> **添加依赖**: 在 `pom.xml` 中添加 `spring-boot-starter-data-jpa` 和数据库相关的依赖，例如 `spring-boot-starter-data-jpa` 和 `h2`（作为示例数据库）。 <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-data-jpa&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;com.h2database&lt;/groupId&gt;
    &lt;artifactId&gt;h2&lt;/artifactId&gt;
    &lt;scope&gt;runtime&lt;/scope&gt;
&lt;/dependency&gt;
</code></pre> </li><li> **配置数据源**: 在 `application.properties` 中配置数据库连接信息。对于 H2 数据库，可以使用内存模式。 <pre><code class="prism language-properties">spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
</code></pre> </li><li> **创建用户模型和仓库**: 定义一个用户实体类和一个继承 `JpaRepository` 的接口。 <pre><code class="prism language-java">import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class User {<!-- -->
    @Id
    private String username;
    private String password;
    // 省略 getter 和 setter
}

import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository&lt;User, String&gt; {<!-- -->
}
</code></pre> </li><li> **实现 UserDetailsService**: 实现 `UserDetailsService` 接口，从数据库中加载用户信息。 <pre><code class="prism language-java">import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;

public class CustomUserDetailsService implements UserDetailsService {<!-- -->

    @Autowired
    private UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {<!-- -->
        User user = userRepository.findById(username)
            .orElseThrow(() -&gt; new UsernameNotFoundException("User not found"));
        return new User(user.getUsername(), user.getPassword(), new ArrayList&lt;&gt;());
    }
}
</code></pre> </li><li> **配置 Spring Security**: 配置 `WebSecurityConfigurerAdapter`，使用自定义的 `UserDetailsService` 和合适的密码编码器。 <pre><code class="prism language-java">import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;

@Autowired
private CustomUserDetailsService userDetailsService;

@Override
protected void configure(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
    auth.userDetailsService(userDetailsService)
        .passwordEncoder(new BCryptPasswordEncoder());
}
</code></pre> </li>1.  **创建登录表单**: 创建一个简单的 HTML 登录表单。 1.  **运行和测试**: 运行应用程序，并通过访问 `http://localhost:8080/login` 来测试登录功能。 
通过这个案例，您可以了解如何结合表单登录和数据库用户存储来实现认证功能。这在实际开发中非常常见，为应用程序提供了更大的灵活性和安全性。

### 1.2.4 拓展案例 2：整合 OAuth2

在这个案例中，我们将演示如何在 Spring Boot 应用中整合 OAuth2，实现第三方登录。我们将以 Google 作为 OAuth2 提供商的例子来实现这一功能。

**案例 Demo**

假设我们有一个 Spring Boot 应用，需要让用户可以通过他们的 Google 账户登录。

**实现步骤**:
<li> **添加 OAuth2 客户端依赖**: 在 `pom.xml` 中添加 `spring-boot-starter-oauth2-client` 依赖。 <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-oauth2-client&lt;/artifactId&gt;
&lt;/dependency&gt;
</code></pre> </li><li> **配置 OAuth2 客户端**: 在 `application.properties` 或 `application.yml` 中配置 Google 的 OAuth2 客户端信息。你需要替换 `client-id` 和 `client-secret` 为你在 Google API Console 中获取的实际值。 <pre><code class="prism language-properties">spring.security.oauth2.client.registration.google.client-id=your-google-client-id
spring.security.oauth2.client.registration.google.client-secret=your-google-client-secret
spring.security.oauth2.client.registration.google.scope=profile,email
</code></pre> </li><li> **安全配置**: 修改你的 `SecurityConfig` 类，以支持 OAuth2 登录。 <pre><code class="prism language-java">import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Override
protected void configure(HttpSecurity http) throws Exception {<!-- -->
    http
        .authorizeRequests()
            .anyRequest().authenticated()
            .and()
        .oauth2Login();
}
</code></pre> 这里我们配置了所有请求都需要认证，并且启用了 OAuth2 登录。 </li><li> **获取用户信息**: 创建一个控制器来处理登录后的用户信息。 <pre><code class="prism language-java">import org.springframework.security.oauth2.client.authentication.OAuth2AuthenticationToken;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class UserController {<!-- -->

    @GetMapping("/user")
    public String user(OAuth2AuthenticationToken token) {<!-- -->
        // 这里可以获取到用户信息
        // token.getPrincipal().getAttributes();
        return "user";
    }
}
</code></pre> </li>1.  **运行和测试**: 启动应用程序，并尝试通过访问 `http://localhost:8080/user` 使用 Google 账户登录。检查用户信息是否正确获取。 
通过这个案例，您可以看到在 Spring Boot 应用中整合 OAuth2 并不复杂。这使得应用可以利用第三方服务提供商的强大认证机制，同时提高了用户体验。

## 1.3 Spring Security 的发展历程

### 1.3.1 基础知识详解

**Spring Security 的演变**
<li> **从 Acegi 到 Spring Security**: 
  1. **Acegi Security**: 最初作为一个独立的安全框架，Acegi Security 为 Spring 应用提供了强大的安全性支持。1. **Spring Security 2.0**: Acegi Security 被正式纳入 Spring 框架，并更名为 Spring Security。这个版本主要专注于简化配置，并引入了新的命名空间和注解驱动的安全配置。 </li><li> **功能增强和改进**: 
  1. **Spring Security 3.0**: 引入了多项新特性，包括对注解的支持，使得开发者可以更灵活地配置安全策略。1. **Spring Security 4.0**: 进一步增强了对 Java 配置的支持，减少了对 XML 的依赖。同时，增强了对 REST API 的安全支持。 </li><li> **适应现代应用的需求**: 
  1. **Spring Security 5.0**: 标志着对现代应用安全的重大更新，包括对 OAuth2 和 OpenID Connect 的支持，以及对 Reactive 应用的安全支持。 </li>- **Spring Security 3.0**: 引入了多项新特性，包括对注解的支持，使得开发者可以更灵活地配置安全策略。- **Spring Security 4.0**: 进一步增强了对 Java 配置的支持，减少了对 XML 的依赖。同时，增强了对 REST API 的安全支持。
**核心特性的演进**
- **认证和授权**: 从基本的表单登录和 HTTP 基本认证到支持 LDAP、OAuth2、OpenID Connect 和 JWT 等多样化认证方式。- **安全性控制的细化**: 引入方法级别的安全控制，允许在不同方法上应用不同的安全策略。- **对 RESTful API 的支持**: 随着 RESTful API 在现代应用中的普及，Spring Security 加强了对无状态 REST API 的安全性支持，例如通过 JWT 实现无状态认证。- **易用性和灵活性**: 通过提供更多的 Java 配置选项，减少了对 XML 的依赖，使得配置更加灵活和易于理解。- **响应式编程的支持**: 为适应 Spring WebFlux 和响应式编程模型的兴起，Spring Security 5 引入了对响应式应用的支持。
通过理解 Spring Security 的发展历程和其核心特性的演进，开发者可以更好地把握其使用方式和最佳实践，从而为应用程序提供强大而灵活的安全解决方案。

### 1.3.2 主要案例：表达式驱动的安全性

在这个案例中，我们将展示如何在 Spring Boot 应用中使用 Spring Security 的表达式驱动安全性，以实现更细粒度的访问控制。

**案例 Demo**

假设我们正在开发一个网上书店应用，需要实现以下安全需求：只有管理员可以添加书籍，而注册用户可以浏览书籍。

**实现步骤**:
1.  **创建 Spring Boot 应用程序**: 使用 Spring Initializr 创建一个新的 Spring Boot 项目，并添加 `spring-boot-starter-web` 和 `spring-boot-starter-security` 依赖。 <li> **配置安全性**: 创建一个继承自 `WebSecurityConfigurerAdapter` 的配置类并开启方法级安全。 <pre><code class="prism language-java">import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->
    // 配置用户认证逻辑
}
</code></pre> </li><li> **设置用户角色和权限**: 在 `configure(AuthenticationManagerBuilder auth)` 方法中设置用户角色和权限。 <pre><code class="prism language-java">@Override
protected void configure(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
    auth.inMemoryAuthentication()
        .withUser("admin").password("{noop}admin123").roles("ADMIN")
        .and()
        .withUser("user").password("{noop}user123").roles("USER");
}
</code></pre> </li><li> **使用安全表达式**: 在你的服务类中使用安全注解来限制方法访问。 <pre><code class="prism language-java">import org.springframework.security.access.prepost.PreAuthorize;

@Service
public class BookService {<!-- -->

    @PreAuthorize("hasRole('ADMIN')")
    public void addBook(Book book) {<!-- -->
        // 逻辑添加书籍
    }

    @PreAuthorize("hasAnyRole('USER', 'ADMIN')")
    public List&lt;Book&gt; listBooks() {<!-- -->
        // 返回书籍列表
    }
}
</code></pre> </li><li> **创建控制器**: 实现一个控制器，调用 `BookService` 的方法。 <pre><code class="prism language-java">@RestController
public class BookController {<!-- -->

    @Autowired
    private BookService bookService;

    @PostMapping("/books")
    public ResponseEntity&lt;String&gt; addBook(@RequestBody Book book) {<!-- -->
        bookService.addBook(book);
        return ResponseEntity.ok("Book added successfully");
    }

    @GetMapping("/books")
    public ResponseEntity&lt;List&lt;Book&gt;&gt; getBooks() {<!-- -->
        return ResponseEntity.ok(bookService.listBooks());
    }
}
</code></pre> </li>1.  **测试安全性**: 运行应用程序，并使用不同角色的用户尝试访问 `/books` 的 GET 和 POST 方法。 
通过这个案例，您可以看到如何在实际项目中使用 Spring Security 的表达式驱动安全性来实现基于角色的细粒度访问控制。这种方法为应用程序提供了强大的安全性和灵活性。

### 1.3.3 拓展案例 1：OAuth2 集成

在这个案例中，我们将展示如何在 Spring Boot 应用中整合 OAuth2，以便用户可以使用外部服务提供商进行认证。我们以集成 GitHub 作为 OAuth2 提供商为例。

**案例 Demo**

假设我们有一个 Spring Boot 应用，我们希望用户能够使用他们的 GitHub 账户登录。

**实现步骤**:
<li> **添加 OAuth2 客户端依赖**: 在 `pom.xml` 中添加 `spring-boot-starter-oauth2-client` 依赖。 <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-oauth2-client&lt;/artifactId&gt;
&lt;/dependency&gt;
</code></pre> </li><li> **配置 OAuth2 客户端**: 在 `application.properties` 或 `application.yml` 中配置 GitHub 的 OAuth2 客户端信息。你需要在 GitHub 创建 OAuth 应用以获取 `client-id` 和 `client-secret`。 <pre><code class="prism language-properties">spring.security.oauth2.client.registration.github.client-id=your-github-client-id
spring.security.oauth2.client.registration.github.client-secret=your-github-client-secret
spring.security.oauth2.client.registration.github.scope=user:email
</code></pre> </li><li> **安全配置**: 修改你的 `SecurityConfig` 类，以支持 OAuth2 登录。 <pre><code class="prism language-java">import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Override
protected void configure(HttpSecurity http) throws Exception {<!-- -->
    http
        .authorizeRequests()
            .anyRequest().authenticated()
            .and()
        .oauth2Login();
}
</code></pre> 这里我们配置了所有请求都需要认证，并且启用了 OAuth2 登录。 </li><li> **创建用户信息端点**: 创建一个控制器来显示登录用户的信息。 <pre><code class="prism language-java">import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {<!-- -->

    @GetMapping("/user")
    public Map&lt;String, Object&gt; user(@AuthenticationPrincipal OAuth2User principal) {<!-- -->
        return Collections.singletonMap("name", principal.getAttribute("name"));
    }
}
</code></pre> </li>1.  **运行和测试**: 启动应用程序，并尝试访问 `http://localhost:8080/user`。你应该能够看到一个重定向到 GitHub 的登录页面。使用你的 GitHub 凭据登录后，应用将显示你的 GitHub 用户名。 
通过这个案例，你可以了解到如何在 Spring Boot 应用中实现 OAuth2 集成，从而允许用户使用外部服务提供商的账户进行认证，这对于提升用户体验和应用安全性都非常有帮助。

### 1.3.4 拓展案例 2：JWT 认证

在这个案例中，我们将演示如何在 Spring Boot 应用中使用 JSON Web Tokens (JWT) 实现无状态认证。这对于保护 REST API 尤其重要。

**案例 Demo**

假设我们正在开发一个提供 REST API 的应用程序，我们希望通过 JWT 来认证和授权用户。

**实现步骤**:
<li> **添加 JWT 依赖**: 在 `pom.xml` 中添加处理 JWT 的依赖库，例如 `java-jwt`。 <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;com.auth0&lt;/groupId&gt;
    &lt;artifactId&gt;java-jwt&lt;/artifactId&gt;
    &lt;version&gt;3.10.3&lt;/version&gt;
&lt;/dependency&gt;
</code></pre> </li><li> **实现 JWT Token 服务**: 创建一个服务类来生成和验证 JWT。 <pre><code class="prism language-java">import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import java.util.Date;

public class JwtTokenService {<!-- -->

    private static final String SECRET = "YourSecretKey";

    public String generateToken(String username) {<!-- -->
        return JWT.create()
                .withSubject(username)
                .withExpiresAt(new Date(System.currentTimeMillis() + 86400000)) // 1 day
                .sign(Algorithm.HMAC256(SECRET));
    }

    public String validateTokenAndGetUsername(String token) {<!-- -->
        return JWT.require(Algorithm.HMAC256(SECRET))
                .build()
                .verify(token)
                .getSubject();
    }
}
</code></pre> </li><li> **创建 JWT 过滤器**: 创建一个 JWT 过滤器来拦截请求并验证 JWT。 <pre><code class="prism language-java">import javax.servlet.FilterChain;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.filter.OncePerRequestFilter;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;

public class JwtFilter extends OncePerRequestFilter {<!-- -->

    private JwtTokenService jwtTokenService = new JwtTokenService();

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) {<!-- -->
        String token = request.getHeader("Authorization");
        if (token != null &amp;&amp; token.startsWith("Bearer ")) {<!-- -->
            token = token.substring(7);
            String username = jwtTokenService.validateTokenAndGetUsername(token);

            if (username != null) {<!-- -->
                UsernamePasswordAuthenticationToken auth = new UsernamePasswordAuthenticationToken(username, null, null);
                SecurityContextHolder.getContext().setAuthentication(auth);
            }
        }
        filterChain.doFilter(request, response);
    }
}
</code></pre> </li><li> **配置 Spring Security**: 在 `WebSecurityConfigurerAdapter` 中配置 JWT 过滤器。 <pre><code class="prism language-java">import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;

@Override
protected void configure(HttpSecurity http) throws Exception {<!-- -->
    http
        .csrf().disable()
        .sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS)
        .and()
        .addFilter(new JwtFilter())
        .authorizeRequests()
        .antMatchers("/api/protected").authenticated()
        .antMatchers("/api/public").permitAll();
}
</code></pre> </li><li> **创建测试端点**: 创建一些测试用的 RESTful 端点。 <pre><code class="prism language-java">import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {<!-- -->

    @GetMapping("/api/protected")
    public String protectedHello() {<!-- -->
        return "Hello from protected API";
    }

    @GetMapping("/api/public")
    public String publicHello() {<!-- -->
        return "Hello from public API";
    }
}
</code></pre> </li>1.  **运行和测试**: 启动应用程序，并使用生成的 JWT 尝试访问 `/api/protected`。没有有效 JWT 的请求应该被拒绝。 
通过这个案例，您可以看到如何在 Spring Boot 应用中实现基于 JWT 的认证。JWT 认证提供了一种有效的方式来保护 REST API，确保只有拥有有效令牌的用户才能访问受保护的资源。
