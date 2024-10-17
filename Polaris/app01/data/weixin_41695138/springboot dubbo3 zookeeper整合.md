
--- 
title:  springboot dubbo3 zookeeper整合 
tags: []
categories: [] 

---
### springboot dubbo3 zookeeper整合
1. 在这个项目的基础上： 1. 项目放到 gitee 上了，地址为： https://gitee.com/qinenqi/zookeeperdubbo.git
### provider项目
1. pom 文件：
```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd"&gt;
    &lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;
    &lt;parent&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-starter-parent&lt;/artifactId&gt;
&lt;!--        &lt;version&gt;2.7.5&lt;/version&gt;--&gt;
&lt;!--        &lt;version&gt;2.3.1.RELEASE&lt;/version&gt;--&gt;
        &lt;version&gt;2.2.6.RELEASE&lt;/version&gt;
        &lt;relativePath/&gt; &lt;!-- lookup parent from repository --&gt;
    &lt;/parent&gt;
    &lt;groupId&gt;com.example&lt;/groupId&gt;
    &lt;artifactId&gt;provider&lt;/artifactId&gt;
    &lt;version&gt;0.0.3&lt;/version&gt;
    &lt;name&gt;provider&lt;/name&gt;
    &lt;description&gt;Demo project for Spring Boot&lt;/description&gt;
    &lt;properties&gt;
        &lt;java.version&gt;1.8&lt;/java.version&gt;
        &lt;dubbo-boot.version&gt;3.0.4&lt;/dubbo-boot.version&gt;
        &lt;zkclient.version&gt;4.2.0&lt;/zkclient.version&gt;
    &lt;/properties&gt;
    &lt;dependencies&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
            &lt;scope&gt;test&lt;/scope&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;org.projectlombok&lt;/groupId&gt;
            &lt;artifactId&gt;lombok&lt;/artifactId&gt;
            &lt;version&gt;1.18.22&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;!-- dubbo-spring-boot依赖 --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.apache.dubbo&lt;/groupId&gt;
            &lt;artifactId&gt;dubbo-spring-boot-starter&lt;/artifactId&gt;
            &lt;version&gt;${dubbo-boot.version}&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.apache.dubbo&lt;/groupId&gt;
            &lt;artifactId&gt;dubbo-dependencies-zookeeper&lt;/artifactId&gt;
            &lt;version&gt;3.0.7&lt;/version&gt;
            &lt;type&gt;pom&lt;/type&gt;
        &lt;/dependency&gt;

    &lt;/dependencies&gt;

    &lt;!--配置当前工程保存在私服中的具体位置--&gt;
    &lt;distributionManagement&gt;
        &lt;repository&gt;
            &lt;!--和maven/settings.xml中server中的id一致，表示使用该id对应的用户名和密码--&gt;
            &lt;id&gt;test-release&lt;/id&gt;
            &lt;!--release版本上传仓库的具体地址--&gt;
            &lt;url&gt;http://192.168.88.100:8081/repository/test-release/&lt;/url&gt;
        &lt;/repository&gt;
        &lt;snapshotRepository&gt;
            &lt;!--和maven/settings.xml中server中的id一致，表示使用该id对应的用户名和密码--&gt;
            &lt;id&gt;test-snapshot&lt;/id&gt;
            &lt;!--snapshot版本上传仓库的具体地址--&gt;
            &lt;url&gt;http://192.168.88.100:8081/repository/test-snapshot/&lt;/url&gt;
        &lt;/snapshotRepository&gt;
    &lt;/distributionManagement&gt;

    &lt;build&gt;
        &lt;plugins&gt;
            &lt;plugin&gt;
                &lt;groupId&gt;org.apache.maven.plugins&lt;/groupId&gt;
                &lt;artifactId&gt;maven-compiler-plugin&lt;/artifactId&gt;
                &lt;version&gt;3.8.1&lt;/version&gt;
                &lt;configuration&gt;
                    &lt;source&gt;1.8&lt;/source&gt;
                    &lt;target&gt;1.8&lt;/target&gt;
                    &lt;encoding&gt;UTF-8&lt;/encoding&gt;
                &lt;/configuration&gt;
            &lt;/plugin&gt;

        &lt;/plugins&gt;
    &lt;/build&gt;

&lt;/project&gt;


```
1. application.yml文件
```
server:
  port: 8085

dubbo:
  application:
    name: provider
  registry:
    address: zookeeper://localhost:2181
    timeout: 600000
    parameters:
      blockUntilConnectedWait: 600000
  protocol:
    name: dubbo
    port: 20880
  scan:
    base-packages: com.example.provider.service



```

