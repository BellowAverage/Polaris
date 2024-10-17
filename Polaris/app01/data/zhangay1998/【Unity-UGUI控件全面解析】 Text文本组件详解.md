
--- 
title:  【Unity-UGUI控件全面解析】| Text文本组件详解 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/4ea0ad75b9c145e5ba7d219b7e425099.png" alt="请添加图片描述"> 

####  
- - <ul><li>- - - - <ul><li>- - - - - - - 


>  
 -  🎬 博客主页： -  🎥 本文由 **呆呆敲代码的小Y** 原创，首发于 **CSDN**🙉 -  🎄 学习专栏推荐： -  🌲 游戏制作专栏推荐： -  🌲Unity实战100例专栏推荐： -  🏅 欢迎点赞 👍 收藏 ⭐留言 📝 如有错误敬请指正！ -  📆 未来很长，值得我们全力奔赴更美好的生活✨ -  ------------------❤️分割线❤️-------------------------  


<img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述">

<img src="https://img-blog.csdnimg.cn/01e7ec91f0984ce4a166bf72cb52bea5.gif" alt="请添加图片描述">

## 🎬【Unity-UGUI控件全面解析】| Text文本组件详解

<img src="https://img-blog.csdnimg.cn/eb148f3a374149c49782f346b8327092.gif" alt="请添加图片描述">

### 一、组件介绍

>  
 - **官方介绍：** The Text control displays a non-interactive piece of text to the user. This can be used to provide captions or labels for other GUI controls or to display instructions or other text.- 译文： 文本控件向用户显示非交互的文本。这可用于为其他GUI控件提供标题或标签，或显示说明或其他文本。- **官方使用手册地址**： **官方API地址**： 


Text文本，是为了向用户展示非交互式的文本信息。用于在工程中显示文字的地方(常用)，简单来说只要能看到字的情况下，一般都是用的这个组件。

在Hierarchy视图，选择 `UI→Text` 新建Text文本：

<img src="https://img-blog.csdnimg.cn/3a9137654512407face7ded537864659.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/fe502b1c9b834b82862f614ceba87e1b.png" alt="在这里插入图片描述">

### 二、组件属性面板

下面来介绍一下，Text组件的属性面板。 <img src="https://img-blog.csdnimg.cn/a092577eba954b5891d9f67beee88787.png" alt="在这里插入图片描述">

|属性|说明
|------
|Text|用于显示的文本
|Font|文本的字体
|Font Style|文本的样式（正常、加粗、斜线）
|Font Size|字体的大小
|Line Spacing|文本行之间的间距
|Rich Text|是否支持富文本，富文本是带有标记标签的文本，增强文本的显示效果
|Alignment|文本的水平和垂直对齐方式
|Align By Geometry|是否以当前所显示的文字中获得的最大长宽（而不是字体的长宽）进行对齐。
|Horizontal Overflow|文字横向溢出处理方式，可以选择Warp隐藏或者Overflow溢出
|Vertical Overflow|文本纵向溢出的处理方式，可以选择Truncate截断或者Overflow溢出
|Best Fit|忽略Font Size设置的文字大小，自适应改变文字大小以适应文本框的大小
|Color|文本的颜色
|Material|用来渲染文本的材质，可以通过设置材质，让文本拥有更加炫酷的效果。
|Raycast Target|是否可以被射线检测，通常情况下可以关闭，因为文本最好只用来显示。
|Raycast Padding|射线投射填充。
|Maskable|是否可以遮盖。

文本控件提供字体大小、样式以及文本对齐方式等常用参数。启用 Rich Text 选项后，文本中的标记元素将视为样式信息，因此可仅让单个单词或短段使用粗体或不同颜色等。

### 三、代码操作组件

