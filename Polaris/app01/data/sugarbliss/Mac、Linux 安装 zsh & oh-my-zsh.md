
--- 
title:  Mac、Linux 安装 zsh & oh-my-zsh 
tags: []
categories: [] 

---
shell 俗称壳，c 语言编写的命令解析器程序，是用户使用 linux 的桥梁。Linux/Unix 提供了很多种 Shell。常用的 Shell 有这么几种，sh、bash、csh 等。可以通过以下命令，查看系统有几种 shell：

```
$ cat /etc/shells

```

目前常用的 Linux 系统和 OS X 系统的默认 Shell 都是 bash。但是真正强大的 Shell 是深藏不露的 zsh，史称『终极 Shell』，由于与 bash 相似，功能又有所加强，zsh 在 Linux 社区获得了关注。但因配置过于复杂，所以初期无人问津。直到国外有个程序员开发出了一个能够快速上手的 zsh 项目，叫做「oh my zsh」，Github 网址是：https://github.com/robbyrussell/oh-my-zsh

## 安装使用 zsh&amp;ohmyzsh 的方法如下：

### 第一步：安装 zsh

一般系统中都有 zsh，不过我们仍需确认，下列命令根据自己系统选择（）

```
// Linux
$ sudo yum install zsh    (Fedora和RedHat以及SUSE中)或
$ sudo apt-get install zsh    (Debian系列，Ubuntu )
// macOS 系统自带了zsh, 一般不是最新版，如果需要最新版可通过Homebrew来安装(确认安装了Homebrew)
$ brew install zsh zsh-completions
// 或者也可以使用MacPorts(包管理工具)
$ sudo port install zsh zsh-completions

```

`rpm包和deb包`是两种 Linux 系统下最常见的安装包格式。rpm 包主要应用在 RedHat 系列包括 Fedora 等发行版的 Linux 系统上，deb 包主要应用于 Debian 系列包括现在比较流行的 Ubuntu 等发行版上。

`yum命令`是在 Fedora 和 RedHat 以及 SUSE 中基于 rpm 的软件包管理器，它可以使系统管理人员交互和自动化地更细与管理 RPM 软件包，能够从指定的服务器自动下载 RPM 包并且安装，可以自动处理依赖性关系，并且一次安装所有依赖的软体包，无须繁琐地一次次下载、安装。

`apt-get命令`是 Debian Linux 发行版中的 APT 软件包管理工具。所有基于 Debian 的发行都使用这个包管理系统。deb 包可以把一个应用的文件包在一起，大体就如同 Windows 上的安装文件。(<u><font color="#009a61"> 更多关于 apt 和 apt-get</font></u> )

### 第二步：更改默认 shell

```
$ echo $SHELL    //把zsh设为默认shell，如果shell列表中没有zsh或者你没有使用chsh权限的时候，不起作用
$ [sudo] chsh -s $(which zsh)  或 chsh -s /bin/zsh

```

关闭终端重新打开后生效

第三步：安装 oh my zsh

安装 oh my zsh 之前必须安装 zsh，否则会收到如下提示：Zsh is not installed! Please install zsh first!

```
#官网上的方法法，需要安装wget或者curl
$ sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
$ sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
#方法二：当然也可以通过git下载 
$ git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh

```

`wget`，Linux 命令，用来从指定的 URL 下载文件。mac 使用这个命令，需要安装。

`curl`，linux 命令，是一种命令行工具，作用是发出网络请求，然后得到和提取数据，显示在 “标准输出”（stdout）上面。它被广泛应用在 Unix、多种 Linux 发行版中，并且有 DOS 和 Win32、Win64 下的移植版本，已经是苹果机上内置的命令行工具之一了。

第三步：配置主题

Oh-My-Zsh 的默认配置文件在：~/.zshrc。编辑～/.zshrc 修改主题，这里我用的是 amuse 主题，更多主体看，直接修改即可，无需下载

```
vim ~/.zshrc

```

在 line 11

<img src="https://img-blog.csdnimg.cn/img_convert/bbd81881f651a1c8857ed34589ff9561.png" alt="image">

重启终端后有效或者使用 source ~/.zshrc 更新配置）

## oh-my-zsh神级插件

### autojump

**效果**

