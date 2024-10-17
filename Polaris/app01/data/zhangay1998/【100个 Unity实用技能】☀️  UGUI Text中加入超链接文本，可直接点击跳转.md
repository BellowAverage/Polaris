
--- 
title:  【100个 Unity实用技能】☀️ | UGUI Text中加入超链接文本，可直接点击跳转 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/4ea0ad75b9c145e5ba7d219b7e425099.png" alt="请添加图片描述">

### <font color="#ff6984" size="5"> Unity </font>小科普

老规矩，先介绍一下<font color="#ff6984" size="4"> **Unity** </font>的科普小知识：<img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述">
- <font color="#ff6984" size="4">**Unity**</font>是 实时3D互动内容创作和运营平台 。- 包括<font color="#green" size="4">游戏开发</font>、<font color="#green" size="4">美术</font>、<font color="#green" size="4">建筑</font>、<font color="#green" size="4">汽车设计</font>、<font color="#green" size="4">影视</font>在内的所有创作者，借助<font color="#ff6984" size="4"> **Unity** </font>将创意变成现实。- <font color="#ff6e84" size="4">**Unity**</font> 平台提供一整套完善的软件解决方案，可用于创作、运营和变现任何实时互动的2D和3D内容，支持平台包括<font color="#green" size="4">手机</font>、<font color="#green" size="4">平板电脑</font>、<font color="#green" size="4">PC</font>、<font color="#green" size="4">游戏主机</font>、<font color="#green" size="4">增强现实</font>和<font color="#green" size="4">虚拟现实设备。 </font>- 也可以简单把 <font color="#ff6e84" size="4">**Unity**</font> 理解为一个<font color="#ee82ee" size="4">游戏引擎</font>，可以用来专业制作<font color="#ee0000" size="4">游戏</font>！
### <font color="#ff6984" size="5"> Unity </font>实用小技能学习

#### 【100个 Unity实用技能】☀️ | UGUI Text中加入超链接文本，可直接点击跳转

在项目中我们可能会有需求让文本显示中增加以一个可以进行点击的具有超链接的文本。

最常见的是在一段正常文本内容中，有中间几个字可以进行点击并执行某种事件，比如很多游戏的聊天大厅中会有玩家发出一段文字并带有装备的名称，此时点击装备就可以弹窗显示装备的信息，这个也算是在文本中加入超链接的一种。

下面就来看一下怎样使用Unity中的UGUI来实现这种效果，实现的方式应该有许多种，这里就演示两种给大家参考使用了！

##### 第一种方法：重写一个Text文本控件

需要新建一个脚本HyperlinkText .cs放到项目中，核心脚本代码如下：

