
--- 
title:  【微信小程序】text和rich-text组件的基本使用 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主🏆 📃个人主页：🥇 🔥系列专栏： 💬个人格言：不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待💖💖💖 


<img src="https://img-blog.csdnimg.cn/75860e007264416dbfd5fc8c6f545ed3.gif#pic_center" alt="在这里插入图片描述"> 

#### 常用的基础内容组件
- - - 


## text

文本组件 类似于HTML中的span标签，是一个行内元素

通过text组件中的selectable属性，实现长按选中文本内容的效果： ✅demo.wxml

```
&lt;view&gt;
    长按复制手机号
    &lt;text selectable&gt;15733271167&lt;/text&gt;
&lt;/view&gt;

```

实现效果如下(选择二维码预览查看效果)

<img src="https://img-blog.csdnimg.cn/302e2110a9464040b5f61bc5dc9f5e65.gif#pic_center" alt="在这里插入图片描述">

## rich-text

富文本组件 支持把HTML字符串渲染为WXML结构

通过rich-text组件的nodes属性节点，把HTML字符串渲染为对应的UI结构

```
&lt;rich-text nodes="&lt;h4 style='color: lightpink;'&gt;不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待💖💖💖&lt;/h4&gt;"&gt;&lt;/rich-text&gt;

```

✅实现效果如下：

<img src="https://img-blog.csdnimg.cn/71838fe2893a424e9c99b6387838854b.png" alt="">

## 结束语🥇

以上就是微信小程序之text和rich-text组件的基本使用 持续更新微信小程序教程，欢迎大家订阅系列专栏 你们的支持就是hacker创作的动力💖💖💖 <img src="https://img-blog.csdnimg.cn/5b80ea7dab574ae5bb3fda934fe3f872.gif#pic_center" alt="在这里插入图片描述">
