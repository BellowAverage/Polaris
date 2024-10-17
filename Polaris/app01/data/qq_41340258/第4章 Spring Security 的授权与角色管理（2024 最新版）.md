
--- 
title:  第4章 Spring Security 的授权与角色管理（2024 最新版） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/be731c10fa4546128c92622d855a4259.png#pic_center" alt="在这里插入图片描述">



#### 文章目录
- - <ul><li>- <ul><li>- - - - - - - - - - - <ul><li>- - - - - - - <ul><li>- - - - - - - - - 


## 4.1 理解授权

欢迎进入授权的迷人世界，这里我们将学习如何在 Spring Security 中精细控制谁可以做什么。想象一下，我们的应用是一个大型的音乐节，授权就是确保每个人都在正确的舞台前摇摆！

### 4.1.1 基础知识详解

#### 授权的核心

授权，简而言之，就是确定一个已认证的用户（即已经通过登录过程的用户）是否拥有执行某项操作的权限。这涉及到两个层面的判断：角色（Role）和权限（Authority）。
- **角色 (Role)**: 角色通常表示用户的分组，每个角色拥有一组权限。例如，"管理员"角色可能有权限修改所有用户的数据，而"普通用户"角色可能只能修改自己的数据。- **权限 (Authority)**: 权限是更细粒度的访问控制，它定义了用户可以执行的具体操作，如"读取文件"、"写入数据"等。
#### 授权策略

Spring Security 提供了多种授权策略，允许开发者根据具体需求来定制访问控制规则：
- **基于 URL 的授权**: 通过配置特定的 URL 模式与所需的角色或权限相关联，来控制对这些 URL 的访问。- **方法级的授权**: 使用注解（如 `@PreAuthorize`、`@Secured`）直接在业务方法上定义访问控制规则，为细粒度的控制提供了便利。
#### 方法级安全

Spring Security 的方法级安全功能是通过 AOP（面向切面编程）实现的，它允许你在不修改业务逻辑代码的情况下，添加额外的安全检查。这种方式非常灵活，可以应用于任何 Spring 管理的 Bean 的方法上。
- **启用方法级安全**: 通过在配置类上使用 `@EnableGlobalMethodSecurity` 注解并设置相应的属性（如 `prePostEnabled`、`securedEnabled`）来启用。- **安全注解**: `@PreAuthorize`、`@PostAuthorize`、`@Secured` 和 `@RolesAllowed` 等注解提供了丰富的选项，用于定义方法的访问控制规则。
#### 动态权限检查

在某些情况下，静态定义的角色或权限可能不足以满足复杂的业务需求。Spring Security 支持动态权限检查，允许在运行时根据具体情况决定是否授权。
- **表达式驱动的访问控制**: `@PreAuthorize` 和 `@PostAuthorize` 注解支持 SpEL（Spring 表达式语言），使得可以在表达式中引用方法参数、调用方法等，实现动态的权限判断。
通过精细地配置和使用 Spring Security 的授权机制，开发者可以为应用构建起一道坚固的安全防线，确保只有拥有适当权限的用户才能访问敏感资源或执行特定操作。这不仅提高了应用的安全性，也为维护良好的用户体验提供了支持。

### 4.1.2 主要案例：基于角色的页面访问控制

在这个案例中，我们将通过一个实际的示例来演示如何在 Spring Security 中实现基于角色的页面访问控制。这将确保只有具备特定角色的用户能访问相应的页面或执行特定的操作，从而提高应用的安全性。

#### 案例 Demo

假设我们的应用有三个主要区域：首页（公开访问）、用户仪表板（仅限登录用户访问）、管理员控制台（仅限管理员访问）。

**步骤 1**: 定义角色

在这个场景中，我们定义两个角色：`ROLE_USER` 和 `ROLE_ADMIN`。

**步骤 2**: 配置 Spring Security

创建一个名为 `WebSecurityConfig` 的安全配置类，继承 `WebSecurityConfigurerAdapter` 并重写相应的方法来配置安全策略。

```
@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .csrf().disable() // 示例中禁用CSRF保护，实际应用中应根据需要启用
            .authorizeRequests()
                .antMatchers("/").permitAll() // 首页允许所有人访问
                .antMatchers("/user/**").hasRole("USER") // 用户仪表板仅限拥有 ROLE_USER 的用户访问
                .antMatchers("/admin/**").hasRole("ADMIN") // 管理员控制台仅限拥有 ROLE_ADMIN 的用户访问
                .anyRequest().authenticated()
                .and()
            .formLogin()
                .loginPage("/login")
                .permitAll() // 提供自定义登录页面
                .and()
            .logout()
                .permitAll(); // 允许所有用户登出
    }

    @Bean
    @Override
    public UserDetailsService userDetailsService() {<!-- -->
        // 在内存中配置一些用户
        InMemoryUserDetailsManager manager = new InMemoryUserDetailsManager();
        manager.createUser(User.withUsername("user").password(passwordEncoder().encode("password")).roles("USER").build());
        manager.createUser(User.withUsername("admin").password(passwordEncoder().encode("password")).roles("ADMIN").build());
        return manager;
    }

    @Bean
    public PasswordEncoder passwordEncoder() {<!-- -->
        // 使用 BCryptPasswordEncoder 对密码进行编码
        return new BCryptPasswordEncoder();
    }
}

```

