
--- 
title:  Node.js+MySQL开发的B2C商城系统源码+数据库（微信小程序端+服务端），界面高仿网易严选商城 
tags: []
categories: [] 

---
下载地址：

#### NideShop商城（微信小程序端）
- 界面高仿网易严选商城(主要是2016年wap版)- 测试数据采集自网易严选商城- 功能和数据库参考ecshop- 服务端api基于Ｎode.js+ThinkJS+MySQL- 计划添加基于Vue.js的后台管理系统、PC版、Ｗap版
#### NideShop商城（服务端）
- 界面高仿网易严选商城(主要是2016年wap版)- 测试数据采集自网易严选商城- 功能和数据库参考ecshop- 服务端api基于Ｎode.js+ThinkJS+MySQL- 计划添加基于Vue.js的后台管理系统、PC版、Ｗap版
本项目需要配合微信小程序端使用，nideshop-mini-program

#### 本地开发环境配置
-  克隆项目到本地 -  创建数据库nideshop并导入项目根目录下的nideshop.sql 
```
CREATE SCHEMA `nideshop` DEFAULT CHARACTER SET utf8mb4 ;

```

>  
 注意数据库字符编码为utf8mb4 

- 更改数据库配置 src/common/config/database.js
```
const mysql = require('think-model-mysql');

module.exports = {
    handle: mysql,
    database: 'nideshop',
    prefix: 'nideshop_',
    encoding: 'utf8mb4',
    host: '127.0.0.1',
    port: '3306',
    user: 'root',
    password: '你的密码',
    dateStrings: true
};

```
- 填写微信登录和微信支付配置 src/common/config/config.js
```
// default config
module.exports = {
  default_module: 'api',
  weixin: {
    appid: '', // 小程序 appid
    secret: '', // 小程序密钥
    mch_id: '', // 商户帐号ID
    partner_key: '', // 微信支付密钥
    notify_url: '' // 微信异步通知，例：https://www.nideshop.com/api/pay/notify
  }
};

```
- 安装依赖并启动
```
npm install
npm start

```

访问http://127.0.0.1:8360/

#### 项目截图

<img src="https://img-blog.csdnimg.cn/img_convert/5b56bf126794710e39e3fed18b8ce145.png" alt="首页">

<img src="https://img-blog.csdnimg.cn/img_convert/dbf40718a692cf0fbbcece844423f7e1.png" alt="专题">

<img src="https://img-blog.csdnimg.cn/img_convert/f7112c1dc067898fab7260087915c100.png" alt="分类">

<img src="https://img-blog.csdnimg.cn/img_convert/db94b9845e50bd7cad718aa6285f8ecb.png" alt="商品列表">

<img src="https://img-blog.csdnimg.cn/img_convert/5f8088f5d9f8d60ee3a43994e7e7d86b.png" alt="商品详情">

<img src="https://img-blog.csdnimg.cn/img_convert/f6b09df80e5ea4f48ac0b272dc06f121.png" alt="购物车">

<img src="https://img-blog.csdnimg.cn/img_convert/aa13d86dd9b9676244269da8b8e63f10.png" alt="订单中心">

#### 功能列表
- 首页- 分类首页、分类商品、新品首发、人气推荐商品页面- 商品详情页面，包含加入购物车、收藏商品、商品评论功能- 搜索功能- 专题功能- 品牌功能- 完整的购物流程，商品的加入、编辑、删除、批量选择，收货地址的选择，下单支付- 会员中心（订单、收藏、足迹、收货地址、意见反馈） …
#### 项目结构

```
├─config                
├─lib
│  └─wxParse　　　
├─pages
│  ├─auth
│  │  ├─login
│  │  ├─register
│  │  └─reset
│  ├─brand
│  ├─brandDetail
│  ├─cart
│  ├─catalog
│  ├─category
│  ├─comment
│  ├─goods
│  ├─hotGoods
│  ├─index
│  ├─logs
│  ├─newGoods
│  ├─pay
│  ├─search
│  ├─shopping
│  │  ├─address
│  │  ├─addressAdd
│  │  └─checkout
│  ├─topic
│  ├─topicDetail
│  └─ucenter
│      ├─address
│      ├─addressAdd
│      ├─collect
│      ├─coupon
│      ├─feedback
│      ├─footprint
│      ├─index
│      ├─order
│      └─orderDetail
├─static
│  └─images
└─utils

```

下载地址：
