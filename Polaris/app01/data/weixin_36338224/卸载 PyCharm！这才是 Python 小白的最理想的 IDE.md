
--- 
title:  卸载 PyCharm！这才是 Python 小白的最理想的 IDE 
tags: []
categories: [] 

---
若你在搜索引擎（如百度）或者各种问答社区（如知乎）搜索『**学习Python 最好的 IDE/编辑器是哪个？**』

我想答案肯定是：PyCharm、Jupyter、VSCode、Vim、Sublime Text

不过，在我看来，**最好的编辑器** 应当视情况而定，比如
- 如果你是搞数据分析、机器学习的，推荐你使用 Jupyter- 如果是搞大型工程项目的，经常要阅读开源项目代码，推荐你使用 PyCharm- 如果你需要使用多种编辑语言，并且不喜欢使用 JB 家的破解版软件，推荐你使用 VS Code- 如果你闲得淡疼、追求极客，那推荐你使用 Vim
除此之外，还有非常多优秀的 Python 代码编辑器，比如 Sublime Text、Atom、Wing、Spyder 等。

但是我今天要介绍的这个 IDE ，你很有可能没有使用过，更有可能连听都没听过，它叫 `Thonny`，它是由塔尔图大学开发，适合新手程序员。其界面没有任何复杂或多余功能，很容易上手。另一个适合新手的地方是，你可以看到 Python 在每一步中对你的表达式的评估。

我推荐所有的 Python 新手，都去安装一个 Thonny 。

理由如下：
- 它支持全平台（Windows，Mac，Linux）- 它支持简体中文，对英文不好的同学非常友好- **它界面简洁直白，内置的功能都是完全面向新手的**- **它内置 Python 3，无需新手额外安装Python和配置环境**- **它的调试界面非常直观，可吊打市面上 90% 的编辑器**- **它提供比代码行粒度更小的调试模式，是它闪光点之一**- 它支持语法高亮，应该是基本功能了- 它支持代码补全（只可惜不是自动，而是手动）- **它内置非常简洁易用的图形界面包管理器**
下面一一为大家进行演示

### 1. 全平台支持

无论你使用的是 Win、Mac，还是 Linux，Thonny 都有对应的版本支持。

Win 和 Mac 版本的安装包，我已经全部打包好了，可点此下载：https://wws.lanzous.com/iX5rWlvkdfa

对于 Linux 用户，需要使用命令来安装

```
# Binary bundle for PC (Thonny+Python):
$ wget -O - https://thonny.org/installer-for-linux)

# With pip
$ pip3 install thonny

# Debian, Raspbian, Ubuntu, Mint and others:
sudo apt install thonny

# Fedora
$ sudo dnf install thonny

```

### 2. 支持简体中文

Thonny 是虽然是外国人开发的，不过它目前也是支持简体中文的，这对于英文不好的初学者，真的是福音。

在你安装的时候就会提示你进行语言选择

<img src="https://img-blog.csdnimg.cn/img_convert/f4667145eaca5ad48c694c5932bae399.png" alt="">

如果安装时忘记设置，同样也是可以在菜单栏二次更改。

<img src="https://img-blog.csdnimg.cn/img_convert/872638b8aebb7cce8bd45741405dcd3f.png" alt="">

### 3. 内置 Python

对于新手来说，最重要的就是能够尽快有一个可以跑代码的环境

Thonny 内置了 Python 3.7.9 ，因此它不需要你去官网下载 Python 解释器，也不用你去学习如何配置环境变量。

<img src="https://img-blog.csdnimg.cn/img_convert/14de863093d1997d8adc5409a6983688.png" alt="">

通过查看 os 模块的路径，可以得知这个 Python 的安装路径

<img src="https://img-blog.csdnimg.cn/img_convert/3937fb880767de4fe248c70f29dc910b.png" alt="">

当然了，如果你觉得 Python 3.7 已经过时了，想使用最新的 Python 3.9 也是可以设置的

<img src="https://img-blog.csdnimg.cn/img_convert/993a80d4734a8ebd14ce2c61a0b6ce07.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/050c60605a6b3621e5b613b75be47c11.png" alt="">

### 4. 简洁的界面

整个软件的界面非常的简洁，可以说多余的功能一个都没有，而该有的功能也一个不少。