**步骤 3**: 测试访问控制

启动应用，并尝试访问不同区域：
- 访问 `/` 应该对所有人开放。- 访问 `/user/dashboard` 时，如果未登录或不具备 `ROLE_USER` 角色，应重定向到登录页面。- 访问 `/admin/control` 时，仅当用户拥有 `ROLE_ADMIN` 角色时才能访问，否则应拒绝访问。
### 4.1.3 拓展案例 1：自定义投票策略

在更复杂的安全需求中，简单的角色检查可能不足以满足需求，这时可以通过自定义投票策略来进行细粒度的控制。Spring Security 提供了一个灵活的访问决策管理器（`AccessDecisionManager`），它可以根据多个投票器（`AccessDecisionVoter`）的投票结果来决定是否授予访问权限。

#### 案例 Demo

假设我们有一个需求，只允许在特定时间段内访问某些资源。我们可以通过实现一个自定义的投票器来实现这一需求。

**步骤 1**: 创建自定义投票器

首先，我们创建一个自定义投票器 `TimeBasedAccessDecisionVoter`，它将根据当前时间和预定义的时间段来决定是否投票赞成访问。

```
import org.springframework.security.access.AccessDecisionVoter;
import org.springframework.security.access.ConfigAttribute;
import org.springframework.security.core.Authentication;
import org.springframework.security.web.FilterInvocation;

import java.time.LocalTime;
import java.util.Collection;

public class TimeBasedAccessDecisionVoter implements AccessDecisionVoter&lt;FilterInvocation&gt; {<!-- -->

    private final LocalTime allowedStartTime;
    private final LocalTime allowedEndTime;

    public TimeBasedAccessDecisionVoter(String startTime, String endTime) {<!-- -->
        this.allowedStartTime = LocalTime.parse(startTime);
        this.allowedEndTime = LocalTime.parse(endTime);
    }

    @Override
    public int vote(Authentication authentication, FilterInvocation fi, Collection&lt;ConfigAttribute&gt; attributes) {<!-- -->
        LocalTime now = LocalTime.now();
        if (now.isAfter(allowedStartTime) &amp;&amp; now.isBefore(allowedEndTime)) {<!-- -->
            return ACCESS_GRANTED;
        } else {<!-- -->
            return ACCESS_DENIED;
        }
    }

    @Override
    public boolean supports(ConfigAttribute attribute) {<!-- -->
        return true;
    }

    @Override
    public boolean supports(Class&lt;?&gt; clazz) {<!-- -->
        return FilterInvocation.class.isAssignableFrom(clazz);
    }
}

```

**步骤 2**: 配置访问决策管理器

接下来，在安全配置类中配置自定义的访问决策管理器，将我们的自定义投票器添加到其中。

```
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.annotation.web.configurers.ExpressionUrlAuthorizationConfigurer;
import org.springframework.security.access.vote.AffirmativeBased;
import org.springframework.security.access.vote.ConsensusBased;
import org.springframework.security.access.vote.UnanimousBased;
import java.util.List;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http.authorizeRequests()
            .anyRequest().authenticated()
            .accessDecisionManager(accessDecisionManager());
    }

    public AccessDecisionManager accessDecisionManager() {<!-- -->
        List&lt;AccessDecisionVoter&lt;?&gt;&gt; decisionVoters = List.of(
                new TimeBasedAccessDecisionVoter("09:00", "17:00")
        );
        return new AffirmativeBased(decisionVoters); // 使用肯定性决策策略
    }
}

```

这里，我们使用 `AffirmativeBased` 访问决策管理器，并添加了我们的 `TimeBasedAccessDecisionVoter` 作为投票器。这意味着，如果自定义投票器投票赞成，则允许访问；否则，拒绝访问。

#### 测试自定义投票策略

启动应用并尝试在不同时间访问受保护的资源。你会发现，只有在定义的时间段内（例如上午 9:00 至下午 5:00），请求才会被允许；其他时间则会被拒绝。

