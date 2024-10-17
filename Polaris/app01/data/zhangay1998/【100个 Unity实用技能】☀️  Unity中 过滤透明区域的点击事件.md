
--- 
title:  【100个 Unity实用技能】☀️ | Unity中 过滤透明区域的点击事件 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/4ea0ad75b9c145e5ba7d219b7e425099.png" alt="请添加图片描述">

### <font color="#ff6984" size="5"> Unity </font>小知识 大智慧

>  
 -  🎬 博客主页： -  🎥 本文由 **呆呆敲代码的小Y** 原创，首发于 **CSDN**🙉 -  🎄 学习专栏推荐： -  🌲 游戏制作专栏推荐： -  🌲Unity实战100例专栏推荐： -  🏅 欢迎点赞 👍 收藏 ⭐留言 📝 如有错误敬请指正！ -  📆 未来很长，值得我们全力奔赴更美好的生活✨ -  ------------------❤️分割线❤️-------------------------  


<img src="https://img-blog.csdnimg.cn/01e7ec91f0984ce4a166bf72cb52bea5.gif" alt="请添加图片描述">

### <font color="#ff6984" size="5"> Unity </font>实用技能学习

#### Unity中 过滤透明区域的点击事件

在Unity中我们有时候会遇到一些带有透明度的图片按钮，有些时候可能并不希望点击按钮的透明区域时也触发点击事件，这个时候就要进行额外处理，下面整理了几种方法可以进行参考使用！

<img src="https://img-blog.csdnimg.cn/direct/d5d933c3c9cb4f86bf239546954517e4.png" alt="在这里插入图片描述">

##### 像素检测 过滤透明区域

这种方法是通过读取Sprite在某一点的像素值(RGBA)，如果该点的像素值中的Alpha小于一定的阈值（比如0.5）则表示该点是透明的，即用户点击的位置在精灵边界以外，否则用户点击的位置在精灵边界内部。

这种做法就是通过判断点击的某一点是否达到我们期望的像素Alpha阈值，达到阈值就响应事件，未达到阈值就说明点击了透明区域，此时不响应事件。

UGUI在处理控件是否被点击的时候，主要是根据IsRaycastLocationValid这个方法的返回值来进行判断的，而这个方法用到的基本原理则是判断指定点对应像素的RGBA数值中的Alpha是否大于某个指定临界值。

**一、使用Image组件自带的参数检测**

而UGUI中可以通过Image组件拿到一个`alphaHitTestMinimumThreshold` ，这个值代表的含义就是期望的像素Alpha阈值，通过改变这个值就可以实现过滤透明区域的点击事件。

```
this.GetComponent&lt;Image&gt;().alphaHitTestMinimumThreshold = 0.1f;

```

所以使用方法很简单，拿到指定按钮上的Image组件，改变这个Image的alphaHitTestMinimumThreshold即可实现过滤透明区域的所有点击事件，下面看下实际使用方法及效果。

通过控制`alpahThreshold`的值可以实现透明过滤的强度，也就是透明度过滤的阈值。比如alpahThreshold 为0则代表只过滤全透明的区域，alpahThreshold 为0.5则是把半透明一下的过滤掉，alpahThreshold 为1的话那就整张图都被过滤了，都不会响应事件。

准备两个带有透明度的切图，然后放置到场景的Button组件上，测试代码如下：

```
using UnityEngine;
using UnityEngine.UI;

public class UnityImageAlphaTest : MonoBehaviour
{<!-- -->
    public Button btnImage1;
    public Button btnImage2;

    [Header("透明度过滤阈值")]
    public float alpahThreshold = 0.5f;

    void Start()
    {<!-- -->
        btnImage1.onClick.AddListener(OnClickImage);
        btnImage2.onClick.AddListener(OnClickImage);

        btnImage2.GetComponent&lt;Image&gt;().alphaHitTestMinimumThreshold = alpahThreshold;
    }

    private void OnClickImage()
    {<!-- -->
        Debug.Log("点击图片测试！");
    }
}

```

