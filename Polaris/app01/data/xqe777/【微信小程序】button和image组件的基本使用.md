
--- 
title:  【微信小程序】button和image组件的基本使用 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主🏆 📃个人主页： 🔥系列专栏：🥇 💬个人格言：不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待💖💖💖 


<img src="https://img-blog.csdnimg.cn/75860e007264416dbfd5fc8c6f545ed3.gif#pic_center" alt="在这里插入图片描述">



#### button和image
- - - - - 


## 其他常用组件

①<mark>button</mark>

>  
 按钮组件 功能比HTML中的button按钮丰富 


②<mark>image</mark>

>  
 图片组件 image组件默认宽度约300px、高度约240px 


③<mark>navigator</mark>

>  
 页面导航组件 类似于HTML中的a链接 


## button按钮的基本使用

✅通过type属性指定按钮颜色类型

```
&lt;button&gt;普通按钮&lt;/button&gt;
&lt;button type="primary"&gt;主色调按钮&lt;/button&gt;
&lt;button type="warn"&gt;警告按钮&lt;/button&gt;

```

<img src="https://img-blog.csdnimg.cn/3534f0fdde77447b82cc52db18d4c8b7.png" alt="在这里插入图片描述">

✅size=“mini” 小尺寸按钮

```
&lt;button size="mini"&gt;普通按钮&lt;/button&gt;
&lt;button type="primary" size="mini"&gt;主色调按钮&lt;/button&gt;
&lt;button type="warn" size="mini"&gt;警告按钮&lt;/button&gt;

```

<img src="https://img-blog.csdnimg.cn/c6026500b21c4a2798b0cf3d9a74e7ac.png" alt="在这里插入图片描述">

✅plain 镂空按钮

```
&lt;button size="mini" plain&gt;普通按钮&lt;/button&gt;
&lt;button type="primary" size="mini" plain&gt;主色调按钮&lt;/button&gt;
&lt;button type="warn" size="mini" plain&gt;警告按钮 &lt;/button&gt;

```

<img src="https://img-blog.csdnimg.cn/965b6dc20bf2457b82aa912ebfff9039.png" alt="在这里插入图片描述">

## image组件的基本使用

✅使用src 指向图片路径

```
&lt;image src="/images/秦霄贤.png"&gt;&lt;/image&gt;

```

<img src="https://img-blog.csdnimg.cn/815d4463f8a143dd8d963bce4ed8fcfb.png" alt="在这里插入图片描述">

## image组件的mode属性

image组件的<font color="red" size="4">mode</font>属性用来指定图片的裁剪和缩放模式，常用的<font color="red" size="4">mode</font>属性值如下：

|mode值|说明
|------
|scaleToFill|(默认值)缩放模式，不保持纵横比缩放图片，使图片的宽高完全拉伸至<font color="red" size="2">填满image元素</font>
|aspectFit|缩放模式，<font color="red" size="2">保持纵横比缩放图片，使图片长边能完全显示出来</font>，也就是说，可以完整地将图片显示出来
|aspectFill|缩放模式，<font color="red" size="2">保持纵横比缩放图片，只保证图片的短边能完全显示出来</font>，也就是说，图片通常只在水平或垂直方向是完整的，另一个方向将会发生截取
|widthFix|<font color="red" size="2">缩放模式，宽度不变，高度自动变化</font>，保持原图宽高比不变
|heightFix|<font color="red" size="2">缩放模式，高度不变，宽度自动变化</font>，保持原图宽高比不变

✅使用实例：

```
&lt;image src="/images/秦霄贤.png" mode="aspectFit"&gt;&lt;/image&gt;

```

<img src="https://img-blog.csdnimg.cn/e7a71799f1af4aa1889d4d9bed37edec.png" alt="在这里插入图片描述">

```
&lt;image src="/images/秦霄贤.png" mode="aspectFill"&gt;&lt;/image&gt;

```

<img src="https://img-blog.csdnimg.cn/d3d89eb3a1df4ceea7c2a40a4505d5c5.png" alt="在这里插入图片描述">

```
&lt;image src="/images/秦霄贤.png" mode="widthFix"&gt;&lt;/image&gt;

```

<img src="https://img-blog.csdnimg.cn/09cbd41a689d42448e5c2b9e5a92b54a.png" alt="在这里插入图片描述">

```
&lt;image src="/images/秦霄贤.png" mode="heightFix"&gt;&lt;/image&gt;

```

<img src="https://img-blog.csdnimg.cn/cae2146b45054fe1b99e472b440b7ec4.png" alt="在这里插入图片描述">

## 结束语🥇

以上就是微信小程序之button和image组件的基本使用 持续更新微信小程序教程，欢迎大家订阅系列专栏 你们的支持就是hacker创作的动力💖💖💖

<img src="https://img-blog.csdnimg.cn/5b80ea7dab574ae5bb3fda934fe3f872.gif#pic_center" alt="在这里插入图片描述">