通过实现这个案例，你就学会了如何使用 Spring Security 的高级特性来满足特定的安全需求，提供了一种灵活而强大的方法来根据应用的具体需求定制访问控制策略。

### 4.1.4 拓展案例 2：使用方法级安全进行细粒度控制

方法级安全是 Spring Security 提供的一个强大功能，它允许开发者在单个方法上应用安全注解，从而实现细粒度的访问控制。这种方式非常适用于那些需要根据不同业务逻辑对访问权限进行精细管理的应用。

#### 案例 Demo

假设我们正在开发一个博客系统，其中包含一个文章服务，我们希望只有文章的作者或者管理员才能编辑文章。

**步骤 1**: 启用方法级安全

首先，在你的安全配置类上添加 `@EnableGlobalMethodSecurity` 注解，并设置 `prePostEnabled` 为 `true`，以启用方法级安全。

```
@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class MethodSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->
    // 安全配置内容
}

```

**步骤 2**: 创建文章服务

接下来，创建一个文章服务 `ArticleService`，并在编辑文章的方法上使用 `@PreAuthorize` 注解来定义访问控制规则。

```
@Service
public class ArticleService {<!-- -->

    @PreAuthorize("hasRole('ADMIN') or #article.author.username == authentication.principal.username")
    public void editArticle(Article article) {<!-- -->
        // 编辑文章的逻辑
    }
}

```

在这个例子中，`#article.author.username` 引用了方法参数 `article` 中作者用户名的属性，而 `authentication.principal.username` 引用了当前认证用户的用户名。这条规则的含义是：“只有当当前用户是管理员，或者文章的作者时，才允许编辑文章。”

#### 动态权限验证

假设系统中还有一个需求，即用户可以对文章进行评论，但我们希望在用户被禁言时禁止其评论。

**步骤 1**: 实现用户服务

假设我们有一个 `UserService`，它提供了方法来检查用户是否被禁言。

```
@Service
public class UserService {<!-- -->

    public boolean isUserBanned(String username) {<!-- -->
        // 检查用户是否被禁言的逻辑
        return true; // 假设返回结果
    }
}

```

**步骤 2**: 使用 SpEL 进行动态验证

在评论服务的添加评论方法上使用 `@PreAuthorize`，结合 SpEL 表达式和自定义方法来实现动态权限验证。

```
@Service
public class CommentService {<!-- -->

    @Autowired
    private UserService userService;

    @PreAuthorize("!@userService.isUserBanned(authentication.principal.username)")
    public void addComment(Comment comment) {<!-- -->
        // 添加评论的逻辑
    }
}

```

这里，`@userService.isUserBanned(authentication.principal.username)` 调用了 `UserService` 的 `isUserBanned` 方法来检查当前认证用户是否被禁言，从而动态决定是否允许用户添加评论。

通过在方法上应用安全注解，你可以根据业务逻辑的需要实现复杂的访问控制策略。这种灵活性是 Spring Security 方法级安全特别强大的地方，使得开发者可以轻松应对各种复杂的安全需求。

## 4.2 角色与权限的配置

在 Spring Security 中，角色和权限的概念是实现细粒度访问控制的关键。通过合理配置角色和权限，你可以精确地控制谁可以访问应用中的哪些资源。

### 4.2.1 基础知识详解
<li> **角色 (Roles)**: 
  1. 角色通常用来表示用户的分组，它是一种高级别的权限集合，可以简化权限管理。1. 在 Spring Security 中，角色通常以 `ROLE_` 前缀命名，例如 `ROLE_ADMIN`，`ROLE_USER` 等。1. 角色使得可以通过一次检查来控制对多个资源的访问权限。 </li><li> **权限 (Authorities)**: 
  1. 权限代表对特定行为的访问控制，它是更细粒度的访问权限。1. 权限不一定以 `ROLE_` 前缀命名，可以是任何字符串，如 `READ_PRIVILEGES`，`WRITE_PRIVILEGES` 等。1. 权限允许对用户可以执行的操作进行精确控制。 </li><li> **角色与权限的关系**: 
  1. 一个角色可以包含多个权限，而一个用户可以拥有多个角色。1. 角色和权限共同工作，提供了一种灵活而强大的方式来定义安全策略，确保只有合适的用户能访问应用中的资源。 </li><li> **配置方式**: 
  1. **内存中的配置**：适用于简单应用或开发测试阶段。通过 `AuthenticationManagerBuilder` 直接在安全配置中指定角色和用户。1. **数据库配置**：适用于需要动态管理用户、角色和权限的生产环境。通常结合 `UserDetailsService` 和 `JdbcUserDetailsManager` 或自定义实现来完成。 </li><li> **方法级安全**: 
  1. Spring Security 支持在方法级别进行安全控制，允许在业务逻辑方法上直接声明访问控制规则。1. 使用 `@PreAuthorize`、`@PostAuthorize`、`@Secured` 和 `@RolesAllowed` 等注解，可以基于表达式或直接基于角色进行方法访问控制。1. 方法级安全提供了比URL级安全更细粒度的控制，特别适用于复杂业务逻辑的安全需求。 </li>- 权限代表对特定行为的访问控制，它是更细粒度的访问权限。- 权限不一定以 `ROLE_` 前缀命名，可以是任何字符串，如 `READ_PRIVILEGES`，`WRITE_PRIVILEGES` 等。- 权限允许对用户可以执行的操作进行精确控制。- **内存中的配置**：适用于简单应用或开发测试阶段。通过 `AuthenticationManagerBuilder` 直接在安全配置中指定角色和用户。- **数据库配置**：适用于需要动态管理用户、角色和权限的生产环境。通常结合 `UserDetailsService` 和 `JdbcUserDetailsManager` 或自定义实现来完成。
