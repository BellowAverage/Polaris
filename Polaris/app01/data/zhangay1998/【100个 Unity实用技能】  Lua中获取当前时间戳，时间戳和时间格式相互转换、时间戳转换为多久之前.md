
--- 
title:  【100个 Unity实用技能】 | Lua中获取当前时间戳，时间戳和时间格式相互转换、时间戳转换为多久之前 
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

#### Lua中获取当前时间戳，时间戳转换为时间格式、时间戳转换为多久之前

在Lua中我们有时候时间相关的内容，如获取当前的时间戳，将时间戳转换为时间格式，将时间戳转换为多久之前等。

主要使用了Lua 中的 `os.time` 函数和 `os.tade` 函数。

>  
 Lua 标准库中提供了关于时间的函数`os.time()`和`os.date()`，这两个函数使用起来还是有需要注意的地方的。 这两个函数的结果都是加入了时区；比如我们现在系统是GMT+8; os.time({year=1970, month=1, day=1, hour=0})计算出来的是-28800，也就是86060； 计算的是当前table中给定的时间距离1970.1.1 08：00时间的秒数，所以就得到负数了； 
 C标准库中，time()函数得到的时间戳其实也是加入了时区，也就是说不管你系统是那个时区，该函数返回的都是距离1970.1.1 00:00到当前的秒数； 比如现在是GMT+8 00:00, 那么GMT+9 就是01:00，在这两个 时区同时调用time()函数，得到的值是一样的； 
 时区只会影响到我们转换过来的可读样式，比如os.date()函数，os.date(“*t”, 0)的结果在不同的时区hour字段的值会不一样，世界标准时间以GMT+0为参照，北京时间以GMT+8为参照，中间有8个小时的差距； 


下面就来介绍一下具体实现方法。

**1.Lua中获取当前时间戳方法：**

```
local t = os.time()

```

直接在Lua中执行此方法，可以获取到一个当前时间戳（也就是从1970年到当前时间为止的秒数）

**2.将时间戳转换为时间格式方法：**

```
--时间戳 转时间格式，t 是秒时间戳
function getTimeStamp(t)
    --如果毫秒 就是 t/1000

	-- 格式：年-月-日
    local str  =os.date("%Y-%m-%d",t)
    
    --格式：年-月-日-时
    --local str  =os.date("%Y-%m-%d-%H",t)
    
	--格式：年-月-日-时-分-秒
    --local str  =os.date("%Y-%m-%d %H:%M:%S",t)

    return str
end

```

**3.将时间格式转换为时间戳方法：**

```
local t = os.time(
	{<!-- -->
		--获取指定时间的时间戳，例如2023-3-21 00:00:00
		day=21, month=3, year=2023, hour=0, minute=0, second=0
	}) 

```

**4.时间戳转换为多久之前方法：** 使用时传入参数t， `t = 当前时间戳() - 指定时间的时间戳 `

比如服务端传给我们一封邮件的发送时间，我们可以通过该方法将邮件的发送时间转换为多久前发送。

```
--时间转换成多久前,传入时间戳t
function UIUtil.getTimeLongAgo(t)
    local str = ""
    if t ~= nil then
        if t &lt; 60 then
            str = string.format("%s秒",t)
        elseif t &gt;= 60 and t &lt; 3600 then
            local num = math.floor(t / 60)
            str = string.format("%s分钟",num)
        elseif t &gt;= 3600 and t &lt; 86400 then
            local num = math.floor(t / 3600)
            str = string.format("%s小时",num)
        elseif t &gt; 86400 and t &lt; 2592000 then
            local num = math.floor(t / 86400)
            str = string.format("%s天",num)
        elseif t &gt; 2592000 and t &lt; 31104000 then
            local num = math.floor(t / 2592000)
            str = string.format("%s个月",num)
        else
            local num = math.floor(t / 31104000)
            str = string.format("%s年",num)
        end
    end
    return str
end

```

<img src="https://img-blog.csdnimg.cn/20210613033645219.gif#pic_center" alt="在这里插入图片描述">
