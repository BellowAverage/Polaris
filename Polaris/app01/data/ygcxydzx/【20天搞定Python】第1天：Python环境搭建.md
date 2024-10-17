
--- 
title:  【20天搞定Python】第1天：Python环境搭建 
tags: []
categories: [] 

---
Python能做太多有趣使用的事了，不仅可以做现在火热的人工智能、数据分析，还可以做爬虫、Web开发、自动化运维的事情。 随着Python为我们工作与生活带来更多的便捷后，很多人开始学习Python，关注Python的发展前景、薪资和职业素养的提高。 

于是有了一个大胆的想法，更细致的写一系列的Python相关的文章，首先是20天学会Python基础，里面涵盖了Python必备的基础知识点，希望大家能利用业余时间掌握 Python 开发技能，轻松实现职业转化。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/f310a1393cbb1ee3e848de33d019b6d4.webp?x-oss-process=image/format,png">

## 编程语言是什么？

Python 代码示例：

```
print("hello world")
```

这段代码在稍后的课程就会学习到，它能让电脑在屏幕上打印"hello world"这样一段内容。

可以看到这段代码是由英文单词和标点符号来组成的，实际上编程就像是写作文，只是书写的时候必须要遵守一些特殊的格式规定。

但是计算机是基于二进制的 0 和 1 来处理运算，所以当今的世界才会叫数字化时代。这种 0 和 1 的组合指令又叫做机器语言，机器语言是电脑能够直接处理的指令，换而言之电脑根本不认识我们编程时写的英文单词和标点符号。

那么我们编程写的代码究竟如何控制电脑运行的？

就像我们和外国人说话要把内容翻译成英语一样。如果我们的代码想要运行，就必须要经过翻译处理，把 Python 语言的代码翻译成机器语言，这个过程叫做 编译，用来处理代码编译的软件叫做 编译器。

编程语言就是用来定义 计算机程序 的形式语言。我们通过编程语言来编写程序代码，再通过语言处理程序执行向计算机发送指令，让计算机完成对应的工作。

简单来说，编程语言就是人类和计算机进行交流的语言。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/6699cb890dcf820203ff7b9c9ad7c41d.webp?x-oss-process=image/format,png">

## 计算机是如何处理程序的？

按照冯·诺依曼存储程序的原理，计算机的工作流程大致如下：

用户打开程序，程序开始执行； 操作系统将程序内容和相关数据送入计算机的内存； CPU根据程序内容从内存中读取指令； CPU分析、处理指令，并为取下一条指令做准备； 取下一条指令并分析、处理，如此重复操作，直至执行完程序中全部指令，最后将计算的结果放入指令指定的存储器地址中。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/286b411fee1a5458299f1ec318bb9de7.webp?x-oss-process=image/format,png">

## Python简介

Python是由荷兰人吉多·范罗苏姆（Guido von Rossum，后面都称呼他为Guido）发明的一种编程语言。

## Python的历史

1989年圣诞节：Guido开始写Python语言的编译器。

1991年2月：第一个Python解释器诞生，它是用C语言实现的，可以调用C语言的库函数。

1994年1月：Python 1.0正式发布。

2000年10月：Python 2.0发布，Python的整个开发过程更加透明，生态圈开始慢慢形成。

2008年12月：Python 3.0发布，引入了诸多现代编程语言的新特性，但并不完全兼容之前的Python代码。

>  
 说明：大多数软件的版本号一般分为三段，形如A.B.C，其中A表示大版本号，当软件整体重写升级或出现不向后兼容的改变时，才会增加A；B表示功能更新，出现新功能时增加B；C表示小的改动（例如：修复了某个Bug），只要有修改就增加C。   


## Python的优点

Python的优点很多，简单为大家列出几点。

简单明确，跟其他很多语言相比，Python更容易上手。

开放源代码，拥有强大的社区和生态圈。

能够在Windows、macOS、Linux等各种系统上运行。

## Python的应用领域

目前Python在Web服务器应用开发、云基础设施开发、网络数据采集（爬虫）、数据分析、量化交易、机器学习、深度学习、自动化测试、自动化运维等领域都有用武之地。

## 安装Python环境

想要开始你的Python编程之旅，首先得在计算机上安装Python环境，简单的说就是得安装运行Python程序的工具，通常也称之为Python解释器。我们强烈建议大家安装Python 3的环境，很明显它是目前更好的选择。

## Windows环境

可以在Python官方网站找到下载链接并下载Python 3的安装程序。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/3f173287a6ff1bf907ffa39afff81803.webp?x-oss-process=image/format,png">

对于Windows操作系统，可以下载“executable installer”。需要注意的是，如果在Windows 7环境下安装Python 3，需要先安装Service Pack 1补丁包，大家可以在Windows的“运行”中输入winver命令，从弹出的窗口上可以看到你的系统是否安装了该补丁包。如果没有该补丁包，一定要先通过“Windows Update”或者类似“CCleaner”这样的工具自动安装该补丁包，安装完成后通常需要重启你的Windows系统，然后再开始安装Python环境。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/0087fe640fe55c05bb1cc6e7560ec50d.webp?x-oss-process=image/format,png">

