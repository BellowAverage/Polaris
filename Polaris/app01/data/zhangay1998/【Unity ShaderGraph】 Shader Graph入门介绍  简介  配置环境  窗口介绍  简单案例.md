
--- 
title:  【Unity ShaderGraph】| Shader Graph入门介绍 | 简介 | 配置环境 | 窗口介绍 | 简单案例 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/4ea0ad75b9c145e5ba7d219b7e425099.png" alt="请添加图片描述">



####  
- <ul><li><ul><li>- - <ul><li>- - - - - - 


<img src="https://img-blog.csdnimg.cn/31af18c5dd2a43a7a90ef2bb0661393f.gif#center" alt="请添加图片描述">

#### 前言
- Unity2018版本之后推出了一款名为 `Shader Graph` 的可编程渲染管线工具。- 这个工具可以通过可视化界面拖拽来实现着色器的创建和编辑，大大简化了着色器的制作过程，同时着色效果编译显示也快。- 下面就来介绍一下Shader Graph的基本信息及使用方法，上手非常简单，一起来看看吧！
## 【Unity ShaderGraph】| Shader Graph入门介绍 | 简介 | 配置环境 | 窗口介绍 | 简单案例

### 一、Shader Graph

#### 1.1 渲染管线 简介

在开始学习Shader Graph之前，要先了解一下什么是 `渲染管线（Render Pipline）`。

`渲染管线` 也被称为渲染流水线或像素流水线，是显示芯片内部处理图形信号的相互独立的并行处理单元。这可以比作工厂中的生产流水线，以提高产品的生产能力和效率。在某种程度上，渲染管线对于显卡的工作能力和效率至关重要。

目前Unity中的渲染管线主要有以下几种：
1.  **内置渲染管线（Build-In Render）**：这是Unity最早的渲染管线，也是默认的渲染管线，提供了一套简单的渲染流程，但相对来说功能较为基础，对于一些高级的图形效果可能无法实现。 1.  **SRP 可编程渲染管线技术（Scriptable Render Pipline）** ：可以在Unity通过C#脚本调用API配置或执行渲染命令的方式来实现渲染流程，SRP将这些命令传递给Unity底层图形体系结构（low-level graphics architecture），然后再将指令发送给图形API（Graphics API），最终由GPU进行处理，SRP 技术可以强化通用渲染管线 (URP) 和高清渲染管线 (HDRP)。URP和HDRP建立在SRP之上，还可以在 SRP 之上创建自己的自定义渲染管线。 1.  **URP 通用渲染管线（Universal Render Pipeline）**：从Unity 2019.3版本开始，Unity引入了通用渲染管线URP，它是一种快速的单通道前向渲染器，主要设计用于不支持计算着色器技术的低端设备，例如较早的智能手机、平板电脑和XR设备。但是，URP还可为中端设备（如游戏主机和PC）提供更高质量的图形性能。 1.  **HDRP 高清渲染管线（High Definition Render Pipeline）**：这是Unity的高质量渲染管线，主要针对高端设备，例如最新的智能手机、游戏主机和PC等。它提供了更高的视觉效果和更真实的图像表现，同时也需要更高的计算能力。 
以上就是目前Unity中主要的渲染管线，每种都有其特定的运用场景和优缺点，选择哪种渲染管线需要根据具体项目需求和目标平台性能来进行选择。

以Universal Render Pipeline（URP）为例，Unity中的渲染管线的主要步骤如下：
1. **顶点着色器**：这个阶段主要处理顶点相关的操作，比如顶点位置，颜色，纹理坐标等相关的变换。1. **光栅化**：这个阶段将顶点数据转换成片元（像素）数据，这个过程也涉及到裁剪和剔除等操作，比如将视野外的模型裁剪掉，剔除背面等操作。1. **片元着色器**：这个阶段会针对每个片元（像素）进行操作，主要处理光照和材质等效果。1. **输出合并**：这个阶段会进行一些操作比如深度测试、模板测试、颜色混合等，最后将渲染结果输出到屏幕上。
这些步骤是渲染管线的核心流程，其中每个步骤都可以根据需要进行细分和扩展。

渲染管线这里就简单介绍一下，对渲染管线感兴趣的小伙伴可以去查阅这方面的详细文档介绍，学习ShaderGraph只需简单了解即可。

#### 1.2 Shader Graph 简介

`Shader Graph` 是Unity中的一个可视化着色器编辑工具，它允许开发者通过连接节点来创建和编辑自定义的着色器效果。使用ShaderGraph，开发者可以以图形化方式创建复杂的渲染效果，而无需编写复杂的着色器代码。

