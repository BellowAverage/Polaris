
--- 
title:  【100个 Unity实用技能】☀️ | Unity中C#获取当前时间戳，时间戳和时间格式相互转换、时间戳转换为多久之前 
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
### <font color="#ff6984" size="5"> Unity </font>C#获取当前时间戳，时间戳和时间格式相互转换、时间戳转换为多久之前

##### 什么是时间戳

`时间戳` 一般是指格林威治时间1970年1月1日0时0分0秒起至现在的总毫秒数。

1970年01月01日00时00分00秒的来历：UNIX系统认为1970年1月1日0点是时间纪元，所以我们常说的UNIX时间戳是以1970年1月1日0点为计时起点时间的。

>  
 时间戳在有的地方是以秒数计算的，本文时间戳转换全部以毫秒数计算，防止搞混即可。 


##### 1. 获取当前时间的方法

```
        //方法一
        DateTime now = DateTime.Now;
        Debug.Log("当前北京时间：" + now);
        
        //方法二
        DateTime utcNow = DateTime.UtcNow;
        Debug.Log("当前国际时间：" + utcNow);

```

<img src="https://img-blog.csdnimg.cn/4e630da69e7145f69cdeb5b2dd4a04bb.png" alt="在这里插入图片描述">

##### 2. 获取当前时间戳的方法（此处获取的）

```
        //方法一
        long now1 = DateTime.UtcNow.Ticks;
        Debug.Log("当前时间戳：" + now1);
        
        //方法二
        long now2 = DateTime.Now.ToUniversalTime().Ticks;
        Debug.Log("当前时间戳：" + now2);

```

<img src="https://img-blog.csdnimg.cn/b4e895c7ab4b45158fce210d8b6b7de0.png" alt="在这里插入图片描述">

##### 3. 日期转为时间戳

```
        //方法一
        TimeSpan st = DateTime.UtcNow - new DateTime(1970, 1, 1, 0, 0, 0);
        Debug.Log("日期转为时间戳:"+Convert.ToInt64(st.TotalMilliseconds));
        
        //方法二
        double timeStamp = ((DateTime.Now.ToUniversalTime().Ticks - 621355968000000000) / 10000);
        Debug.Log("日期转为时间戳:" + timeStamp);

```

<img src="https://img-blog.csdnimg.cn/80e38b163837451d8ccfb75dd1f792c6.png" alt="在这里插入图片描述">

##### 4. 时间戳转时间

```
        //方法一
        DateTime startTime = TimeZoneInfo.ConvertTime(new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc), TimeZoneInfo.Local);
        DateTime dt = startTime.AddMilliseconds(st);//st为传入的时间戳
        Debug.Log("时间戳转时间:" + dt);
        
        //方法二
        DateTime startTime1 = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);
        DateTime dt1 = startTime1.AddMilliseconds(st);//st为传入的时间戳
        Debug.Log("时间戳转时间:" + dt);

```

<img src="https://img-blog.csdnimg.cn/942e9b738d1f4928a66be96347fdbe38.png" alt="在这里插入图片描述">

##### 5. 将时间戳转换为多久之前 的方法（此处方法传入的秒时间戳）

```
    /// &lt;summary&gt;
    /// 将秒数时间戳转换为多久之前。传入时间戳t(t= 当前时间戳() - 指定时间的时间戳 )
    /// &lt;/summary&gt;
    /// &lt;param name="t"&gt;&lt;/param&gt;
    /// &lt;returns&gt;&lt;/returns&gt;
    public string GetTimeLongAgo(double t)
    {<!-- -->
        string str = "";
        double num;
        if (t &lt; 60)
        {<!-- -->
            str = string.Format("{0}秒前", t);
        }
        else if (t &gt;= 60 &amp;&amp; t &lt; 3600)
        {<!-- -->
            num = Math.Floor(t / 60);
            str = string.Format("{0}分钟前", num);
        }
        else if (t &gt;= 3600 &amp;&amp; t &lt; 86400)
        {<!-- -->
            num = Math.Floor(t / 3600);
            str = string.Format("{0}小时前", num);
        }
        else if (t &gt; 86400 &amp;&amp; t &lt; 2592000)
        {<!-- -->
            num = Math.Floor(t / 86400);
            str = string.Format("{0}天前", num);
        }
        else if (t &gt; 2592000 &amp;&amp; t &lt; 31104000)
        {<!-- -->
            num = Math.Floor(t / 2592000);
            str = string.Format("{0}月前", num);
        }
        else
        {<!-- -->
            num = Math.Floor(t / 31104000);
            str = string.Format("{0}年前", num);
        }
        return str;
    }

```

```
	Debug.Log(GetTimeLongAgo(601));

```

<img src="https://img-blog.csdnimg.cn/e10e72828ff642428ce2268019ec03af.png" alt="在这里插入图片描述">

<font color="#ff6984" size="5"> **资料白嫖，技术互助**</font>

|学习路线指引（点击解锁）|知识定位|人群定位
|------
||入门级|本专栏从Unity入门开始学习，快速达到Unity的入门水平
||进阶级|计划制作Unity的 100个实战案例！助你进入Unity世界，争取做最全的Unity原创博客大全。
||难度偏高|分享学习一些Unity成品的游戏Demo和其他语言的小游戏！
||互助/吹水|数万人游戏爱好者社区，聊天互助，白嫖奖品
||Unity查漏补缺|针对一些Unity中经常用到的一些小知识和技能进行学习介绍，核心目的就是让我们能够快速学习Unity的知识以达到查漏补缺

<img src="https://img-blog.csdnimg.cn/20210613033645219.gif#pic_center" alt="在这里插入图片描述">
