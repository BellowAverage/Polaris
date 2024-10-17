
--- 
title:  第5章 Spring Security 的高级认证技术（2024 最新版） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/3170fe0496a748aa9fe7d945010434b3.png#pic_center" alt="在这里插入图片描述">



#### 文章目录
- - <ul><li>- <ul><li>- - - - - - - - - - - - <ul><li>- - - - - - - <ul><li>- - <ul><li>- - - - - - 


## 5.1 OAuth2 和 OpenID Connect

在现代应用开发中，OAuth2 和 OpenID Connect (OIDC) 是保护资源和身份验证的关键技术。让我们先深入了解一下这两种技术的基础，然后通过实用案例来探索它们在实际开发中的应用。

### 5.1.1 基础知识详解

在深入探讨具体案例之前，让我们对 OAuth2 和 OpenID Connect (OIDC) 的基础知识进行更详尽的解析。这两个协议在现代网络安全和身份验证中扮演着至关重要的角色，为用户提供了一种安全、高效的方式来访问和分享他们在不同服务中的资源和信息。

#### OAuth2

OAuth2 是一个开放标准的授权协议，它允许第三方应用代表用户安全地执行操作，而无需用户共享其登录凭据。OAuth2 的设计围绕四种角色展开：
1. **资源所有者**：通常指的是用户，控制其数据的访问权限。1. **客户端**：尝试代表资源所有者访问其在资源服务器上的受保护资源的第三方应用。1. **资源服务器**：托管用户数据的服务器，响应客户端的资源请求。1. **授权服务器**：验证资源所有者的身份并发放令牌给客户端，允许其访问资源服务器上的资源。
OAuth2 定义了四种授权流程，以适应不同的客户端类型和安全需求：
- **授权码模式**：适用于有自己后端服务的客户端，是最常用的流程。- **隐式授权模式**：适用于纯前端应用，如单页应用（SPA）。- **密码凭证模式**：允许用户直接向客户端提供其用户名和密码。- **客户端凭证模式**：适用于客户端访问自己的资源，无需代表用户行动。
#### OpenID Connect

OpenID Connect 建立在 OAuth2 的基础上，是一个身份层，提供了用户身份验证的标准协议。它扩展了 OAuth2，允许客户端除了获取用户授权的资源访问令牌外，还能获取用户的身份信息。OIDC 引入了以下几个关键概念：
- **ID 令牌（ID Token）**：一个 JWT，包含了用户的身份信息。- **用户信息端点（UserInfo Endpoint）**：客户端可以使用访问令牌查询此端点以获取关于用户的更多信息。- **认证服务器（Authorization Server）**：验证用户身份并向客户端发放 ID 令牌和访问令牌。
OIDC 通过提供一个标准化的身份层，使得开发者能够在全球范围内实现互操作性强、安全可靠的用户身份验证解决方案。

#### 结合 OAuth2 和 OIDC

结合 OAuth2 和 OIDC 不仅可以安全地授权第三方应用访问用户资源，还能验证用户的身份，这对于构建现代应用而言至关重要。这两个协议提供的机制，如令牌和授权流程，为用户提供了一个无缝且安全的登录体验，同时也保护了用户的数据安全。

通过掌握这些基础知识，开发者可以更好地理解如何利用 OAuth2 和 OpenID Connect 来构建安全、符合行业标准的认证和授权机制。接下来，我们将通过具体的案例来探索如何在实际开发中应用这些协议。

### 5.1.2 重点案例：使用 OAuth2 和 OpenID Connect 实现社交登录

在这个案例中，我们将探索如何利用 Spring Security 5 支持的 OAuth2 和 OpenID Connect 来实现 Google 社交登录，从而让用户能够使用他们的 Google 账户在我们的应用中登录。

#### 案例 Demo

**步骤 1**: 添加依赖

首先，确保你的 `pom.xml` 包含 Spring Security 5 和 OAuth2 客户端的依赖。

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-oauth2-client&lt;/artifactId&gt;
&lt;/dependency&gt;

```

**步骤 2**: 配置 OAuth2 客户端

在 `application.yml` 或 `application.properties` 文件中，配置 Google 作为 OAuth2 提供者的相关信息。你需要在 Google Cloud Platform 上创建一个 OAuth2 客户端，并获取客户端 ID 和密钥。

```
spring:
  security:
    oauth2:
      client:
        registration:
          google:
            clientId: &lt;YOUR_CLIENT_ID&gt;
            clientSecret: &lt;YOUR_CLIENT_SECRET&gt;
            scope:
              - email
              - profile

```

**步骤 3**: 创建授权和回调控制器

虽然 Spring Security 和 OAuth2 客户端的自动配置已经处理了大部分工作，但你可能仍然需要创建一个控制器来处理登录成功后的逻辑，例如重定向用户或提取用户信息。

```
@Controller
public class OAuth2LoginController {<!-- -->