双击运行刚才下载的安装程序，会打开Python环境的安装向导。在执行安装向导的时候，记得勾选“Add Python 3.x to PATH”选项，这个选项会帮助我们将Python的解释器添加到PATH环境变量中（不理解没关系，照做就行），具体的步骤如下图所示。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/48089ca39bdc432e341c0d2dcbc89bb6.webp?x-oss-process=image/format,png">

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/bc54d2e8aa66b74087f37e04aafd0a0d.webp?x-oss-process=image/format,png">

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/fff95915f72325aa28c4c9101a8c21ce.webp?x-oss-process=image/format,png">

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/503df02c2fa9efe24f02bbde79006dfb.webp?x-oss-process=image/format,png">

安装完成后可以打开Windows的“命令行提示符”工具并输入python --version或python -V来检查安装是否成功，命令行提示符可以在“运行”中输入cmd来打开或者在“开始菜单”的附件中找到它。如果看了Python解释器对应的版本号（如：Python 3.7.8），说明你的安装已经成功了，如下图所示。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/653c5316da78f36d51684a19112804de.webp?x-oss-process=image/format,png">

>  
 说明：如果安装过程显示安装失败或执行上面的命令报错，很有可能是因为你的Windows系统缺失了一些动态链接库文件而导致的问题。如果系统显示api-ms-win-crt*.dll文件缺失，可以在微软官网下载Visual C++ Redistributable for Visual Studio 2015文件进行修复，64位的系统需要下载有x64标记的安装文件。如果是因为安装游戏时更新了Windows的DirectX之后导致某些动态链接库文件缺失问题，可以下载一个DirectX修复工具进行修复。   


## macOS环境

macOS自带了Python 2，但是我们需要安装和使用的是Python 3。可以通过Python官方网站提供的下载链接找到适合macOS的“macOS installer”来安装Python 3，安装过程基本不需要做任何勾选，直接点击“下一步”即可。安装完成后，可以在macOS的“终端”工具中输入python3命令来调用Python 3解释器，因为如果直接输入python，将会调用Python 2的解释器。

>  
 说明：如果对安装Python环境有任何疑问，可以参考这个视频讲解。视频链接：https://pan.baidu.com/s/1Tu8wy9IExP_Co6CurVr2Pg，密码：rbao。   


## pip的使用

安装完Python之后，通过查看目录可以看到

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/9ebe36e509b1227bb2f062f6a5c2fe6f.webp?x-oss-process=image/format,png">

 Lib就是Python的标准库，里面包含了各种开发时使用的库文件，但是这些在后面的开发中是远远不够的，我们还需要更多的第三方扩展库。那就需要pip的帮助。

pip 是一个现代的，通用的Python包管理工具。提供了对 Python 包的查找、下载、安装、卸载的功能，便于我们对Python的资源包进行管理。

## 安装

在安装Python时，会自动下载并且安装pip.

## 配置
- 在windows命令行里，输入 pip -V 可以查看pip的版本。<img alt="" src="https://img-blog.csdnimg.cn/img_convert/054585063c90c2324af520339750747d.webp?x-oss-process=image/format,png">- 如果在命令行里，运行pip -V,出现如下提示:<img alt="" src="https://img-blog.csdnimg.cn/img_convert/186ec86e97c2d807da2f6d178f25e231.webp?x-oss-process=image/format,png">
可能是因为在安装python的过程中未勾选 Add Python 3.7 to PATH 选项，需要手动的配置pip的环境变量。  

手动配置如下：
- 右键此电脑--&gt;环境变量--&gt;找到并且双击Path--&gt;在弹窗里点击新建--&gt;找到pip的安装目录，把路径添加进去。<img alt="" src="https://img-blog.csdnimg.cn/img_convert/7729af08f7cc4494f49dbd792c9fc426.webp?x-oss-process=image/format,png">- 这里新添加的路径 C:\Users\你的用户名\AppData\Local\Programs\Python\Python37\Scripts 是Python安装好以后，pip.exe 这个可执行文件所在的目录。<img alt="" src="https://img-blog.csdnimg.cn/img_convert/9a70450274de4c09d57f8d35741d1c3f.webp?x-oss-process=image/format,png">
## 使用pip管理Python包
- pip install &lt;包名&gt; 安装指定的包- pip uninstall &lt;包名&gt; 删除指定的包- pip list 显示已经安装的包- pip freeze 显示已经安装的包，并且以指定的格式显示- pip install -r required.txt 安装required.txt文件里列出的安装包
## 修改pip下载源

运行pip install 命令会从网站上下载指定的python包，默认是从 https://files.pythonhosted.org/ 网站上下载。这是个国外的网站，遇到网络情况不好的时候，可能会下载失败，我们可以通过命令，修改pip现在软件时的源。 格式:

pip install 包名 -i 国内源地址

示例: pip install flask -i https://pypi.mirrors.ustc.edu.cn/simple/ 就是从中国科技大学(ustc)的服务器上下载flask(基于python的第三方web框架)

国内常用的pip下载源列表:
- 阿里云 http://mirrors.aliyun.com/pypi/simple/- 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/- 豆瓣(douban) http://pypi.douban.com/simple/- 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/- 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
## 初识Python总结

到这里，大家已经对Python语言有一个基本的了解，知道它可以做很多的事情，所以也值得我们去学习。要用Python做开发，首先需要在自己的计算机上安装Python环境，上面我们为大家介绍了macOS和Windows两种环境下Python 3环境的安装方法，希望大家都能顺利的安装成功，以便开启我们后续的学习。
