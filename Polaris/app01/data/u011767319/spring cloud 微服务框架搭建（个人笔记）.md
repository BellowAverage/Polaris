
--- 
title:  spring cloud 微服务框架搭建（个人笔记） 
tags: []
categories: [] 

---
### 父工程包引入

```
&lt;properties&gt;
       &lt;spring-cloud-dependencies.version&gt;Hoxton.SR3&lt;/spring-cloud-dependencies.version&gt;
       &lt;nacos.version&gt;2.2.1.RELEASE&lt;/nacos.version&gt;
       &lt;dubbo.version&gt;2.7.5&lt;/dubbo.version&gt;
&lt;/properties&gt;

&lt;dependencyManagement&gt;
        &lt;dependencies&gt;
        	&lt;!--spring-cloud 依赖管理--&gt;
            &lt;dependency&gt;
                &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
                &lt;artifactId&gt;spring-cloud-dependencies&lt;/artifactId&gt;
                &lt;version&gt;${<!-- -->spring-cloud-dependencies.version}&lt;/version&gt;
                &lt;type&gt;pom&lt;/type&gt;
                &lt;scope&gt;import&lt;/scope&gt;
            &lt;/dependency&gt;
            &lt;!--nacos--&gt;
            &lt;dependency&gt;
                &lt;groupId&gt;com.alibaba.cloud&lt;/groupId&gt;
                &lt;artifactId&gt;spring-cloud-starter-alibaba-nacos-discovery&lt;/artifactId&gt;
                &lt;version&gt;${<!-- -->nacos.version}&lt;/version&gt;
            &lt;/dependency&gt;
            &lt;!--dubbo start--&gt;
            &lt;dependency&gt;
                &lt;groupId&gt;org.apache.dubbo&lt;/groupId&gt;
                &lt;artifactId&gt;dubbo-spring-boot-starter&lt;/artifactId&gt;
                &lt;version&gt;${<!-- -->dubbo.version}&lt;/version&gt;
            &lt;/dependency&gt;
            &lt;!--dubbo end--&gt;
        &lt;/dependencies&gt;
&lt;/dependencyManagement&gt;

```

### naocs注册中心

>  
 本人使用的是nacos 作为注册中心 nacos是阿里开源的。具有可视化页面。 


**子项目引包**

```
&lt;dependencies&gt;
    &lt;!--nacos--&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;com.alibaba.cloud&lt;/groupId&gt;
        &lt;artifactId&gt;spring-cloud-starter-alibaba-nacos-discovery&lt;/artifactId&gt;
    &lt;/dependency&gt;
&lt;/dependencies&gt;


```

**配置文件**

```
spring:
  application:
    name: gateway
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8848

```

### duboo

**配置**

```
dubbo:
  application:
    name: ${<!-- -->spring.application.name}
  provider:
    timeout: 5000
  consumer:
    check: false #不检查服务是否启动
    timeout: 5000
  registry:
    address: nacos://${<!-- -->spring.cloud.nacos.discovery.server-addr}
    check: false #不检查注册表
  protocol:
    name: dubbo
    port: 20881
  scan:
    base-packages: com.*.*.service

```

### zuul 网关

>  
 超时问题太烦了，感觉和spring 框架就不匹配。难受。本人已经放弃了 


**怎么解决跨域问题呢，因为zuul 是基于servlet的。直接在WebMvcConfig解决就行了**

```
@Configuration
@EnableWebMvc
public class WebMvcConfig implements WebMvcConfigurer {<!-- -->
	/* 解决跨域问题 */
    @Override
    public void addCorsMappings(CorsRegistry registry) {<!-- -->
        // 设置允许跨域的路径
        registry.addMapping("/**")
                //放行哪些原始域
                .allowedOrigins("*")
                //是否发送Cookie信息
                .allowCredentials(true)
                //放行哪些原始域(请求方式)
                .allowedMethods("*")
                //放行哪些原始域(头部信息)
                .allowedHeaders("*")
                // 跨域允许时间
                .maxAge(3600);
    }
}

```

**配置**