通过掌握角色和权限的基础知识以及它们在 Spring Security 中的应用方式，开发者可以为应用构建起一套既强大又灵活的安全策略，有效地保护应用资源，确保只有授权用户才能访问敏感信息或执行关键操作。

### 4.2.2 主要案例：配置内存中的用户、角色和权限

在这个案例中，我们将通过一个实际的示例来演示如何在 Spring Security 中使用内存配置来定义用户、角色和权限。这种方式非常适合于简单的应用或是在开发和测试阶段快速搭建安全框架。

#### 案例 Demo

假设我们正在开发一个小型的博客系统，其中包含三类用户：管理员（`ADMIN`）、作者（`AUTHOR`）和访客（`VISITOR`）。每种用户类型都有不同的权限集合。

**步骤 1**: 创建安全配置类

首先，创建一个名为 `WebSecurityConfig` 的安全配置类，继承 `WebSecurityConfigurerAdapter` 并重写 `configure(AuthenticationManagerBuilder auth)` 方法来配置用户、角色和权限。

```
@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
        auth.inMemoryAuthentication()
            .passwordEncoder(NoOpPasswordEncoder.getInstance())
            .withUser("admin").password("adminPass").roles("ADMIN")
            .and()
            .withUser("author").password("authorPass").authorities("ROLE_AUTHOR", "CREATE_POST", "EDIT_POST")
            .and()
            .withUser("visitor").password("visitorPass").roles("VISITOR");
    }
}

```

在这个配置中，我们使用了 `NoOpPasswordEncoder` 为了简化示例，实际应用中推荐使用 `BCryptPasswordEncoder`。

**步骤 2**: 定义访问控制规则

继续在 `WebSecurityConfig` 中，重写 `configure(HttpSecurity http)` 方法来定义各种URL路径的访问控制规则。

```
@Override
protected void configure(HttpSecurity http) throws Exception {<!-- -->
    http
        .authorizeRequests()
        .antMatchers("/").permitAll() // 首页允许所有人访问
        .antMatchers("/admin/**").hasRole("ADMIN") // 管理员界面仅管理员可访问
        .antMatchers("/blog/new", "/blog/edit/*").hasAuthority("CREATE_POST") // 博客创建和编辑仅作者可访问
        .anyRequest().authenticated() // 其他所有请求都需要认证
        .and()
        .formLogin() // 启用默认登录页面
        .and()
        .logout(); // 启用默认登出功能
}

```

#### 动态角色和权限的数据库配置

在生产环境中，通常需要从数据库动态加载用户、角色和权限信息，以便于管理。你可以通过实现 `UserDetailsService` 接口并使用 JPA 或 MyBatis 等ORM框架从数据库加载用户信息。

#### 基于表达式的访问控制

Spring Security 支持基于表达式的访问控制（SpEL），这为定义复杂的访问控制逻辑提供了强大的灵活性。

```
http
    .authorizeRequests()
    .antMatchers("/blog/**").access("hasRole('ROLE_AUTHOR') or hasRole('ROLE_ADMIN')")
    .anyRequest().authenticated();

```

通过实现这个案例，你可以看到如何在 Spring Security 中配置内存中的用户、角色和权限。这种方法虽然简单，但能够为你的应用提供一个快速而安全的认证和授权机制。在实际生产环境中，你可能会需要使用数据库来存储这些信息，以支持动态的权限管理和更细粒度的访问控制。

### 4.2.3 拓展案例 1：动态角色和权限的数据库配置

在实际生产环境中，角色和权限的配置通常需要更加灵活和动态，以便于管理和扩展。通过数据库配置用户、角色和权限信息，可以实现这一目标。以下是如何在 Spring Security 中实现动态角色和权限配置的示例。