```
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.Text.RegularExpressions;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.EventSystems;
using UnityEngine.UI;
 
/// &lt;summary&gt;
/// 文本控件,支持超链接
/// &lt;/summary&gt;
public class HyperlinkText : Text, IPointerClickHandler
{<!-- -->
    /// &lt;summary&gt;
    /// 超链接信息类
    /// &lt;/summary&gt;
    private class HyperlinkInfo
    {<!-- -->
        public int startIndex;
 
        public int endIndex;
 
        public string name;
 
        public readonly List&lt;Rect&gt; boxes = new List&lt;Rect&gt;();
    }
 
    /// &lt;summary&gt;
    /// 解析完最终的文本
    /// &lt;/summary&gt;
    private string m_OutputText;
 
    /// &lt;summary&gt;
    /// 超链接信息列表
    /// &lt;/summary&gt;
    private readonly List&lt;HyperlinkInfo&gt; m_HrefInfos = new List&lt;HyperlinkInfo&gt;();
 
    /// &lt;summary&gt;
    /// 文本构造器
    /// &lt;/summary&gt;
    protected static readonly StringBuilder s_TextBuilder = new StringBuilder();
 
    [Serializable]
    public class HrefClickEvent : UnityEvent&lt;string&gt; {<!-- --> }
 
    [SerializeField]
    private HrefClickEvent m_OnHrefClick = new HrefClickEvent();
 
    /// &lt;summary&gt;
    /// 超链接点击事件
    /// &lt;/summary&gt;
    public HrefClickEvent onHrefClick
    {<!-- -->
        get {<!-- --> return m_OnHrefClick; }
        set {<!-- --> m_OnHrefClick = value; }
    }
 
 
    /// &lt;summary&gt;
    /// 超链接正则
    /// &lt;/summary&gt;
    private static readonly Regex s_HrefRegex = new Regex(@"&lt;a href=([^&gt;\n\s]+)&gt;(.*?)(&lt;/a&gt;)", RegexOptions.Singleline);
 
    private HyperlinkText mHyperlinkText;
 
    protected override void Awake()
    {<!-- -->
        base.Awake();
        mHyperlinkText = GetComponent&lt;HyperlinkText&gt;();
    }
    protected override void OnEnable()
    {<!-- -->
        base.OnEnable();
        mHyperlinkText.onHrefClick.AddListener(OnHyperlinkTextInfo);
    }
 
    protected override void OnDisable()
    {<!-- -->
        base.OnDisable();
        mHyperlinkText.onHrefClick.RemoveListener(OnHyperlinkTextInfo);
    }
 
 
    public override void SetVerticesDirty()
    {<!-- -->
        base.SetVerticesDirty();
#if UNITY_EDITOR
        if (UnityEditor.PrefabUtility.GetPrefabType(this) == UnityEditor.PrefabType.Prefab)
        {<!-- -->
            return;
        }
#endif
        m_OutputText = GetOutputText(text);
 
    }
 
 
    protected override void OnPopulateMesh(VertexHelper toFill)
    {<!-- -->
        var orignText = m_Text;
        m_Text = m_OutputText;
        base.OnPopulateMesh(toFill);
        m_Text = orignText;
        UIVertex vert = new UIVertex();
 
        // 处理超链接包围框
        foreach (var hrefInfo in m_HrefInfos)
        {<!-- -->
            hrefInfo.boxes.Clear();
            if (hrefInfo.startIndex &gt;= toFill.currentVertCount)
            {<!-- -->
                continue;
            }
 
            // 将超链接里面的文本顶点索引坐标加入到包围框
            toFill.PopulateUIVertex(ref vert, hrefInfo.startIndex);
            var pos = vert.position;
            
            var bounds = new Bounds(pos, Vector3.zero);
            for (int i = hrefInfo.startIndex, m = hrefInfo.endIndex; i &lt; m; i++)
            {<!-- -->
                if (i &gt;= toFill.currentVertCount)
                {<!-- -->
                    break;
                }
 
                toFill.PopulateUIVertex(ref vert, i);
                pos = vert.position;
                if (pos.x &lt; bounds.min.x) // 换行重新添加包围框
                {<!-- -->
                    hrefInfo.boxes.Add(new Rect(bounds.min, bounds.size));
                    bounds = new Bounds(pos, Vector3.zero);
                }
                else
                {<!-- -->
                    bounds.Encapsulate(pos); // 扩展包围框
 
                }
            }
 
            hrefInfo.boxes.Add(new Rect(bounds.min, bounds.size));
        }
    }
 
    /// &lt;summary&gt;
    /// 获取超链接解析后的最后输出文本
    /// &lt;/summary&gt;
    /// &lt;returns&gt;&lt;/returns&gt;
    protected virtual string GetOutputText(string outputText)
    {<!-- -->
        s_TextBuilder.Length = 0;
        m_HrefInfos.Clear();
        var indexText = 0;
        foreach (Match match in s_HrefRegex.Matches(outputText))
        {<!-- -->
            s_TextBuilder.Append(outputText.Substring(indexText, match.Index - indexText));
 
            string str = s_TextBuilder.ToString();
            char[] array = str.ToCharArray();                //把字符串转化成字符数组
            IEnumerator enumerator = array.GetEnumerator();         //得到枚举器
            StringBuilder stringBuilder = new StringBuilder();
            while (enumerator.MoveNext())                         //开始枚举
            {<!-- -->
                if ((char)enumerator.Current != ' ')         //向StringBuilder类对象添加非空格字符
                    stringBuilder.Append(enumerator.Current.ToString());
            }
 
            var group = match.Groups[1];
            var hrefInfo = new HyperlinkInfo
            {<!-- -->
                startIndex = stringBuilder.Length * 4, // 超链接里的文本起始顶点索引
                endIndex = (stringBuilder.Length + match.Groups[2].Length - 1) * 4 + 3 ,
                name = group.Value
            };
 
            m_HrefInfos.Add(hrefInfo);
            s_TextBuilder.Append("&lt;color=blue&gt;");  // 超链接颜色
            s_TextBuilder.Append(match.Groups[2].Value);
            s_TextBuilder.Append("&lt;/color&gt;");
            indexText = match.Index + match.Length;
        }
        s_TextBuilder.Append(outputText.Substring(indexText, outputText.Length - indexText));
        return s_TextBuilder.ToString();
    }
 
    /// &lt;summary&gt;
    /// 点击事件检测是否点击到超链接文本
    /// &lt;/summary&gt;
    /// &lt;param name="eventData"&gt;&lt;/param&gt;
    public void OnPointerClick(PointerEventData eventData)
    {<!-- -->
        Vector2 lp = Vector2.zero;
        
        RectTransformUtility.ScreenPointToLocalPointInRectangle(rectTransform, eventData.position, eventData.pressEventCamera, out lp);
 
        foreach (var hrefInfo in m_HrefInfos)
        {<!-- -->
            var boxes = hrefInfo.boxes;
            for (var i = 0; i &lt; boxes.Count; ++i)
            {<!-- -->
                if (boxes[i].Contains(lp))
                {<!-- -->
                    m_OnHrefClick.Invoke(hrefInfo.name);
                    return;
                }
            }
        }
    }
    /// &lt;summary&gt;
    /// 当前点击超链接回调
    /// &lt;/summary&gt;
    /// &lt;param name="info"&gt;回调信息&lt;/param&gt;
    private void OnHyperlinkTextInfo(string info)
    {<!-- -->
        Debug.Log("超链接信息：" + info);
        Application.OpenURL(info);
    }
}

```