```
zuul:
  # host配置适用于routes 为url请求服务的路由方式,如果是service-id路由方式则配置ribbon
  host:
    connect-timeout-millis: 6000
    socket-timeout-millis: 6000
    max-per-route-connections: 2000
    max-total-connections: 10000
ribbon:
  #请求处理的超时时间 下级服务响应最大时间,超出时间消费方（路由也是消费方）返回timeout
  ReadTimeout: 5000
  #ribbon请求连接的超时时间- 限制3秒内必须请求到服务，并不限制服务处理的返回时间
  ConnectTimeout: 3000
#设置hystrix超时(Edgware版本下default配置不生效,默认超时2秒,建议hystrix超时时间&gt;其他超时时间配置[如ribbon])
hystrix:
  command:
    default:
      execution:
        isolation:
          thread:
            timeoutInMilliseconds: 5000

```

**自定义启动类配置**

```
/**
 * @email 867170960@qq.com
 * @author:刘俊秦
 * @date: 2019/5/16 0016
 * @time: 上午 8:51
 * @remarks:自定义配置类
 */
@Component
@EnableDiscoveryClient
@EnableZuulProxy
public class CustomConfiguration {<!-- -->


}

```

### Gateway 网关

>  
 由于是Webflux 与web框架冲突。好用 


配置

```
spring:
  cloud:
    gateway:
      globalcors:
      	#跨域解决方案
        globalcors:
        corsConfigurations:
          '[/**]':
            #这里有个allowCredentials: true这个东西是设置允许访问携带cookie的，这点一定要和前端对应！
            allowCredentials: true
            #可以填写多个域名用","隔开 例如："http://www.xiaolc.cn,https://spring.io"  "*"代表允许所有
            allowedOrigins: "*"
            allowedMethods: "*"
            allowedHeaders: "*"
     routes:
     - id: gateway

```

### 如何优雅的扩展oauth2的认证方式。

>  
 本人参考了大量的文章。后觉得使用改变原aouth2框架的情况下，扩展我们需要的图片验证码登陆。短信登陆之类的认证方式 在原创作者的代码上进行了微量的修改，使代码更加简洁易懂。认证流程也不会被调用两次或多次重复的情况。 （这里的代码不是全部的，我只将核心的贴出来，仅供诸君参考） 


**导包**

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
    &lt;artifactId&gt;spring-cloud-starter-security&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
    &lt;artifactId&gt;spring-cloud-starter-oauth2&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;org.apache.commons&lt;/groupId&gt;
    &lt;artifactId&gt;commons-lang3&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;com.alibaba&lt;/groupId&gt;
    &lt;artifactId&gt;fastjson&lt;/artifactId&gt;
    &lt;version&gt;1.2.60&lt;/version&gt;
&lt;/dependency&gt;

```

**WebSecurityConfig 配置如下**

```
package com.ljq.oauth2.config.basic;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

@Configuration
@EnableGlobalMethodSecurity(securedEnabled = true, prePostEnabled = true)
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Bean
    public PasswordEncoder passwordEncoder() {<!-- -->
        return new BCryptPasswordEncoder();
    }

    @Bean
    public AuthenticationManager authenticationManagerBean() throws Exception {<!-- -->
        return super.authenticationManagerBean();
    }

    //安全拦截机制（最重要）
    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
                .csrf().disable()
                .formLogin()
                .and()
                .authorizeRequests()
                .antMatchers(HttpMethod.OPTIONS).permitAll()
                .anyRequest().authenticated()
        ;
    }

}


```

**TokenConfig 的配置（作者使用jwt的token 不使用原有的短token）**

```
package com.ljq.oauth2.config.basic;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.oauth2.provider.token.TokenStore;
import org.springframework.security.oauth2.provider.token.store.JwtAccessTokenConverter;
import org.springframework.security.oauth2.provider.token.store.JwtTokenStore;

@Configuration
public class TokenConfig {<!-- -->

    private static String signing_key = "liu_jun_qiin";

    /**
     * 功能描述:
     * 〈定义令牌〉
     *
     * @return : org.springframework.security.oauth2.provider.token.TokenStore
     * @author : ljq-刘俊秦
     * @date : 2020/6/6 0006 下午 2:30
     */
    @Bean
    public TokenStore tokenStore() {<!-- -->
        return new JwtTokenStore(accessTokenConverter());
    }

    @Bean
    public JwtAccessTokenConverter accessTokenConverter() {<!-- -->
        var converter = new JwtAccessTokenConverter();
        converter.setSigningKey(signing_key);
        return converter;
    }

}


```

**AuthorizationServer oauth2认证的配置**

```
package com.ljq.oauth2.config.basic;

