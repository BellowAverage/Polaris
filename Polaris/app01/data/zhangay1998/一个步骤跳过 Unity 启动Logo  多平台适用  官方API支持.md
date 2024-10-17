
--- 
title:  一个步骤跳过 Unity 启动Logo | 多平台适用 | 官方API支持 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/4ea0ad75b9c145e5ba7d219b7e425099.png" alt="请添加图片描述">



####  
- <ul><li><ul><li>- - - <ul><li>- 


<img src="https://img-blog.csdnimg.cn/16f302592dc840c58a16a9e1259e0e29.png" alt="在这里插入图片描述">

#### 前言
- 众所周知，使用Unity引擎打包的工程在启动时都带有Unity的默认启动Logo。- 这个问题可以通过购买Unity专业版以及零元购解决，但是对于多数人来说一般不会使用这种方法。- 之前已经写过一篇文章使用aar的方式从安卓端去掉Unity的启动Logo：- 那本篇文章就来使用一种更简单的方法来直接去掉启动Logo，只需要一个脚本即可完成。
## <font color="#ff6984" size="5"> 【Unity实战篇 】</font> | 一个步骤跳过 Unity Logo 界面 | 多平台适用 | 官方API支持

<img src="https://img-blog.csdnimg.cn/f810f10aae304ec1ac7dbc722f9bd567.gif" alt="请添加图片描述">

### 使用方法

在Unity工程中创建一个脚本`SkipSplash.cs`，然后将该脚本放到除了`Editor`以外的文件夹就可以了，不需要挂载。

脚本代码如下：

```
#if !UNITY_EDITOR
using UnityEngine;
using UnityEngine.Rendering;

public class SkipSplash
{<!-- -->
    [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.BeforeSplashScreen)]
    private static void BeforeSplashScreen()
    {<!-- -->
#if UNITY_WEBGL
        Application.focusChanged += Application_focusChanged;
#else
        System.Threading.Tasks.Task.Run(AsyncSkip);
#endif
    }

#if UNITY_WEBGL
    private static void Application_focusChanged(bool obj)
    {<!-- -->
        Application.focusChanged -= Application_focusChanged;
        SplashScreen.Stop(SplashScreen.StopBehavior.StopImmediate);
    }
#else
    private static void AsyncSkip()
    {<!-- -->
        SplashScreen.Stop(SplashScreen.StopBehavior.StopImmediate);
    }
#endif
}
#endif

```

### 核心 API

该脚本主要用到了两个API： `RuntimeInitializeOnLoadMethodAttribute` 与`SplashScreen` 。
- - 
#### 1. RuntimeInitializeOnLoadMethodAttribute

<img src="https://img-blog.csdnimg.cn/b86e9152060f4cdc9998cd6bb60ce248.png" alt="在这里插入图片描述">

`RuntimeInitializeOnLoadMethodAttribute`一般会配合`RuntimeInitializeLoadType`进行使用。

 有以下类型：

<th align="left">类型</th><th align="left">介绍</th>
|------
<td align="left">AfterSceneLoad</td><td align="left">在场景加载后</td>
<td align="left">BeforeSceneLoad</td><td align="left">在场景加载前</td>
<td align="left">AfterAssembliesLoaded</td><td align="left">加载完所有程序集并初始化预加载资源时的回调</td>
<td align="left">BeforeSplashScreen</td><td align="left">在显示启动画面之前</td>
<td align="left">SubsystemRegistration</td><td align="left">用于子系统注册的回调</td>

在之前写过的一篇小知识文章中用到过这个RuntimeInitializeOnLoadMethodAttribute： 

`RuntimeInitializeOnLoadMethodAttribute` 主要负责的是在显示启动画面之前调用这个静态方法，也就是执行跳过Logo方法的时间。

#### 2. SplashScreen

<img src="https://img-blog.csdnimg.cn/972c1a0a680a4325a2647982f7df1f14.png" alt="在这里插入图片描述">

`SplashScreen` 是负责跳过Logo的核心方法，与上面的RuntimeInitializeOnLoadMethodAttribute进行配合，在在显示启动画面之前停止 SplashScreen 渲染即可完成Unity启动Logo的去除！

```
SplashScreen.Stop(SplashScreen.StopBehavior.StopImmediate)

```

### 效果展示

<img src="https://img-blog.csdnimg.cn/f810f10aae304ec1ac7dbc722f9bd567.gif" alt="请添加图片描述">

<img src="https://img-blog.csdnimg.cn/a4a26c8f05ab45209bdf68adc64472c7.gif" alt="请添加图片描述">

可以看到非常简单的就实现了去掉Unity的启动Logo，只需要一个脚本放到工程中就好了，限制是需要 Unity2019.4 或更高版本。

实测了Unity2021、2020及2019.4版本发现都可以正常使用。

**优点：** 该方法非常简单方便，一个脚本可以实现多平台去掉启动Logo。

**缺点：** 当工程比较大时，此方法去除Logo的效果可能会很差，可能会出现Logo一闪而过或者卡出几帧Logo的画面。 还可能会出现长达4、5秒的黑屏时间，这是因为应用程序正在加载，即使我们停止了Logo，但是并不能影响这个加载的流程时间。 这个时候跳过启动Logo的意义就不大了，正确的方法应该是在此空挡时间换成自己的启动画面，这样就需要另外写方法进行操作了。

## 总结
- 本文讲了一下怎样方便快速跳过 Unity 启动Logo的方法，非常的简单实用。- 如果想去除启动Logo画面的同时并替换成自己的启动动画则可以参考下面的文章- - 
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
