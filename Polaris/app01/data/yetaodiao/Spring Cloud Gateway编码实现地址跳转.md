
--- 
title:  Spring Cloud Gateway编码实现地址跳转 
tags: []
categories: [] 

---
#### **Spring Cloud Gateway编码实现地址跳转一般路由规则**
- 先来看一个普通的路由规则，如下所示，意思是将所有/hello/**的请求转发到这个地址去：
```
&lt;span style="color:#393939"&gt;&lt;span style="background-color:#faf7ef"&gt;&lt;code class="language-yaml language-yml"&gt;&lt;span style="color:#ff0000"&gt;spring:&lt;/span&gt;
  &lt;span style="color:#ff0000"&gt;application:&lt;/span&gt;
    &lt;span style="color:#ff0000"&gt;name:&lt;/span&gt; &lt;span style="color:#a31515"&gt;hello-gateway&lt;/span&gt;
  &lt;span style="color:#ff0000"&gt;cloud:&lt;/span&gt;
    &lt;span style="color:#ff0000"&gt;gateway:&lt;/span&gt;
      &lt;span style="color:#ff0000"&gt;routes:&lt;/span&gt;
        &lt;span style="color:#00b0e8"&gt;-&lt;/span&gt; &lt;span style="color:#ff0000"&gt;id:&lt;/span&gt; &lt;span style="color:#a31515"&gt;path_route&lt;/span&gt;
          &lt;span style="color:#ff0000"&gt;uri:&lt;/span&gt; &lt;span style="color:#a31515"&gt;http://127.0.0.1:8082&lt;/span&gt;
          &lt;span style="color:#ff0000"&gt;predicates:&lt;/span&gt;
          &lt;span style="color:#00b0e8"&gt;-&lt;/span&gt; &lt;span style="color:#a31515"&gt;Path=/hello/**&lt;/span&gt;
&lt;/code&gt;&lt;/span&gt;&lt;/span&gt;
```
- 上述规则的功能如下图所示，假设这就是生产环境的样子，192.168.50.99:8082是提供服务的后台应用： <img alt="" src="https://img-blog.csdnimg.cn/img_convert/917c3ca58e9935e7f44a79196c6ed02f.png"> 
#### **特殊规则**
- 以上是常规情况，但也有些特殊情况，要求SpringCloud Gateway把浏览器的请求转发到不同的服务上去- 如下图所示，在之前的环境中增加了另一个服务（即蓝色块），假设蓝色服务代表测试环境 <img alt="" src="https://img-blog.csdnimg.cn/img_convert/fefbf00e8f59bfd70bf224dbaf5ec6bd.png"> - 浏览器发起的/hello/str请求中，如果header中带有tag-test-user，并且值等于**true**，此时要求SpringCloud Gateway把这个请求转发到测试环境- 如果浏览器的请求header中没有tag-test-user，SpringCloud Gateway需要像以前那样继续转发到192.168.50.99:8082- 很明显，上述需求难以通过配置来实现，因为转发的地址和转发逻辑都是围绕业务逻辑来定制的，这也就是本篇的目标：对同一个请求path，可以通过编码转发到不同的地方去- 实现上述功能的具体做法是：自定义过滤器
#### **设计**
- 编码之前先设计，把关键点想清楚再动手- 今天咱们要开发一个SpringCloud Gateway应用，里面新增一个自定义过滤器- 实现这个功能需要三个知识点作为基础，也就是说，您会通过本篇实战掌握以下知识点：1. 自定义过滤器1. 自定义过滤器的配置参数和bean的映射1. 编码构造Route实例- 用思维导图将具体工作内容展开，如下图所示，咱们就按部就班的实现吧： <img alt="" src="https://img-blog.csdnimg.cn/img_convert/b1661a7158828cb129b7597e43920377.png"> 
#### **源码下载**
- 本篇实战中的完整源码可在GitHub下载到，地址和链接信息如下表所示()：
<th style="background-color:#fafafa;text-align:left;">名称</th><th style="background-color:#fafafa;text-align:left;">链接</th><th style="background-color:#fafafa;text-align:left;">备注</th>
|------
<td style="border-color:#c0c0c0;text-align:left;">项目主页</td><td style="border-color:#c0c0c0;text-align:left;"></td><td style="border-color:#c0c0c0;text-align:left;">该项目在GitHub上的主页</td>
<td style="border-color:#c0c0c0;text-align:left;">git仓库地址(https)</td><td style="border-color:#c0c0c0;text-align:left;"></td><td style="border-color:#c0c0c0;text-align:left;">该项目源码的仓库地址，https协议</td>
<td style="border-color:#c0c0c0;text-align:left;">git仓库地址(ssh)</td><td style="border-color:#c0c0c0;text-align:left;">git@github.com:zq2599/blog_demos.git</td><td style="border-color:#c0c0c0;text-align:left;">该项目源码的仓库地址，ssh协议</td>
- 这个git项目中有多个文件夹，本篇的源码在spring-cloud-tutorials文件夹下，如下图红框所示： <img alt="" src="https://img-blog.csdnimg.cn/img_convert/17c888a57d3c715fc2e174ac19ce0240.png"> - spring-cloud-tutorials内部有多个子项目，本篇的源码在gateway-dynamic-route文件夹下，如下图红框所示：
#### **编码**
- 新建名为gateway-dynamic-route的maven工程，其pom.xml内容如下：
```
&lt;span style="color:#393939"&gt;&lt;span style="background-color:#faf7ef"&gt;&lt;code class="language-xml"&gt;&lt;span style="color:#2b91af"&gt;&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;/span&gt;
&lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;project&lt;/span&gt; &lt;span style="color:#ff0000"&gt;xmlns&lt;/span&gt;=&lt;span style="color:#a31515"&gt;"http://maven.apache.org/POM/4.0.0"&lt;/span&gt;
         &lt;span style="color:#ff0000"&gt;xmlns:xsi&lt;/span&gt;=&lt;span style="color:#a31515"&gt;"http://www.w3.org/2001/XMLSchema-instance"&lt;/span&gt;
         &lt;span style="color:#ff0000"&gt;xsi:schemaLocation&lt;/span&gt;=&lt;span style="color:#a31515"&gt;"http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"&lt;/span&gt;&gt;&lt;/span&gt;
    &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;parent&lt;/span&gt;&gt;&lt;/span&gt;
        &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;artifactId&lt;/span&gt;&gt;&lt;/span&gt;spring-cloud-tutorials&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;artifactId&lt;/span&gt;&gt;&lt;/span&gt;
        &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;groupId&lt;/span&gt;&gt;&lt;/span&gt;com.bolingcavalry&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;groupId&lt;/span&gt;&gt;&lt;/span&gt;
        &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;version&lt;/span&gt;&gt;&lt;/span&gt;1.0-SNAPSHOT&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;version&lt;/span&gt;&gt;&lt;/span&gt;
    &lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;parent&lt;/span&gt;&gt;&lt;/span&gt;
    &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;modelVersion&lt;/span&gt;&gt;&lt;/span&gt;4.0.0&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;modelVersion&lt;/span&gt;&gt;&lt;/span&gt;

    &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;artifactId&lt;/span&gt;&gt;&lt;/span&gt;gateway-dynamic-route&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;artifactId&lt;/span&gt;&gt;&lt;/span&gt;

    &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;dependencies&lt;/span&gt;&gt;&lt;/span&gt;
        &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;dependency&lt;/span&gt;&gt;&lt;/span&gt;
            &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;groupId&lt;/span&gt;&gt;&lt;/span&gt;com.bolingcavalry&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;groupId&lt;/span&gt;&gt;&lt;/span&gt;
            &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;artifactId&lt;/span&gt;&gt;&lt;/span&gt;common&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;artifactId&lt;/span&gt;&gt;&lt;/span&gt;
            &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;version&lt;/span&gt;&gt;&lt;/span&gt;${project.version}&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;version&lt;/span&gt;&gt;&lt;/span&gt;
        &lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;dependency&lt;/span&gt;&gt;&lt;/span&gt;
        &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;dependency&lt;/span&gt;&gt;&lt;/span&gt;
            &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;groupId&lt;/span&gt;&gt;&lt;/span&gt;org.springframework.cloud&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;groupId&lt;/span&gt;&gt;&lt;/span&gt;
            &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;artifactId&lt;/span&gt;&gt;&lt;/span&gt;spring-cloud-starter-gateway&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;artifactId&lt;/span&gt;&gt;&lt;/span&gt;
        &lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;dependency&lt;/span&gt;&gt;&lt;/span&gt;
    &lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;dependencies&lt;/span&gt;&gt;&lt;/span&gt;
    &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;build&lt;/span&gt;&gt;&lt;/span&gt;
        &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;plugins&lt;/span&gt;&gt;&lt;/span&gt;
            &lt;span style="color:#008000"&gt;&lt;!-- 如果父工程不是springboot，就要用以下方式使用插件，才能生成正常的jar --&gt;&lt;/span&gt;
            &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;plugin&lt;/span&gt;&gt;&lt;/span&gt;
                &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;groupId&lt;/span&gt;&gt;&lt;/span&gt;org.springframework.boot&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;groupId&lt;/span&gt;&gt;&lt;/span&gt;
                &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;artifactId&lt;/span&gt;&gt;&lt;/span&gt;spring-boot-maven-plugin&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;artifactId&lt;/span&gt;&gt;&lt;/span&gt;
                &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;configuration&lt;/span&gt;&gt;&lt;/span&gt;
                    &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;mainClass&lt;/span&gt;&gt;&lt;/span&gt;com.bolingcavalry.gateway.GatewayDynamicRouteApplication&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;mainClass&lt;/span&gt;&gt;&lt;/span&gt;
                &lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;configuration&lt;/span&gt;&gt;&lt;/span&gt;
                &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;executions&lt;/span&gt;&gt;&lt;/span&gt;
                    &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;execution&lt;/span&gt;&gt;&lt;/span&gt;
                        &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;goals&lt;/span&gt;&gt;&lt;/span&gt;
                            &lt;span style="color:#0000ff"&gt;&lt;&lt;span style="color:#0000ff"&gt;goal&lt;/span&gt;&gt;&lt;/span&gt;repackage&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;goal&lt;/span&gt;&gt;&lt;/span&gt;
                        &lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;goals&lt;/span&gt;&gt;&lt;/span&gt;
                    &lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;execution&lt;/span&gt;&gt;&lt;/span&gt;
                &lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;executions&lt;/span&gt;&gt;&lt;/span&gt;
            &lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;plugin&lt;/span&gt;&gt;&lt;/span&gt;
        &lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;plugins&lt;/span&gt;&gt;&lt;/span&gt;
    &lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;build&lt;/span&gt;&gt;&lt;/span&gt;
&lt;span style="color:#0000ff"&gt;&lt;/&lt;span style="color:#0000ff"&gt;project&lt;/span&gt;&gt;&lt;/span&gt;
&lt;/code&gt;&lt;/span&gt;&lt;/span&gt;
```
- 启动类是普通的SpringBoot启动类：
```
&lt;span style="color:#393939"&gt;&lt;span style="background-color:#faf7ef"&gt;&lt;code class="language-java"&gt;&lt;span style="color:#0000ff"&gt;package&lt;/span&gt; com.bolingcavalry.gateway;

&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; org.springframework.boot.SpringApplication;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; org.springframework.boot.autoconfigure.SpringBootApplication;

&lt;span style="color:#2b91af"&gt;@SpringBootApplication&lt;/span&gt;
&lt;span style="color:#0000ff"&gt;public&lt;/span&gt; &lt;span style="color:#0000ff"&gt;class&lt;/span&gt; &lt;span style="color:#a31515"&gt;GatewayDynamicRouteApplication&lt;/span&gt; {
    &lt;span style="color:#0000ff"&gt;public&lt;/span&gt; &lt;span style="color:#0000ff"&gt;static&lt;/span&gt; &lt;span style="color:#0000ff"&gt;void&lt;/span&gt; &lt;span style="color:#a31515"&gt;main&lt;/span&gt;(String[] args) {
        SpringApplication.run(GatewayDynamicRouteApplication.class,args);
    }
}
&lt;/code&gt;&lt;/span&gt;&lt;/span&gt;
```
- 接下来是本篇的核心，自定义过滤器类，代码中已经添加了详细的注释，有几处要注意的地方稍后会提到：
```
&lt;span style="color:#393939"&gt;&lt;span style="background-color:#faf7ef"&gt;&lt;code class="language-java"&gt;&lt;span style="color:#0000ff"&gt;package&lt;/span&gt; com.bolingcavalry.gateway.filter;

&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; lombok.Data;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; lombok.ToString;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; lombok.extern.slf4j.Slf4j;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; org.springframework.cloud.gateway.filter.GatewayFilter;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; org.springframework.cloud.gateway.filter.factory.AbstractGatewayFilterFactory;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; org.springframework.cloud.gateway.route.Route;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; org.springframework.http.HttpHeaders;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; org.springframework.http.HttpMethod;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; org.springframework.http.server.reactive.ServerHttpRequest;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; org.springframework.stereotype.Component;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; org.springframework.util.MultiValueMap;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; org.springframework.web.util.UriComponentsBuilder;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; java.net.URI;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; &lt;span style="color:#0000ff"&gt;static&lt;/span&gt; org.springframework.cloud.gateway.support.ServerWebExchangeUtils.GATEWAY_ROUTE_ATTR;

&lt;span style="color:#2b91af"&gt;@Component&lt;/span&gt;
&lt;span style="color:#2b91af"&gt;@Slf4j&lt;/span&gt;
&lt;span style="color:#0000ff"&gt;public&lt;/span&gt; &lt;span style="color:#0000ff"&gt;class&lt;/span&gt; &lt;span style="color:#a31515"&gt;BizLogicRouteGatewayFilterFactory&lt;/span&gt; &lt;span style="color:#0000ff"&gt;extends&lt;/span&gt; &lt;span style="color:#a31515"&gt;AbstractGatewayFilterFactory&lt;/span&gt;&lt;BizLogicRouteGatewayFilterFactory.BizLogicRouteConfig&gt; {

    &lt;span style="color:#0000ff"&gt;private&lt;/span&gt; &lt;span style="color:#0000ff"&gt;static&lt;/span&gt; &lt;span style="color:#0000ff"&gt;final&lt;/span&gt; &lt;span style="color:#a31515"&gt;String&lt;/span&gt; &lt;span style="color:#008000"&gt;TAG_TEST_USER&lt;/span&gt; &lt;span style="color:#ab5656"&gt;=&lt;/span&gt; &lt;span style="color:#a31515"&gt;"tag-test-user"&lt;/span&gt;;

    &lt;span style="color:#0000ff"&gt;public&lt;/span&gt; &lt;span style="color:#a31515"&gt;BizLogicRouteGatewayFilterFactory&lt;/span&gt;() {
        &lt;span style="color:#0000ff"&gt;super&lt;/span&gt;(BizLogicRouteConfig.class);
    }

    &lt;span style="color:#2b91af"&gt;@Override&lt;/span&gt;
    &lt;span style="color:#0000ff"&gt;public&lt;/span&gt; GatewayFilter &lt;span style="color:#a31515"&gt;apply&lt;/span&gt;(BizLogicRouteConfig config) {

        &lt;span style="color:#0000ff"&gt;return&lt;/span&gt; (exchange, chain) -&gt; {
            &lt;span style="color:#008000"&gt;// 本次的请求对象&lt;/span&gt;
            &lt;span style="color:#a31515"&gt;ServerHttpRequest&lt;/span&gt; &lt;span style="color:#008000"&gt;request&lt;/span&gt; &lt;span style="color:#ab5656"&gt;=&lt;/span&gt;  exchange.getRequest();

            &lt;span style="color:#008000"&gt;// 调用方请求时的path&lt;/span&gt;
            &lt;span style="color:#a31515"&gt;String&lt;/span&gt; &lt;span style="color:#008000"&gt;rawPath&lt;/span&gt; &lt;span style="color:#ab5656"&gt;=&lt;/span&gt; request.getURI().getRawPath();

            log.info(&lt;span style="color:#a31515"&gt;"rawPath [{}]"&lt;/span&gt;, rawPath);

            &lt;span style="color:#008000"&gt;// 请求头&lt;/span&gt;
            &lt;span style="color:#a31515"&gt;HttpHeaders&lt;/span&gt; &lt;span style="color:#008000"&gt;headers&lt;/span&gt; &lt;span style="color:#ab5656"&gt;=&lt;/span&gt; request.getHeaders();

            &lt;span style="color:#008000"&gt;// 请求方法&lt;/span&gt;
            &lt;span style="color:#a31515"&gt;HttpMethod&lt;/span&gt; &lt;span style="color:#008000"&gt;httpMethod&lt;/span&gt; &lt;span style="color:#ab5656"&gt;=&lt;/span&gt; request.getMethod();

            &lt;span style="color:#008000"&gt;// 请求参数&lt;/span&gt;
            MultiValueMap&lt;String, String&gt; queryParams = request.getQueryParams();

            &lt;span style="color:#008000"&gt;// 这就是定制的业务逻辑，isTestUser等于ture代表当前请求来自测试用户，需要被转发到测试环境&lt;/span&gt;
            &lt;span style="color:#a31515"&gt;boolean&lt;/span&gt; &lt;span style="color:#008000"&gt;isTestUser&lt;/span&gt; &lt;span style="color:#ab5656"&gt;=&lt;/span&gt; &lt;span style="color:#a31515"&gt;false&lt;/span&gt;;

            &lt;span style="color:#008000"&gt;// 如果header中有tag-test-user这个key，并且值等于true(不区分大小写)，&lt;/span&gt;
            &lt;span style="color:#008000"&gt;// 就认为当前请求是测试用户发来的&lt;/span&gt;
            &lt;span style="color:#0000ff"&gt;if&lt;/span&gt; (headers.containsKey(TAG_TEST_USER)) {
                &lt;span style="color:#a31515"&gt;String&lt;/span&gt; &lt;span style="color:#008000"&gt;tageTestUser&lt;/span&gt; &lt;span style="color:#ab5656"&gt;=&lt;/span&gt; headers.get(TAG_TEST_USER).get(&lt;span style="color:#880000"&gt;0&lt;/span&gt;);

                &lt;span style="color:#0000ff"&gt;if&lt;/span&gt; (&lt;span style="color:#a31515"&gt;"true"&lt;/span&gt;.equalsIgnoreCase(tageTestUser)) {
                    isTestUser = &lt;span style="color:#a31515"&gt;true&lt;/span&gt;;
                }
            }

            URI uri;

            &lt;span style="color:#0000ff"&gt;if&lt;/span&gt; (isTestUser) {
                log.info(&lt;span style="color:#a31515"&gt;"这是测试用户的请求"&lt;/span&gt;);
                &lt;span style="color:#008000"&gt;// 从配置文件中得到测试环境的uri&lt;/span&gt;
                uri = UriComponentsBuilder.fromHttpUrl(config.getTestEnvUri() + rawPath).queryParams(queryParams).build().toUri();
            } &lt;span style="color:#0000ff"&gt;else&lt;/span&gt; {
                log.info(&lt;span style="color:#a31515"&gt;"这是普通用户的请求"&lt;/span&gt;);
                &lt;span style="color:#008000"&gt;// 从配置文件中得到正式环境的uri&lt;/span&gt;
                uri = UriComponentsBuilder.fromHttpUrl(config.getProdEnvUri() + rawPath).queryParams(queryParams).build().toUri();
            }

            &lt;span style="color:#008000"&gt;// 生成新的Request对象，该对象放弃了常规路由配置中的spring.cloud.gateway.routes.uri字段&lt;/span&gt;
            &lt;span style="color:#a31515"&gt;ServerHttpRequest&lt;/span&gt; &lt;span style="color:#008000"&gt;serverHttpRequest&lt;/span&gt; &lt;span style="color:#ab5656"&gt;=&lt;/span&gt; request.mutate().uri(uri).method(httpMethod).headers(httpHeaders -&gt; httpHeaders = httpHeaders).build();

            &lt;span style="color:#008000"&gt;// 取出当前的route对象&lt;/span&gt;
            &lt;span style="color:#a31515"&gt;Route&lt;/span&gt; &lt;span style="color:#008000"&gt;route&lt;/span&gt; &lt;span style="color:#ab5656"&gt;=&lt;/span&gt; exchange.getAttribute(GATEWAY_ROUTE_ATTR);
            &lt;span style="color:#008000"&gt;//从新设置Route地址&lt;/span&gt;
            &lt;span style="color:#a31515"&gt;Route&lt;/span&gt; &lt;span style="color:#008000"&gt;newRoute&lt;/span&gt; &lt;span style="color:#ab5656"&gt;=&lt;/span&gt;
                    Route.async().asyncPredicate(route.getPredicate()).filters(route.getFilters()).id(route.getId())
                            .order(route.getOrder()).uri(uri).build();
            &lt;span style="color:#008000"&gt;// 放回exchange中&lt;/span&gt;
            exchange.getAttributes().put(GATEWAY_ROUTE_ATTR,newRoute);

            &lt;span style="color:#008000"&gt;// 链式处理，交给下一个过滤器&lt;/span&gt;
            &lt;span style="color:#0000ff"&gt;return&lt;/span&gt; chain.filter(exchange.mutate().request(serverHttpRequest).build());
        };
    }

    &lt;span style="color:#008000"&gt;/**
     * 这是过滤器的配置类，配置信息会保存在此处
     */&lt;/span&gt;
    &lt;span style="color:#2b91af"&gt;@Data&lt;/span&gt;
    &lt;span style="color:#2b91af"&gt;@ToString&lt;/span&gt;
    &lt;span style="color:#0000ff"&gt;public&lt;/span&gt; &lt;span style="color:#0000ff"&gt;static&lt;/span&gt; &lt;span style="color:#0000ff"&gt;class&lt;/span&gt; &lt;span style="color:#a31515"&gt;BizLogicRouteConfig&lt;/span&gt; {
        &lt;span style="color:#008000"&gt;// 生产环境的服务地址&lt;/span&gt;
        &lt;span style="color:#0000ff"&gt;private&lt;/span&gt; String prodEnvUri;

        &lt;span style="color:#008000"&gt;// 测试环境的服务地址&lt;/span&gt;
        &lt;span style="color:#0000ff"&gt;private&lt;/span&gt; String testEnvUri;
    }
}
&lt;/code&gt;&lt;/span&gt;&lt;/span&gt;
```
- 上述代码中要注意的地方如下：1. BizLogicRouteConfig是过滤器的配置类，可以在使用过滤器时在配置文件中配置prodEnvUri和testEnvUri的值，在代码中可以通过这两个字段取得配置值1. 过滤器的工厂类名为BizLogicRouteGatewayFilterFactory，按照规则，过滤器的名字是BizLogicRoute1. 在apply方法中，重新创建ServerHttpRequest和Route对象，它们的参数可以按照业务需求随意设置，然后再将这两个对象设置给SpringCloud gateway的处理链中，接下来，处理链上的其他过滤拿到的就是新的ServerHttpRequest和Route对象了
#### **配置**
- 假设生产环境地址是，测试环境地址是，整个SpringCloud Gateway应用的配置文件如下，可见使用了刚刚创建的过滤器，并且为此过滤器配置了两个参数：
```
&lt;span style="color:#393939"&gt;&lt;span style="background-color:#faf7ef"&gt;&lt;code class="language-yaml language-yml"&gt;&lt;span style="color:#ff0000"&gt;server:&lt;/span&gt;
  &lt;span style="color:#008000"&gt;#服务端口&lt;/span&gt;
  &lt;span style="color:#ff0000"&gt;port:&lt;/span&gt; &lt;span style="color:#880000"&gt;8086&lt;/span&gt;