import com.ljq.oauth2.filter.IntegrationAuthenticationFilter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.oauth2.config.annotation.configurers.ClientDetailsServiceConfigurer;
import org.springframework.security.oauth2.config.annotation.web.configuration.AuthorizationServerConfigurerAdapter;
import org.springframework.security.oauth2.config.annotation.web.configuration.EnableAuthorizationServer;
import org.springframework.security.oauth2.config.annotation.web.configurers.AuthorizationServerEndpointsConfigurer;
import org.springframework.security.oauth2.config.annotation.web.configurers.AuthorizationServerSecurityConfigurer;
import org.springframework.security.oauth2.provider.ClientDetailsService;
import org.springframework.security.oauth2.provider.code.AuthorizationCodeServices;
import org.springframework.security.oauth2.provider.code.InMemoryAuthorizationCodeServices;
import org.springframework.security.oauth2.provider.token.AuthorizationServerTokenServices;
import org.springframework.security.oauth2.provider.token.DefaultTokenServices;
import org.springframework.security.oauth2.provider.token.TokenEnhancerChain;
import org.springframework.security.oauth2.provider.token.TokenStore;
import org.springframework.security.oauth2.provider.token.store.JwtAccessTokenConverter;

import javax.annotation.Resource;
import java.util.Arrays;

@Configuration
@EnableAuthorizationServer
public class AuthorizationServer extends AuthorizationServerConfigurerAdapter {<!-- -->


    @Resource
    private TokenStore tokenStore;

    @Resource
    private JwtAccessTokenConverter accessTokenConverter;

    @Resource
    private ClientDetailsService clientDetailsService;

    @Resource
    private AuthorizationCodeServices authorizationCodeServices;

    @Resource
    private AuthenticationManager authenticationManager;

    @Resource
    private PasswordEncoder passwordEncoder;

    @Resource
    private IntegrationAuthenticationFilter integrationAuthenticationFilter;

	/**
     * 功能描述:
     * 〈去除调用两次自定义过滤连〉
     *  由于integrationAuthenticationFilter注解了@Component 注册了一遍
     *  下一又加入了一次过滤连，所有需要这个bean 重置一下
     * @param integrationAuthenticationFilter 1
     * @return : org.springframework.boot.web.servlet.FilterRegistrationBean&lt;?&gt;
     * @author : ljq-刘俊秦
     * @date : 2020/6/10 0010 下午 2:39
     */
    @Bean
    public FilterRegistrationBean&lt;?&gt; registration(IntegrationAuthenticationFilter integrationAuthenticationFilter) {<!-- -->
        FilterRegistrationBean&lt;IntegrationAuthenticationFilter&gt; registration = new FilterRegistrationBean&lt;&gt;(integrationAuthenticationFilter);
        registration.setEnabled(false);
        return registration;
    }


    /**
     * 功能描述:
     * 〈配置token 服务〉
     *
     * @return : org.springframework.security.oauth2.provider.token.AuthorizationServerTokenServices
     * @author : ljq-刘俊秦
     * @date : 2020/6/6 0006 下午 9:46
     */
    @Bean
    public AuthorizationServerTokenServices tokenService() {<!-- -->
        var service = new DefaultTokenServices();
        service.setClientDetailsService(clientDetailsService);
        service.setSupportRefreshToken(true);
        service.setTokenStore(tokenStore);
        //配置jwtToken
        var tokenEnhancer = new TokenEnhancerChain();
        tokenEnhancer.setTokenEnhancers(Arrays.asList(accessTokenConverter));
        service.setTokenEnhancer(tokenEnhancer);
        service.setAccessTokenValiditySeconds(7200); //令牌默认有效期2小时
        service.setRefreshTokenValiditySeconds(7200); //刷新令牌默认时间有效期3天
        return service;
    }

    /**
     * 功能描述:
     * 〈设置授权码模式的授权码如何存取〉
     *
     * @return : org.springframework.security.oauth2.provider.code.AuthorizationCodeServices
     * @author : ljq-刘俊秦
     * @date : 2020/6/6 0006 下午 9:46
     */
    @Bean
    public AuthorizationCodeServices authorizationCodeServices() {<!-- -->
        //设置授权码模式的授权码如何存取，暂时采用内存方式
        return new InMemoryAuthorizationCodeServices();
    }