```
using UnityEngine;
using UnityEngine.UI;

public class UGUI_Text : MonoBehaviour
{<!-- -->
    private Text m_Text;
    private void Awake()
    {<!-- -->
        m_Text = transform.GetComponent&lt;Text&gt;();
        SetTextStyle();
    }

    public void SetTextStyle()
    {<!-- -->
        m_Text.text = "Xiao Y";

        #region ------ 【Charater】 ------
        //字体大小
        m_Text.fontSize = 15;
        //文字格式正常,斜体,粗斜,加粗
        m_Text.fontStyle = FontStyle.Normal;//.Italic.BoldAndItalic.Bold;
        //行间距
        m_Text.lineSpacing = 1.2f;
        //是否支持富文本
        m_Text.supportRichText = true;
        #endregion

        #region ------ 【Prargraph】 ------
        //对齐方式 各种TextAnchor枚举对齐
        m_Text.alignment = TextAnchor.LowerCenter;
        //使用字形几何范围来执行水平对齐，而不是使用音质度量。
        m_Text.alignByGeometry = false;

        //水平竖直模式 ==》 Overflow:溢出模式【不考虑文本的width或者height的限制,显示全部文本内容】
        //Wrap 或者 Truncate 在文本width或者height区域内显示,超出部分被隐藏【包括字体大小超出】
        m_Text.horizontalOverflow = HorizontalWrapMode.Overflow;
        m_Text.verticalOverflow = VerticalWrapMode.Truncate;

        //应该允许文本自动调整大小。
        m_Text.resizeTextForBestFit = true;
        //设置 BestFit 为True后
        //当前文本区域显示不开后，内容会自动缩小字号;  【忽略原字体大小】
        m_Text.resizeTextMinSize = 15;
        m_Text.resizeTextMaxSize = 30;
        #endregion

        //文本颜色 【有渐变色时,此属性不起作用】
        m_Text.color = new Color32(0, 0, 0, 0);

        //文本材质 path:是Resources下面材质目录
        m_Text.material = Resources.Load("path", typeof(Material)) as Material;

        //是否进行射线检测
        m_Text.raycastTarget = false;
    }
}

```

### 四、组件常用方法示例

#### 4.1 改变Text文本颜色

方法一：通过代码修改字体颜色

```
using UnityEngine;
using UnityEngine.UI;

public class UGUI_Text : MonoBehaviour
{<!-- -->
    private Text m_Text;

    void Start()
    {<!-- -->
        m_Text = transform.GetComponent&lt;Text&gt;();
        m_Text.color = new Color(0 / 255f, 0 / 255f, 255 / 255f, 255 / 255f);
    }
}

```

这种方法是直接给Text组件的Color属性赋值即可。 <img src="https://img-blog.csdnimg.cn/1bce27777d474b17822a67b376af2912.png" alt="在这里插入图片描述"> 方法二：通过标签代码修改字体颜色

```
&lt;color=red&gt;Xiao Y&lt;/color&gt;

```

<img src="https://img-blog.csdnimg.cn/46e3ef62cc55429f80b1ab81eb0254c2.png" alt="在这里插入图片描述"> 前提是打开了富文本选项，否则不会变色。 <img src="https://img-blog.csdnimg.cn/a0f68f91ca444673a30a570058b68dcf.png" alt="在这里插入图片描述">

#### 4.2 文本换行问题

在代码中使Text组件中的内容换行时，可以直接用换行符`\n`来执行

```
using UnityEngine;
using UnityEngine.UI;

public class UGUI_Text : MonoBehaviour
{<!-- -->
    private Text m_Text;

    void Start()
    {<!-- -->
        m_Text = transform.GetComponent&lt;Text&gt;();
        m_Text.text = "&lt;color=red&gt;Unity&lt;/color&gt;\n&lt;color=green&gt;小Y&lt;/color&gt;";
    }
}

```

效果： <img src="https://img-blog.csdnimg.cn/b09605ecaff04323a3c6bed0144b519d.png" alt="在这里插入图片描述">

但是直接在Editor的Text文本框中输入\n则是不可以的。 <img src="https://img-blog.csdnimg.cn/57a37e7b4be64545948941547003ce16.png" alt="在这里插入图片描述"> 这时候需要使用代码进行修复，使用Replace方法进行替换，这样在Text文本框内的\n就会执行换行功能了。

```
using UnityEngine;
using UnityEngine.UI;

public class UGUI_Text : MonoBehaviour
{<!-- -->
    private Text m_Text;

    void Start()
    {<!-- -->
        m_Text = transform.GetComponent&lt;Text&gt;();
        m_Text.text = m_Text.text.Replace("\\n", "\n");
    }
}

```