ShaderGraph提供了一个直观的界面，其中包含各种节点，开发者可以将它们连接起来以构建想要的效果。这些节点代表了着色器中的各个部分，例如顶点处理、片段处理、表面函数等。通过连接节点，可以定义材质的输入和输出，并在节点之间传递数据。

ShaderGraph支持多个渲染管线，包括Unity的内置管线和Universal Render Pipeline（URP）。在创建ShaderGraph时，开发者可以选择所需的目标管线，并且ShaderGraph会相应地生成相应的着色器代码。

使用ShaderGraph，开发者可以轻松地实现各种常见的着色器效果，例如颜色混合、纹理映射、法线映射和光照计算等。此外，ShaderGraph还支持自定义节点，开发者可以编写自己的节点来实现特定的效果。

除了可视化编辑功能外，ShaderGraph还具有实时预览功能，开发者可以在编辑器中即时查看和调整效果。这使得迭代开发变得更加便捷和高效，开发者可以快速调整参数并立即看到结果。

另一个强大的功能是ShaderGraph的可移植性。开发者可以将创建的ShaderGraph保存为可重用的自定义着色器，然后在不同的项目中重用它们。这简化了着色器的管理和共享，同时也提高了代码复用性和开发效率。

官方称ShaderGraph具有如下的特点：
1. 直观构建着色器。用户无需编写代码，而是在图形框架中创建和连接节点。1. 提供反映更改的即时反馈。这对于不熟悉着色器创建的用户来说是非常友好的。1. **Shader Graph仅与可编写脚本的渲染管线(SRP)兼容**。这个渲染管线包括高清晰度渲染管线(HDRP)和通用渲染管线(URP)，这两个SRP在Unity 2018.1及更高版本中都可用。然而，传统的内置渲染管线不支持Shader Graph。
此外，Shader Graph是基于可编程流水线，通过节点图的方式来实现可视化的Shader的编程，这种方式可以让用户不必再编写大量的代码以及考虑语法和错误调试等问题。

总而言之，ShaderGraph是Unity中一个强大而直观的工具，它使得创建自定义着色器效果变得更加容易和可视化。无论是新手还是经验丰富的开发者，都可以通过ShaderGraph快速实现各种复杂的渲染效果，并将其应用于自己的游戏或应用程序中。

### 二、Shader Graph相关链接
- Shader Graph官方文档：- Shader Graph官方文档：- Shader Graph官方示例： - Shader Graph学习专栏：
### 三、Shader Graph 注意事项

由于随着Unity版本及Shader Graph的不断更新，一些旧版本的功能和界面都已经发生变化。

包括之前一些关于ShaderGraph的优质文章，可能由于版本更迭的原因，导致现在跟着学习会出现内容与实际操作不匹配的情况。

经过我自己测试发现，使用 `Unity2020` 及以后的版本，差不多对应 `Shader Graph 10.0` 以后的版本，在使用过程中没有太大区别，只是功能有变化，所以不会影响学习参考。

为了方便大家学习，所以后续本系列内容使用的Unity版本为Unity2023.1+，使用的Shader Graph版本为15.0。

（使用Unity2023.1.9版本老是出现bug，这版Unity真拉胯呀，着实不推荐使用。。。）

### 四、Shader Graph 配置环境搭建

由于Shader Graph只能与可编写脚本的渲染管线(SRP)兼容，所以在项目中要使用 高清晰度渲染管线(HDRP)和通用渲染管线(URP)才可以，也就意味着使用的Unity版本要2018.1及更高版本才可以。

#### 4.1 Shader Graph导入

首先要在项目中导入 Shader Graph资源包，打开项目后选择菜单键`Windows -&gt; Package Manager -&gt; Shader Graph`，搜索Shader Graph并安装。 <img src="https://img-blog.csdnimg.cn/f2a3e164864146d0a163107b6b77a984.png" alt="在这里插入图片描述">

然后要导入URP或HDRP，下面以URP为例演示，在PackageManager中搜索RP，然后找到URP进行安装。 <img src="https://img-blog.csdnimg.cn/b6ed732442064ef3a9b0689e1cefc0dd.png" alt="在这里插入图片描述">

上述方法只能根据Unity版本的不同安装固定的资源包版本，若是想安装自己指定的版本，可以来到Unity项目目录下找到json文件，然后在文件中修改想要的版本即可。 <img src="https://img-blog.csdnimg.cn/afd5efb7159c490490c8191a9ac904c8.png" alt="在这里插入图片描述">

