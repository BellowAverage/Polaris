
--- 
title:  第6章 Spring Security 的 Web 安全性（2024 最新版） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/20d975288c32413b997ecccdc63081bf.png#pic_center" alt="在这里插入图片描述">



#### 文章目录
- - <ul><li>- <ul><li>- - - - - - - - - - <ul><li>- - - - - - - - - - - - <ul><li>- - - - - - - 


## 6.1 CSRF 防护

跨站请求伪造（CSRF）是一种网络攻击方式，攻击者诱使用户在不知情的情况下，通过用户已登录的Web应用发送恶意请求。幸运的是，通过适当的防护措施，可以有效防止这类攻击。

### 6.1.1 基础知识详解

跨站请求伪造（CSRF）是一种常见的网络攻击，它利用了Web应用中用户会话的自动化完成机制。在不知情的情况下，攻击者可以诱导用户执行非预期的操作，如更改密码、转账等。了解CSRF的基本概念和防护机制对于开发安全的Web应用至关重要。

#### CSRF 攻击原理
1. **用户登录**：用户在某个Web应用中登录，并在其浏览器中保持了登录状态（通常是通过Cookies）。1. **恶意请求**：用户访问了一个恶意网站，该网站包含了一个指向上述Web应用的恶意请求（例如，一个隐藏的表单或者一段JavaScript代码）。1. **自动提交**：由于用户的浏览器仍然保持着对目标Web应用的登录状态，所以恶意请求会自动携带用户的会话Cookies并被提交。1. **非预期操作**：如果目标Web应用没有适当的防护机制，恶意请求就可能以用户的身份执行非预期的操作。
#### CSRF 防护机制
1.  **CSRF 令牌**：最常见的防护机制是使用CSRF令牌（也称为anti-CSRF令牌）。每次用户发起请求时，服务器会生成一个唯一的、不可预测的令牌，并在响应中返回给用户（通常是作为表单的一部分或通过HTTP头发送）。然后，用户在后续请求中必须提交这个令牌，服务器将验证令牌的有效性。 1.  **双重提交Cookies**：这种方法不需要在服务器端存储CSRF令牌。它假定攻击者无法读取或设置目标站点的Cookies。令牌存储在一个Cookie中，并且通过请求（如表单字段）再次提交。服务器验证Cookie中的令牌和请求中的令牌是否匹配。 1.  **自定义请求头**：由于跨站请求通常无法设置自定义请求头，因此检查HTTP请求中是否存在自定义头（如`X-Requested-With`）也是一种简单有效的防护手段。 1.  **Referer验证**：检查HTTP请求的`Referer`头部可以帮助确定请求是否来自于信任的来源。然而，由于隐私考虑，一些用户或浏览器可能会禁用或篡改`Referer`头部，限制了这种方法的有效性。 
#### 最佳实践
- **为所有表单和状态改变请求使用CSRF令牌**：确保每个执行状态改变的请求（如POST、PUT、DELETE等）都需要一个有效的CSRF令牌。- **使用框架提供的CSRF防护**：许多Web框架（如Spring Security）提供了内置的CSRF防护支持，开发者应该充分利用这些特性来保护应用。- **定期旋转CSRF令牌**：定期更换CSRF令牌可以减少令牌被猜测或泄露的风险。- **为CSRF令牌设置适当的作用域**：令牌应该是特定于用户会话的，并且应该限制其在应用中的作用域，以避免跨站点的泄露风险。
通过理解CSRF攻击的工作原理和实施有效的防护措施，开发者可以显著提高Web应用的安全性，保护用户免受这种攻击方式的影响。

### 6.1.2 重点案例：Spring Security 中的 CSRF 防护

Spring Security 提供了一套全面的 CSRF 防护机制，确保应用安全地处理每一个请求。通过实用的案例，我们将一步步探索如何在 Spring Boot 应用中利用 Spring Security 实现 CSRF 防护。

#### 案例 Demo

假设我们正在开发一个简单的博客平台，用户需要登录后才能发布文章。以下是如何通过 Spring Security 添加 CSRF 防护的步骤。

**步骤 1**: 启用 Spring Security

首先，确保你的 Spring Boot 应用中已经添加了 Spring Security 依赖。

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-security&lt;/artifactId&gt;
&lt;/dependency&gt;

```

**步骤 2**: 配置 CSRF 保护

在 Spring Security 配置中，CSRF 保护默认是启用的。但是，为了展示如何显式启用 CSRF 保护，并演示如何配置，我们将在 `WebSecurityConfig` 类中添加相关配置。

```
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->
    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            // 其他配置...
            .csrf().enable(); // 显式启用 CSRF 保护
    }
}

