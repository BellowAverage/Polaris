
--- 
title:  保姆级教程！将 Vim 打造一个 IDE （Python 篇） 
tags: []
categories: [] 

---
从上周开始我就开始折腾 ，搞了一下 Vim IDE for Python &amp; Go，我将整个搭建的过程整理成本篇文章分享出来，本篇是 Python 版本的保姆级教程，实际上我还写了 Go 版本的，有想看的可以本篇文章点个赞，我下篇就发

<img src="https://img-blog.csdnimg.cn/20211027082428650.png" alt="效果图">

一说到 IDE，总有人会因 which one is 世界上最好的编辑工具 而吵得不可开交，但本文不会涉及、也不想误导大家，我相信不同的人、不同的使用场景都有着有不同的最优解，世界上没有一招通吃的编辑器。

如果是在桌面端，PyCharm 和 VS Code 已经做得足够优秀，很难再有第三个编辑器可以与之匹敌。

<img src="https://img-blog.csdnimg.cn/20211027082430523.png" alt="">

但若要说在服务端？似乎没得选，Vim 几乎是你唯一的选择。

Vim 是极具生产力的工具，甚至在某些人的眼中，它是一个魔鬼般的编辑器，之所以这么说，是因为它的上手门槛极高，学习曲线非常的陡。

一是，它是针对程序员群体的专有编译器，你需要额外学习并理解它的设计理念，并且需要记住非常多复杂的操作指令。

二是，对于工程项目代码，它并不是一个开箱即用的编辑器，需要你安装大量的插件、进行大量的配置才能成为一个称手的 IDE 工具。

之所以，我使用 Vim 作为开发的工具，原因有四：
1. **直接**：正常本地 IDE 编码完后，要上传远程服务端进行编译及测试，比较麻烦，我直接在 SSH 服务端进行编码更为直接。1. **省心**：多种语言不用再安装多个专有的编辑器，比如 PyCharm、Goland 等，而且不用再为各种付费软件破解劳心费力。1. **方便**：提高 iPad 的生产力，外出不带电脑也可以在线写代码，省得每次都带个重重的电脑。1. **装逼**：你不觉得挺酷的吗？（逃...
如果你对 Vim 操作一无所知，那么请先去了解一下 Vim 的日常使用方法，否则以下内容并不适合你。

### 1. 准备工作

本文是在 Mac 环境下进行操作演示的，但同样适用于 Linux 环境（少许差异，我会在相应位置点出），如果你只有 Windows 系统，可以使用 GVim。

在开始安装配置之前，先说一下本文的一个整体思路：
1. 准备运行环境：安装 Python 或者 Go 环境1. 准备Vim 版本：使用 Vim 8.2 的最高版本1. 插件安装环境：插件都在 Github 及其他外网，需要你配置一些代理1. 插件安装：一键批量安装插件1. 插件配置：插件安装上后，要进行一些配置才能好用1. 插件使用：演示每个插件的使用方法
### 2. 准备运行环境

Vim 原生对 Python 提供了支持，当你安装 8.2 版本的 Vim 时，会自动安装 Python ，只不过该安装版本并不是你需要的版本，不过不要紧，Vim 运行使用的 Python 版本是可以配置的。

我这边使用的版本是 Python 3.10.0

```
$ python3 --version
Python 3.10.0
```

### 3. 安装/升级 Vim 8.2

正常的 Mac 或者 Linux 机器都会自带 Vim 工具，只不过可能版本比较低，如果使用这些版本的 Vim ，后面有些插件会安装不上或者使用不了，就比如 `YouCompleteMe` 这个非常重要的插件，如果你不使用 Vim 8.1+ ，你每次用 vim 都会提示你，非常影响体验

```
$ vim main.go
YouCompleteMe unavailable: requires Vim 8.1.2269+.
Press ENTER or type command to continue
```

这些插件已经持续更新了很多年，对于老版的 Vim 不再提供支持这也可以理解。

如果你使用的 Linux ，整个过程会顺畅很多，在这里我使用的是 CentOS 7.6 的 Linux。

