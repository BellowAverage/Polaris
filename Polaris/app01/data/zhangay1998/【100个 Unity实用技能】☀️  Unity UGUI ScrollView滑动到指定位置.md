
--- 
title:  【100个 Unity实用技能】☀️ | Unity UGUI ScrollView滑动到指定位置 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/4ea0ad75b9c145e5ba7d219b7e425099.png" alt="请添加图片描述">

### <font color="#ff6984" size="5"> Unity </font>小科普

老规矩，先介绍一下<font color="#ff6984" size="4"> **Unity** </font>的科普小知识：
- <font color="#ff6984" size="4">**Unity**</font>是 实时3D互动内容创作和运营平台 。- 包括<font color="#green" size="4">游戏开发</font>、<font color="#green" size="4">美术</font>、<font color="#green" size="4">建筑</font>、<font color="#green" size="4">汽车设计</font>、<font color="#green" size="4">影视</font>在内的所有创作者，借助<font color="#ff6984" size="4"> **Unity** </font>将创意变成现实。- <font color="#ff6e84" size="4">**Unity**</font> 平台提供一整套完善的软件解决方案，可用于创作、运营和变现任何实时互动的2D和3D内容，支持平台包括<font color="#green" size="4">手机</font>、<font color="#green" size="4">平板电脑</font>、<font color="#green" size="4">PC</font>、<font color="#green" size="4">游戏主机</font>、<font color="#green" size="4">增强现实</font>和<font color="#green" size="4">虚拟现实设备。 </font>- 也可以简单把 <font color="#ff6e84" size="4">**Unity**</font> 理解为一个<font color="#ee82ee" size="4">游戏引擎</font>，可以用来专业制作<font color="#ee0000" size="4">游戏</font>！
### <font color="#ff6984" size="5"> Unity </font>实用小技能学习

#### Unity UGUI ScrollView滑动到指定位置

Unity 中在使用ScrollView的时候，有需求是需要将ScrollView定位到指定的Item上。

如领取一个奖励列表时，每次打开ScrollView让其滑动到最后一个可领取的Item中。

##### 方法一：计算比例完成滑动

这里只要计算好item的比例并利用ScrollView的API即可轻松完成该功能，主要用到`verticalNormalizedPosition `与`horizontalNormalizedPosition `两个参数。 代码如下：

```
using UnityEngine;
using UnityEngine.UI;
public class ScrollViewTest : MonoBehaviour
{<!-- -->
    private ScrollRect scrollRect;
 
    private void Start()
    {<!-- -->
        scrollRect= GetComponent&lt;ScrollRect&gt;();
    }
    
    /// &lt;summary&gt;
    /// 设置Rect位置
    /// &lt;/summary&gt;
    /// &lt;param name="value"&gt;取值范围0-1 ，0代表滑动到最底部或者最左边，1代表滑动到最顶部或者最右边&lt;/param&gt;
    /// &lt;param name="isvertical"&gt;是否设置Vertical竖向滑动&lt;/param&gt;
    public void SetRectPos(float value, bool isvertical)
    {<!-- -->
        if (isvertical)
            scrollRect.verticalNormalizedPosition = value;
        else
            scrollRect.horizontalNormalizedPosition = value;
    }
}

```

我们需要拿到这个Item在ScrollView中的索引位置，将其与当前所有的Item进行计算，得到一个大小在 `0 ~ 1` 的float值，将其传入方法即可完成滑动。

##### 方法二：计算位置进行滑动

使用计算的方式，计算出指定的item的坐标，然后进行赋值即可。

```
using UnityEngine;
using DG.Tweening;
using UnityEngine.UI;
 
public class ScrollViewNevigation : MonoSingleton&lt;ScrollViewNevigation&gt;
{<!-- -->
 
    private ScrollRect scrollRect;
    private RectTransform viewport;
    private RectTransform content;
 
	// Use this for initialization
	void Start ()
	{<!-- -->
 
	    Init();
	    //Nevigate(content.GetChild(45).GetComponent&lt;RectTransform&gt;());
	}

    private void Init()
    {<!-- -->
        if (scrollRect == null)
        {<!-- -->
            scrollRect = this.GetComponent&lt;ScrollRect&gt;();
        }
        if (viewport == null)
        {<!-- -->
            viewport = this.transform.Find("Viewport").GetComponent&lt;RectTransform&gt;();
        }
 
        if (content == null)
        {<!-- -->
            content = this.transform.Find("Viewport/Content").GetComponent&lt;RectTransform&gt;();
        }
    }
 
    public void Nevigate(RectTransform item)
    {<!-- -->
 
        Vector3 itemCurrentLocalPostion = scrollRect.GetComponent&lt;RectTransform&gt;().InverseTransformVector(ConvertLocalPosToWorldPos(item));
        Vector3 itemTargetLocalPos = scrollRect.GetComponent&lt;RectTransform&gt;().InverseTransformVector(ConvertLocalPosToWorldPos(viewport));
 
        Vector3 diff = itemTargetLocalPos - itemCurrentLocalPostion;
        diff.z = 0.0f;
 
        var newNormalizedPosition = new Vector2(
            diff.x / (content.GetComponent&lt;RectTransform&gt;().rect.width - viewport.rect.width),
            diff.y / (content.GetComponent&lt;RectTransform&gt;().rect.height - viewport.rect.height)
            );
 
        newNormalizedPosition = scrollRect.GetComponent&lt;ScrollRect&gt;().normalizedPosition - newNormalizedPosition;
 
        newNormalizedPosition.x = Mathf.Clamp01(newNormalizedPosition.x);
        newNormalizedPosition.y = Mathf.Clamp01(newNormalizedPosition.y);
 
 		//有DOTween时使用
        DOTween.To(() =&gt; scrollRect.GetComponent&lt;ScrollRect&gt;().normalizedPosition, x =&gt; scrollRect.GetComponent&lt;ScrollRect&gt;().normalizedPosition = x, newNormalizedPosition, 0.8f);
        //无DOTween时使用
        scrollRect.GetComponent&lt;ScrollRect&gt;().normalizedPosition = newNormalizedPosition;
    }
 
    private Vector3 ConvertLocalPosToWorldPos(RectTransform target)
    {<!-- -->
        var pivotOffset = new Vector3(
            (0.5f - target.pivot.x) * target.rect.size.x,
            (0.5f - target.pivot.y) * target.rect.size.y,
            0f);
 
        var localPosition = target.localPosition + pivotOffset;
 
        return target.parent.TransformPoint(localPosition);
    }
}

```

调用其中方法Nevigate()传入指定的Item即可。

>  
 -  🎬 博客主页： -  🎥 本文由 **呆呆敲代码的小Y** 原创，首发于 **CSDN**🙉 -  🎄 学习专栏推荐： -  🌲 游戏制作专栏推荐： -  🌲Unity实战100例专栏推荐： -  🏅 欢迎点赞 👍 收藏 ⭐留言 📝 如有错误敬请指正！ -  📆 未来很长，值得我们全力奔赴更美好的生活✨ -  ------------------❤️分割线❤️-------------------------  


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