```

**步骤 3**: 在表单中包含 CSRF 令牌

对于每个需要 CSRF 保护的表单，Spring Security 需要你在表单中包含一个 CSRF 令牌。如果你使用的是 Thymeleaf，它会自动为你的表单添加 CSRF 令牌。

```
&lt;form action="/postArticle" method="post"&gt;
    &lt;input type="text" name="title" /&gt;
    &lt;input type="text" name="content" /&gt;
    &lt;!-- Thymeleaf 自动添加 CSRF 令牌 --&gt;
    &lt;button type="submit"&gt;发布文章&lt;/button&gt;
&lt;/form&gt;

```

**步骤 4**: 处理 AJAX 请求中的 CSRF 令牌

对于 AJAX 请求，你需要手动将 CSRF 令牌添加到请求的头部。

首先，从页面中获取 CSRF 令牌（假设你已经将其存储在了一个 meta 标签中）。

```
&lt;meta name="_csrf" content="${_csrf.token}"/&gt;
&lt;meta name="_csrf_header" content="${_csrf.headerName}"/&gt;

```

然后，在发送 AJAX 请求时，从 meta 标签中读取并添加 CSRF 令牌。

```
const csrfToken = document.querySelector('meta[name="_csrf"]').getAttribute('content');
const csrfHeader = document.querySelector('meta[name="_csrf_header"]').getAttribute('content');

fetch('/postArticle', {<!-- -->
    method: 'POST',
    headers: {<!-- -->
        'Content-Type': 'application/json',
        [csrfHeader]: csrfToken // 添加 CSRF 令牌到请求头
    },
    body: JSON.stringify({<!-- -->title: '新文章', content: '文章内容'})
});

```

#### 测试 CSRF 防护

启动应用并尝试发布文章。你会发现，只有当请求中包含有效的 CSRF 令牌时，文章才能成功发布。

通过这个案例，你可以看到 Spring Security 如何帮助我们简单有效地实现 CSRF 防护，从而保护应用免受跨站请求伪造攻击。无论是传统的表单提交还是现代的 AJAX 请求，Spring Security 都为我们提供了强大的工具和机制来确保每个请求的安全。

### 6.1.3 拓展案例 1：自定义 CSRF 令牌仓库

在某些场景下，应用可能需要更灵活地处理 CSRF 令牌，比如在分布式系统中共享 CSRF 令牌或在客户端和服务器之间以不同的方式传递令牌。这时，通过实现自定义 CSRF 令牌仓库（`CsrfTokenRepository`）来满足这些特定需求就显得尤为重要。

#### 案例 Demo

假设我们的应用需要将 CSRF 令牌存储在 Redis 中，以支持在多个实例间共享令牌。以下是如何实现一个自定义的 CSRF 令牌仓库的步骤。

**步骤 1**: 实现 `CsrfTokenRepository`

首先，创建一个新的类 `RedisCsrfTokenRepository` 实现 `CsrfTokenRepository` 接口。这个类将负责从 Redis 获取和存储 CSRF 令牌。

```
public class RedisCsrfTokenRepository implements CsrfTokenRepository {<!-- -->
    private final RedisTemplate&lt;String, CsrfToken&gt; redisTemplate;

    public RedisCsrfTokenRepository(RedisTemplate&lt;String, CsrfToken&gt; redisTemplate) {<!-- -->
        this.redisTemplate = redisTemplate;
    }

    @Override
    public CsrfToken generateToken(HttpServletRequest request) {<!-- -->
        String tokenId = UUID.randomUUID().toString();
        return new DefaultCsrfToken("X-CSRF-TOKEN", "_csrf", tokenId);
    }

    @Override
    public void saveToken(CsrfToken token, HttpServletRequest request, HttpServletResponse response) {<!-- -->
        String key = resolveSessionKey(request);
        if (token == null) {<!-- -->
            redisTemplate.delete(key);
        } else {<!-- -->
            redisTemplate.opsForValue().set(key, token, 30, TimeUnit.MINUTES);
        }
    }

    @Override
    public CsrfToken loadToken(HttpServletRequest request) {<!-- -->
        String key = resolveSessionKey(request);
        return redisTemplate.opsForValue().get(key);
    }

    private String resolveSessionKey(HttpServletRequest request) {<!-- -->
        return "csrf:" + request.getSession().getId();
    }
}

```

**注意**：在实际应用中，你需要配置 `RedisTemplate` 以正确序列化和反序列化 `CsrfToken` 对象。

**步骤 2**: 配置 Spring Security 使用自定义 CSRF 令牌仓库

接下来，在你的 Spring Security 配置中指定应用使用 `RedisCsrfTokenRepository` 作为 CSRF 令牌仓库。

```
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->
    @Autowired
    private RedisTemplate&lt;String, CsrfToken&gt; redisTemplate;

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .csrf()
            .csrfTokenRepository(new RedisCsrfTokenRepository(redisTemplate));
    }
}

