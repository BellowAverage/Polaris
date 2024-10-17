
--- 
title:  第7章 Spring Security 的 REST API 与微服务安全（2024 最新版） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/c8cd3bf5add94557805f2bf957d5bd04.png#pic_center" alt="在这里插入图片描述">



#### 文章目录
- - <ul><li>- - <ul><li>- - - - - - - <ul><li>- - - - - <ul><li>- - 


## 7.1 保护 REST API

在数字化时代，REST API是现代Web应用和微服务架构中数据交互的关键组成部分。然而，随着它们的普及和重要性的增加，保护这些API免受恶意攻击变得尤为重要。本节将探讨保护REST API的基础知识和实用案例。

### 7.1.1 基础知识详解

在构建和维护REST API时，安全性是一个不容忽视的要素。REST API作为应用程序与外界交互的接口，常常面临着各种安全威胁，包括但不限于身份盗窃、数据泄露、服务拒绝攻击等。因此，采取有效的安全措施保护REST API是至关重要的。以下是保护REST API时需掌握的基础知识。

**身份验证 (Authentication)**
- **定义**：确定请求者的身份，确保只有合法用户可以访问API。<li>**方法**： 
  <ul>- **基本认证**：通过HTTP头传递用户名和密码的简单认证方法，需要使用HTTPS来避免凭证泄露。- **令牌认证**：如JWT，通过签名的令牌确认用户身份，支持无状态认证。- **OAuth/OAuth2**：为第三方应用提供限制的访问权限，而无需暴露用户的凭证。
**授权 (Authorization)**
- **定义**：确定已认证的用户可以执行的操作或访问的数据。<li>**实现方式**： 
  <ul>- **角色基础的访问控制（RBAC）**：根据用户的角色来决定其权限。- **属性基础的访问控制（ABAC）**：根据属性（用户属性、资源属性和环境属性）来动态决定访问权限。
**传输安全 (Transport Security)**
- **HTTPS**：使用SSL/TLS加密HTTP请求和响应，防止数据在传输过程中被截获或篡改。- **HSTS**（HTTP Strict Transport Security）：强制客户端（如浏览器）使用HTTPS与服务器建立连接。
**数据保护**
- **数据加密**：对敏感数据进行加密处理，保护存储在服务器上或传输过程中的数据。- **数据脱敏**：在公开的响应中避免直接展示敏感数据，如用户ID、电子邮件地址等。
**输入验证**
- **目的**：防止恶意输入导致的安全漏洞，如SQL注入、XSS攻击。- **实践**：对所有输入数据进行验证，拒绝不符合预期格式的请求。
**错误处理**
- **优雅处理**：错误信息应足够通用，避免泄露敏感信息或系统细节。- **日志记录**：记录错误日志，但避免在日志中记录敏感信息。
**限制与节流 (Rate Limiting and Throttling)**
- **目的**：防止API滥用，保护后端服务不受恶意攻击或过载。- **实现**：限制来自单一来源的请求频率，当达到限制时返回适当的HTTP状态码。
通过这些基础知识的详解，我们可以看到保护REST API涉及到多个方面，包括但不限于身份验证、授权、传输安全、数据保护和输入验证等。正确实施这些安全措施，可以有效提高API的安全性，保护用户数据和服务的稳定性。

### 7.1.2 重点案例：使用 JWT 进行身份验证和授权

JSON Web Token（JWT）是一种开放标准（RFC 7519），用于在双方之间安全地传输信息作为 JSON 对象。由于其紧凑和自包含的特性，JWT 非常适合用于 REST API 的身份验证和授权。以下案例将引导你实现 JWT 在 Spring Boot 应用中的身份验证和授权。

#### 案例 Demo

**步骤 1**: 引入 JWT 库依赖

首先，在 Spring Boot 项目的`pom.xml`中添加对 JWT 库的依赖。这里我们使用`jjwt`库作为示例：

```
&lt;dependency&gt;
    &lt;groupId&gt;io.jsonwebtoken&lt;/groupId&gt;
    &lt;artifactId&gt;jjwt&lt;/artifactId&gt;
    &lt;version&gt;0.9.1&lt;/version&gt;
&lt;/dependency&gt;

```

**步骤 2**: 创建JWT工具类

创建一个JWT工具类`JwtUtil`，用于生成和验证 JWT 令牌：

```
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import org.springframework.stereotype.Component;

import java.util.Date;
import java.util.function.Function;

@Component
public class JwtUtil {<!-- -->
    private String secret = "yourSecretKey"; // 用于签名的密钥

    public String extractUsername(String token) {<!-- -->
        return extractClaim(token, Claims::getSubject);
    }

    public Date extractExpiration(String token) {<!-- -->
        return extractClaim(token, Claims::getExpiration);
    }

    public &lt;T&gt; T extractClaim(String token, Function&lt;Claims, T&gt; claimsResolver) {<!-- -->
        final Claims claims = extractAllClaims(token);
        return claimsResolver.apply(claims);
    }

    private Claims extractAllClaims(String token) {<!-- -->
        return Jwts.parser().setSigningKey(secret).parseClaimsJws(token).getBody();
    }

    private Boolean isTokenExpired(String token) {<!-- -->
        return extractExpiration(token).before(new Date());
    }

    public String generateToken(String username) {<!-- -->
        return Jwts.builder().setSubject(username)
                .setIssuedAt(new Date(System.currentTimeMillis()))
                .setExpiration(new Date(System.currentTimeMillis() + 1000 * 60 * 60 * 10)) // 10小时有效期
                .signWith(SignatureAlgorithm.HS256, secret).compact();
    }

    public Boolean validateToken(String token, String username) {<!-- -->
        final String tokenUsername = extractUsername(token);
        return (username.equals(tokenUsername) &amp;&amp; !isTokenExpired(token));
    }
}

```

