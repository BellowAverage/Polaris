
--- 
title:  半年的心血，《PyCharm中文指南》 v2.0 版本，可以发布了 
tags: []
categories: [] 

---
大家好，我是明哥。

去年 9 月份，我花了两个月的时间，整理发布了第一版的 《PyCharm 中文指南》，初衷是为了帮助那些刚入门 Python，却被 PyCharm 这个庞然大物被劝退的同学们，如何利用 PyCharm 去提高编码效率，应该可以算当下第一本系统介绍 PyCharm 使用技巧的中文电子书。

为了更好的向各位读者展示 PyCharm 使用技巧，在原博客里，录制了近百张的 GIF 动态图，但是在导出为 PDF 后，动态图会自动转成静态图（由动态图转成静态图的，在书中我有标注出来），因此我建议在有条件的情况下，尽量去原博客（http://pycharm.iswbm.com） 进行学习。

**本书的内容非常地多，在完全不包含代码的情况下，文字就已经达到 6万多，PDF文档有 200 多页**，因为它面向的是所有的 Python 开发者，而不仅仅适用于 Python 新手，我相信即使你使用 PyCharm 有一些年头了，在本书中，依然能习得不少高效的使用技巧。

### 新版说明

当前你看到的手册版本为 2.0，这个新的版本，增加了数据库操作的章节，并且补充完善了一些其他章节的内容，解决了 Github 上一些朋友提出的 issue。

但仅是这些改动，其实还不足以让这本手册直接从之前的 1.1 跨到 2.0 版本。

在之前 1.0 和 1.1 的版本中，由于大部分内容是基于 Mac 操作系统下进行编写的，因此有很多用 Windows 的朋友提出了建议，看能不能把不同系统的快捷键都标注上？

为了满足这些朋友的需要，我花了一点时间，整理出当前你所看到的2.0 版手册。

<img src="https://img-blog.csdnimg.cn/img_convert/b7fc830e590950939fd74a6785f94df4.png" alt="">

2.0 版本最大的改动是，我将原手册拆分为 Windows 和 Mac 两版本的

使用 Windows 的朋友可以看 Windows 版本的：http://pycharm.iswbm.com/zh_CN/win/

<img src="https://img-blog.csdnimg.cn/img_convert/27b9e7a19096259d61fbd400cd96621d.png" alt="">

使用 Mac 的朋友可以看 Mac 版本的：http://pycharm.iswbm.com/zh_CN/mac/

<img src="https://img-blog.csdnimg.cn/img_convert/1ca2773f6f805e99ea12a3a9ccfa9597.png" alt="">

文档中的快捷键已经全部适配各自的系统，但是截图及 GIF ，出于工作量的考虑，没有再重新录制，并且我认为重新截图和录制 GIF 不是很有必要，同一版本的 PyCharm 的 Mac 和 Windows 界面的可以说差异不大，不会影响你学习该文档。

### 文档内容

#### 第一章：下载与安装

这一章的内容，比较基础，介绍了
- 多个版本之间的区别？- 是否有必要使用专业版？- 使用专业版的五种方法- 如何免费且正当的使用专业版？- 如何获得永久免破解(永不失效)的专业版？
<img src="https://img-blog.csdnimg.cn/img_convert/97204efe8aea3fc0c528aecd1840d4ac.png" alt="">

#### 第二章：调试与运行

第一章安装好后，第二章就直奔主题，学习配置 Python 环境，然后开始学习如何运行和调试程序。

这一章里，我盘点了在 PyCharm 中执行 Python 代码所有方法：
- 快捷键及右键运行代码- main 函数入口执行程序- 有参数的情况下运行程序
单单会运行代码，还远远不够，开发 + 调试，是必备技能，我整理了多种调试技巧
- 对所有调试的按钮进行详细的图解- 程序运行出错如何自动进入调试模式- 远程调试环境的搭建- 如何搭建搭建一劳永逸的开发环境
<img src="https://img-blog.csdnimg.cn/img_convert/42da0fe51e3f84af996ece23ab82ecfa.png" alt="">

#### 第三章：界面与排版

PyCharm 默认的主题及代码高亮配色实在不忍直视，想要看得舒服，下面每个要素都很重要：
- 合适的字体及其大小- 合适的背景色或背景图- 合适的代码高亮配色
不如跟着这一章节来把 PyCharm 配置成你最喜欢的样子，眼睛看着舒服，没有那么疲劳，效率自然就上去了

<img src="https://img-blog.csdnimg.cn/img_convert/43865f6a5169227c37f328473195976e.png" alt="">

#### 第四章：代码的编辑

做为一个 IDE ，代码的编辑是最基本的功能了，除了一些大家熟知的代码自动补全，PyCharm 基本还有一些更加高级的玩法，比如：
- 如何快速的实现父类方法的重写- 如何快速的实现接口方法- 如何实现变量的大小写转换- 如何实现代码的随处折叠- 如何查看函数的签名？- 如何查看上下文信息？- 如何在当前标签页中预览模块文档？
本章将一一为你介绍