```

通过这种方式，应用的 CSRF 令牌将被存储在 Redis 中，支持在多个应用实例间共享令牌，这对于构建可扩展的分布式应用尤为重要。

#### 测试自定义 CSRF 令牌仓库

现在，当用户访问应用并生成 CSRF 令牌时，这些令牌将被存储在 Redis 中。无论用户是通过哪个实例发起请求，应用都能从 Redis 中检索到相应的 CSRF 令牌，并进行验证。

通过实现自定义的 CSRF 令牌仓库，你可以根据应用的具体需求灵活地处理 CSRF 令牌，无论是在客户端和服务器之间自定义传递令牌的方式，还是在分布式系统中共享令牌，都能提供一个安全可靠的解决方案。

### 6.1.4 拓展案例 2：禁用特定请求的 CSRF 防护

虽然 CSRF 防护是保护 Web 应用安全的重要机制，但在某些情况下，你可能需要为特定的请求路径禁用 CSRF 防护。例如，对于某些第三方服务的回调端点或是性能敏感的 API，可能不适合执行 CSRF 检查。Spring Security 提供了灵活的配置选项，允许你根据需要调整 CSRF 防护的范围。

#### 案例 Demo

假设我们有一个应用，其中包含一个第三方支付服务的回调端点 `/payment/notify`，由于这个端点是由支付服务提供商直接调用的，用户不会直接与之交互，因此我们可以安全地为这个特定路径禁用 CSRF 防护。

**步骤 1**: 配置 Spring Security

在 Spring Security 的配置类中，使用 `ignoringAntMatchers()` 方法指定需要禁用 CSRF 防护的路径。

```
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .csrf()
            .ignoringAntMatchers("/payment/notify") // 禁用 /payment/notify 端点的 CSRF 防护
            .and()
            .authorizeRequests()
            .antMatchers("/payment/notify").permitAll() // 允许所有用户无需认证即可访问
            .anyRequest().authenticated(); // 其他所有请求都需要认证
    }
}

```

通过这种配置，`/payment/notify` 端点将不再要求请求中包含 CSRF 令牌，同时允许未经认证的用户访问，确保支付服务的回调请求能够成功到达并被处理。

**步骤 2**: 处理回调请求

接下来，实现一个控制器来处理 `/payment/notify` 端点的请求。

```
@RestController
public class PaymentController {<!-- -->

    @PostMapping("/payment/notify")
    public ResponseEntity&lt;String&gt; paymentNotification(@RequestBody PaymentNotification notification) {<!-- -->
        // 处理支付通知逻辑
        return ResponseEntity.ok("Payment processed");
    }
}