之前写过一篇文章介绍内容换行问题，有需要的也可以参考： 

#### 4.3 空格自动换行问题

在Text文本框输入空格时，后面的内容若是在本行中显示不开时，就会默认自动给我们换行显示。

如下所示： <img src="https://img-blog.csdnimg.cn/c1985daa8c2d49d39ea2002cbb907aa5.png" alt="在这里插入图片描述">

但这有时候并不是我们的本意，所以需要使用代码进行处理。

```
using UnityEngine;
using UnityEngine.UI;

public class UGUI_Text : MonoBehaviour
{<!-- -->
    private Text m_Text;

    void Start()
    {<!-- -->
        m_Text = transform.GetComponent&lt;Text&gt;();
        m_Text.text = m_Text.text.Replace(" ", "\u3000");
    }
}

```

代码处理后效果： <img src="https://img-blog.csdnimg.cn/3452c78c96c945ef94113a26d73d6eeb.png" alt="在这里插入图片描述"> 与上面的换行类似，也是使用Replace方法进行替换，将空格替换为"\u3000"字符就可以了。

#### 4.4 逐字显示效果

**方法一**：在Unity中使用代码实现

```
using System.Collections;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.UI;

public class UGUI_Text : MonoBehaviour
{<!-- -->
    public uint m_TextIndent;       //首行缩进--字符数
    [TextArea(4, 10)]
    public string m_Text;           //显示的文本内容
    public bool m_Enable;           //是否在OnEnable中初始化Play
    private Text m_Conetnt;         //用于显示的文本
    [Header("字/每秒")]
    public float m_ShowSpeed = 1;   //动态文字的速度
                                    //与文字播放同时播放的音频
    public AudioClip m_AudioClip;
    //文字播完回调
    public CallBack m_CallBack = new CallBack();

    public ScrollRect m_ScrollRect;


    private char[] m_Text_Char;
    private bool suspend = false;
    private AudioSource m_AudioSource;


    private void Awake()
    {<!-- -->
        m_Conetnt = this.GetComponent&lt;Text&gt;();
    }
    private void OnEnable()
    {<!-- -->
        if (m_Enable)
            Play();
    }
    /// &lt;summary&gt;
    /// 重新播放
    /// &lt;/summary&gt;
    public void Play()
    {<!-- -->
        suspend = false;
        //\u3000为中文空格英文空格会引起unity中Text的自动换行因此将内容中的英文空格换成中文空格
        string str = m_Text.Replace(" ", "\u3000");
        string LineHead = "";
        //设置段落的首行缩进的字符数
        if (m_TextIndent != 0)
        {<!-- -->
            for (int i = 0; i &lt; m_TextIndent; i++)
            {<!-- -->
                LineHead += "\u3000";
            }
            str = str.Replace("\n", "\n" + LineHead);
            str = LineHead + str;
        }
        //将转换好的文本转换成Char数组以便于逐字读写
        m_Text_Char = str.ToCharArray();
        //当音频不为空时，处理音频的播放
        if (m_AudioClip != null)
        {<!-- -->
            if (m_AudioSource == null)
                m_AudioSource = this.GetComponent&lt;AudioSource&gt;();
            if (m_AudioSource == null)
                m_AudioSource = this.gameObject.AddComponent&lt;AudioSource&gt;();
            m_AudioSource.clip = m_AudioClip;
            //读写速度根据音频长度平均计算
            m_ShowSpeed = str.Length / m_AudioClip.length;
        }
        StartCoroutine("Player");
    }
    /// &lt;summary&gt;
    /// 播放无语音
    /// &lt;/summary&gt;
    /// &lt;param name="varCentent"&gt;播放的内容&lt;/param&gt;
    public void Play(string varCentent)
    {<!-- -->
        m_Text = varCentent;
        m_AudioClip = null;
        Play();
    }
    /// &lt;summary&gt;
    /// 播放有语音
    /// &lt;/summary&gt;
    /// &lt;param name="varCentent"&gt;播放的内容&lt;/param&gt;
    /// &lt;param name="audio"&gt;跟踪的语言&lt;/param&gt;
    public void Play(string varCentent, AudioClip audio)
    {<!-- -->
        m_Text = varCentent;
        m_AudioClip = audio;

        Play();
    }

    /// &lt;summary&gt;
    /// 暂停播放
    /// &lt;/summary&gt;
    public void Pause()
    {<!-- -->
        suspend = true;
    }
    /// &lt;summary&gt;
    /// 恢复播放
    /// &lt;/summary&gt;
    public void Recovery()
    {<!-- -->
        suspend = false;
    }

    /// &lt;summary&gt;
    /// 停止播放（无法继续）
    /// &lt;/summary&gt;
    public void Stop()
    {<!-- -->
        StopCoroutine("Player");
    }


    IEnumerator Player()
    {<!-- -->
        float idx = 0;
        m_Conetnt.text = "";
        yield return 0;
        if (m_AudioSource != null)
            m_AudioSource.Play();
        RectTransform TempCententRect = null;
        RectTransform TempScrollRect = null;
        if (m_ScrollRect != null)
        {<!-- -->
            TempCententRect = m_ScrollRect.content.GetComponent&lt;RectTransform&gt;();
            TempScrollRect = m_ScrollRect.GetComponent&lt;RectTransform&gt;();
        }
        while (idx &lt;= m_Text_Char.Length)
        {<!-- -->
            //暂停处理
            if (suspend)
            {<!-- -->
                yield return new WaitForFixedUpdate();
                continue;
            }
            float TempTimes = Time.fixedDeltaTime;
            float currfont = TempTimes * m_ShowSpeed;
            //更新应显示的字的数量
            idx += currfont;
            string currcentent = "";
            //获取显示的字的内容
            for (int i = 0; i &lt; m_Text_Char.Length; i++)
            {<!-- -->
                if (i &lt;= idx)
                    currcentent += m_Text_Char[i];
                //过滤换行字符
                else if (m_Text_Char[i] == '\n')
                    idx += 1;
                //过滤空格
                else if (m_Text_Char[i] == ' ' || m_Text_Char[i] == '\u3000')
                    idx += 1;
                else
                    break;
            }
            m_Conetnt.text = currcentent;
            //当有ScrollRect时让文字始终显示刷新文字的地方
            if (m_ScrollRect != null)
            {<!-- -->
                //更新滑动区域大小使之与文本框大小相同（仅高度相同）
                TempCententRect.sizeDelta = new Vector2(TempCententRect.sizeDelta.x, m_Conetnt.preferredHeight);
                //当滑动高度大于ScrollRect的显示高度时保证滑动区域始终在最下方
                if (TempCententRect.sizeDelta.y &gt; TempScrollRect.sizeDelta.y)
                {<!-- -->
                    if (m_ScrollRect.verticalScrollbar != null)
                        m_ScrollRect.verticalScrollbar.value = 0;
                }
            }
            //与FixedUpdate同步避免程序卡死
            yield return new WaitForFixedUpdate();
        }
        //当音频不为空时处理音频
        if (m_AudioSource != null)
        {<!-- -->
            //当音频未播放完成时不结束进程
            while (m_AudioSource.isPlaying)
            {<!-- -->
                //与FixedUpdate同步避免程序卡死
                yield return new WaitForFixedUpdate();
            }
        }
        //音频播放完成清理音频信息
        if (m_AudioSource != null)
            Destroy(m_AudioSource);
        //等待一帧以便以上信息运行完成
        yield return 0;
        m_AudioSource = null;
        //执行播放完成回调
        m_CallBack.Invoke();
    }
    public class CallBack : UnityEvent
    {<!-- -->
        public CallBack()
        {<!-- -->
        }
    }
}

```

