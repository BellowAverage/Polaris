
--- 
title:  Python的哪个Web框架学习周期短，学习成本低？ 
tags: []
categories: [] 

---
不用学前端编程，你就能用 Python 简单高效写出漂亮的交互式 Web 应用，将你的数据分析成果立即展示给团队和客户。

<img src="https://img-blog.csdnimg.cn/d78b5fc006e84210be22a76e2b1b6e6e.jpeg#pic_center" alt="在这里插入图片描述">

### **痛点**

从我开始折腾数据分析工具的那一天，就没有想明白一件事儿 —— 我打算把数据分析的成果做成一个 Web 应用，为什么这么难？

我需要的核心功能，无非是在网页上接收用户输入，然后做分析处理，把分析结果反馈给用户，完事儿。

可是这谈何容易？

很多人都会微笑着告诉你，想做 Web 应用？这得学前端编程， HTML + Javascript 了解一下吧！

什么？你还需要在后台做数据分析？那你就得学 Web 框架了。

你说喜欢 Python ？那就学个 Django 或者 Flask 好了。

真正让我痛苦的，不是 Web 框架的操作有多么琐碎，而是教程里的**案例**，为什么都那么奇怪？

几乎所有的教程，都指向一个目标：

>  
 来，我教你做一个 blog 出来！ 


<img src="https://img-blog.csdnimg.cn/772ad8ae9c11403db435ee526ab7b6bc.jpeg#pic_center" alt="在这里插入图片描述">

我用你教？！

我要是想用 blog ，可以直接注册一个免费的啊！为什么我要自己开发个 blog 出来？

为什么你就不能告诉我，该怎么把我目前的数据分析结果，迅速挪到 Web 页面上，跟用户实时交互？

虽然二者的结果，都是做一个 Web 应用出来。但是，它们关注的焦点，需要的功能，能一样吗？

但是人家写书和做教程的人，就是不疾不徐，**坚持一定要**教会你，如何做一个 blog 出来……

你不学，又能怎么办呢？你难道想只凭 Python 脚本，就做一个 Web 应用出来？

还真别说，最近，这个事儿从幻想，**变成了现实**。

### **样例**

这不，我就用纯 Python 脚本写了个 Web 应用。

我编写的代码里，没有一丝半毫的 Web 框架，Javascript，甚至是 HTML 。

这玩意儿能用吗？

你自己来试试看。

请你打开浏览器，输入以下链接：

https://helloworld-streamlit.herokuapp.com/

你会看到下面的初始化界面。

<img src="https://img-blog.csdnimg.cn/ddc987d59c2e4485be2efb3dca30a604.jpeg#pic_center" alt="在这里插入图片描述">

初始化完毕之后，页面会分成左右两栏。左面是两个下拉候选框，分别让你指定需要分析的数据范围。

<img src="https://img-blog.csdnimg.cn/0256f4be18ef42f9978539148d13b2ec.jpeg#pic_center" alt="在这里插入图片描述">

上面一个，是事件类型；

<img src="https://img-blog.csdnimg.cn/9da0621f09504a51b7bbb87927f41aae.jpeg#pic_center" alt="在这里插入图片描述">

下面一个，是事件发生归属地。

<img src="https://img-blog.csdnimg.cn/8db7a82c83ff4bc682687eb49f7ddb9f.jpeg#pic_center" alt="在这里插入图片描述">

只不过，当时我们更注重的，是用循环神经网络搭建了一个严重拥堵事件预测模型。

<img src="https://img-blog.csdnimg.cn/6b80b39616994792875df0932951e282.jpeg#pic_center" alt="在这里插入图片描述">

而今天，我们是要进行探索性数据分析，也就是根据我们感兴趣的目标，对数据进行整理操作，然后可视化显示。

<img src="https://img-blog.csdnimg.cn/616a2eae95e84fec91167cb9f3a12721.jpeg#pic_center" alt="在这里插入图片描述">

选定之后，你会看到右侧提示两个信息：
- 你筛选之后，数据框包含行数；- 在层叠地图上的可视化结果。
<img src="https://img-blog.csdnimg.cn/081b124342bb4dfe9735127bd29c4b09.jpeg#pic_center" alt="在这里插入图片描述">

怎么样？

麻雀虽小，五脏俱全。

虽然咱们这个 Web 应用很简单，不过交互分析该有的功能和流程，基本上都涵盖了。

你可能会问：

>  
 王老师，编这么一个应用出来，不简单吧？ 


让我带你到幕后，看看是不是很复杂。

### **幕后**

我把这个应用的全部源代码，都为你存储到了 Github 上。

<img src="https://img-blog.csdnimg.cn/15a933f3d724418fbf2e40c796db1ad2.jpeg#pic_center" alt="在这里插入图片描述">

可以看到，一共包含了 4 个文件。

有意思的是，其中 3 个，包括：
- Procfile- setup.sh- requirements.txt
都只是部署到远程服务器时，需要用到的配置文件而已。

也就是说，只有最后一个 helloworld.py 是主角，它包含了实现咱们**全部交互式数据分析功能**的 Python 脚本文件。

这代码，少说也得有几百行吧？

