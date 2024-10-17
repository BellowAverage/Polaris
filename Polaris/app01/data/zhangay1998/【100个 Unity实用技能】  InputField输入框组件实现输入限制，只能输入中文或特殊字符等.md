
--- 
title:  【100个 Unity实用技能】 | InputField输入框组件实现输入限制，只能输入中文或特殊字符等 
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
### <font color="#ff6984" size="5"> Unity </font>实用小技能学习

#### InputField输入框组件实现输入限制，只能输入中文或特殊字符等

在使用InputField的过程中，有些时候我们需要对一些输入字符做限制。 比如只允许输入整数，字母数字，允许字母和数字但无法输入符号，只能输入中文等输入限制。

这个使用InputField组件自带的属性ContentType可以直接解决掉部分限制。比如只能输入整数及只能输入字母和数字等，但是某些特殊性的限制就只能通过我们使用代码进行特殊限制了。

下面来介绍**只能输入中文的具体方法**。

首先新建一个脚本挂载到InputField组件的游戏对象上(或者其他场景物体)。

**方法一：onValidateInput：自定义验证回调** 此方法是使用Unity InputField组件的回调方法对每个输入的字符进行字符验证，然后我们对该字符进行相关判定即可。

代码如下：

```
using UnityEngine.UI;
using UnityEngine;

public class InputFieldTest : MonoBehaviour
{<!-- -->
    private InputField m_inputField;
    protected void Awake()
    {<!-- -->
        m_inputField= GetComponent&lt;InputField&gt;();
        m_inputField.onValidateInput = ValidateCallback;
    }

    private char ValidateCallback(string text, int charIndex, char ch)
    {<!-- -->
        //Debug.Log($"测试语言。text:{text}, charIndex:{charIndex}, ch:{ch}");
        if (ch &gt;= 0x4e00 &amp;&amp; ch &lt;= 0x9fa5)//汉字的范围
        {<!-- -->
            return ch;
        }
        else
        {<!-- -->
            return (char)0;
        }
    }
}

```

**方法二：onValueChanged配合Regex类**

此方法使用了.Net的 ，需要引入命名空间 `System.Text.RegularExpressions`。 然后使用 `Regex.IsMatch()` 进行匹配项验证，来筛选我们的字符做判定。

```
IsMatch(String) | 指示 Regex 构造函数中指定的正则表达式在指定的输入字符串中是否找到了匹配项。

```

代码如下：

```
using UnityEngine.UI;
using UnityEngine;
using System.Text.RegularExpressions;

public class InputFieldTest : MonoBehaviour
{<!-- -->
    private InputField m_inputField;
    protected void Awake()
    {<!-- -->
        m_inputField= GetComponent&lt;InputField&gt;();
        m_inputField.onValueChanged.AddListener(OnInputFieldValueChang);
    }
    private void OnInputFieldValueChang(string inputInfo)
    {<!-- -->
        Regex reg = new Regex("^[\u4e00-\u9fa5]+$");
        if (reg.IsMatch(inputInfo))
        {<!-- -->
            m_inputField.text = inputInfo;
        }
        else
        {<!-- -->
            if (m_inputField.text == "")
            {<!-- -->
                m_inputField.text = "";
            }
            else
            {<!-- -->
                m_inputField.text = inputInfo.Substring(0, inputInfo.Length - 1);
            }
        }
    }
}

```

效果如下： <img src="https://img-blog.csdnimg.cn/a27a603471c74d18817cc6e8efad1ab8.gif" alt="请添加图片描述">

若是想要一些指定的其他特殊输入限制，只需要变换if中的正则表达式条件即可。

UGUI组件学习文章： 正则表达式参考文章：

<img src="https://img-blog.csdnimg.cn/20210613033645219.gif#pic_center" alt="在这里插入图片描述">