<img src="https://img-blog.csdnimg.cn/9f594870e1884998a51cfb3d50ce74aa.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b8eac7453acf442681fd09a3bb42e709.gif" alt="请添加图片描述"> 此方法参考：

**方法二**：使用 `DOTween插件`实现

使用 DOTween 中的方法 DOText() 可以实现逐字显示效果。

```
using UnityEngine;
using UnityEngine.UI;
using DG.Tweening;

public class UGUI_Text : MonoBehaviour {<!-- -->

	private Text m_Text;
	void Start () {<!-- -->
		//获取Text组件
		m_Text= this.GetComponent&lt;Text&gt;();
		//您要显示文本内容
		string temp_content = "小Y 测试Text文本框逐字显示效果。";
		
		m_Text.DOText(temp_content, 6);

		//带回调的方式
		//m_Text.DOText(temp_content, 6).OnComplete(()=&gt; {<!-- -->
		//	Debug.Log("逐字显示完成的回调");
		//});

		//添加Ease枚举中设定的缓动动画
		//m_Text.DOText(temp_content, 6).SetEase(Ease.InBack).OnComplete(() =&gt; {<!-- -->
		//	Debug.Log("逐字显示完成的回调");
		//});
	}
}

```

<img src="https://img-blog.csdnimg.cn/e82efb51b1aa4575a30c172efdc40cc3.gif" alt="请添加图片描述">