<img src="https://img-blog.csdnimg.cn/img_convert/724cd361d6b1ce213c9ef3a7b229c700.png" alt="">

#### 第五章：快捷与效率

我们使用 IDE 的诉求，就是要提高编码的效率，PyCharm 带给我们的不仅仅只是代码提示与补全，在上一章节里，我就罗列了一些写代码时常用的编辑技巧。

不过与第四章不同的是，这一章节更加注重 **效率** 二字，都是我根据平时的使用习惯积累的高效技巧，如果不刻意去学习配置，有的是挺难发现的，比如：
- 如何录制宏，把多次重复的步骤封装成快捷指令？- 如何使用收藏夹，收藏框架的关键代码位？- 如何使用代码模板，提高编码的效率？- 如何快速、准确无误的重构框架代码？- 如何快速选择代码块？
这些技巧一旦熟练掌握了，效率和编码体验的提升，一定会上一个台阶。

<img src="https://img-blog.csdnimg.cn/img_convert/162af59f4d0095274776610e6c5c0001.png" alt="">

#### 第六章：搜索与导航

提及 Python 编辑器时，很多人会拿 VS Code 来和 PyCharm 进行对比，觉得 VS Code 是宇宙第一编辑器，如果把话题中"Python 编辑器" 的 Python 去掉，我还能接受，可如果加上了 Python ，我不敢苟同。

就单单阅读框架源代码这一需求，我相信 VSCode 是 打不赢 PyCharm 的。

如果平时有框架源代码阅读需求的同学，这一章节可千万别错过了，在我看来，这一章是本书最为灵魂的一个章节了，熟练掌握各种姿势的代码检索、导航功能，会让你在看代码时如鱼得水。

这一节里的内容全部都是精华，好好的阅读本章内容，相信你会回来给我点赞的。

<img src="https://img-blog.csdnimg.cn/img_convert/feaa4db9a54ac70e0c1dc1d7b3165b59.png" alt="">

#### 第七章：版本与管理

正规的项目代码，通常是版本控制系统的，PyCharm 支持最主流的各种版本控制系统 `Git` ，有了 PyCharm 后，其实你完全没有必要再去下载其他第三方的 Git 可视化管理软件。

考虑到这一章要是只讲 Git，那么内容可能不会很多，所幸的是，PyCharm 可以搭配 Git 这一分布式版本控制系统外，自己本身就拥有非常多的本地版本管理的功能，这些功能用好了都非常的实用。

<img src="https://img-blog.csdnimg.cn/img_convert/faa5f739faf8cee4d18d2ac5e62233ff.png" alt="">

#### 第八章：插件与工具

纵观整个软件圈，那些开放接口、支持第三方自定义插件的应用，哪一个不是NB的存在，比如 Chrome，VSCode

PyCharm 自然也不例外，它有自己的插件商店，上面有非常多实用的插件，安装一下就能使用，还有一些民间的插件，无法上商店的（比如大家熟知的破解插件），你也可以直接拖动进行安装。

本章除了介绍我日常的必备插件之外 ，还会附带介绍 PyCharm 自带的开发辅助工具，正是有了这些插件和工具的存在，让 PyCharm 在众多编辑器可以 以一打十，还一点都不虚。

<img src="https://img-blog.csdnimg.cn/img_convert/632a56718cebe8c5e670c95ff5e70410.png" alt="">

#### 第九章：常用的技巧

这一章也是一些使用技巧的总结 ，但是太细了，又不好分类，就全部放在这里。

<img src="https://img-blog.csdnimg.cn/img_convert/4412869c6350ada1a19246780f77a27d.png" alt="">

#### 第十章：操作数据库

这章在原来的版本中是没有，后来看到有朋友在 Github上提了 issue，希望增加操作数据库方面的内容，因此这个版本中把数据库这部分也补上了。

PyCharm 支持连接市面上绝大多数的数据库，MySQL、Mongo，SQLite 等等，有很多还是我没有见过的数据库类型。

本章以 MySQL 为例进行讲解，使用体验下来，感觉查询结果的导出可以说是一大亮点，可以转为几乎你可以想到的所有格式：csv, xlsx, json, html , xml , sql ,markdown 等等非常多的格式。

<img src="https://img-blog.csdnimg.cn/img_convert/3009aa864cf695b9b09a65755384cbb6.png" alt="">

### 如何获取

**文档本身完全公开免费，如果文档对你有用，还请点个赞 + 喜欢，你的这份支持与认可对我挺重要的**

Mac 版《PyCharm中文指南 v2.0》：https://wws.lanzous.com/iJPIvner86d

Win 版《PyCharm中文指南 v2.0》：https://wws.lanzous.com/iG3yfner8uh

### 写在结尾

我尽力让该文档全面、详细、易懂，也请大家帮我宣传一下，多一个人学习到该文档，我单位时间产出的价值就多一分。

同时大家如果对该文档有任何建议，都欢迎大家去 github (https://github.com/iswbm/pycharm-guide) 上提 issue，任何能提高文档质量的建议我都虚心接纳。

如果该文档，对你学习 PyCharm 有帮助，还请帮忙在 github 点个 star，你的这份认可对我很重要。