    @GetMapping("/loginSuccess")
    public String getLoginInfo(OAuth2AuthenticationToken authentication) {<!-- -->
        OAuth2AuthorizedClientService authorizedClientService; // 假设已注入
        OAuth2AuthorizedClient client = authorizedClientService.loadAuthorizedClient(
                authentication.getAuthorizedClientRegistrationId(), authentication.getName());

        String userInfoEndpointUri = client.getClientRegistration()
                .getProviderDetails().getUserInfoEndpoint().getUri();

        if (!StringUtils.isEmpty(userInfoEndpointUri)) {<!-- -->
            RestTemplate restTemplate = new RestTemplate();
            HttpHeaders headers = new HttpHeaders();
            headers.add(HttpHeaders.AUTHORIZATION, "Bearer " + client.getAccessToken().getTokenValue());
            HttpEntity&lt;String&gt; entity = new HttpEntity&lt;&gt;("", headers);
            ResponseEntity&lt;Map&gt; response = restTemplate.exchange(userInfoEndpointUri, HttpMethod.GET, entity, Map.class);
            Map userAttributes = response.getBody();
            // 根据 userAttributes 处理用户信息
        }

        return "redirect:/home";
    }
}

```

在这个控制器中，我们使用 `OAuth2AuthenticationToken` 来获取 `OAuth2AuthorizedClient`，它包含了当前用户的 OAuth2 令牌信息。然后，我们可以使用这个令牌调用用户信息端点来获取用户的详细信息。

**步骤 4**: 配置安全性

确保你的 Spring Security 配置支持 OAuth2 登录，并正确处理登录后的重定向。

```
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .authorizeRequests(authorizeRequests -&gt;
                authorizeRequests
                    .anyRequest().authenticated()
            )
            .oauth2Login(oauth2Login -&gt;
                oauth2Login
                    .loginPage("/login")
                    .defaultSuccessUrl("/loginSuccess", true)
            );
    }
}

```

通过这个配置，Spring Security 会自动处理 OAuth2 登录流程，并在成功认证后重定向到 `/loginSuccess` 路径。

通过实现这个案例，你可以为你的应用添加使用 Google 账户登录的功能，提供一种方便快捷的登录方式，同时也增强了应用的安全性。使用 OAuth2 和 OpenID Connect 实现社交登录，不仅简化了认证流程，还提高了用户体验。

### 5.1.3 拓展案例 1：访问受保护资源

在用户通过 OAuth2 和 OpenID Connect 实现社交登录之后，一个常见的需求是访问用户在社交平台上的受保护资源，比如访问用户的Google日历。在这个案例中，我们将探讨如何使用用户的授权信息来访问这些受保护资源。

#### 案例 Demo

**步骤 1**: 获取用户授权

这一步已经在之前的社交登录案例中完成。在用户成功通过 Google 登录后，应用将获得一个访问令牌（Access Token），这个令牌允许应用代表用户访问其在 Google 的受保护资源。

**步骤 2**: 使用访问令牌访问受保护资源

假设我们想要获取用户的 Google 联系人列表。首先，需要确保在 Google Cloud Platform 上的客户端配置中请求了正确的权限（或作用域），例如 `https://www.googleapis.com/auth/contacts.readonly`。

然后，我们可以使用获取到的访问令牌调用 Google 联系人 API。

```
@RestController
public class GoogleContactsController {<!-- -->

    @Autowired
    private OAuth2AuthorizedClientService authorizedClientService;

    @GetMapping("/contacts")
    public ResponseEntity&lt;List&gt; getGoogleContacts(@AuthenticationPrincipal OAuth2User oauth2User) {<!-- -->
        OAuth2AuthorizedClient client = authorizedClientService
                .loadAuthorizedClient("google", oauth2User.getName());
        String accessToken = client.getAccessToken().getTokenValue();

        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setBearerAuth(accessToken);
        HttpEntity&lt;String&gt; entity = new HttpEntity&lt;&gt;("parameters", headers);

        ResponseEntity&lt;List&gt; response = restTemplate.exchange(
                "https://people.googleapis.com/v1/people/me/connections?personFields=names,emailAddresses",
                HttpMethod.GET, entity, List.class);

        return response;
    }
}

```

在这个控制器中，我们首先从 `OAuth2AuthorizedClientService` 获取到代表用户会话的 `OAuth2AuthorizedClient` 对象，这个对象中包含了当前用户的访问令牌。然后，我们设置一个带有 Bearer 认证头的 HTTP 请求，使用 `RestTemplate` 发送请求到 Google 联系人 API，并返回响应。

**注意**：为了简化示例，这里直接将 `List.class` 作为响应类型。在实际应用中，你可能需要定义一个更具体的类来匹配 API 响应的结构。

#### 测试访问受保护资源

启动应用，确保用户已通过 Google 登录，然后访问 `/contacts` 端点。应用将代表用户调用 Google 联系人 API，并返回用户的联系人列表。

通过这个案例，你可以看到如何在用户授权后，使用 OAuth2 访问令牌来获取用户在第三方服务上的受保护资源。这种能力极大地扩展了应用的功能，使得它们能够为用户提供更加个性化和丰富的服务。

### 5.1.4 拓展案例 2：实现自定义 OIDC 提供者

