
--- 
title:  JAVA校园闲置物品交易系统源码+数据库，为在校师生提供闲置物品发布、物品查询、物品交易等功能 
tags: []
categories: [] 

---
## 校园闲置平台

校园闲置物品交易系统，为在校师生提供闲置物品发布、物品查询、物品交易等功能。
- 使用JAVA编写的(javaweb和ssm)
### Summary
- - - - 
### 项目的技术栈
-  IoC容器:Spring -  web框架:SpringMVC (PHP版为ThinkPHP) -  orm框架:Mybatis -  安全框架:SpringSecurity -  数据源:Druid -  日志: SLF4J -  Json: FastJson -  前端框架:LayUI 
### 项目功能介绍
1.  进入系统之后可以通过搜索，个人中心功能来浏览别人的信息、还有发布自己的商品信息 <img src="https://img-blog.csdnimg.cn/img_convert/8f3f0899a93d37e9f4aed3bc85a487ff.png" alt="image"> <img src="https://img-blog.csdnimg.cn/img_convert/8239c9549d152cc9406d8933f6179f58.png" alt="image"> 1.  用户可以进行登录注册进入系统 <img src="https://img-blog.csdnimg.cn/1e04b65de1514a7bad0257822678bbb3.png" alt="在这里插入图片描述"> 
### 项目运行环境

环境搭建说明：
- 开发环境为jdk11，基于maven构建；- 使用eclipase或Intellij Idea开发(推荐使用Intellij Idea)- 基于SpringBoot搭建，大大简化了配置操作。- 本项目使用了lombok,在查看本项目时如果您没有下载lombok 插件，请先安装,不然找不到get/set方法；
运行环境

>  
 Java版 

- apache-tomcat-9.0.38- mysql-5.7.32-winx64
### 部署项目

完整代码下载地址：
<li> 配置环境、初始化项目 
  <ol>1.  下载Mysql,创建一个数据库名字为schooltrade,导入sql即可 1.  下载Tomcat 
配置开发环境
1. 使用IDE导入项目,之后配置项目启动方式,使用刚才下载好的Tomcat
权限介绍：
1. 管理员，默认账户为admin,密码为admin