需要注意的是某些资源包的版本可能会与当前Unity版本不适配出现报错现象，所以若是没有特殊需求，还是建议直接使用Unity中固定的版本即可。

#### 4.2 ShaderGraph配置

通过菜单`Asset --&gt; Create --&gt; “Rendering --&gt; Universal Render Popeline --&gt; Pipeline Asset(Forward Renderer)` 或者Project面板右键也可以创建URP渲染管线配置文件。 <img src="https://img-blog.csdnimg.cn/4018ba79945d47389ce98d26d82e4ba2.png" alt="在这里插入图片描述">

然后选择菜单键`Editor -&gt; Project Setting -&gt; Graphics` ，将创建的URP渲染管线配置文件拖到Graphics面板中的`Scriptable Render Pipeline Settings`上去即可。 <img src="https://img-blog.csdnimg.cn/5d1a58d2d09942d9bb8d3d895aefe4ae.png" alt="在这里插入图片描述">

这样我们就完成了基本的配置，下面就可以正式使用ShaderGraph了。

### 五、Shader Graph 窗口介绍

#### 5.1 创建ShaderGraph示例

在Project面板右键 `Create → Shader Graph → URP`，选择 Lit Shader Graph 或 Unlit Shader Graph，创建 Shader Graph。 <img src="https://img-blog.csdnimg.cn/1041e2a4d7034686aa070710cfec4177.png" alt="在这里插入图片描述"> 需要注意的是根据Unity版本的不同，此处创建ShaderGraph时可能路径会有所不同，只要找到带有ShaderGraph后缀的即可使用。

Lit Shader Graph和Unlit Shader Graph的主要区别在于是否包含光照模型。
- **Lit Shader Graph带有光照模型**，它基于物理的光照模型（PBR），使用法类似于表面着色器。这意味着在Lit Shader Graph中，你可以实现光照的反射、投射和散射等效果，创建出更逼真、更具视觉冲击力的图形。- **Unlit Shader Graph没有光照模型**，你需要自己编写光照计算流程。这意味着在Unlit Shader Graph中，无法直接实现光照的反射、投射和散射等效果，而是需要用其他手段模拟这些效果，或者实现其他类似的效果。不过，这也给了Unlit Shader Graph更大的灵活性，因为它不依赖于固定的光照模型，可以根据需要进行更定制化的处理。
创建完Shader Graph之后会出现一个shadergraph文件，双击打开该文件即可弹窗ShaderGraph的窗口面板。 <img src="https://img-blog.csdnimg.cn/8a2e55446c56462097124eef2a60df65.png" alt="在这里插入图片描述">

#### 5.2 Shader Graph 窗口组成

Shader Graph 由 `Blackboard`、`Graph Inspector`、`Main Preview`、`Vertex`、`Fragment`、`Node` 等模块组成。 <img src="https://img-blog.csdnimg.cn/247f202d7c924c15b5b72124af6afecc.png" alt="在这里插入图片描述">
- **Blackboard**：用于创建外部属性，相当于 Shader 中的 Properties，可以创建 Float、Vector2~4、Color、Boolean、Gradient、Texture2D、Texture2D Array、Texture3D、Cubemap、Matrix2~4 等类型变量。- **Graph Inspector**：包含节点设置和图设置两个选项卡，节点设置中可以设置节点命名、参数值域、默认值等信息；图设置中可以设置着色器数值计算精度、支持的渲染管线（Built-in 或 Universal）、管线参数等。- **Main Preview**：用于预览着色器渲染效果，在该窗口右键，可以选择预览的模型。- **Vertex**：顶点着色器，顶点变换、法线变换、切线变换在这里进行。- **Fragment**：片元着色器，光照计算、贴图在这里进行，在 Graph Inspector 窗口的 Graph Settings 选项卡里的 Material 中可以选择 Lit（PBR 光照模型）或 Unlit（无光照模型）的片元着色器。- **Node**：节点，在 Shader Graph 窗口的空白区域右键，选择 Create Node，创建相应节点，节点类型主要有 Artistic（对比度、饱和度、白平衡等美术调整）、Channel（合并和分离通道等）、Input（顶点位置、颜色、法线、时间等输入）、Math（加减乘除等数学运算）、Procedural（噪声、圆形、多边形等程序纹理）、Utility（逻辑判断、自定义函数等实用工具）、UV（球形扭曲、旋转贴图等 uv 变换）。
可以在官网文档查阅关于更多节点的作用：

