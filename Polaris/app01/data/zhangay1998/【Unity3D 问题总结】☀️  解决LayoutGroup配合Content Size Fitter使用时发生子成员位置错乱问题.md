
--- 
title:  【Unity3D 问题总结】☀️ | 解决LayoutGroup配合Content Size Fitter使用时发生子成员位置错乱问题 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/4ea0ad75b9c145e5ba7d219b7e425099.png" alt="请添加图片描述">

>  
 -  🎬 博客主页： -  🎥 本文由 **呆呆敲代码的小Y** 原创，首发于 **CSDN**🙉 -  🎄 学习专栏推荐： -  🌲 游戏制作专栏推荐： -  🌲Unity实战100例专栏推荐： -  🏅 欢迎点赞 👍 收藏 ⭐留言 📝 如有错误敬请指正！ -  📆 未来很长，值得我们全力奔赴更美好的生活✨ -  ------------------❤️分割线❤️-------------------------  


<img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述">

<img src="https://img-blog.csdnimg.cn/01e7ec91f0984ce4a166bf72cb52bea5.gif" alt="请添加图片描述">

### <font color="#ff6984" size="5"> Unity </font>小科普

老规矩，先介绍一下<font color="#ff6984" size="4"> **Unity** </font>的科普小知识：<img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述">
- <font color="#ff6984" size="4">**Unity**</font>是 实时3D互动内容创作和运营平台 。- 包括<font color="#green" size="4">游戏开发</font>、<font color="#green" size="4">美术</font>、<font color="#green" size="4">建筑</font>、<font color="#green" size="4">汽车设计</font>、<font color="#green" size="4">影视</font>在内的所有创作者，借助<font color="#ff6984" size="4"> **Unity** </font>将创意变成现实。- <font color="#ff6e84" size="4">**Unity**</font> 平台提供一整套完善的软件解决方案，可用于创作、运营和变现任何实时互动的2D和3D内容，支持平台包括<font color="#green" size="4">手机</font>、<font color="#green" size="4">平板电脑</font>、<font color="#green" size="4">PC</font>、<font color="#green" size="4">游戏主机</font>、<font color="#green" size="4">增强现实</font>和<font color="#green" size="4">虚拟现实设备。 </font>- 也可以简单把 <font color="#ff6e84" size="4">**Unity**</font> 理解为一个<font color="#ee82ee" size="4">游戏引擎</font>，可以用来专业制作<font color="#ee0000" size="4">游戏</font>！
### <font color="#ff6984" size="5"> 【Unity3D 问题总结】 </font>

#### 【Unity3D 问题总结】☀️ | 解决LayoutGroup配合Content Size Fitter使用时发生子成员位置错乱问题

**问题描述：** 通过LayoutGroup组件配合 Content Size Fitter实现子成员自适应大小的功能，当子类动态生成或者内容发生变化时，父类未及时扩张或缩小导致内容发生视觉错误。

或者配合DoTween等组件使用时，内容也会出现错乱现象导致。

<img src="https://img-blog.csdnimg.cn/da3cedc98e8a4867ba7f65c13e0cd3ce.gif" alt="请添加图片描述"> 这里是父对象使用了LayoutGroup和Content Size Fitter，子对象使用了Content Size Fitter。 <img src="https://img-blog.csdnimg.cn/dbdd603b69714dd2b2fc654ba83c9489.png" alt="在这里插入图片描述">

这种问题的触发在于布局组件已经在某一帧内对布局元素进行渲染完毕了，但此时我们又通过代码或者其他方式对其进行了修改，导致内容发生了视觉上的错乱现象。

可以看到上述图片中通过重新激活组件或游戏对象则可以通过重新渲染得到正确的内容显示，但这只是一种解决方案，下面介绍更多解决方法。

##### 方法一：通过开关GameObject 的方法等一帧重新触发布局效果

这也是上图中的演示方法，通过关闭再打开GameObject的方法可以达到让布局元素重新进行布局的效果。 <img src="https://img-blog.csdnimg.cn/da3cedc98e8a4867ba7f65c13e0cd3ce.gif" alt="请添加图片描述">

##### 方法二： 使用代码进行强制刷新布局。

```
//rectTransform 为控制布局元素的父物体。
LayoutRebuilder.ForceRebuildLayoutImmediate(rectTransform);

```

此方法可以在我们对子成员的内容修改后调用，调用该方法可以让布局元素重新布局，不会出现内容错乱的现象，一般来说使用该方法就可以解决大部分该问题。

同样可以使用的代码还有以下几种：

```
horizLayoutGroup.CalculateLayoutInputHorizontal();
horizLayoutGroup.CalculateLayoutInputVertical();
horizLayoutGroup.SetLayoutHorizontal();
horizLayoutGroup.SetLayoutVertical();

```

#### 方法三：更换布局组件使用方法

布局组件勾选Control Child Size，并添加Content Size Fitter组件勾选水平或垂直，子对象就无需操作了。 此时在子对象上增删内容都可以达成自适应效果，完美解决问题。 <img src="https://img-blog.csdnimg.cn/0e5f14bc23a04000b48c19b9c50fbaf6.png" alt="在这里插入图片描述">

<font color="#ff6984" size="5"> **资料白嫖，技术互助**</font>

|学习路线指引（点击解锁）|知识定位|人群定位
|------
||入门级|本专栏从Unity入门开始学习，快速达到Unity的入门水平
||进阶级|计划制作Unity的 100个实战案例！助你进入Unity世界，争取做最全的Unity原创博客大全。
||难度偏高|分享学习一些Unity成品的游戏Demo和其他语言的小游戏！
||互助/吹水|数万人游戏爱好者社区，聊天互助，白嫖奖品
||Unity查漏补缺|针对一些Unity中经常用到的一些小知识和技能进行学习介绍，核心目的就是让我们能够快速学习Unity的知识以达到查漏补缺

<img src="https://img-blog.csdnimg.cn/20210613033645219.gif#pic_center" alt="在这里插入图片描述">