**步骤 3**: 实现 JWT 请求过滤器

创建`JwtRequestFilter`类，它将在每次请求时检查 JWT 令牌的有效性：

```
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.web.filter.OncePerRequestFilter;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class JwtRequestFilter extends OncePerRequestFilter {<!-- -->

    @Autowired
    private MyUserDetailsService userDetailsService;

    @Autowired
    private JwtUtil jwtUtil;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain chain)
            throws ServletException, IOException {<!-- -->
        
        final String authorizationHeader = request.getHeader("Authorization");

        String username = null;
        String jwt = null;

        if (authorizationHeader != null &amp;&amp; authorizationHeader.startsWith("Bearer ")) {<!-- -->
            jwt = authorizationHeader.substring(7);
            username = jwtUtil.extractUsername(jwt);
        }

        if (username != null &amp;&amp; SecurityContextHolder.getContext().getAuthentication() == null) {<!-- -->
            UserDetails userDetails = this.userDetailsService.loadUserByUsername(username);

            if (jwtUtil.validateToken(jwt, userDetails.getUsername())) {<!-- -->
                UsernamePasswordAuthenticationToken authToken = 
                        new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());
                authToken.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
                SecurityContextHolder.getContext().setAuthentication(authToken);
            }
        }
        chain.doFilter(request, response);
    }
}

```

**步骤 4**: 配置 Spring Security

最后，在 Spring Security 配置中注册`JwtRequestFilter`：

```
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.http.SessionCreation

Policy;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Autowired
    private JwtRequestFilter jwtRequestFilter;

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http.csrf().disable()
                .authorizeRequests().antMatchers("/authenticate").permitAll()
                .anyRequest().authenticated()
                .and().sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS);
        http.addFilterBefore(jwtRequestFilter, UsernamePasswordAuthenticationFilter.class);
    }
}

```

通过这些步骤，你的 Spring Boot 应用现在能够利用 JWT 进行身份验证和授权，从而保护 REST API 免受未授权访问。记得保密你的 JWT 密钥，并定期更新以维护系统安全。

### 7.1.3 拓展案例 1：API 密钥认证

API 密钥认证是一种简单但有效的安全措施，用于控制对 REST API 的访问。它适用于服务到服务的通信，其中一个服务需要验证另一个服务的请求。以下案例演示了如何在 Spring Boot 应用中实现 API 密钥认证。

#### 案例 Demo

**步骤 1**: 定义 API 密钥存储

首先，假设我们有一个简单的方式来存储和验证 API 密钥。在实际应用中，这些密钥可能会存储在数据库或配置文件中。这里我们使用一个简单的 Map 模拟。

```
import org.springframework.stereotype.Component;

import java.util.HashMap;
import java.util.Map;

@Component
public class ApiKeyStore {<!-- -->
    private final Map&lt;String, String&gt; apiKeys = new HashMap&lt;&gt;();

    public ApiKeyStore() {<!-- -->
        // 初始化一些API密钥，实际应用中应该从安全的地方加载
        apiKeys.put("service1", "key-123");
        apiKeys.put("service2", "key-456");
    }

    public boolean validateKey(String serviceId, String apiKey) {<!-- -->
        return apiKey.equals(apiKeys.get(serviceId));
    }
}

```

**步骤 2**: 实现 API 密钥认证过滤器

创建`ApiKeyAuthenticationFilter`类，该过滤器负责拦截请求并验证 API 密钥。

```
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.filter.OncePerRequestFilter;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class ApiKeyAuthenticationFilter extends OncePerRequestFilter {<!-- -->

    @Autowired
    private ApiKeyStore apiKeyStore;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain chain)
            throws ServletException, IOException {<!-- -->
        
        String serviceId = request.getHeader("Service-Id");
        String apiKey = request.getHeader("API-Key");

        if (serviceId == null || apiKey == null || !apiKeyStore.validateKey(serviceId, apiKey)) {<!-- -->
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Invalid API Key");
            return;
        }

        chain.doFilter(request, response);
    }
}

```

**步骤 3**: 在Spring Security 配置中注册 API 密钥认证过滤器

接下来，需要在 Spring Security 配置中添加`ApiKeyAuthenticationFilter`。

```
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.context.annotation.Bean;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Bean
    public ApiKeyAuthenticationFilter apiKeyAuthenticationFilter() {<!-- -->
        return new ApiKeyAuthenticationFilter();
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .addFilterBefore(apiKeyAuthenticationFilter(), UsernamePasswordAuthenticationFilter.class)
            .authorizeRequests()
                .anyRequest().authenticated()
            .and()
            .csrf().disable();
    }
}

```