    /**
     * 用来配置客户端详情服务（ClientDetailsService），客户端详情信息在
     * 这里进行初始化，你能够把客户端详情信息写死在这里或者是通过数据库来存储调取详情信息。
     */
    @Override
    public void configure(ClientDetailsServiceConfigurer clients) throws Exception {<!-- -->
        clients
                .inMemory()
                .withClient("c1")
                .secret(passwordEncoder.encode("liu_jun_qin"))
                .redirectUris("res1")
                .authorizedGrantTypes(
                        "authorization_code",
                        "password",
                        "client_credentials",
                        "implicit",
                        "refresh_token"
                )
                .scopes("all")
                .autoApprove(false)
                .redirectUris("http://www.baidu.com")
        ;
    }

    /**
     * 用来配置令牌（token）的访问端点和令牌服务(token services)
     */
    @Override
    public void configure(AuthorizationServerEndpointsConfigurer endpoints) throws Exception {<!-- -->
        endpoints
                .tokenServices(tokenService())
                .authenticationManager(authenticationManager)
                .authorizationCodeServices(authorizationCodeServices)
                .allowedTokenEndpointRequestMethods(HttpMethod.GET, HttpMethod.POST)
        ;
    }

    /**
     * 用来配置令牌端点的安全约束
     */
    @Override
    public void configure(AuthorizationServerSecurityConfigurer security) throws Exception {<!-- -->
        security.allowFormAuthenticationForClients()
                .tokenKeyAccess("isAuthenticated()")
                .checkTokenAccess("permitAll()")
                .addTokenEndpointAuthenticationFilter(integrationAuthenticationFilter)
        ;
    }


}


```

>  
 首先了解一下 权限认证的过滤连。在我们需要的地方插入自定义的过滤拦截 


**IntegrationAuthenticationFilter 配置集成认证，用来分发我们的过滤器-例如：图片验证码登陆、短信登陆这些**

```
package com.ljq.oauth2.filter;

import com.alibaba.fastjson.JSONObject;
import com.ljq.oauth2.config.authenticationIntegrate.IntegrationAuthentication;
import com.ljq.oauth2.config.authenticationIntegrate.IntegrationAuthenticationContext;
import com.ljq.oauth2.config.authenticationIntegrate.IntegrationAuthenticator;
import com.ljq.oauth2.exception.BaseException;
import com.ljq.oauth2.util.ServiceResult;
import org.springframework.beans.BeansException;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.security.web.util.matcher.AntPathRequestMatcher;
import org.springframework.security.web.util.matcher.OrRequestMatcher;
import org.springframework.security.web.util.matcher.RequestMatcher;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.GenericFilterBean;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Map;

@Component
public class IntegrationAuthenticationFilter extends GenericFilterBean implements ApplicationContextAware {<!-- -->

    private static final String AUTH_TYPE_PARM_NAME = "auth_type";

    private static final String OAUTH_TOKEN_URL = "/oauth/token";

    private Collection&lt;IntegrationAuthenticator&gt; authenticators;

    private ApplicationContext applicationContext;

    private final RequestMatcher requestMatcher;


