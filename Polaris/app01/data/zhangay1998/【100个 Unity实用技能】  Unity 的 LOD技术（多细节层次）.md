
--- 
title:  【100个 Unity实用技能】 | Unity 的 LOD技术（多细节层次） 
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
### <font color="#ff6984" size="5"> Unity </font>踩坑小知识点学习

### Unity中的 LOD技术（多细节层次）

`LOD(Level of detail) 多层次细节`，是最常⽤的游戏优化技术。 它按照模型的位置和重要程度决定 物体渲染的资源分配，降低⾮重要物体的⾯数和细节度，从⽽获得⾼效率的渲染运算。

这就是说，根据摄像机与模型的距离，来决定显示哪一个模型，一般距离近的时候显示高精度多细节模型，距离远的时候显示低精度低细节模型，来加快整体场景的渲染速度。
- **作用**：优化GPU- **缺点**：同一模型要准备多个模型，消耗内存- **特点**：以内存做消耗来优化GPU
##### 使用示例

在场景中对某一个游戏对象 准备三个不同精度的模型

<img src="https://img-blog.csdnimg.cn/b7cb72684aff41498b74bd7f75302af4.png" alt="在这里插入图片描述"> 创建一个空物体，并把3个精度的模型放下边，给空对象添加上 **LOD组件** <img src="https://img-blog.csdnimg.cn/7c9f3af0656b44069c523c3418fe52ac.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5ZGG5ZGG5pWy5Luj56CB55qE5bCPWQ==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 然后点击 **LOD组件** 的各个精度添加上不同精度的模型 <img src="https://img-blog.csdnimg.cn/59666a7f260d49c998a9cdf98230bfd2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5ZGG5ZGG5pWy5Luj56CB55qE5bCPWQ==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

然后此时移动 场景摄像机 或者 组件的摄像机 就可以看到效果了，如下所示： <img src="https://img-blog.csdnimg.cn/dcdeab5701964b50a3f4ca28537fa251.gif" alt="请添加图片描述"> 它会根据游戏对象与摄像机之间的距离来切换不同精度的模型，达到一个高效率的渲染效果。

就像我们 大逃杀游戏 里面的效果一样，在飞机上的时候看地面都是光秃秃的，等到了地上之后才能看到房子和花花草草之类的图形。

##### LOD组件参数

LOD组件 有一个参数 **Fade Mode（淡化模式）**

<img src="https://img-blog.csdnimg.cn/e4837e51954746de9bf039b51e727ba3.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/eab9c05aaee34c15b1d111317ace5cee.png" alt="在这里插入图片描述"> 有三种模式可以选择，`None` 、`Cross Fade` 和 `Speed Tree`

**None** 就是一个默认模式，不作处理。

其中**Cross Fade**为交叉淡入淡出，在这个选下还有一个可变属性叫Fade Transition Width（淡入淡出过渡宽度）

**Fade Transition Width** 是一个从0~1之间的值，代表淡入淡出的过渡区域占当前LOD级别的比例。如果值较小的话，可以延迟两个LOD级别混合的开始并且过渡更快，因为Unity通常使用的是屏幕空间抖动或透明度来实现交叉渐变。 <img src="https://img-blog.csdnimg.cn/cbe85f53cb5b430fab5851c75f14f9b8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5ZGG5ZGG5pWy5Luj56CB55qE5bCPWQ==,size_12,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

**Speed Tree** 只需要物体提供0~1的状态，然后两个LOD级别的混合是从0开始到1结束的，也就是开始时是与前一级别的LOD一致，转换结束时就与后一个LOD级别完全匹配了。

**Speed Tree** 模式仅用于在两个Mesh LOD级别之间进行混合，即当前和下一个LOD级别都具有Mesh Renderer（网格渲染器）时。当转换到Billboard LOD级别或完全淡出时，Unity会执行Cross Fade风格的混合。 <img src="https://img-blog.csdnimg.cn/b9e95a92c81342bda939761723fa2962.png" alt="在这里插入图片描述">

##### Project Settings中与LOD组件相关参数

菜单栏：`Edit &gt; Project Settings &gt; Quality`，打开Quality Setting窗口

找到Other下的参数，如图所示： <img src="https://img-blog.csdnimg.cn/175737b17c4e425287de52a691651308.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/04a6163c9e434415a23a1fc8a6959703.png" alt="在这里插入图片描述">

`Maximum LOD Level`：是最大LOD级别，表示游戏中使用的最高LOD级别。在该级别以上的模型不会被使用，并且在编译时忽略。（这将节省存储空间和内存空间）。

`LOD Bias `：LOD偏离 ，LOD级别基于物体在屏幕上的大小。当物体大小在两个LOD级别之间，可以选择使用低细节模型或高细节模型。数值取值范围为0-1，数值越接近0，越偏向于选择低细节模型。

#### 👑评论区抽奖送书

最后在评论区进行抽取三名幸运的小伙伴送下面这本书籍

在这里搞个小活动抽奖送给大家，对看书感兴趣的小伙伴可以参加一波呀，抽中概率很大哦！

**《Unity和C# 游戏编程入门（第5版）》**

##### 🎁规则如下：
<td bgcolor="76eec6"> 🚀 规则如下🚀 </td>
-  给本篇博客文章 `点赞` `收藏` `评论` 三连，然后就可以在博客文章评论区抽奖送一本Unity入门的书籍！ -  总共`抽三本`，中的几率还是很大的哦～ 想看书的小伙伴参与起来！ -  `中奖信息`文章发布时间的三天后下午本篇文章评论区公布！记得留意呀！ -  没抽到的，但是喜欢这本书的小伙伴也可以在网上自行购买哈，官方正品商店购买即可！ <td bgcolor="76eec6"> 🚀 规则如上🚀 </td>

#### 🎄推荐理由(⭐⭐⭐⭐⭐)
- **《Unity和C#游戏编程入门（第5版）》** 为从零开始学习C#编程提供了一条清晰的路径，绕过了复杂的术语和难以理解的编程逻辑，通过在Unity中创建一个简单的游戏来实现知识的掌握。- 第5版中，对C#功能的介绍针对新版的Unity游戏引擎进行了更新，同时增加了介绍中级集合类型的章节。读者将从软件编程与C#语言的基础开始，学习C#编程中的核心概念，包括变量、类和面向对象编程。- 在具备了C#编程的基本能力后，读者将进入Unity游戏开发的世界，并发掘如何通过C#脚本来实现简单的游戏机制。 <img src="https://img-blog.csdnimg.cn/ca7c27bef188430083b8077289fd7d83.jpeg" alt="在这里插入图片描述">
没抽到的小伙伴也可以官方平台自行购买哦： 京东移动端地址：https://item.m.jd.com/product/13706878.html

如果实在喜欢但是没抽到你的话，可以在评论区说一下，后续可以再给大家继续送福利！

<img src="https://img-blog.csdnimg.cn/20210613033645219.gif#pic_center" alt="在这里插入图片描述">