实现自定义的 OpenID Connect (OIDC) 提供者涉及到创建一个遵循 OpenID Connect 协议的认证服务器，该服务器能够处理认证请求、发放令牌，并提供用户信息。这个过程比较复杂且超出了简单的示例范围，但我可以概述关键步骤和概念，以及如何使用 Spring Security 5 支持的功能来实现它。

#### 概述

实现自定义 OIDC 提供者通常涉及以下几个关键组件：
1. **授权服务器**：负责处理认证和授权请求，发放 ID 令牌和访问令牌。1. **用户信息端点**：提供经过认证的客户端访问用户信息的接口。1. **客户端注册**：允许第三方客户端注册并获取访问授权服务器所需的凭证。
#### 步骤 1: 设置授权服务器

使用 Spring Security OAuth2 Boot 2.x 版本之前，你可以利用其提供的 `@EnableAuthorizationServer` 注解来快速创建一个授权服务器。但在最新的 Spring Security 5 中，推荐的做法是使用外部授权服务器，或者通过手动配置方式来实现 OIDC 功能。

对于自定义 OIDC 提供者，你需要创建几个关键的端点：
- **授权端点**：处理认证请求，生成授权码。- **令牌端点**：交换授权码以获取令牌。- **用户信息端点**：提供用户信息。
#### 步骤 2: 实现用户信息端点

用户信息端点是 OIDC 提供者用来提供用户信息的接口。这通常是一个受保护的 API，只有在提供了有效的访问令牌时才能访问。

```
@RestController
@RequestMapping("/userinfo")
public class UserInfoController {<!-- -->

    @GetMapping
    public Map&lt;String, Object&gt; userInfo(@AuthenticationPrincipal OidcUser user) {<!-- -->
        Map&lt;String, Object&gt; userInfo = new HashMap&lt;&gt;();
        userInfo.put("sub", user.getSubject());
        userInfo.put("name", user.getFullName());
        // 添加更多用户信息
        return userInfo;
    }
}

```

在这个例子中，我们定义了一个简单的用户信息端点，它返回当前用户的一些基本信息。这些信息通常从 `OidcUser` 对象中提取，该对象代表了通过 OIDC 认证的用户。

#### 步骤 3: 配置客户端注册

在自定义 OIDC 提供者中，你需要提供一种机制来注册和管理第三方客户端。这通常涉及到存储客户端ID、客户端密钥和重定向URI等信息。

虽然 Spring Security 框架为客户端注册提供了支持，但在自定义 OIDC 提供者的情况下，你可能需要手动管理这些信息，比如使用数据库来存储客户端详情。

#### 注意

由于 Spring Security 5 放弃了内置的授权服务器支持，如果你需要构建完整的自定义 OIDC 提供者，可能需要依赖额外的库或服务，如 Keycloak，或者使用 Spring Security 的低级 API 自己实现相关功能。

这个拓展案例展示了如何开始构建一个自定义 OIDC 提供者的基础框架。实际上，这是一个复杂的过程，需要深入理解 OAuth2 和 OIDC 协议的细节。对于大多数应用来说，使用现成的解决方案（如 Keycloak 或 Auth0）可能是一个更实用和时间效率更高的选择。

## 5.2 使用 JWT

JSON Web Tokens (JWT) 是一种开放标准（RFC 7519），用于在网络应用环境间安全地传输声明（如认证信息）。JWTs 可以被签名（使用秘密或公钥/私钥对），甚至可以被加密。

### 5.2.1 基础知识详解

在深入探索 JWT 在现代认证机制中的应用之前，让我们先对 JWT 的基础知识进行更全面的解读。JSON Web Tokens（JWT）为在网络应用间安全地传递声明（claims）提供了一种紧凑且自包含的方式。理解 JWT 的结构和工作原理是关键，这将帮助我们更好地利用它在认证和授权过程中的强大功能。

#### JWT 结构

JWT 通常由三部分组成，每部分之间用点（`.`）分隔：
<li> **Header（头部）**: 
  1. 包含了用于处理令牌的元数据，主要是令牌的类型（`typ`，通常是 JWT）和所使用的签名或加密算法（`alg`，例如 HS256、RS256）。1. 示例：`{"alg": "HS256", "typ": "JWT"}`。 </li><li> **Payload（负载）**: 
  1. 包含所要传递的声明，声明是关于实体（通常指用户）和其他数据的陈述。这些声明可以是预定义的、公共的或是私有的。1. 预定义的声明（Registered claims）：如 `iss`（发行者）、`exp`（过期时间）、`sub`（主题）等。1. 示例：`{"sub": "1234567890", "name": "John Doe", "admin": true}`。 </li><li> **Signature（签名）**: 
  1. 通过对 header 和 payload 部分进行编码，然后使用 header 中指定的算法和一个密钥进行签名来生成。1. 签名的目的是为了验证消息的发送者是谁，以及确保消息在传输过程中未被篡改。 </li>- 包含所要传递的声明，声明是关于实体（通常指用户）和其他数据的陈述。这些声明可以是预定义的、公共的或是私有的。- 预定义的声明（Registered claims）：如 `iss`（发行者）、`exp`（过期时间）、`sub`（主题）等。- 示例：`{"sub": "1234567890", "name": "John Doe", "admin": true}`。
