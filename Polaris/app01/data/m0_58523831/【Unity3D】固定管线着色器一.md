
--- 
title:  【Unity3D】固定管线着色器一 
tags: []
categories: [] 

---
##### 1 前言

（Shader）是渲染管线中最重要的一环，Unity3D 底层基于 OpenGL 实现，读者可以通过  了解 Unity3D 渲染流程。

OpenGL 1.x 为固定管线，2.x 之后才支持可编程管线，Unity3D 固定管线着色器使用 ShaderLab 语言实现。ShaderLab 是 Unity  的服务语言，是基于命令的语言。

每个游戏对象需要绑定至少一个材质（Material）才能渲染，即使材质为 None，系统也会绑定一个默认的材质。每个材质都需要绑定一个Shader，系统一般默认绑定 Standard Shader，用户也可以绑定到自定义的 Shader 上。当用户创建好 Material 和 Shader 后，选中 Material，在 Inspector 窗口通过如下方式绑定到自定义 Shader 上：

<img src="https://img-blog.csdnimg.cn/37ed224711dc41f9a79e1c9e7d8f09be.png" alt="">

##### 2 Shader 代码框架

在 Assets 窗口
