
--- 
title:  一个创意十足的 Python 命令行工具 -- trypackage 
tags: []
categories: [] 

---
听到某些人说 xx 库非常好用的时候，我们总是忍不住想要去亲自试试。

有一些库，之所以好用，是对一些库做了更高级的封闭，你装了这个库，就会附带装了 n 多依赖库，就比如前一篇文章介绍的 streamlit 来说，依赖包就达 90 几个之多？

比百度全家桶，还 tm 的全家桶啊…

也正是因为害怕会污染我的全局 Python 环境，我通常在试用新包的时候，都会使用 venv 创建虚拟环境，再去安装，完事之后，再清理虚拟环境即可。

有没有发现，整个流程，其实还是挺麻烦的。

刚好昨天晚上，Github 上瞎逛，被我发现一个库，可以解决我一直以来的烦扰。

这个库叫 `trypackage`，为试库而生的库。

整体的效果可以看下面这张动图

![](http://image.iswbm.com/Kapture 2022-01-11 at 00.09.07.gif)

当你使用 `try xx` 命令时，它会做哪些事呢？
- 安装指定版本的 Python 解释器- 创建临时的虚拟环境- 激活虚拟环境- 在虚拟环境中安装你要试用的 Python 库- 直接进入 Python Shell 模式- 自动将你要试用的库导入进来
### 1. 如何安装

一条命令就可以安装它

```
python3 -m pip install trypackage


```

可以看到 trypackage 只依赖一个 click 命令行库，还是很轻量的

<img src="https://img-blog.csdnimg.cn/img_convert/e33f70752a0b4629b70acd18dd11dbab.png" alt="">

其实不是这样，try 会基于 virtualenv 创建虚拟环境，因此还要安装 virtualenv 和 virtualenvwrapper

```
python3 -m pip install virtualenv virtualenvwrapper


```

### 2. 基本使用

使用 `try requests`，try 就会创建一个虚拟环境，然后在该虚拟环境中，安装 requests ，安装完成后，自动进入 Python Shell 的模式，并且自动导入好你要试用的包

<img src="https://img-blog.csdnimg.cn/img_convert/1c9bab296f394f3a10507ad122f88186.png" alt="">

最贴心的是，试用完后，退出 Python Shell ，会自动清理掉虚拟环境。

### 3. 更多用法

#### 指定 python 版本

我的环境没有安装 Python 3.8，通过 `-p` 参数，可以指定 Python 3.8 ，安装的过程太快，快得让我有点怀疑这是不是真正的去安装 Python 3.8 解释器了。

<img src="https://img-blog.csdnimg.cn/img_convert/e48e957ee970392c3b91c2fc1470c8a9.png" alt="">

也可以直接指定本地的 Python 版本，例如

```
try requests -p /usr/bin/python3.7.1


```

#### 指定运行模式

Try 直接的运行模式非常多

**1、当你不指定时，默认使用 python shell 的模式**

```
# 二者等价
try requests
try requests --shell python


```

**2、使用 ipython 有两种指定方式**

```
# 二者等价
try requests --ipython
try requests --shell ipython


```

<img src="https://img-blog.csdnimg.cn/img_convert/79681bc4e9c9dd943c8cf75fe480e226.png" alt="">

**3、使用 ptpython 或者 ptipython**

这两种模式都有代码提示与自动补全功能

<img src="https://img-blog.csdnimg.cn/img_convert/ac6a8ad922373723f1f17cd39d53d6e3.png" alt="">

**4、使用 bpython 模式**

Bpython 的代码提示与补全比 ptpython 、ptipython ，更强一点，其他的区别还没试用到。

<img src="https://img-blog.csdnimg.cn/img_convert/6abfa3c9049282b7f46af79e1576b72d.png" alt="">

#### 在编辑器中打开

```
try requests --editor


```

#### 指定 Github 仓库包

```
# 语法示例
try &lt;user&gt;/&lt;repo&gt; 

# 安装 Github 上的 Kenneth/requests 上的 master 版本
try kennethreitz/requests  


```

#### 指定已经存在的虚拟环境

```
try requests --virtualenv ~/.try/sandbox 


```

#### 持久化虚拟环境

默认情况下，你退出后，会自动清理掉虚拟环境，若有特殊需要，可指定 `--keep` 参数来持久化虚拟环境

<img src="https://img-blog.csdnimg.cn/img_convert/9c4e11bc9ef2902b579616056b3a992d.png" alt="">

#### 指定虚拟环境的目录

默认情况下，try 会将虚拟环境创建在一个默认的目录中，这个目录比较深，不容易记住，你可以指定 `--tmpdir` 参数，告诉 try 要将虚拟环境创建在这里，这个参数对于想要持久化虚拟环境的人会很有用。

```
try requests --tmpdir ~/.try


```

### 4. 配置文件

try 虽然提供命令行入参的方式来识别用户选项，但对于一些用户来说，更希望能一次性修改 try 的默认选项，而不用每次都指定多个参数。

这时候，可以在你的 APP 目录下新增一个 config.ini 文件，内容模板如下

```
[env]
virtualenv=~/.try/sandbox
python=3.8
shell=ipython
keep=false
always_use_editor=false
tmpdir=~/.try


```

所谓的 APP 目录，在不同的系统中是不一样的，可以使用如下代码来查看

```
&gt;&gt;&gt; import click
&gt;&gt;&gt; click.get_app_dir("try")
'/Users/iswbm/Library/Application Support/try'
&gt;&gt;&gt;


```

有了 config.ini，再次 try ，就会发现效果与配置一样的预期一致。

<img src="https://img-blog.csdnimg.cn/img_convert/a1dfbdaf49e9c9a6b94c2e5fe3ed565b.png" alt="">

### 5. 总结一下

Try 是一个非常实用的命令行工具，可以说完全击中我的痛点，能把这样一个库做出来，真的是创意十足，再一次印证 Python 是懒人第一语言 。。

### 絮叨一下

我在CSDN上写过很多的 Python 相关文章，其中包括 Python 实用工具，Python 高效技巧，PyCharm 使用技巧，很高兴得到了很多朋友的认可和支持。在他们的鼓励之下，我将过往文章分门别类整理成三本 PDF 电子书

**PyCharm 中文指南**

《PyCharm 中文指南》使用 300 多张 GIF 动态图的形式，详细讲解了最贴合实际开发的 105个 PyCharm 高效使用技巧，内容通俗易懂，适合所有 Python 开发者。

在线体验地址：https://pycharm.iswbm.com

<img src="https://img-blog.csdnimg.cn/img_convert/3dc57c805f4271a6b12292348a9dd9c6.png" alt="">

**Python 黑魔法指南**

《Python黑魔法指南》目前迎来了 v3.0 的版本，囊集了 100 多个开发小技巧，非常适合在闲时进行碎片阅读。

在线体验地址：https://magic.iswbm.com

<img src="https://img-blog.csdnimg.cn/img_convert/f4b64b8115ad85ec8aace9854821a5dc.png" alt="">

**Python 中文指南**

学 Python 最好的学习资料永远是 Python 官方文档，可惜现在的官方文档大都是英文，虽然有中文的翻译版了，但是进度实在堪忧。为了照顾英文不好的同学，我自己写了一份 面向零基础的朋友 的在线 Python 文档 – 《Python中文指南》

在线体验地址：https://python.iswbm.com

<img src="https://img-blog.csdnimg.cn/img_convert/fb98d32afa4679972f711e3cdae95f9a.png" alt="">