首先找到系统里安装的 vim 包有哪些，然后使用 `yum remove` 去卸载它

```
[root@iswbm ~]# yum list installed | grep -i vim
vim-common.x86_64                       2:7.4.629-8.el7_9              @updates
vim-enhanced.x86_64                     2:7.4.629-8.el7_9              @updates
vim-filesystem.x86_64                   2:7.4.629-8.el7_9              @updates
vim-minimal.x86_64                      2:7.4.629-8.el7_9              @updates
[root@iswbm ~]#
[root@iswbm ~]# yum remove vim-common vim-enhanced vim-filesystem vim-minimal
```

后面我会使用源码编译的方法去安装 Vim 8.2，但编译需要安装如下这些基础依赖

```
[root@iswbm ~]# yum install -y gcc make ncurses ncurses-devel
[root@iswbm ~]# yum install ctags git tcl-devel \
    ruby ruby-devel \
    lua lua-devel \
    luajit luajit-devel \
    python python-devel \
    perl perl-devel \
    perl-ExtUtils-ParseXS \
    perl-ExtUtils-XSpp \
    perl-ExtUtils-CBuilder \
    perl-ExtUtils-Embed
```

从 Github 上下载源代码

```
git clone https://github.com/vim/vim.git
```

进入 `vim/src` 目录执行如下三个命令编译安装

```
[root@iswbm ~]# ./configure --prefix=/usr/local/vim \
--enable-pythoninterp=yes \
--enable-python3interp=yes \
--with-python-command=python \
--with-python3-command=python3
[root@iswbm ~]# make &amp;&amp; make install
[root@iswbm ~]# 
```

不出意外的话，命令执行完成后，你只要再配置个软件链接，就可以正常使用 8.2 版本的 Vim 了。

```
[root@iswbm ~]# ln -s /usr/local/vim/bin/vim /usr/bin/vim
[root@iswbm src]# vim --version | head -n 1
VIM - Vi IMproved 8.2 (2019 Dec 12, compiled Oct 19 2021 22:05:46)
```

### 4. 插件安装

Vim 本身提高的功能已经非常强大，但无奈上手难度实在太大，安装一些定制化的插件，能让整个 Vim 界面管理与使用更加符合人类的直觉，降低使用门槛。

具体要安装哪些插件，还要是看你想把 Vim 打造成什么样子？

这个倒不必闷着头空想，对照着桌面端的 IDE 软件去抄作业就 OK 了嘛。

对于我个人来说，我日常使用 IDE 最多的功能有：
- 自动代码补全- 代码追踪跳转- 静态代码检查- 运行调试代码- 全局搜索代码- 项目代码书签- 代码版本管理- 代码高亮显示- 工程项目的文件树- 单文件代码结构树- 可同时打开多文件- Markdown 实时预览
那我就对照这个功能去找对应的插件即可
- **YouCompleteMe**：提供自动代码补全与代码追踪跳转- **auto-pairs**：自动补全括号的插件，包括小括号，中括号，以及花括号- **NERDTree**：提供工程项目的文件树、支持书签功能- **vim-nerdtree-tabs**：可以打开多个代码文件，使 nerdtree 的 tab 更加友好些- **nerdtree-git-plugin**：可以在导航目录中看到 git 版本信息- **tagbar**：可以查看当前代码文件中的变量和函数列表的插件，并切换和跳转到代码中对应的变量和函数的位置- **vim-airline**：Vim状态栏插件，包括显示行号，列号，文件类型，文件名，以及Git状态- **vim-gitgutter**：可以在文档中显示 git 信息- **vim-one**：代码配色方案- **markdown-preview.vim**：Markdown 预览支持- **mathjax-support-for-mkdp**：Markdown 数学公式预览支持- **vim-godef**：go 中的代码追踪，输入 gd 就可以自动跳转- **fatih/vim-go**：静态检查等一系列 go 相关工具- **ultisnips** / **vim-snippets**：自动生成 代码块
那么如何安装这些插件呢？

很简单，你只要使用 vi 在你的 `~/.vimrc` 文件中，贴入下面这段配置到文件末尾