通过以上步骤，Spring Boot 应用现在能够使用 API 密钥进行简单的身份验证。任何未提供有效 API 密钥的请求都将被拒绝访问。

#### 测试API密钥认证

启动应用并尝试发送请求到受保护的端点，确保在请求头中包含有效的`Service-Id`和`API-Key`。如果密钥验证失败，应收到 HTTP 401 Unauthorized 错误。

这种 API 密钥认证方法虽然简单，但在某些场景下非常有效，尤其是在服务对服务的通信中。记得保护好你的 API 密钥，避免泄露。

### 7.1.4 拓展案例 2：使用 OAuth2 保护 API

OAuth2是一个开放标准，允许用户授权第三方应用访问其服务器资源，而无需将用户名和密码直接暴露给第三方应用。这种机制特别适合需要跨应用授权的场景。在本案例中，我们将展示如何在Spring Boot应用中使用OAuth2保护REST API。

#### 案例 Demo

**步骤 1**: 引入Spring Security OAuth2依赖

首先，确保你的Spring Boot项目中包含了Spring Security OAuth2的依赖。在`pom.xml`文件中添加：

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.security&lt;/groupId&gt;
    &lt;artifactId&gt;spring-security-oauth2&lt;/artifactId&gt;
    &lt;version&gt;2.3.6.RELEASE&lt;/version&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.security&lt;/groupId&gt;
    &lt;artifactId&gt;spring-security-jwt&lt;/artifactId&gt;
    &lt;version&gt;1.0.10.RELEASE&lt;/version&gt;
&lt;/dependency&gt;

```

**步骤 2**: 配置授权服务器

创建一个配置类`AuthorizationServerConfig`来配置OAuth2授权服务器。这里我们使用内存中的客户端和用户存储作为示例。

```
import org.springframework.context.annotation.Configuration;
import org.springframework.security.oauth2.config.annotation.configurers.ClientDetailsServiceConfigurer;
import org.springframework.security.oauth2.config.annotation.web.configuration.EnableAuthorizationServer;
import org.springframework.security.oauth2.config.annotation.web.configuration.AuthorizationServerConfigurerAdapter;

@Configuration
@EnableAuthorizationServer
public class AuthorizationServerConfig extends AuthorizationServerConfigurerAdapter {<!-- -->

    @Override
    public void configure(ClientDetailsServiceConfigurer clients) throws Exception {<!-- -->
        clients.inMemory()
                .withClient("client-id")
                .secret("{noop}client-secret")
                .authorizedGrantTypes("authorization_code", "refresh_token", "password")
                .scopes("read", "write")
                .autoApprove(true);
    }
}

```

**步骤 3**: 配置资源服务器

创建一个配置类`ResourceServerConfig`来配置OAuth2资源服务器。这里我们定义了一些安全限制，以保护API端点。

```
import org.springframework.context.annotation.Configuration;
import org.springframework.security.oauth2.config.annotation.web.configuration.EnableResourceServer;
import org.springframework.security.oauth2.config.annotation.web.configuration.ResourceServerConfigurerAdapter;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;

@Configuration
@EnableResourceServer
public class ResourceServerConfig extends ResourceServerConfigurerAdapter {<!-- -->

    @Override
    public void configure(HttpSecurity http) throws Exception {<!-- -->
        http
                .authorizeRequests()
                .antMatchers("/api/**").authenticated()
                .anyRequest().permitAll();
    }
}

```

**步骤 4**: 定义用户详情服务

为了支持"password"授权类型，你需要定义一个`UserDetailsService`。在这个例子中，我们简单地在内存中创建一个用户。

```
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;

@Configuration
public class UserDetailsConfig {<!-- -->

    @Bean
    public UserDetailsService userDetailsService() {<!-- -->
        InMemoryUserDetailsManager manager = new InMemoryUserDetailsManager();
        manager.createUser(User.withUsername("user").password("{noop}password").roles("USER").build());
        return manager;
    }
}

