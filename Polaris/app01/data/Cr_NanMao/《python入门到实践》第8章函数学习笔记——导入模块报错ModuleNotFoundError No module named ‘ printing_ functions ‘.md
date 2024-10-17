
--- 
title:  《python入门到实践》第8章函数学习笔记——导入模块报错ModuleNotFoundError: No module named ‘ printing_ functions ‘ 
tags: []
categories: [] 

---
>  
         前言：《python入门到实践》这本书第一部分教学全程使用Sublime Text。我是用macOS版本的Sublime Text，macOS的Sublime Text在你编写好程序保存时是不会在程序名字后面自动加上.py后缀的。 


问题描述：在学习到《python入门到实践》这本书的第8章函数，P138的练习8-15（打印模型）时，按照书上把printing_functions.py模块文件和printing_models.py敲出来后，运行printing_models.py出现ModuleNotFoundError: No module named ' printing_ functions '的报错。截图如下。

<img alt="" height="225" src="https://img-blog.csdnimg.cn/9954072e388f40f9a7e70bcaff8311e2.png" width="346">

在搜索了百度和CSDN的各种解答后，发现解答都是说模块与调用模块的.py文件路径的问题，需要怎么修改路径巴拉巴拉。。。虽说这些解答都非常不错！但是！这个报错并不是由于路径问题造成的报错，而是我前言所说的：“macOS的Sublime Text在你编写好程序保存时是不会在程序名字后面自动加上.py后缀的。”---是这个问题才导致程序报错的。

解决办法：将模块文件名字后加上拓展名.py就可以解决问题了！！如下图。

<img alt="" height="125" src="https://img-blog.csdnimg.cn/c7d47c3965804d89a2e048e2b2a55ee9.png" width="255">

<img alt="" height="259" src="https://img-blog.csdnimg.cn/cd0978ea94ed4a358c8260e4bca511de.png" width="397">

****ps：本篇文章是基于《python入门到实践》这本书中的课后练习作出的问题解决方法。刚学python，出现的问题也比较基础。我觉得肯定也有其他跟我一样的python小白学习这本书时出现了同样的问题，希望能帮助到各位朋友～****

****希望大家即使遇到问题也都能坚持下来！****