```

#### 测试禁用 CSRF 防护

启动应用后，尝试向 `/payment/notify` 端点发送一个 POST 请求，即使请求中不包含 CSRF 令牌，请求也应该成功被接受和处理。

通过在特定场景下禁用 CSRF 防护，你可以为需要与外部系统交互的端点提供灵活性，同时仍然保持应用的安全性。重要的是，这种配置应谨慎使用，确保不会意外地为敏感操作禁用了 CSRF 防护，从而降低安全风险。

通过这些案例，你可以看到 CSRF 防护是网络安全中的重要组成部分，Spring Security 提供了强大而灵活的机制来保护应用免受 CSRF 攻击。正确实施 CSRF 防护措施，可以有效提升应用的安全性。

## 6.2 跨域请求处理（CORS）

在构建现代 Web 应用时，跨域资源共享（CORS）是一个常见的挑战。CORS 是一种机制，它允许限制的资源（如字体、JavaScript 等）在一个网页应用被另一个不同源（域名、协议或端口）的网页请求时，如何被请求。理解和合理配置 CORS 对于保护 Web 应用、提供灵活的服务消费体验至关重要。

### 6.2.1 基础知识详解

跨域资源共享（CORS）是一个 W3C 标准，允许网页脚本能够向不同源（域、协议或端口）的服务器发出请求，从而克服了 AJAX 直接由浏览器同源政策所施加的限制。在深入探讨如何在应用中实现和配置 CORS 之前，了解其基础知识和工作原理是非常重要的。

#### 同源政策
- **定义**：同源政策是一种约定，它限制了一个源的文档或脚本如何与另一个源的资源进行交互。这是一个重要的安全机制，用于隔离潜在恶意文件。- **源的定义**：源是由协议、域名和端口三部分组成的。只有当这三部分完全匹配时，两个 URL 才属于同一个源。
#### CORS 工作原理
<li> **简单请求**： 
  <ul>- 满足特定条件的请求被视为简单请求（例如使用 GET、HEAD 或 POST 方法，且 HTTP 头部限于一组特定集合）。- 浏览器直接发出简单请求，但会在请求头中添加 `Origin` 字段，服务器根据这个字段决定是否允许该跨域请求。
**预检请求（Preflight）**：
- 不符合简单请求条件的请求，浏览器会先发送一个预检请求，使用 OPTIONS 方法，询问服务器是否允许该跨域请求。- 预检请求的响应中，服务器可以指定允许的方法、头部信息和是否允许携带凭证等信息。
#### CORS 响应头
- **Access-Control-Allow-Origin**：指定哪些网站可以参与跨域资源共享。- **Access-Control-Allow-Methods**：指明在实际请求中允许使用的 HTTP 方法。- **Access-Control-Allow-Headers**：指明实际请求中允许携带的首部字段。- **Access-Control-Allow-Credentials**：指明是否允许发送 Cookie。- **Access-Control-Max-Age**：指明预检请求的结果能够被缓存多久。
#### 实现 CORS 支持
- **服务器端配置**：服务器需要正确处理和响应跨域请求，包括处理预检请求并在响应中设置适当的 CORS 相关头部。- **客户端支持**：在发起跨域 AJAX 请求时，客户端（如 Web 浏览器）将自动处理 CORS 流程，开发者需要确保请求符合 CORS 要求，可能需要设置特定的请求头。
#### 安全考虑
- **精确配置**：`Access-Control-Allow-Origin` 不应该设置为 `*`（表示接受任意域的请求），除非资源完全公开。对于需要凭证的请求，这个值必须是请求页面的完整源，不可以使用 `*`。- **限制方法和头部**：仅允许应用所需的方法和头部，减少潜在的攻击面。
CORS 的正确实现和配置对于保护 Web 应用的安全、提供跨域服务至关重要。理解其基础知识有助于开发者在保障安全的同时，实现应用的灵活访问和资源共享。

### 6.2.2 重点案例：在 Spring Boot 应用中配置 CORS

在这个案例中，我们将通过一个 Spring Boot 应用来展示如何灵活地配置 CORS，使得前端应用能够安全地跨域请求后端资源。我们假设后端API托管在 `https://api.example.com`，而前端应用运行在 `https://app.example.com`。

#### 案例 Demo

**步骤 1**: 全局 CORS 配置

全局配置是一种简单且通用的方式来设置 CORS，适用于整个 Spring Boot 应用。在 `WebSecurityConfig` 类中通过重写 `configure(HttpSecurity http)` 方法实现。

```
@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            // 其他安全配置...
            .cors(cors -&gt; cors
                .configurationSource(request -&gt; {<!-- -->
                    CorsConfiguration config = new CorsConfiguration();
                    config.setAllowedOrigins(List.of("https://app.example.com"));
                    config.setAllowedMethods(List.of("GET", "POST", "PUT", "DELETE"));
                    config.setAllowedHeaders(List.of("Content-Type", "Authorization"));
                    config.setAllowCredentials(true);
                    return config;
                })
            );
    }
}

```

这段代码中，我们为来自 `https://app.example.com` 的请求配置了 CORS，允许了常用的 HTTP 方法，并允许携带认证信息（如 Cookies 和 HTTP 认证）。

**步骤 2**: 控制器级别的 CORS 配置

如果你想对特定的控制器或请求映射进行更细粒度的 CORS 配置，可以使用 `@CrossOrigin` 注解。

```
@RestController
@RequestMapping("/api")
public class DataController {<!-- -->

    @CrossOrigin(origins = "https://app.example.com", methods = {<!-- -->RequestMethod.GET, RequestMethod.POST}, maxAge = 3600)
    @GetMapping("/data")
    public ResponseEntity&lt;String&gt; getData() {<!-- -->
        return ResponseEntity.ok("Data from backend");
    }
}

```

在这个例子中，`/api/data` 端点专门为 `https://app.example.com` 配置了 CORS，允许 GET 和 POST 请求，并设置了预检请求的缓存时间为 3600 秒。

**步骤 3**: 使用 `WebMvcConfigurer` 自定义 CORS 配置

对于需要更复杂的 CORS 配置，例如根据请求动态决定允许的源，可以实现 `WebMvcConfigurer` 接口并重写 `addCorsMappings` 方法。

```
@Configuration
public class WebConfig implements WebMvcConfigurer {<!-- -->

    @Override
    public void addCorsMappings(CorsRegistry registry) {<!-- -->
        registry.addMapping("/api/**")
                .allowedOrigins("https://app.example.com")
                .allowedMethods("GET", "POST", "PUT", "DELETE")
                .allowedHeaders("Content-Type", "Authorization")
                .allowCredentials(true)
                .maxAge(3600);
    }
}

```