    public IntegrationAuthenticationFilter() {<!-- -->
        this.requestMatcher = new OrRequestMatcher(
                new AntPathRequestMatcher(OAUTH_TOKEN_URL, "GET"),
                new AntPathRequestMatcher(OAUTH_TOKEN_URL, "POST")
        );
    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {<!-- -->

        HttpServletRequest request = null;
        HttpServletResponse response = null;
        try {<!-- -->
            request = (HttpServletRequest) servletRequest;
            response = (HttpServletResponse) servletResponse;

            if (requestMatcher.matches(request)) {<!-- -->
                //设置integrate登录信息
                IntegrationAuthentication integrationAuthentication = new IntegrationAuthentication();
                integrationAuthentication.setAuthType(request.getParameter(AUTH_TYPE_PARM_NAME));
                integrationAuthentication.setAuthParameters(request.getParameterMap());
                IntegrationAuthenticationContext.set(integrationAuthentication);
                try {<!-- -->
                    //预处理
                    this.prepare(integrationAuthentication);
                    
					filterChain.doFilter(request, response);
					
                    //后置处理
                    this.complete(integrationAuthentication);
                } finally {<!-- -->
                    IntegrationAuthenticationContext.clear();
                }
            }
            filterChain.doFilter(request, response);
        } catch (BaseException e) {<!-- -->
            writePrint(response, ServiceResult.failure(e.getCode(), e.getMessage()));
        }
    }

    /**
     * 进行预处理
     *
     * @param integrationAuthentication
     */
    private void prepare(IntegrationAuthentication integrationAuthentication) {<!-- -->

        //延迟加载认证器
        if (this.authenticators == null) {<!-- -->
            synchronized (this) {<!-- -->
                Map&lt;String, IntegrationAuthenticator&gt; integrationAuthenticatorMap = applicationContext.getBeansOfType(IntegrationAuthenticator.class);
                if (integrationAuthenticatorMap != null) {<!-- -->
                    this.authenticators = integrationAuthenticatorMap.values();
                }
            }
        }

        if (this.authenticators == null) {<!-- -->
            this.authenticators = new ArrayList&lt;&gt;();
        }

        for (IntegrationAuthenticator authenticator : authenticators) {<!-- -->
            if (authenticator.support(integrationAuthentication)) {<!-- -->
                authenticator.prepare(integrationAuthentication);
            }
        }
    }

    /**
     * 后置处理
     *
     * @param integrationAuthentication
     */
    private void complete(IntegrationAuthentication integrationAuthentication) {<!-- -->
        for (IntegrationAuthenticator authenticator : authenticators) {<!-- -->
            if (authenticator.support(integrationAuthentication)) {<!-- -->
                authenticator.complete(integrationAuthentication);
            }
        }
    }

    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {<!-- -->
        this.applicationContext = applicationContext;
    }


    public void writePrint(HttpServletResponse response, ServiceResult serviceResult) throws IOException {<!-- -->
        response.setContentType("application/json; charset=utf-8");
        response.setCharacterEncoding("UTF-8");
        var printWriter = response.getWriter();
        printWriter.write(JSONObject.toJSONString(serviceResult));
    }

}


```

**IntegrationAuthentication 收集登陆认证信息**

```
package com.ljq.oauth2.config.authenticationIntegrate;

import lombok.Data;

import java.util.Map;

/**
 * 功能描述:
 * 〈收集登陆认证信息〉
 *
 * @author : ljq-刘俊秦
 * @date : 2020/6/6 0006 下午 5:41
 */
@Data
public class IntegrationAuthentication {<!-- -->

    private String authType;
    private String username;
    private Map&lt;String, String[]&gt; authParameters;

    public String getAuthParameter(String paramter) {<!-- -->
        String[] values = this.authParameters.get(paramter);
        if (values != null &amp;&amp; values.length &gt; 0) {<!-- -->
            return values[0];
        }
        return null;
    }

}


```

**IntegrationAuthenticator 认证处理配置接口**

```
package com.ljq.oauth2.config.authenticationIntegrate;

import com.ljq.oauth2.pojo.vo.AuthUserVo;

/**
 * 功能描述:
 * 〈认证处理配置接口〉
 *
 * @author : ljq-刘俊秦
 * @date : 2020/6/8 0008 下午 3:48
 */
public interface IntegrationAuthenticator {<!-- -->

    /**
     * 处理集成认证
     * @param integrationAuthentication
     * @return
     */
    AuthUserVo authenticate(IntegrationAuthentication integrationAuthentication);


    /**
     * 进行预处理
     * @param integrationAuthentication
     */
    void prepare(IntegrationAuthentication integrationAuthentication);

     /**
     * 判断是否支持集成认证类型
     * @param integrationAuthentication
     * @return
     */
    boolean support(IntegrationAuthentication integrationAuthentication);

    /** 认证结束后执行
     * @param integrationAuthentication
     */
    void complete(IntegrationAuthentication integrationAuthentication);

}


```

**IntegrationAuthenticationContext 将认证信息储存在上下文中，集成身份验证上下文**

```
package com.ljq.oauth2.config.authenticationIntegrate;

/**
 * 功能描述:
 * 〈将认证信息储存在上下文中，集成身份验证上下文〉
 *
 * @author : ljq-刘俊秦
 * @date : 2020/6/6 0006 下午 5:42
 */
public class IntegrationAuthenticationContext {<!-- -->

    private static ThreadLocal&lt;IntegrationAuthentication&gt; holder = new ThreadLocal&lt;&gt;();

    public static void set(IntegrationAuthentication integrationAuthentication){<!-- -->
        holder.set(integrationAuthentication);
    }