#### 案例 Demo

假设我们有一个博客系统，其中用户信息、角色和权限都存储在数据库中。

**步骤 1**: 创建数据库模型

首先，我们需要在数据库中创建用户（`User`）、角色（`Role`）和权限（`Permission`）的模型。以下是一个简化的模型示例：

```
CREATE TABLE `users` (
  `id` BIGINT AUTO_INCREMENT PRIMARY KEY,
  `username` VARCHAR(50) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `enabled` BOOLEAN NOT NULL
);

CREATE TABLE `roles` (
  `id` BIGINT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(50) NOT NULL
);

CREATE TABLE `user_roles` (
  `user_id` BIGINT NOT NULL,
  `role_id` BIGINT NOT NULL,
  PRIMARY KEY (`user_id`, `role_id`),
  FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
);

CREATE TABLE `permissions` (
  `id` BIGINT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(50) NOT NULL
);

CREATE TABLE `role_permissions` (
  `role_id` BIGINT NOT NULL,
  `permission_id` BIGINT NOT NULL,
  PRIMARY KEY (`role_id`, `permission_id`),
  FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`),
  FOREIGN KEY (`permission_id`) REFERENCES `permissions` (`id`)
);

```

**步骤 2**: 实现 `UserDetailsService`

接下来，我们需要实现 `UserDetailsService` 接口，以从数据库加载用户信息及其角色和权限。

```
@Service
public class CustomUserDetailsService implements UserDetailsService {<!-- -->

    @Autowired
    private UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {<!-- -->
        User user = userRepository.findByUsername(username)
                .orElseThrow(() -&gt; new UsernameNotFoundException("User not found: " + username));

        Set&lt;GrantedAuthority&gt; authorities = new HashSet&lt;&gt;();
        user.getRoles().forEach(role -&gt; {<!-- -->
            authorities.add(new SimpleGrantedAuthority(role.getName()));
            role.getPermissions().forEach(permission -&gt; authorities.add(new SimpleGrantedAuthority(permission.getName())));
        });

        return new org.springframework.security.core.userdetails.User(user.getUsername(), user.getPassword(), authorities);
    }
}

```

**步骤 3**: 配置 `WebSecurityConfig`

在安全配置类中使用自定义的 `UserDetailsService` 和合适的密码编码器。

```
@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Autowired
    private CustomUserDetailsService customUserDetailsService;

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
        auth.userDetailsService(customUserDetailsService)
            .passwordEncoder(passwordEncoder());
    }

    @Bean
    public PasswordEncoder passwordEncoder() {<!-- -->
        return new BCryptPasswordEncoder();
    }

    // 其他配置...
}

```

**步骤 4**: 测试动态角色和权限

启动应用，并测试不同角色的用户访问受限资源，验证动态角色和权限配置是否生效。

通过实现这个案例，你就可以在 Spring Security 中实现动态的角色和权限管理。这种方式为应用提供了更大的灵活性和扩展性，使得管理用户访问权限变得更加简单和高效。

### 4.2.4 拓展案例 2：使用方法级安全进行角色和权限控制

当你需要在更细粒度的级别上控制访问权限时，方法级安全是一个强大的工具。Spring Security 通过注解提供了这种控制能力，允许你直接在服务或控制器层的方法上定义访问策略。

#### 案例 Demo

假设我们的博客系统需要对不同的操作定义详细的访问控制策略，例如只允许文章的作者或管理员编辑文章，而访客只能阅读文章。

**步骤 1**: 启用方法级安全

首先，确保你的安全配置类启用了方法级安全。通过在配置类上添加 `@EnableGlobalMethodSecurity` 注解，并设置 `prePostEnabled` 为 `true`。

```
@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class MethodSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->
    // 安全配置内容
}

```

**步骤 2**: 定义角色和权限

在这个示例中，我们假设已经通过某种方式（例如，动态角色和权限的数据库配置案例）定义了用户的角色和权限。

**步骤 3**: 应用方法级安全注解

在服务类中，我们可以使用 `@PreAuthorize` 或 `@PostAuthorize` 注解来定义访问控制策略。

```
@Service
public class BlogService {<!-- -->

    // 只有作者或管理员可以编辑文章
    @PreAuthorize("hasRole('ROLE_ADMIN') or (hasRole('ROLE_AUTHOR') and #article.author == authentication.name)")
    public void editArticle(Article article) {<!-- -->
        // 编辑文章的逻辑
    }

    // 所有人都可以阅读文章
    @PreAuthorize("permitAll()")
    public Article readArticle(Long articleId) {<!-- -->
        // 读取文章的逻辑
        return new Article();
    }
}