脚本完成后，在场景中新建一个Text组件（或者Create-&gt;Empty也可以），然后将原有的Text组件删掉，添加刚才新建的脚本组件HyperlinkText 。

此时在该组件中添加文字`文本测试：&lt;a href=https://xiaoy.blog.csdn.net/&gt;[小Y博客]&lt;/a&gt;`，场景中如下显示： <img src="https://img-blog.csdnimg.cn/2edac8f1cd4141e6ab354d92197fdf00.png" alt="在这里插入图片描述">

此时运行项目，对蓝色字体进行点击即可完成超链接跳转功能。

如不想跳转网页链接，而是执行项目中的某个事件（如打开某个窗口），可以在脚本中的`OnHyperlinkTextInfo()`方法中进行具体事件的逻辑添加。 <img src="https://img-blog.csdnimg.cn/48d5b2ec56b14ec78e4ac135d1ebd4e1.gif" alt="请添加图片描述">

##### 第二种方法：通过在Text组件中内嵌Button的方式完成点击功能

这个方法其实就是属于比较朴实无华的方案了，通过在Text组件再添加一个Button放到指定文字下面完成点击事件，这就属于基本的UGUI操作了，不属于超链接文本那一类。

不过从表现效果来看，功能是完全可以完成实现的，并且还可以通过富文本来定制各种颜色的文本显示效果。 <img src="https://img-blog.csdnimg.cn/3ba8d4cb5d404e148e9f7ac1ca61224c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/82e6aafdb00c40f8a3c69dd06a6a5eb4.png" alt="在这里插入图片描述">

对于一些需要静态显示的文本来说，这种最原始的方法反而可以更有效的实现功能，但如果是动态文本，那还是不推荐这种方法的。

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