    public static IntegrationAuthentication get(){<!-- -->
        return holder.get();
    }

    public static void clear(){<!-- -->
        holder.remove();
    }
}


```

**AbstractPreparableIntegrationAuthenticator 认证处理配置 实现成抽象类-可单独处理特殊数据**

```
package com.ljq.oauth2.config.authenticationIntegrate;

import com.ljq.oauth2.pojo.vo.AuthUserVo;

/**
 * 功能描述:
 * 〈认证处理配置 实现成抽象类-可单独处理特殊数据〉
 *
 * @author : ljq-刘俊秦
 * @date : 2020/6/8 0008 下午 3:50
 */
public abstract class AbstractPreparableIntegrationAuthenticator implements IntegrationAuthenticator {<!-- -->

    @Override
    public abstract AuthUserVo authenticate(IntegrationAuthentication integrationAuthentication);

    @Override
    public abstract void prepare(IntegrationAuthentication integrationAuthentication);

    @Override
    public abstract boolean support(IntegrationAuthentication integrationAuthentication);

    @Override
    public void complete(IntegrationAuthentication integrationAuthentication) {<!-- -->

    }

}


```

**默认登录处理 UsernamePasswordAuthenticator**

```
/**
 * 默认登录处理
 *
 * @author LIQIU
 * @date 2018-3-31
 **/
@Component
@Primary
public class UsernamePasswordAuthenticator extends AbstractPreparableIntegrationAuthenticator {<!-- -->

    @Resource
    private IUserService userService;

    @Override
    public AuthUserVo authenticate(IntegrationAuthentication integrationAuthentication) {<!-- -->
        String username = integrationAuthentication.getUsername();
        var user = userService.getByUserName(Long.parseLong(username));
        var authUserVo = new AuthUserVo();
        BeanUtils.copyProperties(user, authUserVo);
        return  authUserVo;
    }

    @Override
    public void prepare(IntegrationAuthentication integrationAuthentication) {<!-- -->

    }

    @Override
    public boolean support(IntegrationAuthentication integrationAuthentication) {<!-- -->
        return StringUtils.isEmpty(integrationAuthentication.getAuthType());
    }

    @Override
    public void complete(IntegrationAuthentication integrationAuthentication) {<!-- -->
        super.complete(integrationAuthentication);
    }
}


```

>  
 关键地方 本在在这写了一个假的验证，不贴项目里边的redis 验证 仅供参考 


**图片验证码处理器**

```
/**
 * 功能描述:
 * 〈图片验证码处理器〉
 *
 * @author : ljq-刘俊秦
 * @date : 2020/6/6 0006 下午 7:21
 */
@Component
public class VerificationCodeIntegrationAuthenticator extends UsernamePasswordAuthenticator {<!-- -->

    private final static String VERIFICATION_CODE_AUTH_TYPE = "vc";

    @Resource
    private IUserService userService;

    @Override
    public AuthUserVo authenticate(IntegrationAuthentication integrationAuthentication) {<!-- -->
        //获取用户名，实际值是手机号
        String username = integrationAuthentication.getUsername();
        var user = userService.getByUserName(Long.parseLong(username));
        var authUserVo = new AuthUserVo();
        BeanUtils.copyProperties(user, authUserVo);
        return  authUserVo;
    }

    @Override
    public void prepare(IntegrationAuthentication integrationAuthentication) {<!-- -->
        String vcToken = integrationAuthentication.getAuthParameter("vc_token");
        String vcCode = integrationAuthentication.getAuthParameter("vc_code");

        //验证验证码
        var yzm = RedisUtils.get(vcToken);
        if (yzm == null) {<!-- -->
            throw new BaseException(ReturnCode.VERIFICATION_NOT_EXISTENCE);
        }
        if (!yzm.equalsIgnoreCase(vcCode)) {<!-- -->
            throw new BaseException(ReturnCode.CAPTCHA);
        }

    }

    @Override
    public boolean support(IntegrationAuthentication integrationAuthentication) {<!-- -->
        return VERIFICATION_CODE_AUTH_TYPE.equals(integrationAuthentication.getAuthType());
    }

