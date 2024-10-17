
--- 
title:  【微信小程序】全局配置和windows节点常用配置 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主🏆 📃个人主页： 🔥系列专栏：🥇 💬个人格言：不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待💖💖💖 


<img src="https://img-blog.csdnimg.cn/75860e007264416dbfd5fc8c6f545ed3.gif#pic_center" alt="在这里插入图片描述"> 

#### 常用配置
- - - 


## 全局配置文件及常用配置项

小程序根目录下的app.json文件是小程序的全局配置文件，常用的配置项如下： pages 记录当前小程序所有页面的存放路径 windows 全局设置小程序窗口的外观 tabBar 设置小程序底部的tabBar效果 style 是否启用新版的组件样式

## 了解window节点常用的配置

|属性名|类型|默认值|说明
|------
|navigationBarTitleText|String|字符串|导航栏标题文字内容
|navigationBarBackgroundColor|HexColor|#00000|导航栏背景颜色，如#00000
|navigationTextStyle|String|white|导航栏标题颜色，仅支持black/white
|backgroundColor|HexColor|#fffff|窗口的背景色
|backgroundTextStyle|String|dark|下拉loading的样式，仅支持dark/light
|enablePullDownRefresh|Boolean|false|是否全局下拉刷新
|onReachBottomDistance|Number|50|页面上拉触发时距页面底部距离，单位为px

## 结束语

以上就是微信小程序之全局配置和windows节点常用配置项 持续更新微信小程序教程，欢迎大家订阅系列专栏 你们的支持就是hacker创作的动力💖💖💖

<img src="https://img-blog.csdnimg.cn/5b80ea7dab574ae5bb3fda934fe3f872.gif#pic_center" alt="在这里插入图片描述">