```

#### 测试 OAuth2 保护的 API

启动应用后，首先获取访问令牌：
- 对于"password"授权类型，可以使用HTTP请求直接向授权服务器发送用户名和密码来获取令牌。- 对于"authorization_code"类型，需要通过用户代理（如Web浏览器）重定向到授权服务器的登录页面，用户登录后，授权服务器会将令牌重定向回客户端指定的重定向URI。
一旦获取到访问令牌，就可以在请求的`Authorization`头中使用它来访问受保护的资源。

通过以上步骤，你的Spring Boot应用现在能够利用OAuth2进行身份验证和授权，从而保护REST API免受未经授权的访问。这种方法为应用提供了强大的安全性和灵活性，使其能够安全地与外部应用或服务进行交互。

通过实现这些策略和案例，你可以有效地保护你的 REST API 免受常见安全威胁，确保数据的安全和服务的可用性。记住，安全是一个持续的过程，需要定期审查和更新你的安全策略和实践。

## 7.2 微服务安全最佳实践

微服务架构通过将应用拆分为一系列较小、独立的服务来提高灵活性和可维护性。然而，这种分散的架构也带来了新的安全挑战。保护微服务不仅要求保证数据的安全，还要确保服务间通信的安全。以下是微服务安全的一些基础知识和最佳实践。

### 7.2.1 基础知识详解

在微服务架构中，应用被拆分成多个服务，每个服务执行特定的功能，并通过网络进行通信。这种架构提高了应用的可伸缩性和灵活性，但同时也引入了新的安全挑战。下面详细探讨微服务安全的关键方面和最佳实践。

**服务间通信安全**
- **TLS/SSL加密**：所有服务间的通信都应通过TLS（传输层安全协议）进行加密，确保数据传输过程中的机密性和完整性。- **双向SSL**：在某些情况下，服务之间还需要相互验证对方的身份，这可以通过双向SSL（又称为客户端证书认证）来实现。
**身份验证和授权**
- **统一身份认证机制**：微服务架构应该有一个集中的身份认证服务，所有服务都应通过这个服务来认证用户身份。- **细粒度授权**：授权决策应基于用户的角色或权限，以及服务的安全策略。可以实现角色基础访问控制（RBAC）或更灵活的属性基访问控制（ABAC）。
**API 网关**
- **集中安全控制**：API网关作为微服务架构中的统一入口，可以在这里集中实施身份验证、授权、流量限制等安全策略。- **流量管理**：API网关可以对流量进行监控和控制，实现请求限流和熔断，防止服务被过度使用或恶意攻击。
**安全令牌服务**
- **OAuth2和JWT**：OAuth2是一个授权框架，允许第三方应用代表用户访问其资源，而JWT（JSON Web Token）通常用于在OAuth2流程中携带身份验证和授权信息。
**微服务防御措施**
- **输入验证**：所有服务都应实施严格的输入验证，以防止SQL注入、跨站脚本（XSS）等攻击。- **依赖管理**：定期更新服务的依赖库，修补已知的安全漏洞。- **错误处理**：适当的错误处理可以防止敏感信息泄露，应避免在响应中返回过多的错误细节。
**安全编码实践**
- **代码审计和扫描**：定期进行代码审计和使用自动化工具扫描代码，以发现潜在的安全问题。- **敏感数据保护**：对敏感数据进行加密处理，并在存储和传输时采取适当的保护措施。
通过理解和实施这些基础知识和最佳实践，你可以为微服务架构构建坚实的安全基础，保护你的应用免受各种网络安全威胁。安全是一个持续的过程，需要不断地审视、更新和改进安全策略和措施。

### 7.2.2 重点案例：使用 JWT 实现服务间认证

在微服务架构中，服务间认证是确保每个服务的请求都来自受信任来源的重要机制。使用JSON Web Tokens（JWT）进行服务间认证不仅能提供安全保障，还能确保认证过程的轻量和高效。以下案例演示了如何在Spring Boot微服务架构中实现JWT进行服务间认证。

#### 案例 Demo

**步骤 1**: 创建JWT工具类

首先，创建一个`JwtTokenUtil`类来处理JWT的生成和验证。这个类将提供生成JWT的方法和验证JWT的方法。

```
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.util.Date;
import java.util.function.Function;

@Component
public class JwtTokenUtil {<!-- -->
    @Value("${jwt.secret}")
    private String secret;

    @Value("${jwt.expiration}")
    private Long expiration;

    public String generateToken(String subject) {<!-- -->
        return Jwts.builder()
            .setSubject(subject)
            .setIssuedAt(new Date(System.currentTimeMillis()))
            .setExpiration(new Date(System.currentTimeMillis() + expiration))
            .signWith(SignatureAlgorithm.HS512, secret)
            .compact();
    }

    public Boolean validateToken(String token, String subject) {<!-- -->
        final String tokenSubject = getClaimFromToken(token, Claims::getSubject);
        return (subject.equals(tokenSubject) &amp;&amp; !isTokenExpired(token));
    }

    public &lt;T&gt; T getClaimFromToken(String token, Function&lt;Claims, T&gt; claimsResolver) {<!-- -->
        final Claims claims = getAllClaimsFromToken(token);
        return claimsResolver.apply(claims);
    }

    private Claims getAllClaimsFromToken(String token) {<!-- -->
        return Jwts.parser().setSigningKey(secret).parseClaimsJws(token).getBody();
    }

    private Boolean isTokenExpired(String token) {<!-- -->
        final Date expiration = getClaimFromToken(token, Claims::getExpiration);
        return expiration.before(new Date());
    }
}

```

在`application.properties`中配置JWT密钥和过期时间：

```
jwt.secret=YourSecretKey
jwt.expiration=604800000  # JWT token的过期时间（这里设置为7天）

```

**步骤 2**: 实现服务间请求拦截器

创建一个`FeignClientInterceptor`拦截器，用于在发送服务间请求时附加JWT。

```
import feign.RequestInterceptor;
import feign.RequestTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class FeignClientInterceptor implements RequestInterceptor {<!-- -->

    @Autowired
    private JwtTokenUtil jwtTokenUtil;

    @Override
    public void apply(RequestTemplate template) {<!-- -->
        template.header("Authorization", "Bearer " + jwtTokenUtil.generateToken("service-account"));
    }
}