#### JWT 的优势和用途
<li> **自包含**: 
  1. JWT 自包含了所有必要的信息，使得它无需回数据库查询即可完成认证和授权过程，这对于分布式微服务架构尤其重要。 </li><li> **跨语言支持**: 
  1. 由于 JWT 是基于 JSON 的，它自然地被各种编程语言支持，这使得 JWT 在多种应用和服务间传递信息成为可能。 </li><li> **性能优异**: 
  1. JWT 由于其自包含性，减少了需要查询数据库的次数，这对于需要高性能和低延迟的应用来说是一个重要优势。 </li><li> **易于传输**: 
  1. JWT 由于其紧凑的结构，可以轻松地通过 URL、POST 参数或者在 HTTP 的 Header 中传输。 </li>- 由于 JWT 是基于 JSON 的，它自然地被各种编程语言支持，这使得 JWT 在多种应用和服务间传递信息成为可能。- JWT 由于其紧凑的结构，可以轻松地通过 URL、POST 参数或者在 HTTP 的 Header 中传输。
#### 安全考虑
- 虽然 JWT 的 Payload 是 Base64 编码的，这意味着它可以被任何人解码并读取，因此不应在 JWT 中包含任何敏感信息，除非它是加密的。- 使用 HTTPS 来防止令牌在传输过程中被拦截。- 确保 JWT 的有效期适当，以减少令牌被盗用的风险。
通过深入了解 JWT 的基础知识，我们为进一步探索如何在实际项目中应用 JWT 奠定了坚实的基础。JWT 不仅能够提高应用的安全性，还能在保持良好用户体验的同时简化认证和授权流程。

### 5.2.2 重点案例：使用 JWT 实现无状态认证

在这个案例中，我们将演示如何在 Spring Boot 应用中使用 JWT 来实现无状态认证机制。这种方式允许应用在无需保存用户会话状态的情况下，安全地识别和授权请求。

#### 案例 Demo

假设我们正在开发一个简单的博客系统，其中用户需要登录后才能创建和编辑文章。以下是实现步骤：

**步骤 1**: 添加 JWT 依赖

首先，向 `pom.xml` 文件中添加 JWT 支持库的依赖，如 `jjwt`。

```
&lt;dependency&gt;
    &lt;groupId&gt;io.jsonwebtoken&lt;/groupId&gt;
    &lt;artifactId&gt;jjwt&lt;/artifactId&gt;
    &lt;version&gt;0.9.1&lt;/version&gt;
&lt;/dependency&gt;

```

**步骤 2**: 创建 JWT 工具类

接下来，创建一个 `JwtUtil` 类来生成和验证 JWT。

```
@Component
public class JwtUtil {<!-- -->
    private String secretKey = "secret"; // 在实际应用中，应从配置文件或环境变量中获取
    private long validityInMilliseconds = 3600000; // 1h

    public String createToken(String username) {<!-- -->
        Claims claims = Jwts.claims().setSubject(username);
        Date now = new Date();
        Date validity = new Date(now.getTime() + validityInMilliseconds);

        return Jwts.builder()
                .setClaims(claims)
                .setIssuedAt(now)
                .setExpiration(validity)
                .signWith(SignatureAlgorithm.HS256, secretKey)
                .compact();
    }

    public String getUsername(String token) {<!-- -->
        return Jwts.parser().setSigningKey(secretKey).parseClaimsJws(token).getBody().getSubject();
    }

    public boolean validateToken(String token) {<!-- -->
        try {<!-- -->
            Jwts.parser().setSigningKey(secretKey).parseClaimsJws(token);
            return true;
        } catch (JwtException | IllegalArgumentException e) {<!-- -->
            throw new IllegalStateException("Expired or invalid JWT token");
        }
    }
}

```

**步骤 3**: 实现 JWT 请求过滤器

创建 `JwtTokenFilter` 类来验证每个请求的 JWT。

```
public class JwtTokenFilter extends OncePerRequestFilter {<!-- -->
    @Autowired
    private JwtUtil jwtUtil;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {<!-- -->
        String token = request.getHeader("Authorization");
        if (token != null &amp;&amp; jwtUtil.validateToken(token)) {<!-- -->
            Authentication auth = new UsernamePasswordAuthenticationToken(jwtUtil.getUsername(token), null, Collections.emptyList());
            SecurityContextHolder.getContext().setAuthentication(auth);
        }
        filterChain.doFilter(request, response);
    }
}

```

**步骤 4**: 配置 Spring Security

配置 Spring Security 以使用我们的 JWT 过滤器。

```
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->
    @Autowired
    private JwtTokenFilter jwtTokenFilter;

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .httpBasic().disable()
            .csrf().disable()
            .sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            .and()
                .authorizeRequests()
                .antMatchers("/login").permitAll()
                .anyRequest().authenticated()
            .and()
                .addFilterBefore(jwtTokenFilter, UsernamePasswordAuthenticationFilter.class);
    }
}

```

