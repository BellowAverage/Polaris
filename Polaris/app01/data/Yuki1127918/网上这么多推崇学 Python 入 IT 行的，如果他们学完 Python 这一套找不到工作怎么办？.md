
--- 
title:  网上这么多推崇学 Python 入 IT 行的，如果他们学完 Python 这一套找不到工作怎么办？ 
tags: []
categories: [] 

---
掌握一门技能，是需要花成本的。决策之前，做个前景判断，衡量投入产出比，是应该的。

然而，一旦深入思考，你可能自己就会对学 Python 的价值，颇为疑虑。

因为大部分人看待这个问题，是在判断 Python 学过后，能否提升自己的竞争力。

国人常说的俗谚，有一句“一招鲜，吃遍天”。也就是掌握了某种供不应求的技能，于是可以坐享这种技能带来的益处与红利。

你可以暂停阅读20秒钟，在头脑里，自行匹配满足上述条件的相应技能，或是代表该技能的证书。

想好后，咱们继续。

这样的技能，确实是存在。但是，要达到“吃遍天”的效果，需要你衡量市场上的供求关系。

我们都知道，近几年市场对 Python 的需求确实很高。许多岗位招聘条件里面，都有 Python 这一项。

<img src="https://img-blog.csdnimg.cn/c8a6025238564a62b658fa6fa11ed100.jpeg#pic_center" alt="在这里插入图片描述">

然而，供求关系的另一方，也就是供给，情况如何呢？

很不容乐观。

我不是说供给太少，而是太多了些。

别忘了， Python 最大的特点，就是简单易学。

因此，没有门槛，没有护城河，连上小学的孩子，课本上都要教 Python 了。

<img src="https://img-blog.csdnimg.cn/9104a8070b8444e3a19808e7c6e88561.jpeg#pic_center" alt="在这里插入图片描述">

需求再大，如果供给是这样的，价格也很难上去。

所以，如果你的打算，是学好 Python 以后，直接用它变现，那你一定要三思而后行。

这是不是说，你不该学 Python 呢？

恰恰相反，你真的应该学 Python 。

你可能会疑惑：老师，你这不是前后矛盾吗？

不是。

Python 要学，但这项技能，真的不是这么应用的。

### **连接**

Python 无门槛，这么简单，学会了也毫不稀奇，那学它还有什么用？

用处大了。

因为它可以让你和一张巨大的协作网络连接起来。这张网络的溢出效应，对你来说益处可谓巨大。

<img src="https://img-blog.csdnimg.cn/aa09433856fb4ba5a79223b0685e8ed9.jpeg#pic_center" alt="在这里插入图片描述">

举个例子。

机器学习听说过吧？最近很火的。

从前人们做机器学习，用的工具叫做 Matlab 。

直到6、7年前，当 Andrew Ng 制作后来成为经典的《机器学习》课程时，用的工具还是 Matlab 。

<img src="https://img-blog.csdnimg.cn/caab34fe97f043218e6d3994c8e3a2ab.jpeg#pic_center" alt="在这里插入图片描述">

当然，因为当时 Matlab 很贵，所以 Andrew Ng 鼓励大家用 Octave （一种 Matlab 的开源实现版本）替代。

我学这门课程的时候，很痛苦。其中最重要的原因，就是 Matlab / Octave 的使用。

这是当时做的第 8 次作业，你看看为了做个协同过滤（Collaborative Filtering），需要多少个文件。

<img src="https://img-blog.csdnimg.cn/e05e292edf514feea755fbd163e1d7b2.jpeg#pic_center" alt="在这里插入图片描述">

随便打开一个代码文件，是这样的：

<img src="https://img-blog.csdnimg.cn/e560c5204bd94bff995d4b59f93edff7.jpeg#pic_center" alt="在这里插入图片描述">

结果是，大部分学员，根本就不知道，该如何完整撰写一个协同过滤算法的程序。大家只能满足于课程的要求，即在每个文件指定的位置上，做完形填空。

因此，那时候你要是打算使用机器学习，就必须要抱着一本 Matlab 的书啃下来。因为只有明白了它怎么用，你才真正能壮起胆子，尝试从头到尾，去实践自己从 MOOC 学来的机器学习技能。

其他基于 Python 的机器学习课程，也像雨后春笋一般遍地开花。

例如在 fast.ai 的课程里，实现同样的协同过滤功能，你再也不用写那一堆 Matlab 文件和函数了。

你需要的，仅是以下这几行代码：

```
from fastai.collab import *
path = untar_data(URLs.ML_SAMPLE)
ratings = pd.read_csv(path/'ratings.csv')
ratings.head()
data = CollabDataBunch.from_df(ratings)
learn = collab_learner(data, n_factors=50, y_range=(0.,5.))
learn.fit_one_cycle(5, 5e-3, wd=0.1)


```

好了，搞定。

Python 没有门槛。但是通过掌握它，你可以用更短的时间，更高的效率学习和掌握机器学习，甚至是深度学习的技能。

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
