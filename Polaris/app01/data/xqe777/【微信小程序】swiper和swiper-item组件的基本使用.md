
--- 
title:  【微信小程序】swiper和swiper-item组件的基本使用 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主🏆 📃个人主页： 🔥系列专栏： 💬个人格言：不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待💖💖💖 


<img src="https://img-blog.csdnimg.cn/75860e007264416dbfd5fc8c6f545ed3.gif#pic_center" alt="在这里插入图片描述">



#### swiper和swiper-item
- - - 


## 实现轮播图效果

<img src="https://img-blog.csdnimg.cn/cab897b487ea442893b5ae5b36703b44.gif#pic_center" alt="在这里插入图片描述">

<mark>list.wxml</mark>

```
&lt;!--轮播图的结构--&gt;
&lt;swiper class="swiper-container"&gt;
    &lt;!--第一个轮播图--&gt;
    &lt;swiper-item&gt;
    &lt;view class="item"&gt;A&lt;/view&gt;
    &lt;/swiper-item&gt;
    &lt;!--第二个轮播图--&gt;
    &lt;swiper-item&gt;
        &lt;view class="item"&gt;B&lt;/view&gt;
    &lt;/swiper-item&gt;
    &lt;!--第三个轮播图--&gt;
    &lt;swiper-item&gt;
        &lt;view class="item"&gt;C&lt;/view&gt;
    &lt;/swiper-item&gt;
&lt;/swiper&gt;


```

<mark>list.wxss</mark>

```
/* 轮播图样式 */
.swiper-container{<!-- -->
    height: 150px;
}

.item{<!-- -->
    height: 100%;
    line-height: 150px;
    text-align: center;
}

swiper-item:nth-child(1) .item{<!-- -->
    background-color: lightgreen;
}
swiper-item:nth-child(2) .item{<!-- -->
    background-color: lightskyblue;
}
swiper-item:nth-child(3) .item{<!-- -->
    background-color: lightpink;
}

```

## swiper组件的常用属性

|属性|类型|默认值|说明
|------
|indicator-dots|boolean|false|是否显示面板提示点
|indictor-color|color|rgba(0,0,0,3)|指示点颜色
|indictor-active-color|color|#000000|当前选择的指示点颜色
|autoplay|boolean|false|是否自动切换
|interval|number|5000|自动切换时间间隔
|circular|boolean|false|是否采用衔接滑动

✅显示指示点颜色

<img src="https://img-blog.csdnimg.cn/7bd853ccc2b84791a8fb47407839a97f.png" alt="在这里插入图片描述">

✅设置指示点颜色

<img src="https://img-blog.csdnimg.cn/6b113e4e829b4b78b710b4cfe4f47943.png" alt="在这里插入图片描述"> ✅设置当前选择的指示点颜色

<img src="https://img-blog.csdnimg.cn/c56c9149112b4e3dbd6f0be81fafcea5.png" alt="在这里插入图片描述"> ✅设置1秒自动切换

<img src="https://img-blog.csdnimg.cn/01b45c6f073549619f5e1431d54be77f.gif#pic_center" alt="在这里插入图片描述">

✅设置衔接滑动

<img src="https://img-blog.csdnimg.cn/cf14e884f5584a9185d213f39156e11e.gif#pic_center" alt="在这里插入图片描述">

## 结束语

以上就是微信小程序之swiper和swiper-item组件的基本使用 持续更新微信小程序教程，欢迎大家订阅系列专栏 你们的支持就是hacker创作的动力💖💖💖

<img src="https://img-blog.csdnimg.cn/5b80ea7dab574ae5bb3fda934fe3f872.gif#pic_center" alt="在这里插入图片描述">
