
--- 
title:  AI入门篇||一文掌握 包 conda Anaconda Mniconda pip Repo python 概念区别联系，发行版镜像链接 
tags: []
categories: [] 

---
## AI入门篇||一文掌握 包 conda Anaconda Mniconda pip Repo python 概念区别联系，发行版镜像链接

<img src="https://img-blog.csdnimg.cn/05eb278701e9401e9f11f149d8dd3098.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biF5bS9eg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="Conda &amp; Anaconda &amp; Miniconda "> ****画完这个图发现这个图并不确切** **

聪明人已经看出来了，conda的儿子又包含conda

conda不是分为Anaconda和Miniconda,而是表达一种优先级，conda是包管理工具，而Aniconda和miniconda是软件发行版：
- 软件发行版是在系统上提前编译和配置好的软件包集合， 装好了后就可以直接用。- 包管理器是自动化软件安装，更新，卸载的一种工具。- Conda，有命令”conda install”, “conda update”, “conda remove”, 所以很明显，conda是包管理器。
Anaconda是python的发行版，内置了众多 Python 包和附加软件（pydata 生态圈里的软件），所以肯定要内置conda进行包管理

### 什么是包？

包（Package）其实就是一个软件集合，安装完包之后，我们就可以使用包里的软件了。Windows上缺少包的概念，类Unix系统一般使用包管理软件（Package Manager）来管理和安装软件，我们在手机上常用的应用商店其实就是一个包管理软件。

### 什么是Repo？

包管理仓库:软件发布者将编译好的软件发布到包管理仓库（Repository，简称Repo），用户通过包管理软件来下载和安装，只不过类Unix系统一般使用命令行来安装这些软件。 常见的包管理有： 在操作系统上安装软件：Ubuntu的apt、CentOS的yum、macOS的homebrew 在编程语言中安装别人开发的库：Python的pip、Ruby的Gem 包管理软件有对应的Repo：pip的PyPI，conda的http://Anaconda.org、R的CRAN

### 什么是conda?

Conda 是一个开源的软件包管理系统和环境管理系统，用于安装多个版本的软件包及其依赖关系，并在它们之间轻松切换。

### 什么是Anaconda?

Anaconda（官方网站）就是可以便捷获取包且对包能够进行管理，同时对环境可以统一管理的发行版本。Anaconda包含了conda、Python在内的180+个科学包及其依赖项 具体由什么包和依赖项呢？百度百科列出来了 

### 什么是Miniconda？

Miniconda是一个免费的conda最小安装程序。它是Anaconda的一个小型引导版本，只包括conda、Python、它们所依赖的包，以及少量其他有用的包，包括pip、zlib和其他一些包。

### pip和conda区别和联系

**联系**：都是用来加载包的

|区别|conda|pip|所以
|------
|安装的包|它从http://Anaconda.org上拉取数据。Anaconda上有一些主流Python包，但在数量级上明显少于PyPI，缺少一些小众的包。|从PyPI（Python Package Index）上拉取数据，或者说它的Repo在PyPI上。绝大多数的Python包会优先发布到PyPI上|这一点不代表conda包包含pip下载的包
||(其中大部分是python包|只支持python|如果其他语言写的包类似C/C++、R 只能用conda
|编译|编译好的二进制包|源码和二进制|所以pip需要编译器支持，如果没有某个编译器可能不能用;所以conda包大
|环境依赖|检查当前环境下所有包之前的依赖关系|不检查|conda更加严格，conda安装后基本能用，但可能pip安装后不work
|优点|是一个环境管理工具，可以创建环境，进行环境隔离,pip几乎只是一个安装包的软件|pip快，包小，开发者使用可以了解包之间的依赖，避免成为一个无情的调包侠|所以老实人还是conda吧

### conda和python的关系

没什么必然关系，反倒是Anaconda和conda关系比较大

还有什么疑问可以看这个个人网站（应该是个个人网站，写的很好,关于这方面的一些误解解释的很清楚，羡慕.jpg）



### Anaconda || Miniconda下载

流程得话可以参照其他人的博客什么的下载一遍，建议自己先在一个旧电脑上或者别人的电脑上 (滑稽.jpg）探索，把所有问题都解决了再重新下载一遍在常用电脑上。

****强烈不建议conda和pip混着用，那virtualenv和conda创建虚拟环境没用啊，根据需求选，隔离python运行环境,否则可能会出现好几个长得一样的包存在不知道用哪个，或者存在冲突****

#### 镜像：

 2020-06-14 update: 为了分担清华源镜像的压力，最近北京外国语大学也开启了镜像站点，同样是由清华TUNA团队维护的，如果有小伙伴遇到清华源速度很慢的情况的话，可以考虑换成北外的镜像。 新闻传送门： 镜像传送门： 2020-08-05 update: 为了方便大家(当然主要是自己偷懒用), 把北外的链接也给写出来, 这样就可以直接复制粘贴了~当然两者取其一就可以了, 不用重复添加. 另外, 查看了中科大的镜像, 点击这个地址会直接跳转到清华tuna的镜像站点. 所以目前看起来国内是只有清华和北外两个镜像站点可用了

### 目前国内提供conda镜像的大学

清华大学:  北京外国语大学:  南京邮电大学:  南京大学:  重庆邮电大学:  上海交通大学:  哈尔滨工业大学: 

参照原文链接： [https://blog.csdn.net/weixin_28665677/article/details/112138703] [https://www.jianshu.com/p/edaa744ea47d] [https://www.zhihu.com/question/395145313/answer/1230725052] [https://www.zhihu.com/question/395145313/answer/1257660174] [https://blog.csdn.net/sigmarising/article/details/88774548]