实现目录间快速跳转，想去哪个目录直接 j + 目录名，不用在频繁的 cd 了！ <img src="https://img-blog.csdnimg.cn/img_convert/2e4ec6afd459080f2caee8c4bdffe76c.png" alt="image"><img src="https://img-blog.csdnimg.cn/img_convert/1882b0c56802ab782d1bdbbaa10d0adc.png" alt="image">

**安装**

Mac 系统

```
$ brew install autojump

```

如果你是 linux 系统

```
$ git clone git://github.com/joelthelion/autojump.git

```

cd /autojump，执行

```
$ ./install.py

```

vim ~/.zshrc，把以下代码加到尾部

```
# 使用brew安装的
[[ -s $(brew --prefix)/etc/profile.d/autojump.sh ]] &amp;&amp; . $(brew --prefix)/etc/profile.d/autojump.sh
source $ZSH/oh-my-zsh.sh
# 使用git安装的
[[ -s ~/.autojump/etc/profile.d/autojump.sh ]] &amp;&amp; . ~/.autojump/etc/profile.d/autojump.sh

```

### zsh-autosuggestion

**效果**

如图所示，输入命令时可提示自动补全（灰色部分），然后按键盘 → 即可补全（）

<img src="https://img-blog.csdnimg.cn/img_convert/ac131c367bcc94701d2053de0ee8d758.png" alt="image">

**安装**

```
$ git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions

```

**修改提示词的颜色**

```
vim ~/.zshrc

```

在最后一行追加:

```
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=yellow'

```

使之生效：

```
source ~/.zshrc

```

支持一下几种颜色

```
black、red、green、yellow、blue、magenta、cyan、 white

```

**修改默认的快捷键补全方式**

例如，这将绑定 ctrl + space 表示接受当前建议。

```
bindkey '^ ' autosuggest-accept

```

同样也是追加到`vim ~/.zshrc`

使之生效：

```
source ~/.zshrc

```

支持以下几种模式：

`autosuggest-accept`：接受当前的建议。

`autosuggest-execute`：接受并执行当前的建议。

`autosuggest-clear`：清除当前建议。

`autosuggest-fetch`：获取建议（即使建议被禁用也能工作）。

`autosuggest-disable`：禁用建议。

`autosuggest-enable`：重新启用建议。

`autosuggest-toggle`：在启用/禁用建议之间切换。

我设置的是：

```
bindkey ',' autosuggest-execute

```

### zsh-syntax-highlighting

**效果**

日常用的命令会高亮显示，命令错误显示红色，如下图（）

<img src="https://img-blog.csdnimg.cn/img_convert/a7b3eb2cd42b90aeda091b717fa21234.png" alt="image">

**安装**

```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

```

先在配置文件.zshrc 的 plugins 中添加添加插件（可灵活更改）

<img src="https://img-blog.csdnimg.cn/img_convert/623b84423d346277947a9dc9273695ae.png" alt="image">

最后用 `source ~/.zshrc` 命令更新配置文件，重启终端即可使用，来面对你船新的 zsh 吧！

## Powerline

此时的oh-my-zsh主题显示应该不正常：

主要是因为，当前系统的字体不支持oh-my-zsh，需要Powerline字体。
- 如果你是MAC系统需要安装item2- 如果你是Windows系统，用xshell、SecureCRT等远程连接的linux系统，则需要在Windows系统上安装支持Powerline的字体
### Windows系统



下载后解压，右键安装即可。

#### 安装powerline字体

#### SeureCRT配置使用

**SecureCRT/ Options / Global Options/ Default Session / Edit Default Settings…/ Appearance/ Font**

点击 font ， 可以修改字体和字体大小；找到一 Powerline 结尾的字体就可以；

<img src="https://img-blog.csdnimg.cn/img_convert/d0d72bc6e85e5c8b8d04337f6ecb2d16.png" alt="image.png">

### MAC系统

#### 安装powerline字体

```
git clone https://github.com/powerline/fonts.git

```

进入fonts目录

```
cd fonts
./install.sh

```

删除fonts目录

```
cd ..
rm -rf fonts

```

#### iTerm2 配置使用

打开左上标签

**iTerm2 / Preference / Profiles / Text - font**

选择 change font ， 可以修改字体和字体大小；找到一 Powerline 结尾的字体就可以；

## <img src="https://img-blog.csdnimg.cn/img_convert/f7fdd539b640ff34f1c92c85199b3172.webp?x-oss-process=image/format,png" alt="image">

参考： https://www.zrahh.com/archives/118.html https://www.zrahh.com/archives/167.html