**步骤 5**: 实现登录端点

最后，实现一个简单的登录端点，用于验证用户凭据并返回 JWT。

```
@RestController
public class AuthenticationController {<!-- -->
    @Autowired
    private JwtUtil jwtUtil;

    // 假设有一个自定义的方法来验证用户凭据
    @PostMapping("/login")
    public ResponseEntity&lt;?&gt; login(@RequestParam String username, @RequestParam String password) {<!-- -->
        // 验证用户凭据（省略）
        String token = jwtUtil.createToken(username);
        return ResponseEntity.ok(token);
    }
}

```

通过这个案例，你可以看到使用 JWT 实现无状态认证的基本步骤。这种方法不仅提高了应用的安全性，还因其无状态特性，使得应用易于扩展。

### 5.2.3 拓展案例 1：刷新令牌

在实际应用中，为了提高安全性和改善用户体验，通常采用较短的 JWT 有效期，并提供刷新令牌机制来允许用户在访问令牌过期后，无需重新登录即可获取新的访问令牌。刷新令牌通常具有比访问令牌更长的有效期，并且可以用来多次获取新的访问令牌，直到刷新令牌本身过期。

#### 案例 Demo

假设我们正在开发一个博客系统，用户登录后将获得一个访问令牌和一个刷新令牌。

**步骤 1**: 扩展 `JwtUtil` 类

首先，我们需要扩展之前创建的 `JwtUtil` 类，添加生成刷新令牌的方法。

```
public class JwtUtil {<!-- -->
    private String secretKey = "secret"; // 实际应用中应更安全
    private long validityInMilliseconds = 3600000; // 访问令牌有效期: 1小时
    private long refreshTokenValidityInMilliseconds = 28_800_000; // 刷新令牌有效期: 8小时

    // 原有的 createToken 方法...

    public String createRefreshToken(String username) {<!-- -->
        Date now = new Date();
        Date validity = new Date(now.getTime() + refreshTokenValidityInMilliseconds);

        return Jwts.builder()
                .setSubject(username)
                .setIssuedAt(now)
                .setExpiration(validity)
                .signWith(SignatureAlgorithm.HS256, secretKey)
                .compact();
    }

    // 原有的 validateToken 和 getUsernameFromJWT 方法...
}

```

**步骤 2**: 实现刷新令牌的存储

为了跟踪刷新令牌，我们需要在服务器端存储它们。在简单的示例中，可以将刷新令牌存储在内存或数据库中。

```
@Component
public class RefreshTokenStore {<!-- -->
    private final Map&lt;String, String&gt; refreshTokenStore = new ConcurrentHashMap&lt;&gt;();

    public void storeToken(String username, String refreshToken) {<!-- -->
        refreshTokenStore.put(username, refreshToken);
    }

    public String getRefreshToken(String username) {<!-- -->
        return refreshTokenStore.get(username);
    }

    // 添加验证刷新令牌的方法等...
}

```

**步骤 3**: 处理刷新令牌请求

接下来，实现一个端点来处理刷新令牌请求，验证刷新令牌，并发放新的访问令牌。

```
@RestController
public class RefreshTokenController {<!-- -->

    @Autowired
    private JwtUtil jwtUtil;
    @Autowired
    private RefreshTokenStore refreshTokenStore;

    @PostMapping("/refresh")
    public ResponseEntity&lt;?&gt; refreshAuthentication(@RequestParam String refreshToken) {<!-- -->
        // 简化示例，实际应更严格地验证刷新令牌
        String username = jwtUtil.getUsername(refreshToken);
        String storedRefreshToken = refreshTokenStore.getRefreshToken(username);
        if (refreshToken.equals(storedRefreshToken) &amp;&amp; jwtUtil.validateToken(refreshToken)) {<!-- -->
            String newToken = jwtUtil.createToken(username);
            return ResponseEntity.ok(newToken);
        } else {<!-- -->
            return ResponseEntity.status(HttpStatus.FORBIDDEN).body("Invalid refresh token");
        }
    }
}

```

**步骤 4**: 调整登录逻辑

最后，调整登录逻辑以同时发放访问令牌和刷新令牌。

```
@PostMapping("/login")
public ResponseEntity&lt;?&gt; login(@RequestParam String username, @RequestParam String password) {<!-- -->
    // 验证用户凭据（省略）
    String token = jwtUtil.createToken(username);
    String refreshToken = jwtUtil.createRefreshToken(username);
    refreshTokenStore.storeToken(username, refreshToken);
    return ResponseEntity.ok(Map.of("accessToken", token, "refreshToken", refreshToken));
}

```

通过实现刷新令牌机制，你的应用可以提供更安全且用户友好的认证体验，使用户在访问令牌过期后能够轻松地继续访问应用资源，而无需频

繁地重新登录。

### 5.2.4 拓展案例 2：微服务间的 JWT 验证

