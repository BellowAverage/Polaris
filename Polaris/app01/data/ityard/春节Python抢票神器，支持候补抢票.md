
--- 
title:  春节Python抢票神器，支持候补抢票 
tags: []
categories: [] 

---
车栗子 发自 凹非寺 

量子位 报道 | 公众号 QbitAI

想要回家的小伙伴们，大概经历了一波抢票大战。

顺便把一个**Python抢票工具**，送到了GitHub趋势榜第一。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9NUTRGb0cxSG1uS3pBeHVtV3lJVmNNdVhHZDM3dEk1V21kOGlibGRoZVR5MWRXM2NaV1FnUzFOTVRkd29URHU0SmVYTmlja3JObmljWUQzNGFVSVB6djJYZy82NDA?x-oss-process=image/format,png">

项目名很干脆，就是**12306**，来自名叫**文贤平**的程序员。

这很可能是全GitHub最德高望重的购票小助手了，功能一直在更新，且现已支持**Python 3.6**以上版本。

有些后起之秀，也是在它的基础上开发出来，然后广受欢迎。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9NUTRGb0cxSG1uS3pBeHVtV3lJVmNNdVhHZDM3dEk1V01VWFBXWlYyeWs0Zk03TDYwQVpRVUppYXdWT1dCa29BbmVadE92aExBVHlhT1VQdjgyS3dqbGcvNjQw?x-oss-process=image/format,png">

标星5k的**py12306**便是其中之一，它支持分布式抢票。

### 热榜第一的抢票神器

文贤平/文先森 (testerSunshine) 的抢票小助手12306，虽然诞生在2018年初，但最近一次提交代码，是在今年**9月5日**，现在还十分新鲜。

这只得力的小助手，思路清晰又紧凑：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9ZaWNVaGs1YUFHdERFenIwTGliTjVPVEZEOVZNT1VncWliUGlhTUN4U3lvQmJ0R3Q2VFplQzZOMDZQMWwwZGdyTGliWlc3cGE2UUlENXRmV3VEN2lic3lKRVdBUS82NDA?x-oss-process=image/format,png">

从查询余票开始，到付款完成，最后获取订单号。一气呵成，不怕人类手速太慢。

有了它，文先森去年就丝滑地抢到了回家的票。而后，便努力帮助抢票助手继续进化。

到目前为止，文先森与一众贡献者，已经在项目里提交了361次代码，实现的功能有这些：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9NUTRGb0cxSG1uS3pBeHVtV3lJVmNNdVhHZDM3dEk1VzhLZE1RQmljb3NOcUtxUDR6cXp2bXZmeDcwY0c5N2tuRXV4OGViTFVlMlAwZU9jVm9DUVdpYXhnLzY0MA?x-oss-process=image/format,png">

从更新日志看来，最近加入的重要功能是**候补订单**。

所谓候补，就是在票卖完的情况下预先付款，等其他人退票之后自动补上，是我国2019年春运才出现的新机制。

但文先森也还不清楚，这项功能在抢票助手里的需求是怎样的，所以正在密集地尝试和调整：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9ZaWNVaGs1YUFHdERFenIwTGliTjVPVEZEOVZNT1VncWliUGliTVltQnViVnJCbzhjSkR6WDJNSTg3bmdNbG5CV1RyaWFBckhwZVhOVzl3RXJ2WjlCSElXTFBnLzY0MA?x-oss-process=image/format,png">

在实现新功能的同时，已有的功能也在不断优化。

这个抢票工具越来越强大，GitHub标星数量比起年初的4k，也已经翻了一番。

随着项目的成长，文先森在8月31日宣布了一件重要的事：

>  
  放弃支持Python 2.7，只支持**3.6**以上版本。 
 

具体的食用方法，可以从传送门前往项目页观察。

如果，你在食用过程中遇到了障碍，**使用帮助**目录里也没找到解答，除了发起Issue，还可以进群讨论：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdERFenIwTGliTjVPVEZEOVZNT1VncWliUEtaQzIwemR5amFGc0o3dGxVMHhwQzdiTEE1elFBdGlhU1UxelBqM3dEZDc5M0dMM1dpYnBmY0dnLzY0MA?x-oss-process=image/format,png">

把失败的log发到群里，大佬说不定能帮你调出来。

不过，有了抢票助手，也不是一定买得到票。

所以，多试几种工具也是好的，尤其是可以**同时进行多个任务**的那种。

### 分布式抢票助手

一位名叫pjialin的程序员，借鉴了文先森的部分代码实现，开发了一个**分布式**工具，名叫**py12306购票助手**。

就是说，一台机器抢不到，可以让许多硬件一起跑。

它还支持**多任务** (多班列车) 、**多日期**、**多账号**一起查。

另一个机智的功能是，同时观察**多个****始发站**和**到达站**的组合。

比如，北京出发的票没有了，就跑去下一站上车；或者家门口买不到，就直接买到终点：愿意妥协但限于手速的小伙伴，也能交给工具自动查看了。

项目作者说，试过文先森的算法和bypass12306，未果，这才做出了自己的抢票工具。

用上这个新工具，他一下子抢到了好几张票。

同样是支持Python 3.6以上版本，这个项目现在也有4k标星了。

### 薪火承传

2010年初，官方上线12306。从那时起，程序员就开始用自己的方法查询余票了。

后来，越来越多的程序员加入这个队伍，他们的力量也越发强大，大到能让GitHub垮掉。

2012年，一位叫做iFish的大佬开发的插件，被各家浏览器的春节版本纷纷搭载，12306官方也引用了里面的一个资源。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdERFenIwTGliTjVPVEZEOVZNT1VncWliUHRmM1k4d1FlUEwyMFFETmdPeXlsdkQzckJEMnlXdFVnV3dVMHY0eVl3STdGc0tQSTZ4SmRWQS82NDA?x-oss-process=image/format,png">

就是它引发了著名的**12306订票助手拖垮GitHub**事件。

原因是插件的早期版本，用GitHub的Raw File服务作CDN，且如果返回403错误，就5秒重试一次，永久重试。

iFish大佬应该不会想到，巨大的访问量导致Github受到DDOS攻击，速度扑街。GitHub甚至想到找人联系12306官方，去除那个引用。

虽然，当年的事件过去了，但程序员对回家的渴望还在那里，就会不断孕育出新的抢票工具，拯救自己，拯救世界。

最后，祝小伙伴们都能顺利回家。

在公众号**Python小二**后台回复**12306**获取抢票项目。

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcFh1ZmlibEhVcndWT0loNFg4WWhwYXBpYU1rQk9sSE16b0ZRQm1Qd3dUWEREOG1Dd3pQWEdydUxRbEVBR1VTT3c4aWNQV0FydnRRaWFMTVEvNjQw?x-oss-process=image/format,png">

微信扫描关注，查看更多内容