```
" 插件开始的位置
call plug#begin('~/.vim/plugged')

" 代码自动完成，安装完插件还需要额外配置才可以使用
Plug 'ycm-core/YouCompleteMe'

" 用来提供一个导航目录的侧边栏
Plug 'scrooloose/nerdtree'

" 可以使 nerdtree 的 tab 更加友好些
Plug 'jistr/vim-nerdtree-tabs'

" 可以在导航目录中看到 git 版本信息
" Plug 'Xuyuanp/nerdtree-git-plugin'

" 查看当前代码文件中的变量和函数列表的插件，
" 可以切换和跳转到代码中对应的变量和函数的位置
" 大纲式导航, Go 需要 https://github.com/jstemmer/gotags 支持
Plug 'preservim/tagbar'

" 自动补全括号的插件，包括小括号，中括号，以及花括号
Plug 'jiangmiao/auto-pairs'

" Vim状态栏插件，包括显示行号，列号，文件类型，文件名，以及Git状态
Plug 'vim-airline/vim-airline'

" Shorthand notation; fetches https://github.com/junegunn/vim-easy-align
" 可以快速对齐的插件
Plug 'junegunn/vim-easy-align'

" 可以在文档中显示 git 信息
Plug 'airblade/vim-gitgutter'

" markdown 插件
Plug 'iamcco/mathjax-support-for-mkdp'
Plug 'iamcco/markdown-preview.vim'

" 下面两个插件要配合使用，可以自动生成代码块
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'

" go 主要插件
Plug 'fatih/vim-go', { 'tag': '*' }

" go 中的代码追踪，输入 gd 就可以自动跳转
Plug 'dgryski/vim-godef'

" 可以在 vim 中使用 tab 补全
"Plug 'vim-scripts/SuperTab'

" 可以在 vim 中自动完成
"Plug 'Shougo/neocomplete.vim'


" 插件结束的位置，插件全部放在此行上面
call plug#end()
```

然后输入命令 `:wq` 保存并退出 vi。

安装插件的管理工具有很多，比如 Vundle，vim-plug 等。

Vundle是一款非常出名且历史悠久的Vim插件管理工具。但随着安装的vim插件越来越多，使用Vundle来管理这些插件时效率变得越来越低，vim启动耗时也越来越大。

而vim-plug是一款非常轻量又高效的vim插件管理工具。它支持全异步、多线程并行安装插件，支持git分支、标签等，可以对插件进行回滚更新、还支持按需加载插件(On-demand loading)，可以指定对特定文件类型加载对应vim插件，大大加快了vim启动时间。

因此我这里会使用 vim-plug 这个管理工具，使用如下命令就可以安装 `vim-plug` 插件管理工具

