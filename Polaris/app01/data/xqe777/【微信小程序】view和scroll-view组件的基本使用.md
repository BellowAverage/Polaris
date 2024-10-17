
--- 
title:  【微信小程序】view和scroll-view组件的基本使用 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主🏆 📃个人主页： 🔥系列专栏： 💬个人格言：但行好事，莫问前程 


<img src="https://img-blog.csdnimg.cn/75860e007264416dbfd5fc8c6f545ed3.gif#pic_center" alt="在这里插入图片描述">



#### view和scroll-view
- - - - - 


## 小程序组件的分类

小程序中的组件也是由宿主环境提供的，开发者可以使用组件快速搭建出页面结构，官方把小程序里的组件分为了9大类，分别是 ①视图容器 ②基础内容 ③表单组件 ④导航组件 ⑤媒体组件 ⑥map地图组件 ⑦canvas画布组件 ⑧开放能力 ⑨无障碍访问

## 常见的视图容器类组件

①view 普通视图区域 类似于HTML中的div，是一个块级元素 常用于实现页面的布局效果 ②scroll-view 可滚动的视图区域 常用于实现滚动列表效果 ③swiper和swiper-item 轮播图容器组件和轮播图item组件

## view组件的基本使用

🔥在hacker页面实现如图所示的flex横向布局效果：

<img src="https://img-blog.csdnimg.cn/6a4f973c7fd3405abe050edeaf4c2c2e.png" alt="在这里插入图片描述">

✅hacker.wxml

```
&lt;!--pages/hacker/hacker.wxml--&gt;
&lt;view class="container1"&gt;
    &lt;view&gt;A&lt;/view&gt;
    &lt;view&gt;B&lt;/view&gt;
    &lt;view&gt;C&lt;/view&gt;
&lt;/view&gt;

```

✅hacker.wxss

```
/* pages/hacker/hacker.wxss */
.container1 view{<!-- -->
    width: 100px;
    height: 100px;
    text-align:center;
    line-height: 100px;
}
.container1 view:nth-child(1){<!-- -->
    background-color:lightgreen;
}
.container1 view:nth-child(2){<!-- -->
    background-color: lightskyblue;
}
.container1 view:nth-child(3){<!-- -->
    background-color: lightpink;
}

.container1{<!-- -->
    display: flex;
    justify-content: space-around;
}

```

## scroll-view组件的基本使用

🔥在hacker页面实现如图所示的纵向滚动效果：

<img src="https://img-blog.csdnimg.cn/b4deab9d447b4e34a01fef462cecb200.gif#pic_center" alt="在这里插入图片描述">

✅hacker.wxml

```
&lt;!--pages/hacker/hacker.wxml--&gt;
&lt;!--scroll-y属性：允许纵向滚动--&gt;
&lt;!--scroll-x属性：允许横向滚动--&gt;
&lt;!--注意：使用竖向滚动时必须给scroll-view一个固定高度--&gt;
&lt;scroll-view class="container1"scroll-y&gt;
    &lt;view&gt;A&lt;/view&gt;
    &lt;view&gt;B&lt;/view&gt;
    &lt;view&gt;C&lt;/view&gt;
&lt;/scroll-view&gt;

```

✅hacker.wxss

```
/* pages/hacker/hacker.wxss */
.container1 view{<!-- -->
    width: 100px;
    height: 100px;
    text-align:center;
    line-height: 100px;
}
.container1 view:nth-child(1){<!-- -->
    background-color:lightgreen;
}
.container1 view:nth-child(2){<!-- -->
    background-color: lightskyblue;
}
.container1 view:nth-child(3){<!-- -->
    background-color: lightpink;
}

.container1{<!-- -->
    width: 100px;
    /* 给 scroll-view 固定高度 */
    height: 100px;
}


```

## 结束语

以上就是微信小程序之view和scroll-view组件的基本使用 持续更新微信小程序教程，欢迎大家订阅系列专栏 你们的支持就是hacker创作的动力💖💖💖

<img src="https://img-blog.csdnimg.cn/5b80ea7dab574ae5bb3fda934fe3f872.gif#pic_center" alt="在这里插入图片描述">