#### 5.3 Shader Graph 窗口使用技巧

Shader Graph 窗口中的Blackboard、Graph Inspector、Main Preview模块可以通过右上角的按钮控制显示和隐藏，点击左上角的 Save Asset 按钮可以保存Shader Graph文件。 <img src="https://img-blog.csdnimg.cn/021d374400b9441cb81a30bd72f4fb87.gif" alt="请添加图片描述">

滑动鼠标滑轮可以放大和缩小节点，按鼠标中键或者Alt+鼠标左键拖拽可以平移场景，在Shader Graph 窗口中鼠标移动到模块的右下角可以调整预览框的大小。 <img src="https://img-blog.csdnimg.cn/808c01c36add40f8bcb87ea46fcd65bf.gif" alt="请添加图片描述">

当节点较多时，可以对其分类整理使得视图更加整洁清晰，还可以对整组进行保存复用。

鼠标按下框选要放在一组中的节点，然后右键选择Group Selection，自定义命名即可创建组。选中组之后，点击右键选择Delete即可删除组。 <img src="https://img-blog.csdnimg.cn/cf6d940f4abe4f04b12501dae0833147.gif" alt="请添加图片描述">

### 六、Shader Graph 简单案例

在Project面板右键 `Create -&gt; Shader Graph -&gt; URP -&gt; Unit Shader Graph `创建一个Shader Graph文件，然后双击打开。

在Shader Graph窗口空白处 `右键 -&gt; Create Node -&gt; 搜索Texture` 创建一个 Sample Texture 2D。

然后将Sample Texture 2D连接到BaceColor节点，可以通过Texture 节点选择图片，然后点击左上角的Save Asset保存文件。 <img src="https://img-blog.csdnimg.cn/d544aaa95a5943f5aeff61c2941a24b1.png" alt="在这里插入图片描述">

然后回到Project面板创建一个Material材质，并将该ShaderGraph拖到材质球上。

然后在场景中添加一个对象，将该材质拖到对象上就可以使用了。 <img src="https://img-blog.csdnimg.cn/866f1cb4da874dfea1f8c0e4ac346e19.png" alt="在这里插入图片描述">

此时会发现，在外部材质球上是无法修改贴图的，还需要在ShaderGraph中添加一个外部属性才可以。

点击+号，添加一个Texture 2D，然后将该Texture 2D拖到中间的空白处，与SampleTexture2D 节点连接起来，然后点击保存。 <img src="https://img-blog.csdnimg.cn/1fada1d824ae432ba7691f690997a400.png" alt="在这里插入图片描述">

此时就可以在外部通过修改材质球上的Texture来修改贴图了。 <img src="https://img-blog.csdnimg.cn/03f6ff845b014fc9af304a2bb09a2f09.png" alt="在这里插入图片描述">

使用ShaderGraph的关键其实就是明白ShaderGraph中各个节点的作用，通过协调好各个节点来完成各式各样的效果。

这比起写Shader代码来说，无疑是简单了太多，但相应的也需要熟悉大量的API文档才可以真正的上手熟练使用ShaderGraph。

<font color="#ff6984" size="5"> Shader Graph 相关资源下载方式： </font>

## 总结
- 在本文中，我们深入探讨了Unity中的`Shader Graph`功能，详细介绍了其作用、应用、优势以及实际价值。ShaderGraph的优点在于其直观的图形化界面和强大的可编程性，使得用户可以轻松地创建和编辑着色器，而无需编写大量的代码。 然而，ShaderGraph也存在一些不足之处，例如其与传统的渲染管线不兼容，以及需要一定的学习成本才能熟练掌握。- ShaderGraph适用于各种游戏开发场景，特别是对于那些需要实现复杂图形效果的场景。通过使用ShaderGraph，开发者可以提高游戏画面质量，增加游戏可玩性，同时还能缩短开发周期和提高工作效率。- 在未来的发展趋势中，我们可以预见到ShaderGraph将会越来越普及，成为游戏开发中的重要工具。随着技术的不断进步，ShaderGraph也将会得到更多的功能和优化，进一步提高游戏图形的效果和质量。- 总的来说，Unity中的ShaderGraph是一个强大的图形化编程工具，它为用户提供了直观、高效的着色器创建和编辑方式。在游戏开发中，ShaderGraph的价值已经得到了广泛的认可，而未来它也将会发挥更大的作用。
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
