
--- 
title:  Bean 的作用域 
tags: []
categories: [] 

---
singleton （默认）将单个 bean 定义限定为每个 Spring IoC 容器的单个对象实例。 prototype 将单个 bean 定义限定为任意数量的对象实例 request 将单个 bean 定义限定为单个 HTTP 请求的生命周期。也就是说，每个 HTTP 请求都有自己的 bean 实例，该实例是在单个 bean 定义的后面创建的。仅在web类型的 ApplicationContext有效。 session 将单个 bean 定义限定为 HTTP 会话的生命周期。仅在web类型的 ApplicationContext有效。 application 将单个 bean 定义限定为 ServletContext 的生命周期。仅在web类型的 ApplicationContext有效。 websocket 将单个 bean 定义限定为 WebSocket 的生命周期。仅在web类型的 ApplicationContext有效。
