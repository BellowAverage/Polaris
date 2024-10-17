
--- 
title:  【100个 Unity实用技能】☀️ | UGUI中 判断屏幕中某个坐标点的位置是否在指定UI区域内 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/4ea0ad75b9c145e5ba7d219b7e425099.png" alt="请添加图片描述">

### <font color="#ff6984" size="5"> Unity </font>小知识 大智慧

>  
 -  🎬 博客主页： -  🎥 本文由 **呆呆敲代码的小Y** 原创，首发于 **CSDN**🙉 -  🎄 学习专栏推荐： -  🌲 游戏制作专栏推荐： -  🌲Unity实战100例专栏推荐： -  🏅 欢迎点赞 👍 收藏 ⭐留言 📝 如有错误敬请指正！ -  📆 未来很长，值得我们全力奔赴更美好的生活✨ -  ------------------❤️分割线❤️-------------------------  


### <font color="#ff6984" size="5"> Unity </font>实用技能学习

#### 【100个 Unity实用技能】☀️ | UGUI中 判断屏幕的某个点的位置是否在指定UI区域内

**问题使用场景**：需要判断玩家此时点击的某个点是否在某个指定的UI区域内，如果在区域内则响应点击事件，不在区域内时不进行响应事件。

##### 第一种方法：使用 rect.Contains() 判断是否在矩形内

使用Unity中的`RectTransformUtility.ScreenPointToLocalPointInRectangle()`可以将屏幕坐标转化为相对RectTransform的本地坐标。

然后再使用RectTransform的`Contains()`方法就可以判断某个坐标点是否在该RectTransform区域内部了。

下面看示例演示，代码如下：

```
using System;
using UnityEngine;
using UnityEngine.UI;

public class UIClickAreaTest : MonoBehaviour
{<!-- -->
    //判断的UI区域
    public RectTransform rectTrans;
    //用于坐标点是否在区域内的标记
    public Image imgFlag;

    private void Update()
    {<!-- -->
        //按下鼠标左键时进行检测
        if (Input.GetMouseButton(0))
        {<!-- -->
            GetClickArea(Input.mousePosition);
        }
    }

    ///传入某个坐标点进行判断
    public void GetClickArea(Vector2 point)
    {<!-- -->
        Vector2 localPoint;
        //将屏幕坐标转化为相对rectTrans的本地坐标
        if (RectTransformUtility.ScreenPointToLocalPointInRectangle(rectTrans, point, Camera.main, out localPoint))
        {<!-- -->
            //rectTrans.rect是rectTrans的本地坐标，不能rectTrans.rect.Contains(point)直接判断，必须先转为本地坐标localPoint
            //判断点击的坐标点是否在rectTrans.rect矩形内
            if (rectTrans.rect.Contains(localPoint))
            {<!-- -->
                imgFlag.color = Color.green;
            }
            else
            {<!-- -->
                imgFlag.color = Color.red;
            }
        }
    }
}

```

需要注意的是使用这种方法时，若Canvas 的 RenderMode 在`Screen Space - Camera`或`World Space`模式下，传入的camera为UI摄像机，然后把目标UI区域拖入自己的脚本中即可。

如果Canvas的模式为在`Screen Space - OverLay`模式下，camara参数应该传入null。 <img src="https://img-blog.csdnimg.cn/direct/a1f0c688310449439f376533b3b59d0b.png" alt="在这里插入图片描述">

测试效果如下：鼠标按下时若在目前区域内则标记的图片变为绿色，鼠标不在区域内则为红色。 <img src="https://img-blog.csdnimg.cn/direct/810f9c148a36459992a22ea484ae294a.gif" alt="请添加图片描述">

##### 第二种方法：使用RectTransformUtility.RectangleContainsScreenPoint判断点是否在区域内

使用Unity中的`RectTransformUtility.RectangleContainsScreenPoint()`可以直接返回某个点是否在指定的RectTransform区域内。

与第一种方法类似，需要根据Canvas的渲染模式进行不同的相机参数处理即可。

