
--- 
title:  可视化 Python 打包 exe，这个神器绝了 
tags: []
categories: [] 

---
免责声明：本文内容来源于网络，文章版权归原作者所有，意在传播相关技术知识&amp;行业趋势，供大家学习交流，若涉及作品版权问题，请联系删除或授权事宜。

### # 1. 什么是auto-py-to-exe

auto-py-to-exe 是一个用于将Python程序打包成可执行文件的图形化工具。本文就是主要介绍如何使用 auto-py-to-exe 完成 python 程序打包。auto-py-to-exe 基于 pyinstaller ，相比于 pyinstaller ，它多了 GUI 界面，用起来更为简单方便

### # 2. 安装 auto-py-to-exe

首先我们要确保我们的 python 环境要大于或等于 2.7 然后在 cmd 里面输入：pip install auto-py-to-exe ，输入完成之后，pip 就会安装 auto-py-to-exe 包了。安装完成之后，我们就可以在 cmd 输入：auto-py-to-exe，来启动 auto-py-to-exe 程序了。

<img src="https://img-blog.csdnimg.cn/img_convert/aeecb2386d1a607f73a1d7e94ad5678f.png" alt="aeecb2386d1a607f73a1d7e94ad5678f.png">

出现上述图片，auto-py-to-exe 就安装成功了。

### # 3. auto-py-to-exe 部分选项介绍

在使用 auto-py-to-exe 打包 python 程序的时候，有许多配置选项需要我们去指定，能正确知道这些选项的作用是十分重要的。下面我将介绍其中一些重要的选项。

(1) Script Location

Script Location 主要是指定我们要打包的 python 文件

<img src="https://img-blog.csdnimg.cn/img_convert/a9d29d59b52ef202993a66d1ae2c8fb8.png" alt="a9d29d59b52ef202993a66d1ae2c8fb8.png">

(2) Onefile

Onefile 下有两个选项，分别是：One Directory 和 One File
- 如果选择 One Directory ，那么程序打包完成后会是一个文件夹的形式展现- 如果选择 One File ，那么程序打包完成后就一个 .exe 文件
(3) Console Window

Console Window 主要设置打包程序运行时，是否出现控制台
- Console Based : 当打包的程序运行时会显示一个控制台界面- Window Based (hide the console) : 会隐藏控制台界面，主要用于带有 GUI 的 python 程序打包
(4) Icon

用于指定打包程序的图标

### # 4. auto-py-to-exe 实战

本节主要以一个计算器程序来介绍如何使用 auto-py-to-exe 来打包程序。

auto-py-to-exe 打包程序主要分 3 部分，分别是：
- 打开 auto-py-to-exe- 配置打包选项- 查看打包效果
####  1. 打开 auto-py-to-exe

打开 cmd ，输入：auto-py-to-exe 打开 auto-py-to-exe 后，我们就要进行配置选择了。

####  2. 配置打包选项

计算器程序，大家可以到 GitHub 去下载，地址是：https://github.com/pythonprogrammingbook/simple_calculator

在打包时，我们要进行的配置主要有：
- Script Location- Onefile- Console Window
Script Location 选择程序的主程序，在计算器项目里，我们选择的是 main.py

Onefile 选择 One File ，因为一个文件看起来比较简洁

由于计算器项目带有 GUI ,所以 Console Window 选择 Window Based (hide the console) ,

Icon 选择一个 ico 文件，此处不是必须操作，可以不设置

<img src="https://img-blog.csdnimg.cn/img_convert/56caacf8e3712a95869b72ec82dea009.png" alt="56caacf8e3712a95869b72ec82dea009.png">

如果程序里面有自己的模块，我们必须把模块的目录添加到 Additional Files 里面。不然会出现 Failed to execute script XXX 错误

<img src="https://img-blog.csdnimg.cn/img_convert/7f55441d38b7408cdb0c5c5b5f52d6ed.png" alt="7f55441d38b7408cdb0c5c5b5f52d6ed.png">

在计算器程序里面我们所有的模块都在 calculation 目录下，所有我们需要将 calculation 路径添加到 Additional Files 里面

<img src="https://img-blog.csdnimg.cn/img_convert/36b77258172951c2810b25e7331fcd54.png" alt="36b77258172951c2810b25e7331fcd54.png">

配置完成之后点击 CONVERT .PY TO .EXE 按钮

这样我们就完成一个计算器项目的打包。

####  3. 查看打包效果

程序完成打包后，我们可以点击 OPEN OUTPUT FOLDER 按钮，然后就会打开打包文件的路径。

<img src="https://img-blog.csdnimg.cn/img_convert/28970cb7cfa5b33057656b28f612deb5.png" alt="28970cb7cfa5b33057656b28f612deb5.png">

在打包文件目录中，我们可以看到一个 main.exe 文件，这就是我们打包文件。

点击 main.exe ，就可以看到一个计算器程序了。

<img src="https://img-blog.csdnimg.cn/img_convert/dbc2f3d5d03725a135c694b1ad37c139.png" alt="dbc2f3d5d03725a135c694b1ad37c139.png">

至此，打包工作圆满完成。

### # 5. 总结一下

本文主要介绍了如何使用 auto-py-to-exe 来对 python 程序进行打包。但只是介绍最简单的 python 程序打包，如果想对复杂的程序进行打包，上面的配置肯定是不行的。

如果想更加深入的了解 auto-py-to-exe ，我建议大家去研究一下 pyinstaller 。auto-py-to-exe 是基于 pyinstaller 的，研究 pyinstaller ，将会对我们深入使用 auto-py-to-exe 有非常明显的效果。

想更加深入了解 pyinstaller 可以去阅读官方文档。







<img src="https://img-blog.csdnimg.cn/img_convert/9fd8ec52873325ece03fef21a683910b.png" alt="9fd8ec52873325ece03fef21a683910b.png">
