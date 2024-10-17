
--- 
title:  Python、Pycharm、Anaconda 三者之间的关系 
tags: []
categories: [] 

---
## Python

Python是一种跨平台的计算机程序语言。是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，被用于独立的、大型项目的开发。

## Pycharm

PyCharm是一种常用的Python IDE，带有一整套可以帮助用户在使用Python语言开发时提高其效率的工具，比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制。此外，该IDE提供了一些高级功能，以用于支持Django框架下的专业Web开发，界面编写代码和运行操作更加简单。

## Anaconda

Anaconda指的是一个开源的Python发行版本，其包含了conda、Python等180多个科学包及其依赖项。因为包含了大量的科学包，Anaconda 的下载文件比较大（约 531 MB），如果只需要某些包，或者需要节省带宽或存储空间，也可以使用Miniconda这个较小的发行版（仅包含conda和 Python）。

Anaconda包括Conda、python以及一大堆安装好的工具包比如：numpy、pandas等。 Miniconda只包括Conda、Python，是Anaconda的简约版。 conda是一个开源的包、环境管理器，可以用于在同一个机器上安装不同版本的软件包及其依赖，并能够在不同的环境之间切换。

## 开发搭配

只学习python语言的初学者可以先下载好特定版本的Python解释器后，然后再搭配界面程序Pycharm来进行简单的语法学习和项目调试，因为不需要考虑不同项目需要不同python工具包的版本问题。即：Python解释器 + Pycharm。

而要进行项目开发的人员，时常有多个项目同时开发，并且不同的项目需要不同版本的工具包，这时使用Anaconda可以帮助我们管理更多项目的环境，将每个项目单独放在一个虚拟环境中，并且使这些环境中工具包相互独立，不会产生工具包版本冲突问题，并且可以下载多个版本的工具包，可以安装多个不同版本的Python解释器。Anaconda自带Python解释器，即：Anaconda + Pycharm。
