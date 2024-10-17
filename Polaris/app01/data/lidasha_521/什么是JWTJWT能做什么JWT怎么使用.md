
--- 
title:  什么是JWT?JWT能做什么?JWT怎么使用? 
tags: []
categories: [] 

---
>  
 提示：文章写完后，目录可以自动生成，如何生成可参考右边的帮助文档 




#### 文章目录
- - - - - - <ul><li>- 


## 什么是JWT?
- `JWT` 全称`JSON Web Token` ，简单的说就是用户登录成功之后，将用户的信息进行加密，然后生成一个`token` 返回给客户端
<img src="https://img-blog.csdnimg.cn/0c89d4f75ebc4e73a939bc5c70ceae5f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

## JWT能做什么?
- **授权**：这是使用 JWT 最常见的场景。用户登录后，每个后续请求都将包含 JWT，从而允许用户访问该令牌允许的路由、服务和资源。单点登录是当今广泛使用 JWT 的一项功能，因为它的开销很小并且能够在不同的域中轻松使用。- **信息交换**：JSON Web 令牌是在各方之间安全传输信息的好方法。因为可以对 JWT 进行签名（例如，使用公钥/私钥对），所以可以确定发件人就是他们所说的那个人。此外，由于使用标头和有效负载计算签名，还可以验证内容没有被篡改。
## JWT 结构

<img src="https://img-blog.csdnimg.cn/90cdeabf54ee4d15bf0199a8313644ea.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

JWT 由以点 ( `.`) 分隔的三部分组成，分别是：
- 标头（HEADER）- 有效载荷（PAYLOAD）- 签名（SIGNATURE）
因此，JWT 通常如下所示：

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

```
<li>**标头（HEADER）** 
  <ul>- 标头**通常**由两部分组成：令牌的类型，即 JWT，以及正在使用的签名算法，例如 HMAC SHA256 或 RSA，并使用 `Base64`编码`组成 JWT 结构的` 第一部分- 令牌的第二部分是有效负载，其中包含声明。声明是关于实体（通常是用户）和附加数据的声明，并使用 `Base64`编码`组成 JWT 结构的` 第二部分- 要创建签名部分，必须获取`编码后`的`标头(HEADER)`、`有效载荷(PAYLOAD)`以及我们提供的一个`密钥`，然后使用`标头(HEADER)`中指定的签名算法进行签名。- 签名的作用是`保证 JWT 没有被篡改过`
## 信息安全问题
- Base64是一种编码,是可逆的，所以，在JWT中，`不应该在有效载荷（PAYLOAD）里面加入任何敏感的数据(如：密码)`。
## SpringBoot应用中如何使用JWT？

### 1.添加依赖

```
&lt;!-- https://mvnrepository.com/artifact/com.auth0/java-jwt --&gt;
&lt;dependency&gt;
    &lt;groupId&gt;com.auth0&lt;/groupId&gt;
    &lt;artifactId&gt;java-jwt&lt;/artifactId&gt;
    &lt;version&gt;3.19.1&lt;/version&gt;
&lt;/dependency&gt;

```
- 生成令牌/解析令牌（`签名算法和密钥`要相同，否则会抛异常）案例
```
public static void main(String[] args) {<!-- -->
      // 生成令牌
      Map&lt;String, Object&gt; map = new HashMap&lt;&gt;();
      map.put("id", 100);
      map.put("name", "李四");
      String token = JWT.create()
              .withClaim("userId", 1) // 设置payload
              .withClaim("userName", "张三")
              .withClaim("user", map) // 自定义Map
              .withIssuedAt(new Date()) // 令牌生成时间
              .withExpiresAt(new Date(System.currentTimeMillis() + 8 * 60 * 60 * 1000)) // 令牌过期时间(8小时有效)
              .sign(Algorithm.HMAC256("Test666"));// 设置签名算法和密钥
      System.out.println("token = " + token);

      // 解析令牌
      JWTVerifier jwtVerifier = JWT.require(Algorithm.HMAC256("Test666")).build();
      DecodedJWT verify = jwtVerifier.verify(token);
      System.out.println("解析结果：" + verify.getClaim("userId").asInt());
      System.out.println("解析结果：" + verify.getClaim("userName").asString());
      System.out.println("解析结果：" + verify.getClaim("user").asMap());
      System.out.println("解析结果：" + verify.getClaim("user").asMap().get("id"));
      System.out.println("解析结果：" + verify.getClaim("user").asMap().get("name"));
  }

```

### 2.拦截器配置（受限请求访问，检验Token）
- 创建返回值对象VO
```
/**
 * 公用返回结果Vo
 * @Date: 2022/04/14 22:01
 * @Version 1.0
 **/
