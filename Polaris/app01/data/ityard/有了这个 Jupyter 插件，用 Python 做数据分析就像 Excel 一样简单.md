
--- 
title:  有了这个 Jupyter 插件，用 Python 做数据分析就像 Excel 一样简单 
tags: []
categories: [] 

---
```


```

###### 萧箫 发自 凹非寺量子位 报道 | 公众号 QbitAI

加载一个Jupyter插件后，无需写代码就能做数据分析，**还帮你生成相应代码**？

<img src="https://img-blog.csdnimg.cn/img_convert/90c0fb386940adb327893e66131b0814.gif">

没错，只需要加载这个名为**Mito**的小工具包，用Python做数据分析，变得和用Excel一样简单：

<img src="https://img-blog.csdnimg.cn/img_convert/39263cf2fa15881b8bff159a5c492427.gif">

运行速度比Excel更快，也不需要到处搜各种Python教程了。

### 好用如Excel，更快更全面

**Mito**是Jupyter notebook的一个**可编辑电子表格**插件，在编辑**.csv**表格（带格式转换功能）时，就能生成相关Python代码。

###### **<img src="https://img-blog.csdnimg.cn/img_convert/4b29f0554f21475a15dda0f7afe2eba1.png">△**Mito，线粒体Mitochondria的缩写

具体来说，Mito的出现，像是将**Python**的强大功能、和**Excel**的易用性进行了结合。

只需要掌握Excel的用法，就能使用Python的数据分析功能，还能将写出来的代码“打包带走”。

它弥补了Excel在数据分析上的几个**缺陷**：
- Excel无法做大数据分析（大型数据集处理得不好）- Excel运行缓慢- Excel无法轻松创建可重复流程
同时，又比SQL和Python更**简单**、直观。毕竟这些专业工具对于0基础初学者来说，需要至少几年时间，才能完全上手。

据Mito内测用户表示，这款插件让他们用Python做数据分析的效率提升了**10倍**，因为用户可以直接在Mito里编写Excel公式，如=SUM(A1, 100)。

<img src="https://img-blog.csdnimg.cn/img_convert/6938aba03ae4ab4c95f395d668c4b8f1.png">

那么，Mito是怎么做到将Excel逻辑转换成Python代码的呢？

作者们编写了一种名为**Transpiler**的程序，有点类似于编译器的功能，采用**抽象语法树**（AST），解析Excel源代码，并转换成Python的源代码。

<img src="https://img-blog.csdnimg.cn/img_convert/c5d66887eed5461d6a08ad6366acf432.png">

相比于采用专业软件如Alteryx（需要5000美元/月）进行数据分析，Mito所生成的Python代码可以根据需要自行修改，灵活性更高一点。

目前，Mito采用**亚马逊云平台** （AWS）保存用户的相关数据，每个用户拥有一个独立账户。

当然，用户也可以选择将数据保存在本地。

### 自动生成Python代码

以分析美国各州的“家庭平均收入”和“允许托运的火车站数量”这两个数据的关系为例。

首先，**上传**“家庭平均收入”和“允许托运的火车站数量”两份数据。

数据处理的格式是.csv，当然也可以输入Excel文件，并用Mito转成两份.csv文件。

<img src="https://img-blog.csdnimg.cn/img_convert/eb39a342dd2466117c5242a16178ac3b.png">

然后，将这两份数据集**合并**在一起，只需要用鼠标勾选对应功能、选中相关数据列就行。

啪！代码就生成好了。

<img src="https://img-blog.csdnimg.cn/img_convert/b86bfb48d73d79d0c78e619eae5a3177.gif">

然后，是做**数据透视表**，在完成分组后，采用聚合（aggregate）功能来切换聚合方法。

<img src="https://img-blog.csdnimg.cn/img_convert/a5798aff4854115b694a22567a02ce3d.gif">

还包括**数据过滤**功能，同样立刻就能生成相关代码。

<img src="https://img-blog.csdnimg.cn/img_convert/e2acc65c92dc5a5bb73713602fc07c06.gif">

包含升降序**排序**功能，快速简洁。

<img src="https://img-blog.csdnimg.cn/img_convert/ff80608716e56d87c43e670655bb495e.gif">

然后就是相关数据统计、分析出结果了，流程直观。

<img src="https://img-blog.csdnimg.cn/img_convert/93376b497da9c121935fd54a2e53ddac.gif">

保存分析文件的方法也很简单，文件是以Python编写的，而不是用比较难懂的VBA。

<img src="https://img-blog.csdnimg.cn/img_convert/422d94f28c5044c079b5902de69ce5da.gif">

要想重复上面的步骤的话，也非常容易，Mito自带“重复已保存分析步骤”功能，一键就能用同样的方法分析其他数据。

<img src="https://img-blog.csdnimg.cn/img_convert/e4b9edcda88a099f32b18cd3d2cf140b.gif">

确实要比一行行编写代码简单多了。

### 关于Mito

那么，Mito的作者们，为什么要搞这个软件？

因为他们发现，所谓的“几天上手Python数据分析”，其实根本没有那么容易……

<img src="https://img-blog.csdnimg.cn/img_convert/024b01db5ea39249a97351d4636c0e98.png">

初学者要想用Python搞数据分析，就得不停地查看各种文档、和求助于StackOverflow。

要想真正快速用Python分析数据，最后还得自己编写软件。

三位作者Aaron Diamond-Reivich、Jake Diamond-Reivich和Nate Rush都来自宾大，在学校期间，他们学习了计算机科学、统计学和商业分析相关的课程。

<img src="https://img-blog.csdnimg.cn/img_convert/5e916f313a8cc71397c463229d1d672c.png">

也正是在搞数据分析的时候，他们萌生了想要制作Mito的想法。

作者表示，软件目前还没有开源，因为他们还在思考，如何支持维护这个项目，并转到开源路径上来。

<img src="https://img-blog.csdnimg.cn/img_convert/bd86b5654fc0034bed6c1220ecc1537a.png">

不过，它现在已经可以使用了。

感兴趣的小伙伴们，可以上手试试了~

项目主页：https://trymito.io/launch

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/9318122bdde999e79aa9c91f615b8e1a.gif">

微信扫码关注，了解更多内容