```
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

接着请重启一下你的终端，保证重新初始化，不然等你后面执行 `PlugInstall` 的时候， 有可能报该命令不存在。

```
Not an editor command: PlugInstall
```

重启完终端后，输入再次打开 `vim` 输入 `:PlugInstall` 开始安装过程

<img src="https://img-blog.csdnimg.cn/20211027082431644.png" alt="">

如果你没有网络问题（不就科学那点事嘛），那么安装会很顺利。。

输入 `:PlugStatus` 就会看到所有的插件都安装 OK。

<img src="https://img-blog.csdnimg.cn/20211027082431967.png" alt="">

### 5. YouCompleteMe

上面的插件安装，其实做的事情也比较简单，就是把 Github 上的仓库拉取到本地的 `~/.vim/plugged` 目录

<img src="https://img-blog.csdnimg.cn/20211027082433267.png" alt="">

一般情况下，这些插件都是开箱即用的，不会有复杂的依赖，但唯独一个插件比较特殊 ，它就是 `YouCompleteMe` ，它号称是最难安装的 Vim 插件。

我在本地的 Mac 机器上装了两个晚上，才算把所有的依赖都解决完成，但在 Linux 上就比较顺利。

具体的安装步骤是
1. 进入 `~/.vim/plugged/YouCompleteMe` 插件目录，修改 `.gitmodules` 中的 github.com 为 镜像网站 hub.fastgit.org1. 然后安装一级依赖：`git submodule update --init`1. 一级依赖正确安装后，再修改 `third_party/ycmd` 目录下所有依赖的`.gitmodules` 中的 github.com 为 镜像网站 hub.fastgit.org1. 然后递归安装其依赖包：`git submodule update --init --recursive`1. 最后执行 `python3 install.py --all` ，--all 会安装该插件支持的所有语言功能。
在 Mac 上安装的过程中，遇到了相当多的问题，还涉及到了改 YouComplete 的代码，最后才得以正常安装下去，可能你在安装的过程中也会遇到类似的问题，如果有问题，欢迎在评论区留言，我会尽力解答。

### 6. 设置镜像代理

上面安装插件的过程其实会去 Github 上下载对应的插件，但由于各种不可描述的原因， 在大陆的服务器上访问 github 是非常慢，甚至是不能访问的。

我在没有进行任何网络设置的情况下， 20 个插件，居然没有一个安装成功。

因此在这里，你得先想办法，让你的服务器能访问以正常速度访问 Github，至于怎么做，有些黑科技我这里不方便展开细说，就给大家介绍一种可以公开、又非常有效的方法。

修改 `~/.vim/autoload/plug.vim` 将

```
let fmt = get(g:, 'plug_url_format', 'https://git::@github.com/%s.git')
```

改成

```
let fmt = get(g:, 'plug_url_format', 'https://git::@hub.fastgit.org/%s.git')
```

将这行

```
\ '^https://git::@github\.com', 'https://github.com', '')
```

改成

```
\ '^https://git::@hub.fastgit\.org', 'https://hub.fastgit.org', '')
```

然后再进入 vim 执行 `:PlugInstall` 就可以了

### 7. 插件使用

大部分插件安装好后，可以立马使用，但有一些插件需要再进行一些配置才能用得更称手。

由于配置非常多，我这里就不直接贴出来了，有感兴趣的加我v：hello-wbm，找我要一下配置表。

**YouComplete**

使用 IDE 最基本的诉求，不就是能够在你编码的时候，自动给出提示，然后自动补全嘛，vim 有了 YouComplete 的加持后，也可以 100% 还原桌面端的编码体验。

<img src="https://img-blog.csdnimg.cn/20211027082444489.png" alt="">

**NERDTree**

打开文件后，使用 F9 或者输入 `NERDTreeToggle` 就会打开侧边栏的文件树，这是 `NERDTree` 给我们提供的便利。

<img src="https://img-blog.csdnimg.cn/20211027082456297.png" alt="">

**tagbar**

打开 Python 文件后，使用 F9 或者输入 `:tagbar` 就可以打开 `tagbar` 窗口，在这个窗口里你可以看到该文件的所有结构体、函数、变量等，这些通通可以称做 tag，当你定位到某个 tag 时，直接回车就可以跳转到左边代码窗口的位置。

<img src="http://image.iswbm.com/20211025124607.gif" alt="">

**vimgrep**

vimgrep 可用于工程项目的代码查找，对于经常阅读源代码的同学是必不可少的利器，它是 Vim 自带的工具，非常之强大。

用完 vimgrep 查找后，正常情况下，不会有任何的反馈，如果你需要查看搜索的结果，并跳转到对应的位置，可以使用 QuickFix ，只要输入 `:cw` 或者 `:copen`

<img src="https://img-blog.csdnimg.cn/2021102708253879.png" alt="">

### 8. 运行代码

使用 Vim 写完代码后，想像 PyCharm 一样直接快捷键运行代码，需要你在 `.vimrc` 中写入如下的配置。

这段配置，不仅包括 Python ，还有 Bash 和 Golang

```
" F5 to run sh/python3
map &lt;F5&gt; :call CompileRunGcc()&lt;CR&gt;
func! CompileRunGcc()
    exec "w"
    if &amp;filetype == 'sh'
        :!time bash %
    elseif &amp;filetype == 'python'
        exec "!time python3 %"
    elseif &amp;filetype == 'go'
        exec "!time go run %"
    endif