这种方法提供了对 CORS 配置全面的控制，允许你针对不同的路径模式定义不同的策略。

#### 测试 CORS 配置

启动你的 Spring Boot 应用后，可以使用前端 JavaScript 代码或者 Postman 发起跨域请求测试 CORS 配置是否生效。例如，从 `https://app.example.com` 页面上发起对 `https://api.example.com/api/data` 的 AJAX 请求，应该能够成功获取数据而不会遇到 CORS 错误。

通过上述案例，你可以看到在 Spring Boot 应用中配置 CORS 的多种方式。这些配置确保了后端服务能够安全地响应来自不同源的前端请求，同时保持了应用的灵活性和安全性。

### 6.2.3 拓展案例 1：自定义 CORS 配置

在复杂的应用架构中，有时需要更灵活地处理跨域请求，比如基于请求的某些特征（例如域名、路径或其他条件）动态允许或拒绝跨域访问。Spring 提供了强大的机制来实现这种自定义 CORS 配置。下面的案例演示了如何根据请求动态配置 CORS。

#### 案例 Demo

假设我们的 Spring Boot 应用需要根据不同的客户端应用动态允许跨域请求，我们可以通过实现 `CorsConfigurationSource` 接口来达到目的。

**步骤 1**: 实现 `CorsConfigurationSource`

创建 `CustomCorsConfigurationSource` 类来实现 `CorsConfigurationSource` 接口。在这个类中，我们将根据请求的来源动态决定 CORS 配置。

```
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;
import javax.servlet.http.HttpServletRequest;
import java.util.Arrays;

public class CustomCorsConfigurationSource implements CorsConfigurationSource {<!-- -->
    
    @Override
    public CorsConfiguration getCorsConfiguration(HttpServletRequest request) {<!-- -->
        CorsConfiguration config = new CorsConfiguration();
        
        String origin = request.getHeader("Origin");
        if ("https://trusted.example.com".equals(origin)) {<!-- -->
            config.setAllowedOrigins(Arrays.asList("https://trusted.example.com"));
            config.setAllowedMethods(Arrays.asList("GET", "POST"));
            config.setAllowedHeaders(Arrays.asList("Content-Type", "Authorization"));
            config.setAllowCredentials(true);
        } else {<!-- -->
            config.setAllowedOrigins(Arrays.asList("https://other.example.com"));
            config.setAllowedMethods(Arrays.asList("GET"));
            // Limit other origins to less sensitive operations
        }
        
        return config;
    }
}

```

在这个例子中，我们根据请求头中的 `Origin` 动态设置了不同的 CORS 策略。对于来自 `https://trusted.example.com` 的请求，我们允许了更多的方法和头部，同时允许凭证。对于其他来源，则应用了更严格的限制。

**步骤 2**: 配置 Spring Security 使用自定义 CORS 配置

接下来，需要在 Spring Security 配置中注册 `CustomCorsConfigurationSource`。

```
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .cors().configurationSource(new CustomCorsConfigurationSource())
            .and()
            .authorizeRequests()
                .anyRequest().authenticated();
    }
}

```

通过 `.cors().configurationSource(new CustomCorsConfigurationSource())`，我们告诉 Spring Security 使用我们自定义的 CORS 配置逻辑。

#### 测试自定义 CORS 配置

启动应用并尝试从 `https://trusted.example.com` 和其他源发起跨域请求，你将看到 CORS 响应头和行为根据请求的来源而有所不同。

这种自定义 CORS 配置方式提供了极高的灵活性，允许开发者基于复杂的业务逻辑来动态决定如何处理跨域请求。它对于需要精细控制跨域策略的大型或安全敏感的应用尤为有用。

### 6.2.4 拓展案例 2：动态 CORS 配置

在一些特定场景下，静态的 CORS 配置可能无法满足需求，例如，当你需要根据数据库中存储的客户端信息或其他动态数据源来决定是否允许跨域请求时。这就需要一种机制来实现动态的 CORS 配置。以下案例将演示如何在 Spring Boot 应用中实现这种动态 CORS 配置。

#### 案例 Demo

假设我们的 Spring Boot 应用需要根据数据库中存储的信息来动态决定是否允许来自特定来源的跨域请求。

**步骤 1**: 创建动态 CORS 配置服务

首先，创建一个服务 `DynamicCorsConfigurationService`，该服务负责根据业务逻辑动态生成 `CorsConfiguration`。

