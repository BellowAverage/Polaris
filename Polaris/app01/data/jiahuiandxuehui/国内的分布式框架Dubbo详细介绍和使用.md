
--- 
title:  国内的分布式框架Dubbo详细介绍和使用 
tags: []
categories: [] 

---
## 介绍

Dubbo 是一款高性能、轻量级的 Java RPC 框架，由阿里巴巴开源并贡献至 Apache 基金会。它能够提供服务的注册与发现、负载均衡、服务治理等功能，简化了分布式系统的开发过程。下面我们将详细介绍 Dubbo 的原理和使用方法，并附上相关的 Java 代码示例。

#### Dubbo的原理

Dubbo 的核心是一个基于 Java 序列化的远程过程调用（RPC）框架，它的工作流程可以分为如下几个步骤：
1. 服务提供者向注册中心注册自己提供的服务。1. 服务消费者从注册中心获取服务提供者的地址，并建立连接。1. 服务消费者通过 RPC 调用远程服务，实现分布式调用
Dubbo 的架构中包含以下几个重要组件：
1. Provider：服务提供者，将服务发布到注册中心，供 Consumer 调用。1. Consumer：服务消费者，从注册中心获取 Provider 的地址，并发起 RPC 调用。1. Registry：注册中心，存储 Provider 的地址信息，供 Consumer 获取。1. Monitor：监控中心，用于统计 Provider 的运行状态和性能指标。 <img src="https://img-blog.csdnimg.cn/a4d45ae149b94dcbb1b4fe48cc156352.png" alt="在这里插入图片描述">
Dubbo 支持多种协议和序列化方式，包括 Dubbo 协议、HTTP 协议、Hessian 协议、Thrift 协议等。同时，它还提供了负载均衡、服务容错、动态路由等功能，可以根据不同的需求进行配置。

## 基本使用
- 编写服务接口
```
public interface HelloService {<!-- -->
    String sayHello(String name);
}


```
- 实现服务接口
```
public class HelloServiceImpl implements HelloService {<!-- -->
    public String sayHello(String name) {<!-- -->
        return "Hello, " + name;
    }
}


```
- 配置Dubbo 在Dubbo的XML配置文件中定义服务提供者和注册中心，配置服务接口和实现类的关联。
```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:dubbo="http://dubbo.apache.org/schema/dubbo"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://dubbo.apache.org/schema/dubbo http://dubbo.apache.org/schema/dubbo/dubbo.xsd"&gt;

    &lt;!-- 指定服务提供者应用名 --&gt;
    &lt;dubbo:application name="hello-provider"/&gt;

    &lt;!-- 指定注册中心地址 --&gt;
    &lt;dubbo:registry address="zookeeper://127.0.0.1:2181"/&gt;

    &lt;!-- 指定通信协议和端口号 --&gt;
    &lt;dubbo:protocol name="dubbo" port="20880"/&gt;

    &lt;!-- 暴露服务 --&gt;
    &lt;dubbo:service interface="com.example.HelloService" ref="helloService"/&gt;

    &lt;!-- 服务接口和实现类的关联 --&gt;
    &lt;bean id="helloService" class="com.example.provider.HelloServiceImpl"/&gt;
&lt;/beans&gt;


```
- 启动服务提供者 在服务提供者的main方法中启动Dubbo。
```
public class Provider {<!-- -->
    public static void main(String[] args) throws Exception {<!-- -->
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("provider.xml");
        context.start();
        System.in.read(); // 按任意键退出
    }
}


```

服务提供者通过启动 Spring 容器来启动 Dubbo 服务，这里使用的是 ClassPathXmlApplicationContext，它会从类路径下加载 provider.xml 文件，初始化 Spring 容器并启动 Dubbo 服务。
- 编写服务消费者
```
public class Consumer {<!-- -->
    public static void main(String[] args) {<!-- -->
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("consumer.xml");
        HelloService helloService = (HelloService) context.getBean("helloService");
        String result = helloService.sayHello("world");
        System.out.println(result);
    }
}


```
- 配置Dubbo 在Dubbo的XML配置文件中定义服务消费者和注册中心。
```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:dubbo="http://dubbo.apache.org/schema/dubbo"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://dubbo.apache.org/schema/dubbo http://dubbo.apache.org/schema/dubbo/dubbo.xsd"&gt;

    &lt;!-- 指定服务消费者应用名 --&gt;
    &lt;dubbo:application name="hello-consumer"/&gt;

    &lt;!-- 指定注册中心地址 --&gt;
    &lt;dubbo:registry address="zookeeper://127.0.0.1:2181"/&gt;

    &lt;!-- 引用远程服务 --&gt;
    &lt;dubbo:reference id="helloService" interface="com.example.HelloService"/&gt;

&lt;/beans&gt;


```
- 启动服务消费者
```
public class Consumer {<!-- -->
    public static void main(String[] args) {<!-- -->
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("consumer.xml");
        HelloService helloService = (HelloService) context.getBean("helloService");
        String result = helloService.sayHello("world");
        System.out.println(result);
    }
}


```

简单的使用就是这样，关于zookeeper我们下次在详细说一下。