    @Override
    public void complete(IntegrationAuthentication integrationAuthentication) {<!-- -->
        //验证完成后删除验证码
        String vcToken = integrationAuthentication.getAuthParameter("vc_token");
        RedisUtils.delete(vcToken);
    }
}


```

**短信登陆验证处理器**

```
/**
 * 功能描述:
 * 〈短信登陆验证处理器〉
 *
 * @author : ljq-刘俊秦
 * @date : 2020/6/8 0008 下午 4:07
 */

@Component
public class SmsIntegrationAuthenticator extends AbstractPreparableIntegrationAuthenticator {<!-- -->

    @Resource
    private IUserService userService;
    @Resource
    private PasswordEncoder passwordEncoder;

    public final static String SMS_AUTH_TYPE = "sms";

    @Override
    public AuthUserVo authenticate(IntegrationAuthentication integrationAuthentication) {<!-- -->
        //获取密码，实际值是验证码
        String password = integrationAuthentication.getAuthParameter("password");
        //获取用户名，实际值是手机号
        String username = integrationAuthentication.getUsername();
        var user = userService.getByUserName(Long.parseLong(username));
        var authUserVo = new AuthUserVo();
        BeanUtils.copyProperties(user, authUserVo);
        authUserVo.setPassword(passwordEncoder.encode(password));
        return authUserVo;
    }

    @Override
    public void prepare(IntegrationAuthentication integrationAuthentication) {<!-- -->
        String smsToken = integrationAuthentication.getAuthParameter("sms_token");
        String smsCode = integrationAuthentication.getAuthParameter("password");

        //验证验证码
        var yzm = RedisUtils.get(smsToken);
        if (yzm == null) {<!-- -->
            throw new BaseException(ReturnCode.VERIFICATION_NOT_EXISTENCE);
        }
        if (!yzm.equalsIgnoreCase(smsCode)) {<!-- -->
            throw new BaseException(ReturnCode.CAPTCHA);
        }

    }

    @Override
    public boolean support(IntegrationAuthentication integrationAuthentication) {<!-- -->
        return SMS_AUTH_TYPE.equals(integrationAuthentication.getAuthType());
    }

    @Override
    public void complete(IntegrationAuthentication integrationAuthentication) {<!-- -->
        //手机登陆完成删除验证码
        String smsToken = integrationAuthentication.getAuthParameter("sms_token");
        RedisUtils.delete(smsToken);
    }

}


```

**实现 UserDetailsService **

```
@Service("userDetailsService")
public class AuthUserImpl implements UserDetailsService {<!-- -->

    @Resource
    private IUserService userService;

    private List&lt;IntegrationAuthenticator&gt; authenticators;

    @Autowired(required = false)
    public void setIntegrationAuthenticators(List&lt;IntegrationAuthenticator&gt; authenticators) {<!-- -->
        this.authenticators = authenticators;
    }

    @Override
    public UserDetails loadUserByUsername(String userName) throws UsernameNotFoundException {<!-- -->

        IntegrationAuthentication integrationAuthentication = IntegrationAuthenticationContext.get();
        //判断是否是集成登录
        if (integrationAuthentication == null) {<!-- -->
            integrationAuthentication = new IntegrationAuthentication();
        }
        integrationAuthentication.setUsername(userName);
        var authUserVo = this.authenticate(integrationAuthentication);

        if(authUserVo == null){<!-- -->
            throw new BaseException(ReturnCode.PHONE_NO_REGISTERED);
        }

        setAuthorize(authUserVo);
        return authUserVo;
    }

    /**
     * 设置授权信息
     */
    public UserDetails setAuthorize(AuthUserVo authUserVo) {<!-- -->
        //真实情况，这里需要查询用户信息。进行组装
        var authorities = userService.getAuthorizes(authUserVo.getId());
        authUserVo.setAuthorities(mapToGrantedAuthorities(authorities));
        return authUserVo;
    }

    /**
     * 功能描述:
     * 〈将用户的权限封装〉
     *
     * @param resources 1
     * @return : java.util.List&lt;org.springframework.security.core.GrantedAuthority&gt;
     * @author : ljq-刘俊秦
     * @date : 2020/6/6 0006 下午 6:26
     */
    private static List&lt;GrantedAuthority&gt; mapToGrantedAuthorities(List&lt;String&gt; resources) {<!-- -->
        return resources.stream()
                .map(SimpleGrantedAuthority::new)
                .collect(Collectors.toList());
    }