```
package com.example.provider.service;

/**
 * @author qeq
 * @date 2022-10-21 16:02
 */
public interface TestService {

    String test();
}


```

```
package com.example.provider.service.impl;

import com.example.provider.service.TestService;
import org.springframework.stereotype.Service;

/**
 * @author qeq
 * @date 2022-10-21 16:03
 */
@Service
public class TestServiceImpl implements TestService {

    @Override
    public String test() {
        return "TestServiceImpl";
    }
}


```

```
package com.example.provider;

import org.apache.dubbo.config.spring.context.annotation.EnableDubbo;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@EnableDubbo
public class ProviderApplication {

    public static void main(String[] args) {
        SpringApplication.run(ProviderApplication.class, args);
    }

}


```

项目 deploy 至私服中，方便consumer调用 <img src="https://img-blog.csdnimg.cn/6d31d6de351e48e7a356cb32ba0f2a61.png" alt="在这里插入图片描述">

### consumer项目：

pom文件：

```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd"&gt;
    &lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;
    &lt;parent&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-starter-parent&lt;/artifactId&gt;
        &lt;version&gt;2.2.6.RELEASE&lt;/version&gt;
        &lt;relativePath/&gt; &lt;!-- lookup parent from repository --&gt;
    &lt;/parent&gt;
    &lt;groupId&gt;com.example&lt;/groupId&gt;
    &lt;artifactId&gt;consumer&lt;/artifactId&gt;
    &lt;version&gt;0.0.1-SNAPSHOT&lt;/version&gt;
    &lt;name&gt;consumer&lt;/name&gt;
    &lt;description&gt;Demo project for Spring Boot&lt;/description&gt;
    &lt;properties&gt;
        &lt;java.version&gt;1.8&lt;/java.version&gt;
    &lt;/properties&gt;
    &lt;dependencies&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
            &lt;scope&gt;test&lt;/scope&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;org.projectlombok&lt;/groupId&gt;
            &lt;artifactId&gt;lombok&lt;/artifactId&gt;
            &lt;version&gt;1.18.22&lt;/version&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;com.example&lt;/groupId&gt;
            &lt;artifactId&gt;provider&lt;/artifactId&gt;
            &lt;version&gt;0.0.3&lt;/version&gt;
        &lt;/dependency&gt;
    &lt;/dependencies&gt;

    &lt;build&gt;
        &lt;plugins&gt;
            &lt;plugin&gt;
                &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
                &lt;artifactId&gt;spring-boot-maven-plugin&lt;/artifactId&gt;
            &lt;/plugin&gt;
        &lt;/plugins&gt;
    &lt;/build&gt;

&lt;/project&gt;


```

application.yml 文件：

```
server:
  port: 8086

dubbo:
  application:
    name: consumer
  registry:
    address: zookeeper://localhost:2181
  protocol:
    name: dubbo




```

```
package com.example.consumer;

import org.apache.dubbo.config.spring.context.annotation.EnableDubbo;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@EnableDubbo
public class ConsumerApplication {

    public static void main(String[] args) {
        SpringApplication.run(ConsumerApplication.class, args);
    }

}


```

```
package com.example.consumer.controller;


import com.example.provider.rpcservice.TestRpcService;
import org.apache.dubbo.config.annotation.DubboReference;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author qeq
 * @date 2022-10-21 14:21
 */
@RestController
@RequestMapping("/testController")
public class TestController {

    @DubboReference
    private TestRpcService testRpcService;

    /**
     *  127.0.0.1:8086/testController/test
     * @author qeq
     * @date 2022/10/21 14:22
     * @return String
     **/
    @RequestMapping("test")
    public String test(){
        String str = "success-consumer: ";
        System.out.println(str);
        String test = testRpcService.test();

        return str + test;
    }
}


```

测试之： 127.0.0.1:8086/testController/test <img src="https://img-blog.csdnimg.cn/f55488ddd9874bfe83dfbb495d262bb2.png" alt="在这里插入图片描述">
