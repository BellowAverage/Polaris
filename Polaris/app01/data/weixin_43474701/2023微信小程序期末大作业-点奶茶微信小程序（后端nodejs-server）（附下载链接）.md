
--- 
title:  2023微信小程序期末大作业-点奶茶微信小程序（后端nodejs-server）（附下载链接） 
tags: []
categories: [] 

---
### 2023微信小程序期末大作业-点奶茶微信小程序



项目启动： 1.导入项目微信小程序项目wx-xiao-server到微信开发工具，替换自己的oppid 2.安卓nodejs环境 3.进入nodejs-server目录下,使用cmd进入到当前项目，使用node exp.js 命令启动后台服务 首页展示： <img src="https://img-blog.csdnimg.cn/direct/7edb00a923004f3fa43c3796c4ccc5be.png" alt="在这里插入图片描述"> 菜单展示 <img src="https://img-blog.csdnimg.cn/direct/402c3aad2ccb423e8dc6fb5a2766b679.png" alt="在这里插入图片描述"> 购物车展示： <img src="https://img-blog.csdnimg.cn/direct/9bc048d0b6a94c75b0b059aa905f0bb2.png" alt="在这里插入图片描述"> 提交订单： <img src="https://img-blog.csdnimg.cn/direct/18f8c65b9dcb4810a9329e8262162290.png" alt="在这里插入图片描述"> 支付详情页展示：

订单查看：

查看历史消费：

部分代码展示：

```
&lt;!--pages/home/home.wxml--&gt;
&lt;block wx:for="{<!-- -->{listData}}" wx:key="itemlist"&gt;
  &lt;!-- 菜单轮播图 --&gt;
  &lt;swiper indicator-dots="{<!-- -->{indicatorDots}}" autoplay="{<!-- -->{autoplay}}" interval="{<!-- -->{interval}}" duration="{<!-- -->{duration}}"&gt;
    &lt;block wx:for="{<!-- -->{item.imgUrls}}" wx:for-item="imgItem" wx:key="{<!-- -->{item.id}}"&gt;
      &lt;swiper-item&gt;
        &lt;image class="slide-image" src="{<!-- -->{imgItem.src}}"&gt;&lt;/image&gt;
      &lt;/swiper-item&gt;
    &lt;/block&gt;
  &lt;/swiper&gt;
  &lt;!--开启点餐之旅 --&gt;
  &lt;view class="menu-bar"&gt;
    &lt;view class="menu-block" bindtap="gostart"&gt;
      &lt;view class="menu-start"&gt;开启点餐之旅→&lt;/view&gt;
    &lt;/view&gt;
  &lt;/view&gt;
  &lt;!-- 中间部分 --&gt;
  &lt;view class="ad-box"&gt;
    &lt;image src="{<!-- -->{item.image_ad}}" class="image-ad"&gt;&lt;/image&gt;
  &lt;/view&gt;
  &lt;!-- 底部商品图 --&gt;
  &lt;view class="bottom-box"&gt;
    &lt;view class="bottom-pic" wx:for="{<!-- -->{item.image_bottom}}" wx:for-item="bottomItem" wx:key="{<!-- -->{item.id}}"&gt;
      &lt;image src="{<!-- -->{bottomItem.src}}" class="btm-image" data-id="{<!-- -->{bottomItem.id}}"&gt;&lt;/image&gt;
    &lt;/view&gt;
  &lt;/view&gt;
&lt;/block&gt;

```

// pages/home/home.js const fetch = require(‘…/…/utils/fetch.js’) Page({<!-- --> data: {<!-- --> // 显示面板指示点 indicatorDots: true, // 图片自动切换 autoplay: true, // 自动切换时间间隔 interval: 5000, // 滑动动画时长 duration: 1000 }, onLoad: function(options) {<!-- --> // 显示模态对话框 wx.showLoading({<!-- --> title: “努力加载中” }) // 请求数据 fetch(‘food/index’).then((res) =&gt; {<!-- --> // 请求成功，关闭对话框 wx.hideLoading(); // 把接口返回数据setData给listData this.setData({<!-- --> listData: res.data, }) },() =&gt; {<!-- --> // 请求失败，关闭对话框，执行fetch.js文件中的fail方法 wx.hideLoading(); }); }, gostart: function() {<!-- --> wx.navigateTo({<!-- --> url: “…/list/list”, }) } })