endfunc
```

配置完后，使用 `F5` 就可以直接运行当前的脚本。

<img src="https://img-blog.csdnimg.cn/20211027082539253.png" alt="">

### 9. 在 iPad 上写代码

如果你和我一样，有自己的服务器，那么你根据上面的步骤把 Vim 配置好后，就可以在 iPad 上通过 SSH 连接服务器进行代码的编写了。

如果你没有服务器，只要可以加我v: hello-wbm，我就送你一台一年期的阿里云服务器，名额有限，我只能说先到先得。

刚好我手上有一台 2020 款的 iPad Pro，平时也是用来视频居多，实在有点对不起 Pro 这个配置，有了 Vim 这个神器，生产力 up 了一点点。。

<img src="https://img-blog.csdnimg.cn/20211027082542135.png" alt="">

### 10. 写在最后

有必要说明一下，之所以花了五天这么长的时间，其实我是把我手上的几台电脑，包括服务器全部配置了 Vim IDE，不同的机器，遇到的问题都有点不太一样，其中在我的 Mac 上，遇到的问题最多，折腾的时间最长，其中有些问题，我 Google 不到答案，最后是看了代码，修改了部分代码才跑下去的。

另外，对于 Vim 来说，最重要的就是 .vimrc 文件，上面的讲解可能我会漏了一些配置讲解，如果你发现使用不是那么顺利，可以下载我的 .vimrc 文件：

本文是 Python 版本的 Vim IDE 搭建指南，代码演示也基本是用的是 Python 代码，根据文中我的思路一步一步操作，你可以搭建属于自己的一套在线 IDE 环境。

我不仅写 Python 代码，还写一些 Go 的代码， Vim 对于 Python 原生提供了比较多的支持，而相比之下，Go 却要安装更多的插件才能达到不错的编码体验，但由于本号大多数是 Python 开发者，这一部分内容，我会再写一篇 Vim for Go 的文章。感兴趣的朋友给我可以给我评论区说一下，我会发给你地址。 

好了，以上就是本篇文章的全部内容，如在安装配置上有任何疑问，欢迎评论区指出~

原文首发于个人博客：

### 文章的最后，插播一个福利

双十一快到了，阿里云也开始搞活动了，刚好我这边可以带大家白Piao 阿里云的服务器。

说白了就是大家 可以一分钱不花，就可以领到服务器，规格是 2c2m（2vcpu 2G memory） 的机器。

昨天在朋友圈发了下，现在已经有 400 人报名参与了，今天借这篇文章再说一下，有想参加的朋友，可以加我v（hello-wbm），带大家一起薅羊毛。

### 絮叨一下

我在 CSDN 上写过很多的 Python 相关文章，其中包括 Python 实用工具，Python 高效技巧，PyCharm 使用技巧，很高兴得到了很多知乎朋友的认可和支持。

在他们的鼓励之下，我将过往文章分门别类整理成三本 PDF 电子书

**PyCharm 中文指南**

《PyCharm 中文指南》使用 300 多张 GIF 动态图的形式，详细讲解了最贴合实际开发的 105个 PyCharm 高效使用技巧，内容通俗易懂，适合所有 Python 开发者。

在线体验地址：

<img src="https://img-blog.csdnimg.cn/20211027082542629.png" alt="">

**Python 黑魔法指南**

《Python黑魔法指南》目前迎来了 v3.0 的版本，囊集了 100 多个开发小技巧，非常适合在闲时进行碎片阅读。

在线体验地址：

<img src="https://img-blog.csdnimg.cn/20211027082542845.png" alt="">

**Python 中文指南**

学 Python 最好的学习资料永远是 Python 官方文档，可惜现在的官方文档大都是英文，虽然有中文的翻译版了，但是进度实在堪忧。为了照顾英文不好的同学，我自己写了一份 面向零基础的朋友 的在线 Python 文档 -- 《Python中文指南》

在线体验地址：

<img src="https://img-blog.csdnimg.cn/20211027082543292.png" alt="">

**有帮助的话，记得帮我**  **点个赞哟~**
