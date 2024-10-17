
--- 
title:  讲讲 Python Launcher 是什么鬼东西？ 
tags: []
categories: [] 

---
   作者：听雨危楼

   https://www.cnblogs.com/Neeo/p/8393805.html

你可能在他处见到过这鬼东西，when you install or uninstall python, and so on。那么你肯定与我一样对这个鬼东西起了一丝兴趣趣！

### 1. 问题所在

由于Python2.x版本的脚本和Python3.x版本的脚本在语法上会有不兼容的情况。那么，必须使用不同的策略来允许【py】脚本使用基于脚本指定的Python解释器版本来选择合适的Python解释器！这句话相当的拗口！说人话，就是我有个test脚本需要Python2.x版本的解释器来执行。

```
python test.py

```

你如何确保执行该脚本的解释器版本就是我需要的解释器！也就是，如何确定你就是我需要的那个姑娘！上面的“python”命令，是系统在PATH中找到的。而PATH中Python变量，有可能被我们手动修改，抛开这个不谈，一般的，‘python’命令是调用Python3.x版本的解释器。但这不完全可靠，因为当系统在PATH中找‘python’命令时，如果Python2.x版本的在Python3.x的前面，那么， Python的默认解释器将变为2.x版本，因为系统找到一个就返回了(系统在Python2.x的安装目录中找到了python.exe)。想想你的Python解释器的安装目录内。不管是哪个版本都有这些：

针对这个弊端，又有了另一个约定：

•python2将引用Python 2.x的某些版本•python3将引用Python 3.x的某些版本

要了解更多的关于Python在‘python’命令方面的其他的约定，请参考PEP 394

#### 在 Linux 中

在Linux中(基于Unix的系统中)，通过软连接的方式来绑定指定的Python解释器。比如：

这些软连将不同的python命令指向一个实际位置的Python解释器的启动目录。而这些在哪用到呢，被【**Shebang**】用到了，也就是俗称的文件头(这里只聊shebang关于Python文件头的部分)。通过文件头系统就去软连中找到对应的那个‘python’命令，而该命令有绑定到一个具体的Python解释器。

```
#!/usr/bin/python2

```

#### 在 Windows 中

上述问题也存在与Windows系统中，那么我们也希望在Windows中和Unix中同样运行【Shebang】的能力，并且——没有什么是又好使又不需要发明新的语法或者约定来描述更让人愉快的事情了！经过后来的完善，在PEP 397中正式出现并伴随Python3.3版本发布。它叫【**Python Launcher**】

### 2. 解决问题

Python launcher是用于Windows中的一个实用程序，可帮助我们定位和执行不同版本的Python解释器。它允许脚本或者命令行指示特定的Python版本的首选项，并将定位并执行该版本。mmp，还是这么拗口！说人话就是它很智能的区分开是你想要手动指定解释版本执行py脚本，还是想使用脚本文件指定的解释器。你手动的选择Python解释器，这是调用了你在【PATH】中的Python变量。举个例子。你在Windows下的cmd中，使用Python3.7版本的解释器，执行一个文件：

```
$ python3.7 test.py

```

这么执行发生了什么？Windows会在PATH中寻找python3.7这个解释器。找到并执行test.py文件。而这个test.py(你从未打开过该文件)文件呢，其实它需要python2.7版本的解释器来执行。这样是不是就有问题了。我们用Python launcher来解决这个问题，这玩意儿它会正确的选择最合适的Python版本。

#### 如何安装 Python launcher

一般的，从3.3版本开始，Python launcher会伴随解释器的安装而可选安装，在安装步骤的可选项中可勾选。如本博客的第一个图所示。它会被放在系统的PATH中(Python3.6版本开始是这样的，之前版本稍有变动，参见Python3.3版本新功能)，如果你不手动添加的话。

另一种方式是单独安装。如本博客的第一个图所示，你可以单独勾选该项使之单独安装。在多个版本Python中，Python launcher只需安装一次，并且兼容所有的Python版本。所以，如果在安装3.6版本是，选择Python launcher选项，那么如果你在安装3.7版本，该项则就无法选中，因为已经安装了。

Python launcher有两个版本，一个是控制台程序，另一个是‘windows’(即GUI)程序。这两个程序对应我们Python安装目录中的‘python.exe’和‘pythonw.exe’这两个可执行文件。

控制台程序被命名为‘py.exe’，而windows程序则命名为‘pyw.exe’，并且pyw.exe将定位并执行pythonw.exe。

```
M:\&gt;where py
C:\Windows\py.exe


M:\&gt;where pyw.exe
C:\Windows\pyw.exe

```

这里仅用控制台程序举例。

#### 如何使用 Python launcher?

如果你安装Python launcher，那么你可以在任意的目录打开cmd测试。

默认的，Python launcher打开了你最新版本的解释器。可以正常的使用和退出。而不是你最近安装的某个版本的解释器。

如果你的系统环境中有多个版本的Python解释器，那么，要想启动，则可以这样：

当然，Python launcher可以帮我们解决某些问题。比如现在有个test.py文件，我们用Python launcher来启动。

```
#! python2.7


import sys
print(sys.version)


# --------- 以上为文件内容， 以下为执行结果 --------------
M:\&gt;py test.py
2.7.14(v2.7.14:84471935ed, Sep162017, 20:19:30) [MSC v.150032 bit (Intel)]

```

可以看到，Python launcher根据文件头自动帮我们调用了指定版本的解释器来执行该文件。我们修改下文件头再来测试。

```
#! python3


import sys
print(sys.version)


# --------- 以上为文件内容， 以下为执行结果 --------------
M:\&gt;py test.py
3.7.0(v3.7.0:1bf9cc5093, Jun272018, 04:06:47) [MSC v.191432 bit (Intel)]

```

这样，Python launcher帮我们找到我们想要的那个姑娘。再来看个没有文件头的。

```
import sys
print(sys.version)


# --------- 以上为文件内容， 以下为执行结果 --------------
M:\&gt;py test.py
3.7.0(v3.7.0:1bf9cc5093, Jun272018, 04:06:47) [MSC v.191432 bit (Intel)]

```

结果，Python launcher默认使用最新版本的解释器来执行。我们也可以绕过文件头，使用我们指定版本的Python解释器。

```
#! python2


import sys
print(sys.version)


# --------- 以上为文件内容， 以下为执行结果 --------------
M:\&gt;py -3 test.py
3.7.0(v3.7.0:1bf9cc5093, Jun272018, 04:06:47) [MSC v.191432 bit (Intel)]


M:\&gt;py -3.5 test.py
3.5.4(v3.5.4:3f56838, Aug82017, 02:07:06) [MSC v.190032 bit (Intel)]

```

如上所示,我们还可以指定版本来执行脚本。

Python社区从多方面考虑下才有的Python launcher，方便我们在windows下使用Python。如果现在的我们用不到它，只需大概知道是干嘛就行，不求甚解。

以上为我个人对Python launcher的理解。如有错误，还望斧正。

<img src="https://img-blog.csdnimg.cn/img_convert/23dc42d3efe76d7638331dc72bee9a4d.png">
