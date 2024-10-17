
--- 
title:  JAVA单商户商城系统源码,前(vue)后(SpringBoot)端分离,支持多平台(h5,小程序,app) 
tags: []
categories: [] 

---
## 前言

完整代码下载地址：
-  linjiashop 是一个基于和的web商城系统 -  linjiashop 包含了商城的后台管理系统,手机h5，小程序版本 -  linjiashop 采用作为底层基础框架搭建，开发过程遇到问题请多阅读该项目文档。 -  linjiashop 是一个采用MIT协议的开源商城系统，任何人任何单位可以免费使用该商城和基于该项目开发搭建自己的商城系统。 
### 演示

#### 演示环境(没有配置下单发短信等功能)
- 用户端H5(基于vue.js)： 演示账号/密码：15011112222/admin- 用户端H5(基于uniapp) 演示账号/密码：15011112222/admin- App(基于uniapp) 演示账号/密码：15011112222/admin- 后台管理： 管理员账号/密码：admin/admin<li>演示环境在线swagger文档： 
  <ul>- 后台管理：http://linjiashop-admin.microapp.store/prod-api/swagger-ui.html- 用户端：http://linjiashop.microapp.store/prod-api/swagger-ui.html
### 功能模块

linjiashop包含了后台管理功能和手机端商城业务功能
<li>基础模块 
  <ul>- 部门管理- 用户管理- 角色管理- 菜单管理- 权限分配- 参数管理- 数据字典管理- 定时任务管理- 操作日志- 登录日志- cms内容管理- 消息管理：配置消息模板，发送短信，邮件消息- 基于idea插件的代码生成- 会员管理- 商品类别- 商品管理- 订单管理- 购物车- banner管理- 收藏列表
### 运行效果图

**商品素材取自小米商城**

#### 手机端H5

<img src="https://img-blog.csdnimg.cn/9c06d5d5c8da4dbebb1b9f07132a7a78.png" alt="在这里插入图片描述">

#### IOS

<img src="https://img-blog.csdnimg.cn/4131d65bc5344e05be0592a665a6485b.png" alt="在这里插入图片描述">

#### Android

<img src="https://img-blog.csdnimg.cn/069ec7bdd3304bafbf05a52870f8226c.png" alt="在这里插入图片描述">

#### 后台管理

<img src="https://img-blog.csdnimg.cn/0c5700c9d6024fbd83040078b89ad66c.png" alt="在这里插入图片描述">

### 技术选型
- 核心框架：Spring Boot- 数据库层：Spring data jpa- 数据库连接池：Druid- 缓存：Ehcache- 前端：后台管理基于，手机端界面基于
### 目录说明
- linjiashop-admin PC端后台管理的前端网页- linjiashop-admin-api PC端后台管理的api服务- linjiashop-mobile 手机商城的前端网页- linjiashop-mobile-api 移动端商城的api服务（h5,小程序，app都用改api服务作为后台接口）- linjiasho-wxapp 微信小程序商城- linjiashop-core 基础模块，包括工具类，dao，service，bean等内容- linjiashop-generator 代码生成模块,根据实体生成dao,service,后台管理的controller和页面,配合IDEA 代码生成插件使用效果更好，使用前请仔细阅读该
### 快速开始
- 克隆本项目- 导入idea或者eclipse- 确保开发工具下载并安装了lombok插件，另外由于lombok有版本差异，如果出现问题，可以更新maven以来中lombok的版本来解决<li>创建数据库：linjiashop<pre><code class="prism language-sql">CREATE DATABASE IF NOT EXISTS linjiashop DEFAULT CHARSET utf8 COLLATE utf8_general_ci; 
CREATE USER 'linjiashop'@'%' IDENTIFIED BY 'linjiaSHOP@191028';
GRANT ALL privileges ON linjiashop.* TO 'linjiashop'@'%';
flush privileges;
</code></pre> </li>- 下载项目测试数据的图片：链接：https://pan.baidu.com/s/1i06H4dAM1M7mYQU9etBrfw 提取码：mqvf ，将图片存放到t_sys_cfg表中system.file.upload.path配置的目录下(注意该目录为绝对路径，该目录可以通过“系统管理”-“参数管理”进行配置)<li>启动后台管理 
  <ul><li>启动后台管理api服务:linjiashop-admin-api 
    <ul><li>修改linjiashop-admin-api中数据库连接配置<pre><code class="prism language-properties">## 首次启动需要设置下列配置项设置为create，以便系统可以自动创建表并导入./import.sql测试数据文件
## 如果下面配置无法自动建表并导入测试数据文件；则可以手动初始化数据库，手动使用的初始化文件文件位于：doc/database.sql
spring.jpa.hibernate.ddl-auto=create
</code></pre> </li>- 启动linjiashop-admin-api主类：cn.enilu.flash.api.AdminApiApplication，访问http://localhost:8082/swagger-ui.html ， 保证api服务启动成功- 运行 npm install --registry=https://registry.npmmirror.com- 运行npm run dev- 启动成功后访问 http://localhost:9528 ,登录，用户名密码:admin/admin<li>启动手商城的api服务:linjiashop-mobile-api 
    <ul>- 修改linjiashop-mobile-api中数据库连接欸配置- 启动linjiashop-mobile-api主类：cn.enilu.flash.MobileApiApplication,访问http://localhost:8081/swagger-ui.html ， 保证api服务启动成功- 运行 npm install --registry=https://registry.npmmirror.com- 运行npm run dev- 启动成功后访问 http://localhost:8080/#/index- 首先启动后台api服务，和h5公用一个后台服务，即：linjiashop-mobile-api<li>进入linjiashop-wxapp目录 
    <ul>- 运行 npm install --registry=https://registry.npmmirror.com- 运行npm run dev- 启动微信开发工具导入linjiashop-wxapp/dist/wx 目录即可预览小程序
### 在线文档
- 项目文档：- 该项目克隆并扩展自web-flash,所以开发的时候多看看web-flash的- 该项目手机端linjiashop-mobile使用有赞Vant组件库，开发过程可以参考Vant的- 该项目微信小程序使用mpvue+vant-weapp，开发过程请参考相关文档：,- 该项目的业务功能和部分功能代码参考复用了，感谢- 
完整代码下载地址：