```
using System;
using UnityEngine;
using UnityEngine.UI;

public class UIClickAreaTest : MonoBehaviour
{<!-- -->
    //判断的UI区域
    public RectTransform rectTrans;
    //用于坐标点是否在区域内的标记
    public Image imgFlag;

    private void Update()
    {<!-- -->
        //按下鼠标左键时进行检测
        if (Input.GetMouseButton(0))
        {<!-- -->
            GetClickArea(Input.mousePosition);
        }
    }

    //第二种方法：使用 RectangleContainsScreenPoint判断是否在矩形内
    public void GetClickArea(Vector2 point)
    {<!-- -->
        //判断点击的坐标点是否在rectTrans.rect矩形内，第三个参数根据Canvas的渲染模式选择是否传入相机
        if (RectTransformUtility.RectangleContainsScreenPoint(rectTrans, point, null))
        {<!-- -->
            imgFlag.color = Color.green;
        }
        else
        {<!-- -->
            imgFlag.color = Color.red;
        }
    }
}

```

##### 第三种方法：使用坐标计算是否在区域内

除了使用上面的方法中使用API来判断之外，还可以计算坐标去进行对比，查看对应的坐标点是否在UI区域内。

下面看示例演示，代码如下：

```
    //判断的UI区域
    public RectTransform rectTrans;
    //用于坐标点是否在区域内的标记
    public Image imgFlag;

    private void Update()
    {<!-- -->
        //按下鼠标左键时进行检测
        if (Input.GetMouseButton(0))
        {<!-- -->
            IsTouchInUi(Input.mousePosition);
        }
    }
    
    public void IsTouchInUi(Vector3 pos)
    {<!-- -->
        float _mapWidth = rectTrans.sizeDelta.x;
        float _mapHight = rectTrans.sizeDelta.y;
        //目标区域锚点为居中时使用 Pivot(0.5,0.5)
        if (pos.x &lt; (rectTrans.position.x + _mapWidth / 2) &amp;&amp; pos.x &gt; (rectTrans.position.x - _mapWidth / 2) &amp;&amp;
            pos.y &lt; (rectTrans.position.y + _mapHight / 2) &amp;&amp; pos.y &gt; (rectTrans.position.y - _mapHight / 2))
        {<!-- -->
            imgFlag.color = Color.green;
        }
        else
        {<!-- -->
            imgFlag.color = Color.red;
        }
    }

```

这种方法不需要改变Canvas的渲染模式，使用默认的Screen Space-Overlay 屏幕空间覆盖模式即可。

但要注意的是目标区域Image组件的 中心点 Pivot 需要设置为居中，否则的话就要根据不同 中心点Pivot 的设置去修改代码中的坐标判断。 <img src="https://img-blog.csdnimg.cn/direct/5ee327b37c1c42ec9fc57c422bd4baf3.png" alt="在这里插入图片描述">

测试效果如下： <img src="https://img-blog.csdnimg.cn/direct/259175dc57294d1a97ceb421540298ea.gif" alt="请添加图片描述">

##### 第四种方法：使用RectTransformUtility配合坐标计算，无需考虑中心点及锚点

第二种方法需要根据Image组件的中心点进行不同的逻辑判断处理，也有办法可以不考虑中心点。

通过 `RectTransformUtility.ScreenPointToLocalPointInRectangle() `将坐标点转换为目标区域的本地坐标，与第一种方法中的处理方式相同。

然后通过计算坐标点在目标区域中心点的 标准化向量 即可得出 改坐标点是否在目标区域内。

不过要注意的是此种方法还是需要跟第一种和第二种方法类似，需要根据Canvas的渲染模式进行相机参数的传入处理。

```
    /// &lt;summary&gt;
    /// 第三种方法：使用RectTransformUtility配合坐标计算，无需考虑锚点
    /// &lt;/summary&gt;
    /// &lt;param name="pos"&gt;&lt;/param&gt;
    public void GetClickAreaUI(Vector3 pos)
    {<!-- -->
        Vector2 localPoint;
        //将选中的点转换为Image区域内的本地点
        RectTransformUtility.ScreenPointToLocalPointInRectangle(rectTrans, pos, Camera.main, out localPoint);

        Vector2 pivot = rectTrans.pivot;
        Vector2 normalizedLocal = new Vector2(pivot.x + localPoint.x / rectTrans.sizeDelta.x, pivot.y + localPoint.y / rectTrans.sizeDelta.y);
        if ((normalizedLocal.x &gt;= 0 &amp;&amp; normalizedLocal.x &lt;= 1) &amp;&amp; ((normalizedLocal.y &gt;= 0 &amp;&amp; normalizedLocal.y &lt;= 1)))
        {<!-- -->
            imgFlag.color = Color.green;
        }
        else
        {<!-- -->
            imgFlag.color = Color.red;
        }
    }

```

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