值得注意的是还需要把过滤透明区域的图片设置为可读写状态（Read/Write Enable 设置为true），如下图所示，否则这种方法不会生效且会报错。 <img src="https://img-blog.csdnimg.cn/direct/c7256f2ea8884ea4b77684a0758a538a.png" alt="在这里插入图片描述">

将两个Button挂载到脚本中，第一个Button不参与透明过滤，第二个Button过滤透明区域点击事件。 <img src="https://img-blog.csdnimg.cn/direct/8a8b8322adb04378a779e3b468b2533c.png" alt="在这里插入图片描述">

此时运行Unity就可以看到效果了，效果如下： <img src="https://img-blog.csdnimg.cn/direct/144751609d584ecb84f90aaf43a7f574.gif" alt="请添加图片描述">

**2.根据点击的坐标计算该点的像素值是否满足阈值**

与上述直接使用Image组件的方法有所区别，这种方法是通过计算我们点击的坐标点的像素值是否达到阈值来判断需要过滤。

但原理是相同的，都是通过像素检测去判断是否选择过滤，下面看下实现代码：

```
using UnityEngine;
using UnityEngine.UI;
public class Model_ButtonSetting : MonoBehaviour, ICanvasRaycastFilter
{<!-- -->
    [Header("透明度过滤阈值")]
    public float alpahThreshold = 0.1f;

    protected Image _image;
    void Start()
    {<!-- -->
        _image = GetComponent&lt;Image&gt;();
    }

    public bool IsRaycastLocationValid(Vector2 sp, Camera eventCamera)
    {<!-- -->
        //将选中的点转换为Image区域内的本地点
        Vector2 localPoint;
        RectTransformUtility.ScreenPointToLocalPointInRectangle(_image.rectTransform, sp, eventCamera, out localPoint);

        Vector2 pivot = _image.rectTransform.pivot;
        Vector2 normalizedLocal = new Vector2(pivot.x + localPoint.x / _image.rectTransform.rect.width, pivot.y + localPoint.y / _image.rectTransform.rect.height);
        Vector2 uv = new Vector2(
            _image.sprite.rect.x + normalizedLocal.x * _image.sprite.rect.width,
            _image.sprite.rect.y + normalizedLocal.y * _image.sprite.rect.height);

        uv.x /= _image.sprite.texture.width;
        uv.y /= _image.sprite.texture.height;


        //获取指定纹理坐标（u, v）处的像素颜色。它返回一个Color结构，其中包含红、绿、蓝和alpha通道的值。
        //Color c = _image.sprite.texture.GetPixel((int)uv.x, (int)uv.y);
        //用于在纹理上执行双线性插值以获取像素颜色值,这个方法使用双线性插值算法来估算纹理中某个位置的颜色,而不是直接从纹理的像素中读取颜色。
        Color c = _image.sprite.texture.GetPixelBilinear(uv.x, uv.y);

        return c.a &gt; alpahThreshold;
    }
}

```

这种方法也需要把过滤透明区域的图片设置为可读写状态（Read/Write Enable 设置为true），否则这种方法也不会生效且会报错。

将上述脚本挂载到需要屏蔽透明区域的按钮上即可生效，简单易用。

<font color="#ff6984" size="5"> **资料白嫖，技术互助**</font>

<th align="left">学习路线指引（点击解锁）</th>|知识定位|人群定位
|------
<td align="left"></td>|入门级|本专栏从Unity入门开始学习，快速达到Unity的入门水平
<td align="left"></td>|进阶级|计划制作Unity的 100个实战案例！助你进入Unity世界，争取做最全的Unity原创博客大全。
<td align="left"></td>|难度偏高|分享学习一些Unity成品的游戏Demo和其他语言的小游戏！
<td align="left"></td>|互助/吹水|数万人游戏爱好者社区，聊天互助，白嫖奖品
<td align="left"></td>|Unity查漏补缺|针对一些Unity中经常用到的一些小知识和技能进行学习介绍，核心目的就是让我们能够快速学习Unity的知识以达到查漏补缺

<img src="https://img-blog.csdnimg.cn/20210613033645219.gif#pic_center" alt="在这里插入图片描述">
