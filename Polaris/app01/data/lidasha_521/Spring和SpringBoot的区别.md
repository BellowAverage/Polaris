
--- 
title:  Spring和SpringBoot的区别 
tags: []
categories: [] 

---
**Spring**
- Spring是一个开源框架，主要用于Java平台。- 它设计出来是为了简化在J2EE环境下的开发和测试进程。- Spring框架是用于开发各种企业应用的全面解决方案，它可以提供大量的模块，如IOC, AOP, DAO, MVC等，用户可以根据业务需要选择使用。
**SpringBoot**
- Spring Boot是基于Spring的一个框架，用于简化Spring应用的初始建设和开发过程的。- 自动配置Spring和其他相关的技术，并包括一键启动运行应用的功能。- Spring Boot可以帮助快速建立独立的、生产级的Spring应用。
**下面是Spring和Spring Boot的主要区别：**
- 配置 **Spring**: 在Spring中，需要自行进行大量配置。我们需要自己指定所有的库的版本，需要自己去写web.xml等配置文件。 **SpringBoot**: 在Spring Boot中，配置会被严重简化。Spring Boot通过自动配置和起步依赖为应用自动配置部分环境。- 开发和测试 **Spring**: 在Spring环境中，开发和测试通常需要额外的设置，如服务器设置或者加载应用到服务器上等等。 **SpringBoot**: Spring Boot内置了服务器，可以使用Java应用来运行Spring Boot应用。- 依赖管理 **Spring**: 在Spring中，开发者需要自己管理并保证所有库和框架的兼容性。 **SpringBoot**: Spring Boot协助管理依赖，并且收到了Spring团队全面的测试，可以大大降低版本冲突的可能性。