```

在 `editArticle` 方法上的 `@PreAuthorize` 注解确保只有文章的作者或者拥有管理员角色的用户可以编辑文章。这里使用了 Spring 表达式语言（SpEL）来访问方法参数 `article` 和当前认证用户的名称。

**步骤 4**: 测试方法级安全控制

启动应用，并尝试以不同角色的用户执行上述定义的操作。你应该会看到只有符合条件的用户才能成功执行 `editArticle` 方法，而 `readArticle` 方法对所有人开放。

#### 使用自定义方法进行安全检查

有时候，你可能需要根据复杂的业务逻辑进行安全检查，这时可以定义自定义方法来辅助安全注解。

**步骤 1**: 创建一个辅助服务

```
@Service
public class SecurityService {<!-- -->

    public boolean isArticleOwner(Long articleId, String username) {<!-- -->
        // 检查指定的用户名是否为文章的所有者
        // 此处省略具体实现
        return true;
    }
}

```

**步骤 2**: 在方法级安全注解中调用自定义方法

```
@Service
public class BlogService {<!-- -->

    @Autowired
    private SecurityService securityService;

    @PreAuthorize("@securityService.isArticleOwner(#articleId, authentication.name)")
    public void editArticle(Long articleId) {<!-- -->
        // 编辑文章的逻辑
    }
}

```

在这个例子中，我们通过调用 `SecurityService` 中的 `isArticleOwner` 方法来动态地检查当前用户是否有权限编辑文章。

通过使用方法级安全控制，你可以在 Spring Security 中实现复杂和细粒度的访问控制策略，确保应用的安全性同时满足业务需求。

## 4.3 方法级安全性

在 Spring Security 中，方法级安全性是一个强大的特性，允许开发者在单个方法上应用安全策略。这种方式提供了比URL级别更细粒度的控制，非常适合那些需要根据不同业务逻辑或数据敏感性来调整访问权限的场景。

### 4.3.1 基础知识详解

#### 方法级安全的关键概念
1.  **@EnableGlobalMethodSecurity**: 这个注解用于在配置类上启用方法级安全设置。它允许开发者启用和配置不同类型的方法级安全注解支持，包括 `prePostEnabled`、`securedEnabled` 和 `jsr250Enabled` 三个参数。 1.  **@PreAuthorize 和 @PostAuthorize**: 这两个注解允许在方法执行之前或之后进行权限验证。`@PreAuthorize` 可以根据表达式的评估结果来决定是否执行方法，而 `@PostAuthorize` 允许根据方法的执行结果来进行安全检查。 1.  **@Secured**: 这个注解用于指定一个方法只能被拥有特定角色的用户访问。它是一种相对简单直接的访问控制形式，不支持SpEL表达式。 1.  **@RolesAllowed**: 类似于 `@Secured`，这个注解来源于JSR-250标准，用于指定执行方法所需的角色列表。 
#### 方法级安全的配置

启用方法级安全需要在配置类中使用 `@EnableGlobalMethodSecurity` 注解，并根据需求设置其参数。
- **prePostEnabled**: 设置为 `true` 以启用 `@PreAuthorize` 和 `@PostAuthorize` 注解。- **securedEnabled**: 设置为 `true` 以启用 `@Secured` 注解。- **jsr250Enabled**: 设置为 `true` 以启用 `@RolesAllowed` 注解。
#### 使用表达式进行权限控制

Spring Security 的方法级安全支持使用Spring表达式语言（SpEL）进行复杂的权限控制。这种方式提供了极高的灵活性，允许开发者在注解中引用bean、方法参数、认证对象等，以实现精细化的访问控制策略。

例如，使用 `@PreAuthorize` 来检查认证用户的角色或调用方法参数的属性：

```
@PreAuthorize("hasRole('ROLE_ADMIN') or #model.createdBy == authentication.name")
public void performSensitiveOperation(Model model) {<!-- -->
    // 方法体...
}

```

这段代码表示只有管理员角色的用户或者模型的创建者本人才能执行该操作。

通过掌握这些基础知识，开发者可以利用Spring Security在应用中实现高度定制化的安全策略，确保敏感操作只能由合适的角色或用户执行。这不仅加强了应用的安全性，也提供了一种灵活且强大的方式来满足复杂的业务需求。

### 4.3.2 主要案例：使用 `@PreAuthorize` 控制方法访问

在这个案例中，我们将演示如何使用 `@PreAuthorize` 注解来实现方法级别的访问控制。假设我们正在开发一个在线图书馆系统，其中包含一个功能允许用户借阅图书。我们希望只有拥有 `ROLE_USER` 角色并且账户状态为激活状态的用户才能借阅图书。

#### 案例 Demo

**步骤 1**: 启用方法级安全

首先，在安全配置类中启用方法级安全，允许使用 `@PreAuthorize` 注解。

```
@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->
    // 安全配置内容
}

