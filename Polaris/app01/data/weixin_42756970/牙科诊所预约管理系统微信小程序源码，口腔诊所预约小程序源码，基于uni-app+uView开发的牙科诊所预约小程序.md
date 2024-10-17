
--- 
title:  牙科诊所预约管理系统微信小程序源码，口腔诊所预约小程序源码，基于uni-app+uView开发的牙科诊所预约小程序 
tags: []
categories: [] 

---
##### 介绍

口腔医院预约平台小程序是基于uni-app+uView+HBuilder X开发的预约类小程序，目前小程序端还没有对接后端，只是一个单纯的演示项目,后期会考虑对接后端接口； 介于我是个小菜鸡，所以这个项目也写得很菜，很多地方都没有完善，如有任何问题可以提交issue。

##### 软件架构

###### 小程序端
- 开发工具：HBuilder X- UI框架：uView
##### 目录结构说明

```
|-- wx-dental-hospital
    |-- App.vue					#页面入口
	|-- components				#自定义组件
    |-- pages					#小程序页面	
    |   |-- appointment			#预约模块
    |   |-- authorize			#登录授权模块
    |   |-- detail				#预约下单模块
    |   |-- index				#首页模块
    |   |-- login				#登录模块
    |   |-- mine				#我的模块
    |   |-- order				#订单信息模块
    |   |-- physician			#医师模块
    |-- utils					#通用工具类

```

##### 平台模块说明
<li>首页 
  <ul>- 轮播图：牙科项目演示- 热门项目推荐- 医院宗旨- 医师团队- 名医推荐- 热门项目预约- 项目分类：项目详细信息- 个人信息- 订单信息
##### 安装教程
1. 下载该代码到你自己的电脑上
完整代码：
1.  使用HBuilder编辑器打开项目，如果你电脑上没有该编辑工具请下载：https://www.dcloud.io/hbuilderx.html 1.  找到/App.vue 1.  配置好的Hbuilder，例如设置好微信开发者工具的路径，小程序appid等，配置教程请参考uni-app官网：https://uniapp.dcloud.io/quickstart-hx 
##### 小程序端页面效果演示

<img src="https://img-blog.csdnimg.cn/234ff129f937439991b1cc8f9eecb72e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2afda368d47f4969a9a7f0986690f0e9.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e689d7ad226d4a54b20dc2ea5b254896.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f47bfa46facc4b03a798664020b92358.png" alt="在这里插入图片描述">
