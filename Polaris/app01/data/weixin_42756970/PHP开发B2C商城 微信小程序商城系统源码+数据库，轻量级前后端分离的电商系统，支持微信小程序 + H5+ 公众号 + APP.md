
--- 
title:  PHP开发B2C商城 微信小程序商城系统源码+数据库，轻量级前后端分离的电商系统，支持微信小程序 + H5+ 公众号 + APP 
tags: []
categories: [] 

---
##### 项目介绍

一款轻量级、高性能、前后端分离的电商系统，支持微信小程序 + H5+ 公众号 + APP，前后端源码完全开源，看见及所得，完美支持二次开发，可学习可商用，让您快速搭建个性化独立商城。

完整代码下载地址：

##### 技术特点
- 前后端完全分离 (互不依赖 开发效率高)- 采用PHP7.4 (强类型严格模式)- Thinkphp6.0.5（轻量级PHP开发框架）- Uni-APP（开发跨平台应用的前端框架）- Ant Design Vue（企业级中后台产品UI组件库）- RBAC（基于角色的权限控制管理）- Composer一键引入三方扩展- 部署运行的项目体积仅30多MB（真正的轻量化）- 所有端代码开源 (服务端PHP、后台vue端、uniapp端)- 简约高效的编码风格 (可能是最适合二开的源码)- 源码中清晰中文注释 (小白也能看懂的代码)
##### 页面展示

<img src="https://img-blog.csdnimg.cn/8e84e01b8da842259207aff14c26a6a1.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/3865b01446054c4a8cf9656c149f7aa1.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/91a8407ca7cb46c8a109a21c124559b3.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d925f70f92bf447987e7325358f583e2.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/fa6bcd80bae34091951070459e2d70d2.png" alt="在这里插入图片描述">

##### 系统演示
- 商城后台演示：https://shop2.yiovo.com/admin/- 用户名和密码：admin yinghuo
##### 源码下载
1.  主商城端（又称后端、服务端，PHP开发 用于管理后台和提供api接口） yoshop2.0 1.  用户端（也叫客户端、前端，uniapp开发 用于生成H5和微信小程序） yoshop2.0-uniapp 
##### 代码风格
- PHP7强类型严格模式- 严格遵守MVC设计模式 同时具有service层和枚举类enum支持- 简约整洁的编码风格 绝不冗余一行代码- 代码注释完整易读性高 尽量保障初级程序员也可读懂 极大提升二开效率- 不允许直接调用和使用DB类（破坏封装性）- 不允许使用原生SQL语句 全部使用链式操作（可维护性强）- 不允许存在复杂SQL查询语句（可维护性强）- 所有的CURD操作均通过ORM模型类 并封装方法（扩展性强）- 数据库设计满足第三范式- 前端JS编码均采用ES6标准
##### 环境要求
- CentOS 7.0+- Nginx 1.10+- PHP 7.1+ (推荐php7.4)- MySQL 5.6+
##### 如何安装

###### 一、自动安装（推荐）
1. 将后端源码上传至服务器站点，并且将站点运行目录设置为/public1. 在浏览器中输入站点域名 + /install，例如：https://www.你的域名.com/install1. 根据页面提示，自动完成安装即可
###### 二、手动安装（不推荐）
1. 将后端源码上传至服务器站点，并且将站点运行目录设置为/public1. 创建一个数据库，例如：yoshop2_db1. 导入数据库表结构文件，路径：/public/install/data/install_struct.sql1. 导入数据库默认数据文件，路径：/public/install/data/install_data.sql1. 修改数据库连接文件，将数据库用户名密码等信息填写完整，路径/.env
##### 后台地址
- 超管后台：https://www.你的域名.com/admin- 商户后台：https://www.你的域名.com/store- 默认的账户密码：admin yinghuo
##### 定时任务

用于自动处理订单状态、优惠券状态、会员等级等

```
php think timer start

```

## [uni-app端]

##### 如何使用uni-app端

###### 一、导入uniapp项目

```
1. 首先下载HBuilderX并安装，地址：https://www.dcloud.io/hbuilderx.html
2. 打开HBuilderX -&gt; 顶部菜单栏 -&gt; 文件 -&gt; 导入 -&gt; 从本地目录导入 -&gt; 选择uniapp端项目目录
3. 找到config.js文件，找到里面的apiUrl项，填入已搭建的后端url地址
4. 打开manifest.json文件，选择微信小程序配置，填写小程序的appid

```

###### 二、本地调试

```
1. 打开HBuilderX -&gt; 顶部菜单栏 -&gt; 运行 -&gt; 运行到浏览器 -&gt; Chrome
2. 如果请求后端api时 提示跨域错误，可安装Chrome插件：【Allow CORS: Access-Control-Allow-Origin】，地址：https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf

```

###### 三、打包发行（H5）

```
1. 打开HBuilderX -&gt; 顶部菜单栏 -&gt; 发行 -&gt; 网站H5-手机版
2. 打包后的文件路径：/unpackage/dist/build/h5
3. 将打包完成的所有文件 复制到商城后端/pulic目录下，全部替换

```

###### 四、打包发行（微信小程序）

```
1. 下载微信开发者工具并安装，地址：https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html
2. 打开HBuilderX -&gt; 顶部菜单栏 -&gt; 发行 -&gt; 小程序-微信
3. 打包后的文件路径：/unpackage/dist/build/mp-weixin
5. 打开微信开发者工具 导入 打包完成的项目
6. 检查没有运行错误，在右上方上传小程序

```

完整代码下载地址：
