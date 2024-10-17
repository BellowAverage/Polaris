
--- 
title:  springboot+nacos+duboo（使用的是spring cloud用法） 
tags: []
categories: [] 

---
### 安装 nacos服务注册中心（本人使用的是1.2.1）

 启动的话，win 使用 startup.cmd的文件，双击启动

### maven 导包

**注意 本人已经被坑过了，让我烦躁了好久**

**建议是使用duboo 2.7.5（2.7.6 版本有问题，需要定义组和版本号，不然@Reference 注入会失败）**

```
&lt;properties&gt;
	&lt;nacos.version&gt;2.2.1.RELEASE&lt;/nacos.version&gt;
     &lt;dubbo.version&gt;2.7.5&lt;/dubbo.version&gt;
&lt;/properties&gt;

&lt;dependencies&gt;
	&lt;!--nacos--&gt;
     &lt;dependency&gt;
          &lt;groupId&gt;com.alibaba.cloud&lt;/groupId&gt;
          &lt;artifactId&gt;spring-cloud-starter-alibaba-nacos-discovery&lt;/artifactId&gt;
          &lt;version&gt;${nacos.version}&lt;/version&gt;
      &lt;/dependency&gt;
      &lt;!--dubbo start--&gt;
      &lt;dependency&gt;
          &lt;groupId&gt;org.apache.dubbo&lt;/groupId&gt;
          &lt;artifactId&gt;dubbo-spring-boot-starter&lt;/artifactId&gt;
          &lt;version&gt;${dubbo.version}&lt;/version&gt;
      &lt;/dependency&gt;
      &lt;!--dubbo end--&gt;
&lt;/dependencies&gt;

```

### yml配置

```
server:
  port: 8001
spring:
  application:
    name: auth
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8848
dubbo:
  application:
    version: 1.0.0
    name: ${spring.application.name}
  registry:
    address: nacos://${spring.cloud.nacos.discovery.server-addr}
  protocol:
    name: dubbo
    port: 20881 #消费者可以不用被发现可以不用配置端口，如果需要就改一下端口
  scan:
    base-packages: com.ronrun.*.service #扫包
 

```

### 定义一个公有接口

**建议：定义一个公有包 使用maven 方式引入公有包就可以使用了**

```
public interface ICsService {
    int add(int a);
}

```

### 生产者

**有配置扫包应该可以不用添加这个注解，本人怕出问题没有尝试，一直有加上这个注解@EnableDubbo**

```
@EnableDubbo
@SpringBootApplication
public class AuthApplication {

    public static void main(String[] args) {
        SpringApplication.run(AuthApplication.class, args);
    }

}


```

```

import com.alibaba.dubbo.config.annotation.Service; //注意使用duboo导包
import com.ronrun.service.ICsService ;
 
@Service
public class CsServiceImpl implements ICsService {
 	private int zhi = 1000;
 	
    @Override
    public int add(int a) {
 		return zhi + a;
    }
}

```

### 消费者

**有配置扫包应该可以不用添加这个注解，本人怕出问题没有尝试，一直有加上这个注解@EnableDubbo**

```
@EnableDubbo
@SpringBootApplication
public class AuthApplication {

    public static void main(String[] args) {
        SpringApplication.run(AuthApplication.class, args);
    }

}


```

```
@RestController
public class CsController {

    @Reference // 该注解是dubbo提供的
    private ICsService csService ;

    @GetMapping("/cs")
    public String cs(int a) {
        return "变化的值"+csService.add(a);
    }
}

```

简单粗暴的配置，欢迎使用

### 解决依赖服务没有启动时，阻止spring初始化的情况

**启动时检查(check)**

>  
 默认情况下dubbo是开启自动检查的,即当项目启动时会自动检查其依赖的服务是否开启,如果没开是会阻止spring的初始化的,即check=true;我们可以将check置为false来关闭启动时检查,如我们在测试或者对其他服务没有依赖的时候可以关闭检查;在springboot中我们可以进行如下配置来关闭启动时检查： 


1、关闭某个服务的启动检查 在引用该服务的@Reference注解上添加check=false,即@Reference(check = false) 2、关闭所有服务的启动时检查 在application.properties中添加dubbo.consumer.check=false

### nacos2启用了两个端口

>  
 8848，9848 


**如果遇到对外8848和9848都需要换端口的情况如下图所示：**

<img src="https://img-blog.csdnimg.cn/e843453471fc444aad978c87b55f07c2.png" alt="在这里插入图片描述"> **那么对外端口如何启动配置呢，解决办法如下**

>  
 直接写9848端口就行，比如9848对应的端口如：31435，对应写到配置文件上的就写30435（原本9848就是8848默认加1000，反着来就行），配置文件单独使用9848（rpc）端口也是可以的 


```
spring:
  cloud:
    nacos:
      server-addr: 192.168.196.129:30435

```
