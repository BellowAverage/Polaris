
--- 
title:  基于Springboot+vue+uni-app的校园失物招领平台源码+数据库，含主体PC端、微信小程序和web后台数据管理平台 
tags: []
categories: [] 

---
##  校园失物招领网站 | lijinghai 

    

  

#### 项目介绍 📖

👉基于Springboot+vue+uni-app的校园失物招领平台. 含平台主体PC端、微信小程序和web后台数据管理平台.

完整代码下载地址：
- 失物招领信息一览- 信息发布(支持图片上传)
#### 项目技术栈 ⭐️
- PC端（WarmSearch-PC)：`Vue 2.0`+`Vue-router`+`Vuex`+`Element-ui`+`Axios`- 后台管理系统(WarmSearch-Web)：基于Vue-admin-ui脚手架- 微信小程序(WarmSearch-uniapp)：uni-app + Vue.js- 后端(WarmSearch)：Springboot 2.4.2 + Java Web Token +MybatisPlus + Swagger- 数据库：MySql 5.7
#### 项目地址 🔗

项目采用前后端分离开发模式，PC端使用:Vue + Element-ui, 小程序使用Uni-app开发，后端数据API采用Java、Spring-Boot开发.

PC端Code地址：WarmSearch-PC

小程序端code地址：WarmSearch-uniapp

后端code地址：WarmSearch

web管理端code地址: WarmSearch-Web

#### 体验地址

由于项目还在不断完善中，所以目前还未上线；

主要还是因为穷，买不起服务器

演示视频：

### 说明

>  
 本项目采用前后端分离技术 Springboot + vue + uniapp + Mysql 
 <blockquote> 
  1.本项目包括后台管理系统 2.前台系统 3.微信小程序部分 
 

### 项目简介
-  本项目前后端分离，前端基于`Vue`+`Vue-router`+`Vuex`+`Element-ui`+`Axios`，参考锤子商城实现。后端基于SpringBoot(框架) + JSON WEB TOKEN(令牌机制) + MybatisPlus + Mysql实现。 -  总体架构 系统设计秉承“前后端分离/SOA”的总体思想，前端使用Vue/ElementUI作为主要框架技术、Nginx作为HTTP服务器，用来提供静态页面访问服务和反向代理作用；后端则以Springboot主流框架技术为主、采用MySQL开源数据库，前后端使用Restful规范交换数据。 系统采用JWT令牌鉴权方式，降低服务器运行消耗，提升系统的伸缩性和扩展性。 -  总体架构 总体设计按“前后端分离”方式，当浏览器请求页面或静态资源时，HTTP Server直接响应；当浏览器请求数据时，该请求仍然先发给HTTP Server，经由该Server转发至Web APP Server。Web APP Server业务处理后将结果数据返回给HTTP Server，最终返回浏览器。在此过程中，Web APP Server返回的仅仅是数据（json格式），没有任何与显示（视图）相关的信息，做到了完全的前后端分离，前端负责页面与展示，后端负责业务处理与数据。 
### 技术栈
- 前台页面展示系统（WarmSearch-PC)：`Vue`+`Vue-router`+`Vuex`+`Element-ui`+`Axios`- 后台管理系统：基于Vue-admin-ui脚手架- 微信小程序：uni-app + Vue.js- 后端：Springboot + Java Web Token +MybatisPlus + Swagger 框架- 数据库：MySql
完整代码下载地址：