随便打开一个测试用的 Python 脚本，点击右上角的运行按钮就可以运行这个脚本程序，程序中打印的内容会在 Shell 窗口中打印，从界面上很容易可以看出，实际上你点击运行按钮后，就是在 Shell 窗口中执行一条 `%Run xx.py` 的魔法命令。

<img src="https://img-blog.csdnimg.cn/img_convert/c1c37624e1d1eb69860a8a5c1307051e.png" alt="">

### 5. 可视化包管理器

同时他还自带了可视化的包管理器，方便新手安装和卸载 Python 的各种第三方包

<img src="https://img-blog.csdnimg.cn/img_convert/6659901583718289182774d896477b5c.png" alt="">

### 6. 手动代码补全

同时作为一款简易的 IDE ， Thonny 同时也是支持代码补全，只不过这代码补全并不是那么智能，需要按下快捷键（⌃ + s）来手动触发。

<img src="https://img-blog.csdnimg.cn/img_convert/e45178bbed18b021fcaf18f4958d53c7.gif" alt="">

### 7. 惊艳全座的调试功能

以上如果还不足以让你动心，别急，我来介绍下 Thonny 最让为惊艳的调试功能。

通过菜单栏调出 `变量面板`，此时你在 Shell 中定义的变量，都会显示在变量面板上，一旦你对变量进行修改，变量面板也会实时刷新。

<img src="https://img-blog.csdnimg.cn/img_convert/3fdb6e9eb8bdc27de2b9e17bb51fce3b.gif" alt="">

通过点击控制面板上的小甲虫，就进入了调试模式，甲虫旁边的四个按钮就会跟着亮起来，分别是
- `步过`（Step Over） ：以代码行为单位的单步调试- `步进` （Step Into）：比步过更细粒度的单步调试，可进入函数- `步出`（Step Out） ：执行到函数执行结束- `恢复执行` ：执行到程序结束
<img src="https://img-blog.csdnimg.cn/img_convert/70c6157f5466814795dcaf2f7a9061f6.gif" alt="">

**咦，你肯定会说，明哥，你别标题党了，这些功能在 PyCharm 上不是都有吗？**

别急，请你接着往下看，Thonny 中的步进调试达到的效果，就算是 PyCharm 也还没有做到如此便于新手学习的调试体验。

它可以把单行表达式，拆分成多个步骤进行调试，在这个过程中，表达式中的变量名会直接显示为其数值，这对于新手理解复杂的单行表达式是非常有帮助的。

具体请看下面这张动图，`age &lt;= 3` 这个表达式，会先显示 age 的变量值，然后和3进行逻辑运算，再把运算的结果显示出来。

<img src="https://img-blog.csdnimg.cn/img_convert/45c1be41e6f0e474b4c985ccb63023ad.gif" alt="">

当你使用 `步进` 进入函数调用，每调用一步函数，都会重新打开一个带有单独的局部变量表和代码指针的新窗口，它能够帮助学习者充分了解函数调用的原理，尤其对于理解递归这种相对复杂的逻辑。

下面以一个生成 **斐波那契数列** 的函数为例演示

<img src="https://img-blog.csdnimg.cn/img_convert/e6abb42aa9acc9f000af85a938793435.png" alt="">

Thonny 中步进调试可以说是它的一大亮点，但是可惜的是Thonny 目前还不支持设置断点，这是比较遗憾的。

### 8. 快捷键一览表

**Windows 的快捷键**

<img src="https://img-blog.csdnimg.cn/img_convert/f683d506d92d83802fad6cf9a3804bd9.png" alt=""> **Mac 的快捷键**

<img src="https://img-blog.csdnimg.cn/img_convert/208d4f4daf0779397d080254a9855cd0.png" alt="">

### 9. 写在最后

取之 Python，用之Python，Thonny 是基于 Python 内置图形库 tkinter开发出来的一个可视化工具，它是完全面向 Python 初学者的 轻量级 Python IDE，它能帮助初学者搞懂每一行代码的运行细节，它帮小白解决了一些繁杂的环境问题，真正做到拿到即学。

在我看来，是最适合 Python 初学者的 IDE ，推荐给你使用。

Thonny 下载链接：https://wws.lanzous.com/iX5rWlvkdfa

另外，我还整理了 100 个 PyCharm 的使用技巧，为了让新手能够直接上手，我花了很多的时间录制了上百张 GIF 动图，有兴趣的前往在线文档阅读：



以下是详细目录：
<li>**第一章：下载与安装** 
  <ul>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 