&lt;span style="color:#ff0000"&gt;spring:&lt;/span&gt;
  &lt;span style="color:#ff0000"&gt;application:&lt;/span&gt;
    &lt;span style="color:#ff0000"&gt;name:&lt;/span&gt; &lt;span style="color:#a31515"&gt;gateway-dynamic-route&lt;/span&gt;
  &lt;span style="color:#ff0000"&gt;cloud:&lt;/span&gt;
    &lt;span style="color:#ff0000"&gt;gateway:&lt;/span&gt;
      &lt;span style="color:#ff0000"&gt;routes:&lt;/span&gt;
        &lt;span style="color:#00b0e8"&gt;-&lt;/span&gt; &lt;span style="color:#ff0000"&gt;id:&lt;/span&gt; &lt;span style="color:#a31515"&gt;path_route&lt;/span&gt;
          &lt;span style="color:#ff0000"&gt;uri:&lt;/span&gt; &lt;span style="color:#a31515"&gt;http://0.0.0.0:8082&lt;/span&gt;
          &lt;span style="color:#ff0000"&gt;predicates:&lt;/span&gt;
          &lt;span style="color:#00b0e8"&gt;-&lt;/span&gt; &lt;span style="color:#a31515"&gt;Path=/hello/**&lt;/span&gt;
          &lt;span style="color:#ff0000"&gt;filters:&lt;/span&gt;
            &lt;span style="color:#00b0e8"&gt;-&lt;/span&gt; &lt;span style="color:#ff0000"&gt;name:&lt;/span&gt; &lt;span style="color:#a31515"&gt;BizLogicRoute&lt;/span&gt;
              &lt;span style="color:#ff0000"&gt;args:&lt;/span&gt;
                &lt;span style="color:#ff0000"&gt;prodEnvUri:&lt;/span&gt; &lt;span style="color:#a31515"&gt;http://127.0.0.1:8082&lt;/span&gt;
                &lt;span style="color:#ff0000"&gt;testEnvUri:&lt;/span&gt; &lt;span style="color:#a31515"&gt;http://127.0.0.1:8087&lt;/span&gt;
&lt;/code&gt;&lt;/span&gt;&lt;/span&gt;
```
- 至此，编码完成了，启动这个服务
#### **开发和启动后台服务，模拟生产和测试环境**
- 接下来开始验证功能是否生效，咱们要准备两个后台服务：1. 模拟生产环境的后台服务是provider-hello，监听端口是8082，其/hello/str接口的返回值是Hello World, 2021-12-12 10:53:091. 模拟测试环境的后台服务是provider-for-test-user，监听端口是8087，其/hello/str接口的返回值是Hello World, 2021-12-12 10:57:11 (from test enviroment)（和生产环境相比，返回内容多了个(from test enviroment)），对应Controller参考如下：
```
&lt;span style="color:#393939"&gt;&lt;span style="background-color:#faf7ef"&gt;&lt;code class="language-java"&gt;&lt;span style="color:#0000ff"&gt;package&lt;/span&gt; com.bolingcavalry.provider.controller;

&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; com.bolingcavalry.common.Constants;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; org.springframework.web.bind.annotation.*;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; java.text.SimpleDateFormat;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; java.util.Date;
&lt;span style="color:#0000ff"&gt;import&lt;/span&gt; java.util.Map;

&lt;span style="color:#2b91af"&gt;@RestController&lt;/span&gt;
&lt;span style="color:#2b91af"&gt;@RequestMapping("/hello")&lt;/span&gt;
&lt;span style="color:#0000ff"&gt;public&lt;/span&gt; &lt;span style="color:#0000ff"&gt;class&lt;/span&gt; &lt;span style="color:#a31515"&gt;Hello&lt;/span&gt; {

    &lt;span style="color:#0000ff"&gt;private&lt;/span&gt; String &lt;span style="color:#a31515"&gt;dateStr&lt;/span&gt;(){
        &lt;span style="color:#0000ff"&gt;return&lt;/span&gt; &lt;span style="color:#0000ff"&gt;new&lt;/span&gt; &lt;span style="color:#a31515"&gt;SimpleDateFormat&lt;/span&gt;(&lt;span style="color:#a31515"&gt;"yyyy-MM-dd hh:mm:ss"&lt;/span&gt;).format(&lt;span style="color:#0000ff"&gt;new&lt;/span&gt; &lt;span style="color:#a31515"&gt;Date&lt;/span&gt;());
    }

    &lt;span style="color:#008000"&gt;/**
     * 返回字符串类型
     * &lt;span style="color:#808080"&gt;@return&lt;/span&gt;
     */&lt;/span&gt;
    &lt;span style="color:#2b91af"&gt;@GetMapping("/str")&lt;/span&gt;
    &lt;span style="color:#0000ff"&gt;public&lt;/span&gt; String &lt;span style="color:#a31515"&gt;helloStr&lt;/span&gt;() {
        &lt;span style="color:#0000ff"&gt;return&lt;/span&gt; Constants.HELLO_PREFIX + &lt;span style="color:#a31515"&gt;", "&lt;/span&gt; + dateStr() + &lt;span style="color:#a31515"&gt;" (from test enviroment)"&lt;/span&gt;;
    }
}
&lt;/code&gt;&lt;/span&gt;&lt;/span&gt;
```
- 以上两个服务，对应的代码都在我的中，如下图红框所示： <img alt="" src="https://img-blog.csdnimg.cn/img_convert/faae8f9c10828a758c3788e59a883289.png"> - 启动gateway-dynamic-route、provider-hello、provider-for-test-user服务- 此时，SpringCloud gateway应用和两个后台服务都启动完成，情况如下图，接下来验证刚才开发的过滤器能不能像预期那样转发： <img alt="" src="https://img-blog.csdnimg.cn/img_convert/ed901535e7028561c7b2bdafc055567a.png"> 
#### **验证**
- 用postman工具向gateway-dynamic-route应用发起一次请求，返回值如下图红框所示，证明这是provider-hello的响应，看来咱们的请求已经正常到达： <img alt="" src="https://img-blog.csdnimg.cn/img_convert/216ed2ec91c91f373acf35feddd9a5f6.png"> - 再发送一次请求，如下图，这次在header中加入键值对，得到的结果是provider-for-test-user的响应 <img alt="" src="https://img-blog.csdnimg.cn/img_convert/3314f18a356b66e04abbc3274cfc5171.png"> - 至此，过滤器的开发和验证已经完成，通过编码，可以把外部请求转发到任何咱们需要的地址去，并且支持参数配置，这个过滤器还有一定的可配置下，减少了硬编码的比率，如果您正在琢磨如何深度操控SpringCloud Gateway，希望本文能给您一些参考；