在基于微服务架构的系统中，服务间的安全通信至关重要。利用 JWT 进行服务间的认证是一种有效的方法，可以确保只有授权的服务能够访问受保护的资源。以下是如何在 Java 中实现微服务间的 JWT 验证的案例。

#### 案例 Demo

假设我们有两个微服务：`ServiceA` 和 `ServiceB`。`ServiceA` 需要调用 `ServiceB` 的受保护接口。

**步骤 1**: 在 `ServiceB` 中验证 JWT

首先，`ServiceB` 需要验证从 `ServiceA` 发来的请求中的 JWT。这可以通过配置一个 JWT 过滤器来完成，类似于前面提到的用户认证过程。

在 `ServiceB` 的 `SecurityConfig` 中配置 JWT 过滤器：

```
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->
    @Autowired
    private JwtTokenFilter jwtTokenFilter;

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .csrf().disable()
            .sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            .and()
                .authorizeRequests()
                .antMatchers("/api/protected").authenticated()
                .anyRequest().permitAll()
            .and()
                .addFilterBefore(jwtTokenFilter, UsernamePasswordAuthenticationFilter.class);
    }
}

```

**步骤 2**: 在 `ServiceA` 中生成 JWT

`ServiceA` 需要生成一个有效的 JWT，用于调用 `ServiceB` 的接口。这个 JWT 可以是由专门的认证服务生成，或者 `ServiceA` 本身生成，具体取决于你的架构设计。

这里假设 `ServiceA` 自行生成 JWT：

```
@Service
public class JwtService {<!-- -->
    public String generateTokenForServiceB() {<!-- -->
        // 生成 JWT 逻辑，可能包括设置特定的 claims，如服务标识
        return jwtUtil.createToken("ServiceA");
    }
}

```

**步骤 3**: `ServiceA` 调用 `ServiceB` 时携带 JWT

当 `ServiceA` 需要调用 `ServiceB` 的受保护接口时，它应在 HTTP 请求的 `Authorization` 头中携带 JWT。

```
@Service
public class ServiceAClient {<!-- -->
    private RestTemplate restTemplate = new RestTemplate();
    @Autowired
    private JwtService jwtService;

    public String callProtectedServiceB() {<!-- -->
        HttpHeaders headers = new HttpHeaders();
        headers.set("Authorization", "Bearer " + jwtService.generateTokenForServiceB());
        HttpEntity&lt;String&gt; entity = new HttpEntity&lt;&gt;(headers);
        
        return restTemplate.exchange(
                "http://ServiceB/api/protected", HttpMethod.GET, entity, String.class).getBody();
    }
}

```

这个简化的例子演示了如何在微服务间使用 JWT 进行安全通信。`ServiceA` 生成一个 JWT 并在调用 `ServiceB` 时将其包含在请求中，而 `ServiceB` 则验证这个 JWT 来确保只有授权的服务可以访问其受保护的接口。

通过实现这种机制，你可以确保你的微服务架构中的服务间通信是安全的，只有拥有正确 JWT 的服务才能访问特定的资源或执行特定的操作。这对于构建可扩展且安全的微服务系统至关重要。

## 5.3 社交登录集成

社交登录集成允许用户使用他们现有的社交媒体账户，如 Facebook、Google 或 Twitter，来直接登录到其他应用或服务中，无需创建新的用户名和密码。这不仅提高了用户体验，还有助于提高注册转化率和用户参与度。

### 5.3.1 基础知识详解

社交登录集成，允许用户使用他们在社交平台上的账户（如 Facebook、Google 或 Twitter）来登录其他在线服务和应用，是现代网络应用中提升用户体验的重要特性。这种认证方式不仅简化了登录过程，还有助于降低新用户注册的门槛。下面是实现社交登录的一些关键基础知识点。

#### 关键组件
<li> **OAuth 2.0**: 
  1. 社交登录的核心是基于 OAuth 2.0 授权框架，它是一个开放标准，用于提供安全的客户端应用访问资源的授权。 </li><li> **OpenID Connect**: 
  1. 在 OAuth 2.0 的基础上，OpenID Connect 为用户身份提供了一个标准化框架。它在 OAuth 2.0 的授权流程中添加了身份层，使得应用能够获取用户的身份信息。 </li>- 在 OAuth 2.0 的基础上，OpenID Connect 为用户身份提供了一个标准化框架。它在 OAuth 2.0 的授权流程中添加了身份层，使得应用能够获取用户的身份信息。
#### OAuth 2.0 和 OpenID Connect 工作流程
<li> **用户选择社交登录**: 
  1. 用户在应用登录页面选择使用社交平台账户登录。 </li><li> **重定向到社交平台**: 
  1. 应用将用户重定向到社交平台的授权页面，请求用户授权应用访问其在该平台上的个人信息。 </li><li> **用户授权**: 
  1. 用户在社交平台上登录（如果尚未登录）并授权应用访问其信息。 </li><li> **授权码交换**: 
  1. 社交平台将用户重定向回应用，并附带一个授权码。应用使用此授权码向社交平台请求访问令牌。 </li><li> **获取用户信息**: 
  1. 应用使用访问令牌调用社交平台的 API，获取用户信息，如姓名和邮箱地址。 </li>- 应用将用户重定向到社交平台的授权页面，请求用户授权应用访问其在该平台上的个人信息。- 社交平台将用户重定向回应用，并附带一个授权码。应用使用此授权码向社交平台请求访问令牌。
