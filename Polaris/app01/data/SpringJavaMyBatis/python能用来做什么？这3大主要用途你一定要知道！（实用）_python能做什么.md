
--- 
title:  python能用来做什么？这3大主要用途你一定要知道！（实用）_python能做什么 
tags: []
categories: [] 

---
导读：如果你想学Python，或者你刚开始学习Python，那么你可能会问：“我能用Python做什么？”

这个问题不好回答，因为Python有很多用途。

但是随着时间，我发现有Python主要有以下三大主要应用：

**Web开发**

**数据科学**：包括机器学习、数据分析和数据可视化

**脚本**

本文将依次介绍。

<img src="https://img-blog.csdnimg.cn/direct/27de803eea5247ee9e9096701edfb17c.png#pic_center" alt="在这里插入图片描述">

01 Web开发

Django和Flask等基于Python的Web框架最近在Web开发中非常流行。

这些Web框架可以帮助你用Python编写服务器端代码(后端代码)。这是在你的额服务器上运行的代码，而不是运行在用户设备和浏览器的代码(前端代码)。
1. 为什么需要Web框架
因为用Web框架可以更容易地构建通用后端逻辑。这包括将不同的URL映射到Python代码块，处理数据库以及生成用户在浏览器中看到的HTML文件。
1. 应该使用哪种Python Web框架
Django和Flask是最流行的两种Python Web框架。如果你刚刚入门，我建议使用其中一种。
1. Django和Flask有什么区别
Gareth Dwyer 关于这个问题有一篇出色的文章，在这里我引用几段： 主要区别

*Flask：能够实现简单、灵活和细致的控制。并能让你自己决定实现方式。

Django：提供了全面的体验：你可以获得管理面板、数据库接口、ORM(对象关系映射)以及开箱即用的应用程序和项目的目录结构。

如何选择

Flask：如果你关注的是经验和学习的机会，或者你想更多地控制使用哪些组件，比如你想使用哪些数据库以及如何与其进行交互。

Django：如果你关注最终产品，或者你正在研究一个简单的应用，比如新闻网站、网店或博客，并且你希望有单一实现的方式。* 换句话说，如果你是初学者，Flask可能是更好的选择，因为它要掌握的组件更少。此外，如果你想要更多的定制，那就选Flask。

根据我的数据工程师朋友Jonathan T Ho的说法，由于Flask 的灵活性，在创建REST API时，Flask 比Django 更适合。

另一方面，如果你想直接构建一些东西，Django可能会让你更快实现。

02 数据科学

数据科学，这里包括机器学习，数据分析和数据可视化。
1. 机器学习是什么
假设你想开发一个能够自动检测图片内容的程序。给出图1，你希望程序识别这是一只狗。

<img src="https://img-blog.csdnimg.cn/direct/c35ca8a655874753b5fff175238c3688.png#pic_center" alt="在这里插入图片描述">

▲图1

给出图2，希望程序能识别这是一张桌子。

<img src="https://img-blog.csdnimg.cn/direct/db958c6ed5e4475fbc3c1accd611a8a2.png#pic_center" alt="在这里插入图片描述">

▲图2

你可能会说，我可以写一些代码来做到这点。例如，如果图片中有很多浅棕色像素，那么可以识别是狗。

或者可以检测图片中的边缘，如果有很多直的边缘，那么就是桌子。

但这种方法很快就不好用了。如果图片中的狗不是棕色毛的怎么办？如果图片只显示桌子的圆形部分怎么办？

这里就需要用到机器学习了。

机器学习通过实现算法，该算法能够自动检测输入中的模式。

例如，你将1000张狗的图片和1000张桌子的图片输入给机器学习算法，让它掌握狗和桌子间的区别。那么当你给出新的图片让它识别是狗还是桌子时，它就能够进行判断。

这有点类似孩子学习新事物的方式。孩子是如何学习认知狗或桌子的呢？就是通过大量的例子。

你不会明确告诉孩子：“如果某个毛茸茸的东西有浅棕色的毛发，那么就可能是狗。”