@ApiModel(value = "ResultVo", description = "公用返回结果Vo")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class ResultVo {<!-- -->

    @ApiModelProperty(value = "状态码", example = "200")
    private Integer code;

    @ApiModelProperty(value = "返回信息", example = "success")
    private String msg;

    @ApiModelProperty(value = "返回数据", example = "data")
    private Object data;
}

```
<li> 创建拦截器，新建`TokenInterceptor`类 
  <ul><li> 认证成功后生成的token，前端通过请求头传递token给后端 <pre><code class="prism language-java">axios({<!-- -->
	method: 'get',
	url: url,
	headers: {<!-- -->
		token: this.token
	}
}).then(res =&gt; {<!-- -->
	console.log(data);
});
</code></pre> </li>
`由于浏览器的预检机制：当前端发送的请求携带自定义配置时，浏览器会发送一次预检请求（method = “OPTIONS”）,如果后端正常响应，再发送第二次请求提交数据`

```
import cn.hutool.core.util.StrUtil;
import com.auth0.jwt.JWT;
import com.auth0.jwt.JWTVerifier;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.exceptions.AlgorithmMismatchException;
import com.auth0.jwt.exceptions.SignatureVerificationException;
import com.auth0.jwt.exceptions.TokenExpiredException;
import com.cy.fmmall.common.vo.ResultStatus;
import com.cy.fmmall.common.vo.ResultVo;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

/**
 * 定义拦截器
 * @Date: 2022/04/14 12:26
 * @Version 1.0
 **/
@Component
public class TokenInterceptor implements HandlerInterceptor {<!-- -->

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws IOException {<!-- -->

        // System.out.println("------这不就进来了吗");

        // 处理 method = “OPTIONS” 预检请求
        String requestMethod = request.getMethod();
        if ("OPTIONS".equalsIgnoreCase(requestMethod)){<!-- -->
            return true;
        }
        
        if (StrUtil.isBlank(token)){<!-- -->
            ResultVo resultVo = new ResultVo(ResultStatus.SUCCESS, "请先登录", null);
            doResponse(response, resultVo);
            return false;
        } else {<!-- -->
            try {<!-- -->
                // 解析令牌
                JWTVerifier jwtVerifier = JWT.require(Algorithm.HMAC256("Lidasha521")).build();
                jwtVerifier.verify(token);
                /*
                 * 常见异常
                 * SignatureVerificationException: 签名不一致异常
                 * TokenExpiredException: 令牌过期异常
                 * AlgorithmMismatchException: 算法不匹配异常
                 */
            } catch (SignatureVerificationException | AlgorithmMismatchException e) {<!-- -->
                ResultVo resultVo = new ResultVo(ResultStatus.FAIL, "Token不合法，请重新登录", null);
                doResponse(response, resultVo);
            } catch (TokenExpiredException e) {<!-- -->
                ResultVo resultVo = new ResultVo(ResultStatus.FAIL, "Token已过期，请重新登录", null);
                doResponse(response, resultVo);
            } catch (Exception e){<!-- -->
                ResultVo resultVo = new ResultVo(ResultStatus.FAIL, "请先登录", null);
                doResponse(response, resultVo);
            }
            return true;
        }
    }

    // 创建json格式返回对象
    private void doResponse(HttpServletResponse response, ResultVo resultVo) throws IOException {<!-- -->
        response.setContentType("application/json");
        response.setCharacterEncoding("utf-8");
        PrintWriter writer = response.getWriter();
        String msg = new ObjectMapper().writeValueAsString(resultVo);
        writer.println(msg);
        writer.flush();
        writer.close();
    }
}

```
- 配置拦截器：新建`InterceptorConfig`类
```
import com.cy.fmmall.api.interceptor.TokenInterceptor;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import javax.annotation.Resource;

/**
 * 配置拦截器
 * @Date: 2022/04/14 12:22
 * @Version 1.0
 **/
@Configuration
public class InterceptorConfig implements WebMvcConfigurer {<!-- -->

    @Resource
    private TokenInterceptor tokenInterceptor;

    @Override
    public void addInterceptors(InterceptorRegistry registry) {<!-- -->
        // 注册拦截器
        InterceptorRegistration interceptorRegistration = registry.addInterceptor(tokenInterceptor);
        // 设置需要拦截的请求（也可设置成list集合）
        interceptorRegistration.addPathPatterns("/product/**");
        // 设置不需要拦截的请求（也可设置成list集合）
        interceptorRegistration.excludePathPatterns("/user/**");
    }
}

```
- 测试结果
<img src="https://img-blog.csdnimg.cn/5b13f7fc604c436ea68b9b46e9bce787.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">