```

**步骤 2**: 创建用户服务

接下来，假设我们有一个用户服务，其中包含用户的角色和状态信息。为了简化，我们在这里不展示用户服务的实现细节。

**步骤 3**: 定义借阅图书的方法

在图书服务类中，我们定义一个方法 `borrowBook`，使用 `@PreAuthorize` 注解来限制只有角色为 `ROLE_USER` 且账户状态为激活的用户才能执行该方法。

```
@Service
public class BookService {<!-- -->

    @PreAuthorize("hasRole('ROLE_USER') and @userService.isAccountActive(authentication.principal.username)")
    public void borrowBook(Long bookId) {<!-- -->
        // 借阅图书的逻辑...
        System.out.println("Book borrowed successfully.");
    }
}

```

在这个例子中，`@userService.isAccountActive(authentication.principal.username)` 调用了自定义的 `UserService` 中的 `isAccountActive` 方法来检查当前认证用户的账户是否激活。这里使用了 SpEL 表达式中的 `@` 符号来引用 Spring 管理的 Bean。

**步骤 4**: 测试方法访问控制

启动应用，并以不同的用户身份尝试借阅图书。你应该会发现只有符合条件（即角色为 `ROLE_USER` 且账户为激活状态）的用户才能成功执行 `borrowBook` 方法。

#### 基于参数的动态权限验证

在一些场景下，你可能需要根据方法参数来动态决定访问权限。例如，只允许用户编辑他们自己的文章。

```
@Service
public class ArticleService {<!-- -->

    @PreAuthorize("#article.author.username == authentication.principal.username")
    public void editArticle(Article article) {<!-- -->
        // 编辑文章的逻辑...
    }
}

```

#### 结合自定义方法进行复杂权限验证

有时候，权限验证逻辑可能非常复杂，需要结合多个条件进行判断。这时，可以定义自定义方法来辅助权限验证。

```
@Service
public class SecurityService {<!-- -->

    public boolean checkAccess(Long articleId, String username) {<!-- -->
        // 复杂的权限验证逻辑...
        return true; // 假设返回结果
    }
}

@Service
public class ArticleService {<!-- -->

    @Autowired
    private SecurityService securityService;

    @PreAuthorize("@securityService.checkAccess(#articleId, authentication.principal.username)")
    public void updateArticle(Long articleId, Article article) {<!-- -->
        // 更新文章的逻辑...
    }
}

```

通过这个案例和其拓展，你可以看到 `@PreAuthorize` 注解如何为 Spring Security 应用提供强大而灵活的方法级访问控制能力，使得开发者能够根据具体的业务需求定制复杂的安全策略。

### 4.3.3 拓展案例 1：使用自定义权限验证

在复杂的应用场景中，可能需要根据业务逻辑进行详细的权限验证。Spring Security 允许开发者定义自定义权限验证方法，这为实现复杂的安全需求提供了极大的灵活性。

#### 案例 Demo

假设我们正在开发一个社交媒体平台，我们需要确保用户只能删除自己的帖子。为此，我们将实现一个自定义权限验证逻辑，以检查当前认证用户是否为帖子的所有者。

**步骤 1**: 创建帖子服务

首先，假设我们有一个 `PostService` 类，其中包含了帖子的各种操作，包括删除帖子的方法。

```
@Service
public class PostService {<!-- -->

    // 假设有一个方法用于检查帖子所有者
    public boolean isOwner(Long postId, String username) {<!-- -->
        // 这里应该包含实际的业务逻辑来验证用户是否为帖子的所有者
        // 为了简化，这里直接返回true
        return true;
    }

    // 删除帖子的方法
    public void deletePost(Long postId) {<!-- -->
        // 删除帖子的逻辑...
        System.out.println("Post deleted successfully.");
    }
}

```

**步骤 2**: 应用自定义权限验证

接下来，我们将在 `PostService` 的 `deletePost` 方法上应用自定义权限验证，以确保只有帖子的所有者才能删除帖子。

```
@Service
public class PostService {<!-- -->

    @Autowired
    private SecurityService securityService;

    @PreAuthorize("@securityService.isOwner(#postId, authentication.principal.username)")
    public void deletePost(Long postId) {<!-- -->
        // 删除帖子的逻辑...
    }
}