你会说，“这是狗，这也是狗。而这是桌子，那个也是桌子。“

机器学习算法的方式大致相同。

我们可以将相同的想法应用于：

推荐系统：比如YouTube，亚马逊和Netflix

人脸识别

语音识别

以及其他应用。

你听过的热门机器学习算法包括：

神经网络

深度学习

支持向量机

随机森林

你可以使用上述任何算法来解决前面提到的图片标签问题。
1. 将Python用于机器学习
有一些热门的机器学习库和Python框架。其中两个最热门的是scikit-learn和TensorFlow。

scikit-learn带有一些内置的热门机器学习算法。

TensorFlow是一个低级库，能让你创建自定义机器学习算法。

如果你刚开始进行机器学习项目，我会建议你先从scikit-learn开始。如果你开始遇到效率问题，那么可以使用TensorFlow。
1. 数据分析和数据可视化
假设你在一家在线销售产品的公司工作。作为数据分析师，你会绘制这样的条形图。

<img src="https://img-blog.csdnimg.cn/direct/a738571b8baa497b81aeb2ef0d7a0d81.png#pic_center" alt="在这里插入图片描述">

▲条形图1 - 用Python生成

从这张图中可以看到在某个周日，男性用户购买了400多件产品，女性用户购买了350件产品。

作为数据分析师，对此你会提出一些可能的解释。明显的解释是，该产品在男性用户中更受欢迎。另一种是样本量太小，而这种差异是偶然的。还可能呢是由于某种原因，男性往往在周日才购买该产品。

为了理解哪种解释是正确的，你可以绘制另一个图。

<img src="https://img-blog.csdnimg.cn/direct/3c01fd976ebf447ebb6e958417b93f5b.png#pic_center" alt="在这里插入图片描述">

▲折线图1 - 用Python生成

不止看周日的数据，还要看到一周的数据。从这张图表中可以看出，在不同的日子里这种差异比较一致。

从这个分析中你会得出结论：这种产品在男性中比在女性中更受欢迎。

但如果你看到像这样的图表呢？

<img src="https://img-blog.csdnimg.cn/direct/23687e3585af4be884c15e6f85900524.png#pic_center" alt="在这里插入图片描述">

▲折线图2 - 用Python生成

那么，怎么解释周日的差异呢？

你可能会说，也许出于某种原因男性只在周日才会更多地购买这款产品。或许这只是巧合。

我在谷歌和微软工作时所做的数据分析工作与这个例子非常相似，只是更复杂一些。在谷歌时我使用Python进行分析，而我在微软使用JavaScript。

在这两家公司我都使用SQL从数据库中提取数据。然后，我用Python和Matplotlib(在谷歌)或JavaScript和D3.js(在微软)来可视化和分析这些数据。
1. 使用Python进行数据分析/可视化
进行数据可视化时，Matplotlib是非常热门的库。

Matplotlib很棒，因为：

容易上手

seaborn等库是基于它的，学习Matplotlib可以帮助你以后学习其他库。
1. 如何用Python学习数据分析/可视化
你首先应该了解数据分析和可视化的基础知识。在学习了数据分析和可视化的基础知识之后，学习统计学基础知识也将会很有帮助。

<img src="https://img-blog.csdnimg.cn/direct/1379d44e761a4f3fbb9ff2b2129ce563.png#pic_center" alt="在这里插入图片描述">

03 脚本

什么是脚本？

脚本通常是指编写能够自动执行简单任务的小程序。

我曾经在日本的一家小型创业公司工作，公司有邮件支持系统，这用来回复客户通过邮件发送给我们的问题。

在那儿工作时，我的任务是计算包含关键字的邮件数量，以便分析我们收到的电子邮件。这可以手动完成，但我写了一个简单的脚本来自动执行此任务。

当时我们使用了Ruby，但对于这类任务Python也是不错的选择。Python适合这类任务，因为它语法简单，易于编写，而且进行测试也很快。

