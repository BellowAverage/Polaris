
--- 
title:  Spring security讲解 
tags: []
categories: [] 

---
## 开心一刻

>  
 为什么程序员总是在深夜工作？因为他们喜欢在黑暗中敲打键盘。 


>  
 为什么程序员不喜欢走路？因为他们喜欢走“for”循环。 


## 简介

Spring Security是一个基于Spring框架的安全认证和授权框架，它提供了一套全面的安全解决方案，可以在Web应用、移动应用和Web服务等不同场景下使用。Spring Security的核心思想是认证和授权，即验证用户身份并授予相应的权限。 Spring Security提供了一些基本的安全特性，如身份验证、访问控制和数据加密等。同时，它还支持多种身份验证机制，如基于表单的身份验证、基于HTTP Basic的身份验证、基于HTTP Digest的身份验证和基于LDAP的身份验证等。

## 实例

下面是一个简单的Spring Security的示例代码，演示了如何实现基于表单的身份验证：

首先，需要在pom.xml文件中添加Spring Security的依赖：

```
&lt;dependency&gt;
  &lt;groupId&gt;org.springframework.security&lt;/groupId&gt;
  &lt;artifactId&gt;spring-security-web&lt;/artifactId&gt;
  &lt;version&gt;${<!-- -->spring-security.version}&lt;/version&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
  &lt;groupId&gt;org.springframework.security&lt;/groupId&gt;
  &lt;artifactId&gt;spring-security-config&lt;/artifactId&gt;
  &lt;version&gt;${<!-- -->spring-security.version}&lt;/version&gt;
&lt;/dependency&gt;


```

然后，在Spring配置文件中添加以下代码：

```
@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

  @Autowired
  private CustomUserDetailsService userDetailsService;

  @Autowired
  private CustomAuthenticationSuccessHandler authenticationSuccessHandler;

  @Autowired
  private CustomAuthenticationFailureHandler authenticationFailureHandler;

  @Override
  protected void configure(HttpSecurity http) throws Exception {<!-- -->
    http
      .authorizeRequests()
        .antMatchers("/public/**").permitAll()
        .anyRequest().authenticated()
        .and()
      .formLogin()
        .loginPage("/login")
        .usernameParameter("username")
        .passwordParameter("password")
        .successHandler(authenticationSuccessHandler)
        .failureHandler(authenticationFailureHandler)
        .permitAll()
        .and()
      .logout()
        .logoutUrl("/logout")
        .logoutSuccessUrl("/login?logout")
        .permitAll();
  }

  @Autowired
  public void configureGlobal(AuthenticationManagerBuilder auth) throws Exception {<!-- -->
    auth
      .userDetailsService(userDetailsService)
      .passwordEncoder(passwordEncoder());
  }

  @Bean
  public PasswordEncoder passwordEncoder() {<!-- -->
    return new BCryptPasswordEncoder();
  }
}


```

这个配置文件定义了一些基本的安全特性，如允许所有用户访问/public路径下的资源，其他请求需要进行身份验证；定义了表单登录的相关配置，包括登录页面、用户名和密码的参数名、登录成功和失败的处理器等；定义了退出登录的相关配置，包括退出登录的URL和退出成功后跳转的页面等。

最后，需要实现一个自定义的UserDetailsService接口，用于从数据库中读取用户信息并进行身份验证。这里给出一个简单的示例：

```
@Service
public class CustomUserDetailsService implements UserDetailsService {<!-- -->

  @Autowired
  private UserRepository userRepository;

  @Override
  public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {<!-- -->
    User user = userRepository.findByUsername(username);
    if (user == null) {<!-- -->
      throw new UsernameNotFoundException("User notfound: " + username);
}
List&lt;GrantedAuthority&gt; authorities = new ArrayList&lt;&gt;();
for (Role role : user.getRoles()) {<!-- -->
authorities.add(new SimpleGrantedAuthority(role.getName()));
}
return new org.springframework.security.core.userdetails.User(
user.getUsername(), user.getPassword(), authorities);
}
}


```

这个UserDetailsService实现从数据库中读取用户信息，并将用户的角色作为GrantedAuthority返回。在Spring Security中，GrantedAuthority表示用户的权限，可以用于访问控制。

除了基于表单的身份验证，Spring Security还支持其他多种身份验证方式，如基于HTTP Basic的身份验证、基于HTTP Digest的身份验证和基于LDAP的身份验证等。同时，它还提供了丰富的访问控制机制，如基于角色的访问控制、基于IP地址的访问控制和基于表达式的访问控制等。

总之，Spring Security是一个非常强大的安全框架，可以帮助开发人员轻松实现各种安全特性，并提高应用程序的安全性。
