
--- 
title:  Vue编写的滑动拼图验证码前端及示例demo源码，vue滑动拼图验证码demo代码 
tags: []
categories: [] 

---
## vue-jigsaw-captcha

##### 介绍

Vue编写的滑动拼图验证码前端示例

##### 操作截图
- 默认状态 <img src="https://img-blog.csdnimg.cn/img_convert/3fb097a278d397e346cb4e12c754feaf.png" alt="open">- 滑动中 <img src="https://img-blog.csdnimg.cn/img_convert/78835c787c17aed0318f6cfee0342b34.png" alt="slice">- 操作成功 <img src="https://img-blog.csdnimg.cn/img_convert/2f73b2086506a60ef9ee65f10efc4362.png" alt="success">- 操作失败 <img src="https://img-blog.csdnimg.cn/img_convert/02428d8d122da35b298ac35ff311cf58.png" alt="error">
##### 软件架构
- vue: 2.5.2- vue-router: 3.0.1- axios: 0.18.0- element-ui: 2.9.0- animate.css: 3.7.2
##### 安装教程

```
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

```

##### 使用说明

完整代码下载地址：

###### Props

|Key|Type|Default|Description
|------
|show|Boolean|false|是否显示验证码弹窗
|router|String|‘’|验证成功后跳转路由
|register|Function||注册验证码方法
|login|Function||验证码校验及登录方法

###### Events

|Key|Attributes|Description
|------
|close||关闭验证码弹窗
