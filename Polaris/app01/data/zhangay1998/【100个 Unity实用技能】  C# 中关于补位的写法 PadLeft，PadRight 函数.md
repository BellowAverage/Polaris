
--- 
title:  【100个 Unity实用技能】 | C# 中关于补位的写法 PadLeft，PadRight 函数 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/4ea0ad75b9c145e5ba7d219b7e425099.png" alt="请添加图片描述">

### <font color="#ff6984" size="5"> Unity </font>小科普

老规矩，先介绍一下<font color="#ff6984" size="4"> **Unity** </font>的科普小知识：<img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述">
- <font color="#ff6984" size="4">**Unity**</font>是 实时3D互动内容创作和运营平台 。- 包括<font color="#green" size="4">游戏开发</font>、<font color="#green" size="4">美术</font>、<font color="#green" size="4">建筑</font>、<font color="#green" size="4">汽车设计</font>、<font color="#green" size="4">影视</font>在内的所有创作者，借助<font color="#ff6984" size="4"> **Unity** </font>将创意变成现实。- <font color="#ff6e84" size="4">**Unity**</font> 平台提供一整套完善的软件解决方案，可用于创作、运营和变现任何实时互动的2D和3D内容，支持平台包括<font color="#green" size="4">手机</font>、<font color="#green" size="4">平板电脑</font>、<font color="#green" size="4">PC</font>、<font color="#green" size="4">游戏主机</font>、<font color="#green" size="4">增强现实</font>和<font color="#green" size="4">虚拟现实设备。 </font>- 也可以简单把 <font color="#ff6e84" size="4">**Unity**</font> 理解为一个<font color="#ee82ee" size="4">游戏引擎</font>，可以用来专业制作<font color="#ee0000" size="4">游戏</font>！
>  
 -  🎬 博客主页： -  🎥 本文由 **呆呆敲代码的小Y** 原创，首发于 **CSDN**🙉 -  🎄 学习专栏推荐： -  🌲 游戏制作专栏推荐： -  🌲Unity实战100例专栏推荐： -  🏅 欢迎点赞 👍 收藏 ⭐留言 📝 如有错误敬请指正！ -  📆 未来很长，值得我们全力奔赴更美好的生活✨ -  ------------------❤️分割线❤️-------------------------  


<img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述">

<img src="https://img-blog.csdnimg.cn/01e7ec91f0984ce4a166bf72cb52bea5.gif" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述">

### <font color="#ff6984" size="5"> Unity </font>实用小技能学习

#### C# 中关于补位的写法 PadLeft，PadRight 函数

C# 的补位函数 PadLeft，PadRight。

在C#中，`PadLeft()` 和 `PadRight()` 是一个字符串方法。此种方法是通过在给定字符串的左侧/右侧补充指定字符到我们指定的长度，它有两个重载方法。
1. String.PadLeft方法（Int32）1. String.PadLeft方法（Int32，字符）
当我们不指定补齐的字符时，系统会用空格将设置的位数补齐，设置特定字符时，使用特定字符将其补齐。

```
using UnityEngine;
using UnityEngine.UI;

public class NumberTest : MonoBehaviour
{<!-- -->
    public Text txt1;
    public Text txt2;
    void Start()
    {<!-- -->
        var number = "01";
        txt1.text = number.ToString().PadLeft(5, '0');// 输出：00001
        txt2.text = number.ToString().PadRight(5, '0'); //输出：01000
    }
}

```

<img src="https://img-blog.csdnimg.cn/641f4586ece94eeca8d37e19ecb5b174.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/20210613033645219.gif#pic_center" alt="在这里插入图片描述">
