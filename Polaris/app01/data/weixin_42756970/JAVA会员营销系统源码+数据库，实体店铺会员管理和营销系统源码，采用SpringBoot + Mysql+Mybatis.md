
--- 
title:  JAVA会员营销系统源码+数据库，实体店铺会员管理和营销系统源码，采用SpringBoot + Mysql+Mybatis 
tags: []
categories: [] 

---
## 会员营销系统介绍

##### 介绍

fuint会员营销系统是一套开源的实体店铺会员管理和营销系统。系统基于前后端分离的架构，后端采用**Java SpringBoot** + **Mysql**，前端基于当前流行的**Uniapp**，**Element UI**，支持小程序、h5。主要功能包含电子优惠券、预存卡、集次卡（计次卡）、短信发送、储值卡、会员积分、会员等级权益体系，支付收款等会员日常营销工具。本系统适用于各类实体店铺，如酒吧、酒店、汽车4S店、鲜花店、甜品店、餐饮店等，是实体店铺会员营销必备的一款利器。 后端下载地址： 前端下载地址：

以下是前台的页面展示：

<img src="https://fuint-cn.oss-cn-shenzhen.aliyuncs.com/screenshots/g1.png?v=1" alt="前台页面1">

<img src="https://fuint-cn.oss-cn-shenzhen.aliyuncs.com/screenshots/g2.png?v=1" alt="前台页面2">

<img src="https://fuint-cn.oss-cn-shenzhen.aliyuncs.com/screenshots/g3.png?v=1" alt="前台页面3">

<img src="https://fuint-cn.oss-cn-shenzhen.aliyuncs.com/screenshots/g4.png?v=1" alt="前台页面4">

<img src="https://fuint-cn.oss-cn-shenzhen.aliyuncs.com/screenshots/g5.png?v=1" alt="前台页面4">

fuint侧重于线下实体店的私域流量的运营，帮助商户降低获客成本。顾客通过扫码支付成为私域流量，支付即可成为会员。积分和卡券功能建立起会员等级体系，通过消息推送和短信营销方便触达用户。

1、会员运营自动化：商家通过日常活动设置，如开卡礼设置，沉睡唤醒等，成为会员后自动给顾客送优惠券，让顾客更有黏性，提升会员运营效率。

2、打通收银系统和会员营销的壁垒，代客下单收银，支付即成为会员。

3、会员体系完整化：积分兑换、积分转赠、会员等级权益、积分加速、买单折扣。

4、会员卡券齐全：预存卡、电子券、优惠券、集次卡、计次卡、会员余额支付。

5、线上代客下单收银系统，后台管理员可帮助临柜的会员下单、扫码支付。

6、支持手机短信、站内弹框消息、微信订阅消息：支持包括发货消息、卡券到期提醒、活动提醒、会员到期提醒、积分余额变动提醒等消息。

小程序前端：https://download.csdn.net/download/weixin_42756970/87388010

**官网演示地址：**

  账号:fuint / 123456 

##### 软件架构

后端：JAVA SpringBoot + MYSQL Mybatis Plus + Redis 前端：采用基于Vue的Uniapp、Element UI，前后端分离，支持微信小程序、支付宝小程、h5等

后台截图：

<img src="https://fuint-cn.oss-cn-shenzhen.aliyuncs.com/screenshots/login.png?v=fuint" alt="登录界面">

<img src="https://fuint-cn.oss-cn-shenzhen.aliyuncs.com/screenshots/homeV2.png?v=fuint" alt="首页">

前端使用技术 2.1 Vue2 2.2 Uniapp 2.3 Element UI

后端使用技术 1.1 SpringBoot 2.5 1.2 Mybatis Plus 1.3 Maven 1.4 SpringSecurity 1.5 Druid 1.6 Slf4j 1.7 Fastjson 1.8 JWT 1.9 Redis 1.10 Quartz 1.11 Mysql 5.8

##### 安装步骤

推荐软件环境版本：jdk 1.8、mysql 5.8
1. 导入db目录下的数据库文件。1. 修改config目录下的配置文件。1. 将工程打包，把jar包上传并执行。
提示：无后端和linux基础的朋友，可以使用**宝塔**部署，非常方便简单。

##### 前台使用说明
1. 会员登录，登录成功后可看到会员的卡券列表。1. 卡券领取和购买，预存券的充值等。1. 核销卡券，会员在前台出示二维码，管理员用微信扫一扫即可核销。1. 卡券转赠，会员可将自己的卡券转赠给其他用户，输入对方的手机号即可完成转赠，获赠的好友会收到卡券赠送的短信。
<img src="https://img-blog.csdnimg.cn/510b59f1eb824b6b8de428fbe1aeaf3e.png" alt="在这里插入图片描述">

<img src="https://fuint-cn.oss-cn-shenzhen.aliyuncs.com/screenshots/member.png?v=fuint">

##### 后台使用
1. 会员管理：会员新增、导入、禁用等。1. 卡券管理：电子券管理为2层结构，即电子券组和电子券。1. 会员积分：会员积分管理，会员积分的操作，会员积分明细查看。1. 转赠管理：卡券转赠记录。1. 短信管理：短信营销功能，已发送的短信列表。1. 系统配置：配置系统管理员权限等。1. 店铺管理：支持多店铺模式。1. 核销管理员:核销人员管理主要包含3个功能：核销人员列表、核销人员审核、核销人员信息编辑。1. 短信模板管理：可配置不同场景和业务的短信内容。1. 卡券发放：单独发放、批量发放，发放成功后给会员发送短信通知1. 操作日志主要针对电子券系统后台的一些关键操作进行日志记录，方便排查相关操作人的行为等问题。1. 发券记录主要根据发券的实际操作情况来记录，分为单用户发券和批量发券，同时可针对该次发券记录进行作废操作。 13.代客下单收银功能。
卡券营销：

<img src="https://fuint-cn.oss-cn-shenzhen.aliyuncs.com/screenshots/coupon-list.png?v=fuint" alt="卡券列表">

收银代客下单功能：店员角色登录后台，从首页的“下单首页”菜单可进入代客收银下单界面，完成代客下单收银的流程。

<img src="https://fuint-cn.oss-cn-shenzhen.aliyuncs.com/screenshots/cashier.png?v=fuint" alt="收银界面">

发起结算：

<img src="https://fuint-cn.oss-cn-shenzhen.aliyuncs.com/screenshots/cashier-1.png?v=fuint" alt="收银结算">

##### 开发计划
1. 完善的报表统计1. 接入支付宝支付1. 分享助力、分享领券、分享获得积分1. 更多营销工具…