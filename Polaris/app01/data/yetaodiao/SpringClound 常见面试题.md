
--- 
title:  SpringClound 常见面试题 
tags: []
categories: [] 

---
## SpringClound 常见面试题

1、单体应用存在哪些问题。

　　答：1）。代码结构混乱

              2）。开发效率降低，多人开发代码合并，修改一处逻辑，可能影响全部功能。

              3）。排查解决问题成本高。单体系统部署在一个进程内，我们修改了一个很小的功能，为了部署上线，可能会影响其他功能的运行。

              4）。扩展能力受限，有的模块是计算密集型的，需要强大的cpu，有的是io密集型的，需要更大的内存，这些模块部署在一起，不得不做出硬件上的选择。比如有的微服务，专门做图片的上传和下载，就比单体应用做上传和下载好。

              5）。阻碍技术创新，一直用单体应用，很多技术都限制死了，无法自由发挥。比如以前使用struts2，不能切换为springmvc。

<img alt="" height="408" src="https://img-blog.csdnimg.cn/fba2d7f0347e43b8a19c361b4c1fbb05.png" width="889">

 

2、Spring Cloud有什么组件。

答：一般回答五大组件：1、服务发现Netflix Eureka；2、客服端负载均衡Netflix Ribbon；3、断路器Netflix Hystrix；4、服务网关Netflix Zuul；5、分布式配置。
1. Spring Cloud config:配置管理工具。1. Spring Cloud netflix:
　　　　Eureka：服务治理组件，包含服务注册中心，服务注册于发现机制的实现。

              Hystrix：（hi check（检查一下））断路器，容错管理组件，帮助服务就来中出现的延迟和为故障提供强大的容错能力。

　　　　Ribbon：（risk 本）客户端负载均衡的服务调用组件。

　　　　Feign：基于Ribbon和Hystrix的声明式服务调用组件。

　　　　Zuul：网关组件，提供智能路由，访问过滤等功能

　　　　Archaius：外部化配置组件

        3. Spring Cloud Bus：消息总线，用于创博急群众的状态变化或事件，以触发后续的处理，比如用来动态刷新配置。

　　　　例如，配合Spring Cloud Config实现微服务应用配置信息的动态更新。

　　 4. Spring Cloud Stream：通过Redis，Rabbit或者kafka实现的消费微服务，可以通过简单的声明式模型来发送或者接受消息。

　　 5. Spring Cloud Sleuth：Spring Cloud应用的分布式跟踪实现，可以完美结合Zipkin

　　 6. Spring Cloud ZooKeeper: 基于ZooKeeper的服务发现与配置管理组件。

       springCloud最新组件消息：

　　1.注册中心与配置中心。springcloud Eureka,springcloud alibaba nacos,springcloud consul,sprongcloud zookeeper

　　2.服务调用。openfeign，restTemplate，ribbon

　　3.服务网关。zuul，springcloudGateway

　　4.消息组件。springcloud stream，springcloud bus

　　5.链路跟踪。sleuth+zipkin。skywalking

　　6.springcloud config配置中心。git，springcloud Bus

　　7.安全控制。springcloud springsecurity/oauth2,jwt

　　8.限流、降级。hystrix，springcloud alibaba sentinel

　　9.springCloud alibaba阿里系技术栈继承

3、 什么是Spring Cloud？

答：它利用Spring Boot的开发便利性巧妙地简化了分布式系统基础设施的开发，如服务发现注册、配置中心、智能路由、消息总线、负载均衡、断路器、数据监控等，都可以用Spring Boot的开发风格做到一键启动和部署。Spring Cloud并没有重复制造轮子，它只是将各家公司开发的比较成熟、经得起实际考验的服务框架组合起来，通过Spring Boot风格进行再封装屏蔽掉了复杂的配置和实现原理，最终给开发者留出了一套简单易懂、易部署和易维护的分布式系统开发工具包。结论就是，springcloud是一套基于springBoot的分布式系统开发工具包。

4、 springBoot和springcloud的区别。

答：第一，定位不同，springBoot是快速便捷的开发个体微服务。springcloud关注全局的服务治理

　　第二、依赖关系不同，springBoot可以离开springcloud单独开发项目，springCloud离不开springboot。

5、 服务注册和发现是什么意思？Spring Cloud 如何实现？ 答：服务注册，是把你这个微服务的信息注册到服务中心，类似于EurEka。

　　服务发现，是指，你从服务中心，获取相关的信息。

　　Springcloud如何实现：通过Eureka 服务器实现，把注册信息，写入Eureka

6、Spring Cloud 和dubbo区别?

7、Spring Cloud Gateway与Zuul的区别？

8、什么是服务熔断？什么是服务降级？ 熔断机制是应对雪崩效应的一种微服务链路保护机制。当某个微服务不可用或者响应时间太长时，会进行服务降级，进而熔断该节点微服务的调用，快速返回“错误”的响应信息。当检测到该节点微服务调用响应正常后恢复调用链路。在Spring Cloud框架里熔断机制通过Hystrix实现，Hystrix会监控微服务间调用的状况，当失败的调用到一定阈值，缺省是5秒内调用20次，如果失败，就会启动熔断机制。

服务降级，一般是从整体负荷考虑。就是当某个服务熔断之后，服务器将不再被调用，此时客户端可以自己准备一个本地的fallback回调，返回一个缺省值。这样做，虽然水平下降，但好歹可用，比直接挂掉强。

Hystrix相关注解@EnableHystrix：开启熔断 @HystrixCommand(fallbackMethod=”XXX”)，声明一个失败回滚处理函数XXX，当被注解的方法执行超时（默认是1000毫秒），就会执行fallback函数，返回错误提示。  