```

在这个例子中，`@PreAuthorize` 注解使用了 SpEL 表达式来引用 `SecurityService` 中的 `isOwner` 方法，并传入了帖子ID和当前认证用户的用户名作为参数，以验证当前用户是否有权删除该帖子。

**步骤 3**: 测试自定义权限验证

启动应用，并以不同用户身份尝试删除帖子。只有当用户为帖子的所有者时，删除操作才应该成功执行。

#### 结合数据库进行权限验证

在更复杂的场景中，可能需要根据数据库中的信息来进行权限验证。例如，验证用户是否有权访问某个特定的资源。

**步骤 1**: 创建权限验证服务

假设我们有一个 `PermissionService`，它可以根据用户和资源ID来检查用户是否具有访问权限。

```
@Service
public class PermissionService {<!-- -->

    public boolean hasPermission(String username, Long resourceId) {<!-- -->
        // 实现根据数据库信息检查用户是否有权访问资源的逻辑
        // 为了简化，这里直接返回true
        return true;
    }
}

```

**步骤 2**: 应用数据库权限验证

在需要进行权限验证的方法上使用 `@PreAuthorize` 注解，并调用 `PermissionService` 的方法来实现基于数据库的权限验证。

```
@Service
public class ResourceService {<!-- -->

    @Autowired
    private PermissionService permissionService;

    @PreAuthorize("@permissionService.hasPermission(authentication.principal.username, #resourceId)")
    public void accessResource(Long resourceId) {<!-- -->
        // 访问资源的逻辑...
    }
}

```

通过实现这些案例，你可以看到如何利用 Spring Security 提供的方法级安全特性和 SpEL 表达式，结合自定义逻辑和数据库信息来实现复杂的权限验证需求，从而为应用提供强大而灵活的安全保护。

### 4.3.4 拓展案例 2：基于返回值的后置授权

后置授权是一种在方法执行后基于其返回值来做出授权决策的机制。这种方式在需要根据操作结果来决定是否授权访问时非常有用，例如，只允许用户查看或修改他们自己创建的资源。

#### 案例 Demo

假设我们正在开发一个任务管理应用，其中包含一个功能允许用户查看任务详情。我们希望确保用户只能查看他们自己创建的任务。

**步骤 1**: 创建任务实体和服务

首先，假设我们有一个 `Task` 实体，其中包含了任务的创建者信息。同时，我们有一个 `TaskService` 类，其中包含了获取任务详情的方法。

```
public class Task {<!-- -->
    private Long id;
    private String title;
    private String creator; // 创建者的用户名

    // 构造器、getter和setter省略
}

@Service
public class TaskService {<!-- -->

    public Task getTaskDetails(Long taskId) {<!-- -->
        // 获取任务详情的逻辑，这里简化为直接返回一个示例任务
        return new Task(taskId, "Example Task", "user1");
    }
}

```

**步骤 2**: 应用后置授权

在 `TaskService` 的 `getTaskDetails` 方法上使用 `@PostAuthorize` 注解来实现后置授权。这里我们根据返回的任务对象的创建者与当前认证用户的用户名进行比较，以确定是否允许访问。

```
@Service
public class TaskService {<!-- -->

    @PostAuthorize("returnObject.creator == authentication.name")
    public Task getTaskDetails(Long taskId) {<!-- -->
        // 获取任务详情的逻辑
        return new Task(taskId, "Example Task", "user1");
    }
}

```

**步骤 3**: 测试后置授权

启动应用，并以不同用户身份尝试获取任务详情。你会发现只有任务的创建者能够成功获取到任务详情，其他用户尝试访问时将会因为授权失败而被拒绝。

#### 自定义后置处理逻辑

在某些情况下，你可能需要执行更复杂的后置处理逻辑，这时可以结合 `@PostAuthorize` 注解和自定义方法来实现。

**步骤 1**: 创建自定义后置处理服务

假设我们有一个 `SecurityService`，它提供了自定义的后置处理逻辑。

```
@Service
public class SecurityService {<!-- -->

    public boolean customPostAuthorizeLogic(Task task) {<!-- -->
        // 实现自定义的后置处理逻辑，例如根据任务的某些属性进行复杂的校验
        // 为了简化，这里直接返回true
        return true;
    }
}

```

**步骤 2**: 结合自定义后置处理逻辑应用后置授权

在需要进行后置授权的方法上，结合 `@PostAuthorize` 注解和自定义的后置处理逻辑。

```
@Service
public class TaskService {<!-- -->

    @Autowired
    private SecurityService securityService;

    @PostAuthorize("@securityService.customPostAuthorizeLogic(returnObject)")
    public Task getTaskDetails(Long taskId) {<!-- -->
        // 获取任务详情的逻辑
        return new Task(taskId, "Example Task", "user1");
    }
}

```

通过使用基于返回值的后置授权和自定义后置处理逻辑，你可以实现复杂的安全需求，确保应用中的敏感操作和数据只对授权用户开放，从而提高应用的安全性。
