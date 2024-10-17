
--- 
title:  【100个 Unity实用技能】 | Unity中Text文本框 和 InputField文本输入框 内容换行问题 
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

### Unity中Text文本框 和 InputField文本输入框 内容换行问题

在进行文本内容输入的时候，可能会遇到想要内容换行的情况。

想要**Text文本进行换行**很简单，在代码中加入 `\n ` 即可。

但是如果我们在Unity 的 Text面板 上手动输入内容加上`\n `的时候确实没法使其换行。

这可能是因为Unity把 `\n`识别成了 `\\n`。

所以我们可以使用代码来替换 以达到换行的效果，示例如下：

```
 _t.text = _t.text.Replace("\\n", "\n");

```

效果如下： <img src="https://img-blog.csdnimg.cn/f646794c99da43908b24b661d4a4621d.gif" alt="请添加图片描述">

但是想要 `InputField 输入框` 中的内容换行的话这样还不够。

还要在 `InputField属性面板` 中将内容类型 改为 **多行提交** 或者 **多行新行**才可以。 <img src="https://img-blog.csdnimg.cn/cb4f39437927435ea6e77ebd33ff5b60.png" alt="在这里插入图片描述">

然后就跟Text文本一样添加 `\n`代码即可，下面用一个示例来演示效果。

代码如下：

```
    public Text _text1;
    public InputField _inputField1;

    private float _timer=0f;
    private int _flag = 0;

    void Update()
    {<!-- -->
        _timer += Time.deltaTime;

        if (_timer&gt;=2)
        {<!-- -->
            _text1.text += "Text文本内容增加了！"+ _flag+ "\n";
            _inputField1.text += "InputField输入框内容增加了！" + _flag + "\n";

            _flag++;
            _timer = 0;
        }
    }

```

效果如下： <img src="https://img-blog.csdnimg.cn/b291eaaca84443e18e1c28faf1cf91c2.gif" alt="请添加图片描述">

很简单的一个小功能，但是偶尔用一次反而找不到如何设置，仅此记录一下。
