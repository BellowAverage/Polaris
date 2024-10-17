
--- 
title:  搭建 Python 高效开发环境： Pycharm + Anaconda 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/4fc6ec37a621f8bd903429b08d84029a.gif">

介绍

先来介绍下两位主角：

**Pycharm**：目前一款主流的 Python 集成开发环境，它带有一整套帮助我们在Python开发时提高效率的工具，比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制。

总的来说，Pycharm 会极大地提高我们 Python 开发的效率和体验，用过都说好。

**Anaconda**：主要针对 Python 的数据科学整合包，包括有 Numpy，Pandas，Sklearn等。重要的是，自带管理软件 conda，它拥有安装，更新，删除，解决包依赖关系的包管理功能。同时，conda拥有环境管理功能，能创建独立运行环境， 使各项目间包环境和版本互不冲突和影响。另外，Conda 还可以管理包括 Bowtie2，FastQC 等软件环境，甚至 R 包环境。

总之，Anaconda 就是我们在编程时的管家，一切麻烦事扔给他，我们只要关注项目本身就行。

<img src="https://img-blog.csdnimg.cn/img_convert/3c1040db7abe26fc2ab6e6e5efd87b6d.gif">

安装 Pycharm

1.网址：https://www.jetbrains.com/pycharm/download/#p=windows
- Professional：收费，专业版会提供扩展，比如远程调试，插件支持，版本控制等- Community：免费，会包含常用的基础功能
这里选择专业版为例，可以先试用30天。有的学校会购买，可以咨询下学校图书馆或计算机学院。也可以去官网购买，当然网上有许多方法可以获得，自行搜索。

<img src="https://img-blog.csdnimg.cn/img_convert/75c115eead87d0c7b984615a46f67344.png">

2.开始安装

<img src="https://img-blog.csdnimg.cn/img_convert/a30b50c914600cebe4664441d4d402d5.png">

3.选择安装位置，Next

>  
  如果有固态硬盘，可以把 Pycharm 放进去，这样会极大的减少项目构建索引，载入导入时间。 
 

<img src="https://img-blog.csdnimg.cn/img_convert/6534fb0cd2c682fa23ddd0c903159917.png">

4.可以根据需要来选择配置，建议全选

<img src="https://img-blog.csdnimg.cn/img_convert/1959536e4d4710b10ef7286341dd09e9.png">

5.安装

<img src="https://img-blog.csdnimg.cn/img_convert/30851ef7e603b6e260cbbbc2b568d927.png">

6.安装完成后，点击刚刚在桌面上的快捷方式

<img src="https://img-blog.csdnimg.cn/img_convert/c0012a95b76a73fe9d7b513a269dfebd.png">

7.同意协议

<img src="https://img-blog.csdnimg.cn/img_convert/afff6c0eb6862c4461fdcc5aca34757a.png">

8.数据是否分享，根据情况来看

<img src="https://img-blog.csdnimg.cn/img_convert/5afaab4db1a0c0f9c52b6fa3c04ef3d5.png">

9.选择主题，我这里选择浅色

<img src="https://img-blog.csdnimg.cn/img_convert/34391a4a4523332ee257011b5eb729e6.png">

10.根据需要安装插件
- IdeaVim：vim是Linux系统常用的编辑器，如果之前已经习惯用vim，可以安装- R：统计学编程语言，因为学习生物信息的原因，这里选择安装- AWS Tookit：是亚马逊云服务的扩增
<img src="https://img-blog.csdnimg.cn/img_convert/04c44a4f7f577577bdadd04fa1ce011f.png">

11.激活

因为这里安装的是专业版，可以先选择试用。点击`Evaluate`

<img src="https://img-blog.csdnimg.cn/img_convert/faf0d709f111c2593d02b994458e1933.png">

<img src="https://img-blog.csdnimg.cn/img_convert/bc0cf2316202b3b08f2396dc522e4789.gif">

安装 Anaconda