##### 实现社交登录的挑战
<li> **配置多个社交登录提供者**: 
  <ul>- 应用可能需要支持多个社交登录平台，每个平台都有其特定的配置要求和流程。
**安全性**:
- 需要确保在整个授权过程中保护用户信息和访问令牌的安全，防止中间人攻击等安全威胁。
**用户数据一致性**:
- 应用需要处理将社交平台返回的用户信息与应用内现有用户记录正确匹配和同步的逻辑。
**用户体验**:
- 社交登录应无缝集成到应用的登录和注册流程中，提供简洁明了的用户界面和指引。
通过深入理解社交登录的基础知识和相关挑战，开发者可以更有效地集成和管理社交登录功能，为用户提供安全、便捷的登录体验，同时确保应用的安全性和用户数据的一致性。

### 5.3.2 重点案例：集成 Google 社交登录

社交登录极大地简化了用户的登录过程，并提高了用户体验。在本案例中，我们将通过实际示例演示如何在 Spring Boot 应用中集成 Google 社交登录。

#### 案例 Demo

**步骤 1**: 添加依赖

为了支持社交登录，首先需要在 `pom.xml` 中添加 Spring Security OAuth2 客户端依赖。

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-oauth2-client&lt;/artifactId&gt;
&lt;/dependency&gt;

```

**步骤 2**: 配置 OAuth2 客户端

在 `application.yml` 文件中配置 Google 作为 OAuth2 客户端。你需要前往 Google Cloud Platform 创建一个 OAuth 2.0 客户端 ID 并获取客户端 ID 和客户端密钥。

```
spring:
  security:
    oauth2:
      client:
        registration:
          google:
            clientId: &lt;YOUR_CLIENT_ID&gt;
            clientSecret: &lt;YOUR_CLIENT_SECRET&gt;
            scope:
              - email
              - profile

```

**步骤 3**: 创建登录控制器

实现一个控制器来处理登录成功后的逻辑。Spring Security 会自动重定向到 `/login/oauth2/code/google` 路径以处理 OAuth2 登录流程，但我们可以定义一个控制器来处理登录成功后的重定向。

```
@Controller
public class SocialLoginController {<!-- -->

    @GetMapping("/loginSuccess")
    public String getLoginInfo(@AuthenticationPrincipal OAuth2User principal, Model model) {<!-- -->
        String name = principal.getAttribute("name");
        model.addAttribute("name", name);
        return "loginSuccess";
    }
}

```

在这个控制器中，`@AuthenticationPrincipal OAuth2User principal` 参数用于接收 OAuth2 登录成功后的用户信息。

**步骤 4**: 配置安全性

确保 Spring Security 配置支持 OAuth2 登录，并正确处理登录成功后的重定向。

```
@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .authorizeRequests(authorizeRequests -&gt;
                authorizeRequests
                    .antMatchers("/", "/error", "/webjars/**").permitAll()
                    .anyRequest().authenticated()
            )
            .oauth2Login(oauth2Login -&gt;
                oauth2Login
                    .loginPage("/login")
                    .defaultSuccessUrl("/loginSuccess", true)
            );
    }
}

```

在这个配置中，`.defaultSuccessUrl("/loginSuccess", true)` 指定了登录成功后的重定向 URL。

#### 测试社交登录

启动应用并访问主页，你应该会看到一个选项让用户通过 Google 账户登录。登录成功后，用户将被重定向到 `/loginSuccess` 路径，并显示用户的名称。

通过这个案例，你可以看到集成 Google 社交登录的基本步骤。这种方法不仅为用户提供了便捷的登录方式，还可以通过用户的社交账户信息来丰富应用的用户体验。

### 5.3.3 拓展案例 1：集成 Facebook 登录

在现代Web应用中，提供多种社交登录选项可以显著提升用户体验。在本案例中，我们将探讨如何在Spring Boot应用中集成Facebook社交登录，以便用户可以使用他们的Facebook账户进行登录。

#### 案例 Demo

**步骤 1**: 添加依赖

确保你的`pom.xml`中已经包含了Spring Security OAuth2客户端依赖。

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-oauth2-client&lt;/artifactId&gt;
&lt;/dependency&gt;

```

**步骤 2**: 配置 OAuth2 客户端

在`application.yml`中配置Facebook作为OAuth2客户端。首先，你需要在创建一个应用，获取客户端ID和客户端密钥。

```
spring:
  security:
    oauth2:
      client:
        registration:
          facebook:
            clientId: &lt;YOUR_FACEBOOK_CLIENT_ID&gt;
            clientSecret: &lt;YOUR_FACEBOOK_CLIENT_SECRET&gt;
            scope:
              - email
              - public_profile

```

**步骤 3**: 创建登录成功控制器