### 五、组件相关扩展使用

#### 5.1 文本描边组件（Outline）

使用Outline组件可以实现文本内容描边效果。

<th align="left">属性</th><th align="left">功能</th>
|------
<td align="left">Effect Color</td><td align="left">轮廓的颜色。</td>
<td align="left">Effect Distance</td><td align="left">轮廓效果在水平和垂直方向的距离。</td>
<td align="left">Use Graphic Alpha</td><td align="left">将图形颜色叠加到效果颜色上。</td>

<img src="https://img-blog.csdnimg.cn/be4b4e852a474d37a3fd8a7aefdfc411.png" alt="在这里插入图片描述">

#### 5.2 阴影组件（Shadow）

使用Shadow组件可以实现文本内阴影效果。

<th align="left">属性</th><th align="left">功能</th>
|------
<td align="left">Effect Color</td><td align="left">阴影的颜色。。</td>
<td align="left">Effect Distance</td><td align="left">阴影的偏移（表示为矢量）。</td>
<td align="left">Use Graphic Alpha</td><td align="left">将图形颜色叠加到效果颜色上。</td>

<img src="https://img-blog.csdnimg.cn/b6808640f90d4e3d850e4ddebd9a8f46.png" alt="在这里插入图片描述">

#### 5.3 渐变色效果

<th align="left">属性</th><th align="left">功能</th>
|------
<td align="left">Top Color</td><td align="left">顶部渐变的颜色。</td>
<td align="left">Bottom Color</td><td align="left">底部渐变的颜色。</td>
<td align="left">Use Graphic Alpha</td><td align="left">将图形颜色叠加到效果颜色上。</td>

<img src="https://img-blog.csdnimg.cn/19d5e8515b2b4427a60ee23bbd23b322.png" alt="在这里插入图片描述">

渐变脚本FontGradient 代码如下：

```
using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using System;

/// &lt;summary&gt;
/// 渐变字体
/// &lt;/summary&gt;
[AddComponentMenu("UI/Effects/Gradient")]
public class FontGradient : BaseMeshEffect
{<!-- -->
    public Color32 topColor = Color.white;
    public Color32 bottomColor = Color.black;
    public bool useGraphicAlpha = true;
    public override void ModifyMesh(VertexHelper vh)
    {<!-- -->
        if (!IsActive())
        {<!-- -->
            return;
        }

        var count = vh.currentVertCount;
        if (count == 0)
            return;

        var vertexs = new List&lt;UIVertex&gt;();
        for (var i = 0; i &lt; count; i++)
        {<!-- -->
            var vertex = new UIVertex();
            vh.PopulateUIVertex(ref vertex, i);
            vertexs.Add(vertex);
        }

        var topY = vertexs[0].position.y;
        var bottomY = vertexs[0].position.y;


        for (var i = 1; i &lt; count; i++)
        {<!-- -->
            var y = vertexs[i].position.y;
            if (y &gt; topY)
            {<!-- -->
                topY = y;
            }
            else if (y &lt; bottomY)
            {<!-- -->
                bottomY = y;
            }

        }

        var height = topY - bottomY;
        for (var i = 0; i &lt; count; i++)
        {<!-- -->
            var vertex = vertexs[i];

            var color = Color32.Lerp(bottomColor, topColor, (vertex.position.y - bottomY) / height);

            vertex.color = color;

            vh.SetUIVertex(vertex, i);
        }
    }
}

```