```

**步骤 3**: 配置服务接收方验证JWT

在服务接收方，创建一个`JwtRequestFilter`过滤器来验证每个进入的请求的JWT。

```
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.filter.OncePerRequestFilter;
import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class JwtRequestFilter extends OncePerRequestFilter {<!-- -->

    @Autowired
    private JwtTokenUtil jwtTokenUtil;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain chain)
            throws ServletException, IOException {<!-- -->
        
        final String requestTokenHeader = request.getHeader("Authorization");

        String jwtToken = null;
        if (requestTokenHeader != null &amp;&amp; requestTokenHeader.startsWith("Bearer ")) {<!-- -->
            jwtToken = requestTokenHeader.substring(7);
            try {<!-- -->
                if (!jwtTokenUtil.validateToken(jwtToken, "service-account")) {<!-- -->
                    throw new ServletException("JWT Token is invalid");
                }
            } catch (Exception e) {<!-- -->
                throw new ServletException("JWT Token validation failed", e);
            }
        } else {<!-- -->
            logger.warn("JWT Token does not begin with Bearer String");
        }
        chain.doFilter(request, response);
    }
}

```

**步骤 4**: 在服务接收方配置Spring Security使用JWT过滤器

最后，在服务接收方的Spring Security配置中，注册`JwtRequestFilter`来验证进入的请求。

```
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurity

ConfigurerAdapter;
import org.springframework.context.annotation.Bean;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Bean
    public JwtRequestFilter jwtRequestFilter() {<!-- -->
        return new JwtRequestFilter();
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http.csrf().disable()
            .addFilterBefore(jwtRequestFilter(), UsernamePasswordAuthenticationFilter.class)
            .authorizeRequests().anyRequest().authenticated();
    }
}

```

通过上述步骤，微服务架构中的服务间通信将通过JWT进行安全认证，确保只有验证通过的服务请求才能被接受和处理。这种方法为服务间通信提供了一个安全的认证机制，有助于防止未授权访问。

### 7.2.3 拓展案例 1：使用 Spring Cloud Security 简化安全配置

Spring Cloud Security 提供了一套简化微服务安全配置的工具，使得实现复杂的安全需求变得更加直接和简单。利用 Spring Cloud Security，可以轻松实现服务间的安全通信、统一的身份验证和授权等功能。以下案例将展示如何使用 Spring Cloud Security 在微服务架构中简化安全配置。

#### 案例 Demo

假设我们有一个微服务架构，需要在服务间实现基于 OAuth2 的安全通信。以下是步骤和示例代码：

**步骤 1**: 引入 Spring Cloud Security 依赖

首先，在微服务项目的`pom.xml`文件中添加 Spring Cloud Security 依赖：

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
    &lt;artifactId&gt;spring-cloud-starter-security&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
    &lt;artifactId&gt;spring-cloud-starter-oauth2&lt;/artifactId&gt;
&lt;/dependency&gt;

```

**步骤 2**: 配置资源服务器

在微服务中配置资源服务器，以使用 OAuth2 令牌进行安全验证。创建一个配置类`ResourceServerConfig` 继承 `ResourceServerConfigurerAdapter`，并使用 `@EnableResourceServer` 注解来启用资源服务器。

```
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.oauth2.config.annotation.web.configuration.EnableResourceServer;
import org.springframework.security.oauth2.config.annotation.web.configuration.ResourceServerConfigurerAdapter;

@EnableResourceServer
public class ResourceServerConfig extends ResourceServerConfigurerAdapter {<!-- -->

    @Override
    public void configure(HttpSecurity http) throws Exception {<!-- -->
        http.authorizeRequests()
            .antMatchers("/public/**").permitAll()  // 公开访问的端点
            .anyRequest().authenticated();  // 其他所有请求都需要验证
    }
}

```

**步骤 3**: 配置OAuth2客户端

如果服务需要作为客户端访问其他受保护的服务，可以在`application.yml`或`application.properties`中配置OAuth2客户端详细信息：

```
security:
  oauth2:
    client:
      clientId: myClientId
      clientSecret: myClientSecret
      accessTokenUri: http://AUTH-SERVER/oauth/token
      userAuthorizationUri: http://AUTH-SERVER/oauth/authorize
    resource:
      userInfoUri: http://AUTH-SERVER/userinfo

```

**步骤 4**: 使用 Feign 客户端进行服务间调用

当使用 Feign 客户端进行服务间调用时，可以通过配置自动携带 OAuth2 令牌。首先，确保 Feign 客户端在请求时携带 OAuth2 令牌：

```
import feign.RequestInterceptor;
import org.springframework.context.annotation.Bean;
import org.springframework.security.oauth2.client.OAuth2RestTemplate;

public class FeignClientConfig {<!-- -->

    @Bean
    public RequestInterceptor oauth2FeignRequestInterceptor(OAuth2RestTemplate oAuth2RestTemplate) {<!-- -->
        return requestTemplate -&gt; {<!-- -->
            requestTemplate.header("Authorization", "Bearer " + oAuth2RestTemplate.getAccessToken().getValue());
        };
    }
}

```