04 其他用途
1. 嵌入式应用
我不是这方面的专家，但我知道Python可以与Rasberry Pi一起用，在硬件爱好者中很流行。
1. 游戏开发
你可以用PyGame来开发游戏，但这并不是最受欢迎的游戏引擎。你可以用它来开发业余爱好项目，但如果你对游戏开发很认真，建议不要选它。

我建议使用Unity的C＃，这是最受欢迎的游戏引擎之一。它能让你为许多平台开发游戏，包括Mac、Windows、iOS和Android。
1. 桌面应用
你可以用Python的Tkinter，但这并不是最热门的选择。Java，C＃和C ++等语言似乎更受欢迎。

最近，一些公司也开始使用JavaScript来开发桌面应用程序。例如，Slack的桌面应用是Electron构建的。它能让你用JavaScript构建桌面应用程序。

就个人而言，如果我要开发桌面应用，我会选择使用JavaScript。它能让你重新使用网络版本的一些代码。

当然，我并不是桌面应用的专家，所以如果你有不同的看法，评论中告诉我。

<img src="https://img-blog.csdnimg.cn/direct/0c65791063bd4597b8b5b7b4d8a49830.png#pic_center" alt="在这里插入图片描述">

4. Python 3还是Python 2

我会推荐Python 3，因为它更新而且更受欢迎。
1. 后端代码与前端代码的区别
假设你想开发类似Instagram的产品，那么你需要为想要支持类型的设备创建前端代码。

你可能会用到：

面向iOS端的Swift

面向Android的Java

面向Web浏览器的JavaScript

每组代码将在每种类型的设备上运行。这类代码将决定应用的布局样式，点击按键的样式等。

但是，您还需要存储用户信息和照片的功能。你要将它们存储在服务器上，而不仅仅存储在用户的设备上，以便每个用户的关注者都可以查看其照片。

这时需要用到后端代码/服务器端代码。你需要编写后端代码来执行以下操作：

记录关注情况

压缩照片，从而不占用太多存储空间

在发现功能中向每个用户推荐照片和新帐户

这是后端代码和前端代码之间的区别。

顺便说一下，Python不是编写后端代码的唯一选择，还有基于JavaScript的Node.js等选择。

**-END-**

<mark>**读者福利：如果大家对Python感兴趣，这套python学习资料一定对你有用**</mark>

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以根据这些资料规划好学习计划和方向。 


<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习、Python量化交易等习教程。带你从零基础系统性的学好Python！</mark>

## 零基础Python学习资源介绍

① Python所有方向的<mark>学习路线图</mark>，清楚各个方向要学什么东西

② 600多节<mark>Python课程视频</mark>，涵盖必备基础、爬虫和数据分析

③ 100多个<mark>Python实战案例</mark>，含50个超大型项目详解，学习不再是只会理论

④ 20款主流手游迫解 <mark>爬虫手游逆行迫解教程包</mark>

⑤ <mark>爬虫与反爬虫攻防</mark>教程包，含15个大型网站迫解

⑥ <mark>爬虫APP逆向实战</mark>教程包，含45项绝密技术详解

⑦ 超<mark>300本Python电子好书</mark>，从入门到高阶应有尽有

⑧ 华为出品独家<mark>Python漫画教程</mark>，手机也能学习

⑨ 历年互联网企业<mark>Python面试真题</mark>,复习时非常方便

<img src="https://img-blog.csdnimg.cn/7c1055f9bb6e41af9262556bdf20e084.png#pic_center" alt="在这里插入图片描述">

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取哈）**</mark> <img src="https://img-blog.csdnimg.cn/9f969354b48f4e3ab0253e89203deca2.png#pic_center" alt="在这里插入图片描述">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉实战案例👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/6cf364e7eeb64b0da07021bce5a59ec6.png#pic_center" alt="在这里插入图片描述">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

## 资料领取

<mark>上述这份完整版的Python全套学习资料已经上传网盘，朋友们如果需要可以微信扫描下方二维码输入“领取资料” 即可自动领取</mark> <font color="red" size="3"> **或者**</font> 【】领取