别担心，打开来看看：

<img src="https://img-blog.csdnimg.cn/785177d31e284bc69049ae981532d805.jpeg#pic_center" alt="在这里插入图片描述">

上面这张截图，就已经包含了实现交互数据分析功能的**全部代码**。

神奇吧？

### **解读**

这么短的代码，为什么能有如此强大的功能？

这是因为它背后使用的一个软件包，叫做 streamlit 。

<img src="https://img-blog.csdnimg.cn/5cbf0e5fe24f44b8893ea3d85a491d73.jpeg#pic_center" alt="在这里插入图片描述">

它是干什么用的？

一言以蔽之，给你赋能，让你能够不去操心什么前端后端。只写 Python ，只关注功能，你就能写出一个交互式 Web 应用出来。

当然，既然最后是 Web 应用，那么实际上前后端的功能都是齐备的。

只不过，这些交由 Streamlit 来帮你费心操办。你根本不用管。

### **爆发**

为什么会有人做了这么一款神器出来？

原因很简单，咱们前面提到的痛点，是大伙儿都有的。

咱们这些麻瓜（Muggle），遇到痛点只能忍着。

但是真正的魔法师（优秀程序员），是忍不了的。

<img src="https://img-blog.csdnimg.cn/e1914d98a2ea486facbfb91ee98ea4c1.jpeg#pic_center" alt="在这里插入图片描述">

在这段来自 PyData LA 2019 的视频里，Streamlit 的 CEO Adrien Treuille 谈及了他在数据智能企业中，长期遭遇的痛点。

最大的痛点，就是数据科学家训练好机器学习模型后，需要验证效果，和用户反馈沟通。

但是，做机器学习的工程师本身，并不掌握这一整套的工具栈。

<img src="https://img-blog.csdnimg.cn/46f5850963344a549f727c6bdd11c466.jpeg#pic_center" alt="在这里插入图片描述">

所以，就得在把全部的数据分析和模型训练工作完成后，把这东西移交给一个**工具制作团队**。

<img src="https://img-blog.csdnimg.cn/887585a5fc4e41edbe6014f8eeb1c78c.jpeg#pic_center" alt="在这里插入图片描述">

人家做完以后，就告诉数据科学团队说，做好了。但是注意，现在处于需求**冻结**阶段。这个应用你们可以随便用，**只是别乱改**。改坏了我们管不了。因为最近两个月，我们还得给其他若干数据分析团队做 app 。大概**几个月以后**，我们又能回来帮助你们了……

Adrien Treuille 很敏锐地捕捉到了这个长期痛点，于是在 2018 年， 创立了 streamlit 。

目标很简单，给数据科学团队提供简单的工具，让他们使用已经掌握的 Python 编程技能，就能直接做 Web 应用。

什么 “等上两三个月不许改”？！你们自己慢慢儿玩儿去吧，我们想怎么改，就怎么改！

至于做出来的东西嘛，可以是这样的：

<img src="https://img-blog.csdnimg.cn/img_convert/851e5aa625181a09a347935edce54018.jpeg" alt="">

### **思考**

尝试过之后，你应该不难发现，Streamlit 给你带来了什么。

如果你学过 Javascript 和 Flask, Django 等 Web 应用开发技术，Streamlit 可以加快你的 Web 应用开发与测试进程。

如果你还没有学过上述技术， Streamlit 可以给你**赋能**，让你一下子有了把数据分析结果**变成产品**的能力。

给你讲点儿更激进的。

有人已经希望能用它替代掉 Flask 用于产品发布了。

<img src="https://img-blog.csdnimg.cn/0bdcdb8b6c6c496aaae785bb78afe85a.jpeg#pic_center" alt="在这里插入图片描述">

还有人说，将来写技术文档，也应该充分使用 Streamlit 。

<img src="https://img-blog.csdnimg.cn/97d99e9cbaf0440a98c7661466a751a9.jpeg#pic_center" alt="在这里插入图片描述">

甚至，还把它比作了数据科学界的 iPhone 。

<img src="https://img-blog.csdnimg.cn/c6297256d2bb488b9d0db624cc9433cd.jpeg#pic_center" alt="在这里插入图片描述">

这里，它是借喻 iPhone 开启智能手机时代，说明 Streamlit 的**划时代性**。

我**不希望**你也变得如此激进。

当然，如果你不希望精通写作技艺，只是想做一个抄书匠糊口。那么印刷术就可能会替代你的工作，结果就不那么美妙了。

### 关于Python技术储备

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以找到适合自己的学习方案 


包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习等习教程。带你从零基础系统性的学好Python！

## 零基础Python学习资源介绍

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。**（全套教程文末领取哈）** <img src="https://img-blog.csdnimg.cn/img_convert/673b13641cf2ddf5e18b5c58afd50200.png#pic_center" alt="">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

###### 这份完整版的Python全套学习资料已经上传CSDN，朋友们如果需要可以微信扫描下方CSDN官方认证二维码免费领取【`保证100%免费`】

<img src="https://img-blog.csdnimg.cn/1d2a69f2d57e4d1cb444037b17af8607.png" alt="">