1.根据系统选择合适的安装包，这里建议选择 Python 3.7 版本下载

https://www.anaconda.com/products/individual#Downloads

<img src="https://img-blog.csdnimg.cn/img_convert/bde25f5d5b0f7c71d38f2fbf8c06f89f.png">

2.安装

<img src="https://img-blog.csdnimg.cn/img_convert/5521d9c084a7ce3fe3f19ddd4908b017.png">

2.同意协议

<img src="https://img-blog.csdnimg.cn/img_convert/7d739329418e835b362abe4611b3bc90.png">

3.Next

<img src="https://img-blog.csdnimg.cn/img_convert/0c2288d14cb6d8b14ba048d594b7111e.png">

4.选择安装路径

这里路径最后放在非系统盘，后续anaconda的操作会占用硬盘空间

我平时会为每种语言建立独立的安装目录，工作目录。这样的好处是在版本更新，和项目依赖关系清晰，后续更新也方便。

<img src="https://img-blog.csdnimg.cn/img_convert/edaf17b7cd4c690dd4a51ba2c26f8a1b.png">

4.开始安装

<img src="https://img-blog.csdnimg.cn/img_convert/6fa7da400df48bc0c68677373a1e9c89.png">

5.Next

<img src="https://img-blog.csdnimg.cn/img_convert/a12416b2b25d97af352f7ff45d4acce9.png">

6.Next

<img src="https://img-blog.csdnimg.cn/img_convert/2fee29debc88573895eb8fee6c0d051d.png">

7.安装完成

<img src="https://img-blog.csdnimg.cn/img_convert/11774ca990fe7f89fc7d3415238e3fde.png">

<img src="https://img-blog.csdnimg.cn/img_convert/ea5184ab1a54c703951b07c81bf0f384.gif">

新建包含 Anaconda 的项目

1.第一次进入Pycharm，先新建项目，进入配置界面

<img src="https://img-blog.csdnimg.cn/img_convert/5248fa7234bc6faa1fb5afd105e5e8a6.png">

2.配置 Python 解释器

<img src="https://img-blog.csdnimg.cn/img_convert/992795ad2110a91f4313780095f380d7.png">

为了方便管理，这里 `Location` 配置项目存放目录，该目录与 Anaconda 在同一目录下。当然，不按照这样的目录结构也可以。

<img src="https://img-blog.csdnimg.cn/img_convert/d96d90af3ab6fa8c156966d235e3740f.png">

3.切换到 `Conda Environment` ，找到我们刚刚安装 Anaconda 的目录并设置，同时勾选为所有项目应用该配置

<img src="https://img-blog.csdnimg.cn/img_convert/f88012c883b8806241ec6e85ab531668.png">

4.配置完成后，解释器被 Pycharm 识别，点击创建

<img src="https://img-blog.csdnimg.cn/img_convert/b107936622cc1e3b77fc0917b1fc3bd8.png">

5.第一次创建项目，Pycharm 有初始化工作要做，耐心等待即可

<img src="https://img-blog.csdnimg.cn/img_convert/a6399e46bb4c9f415f8cf9bb6d7050e4.png">

#### Anaconda 环境的使用示例

0.工作区介绍

<img src="https://img-blog.csdnimg.cn/img_convert/3feb5da28e63817b1b893624651b3727.png">

1.右键项目名，新建 Python 脚本

<img src="https://img-blog.csdnimg.cn/img_convert/8991f3c4c7ad165d7bdc2e6486386947.png">

2.输入名字，注意这里不需要添加 `.py`后缀，回车后创建

<img src="https://img-blog.csdnimg.cn/img_convert/fdcf26a03909f99a06693f4f87984c29.png">

3.编写脚本

<img src="https://img-blog.csdnimg.cn/img_convert/3b2fbff54ce0bcb54515e41b05ec20ab.png">

4.右键脚本名，运行，测试配置是否成功

<img src="https://img-blog.csdnimg.cn/img_convert/df08427963919d5382b09246b9667748.png">