创建一个控制器来处理登录成功后的逻辑。Spring Security将自动处理OAuth2登录流程，我们只需要定义登录成功后的行为。

```
@Controller
public class SocialLoginController {<!-- -->

    @GetMapping("/loginSuccess")
    public String loginSuccess(@AuthenticationPrincipal OAuth2User principal, Model model) {<!-- -->
        String name = principal.getAttribute("name");
        model.addAttribute("name", name);
        // 可以添加更多的用户信息到模型
        return "loginSuccess";
    }
}

```

**步骤 4**: 配置 Spring Security

更新你的Spring Security配置以支持OAuth2登录，并处理登录成功后的重定向。

```
@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .authorizeRequests(authorizeRequests -&gt;
                authorizeRequests
                    .antMatchers("/", "/error", "/webjars/**").permitAll()
                    .anyRequest().authenticated()
            )
            .oauth2Login(oauth2Login -&gt;
                oauth2Login
                    .loginPage("/login")
                    .defaultSuccessUrl("/loginSuccess", true)
            );
    }
}

```

在这个配置中，`.defaultSuccessUrl("/loginSuccess", true)`指定了登录成功后的重定向URL。

#### 测试 Facebook 登录

启动应用并访问主页，你现在应该可以看到一个选项让用户通过Facebook账户登录。登录成功后，用户将被重定向到`/loginSuccess`路径，并可以看到他们的名称等信息。

通过集成Facebook登录，你的应用不仅为用户提供了一种便利的登录方式，还可以利用Facebook提供的丰富用户数据来提升应用的个性化体验。这种社交登录集成方式能够有效提高用户的注册和登录率，从而提升整体的用户参与度。

### 5.3.4 拓展案例 2：自定义用户注册和登录流程

在集成社交登录（如Google或Facebook）后，应用通常需要将社交账户与现有的用户账户系统集成。这可能涉及到在用户首次使用社交账户登录时创建一个新的应用内用户记录，或者将社交账户链接到现有的用户记录。以下是如何在Spring Boot应用中自定义用户注册和登录流程的示例。

#### 案例 Demo

**步骤 1**: 定义用户实体

首先，定义一个用户实体来存储用户信息。在这个实体中，你可以存储用户的基本信息以及与社交账户相关的标识符（如Google的`sub`字段）。

```
@Entity
public class ApplicationUser {<!-- -->
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String username; // 可能是电子邮件地址
    private String name;
    private String googleSub; // 用于存储Google账户的唯一标识符

    // 构造函数、Getter和Setter省略
}

```

**步骤 2**: 实现用户服务

实现一个用户服务来处理用户的创建和查找逻辑。这个服务将检查使用社交账户登录的用户是否已经存在于系统中，并据此创建新用户或更新现有用户记录。

```
@Service
public class UserService {<!-- -->
    @Autowired
    private UserRepository userRepository;

    public ApplicationUser processUserLogin(OAuth2User oAuth2User) {<!-- -->
        String googleSub = oAuth2User.getAttribute("sub"); // 从Google登录信息中获取sub
        ApplicationUser user = userRepository.findByGoogleSub(googleSub);
        if (user == null) {<!-- -->
            user = new ApplicationUser();
            user.setGoogleSub(googleSub);
        }
        user.setUsername(oAuth2User.getAttribute("email"));
        user.setName(oAuth2User.getAttribute("name"));
        return userRepository.save(user);
    }
}

```

**步骤 3**: 自定义OAuth2登录成功处理器

创建一个登录成功处理器，它在用户通过社交账户登录成功后，调用`UserService`来处理用户记录。

```
@Component
public class CustomAuthenticationSuccessHandler extends SavedRequestAwareAuthenticationSuccessHandler {<!-- -->

    @Autowired
    private UserService userService;

    @Override
    public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response,
                                        Authentication authentication) throws ServletException, IOException {<!-- -->
        OAuth2AuthenticationToken authToken = (OAuth2AuthenticationToken) authentication;
        OAuth2User oAuth2User = authToken.getPrincipal();
        ApplicationUser user = userService.processUserLogin(oAuth2User);
        
        // 可以在这里将用户信息添加到会话中
        super.onAuthenticationSuccess(request, response, authentication);
    }
}

```

**步骤 4**: 配置Spring Security使用自定义成功处理器

在Spring Security配置中，指定OAuth2登录成功后使用自定义的成功处理器。

```
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Autowired
    private CustomAuthenticationSuccessHandler successHandler;

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            // 其他配置...
            .oauth2Login(oauth2Login -&gt;
                oauth2Login
                    .successHandler(successHandler)
            );
    }
}

```

#### 测试自定义流程

现在，当用户通过Google社交账户登录时，应用将自动检查用户是否已存在，并据此创建或更新用户记录。登录成功后，用户将被重定向到默认成功URL，此时用户的会话已经包含了其信息。

通过这个案例，你可以看到如何将社交登录与自定义的用户注册和登录流程集成。这种方法不仅能够提高用户体验，还能够确保应用能够有效地管理和利用用户数据。