    private AuthUserVo authenticate(IntegrationAuthentication integrationAuthentication) {<!-- -->
        if (this.authenticators != null) {<!-- -->
            for (IntegrationAuthenticator authenticator : authenticators) {<!-- -->
                if (authenticator.support(integrationAuthentication)) {<!-- -->
                    return authenticator.authenticate(integrationAuthentication);
                }
            }
        }
        return null;
    }

}


```

**ouath2 如何自定义返回自己定义的格式数据，而不是 走DefaultWebResponseExceptionTranslator**

>  
 看源码知道，只需要实现WebResponseExceptionTranslator类的translate 方法即可 所有自定义一个异常处理就行了 


*定义一个MyWebResponseExceptionTranslator *

```
@Component
public class MyWebResponseExceptionTranslator implements WebResponseExceptionTranslator {<!-- -->

    @Override
    public ResponseEntity&lt;?&gt; translate(Exception e) throws Exception {<!-- -->
        if (e instanceof OAuth2Exception) {<!-- -->
            return ResponseEntity.ok(ServiceResult.failure(((OAuth2Exception) e).getHttpErrorCode() + "", e.getMessage()));
        }
        throw e;
    }

}

```

**配置一下 AuthorizationServer（AuthorizationServerConfigurerAdapter）中的配置**

```
@Override
    public void configure(AuthorizationServerEndpointsConfigurer endpoints) throws Exception {<!-- -->
        endpoints
               .exceptionTranslator(myWebResponseExceptionTranslator)
        ;
    }

```

**如何添加自定义的 jwt token扩展数据**

>  
 自定义一个CustomerEnhancer 


```
package com.ronrun.auth.config.securityOath2.token;

import com.alibaba.fastjson.JSON;
import com.ronrun.auth.pojo.vo.AuthUserVo;
import com.ronrun.common.constant.AuthConstant;
import org.springframework.security.oauth2.common.DefaultOAuth2AccessToken;
import org.springframework.security.oauth2.common.OAuth2AccessToken;
import org.springframework.security.oauth2.provider.OAuth2Authentication;
import org.springframework.security.oauth2.provider.token.TokenEnhancer;
import org.springframework.stereotype.Component;

import java.util.HashMap;
import java.util.Map;

@Component
public class CustomerEnhancer implements TokenEnhancer {<!-- -->

    @Override
    public OAuth2AccessToken enhance(OAuth2AccessToken oAuth2AccessToken, OAuth2Authentication oAuth2Authentication) {<!-- -->
        final Map&lt;String, Object&gt; additionalInfo = new HashMap&lt;&gt;();
        var user = (AuthUserVo) oAuth2Authentication.getUserAuthentication().getPrincipal();
        //用户名jwt 默然就已经加入所以无需在添加
        additionalInfo.put(AuthConstant.authUserVo, JSON.toJSONString(user));
        ((DefaultOAuth2AccessToken) oAuth2AccessToken).setAdditionalInformation(additionalInfo);
        return oAuth2AccessToken;
    }

}


```

**认证服务 中配置**

```
@Configuration
@EnableAuthorizationServer
public class AuthorizationServer extends AuthorizationServerConfigurerAdapter {<!-- -->
	@Resource
    private CustomerEnhancer customerEnhancer;

	/**
     * 功能描述:
     * 〈配置token 服务〉
     *
     * @return : org.springframework.security.oauth2.provider.token.AuthorizationServerTokenServices
     * @author : ljq-刘俊秦
     * @date : 2020/6/6 0006 下午 9:46
     */
    @Bean
    public AuthorizationServerTokenServices tokenService() {<!-- -->
        var service = new DefaultTokenServices();
        service.setClientDetailsService(clientDetailsService);
        service.setSupportRefreshToken(true);
        service.setTokenStore(tokenStore);
        //配置jwtToken
        var tokenEnhancer = new TokenEnhancerChain();
        tokenEnhancer.setTokenEnhancers(Arrays.asList(customerEnhancer,accessTokenConverter));
        service.setTokenEnhancer(tokenEnhancer);
        service.setAccessTokenValiditySeconds(7200); //令牌默认有效期2小时
        service.setRefreshTokenValiditySeconds(86400); //刷新令牌默认时间有效期24小时
        return service;
    }

```

**总结**

>  
 想要扩展什么登陆类型可以直接实现AbstractPreparableIntegrationAuthenticator类来处理，自己需要认证的数据。 


### SpringCloud-SpringCloudStream集成kafka