5.运行这个脚本，会自动激活`Scientific Mode`，界面就像这样：

在左下输入`df.head()`，可以直接在控制台查看数据框内容，也可以在右边点击查看。

<img src="https://img-blog.csdnimg.cn/img_convert/413584fc459cb78b523e97921fcae213.png">

<img src="https://img-blog.csdnimg.cn/img_convert/85ec485893cc210874f736f33dea053d.gif">

Conda 环境的使用示例

有了 Anaconda 的支持，为什么还要 Conda 环境？

前面新建的 Anaconda 环境包含各种数据分析，机器学习等包，可以直接拿来用，并不需要再安装一遍，方便实用。

<img src="https://img-blog.csdnimg.cn/img_convert/5dd4f2ce893c87b6c034f913a20d2696.png">

但是，有时候，我们并不需要这么多的包，而是需要特定版本的 Python 或者 Python 包，或是依赖冲突等问题，这就要求有一个独立运行的环境。而 Conda 建立的环境正好满足了这个需求。

1.新建包含有 Conda 环境的项目

<img src="https://img-blog.csdnimg.cn/img_convert/f3e9e98dcb2b080e2639b3cae9256ac6.png">

2.查看启用的环境

点击 Pycharm 下面的 `Termianl` 可以直接控制 Windows 的 CMD 命令行（这里不得不吐槽微软的 CMD 和 PowerShell 界面丑还超难用）。如果你的 Pycharm 运行在 Linux 下，这个工具会接管 Shell。

可以看到在最前面多了一个 `(example)` ，这个代表激活的 conda 环境

<img src="https://img-blog.csdnimg.cn/img_convert/c3f7dcb4af858dfcb0642aa3861c7d20.png">

3.查看 conda 环境里有哪些包

输入命令 `conda list`，可以查看我们建立的环境里包含哪些包。

>  
  学习更多 conda 的包管理，环境管理和渠道管理等技巧可以参考： 
  https://blog.csdn.net/u011262253/article/details/88828229 
 

可以看到，相对 Anaconda 整合了数以百计的包不同，这里只有几个最基础的 Python 包，之后按需添加即可。

<img src="https://img-blog.csdnimg.cn/img_convert/c86a2c809c16630f13f1f8e7107aa3dd.png">

4.切换环境

点击右下角的 conda 环境名，可以切换环境。

这里切换后，代表我们项目目录中所有的脚本都要依赖于这个环境。

<img src="https://img-blog.csdnimg.cn/img_convert/ad73a37f77c2e38588a970fe3cbfce54.png">

但是，需要注意，一些老鸟已经会熟练操作 Conda 了，比如像下面这样来切换环境：

<img src="https://img-blog.csdnimg.cn/img_convert/f538718173f2d3782295ac8dd2ea100c.png">

不幸的是，虽然命令行`conda activate base` 可以将当前环境 `example` 切换为 `base`，但是这里只是将命令行的环境切换了，我们 Pycharm 项目的 conda 环境纹丝不动。

所以想切换当前项目的环境，最好点击右下角图标

5.使用 Conda 环境

这里以绘制一张热图为例来简单使用下配置好的环境

安装`matplotlib`包

<img src="https://img-blog.csdnimg.cn/img_convert/a113767aad611599c315314719abcb9b.png">

写代码

<img src="https://img-blog.csdnimg.cn/img_convert/b43c18c272e7288a7ffa025fd81591a4.png">

出图

<img src="https://img-blog.csdnimg.cn/img_convert/40d5454cb54796ee41d5d622aadda6c4.png">

这里同样也可以激活`Scientific Mode`，可以这么来设置

<img src="https://img-blog.csdnimg.cn/img_convert/d79c9aa6144ce301f47990d118f5279e.png">

效果是这样的：

<img src="https://img-blog.csdnimg.cn/img_convert/ae3a91a068264e6bfba1128da3934bec.png">

往期推荐