上述几种效果可以叠加使用，具体效果可自行尝试。

#### 5.4 Text下划线效果

<img src="https://img-blog.csdnimg.cn/4f3b23112e1b4426b1210da9a47b9e01.png" alt="在这里插入图片描述">

下划线脚本MultipleLinkButton 代码如下：

```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.UI;

class UnderlineProperty
{<!-- -->
    public Color _color;
    public Vector3 _position;
    public float _width;
    public float _height;
    public Vector2 _privot;
}

public class MultipleLinkButton : MonoBehaviour, IPointerDownHandler, IPointerUpHandler
{<!-- -->
    private Text _text;
    private int _curCharacterCount = 0;
    private List&lt;Image&gt; _lines = new List&lt;Image&gt;();
    private System.Action _clickEvent = null; //下划线点击事件
    private bool _isInitUnderline = false;

    public System.Action ClickEvent
    {<!-- -->
        get
        {<!-- -->
            return _clickEvent;
        }

        set
        {<!-- -->
            _clickEvent = value;
        }
    }

    // Use this for initialization
    void Start()
    {<!-- -->
        _text = transform.GetComponent&lt;Text&gt;();
        _text.gameObject.AddComponent&lt;Button&gt;().onClick.AddListener(() =&gt; {<!-- -->
            if (ClickEvent != null)
                ClickEvent();
        });
    }

    void Update()
    {<!-- -->
        //做初始化
        if (_text.cachedTextGenerator.lineCount &gt; 0 &amp;&amp; !_isInitUnderline)
        {<!-- -->
            _isInitUnderline = true;
            _curCharacterCount = _text.cachedTextGenerator.characterCount;
            List&lt;UnderlineProperty&gt; list = GetUnderlinePropertys();
            CreateUnderLines(list);
        }

        //刷新
        if (_isInitUnderline &amp;&amp; _curCharacterCount != _text.cachedTextGenerator.characterCount)
        {<!-- -->
            _curCharacterCount = _text.cachedTextGenerator.characterCount;
            List&lt;UnderlineProperty&gt; list = GetUnderlinePropertys();
            CreateUnderLines(list);
        }
    }

    List&lt;UnderlineProperty&gt; GetUnderlinePropertys()
    {<!-- -->
        List&lt;UnderlineProperty&gt; list = new List&lt;UnderlineProperty&gt;();
        for (int i = 0; i &lt; _text.cachedTextGenerator.lineCount; i++)
        {<!-- -->
            var curPos = _text.cachedTextGenerator.characters[_text.cachedTextGenerator.lines[i].startCharIdx].cursorPos;
            UnderlineProperty property = new UnderlineProperty
            {<!-- -->
                _color = _text.color,
                _height = _text.fontSize / 10 == 0 ? 1 : _text.fontSize / 10,
                _width = GetWidth(_text.cachedTextGenerator.lines[i].startCharIdx, _text.cachedTextGenerator.characters),
                _position = new Vector3(curPos.x, curPos.y - _text.cachedTextGenerator.lines[i].height, 0),
                _privot = GetTextAnchorPivot(_text.alignment)
            };

            list.Add(property);
        }

        return list;
    }

    float GetWidth(int idx, IList&lt;UICharInfo&gt; info)
    {<!-- -->
        float width = 0;
        float start = info[idx].cursorPos.x;
        for (int i = idx; i &lt; info.Count - 1; i++)
        {<!-- -->
            if (info[i].cursorPos.x &gt; info[i + 1].cursorPos.x)
            {<!-- -->
                width = info[i].cursorPos.x - start;
                break;
            }

            if (info.Count - 1 == i + 1)
                width = info[i + 1].cursorPos.x - start;
        }
        return width;
    }

    Vector2 GetTextAnchorPivot(TextAnchor anchor)
    {<!-- -->
        switch (anchor)
        {<!-- -->
            case TextAnchor.LowerLeft: return new Vector2(0, 0);
            case TextAnchor.LowerCenter: return new Vector2(0.5f, 0);
            case TextAnchor.LowerRight: return new Vector2(1, 0);
            case TextAnchor.MiddleLeft: return new Vector2(0, 0.5f);
            case TextAnchor.MiddleCenter: return new Vector2(0.5f, 0.5f);
            case TextAnchor.MiddleRight: return new Vector2(1, 0.5f);
            case TextAnchor.UpperLeft: return new Vector2(0, 1);
            case TextAnchor.UpperCenter: return new Vector2(0.5f, 1);
            case TextAnchor.UpperRight: return new Vector2(1, 1);
            default: return Vector2.zero;
        }
    }

    void CreateUnderLines(List&lt;UnderlineProperty&gt; list)
    {<!-- -->
        for (int i = 0; i &lt; transform.childCount; i++)
            Destroy(transform.GetChild(i).gameObject);
        _lines.Clear();

        for (int i = 0; i &lt; list.Count; i++)
        {<!-- -->
            //初始化
            GameObject obj = new GameObject();
            obj.transform.SetParent(transform, false);
            obj.name = "underline" + i;
            _lines.Add(obj.AddComponent&lt;Image&gt;());
            _lines[i].rectTransform.pivot = list[i]._privot;

            //颜色和大小
            var tex = new Texture2D((int)list[i]._width, (int)list[i]._height, TextureFormat.ARGB32, false);
            Color[] colors = tex.GetPixels();
            for (int j = 0; j &lt; colors.Length; j++)
                colors[j] = list[i]._color;
            tex.SetPixels(colors);
            tex.Apply();
            _lines[i].sprite = Sprite.Create(tex, new Rect(0, 0, tex.width, tex.height), Vector2.zero);
            _lines[i].SetNativeSize();
            _lines[i].rectTransform.sizeDelta = new Vector2(_lines[i].rectTransform.sizeDelta.x, _lines[i].rectTransform.sizeDelta.y);

            //坐标
            float x = list[i]._position.x;
            if (_text.alignment == TextAnchor.MiddleCenter || _text.alignment == TextAnchor.UpperCenter || _text.alignment == TextAnchor.LowerCenter)
                x = 0;
            if (_text.alignment == TextAnchor.MiddleRight || _text.alignment == TextAnchor.UpperRight || _text.alignment == TextAnchor.LowerRight)
                x += list[i]._width;
            _lines[i].rectTransform.anchoredPosition = new Vector2(x, list[i]._position.y);
        }
    }

    /*实现下划线同步点击效果*/
    public void OnPointerDown(PointerEventData eventData)
    {<!-- -->
        for (int i = 0; i &lt; _lines.Count; i++)
        {<!-- -->
            Color[] colors = _lines[i].sprite.texture.GetPixels();
            for (int j = 0; j &lt; colors.Length; j++)
                colors[j] = new Color(colors[j].r, colors[j].g, colors[j].b, colors[j].a * 0.70f);
            _lines[i].sprite.texture.SetPixels(colors);
            _lines[i].sprite.texture.Apply();
        }
    }

    public void OnPointerUp(PointerEventData eventData)
    {<!-- -->
        for (int i = 0; i &lt; _lines.Count; i++)
        {<!-- -->
            Color[] colors = _lines[i].sprite.texture.GetPixels();
            for (int j = 0; j &lt; colors.Length; j++)
                colors[j] = new Color(colors[j].r, colors[j].g, colors[j].b, colors[j].a / 0.70f);
            _lines[i].sprite.texture.SetPixels(colors);
            _lines[i].sprite.texture.Apply();
        }
    }
}

```

此处参考文章：

## 💯总结

关于 `UGUI-Text` 组件的学习教程就到这里啦，若是有关于此组件有什么不明白的也可以在评论区提出一起讨论哦。
- 本系列文章目录如下：- - - - - - - - - - - 【- - 
系列内容使用的Unity版本皆为 Unity 2020 及以上版本，组件的各项参数可能在不同版本之下略有不同，不过不会影响我们使用及教程的介绍，请放心食用(敏感肌也可以使用哦😁)！

<img src="https://img-blog.csdnimg.cn/20210613033645219.gif#pic_center" alt="在这里插入图片描述">
