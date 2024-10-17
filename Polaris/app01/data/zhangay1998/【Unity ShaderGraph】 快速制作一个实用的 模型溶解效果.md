
--- 
title:  【Unity ShaderGraph】| 快速制作一个实用的 模型溶解效果 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/4ea0ad75b9c145e5ba7d219b7e425099.png" alt="请添加图片描述">



####  
- <ul><li><ul><li>- - - - - 


<img src="https://img-blog.csdnimg.cn/31af18c5dd2a43a7a90ef2bb0661393f.gif#pic_center" alt="请添加图片描述">

#### 前言
- 本文将使用ShaderGraph制作一个模型溶解的效果，可以直接拿到项目中使用。- 对ShaderGraph还不了解的小伙伴可以参考这篇文章：- 下面就开始看一下具体的制作流程，然后自己动手制作一个吧！
## 【Unity ShaderGraph】| 快速制作一个实用的 模型溶解效果

### 一、效果展示

<img src="https://img-blog.csdnimg.cn/aa3504574a114928b311089a564fe37c.gif" alt="请添加图片描述">

<font color="#ff6984" size="5"> 资源下载方式： </font>

### 二、简易溶解效果

首先在Project下右键 `Creat - &gt; Shader Graph -&gt; URP -&gt; Lit Shader Graph`创建一个`Lit Shader Graph`。 <img src="https://img-blog.csdnimg.cn/d791bd4a048c491cb668bac388b3a12f.png" alt="在这里插入图片描述">

然后双击打开该ShaderGraph，在`ShaderGraph 面板`中的`Graph Inspector面板`上打开`Alpha Clipping`选项，这样在主节点中才会出现Alpha 和Alpha Clipping参数，将Alpha 改为0.5。

然后在ShaderGraph 面板中添加`Step`、`Noise`两个节点。

然后对两个节点进行连接，如下所示： <img src="https://img-blog.csdnimg.cn/75cb90c2ea8546a0a75d830e8848e79b.png" alt="在这里插入图片描述">

此时通过控制Step的Edge值就可以实现溶解效果了，效果如下所示： <img src="https://img-blog.csdnimg.cn/b3e05b3650b247fb9d3ec7bfbcd5e2d3.gif" alt="请添加图片描述">

调整 Noise 的Scale值可以调整溶解效果的密度。

### 三、进阶溶解效果

通过上面的步骤可以非常简单的实现模型的溶解效果，下面开始在溶解的基础上添加溶解边缘光。

ShaderGraph面板如下所示： <img src="https://img-blog.csdnimg.cn/a004682474f140e5a5c92366a9c615e2.png" alt="在这里插入图片描述">

关键点在于对Noise噪声做两个Step，再添加一个Color节点相乘，最后连到Emission发光节点上。

这样就可以实现在溶解时的溶解边缘发光效果了，通过控制Noise节点的Scale可以调整溶解效果的密度，调整Add节点的B值可以调整溶解发光的强度，调整Color节点可以控制发光的颜色。也可以将Time节点换成外部Float节点，这样就可以手动控制溶解效果。 <img src="https://img-blog.csdnimg.cn/30e224f3023b4ccfb547a7086cf040bb.gif" alt="请添加图片描述">

### 四、应用实例

创建完上述ShaderGraph之后在Project下创建一个材质球Material，然后将该ShaderGraph拖到该材质球上即可应用。

快捷方法是在Project下鼠标选中该ShaderGraph，然后右键Creat创建一个Material，这样我们创建出来的材质球，就自动使用这个Shader了。

然后将材质球拖到对象上就可以使用了。 <img src="https://img-blog.csdnimg.cn/aa3504574a114928b311089a564fe37c.gif" alt="请添加图片描述">

### 五、资源下载方式

>  
 -  🎬 博客主页： -  🎥 本文由 **呆呆敲代码的小Y** 原创 🙉 -  🎄 学习专栏推荐： -  🌲 游戏制作专栏推荐： -  🌲Unity实战100例专栏推荐： -  🏅 欢迎点赞 👍 收藏 ⭐留言 📝 如有错误敬请指正！ -  📆 未来很长，值得我们全力奔赴更美好的生活✨ -  ------------------❤️分割线❤️-------------------------  


<img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述">

<img src="https://img-blog.csdnimg.cn/01e7ec91f0984ce4a166bf72cb52bea5.gif" alt="请添加图片描述">

<font color="#ff6984" size="5"> **资料白嫖，技术互助**</font>

|学习路线指引（点击解锁）|知识定位|人群定位
|------
||入门级|本专栏从Unity入门开始学习，快速达到Unity的入门水平
||进阶级|计划制作Unity的 100个实战案例！助你进入Unity世界，争取做最全的Unity原创博客大全。
||难度偏高|分享学习一些Unity成品的游戏Demo和其他语言的小游戏！
||互助/吹水|数万人游戏爱好者社区，聊天互助，白嫖奖品
||Unity查漏补缺|针对一些Unity中经常用到的一些小知识和技能进行学习介绍，核心目的就是让我们能够快速学习Unity的知识以达到查漏补缺

<img src="https://img-blog.csdnimg.cn/20210613033645219.gif#pic_center" alt="在这里插入图片描述">