在 Feign 客户端接口上应用配置：

```
@FeignClient(name = "other-service", configuration = FeignClientConfig.class)
public interface OtherServiceClient {<!-- -->
    // 定义访问其他服务的方法
}

```

通过上述步骤，你可以利用 Spring Cloud Security 简化微服务架构中的安全配置，无需编写大量的安全配置代码，就可以实现服务间的安全通信和访问控制。这种方法不仅减轻了开发负担，还提高了安全性和可维护性。

### 7.2.4 拓展案例 2：API 网关安全

在微服务架构中，API网关扮演着重要的角色，它不仅是微服务的统一入口，也是实施安全策略的理想位置。通过在API网关层面集中处理身份验证、授权、以及流量控制，可以大大简化单个微服务的安全配置。以下案例将演示如何利用Spring Cloud Gateway实现API网关的安全配置。

#### 案例 Demo

**步骤 1**: 引入Spring Cloud Gateway依赖

首先，确保在微服务项目的`pom.xml`中引入Spring Cloud Gateway依赖：

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
    &lt;artifactId&gt;spring-cloud-starter-gateway&lt;/artifactId&gt;
&lt;/dependency&gt;

```

**步骤 2**: 配置API网关路由

接下来，在`application.yml`中配置API网关的路由规则，将不同的请求转发到对应的微服务：

```
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://USER-SERVICE
          predicates:
            - Path=/user/**
          filters:
            - RemoveRequestHeader=Cookie
        - id: order-service
          uri: lb://ORDER-SERVICE
          predicates:
            - Path=/order/**

```

这里使用了`lb://`前缀指定服务发现中的服务ID，`RemoveRequestHeader`过滤器用来移除敏感的请求头信息。

**步骤 3**: 实现全局过滤器进行身份验证

在API网关中实现一个全局过滤器，用于检查请求是否包含有效的身份验证信息，如JWT令牌。创建`GlobalAuthFilter`类实现`GlobalFilter`接口：

```
import org.springframework.cloud.gateway.filter.GatewayFilterChain;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.HttpStatus;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;

@Component
public class GlobalAuthFilter implements GlobalFilter, Ordered {<!-- -->

    @Override
    public Mono&lt;Void&gt; filter(ServerWebExchange exchange, GatewayFilterChain chain) {<!-- -->
        // 检查请求中的身份验证信息，例如JWT令牌
        String token = exchange.getRequest().getHeaders().getFirst("Authorization");
        if (token == null || !token.startsWith("Bearer ")) {<!-- -->
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }
        // 进行令牌验证...
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {<!-- -->
        return -100; // 设置过滤器优先级
    }
}

```

**步骤 4**: 限流和熔断配置

使用Spring Cloud Gateway的内置支持来配置限流和熔断，保护后端微服务不受恶意访问或流量洪峰的影响。在`application.yml`中添加相应配置：

```
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://USER-SERVICE
          predicates:
            - Path=/user/**
          filters:
            - name: RequestRateLimiter
              args:
                key-resolver: "#{@userKeyResolver}"
                redis-rate-limiter.replenishRate: 10
                redis-rate-limiter.burstCapacity: 20

```

这里配置了一个基于Redis的请求速率限制器，`key-resolver`用于确定限流的键，这里假设已经有一个`userKeyResolver`的Bean定义了用户识别逻辑。

通过这些步骤，你的API网关将能够有效地管理和保护微服务架构中的流量，实现统一的身份验证、授权以及流量控制。通过在API网关集中处理安全逻辑，可以减轻各个微服务的安全负担，简化安全配置和管理。

通过实施这些微服务安全最佳实践，你可以构建一个既灵活又安全的微服务架构，有效保护服务和数据免受各种网络安全威胁的侵害。记得，安全是一个持续的过程，需要定期审查和更新你的安全策略和实践。

## 7.3 API 网关集成

在微服务架构中，API网关作为客户端和服务之间的中介，承担着路由请求、聚合响应、身份验证与授权、以及流量监控等关键职责。通过集成API网关，可以在微服务架构中实现统一的入口点，简化客户端的交互，同时加强服务的安全性和可管理性。

### 7.3.1 基础知识详解

在现代微服务架构中，API网关不仅仅是一个简单的路由器，而是服务和数据流的关键管理点。它承担着请求转发、服务聚合、安全验证、流量控制和监控等多项职责。深入理解API网关的作用和配置方法对于构建一个高效、安全的微服务系统至关重要。

**请求路由**
- **定义**：API网关接收外部请求，并根据预定义的规则将请求转发到对应的后端服务。- **作用**：实现了请求的负载均衡，提高了系统的可用性和扩展性。
**服务聚合**
- **定义**：API网关可以将来自多个微服务的数据聚合成一个统一的响应返回给客户端。- **优势**：减少了客户端需要发送的请求数量，优化了数据交互流程，提高了用户体验。
**身份验证与授权**
- **中心化安全策略**：在API网关层面集中处理所有进入微服务系统的请求的身份验证和授权。- **优点**：简化了单个微服务的安全配置，提高了安全性和维护性。
**流量控制**
- **限流**：限制对API的请求速率，防止服务因过载而崩溃。- **熔断**：在下游服务不可用时，自动停止向其发送请求，防止故障蔓延。
**日志和监控**
- **集中式日志管理**：API网关可以记录所有经过的请求和响应，为系统监控和故障排查提供详细数据。- **监控指标**：收集关于请求延迟、成功率和服务健康状况等关键指标，帮助维护系统稳定性。
**安全性**
- **传输加密**：使用HTTPS等技术加密客户端和API网关之间的通信，保护数据安全。- **跨域资源共享（CORS）**：API网关可以统一处理CORS预检请求，简化后端服务的CORS配置。
通过这些基础知识的了解，我们可以看到API网关在微服务架构中发挥着至关重要的作用，不仅优化了服务的调用和数据的聚合，还大大增强了系统的安全性和可观测性。正确配置和使用API网关，对于保障微服务架构的健康运行至关重要。

### 7.3.2 重点案例：集成 Spring Cloud Gateway

Spring Cloud Gateway提供了一个简单而强大的方式来构建API网关，它与Spring生态系统无缝集成，支持动态路由、过滤和安全性配置。下面的案例将指导你如何在Spring Boot应用中集成Spring Cloud Gateway，实现API网关的基本功能。

#### 案例 Demo

**步骤 1**: 创建Spring Boot项目并引入依赖

首先，确保你的`pom.xml`文件中包含了Spring Cloud Gateway的依赖：

```
&lt;dependencies&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
        &lt;artifactId&gt;spring-cloud-starter-gateway&lt;/artifactId&gt;
        &lt;version&gt;YOUR_SPRING_CLOUD_VERSION&lt;/version&gt;
    &lt;/dependency&gt;
&lt;/dependencies&gt;

&lt;dependencyManagement&gt;
    &lt;dependencies&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
            &lt;artifactId&gt;spring-cloud-dependencies&lt;/artifactId&gt;
            &lt;version&gt;YOUR_SPRING_CLOUD_VERSION&lt;/version&gt;
            &lt;type&gt;pom&lt;/type&gt;
            &lt;scope&gt;import&lt;/scope&gt;
        &lt;/dependency&gt;
    &lt;/dependencies&gt;
&lt;/dependencyManagement&gt;

```

请替换`YOUR_SPRING_CLOUD_VERSION`为当前Spring Cloud的版本，比如`Hoxton.SR9`。

**步骤 2**: 配置路由规则

在`application.yml`文件中配置路由规则，将不同的请求路径路由到对应的微服务：

```
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://USER-SERVICE
          predicates:
            - Path=/user/**
          filters:
            - StripPrefix=1
        - id: product-service
          uri: lb://PRODUCT-SERVICE
          predicates:
            - Path=/product/**
          filters:
            - StripPrefix=1

```

这里使用`lb://`表示使用Spring Cloud的负载均衡，`StripPrefix=1`过滤器用于移除请求路径中的第一部分。

**步骤 3**: 添加全局过滤器进行请求日志记录

创建一个全局过滤器`GlobalLoggingFilter`来记录每个请求的详细信息：

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.stereotype.Component;
import reactor.core.publisher.Mono;

@Component
public class GlobalLoggingFilter implements GlobalFilter, Ordered {<!-- -->

    private final Logger logger = LoggerFactory.getLogger(GlobalLoggingFilter.class);

    @Override
    public Mono&lt;Void&gt; filter(ServerWebExchange exchange, GatewayFilterChain chain) {<!-- -->
        logger.info("Original request path: {}", exchange.getRequest().getPath());
        return chain.filter(exchange)
                .then(Mono.fromRunnable(() -&gt;
                        logger.info("Response status code: {}", exchange.getResponse().getStatusCode())));
    }

    @Override
    public int getOrder() {<!-- -->
        return -1; // 设置过滤器顺序
    }
}

```

**步骤 4**: 配置安全性和跨域（可选）

如果需要，在API网关层面配置安全性和CORS支持：

```
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.reactive.CorsWebFilter;
import org.springframework.web.cors.reactive.UrlBasedCorsConfigurationSource;
import org.springframework.web.util.pattern.PathPatternParser;

@Configuration
public class GatewayConfig {<!-- -->

    @Bean
    public CorsWebFilter corsWebFilter() {<!-- -->
        CorsConfiguration config = new CorsConfiguration();
        config.addAllowedMethod("*");
        config.addAllowedOrigin("*");
        config.addAllowedHeader("*");

        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource(new PathPatternParser());
        source.registerCorsConfiguration("/**", config);

        return new CorsWebFilter(source);
    }
}

```

通过这些步骤，你已经成功地在Spring Boot项目中集成了Spring Cloud Gateway，配置了路由规则，添加了全局日志记录过滤器，并可选地配置了安全性和CORS支持。Spring Cloud Gateway作为API网关，不仅提高了微服务架构的灵活性和可维护性，也加强了整个系统的安全性。

### 7.3.3 拓展案例 1：限流策略

在面对高流量的情况下，限流是保护微服务不被过度使用、避免系统崩溃的关键策略。Spring Cloud Gateway提供了内置的限流功能，可以通过配置轻松实现。以下案例将展示如何在Spring Cloud Gateway中配置限流策略。

#### 案例 Demo

**步骤 1**: 引入Redis依赖

首先，确保你的项目中包含了Redis的依赖，因为Spring Cloud Gateway的限流特性默认是基于Redis实现的。

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-data-redis-reactive&lt;/artifactId&gt;
&lt;/dependency&gt;

```

**步骤 2**: 配置限流规则

在`application.yml`文件中，配置限流规则。你可以根据需要定义不同的限流条件，如IP地址、用户ID等。以下示例展示了如何基于请求路径和IP地址进行限流：

```
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://USER-SERVICE
          predicates:
            - Path=/user/**
          filters:
            - name: RequestRateLimiter
              args:
                key-resolver: "#{@ipKeyResolver}"
                redis-rate-limiter.replenishRate: 5
                redis-rate-limiter.burstCapacity: 10

```

这里的`replenishRate`表示每秒允许的请求数，`burstCapacity`表示在短时间内允许的最大请求数。

**步骤 3**: 实现KeyResolver

创建一个Bean来定义如何解析限流的key。在这个例子中，我们根据客户端IP地址进行限流：

```
import org.springframework.cloud.gateway.filter.ratelimit.KeyResolver;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;

@Configuration
public class RateLimiterConfig {<!-- -->

    @Bean
    KeyResolver ipKeyResolver() {<!-- -->
        return new KeyResolver() {<!-- -->
            @Override
            public Mono&lt;String&gt; resolve(ServerWebExchange exchange) {<!-- -->
                return Mono.just(exchange.getRequest().getRemoteAddress().getAddress().getHostAddress());
            }
        };
    }
}

```

**步骤 4**: 测试限流策略

启动项目，并向配置了限流规则的服务发送请求。如果请求速率超过了配置的`replenishRate`和`burstCapacity`，则会收到`HTTP 429 Too Many Requests`错误响应。

通过这些步骤，你可以在Spring Cloud Gateway中配置灵活的限流策略，有效防止服务被过度请求，保护系统稳定运行。这种基于Redis的限流机制不仅实现简单，而且支持高并发处理，非常适合微服务架构中的流量管理需求。

### 7.3.4 拓展案例 2：使用 JWT 进行身份验证

在微服务架构中，通过JWT（JSON Web Tokens）进行身份验证可以有效地管理和验证用户和服务的身份。JWT为服务间的安全通信提供了一种简便的方式。在这个案例中，我们将展示如何在Spring Cloud Gateway中集成JWT进行身份验证。

#### 案例 Demo

**步骤 1**: 引入 JWT 依赖

首先，确保你的Spring Boot项目中包含JWT处理库的依赖。这里我们使用`jjwt`库作为示例：

```
&lt;dependency&gt;
    &lt;groupId&gt;io.jsonwebtoken&lt;/groupId&gt;
    &lt;artifactId&gt;jjwt&lt;/artifactId&gt;
    &lt;version&gt;0.9.1&lt;/version&gt;
&lt;/dependency&gt;

```

**步骤 2**: 实现JWT验证过滤器

在API网关中创建一个自定义的全局过滤器，用于解析和验证每个请求中的JWT令牌。如果令牌无效，则拒绝访问。

```
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureException;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.gateway.filter.GatewayFilterChain;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Component;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;

@Component
public class JwtAuthenticationFilter implements GlobalFilter, Ordered {<!-- -->

    @Value("${jwt.secret}")
    private String secretKey;

    @Override
    public Mono&lt;Void&gt; filter(ServerWebExchange exchange, GatewayFilterChain chain) {<!-- -->
        String token = exchange.getRequest().getHeaders().getFirst("Authorization");
        if (token == null || !token.startsWith("Bearer ")) {<!-- -->
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }
        try {<!-- -->
            token = token.substring(7); // Remove Bearer prefix
            Claims claims = Jwts.parser()
                                .setSigningKey(secretKey)
                                .parseClaimsJws(token)
                                .getBody();
            // Optionally, further verification logic here
        } catch (SignatureException e) {<!-- -->
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {<!-- -->
        return -100;
    }
}

```

**步骤 3**: 配置应用密钥

在`application.properties`或`application.yml`中配置JWT的密钥：

```
jwt.secret=YourSecretKeyHere

```

请确保这个密钥与生成JWT时使用的密钥相匹配。

**步骤 4**: 测试JWT身份验证

现在，当你通过API网关访问微服务时，需要在HTTP请求的Header中附加有效的JWT令牌。可以使用Postman或其他HTTP客户端工具来测试这一功能。如果没有提供令牌或令牌无效，网关将拒绝访问并返回HTTP状态码`401 Unauthorized`。

通过上述步骤，Spring Cloud Gateway现在能够利用JWT令牌进行身份验证，从而为微服务架构中的安全通信提供了一层额外的保护。这种方法不仅保障了API的安全性，还提高了系统的可扩展性和维护性。