```
import org.springframework.stereotype.Service;
import org.springframework.web.cors.CorsConfiguration;

@Service
public class DynamicCorsConfigurationService {<!-- -->

    // 假设有一个方法从数据库或其他数据源获取允许的来源列表
    public List&lt;String&gt; getAllowedOrigins() {<!-- -->
        // 这里简化为硬编码，实际应用中应从数据库等动态数据源获取
        return Arrays.asList("https://example.com", "https://example2.com");
    }

    public CorsConfiguration getCorsConfiguration() {<!-- -->
        CorsConfiguration config = new CorsConfiguration();
        config.setAllowedOrigins(getAllowedOrigins());
        config.setAllowedMethods(Arrays.asList("GET", "POST", "PUT", "DELETE"));
        config.setAllowedHeaders(Arrays.asList("Content-Type", "Authorization"));
        config.setAllowCredentials(true);
        return config;
    }
}

```

**步骤 2**: 实现 `CorsConfigurationSource` 接口

接下来，实现 `CorsConfigurationSource` 接口，使用上一步创建的服务来动态生成 CORS 配置。

```
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;
import javax.servlet.http.HttpServletRequest;

public class CustomCorsConfigurationSource implements CorsConfigurationSource {<!-- -->

    private final DynamicCorsConfigurationService corsConfigurationService;

    public CustomCorsConfigurationSource(DynamicCorsConfigurationService service) {<!-- -->
        this.corsConfigurationService = service;
    }

    @Override
    public CorsConfiguration getCorsConfiguration(HttpServletRequest request) {<!-- -->
        return corsConfigurationService.getCorsConfiguration();
    }
}

```

**步骤 3**: 配置 Spring Security 使用自定义 CORS 配置源

最后，在 Spring Security 配置中注册你的自定义 CORS 配置源。

```
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Autowired
    private DynamicCorsConfigurationService corsConfigurationService;

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .cors()
            .configurationSource(new CustomCorsConfigurationSource(corsConfigurationService))
            .and()
            .authorizeRequests()
                .anyRequest().authenticated();
    }
}

```

#### 测试动态 CORS 配置

启动应用并尝试从配置的允许来源列表中的域发起跨域请求。你将看到，只有来自这些允许来源的请求才会成功，其他的跨域请求将被拒绝。

通过实现动态 CORS 配置，你可以根据应用的实时需求或策略来灵活控制跨域请求的处理，使得应用更加安全和可控。这种方法特别适用于需要根据用户、时间或其他业务逻辑动态调整跨域策略的场景。

通过这些案例，你可以看到在 Spring Boot 应用中处理 CORS 的多种方式，从简单的注解到复杂的动态配置，Spring 提供了灵活的工具来满足不同场景下的跨域请求需求。正确配置 CORS 不仅可以提升应用的安全性，还可以确保良好的用户体验和服务的可用性。

## 6.3 安全头部和内容安全策略

在现代Web开发中，确保应用的安全性不仅仅是关注数据保护，还包括预防各种网络攻击，比如跨站脚本（XSS）、点击劫持等。为了加强Web应用的安全性，HTTP提供了一系列安全相关的响应头部。其中，内容安全策略（CSP）是一个强大的工具，它允许网站管理者控制页面上可以加载和执行的资源。

### 6.3.1 基础知识详解

在构建Web应用时，确保通信的安全性和防护潜在的客户端攻击是至关重要的。通过利用各种HTTP安全头部和内容安全策略（CSP），开发者可以增加额外的安全层来保护应用和用户。这些机制能够帮助减少和缓解跨站脚本攻击（XSS）、点击劫持、内容混淆等安全威胁。

#### HTTP 安全响应头
<li> **Strict-Transport-Security (HSTS)**: 
  1. 强制客户端（如浏览器）通过HTTPS连接到服务器，减少中间人攻击的风险。1. 示例：`Strict-Transport-Security: max-age=31536000; includeSubDomains` </li><li> **X-Content-Type-Options**: 
  1. 阻止浏览器根据响应的内容或其URL猜测和更改MIME类型，从而阻止MIME类型混淆攻击。1. 示例：`X-Content-Type-Options: nosniff` </li><li> **X-Frame-Options**: 
  1. 指定页面是否可以在`&lt;frame&gt;`, `&lt;iframe&gt;`, `&lt;embed&gt;` 或 `&lt;object&gt;` 中展示，防止点击劫持攻击。1. 示例：`X-Frame-Options: DENY` 或 `X-Frame-Options: SAMEORIGIN` </li><li> **X-XSS-Protection**: 
  1. 启用某些版本的Internet Explorer内置的反射型XSS过滤器。1. 示例：`X-XSS-Protection: 1; mode=block` </li><li> **Content-Security-Policy (CSP)**: 
  1. CSP是一种用于指定哪些动态资源是被允许执行或加载的额外安全层。通过限制资源来源，CSP有助于防止XSS攻击。1. 示例：`Content-Security-Policy: default-src 'self'` </li>- 阻止浏览器根据响应的内容或其URL猜测和更改MIME类型，从而阻止MIME类型混淆攻击。- 示例：`X-Content-Type-Options: nosniff`- 启用某些版本的Internet Explorer内置的反射型XSS过滤器。- 示例：`X-XSS-Protection: 1; mode=block`
#### 内容安全策略（CSP）

CSP允许网站管理员控制页面上可以加载和执行的资源，是防止XSS攻击的强大工具。通过定义一个或多个策略，开发者可以精确指定哪些类型的资源（如脚本、样式表、图片、视频等）可以从哪些来源加载。
<li>**指令**: 
  <ul>- CSP包含多种指令，如`default-src`, `script-src`, `style-src`, `img-src`, `connect-src`等，每种指令控制不同类型资源的加载策略。- 每个指令可以指定允许的来源，如 `'self'`（仅允许来自同一来源的资源）、特定域名、或 `'none'`（不允许加载任何资源）。- CSP还提供了一种报告机制，允许浏览器将违反策略的报告发送到指定的URI，帮助开发者监控和调整CSP策略。
通过合理配置和使用这些安全响应头部和CSP，开发者可以显著提高Web应用的安全性，保护用户免受多种网络攻击。理解和实施这些安全措施是现代Web开发的重要组成部分，对于构建安全可靠的应用至关重要。

### 6.3.2 重点案例：在 Spring Boot 应用中实现 CSP

内容安全策略（CSP）是一个重要的网络安全标准，它帮助网站管理者限制网页上可以加载和执行的资源。通过实施CSP，可以有效防止跨站脚本攻击（XSS）等安全威胁。以下案例展示了如何在Spring Boot应用中实施CSP。

#### 案例 Demo

假设我们的Spring Boot应用需要增加CSP来提升安全性，以下步骤展示了如何通过Spring Security配置CSP。

**步骤 1**: 配置Spring Security

首先，确保Spring Security已经加入到你的项目依赖中。然后，在Spring Security配置类中添加CSP的设置。

```
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            // 其他安全配置...
            .headers()
                .contentSecurityPolicy("default-src 'self'; script-src 'self' https://trustedscripts.example.com; object-src 'none';")
                .reportOnly(true); // 将此行注释以在生产中强制执行CSP
    }
}

```

在这个配置中，我们指定了几个CSP指令：
- `default-src 'self'`: 默认只允许从相同的源加载所有内容。- `script-src 'self' https://trustedscripts.example.com`: 仅从相同的源和`trustedscripts.example.com`加载脚本。- `object-src 'none'`: 不允许加载任何插件内容（如Flash）。
我们还使用了`.reportOnly(true)`将策略设置为仅报告模式，这对于测试和调试CSP非常有用，因为它不会阻止任何内容，而是向指定的报告URI发送违规报告。

**步骤 2**: 添加CSP报告端点

为了收集CSP违规报告，你需要设置一个端点来接收和处理这些报告。

```
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CspReportController {<!-- -->

    @PostMapping("/csp-report")
    public void cspReport(@RequestBody String cspReport) {<!-- -->
        // 在这里处理CSP违规报告，例如记录到日志或数据库
        System.out.println("CSP Report: " + cspReport);
    }
}

```

在生产环境中，你可能希望将这些报告存储在日志文件或数据库中，以便进一步分析。

#### 测试 CSP 配置

启动你的Spring Boot应用，并访问你的网页。如果有任何资源违反了CSP策略（在非仅报告模式下），浏览器将阻止它们并在开发者工具的控制台中显示相关信息。在仅报告模式下，违规内容不会被阻止，但相关违规信息将发送到你配置的报告端点。

通过上述步骤，你可以在Spring Boot应用中实施CSP，显著提高应用的安全性，防止跨站脚本攻击等常见的网络安全威胁。正确配置和测试CSP对于确保Web应用安全至关重要。

### 6.3.3 拓展案例 1：动态加载 CSP

在某些场景下，静态的内容安全策略（CSP）可能无法满足所有需求，特别是在内容或策略需要根据不同用户、页面或其他动态因素变化的复杂应用中。动态加载CSP允许开发者在运行时根据请求的上下文动态构建和应用CSP策略。以下案例演示了如何在Spring Boot应用中实现动态加载CSP。

#### 案例 Demo

假设我们需要根据用户的角色或页面内容动态更改CSP策略，我们可以通过实现`Filter`接口来达到目的。

**步骤 1**: 创建一个自定义过滤器

首先，创建一个自定义的Spring `Filter`，在这个过滤器中，我们将根据请求的特定属性动态设置CSP。

```
import javax.servlet.*;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class DynamicCspFilter implements Filter {<!-- -->

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {<!-- -->
        HttpServletResponse httpServletResponse = (HttpServletResponse) response;
        
        // 示例：根据请求动态设置CSP
        String cspPolicy = "default-src 'self'";
        // 这里可以添加逻辑来根据请求动态决定CSP策略
        // 例如，根据用户角色、请求的页面等因素
        
        httpServletResponse.setHeader("Content-Security-Policy", cspPolicy);
        
        chain.doFilter(request, response);
    }

    @Override
    public void init(FilterConfig filterConfig) {<!-- -->}

    @Override
    public void destroy() {<!-- -->}
}

```

**步骤 2**: 注册过滤器

接下来，需要在Spring Boot应用中注册这个过滤器。这可以通过在一个配置类中定义一个`FilterRegistrationBean`来实现。

```
import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class WebConfig {<!-- -->

    @Bean
    public FilterRegistrationBean&lt;DynamicCspFilter&gt; dynamicCspFilter(){<!-- -->
        FilterRegistrationBean&lt;DynamicCspFilter&gt; registrationBean = new FilterRegistrationBean&lt;&gt;();
        registrationBean.setFilter(new DynamicCspFilter());
        registrationBean.addUrlPatterns("/*"); // 应用于所有请求
        return registrationBean;
    }
}

```

通过这种方式，每次请求都会经过`DynamicCspFilter`，根据过滤器中的逻辑动态设置CSP策略。

#### 测试动态 CSP

启动Spring Boot应用，并尝试访问不同的页面或使用不同用户角色登录，根据`DynamicCspFilter`中的逻辑，你应该能看到不同的CSP策略被应用到不同的响应中。可以通过浏览器的开发者工具查看每个响应的`Content-Security-Policy`头部，确认动态CSP是否按预期工作。

这种动态加载CSP的方法为开发者提供了极高的灵活性，使得可以根据应用的实际运行环境和需求灵活地调整和应用CSP策略，进一步增强了Web应用的安全性。

### 6.3.4 拓展案例 2：使用 CSP 报告 URI

内容安全策略（CSP）提供了一种机制，允许开发者指定一个报告URI，浏览器会将所有违反CSP的报告发送到这个地址。通过分析这些报告，开发者可以调整和优化CSP策略，提高网站的安全性。以下案例演示了如何在Spring Boot应用中设置CSP报告URI，并处理收到的CSP违规报告。

#### 案例 Demo

**步骤 1**: 配置CSP报告URI

首先，在Spring Security配置中添加CSP头部，并指定报告URI。这里，我们使用`/csp-report`作为报告接收端点。

```
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .headers()
                .contentSecurityPolicy("default-src 'self'; report-uri /csp-report;")
            .and()
            .authorizeRequests()
                .anyRequest().authenticated();
    }
}

```

在这个配置中，我们设置了CSP策略`default-src 'self';`，这意味着所有的资源都必须来自同一个源，同时指定了违规报告发送到`/csp-report`。

**步骤 2**: 实现报告接收端点

接下来，需要创建一个控制器来处理收到的CSP违规报告。CSP报告通常以JSON格式发送，因此我们可以通过`@RequestBody`注解接收这些报告。

```
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CspReportController {<!-- -->

    @PostMapping("/csp-report")
    public ResponseEntity&lt;Void&gt; receiveCspReport(@RequestBody String reportJson) {<!-- -->
        // 处理CSP违规报告，例如记录到日志或存储到数据库
        System.out.println("Received CSP report: " + reportJson);
        return ResponseEntity.ok().build();
    }
}

```

**步骤 3**: 测试CSP报告功能

一旦配置完成，你可以通过故意违反CSP策略来测试这个功能，比如尝试从不同的源加载资源。违反CSP的行为会被浏览器捕捉并发送报告到`/csp-report`。你可以检查应用的日志来确认是否成功接收到了CSP违规报告。

#### 分析和使用 CSP 报告

收集和分析CSP报告对于理解和改进你的CSP策略至关重要。通过定期审查这些报告，你可以发现潜在的安全问题或不必要的资源限制，并据此调整CSP策略，以确保既安全又不影响用户体验。

此外，你还可以考虑使用专门的CSP报告处理和分析工具，或将报告存储到数据库中，以便进行更深入的分析和监控。

通过在Spring Boot应用中实现和使用CSP报告URI，开发者可以获得宝贵的反馈信息，帮助优化CSP策略，从而提高Web应用的安全性。

通过上述案例，你可以看到通过实施严格的安全头部和CSP策略，以及监控和处理CSP违规报告，能够显著提升应用的安全性，防止各种网络攻击，保护用户信息安全。这些策略和工具为开发者提供了强大的安全防护能力，是现代Web应用安全不可或缺的一部分。
