
--- 
title:  Linux 之 zsh 
tags: []
categories: [] 

---
### 安装

#### zsh 安装

现在好多 linux 发行版好像都自带 zsh 的，比如说 centos。

```
[root@master ~]# chsh -l
/bin/sh
/bin/bash
/usr/bin/sh
/usr/bin/bash
/usr/bin/tmux
/bin/zsh
/usr/bin/fish

```

如果实在没有的话，就用 yum 安装一个。

```
yum install zsh
```

如果直接切换到 zsh 的话，看起来和默认 bash 好像没太大区别。

```
[root@master ~]# chsh 
Changing shell for root.
New shell [/bin/bash]: /bin/zsh
Shell changed.

```

一般来说，是要配合现在很流行的 oh my zsh 来使用的。

#### oh my zsh 安装

```
[root@master]~# git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh 
Cloning into '/root/.oh-my-zsh'...
remote: Enumerating objects: 26567, done.
remote: Counting objects: 100% (188/188), done.
remote: Compressing objects: 100% (99/99), done.
remote: Total 26567 (delta 97), reused 166 (delta 88), pack-reused 26379
Receiving objects: 100% (26567/26567), 7.76 MiB | 61.00 KiB/s, done.
Resolving deltas: 100% (13325/13325), done.

[root@master]~# cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```

### 使用

再次连接的话，就是下面这种的了。

```
Connecting to 192.168.128.139:22...
Connection established.
To escape to local shell, press 'Ctrl+Alt+]'.

WARNING! The remote SSH server rejected X11 forwarding request.
Last login: Tue Aug 24 11:14:39 2021 from 192.168.128.1

➜  ~ 
➜  ~ cd insight-tool
➜  insight-tool git:(master) ✗ 
```

如果你想下次连接的时候使用默认的 bash 的话，就用 chsh 切换回去就好了。

```
➜  insight-tool git:(master) ✗ chsh -s /bin/bash
Changing shell for root.
Shell changed.

```

 如果你想立即马上切换回 bash 的话，直接输入 bash 就好了。

```
➜  ~ bash
[root@master ~]# 

```

如果还有安装其他的 shell， 任意切换也没有任何问题。

```
[root@master ~]# fish
Welcome to fish, the friendly interactive shell
Type help for instructions on how to use fish
root@master ~# zsh
➜  ~ bash
[root@master ~]# 

```

### 配置

```
➜  ~ vim .zshrc
```

家目录下的这个 .zshrc 就是 zsh 的配置文件了，像主题，插件之类的就需要在里边进行配置。

其实还有个 .zsh_history ，记录了你在 zsh 下各种操作的历史记录，类似于下面这种的。前面那个大数字大家肯定很容易猜到是啥。

```
➜  ~ vim .zsh_history

...
: 1629789654:0;vim .zshrc
: 1629789748:0;vim .zsh_history

```

```
&gt;&gt;&gt; 1629789748 / 365 / 24 / 60 / 60
51.680293886352096

```

对，没错，稍微转换一下就容易发现：就是当前的时刻到 1970 年经历过的秒数。

#### 主题

默认的主题时 robbyrussell，通过注释也可以看出，如果你设置主题为 ”random" 的话，每次进入 zsh 的时候它就会随机帮你选一个主题。

```
➜  ~ vim .zshrc

# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="robbyrussell"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

```

为了体验一下，完全可以尝试一下。

```
ZSH_THEME="random"
```

```
[root@master ~]# zsh
[oh-my-zsh] Random theme 'kphoen' loaded
[root@master:~]
# bash
[root@master ~]# zsh
~ ➤  Random theme 'arrow' loaded
~ ➤  bash                                                                                                   
[root@master ~]# zsh
/root/.oh-my-zsh/themes/emotty.zsh-theme:49: command not found: emotty
[oh-my-zsh] Random theme 'emotty' loaded
root@master  bash                                                                                                 ~
[root@master ~]# zsh
[oh-my-zsh] Random theme 'wuffers' loaded
{} ~ 

```

它所有的主题都存放在 oh-my-zsh 项目 themes 目录下的：

```
➜  themes git:(master) ls | head -n 10
3den.zsh-theme
adben.zsh-theme
af-magic.zsh-theme
afowler.zsh-theme
agnoster.zsh-theme
alanpeabody.zsh-theme
amuse.zsh-theme
apple.zsh-theme
arrow.zsh-theme
aussiegeek.zsh-theme

```

如果你想查看所有主题的效果，请转到这个链接：

#### 插件

插件也是在 .zshrc 这个文件里设置的，默认只配置了 git，可以自行添加。

```
➜  ~ vim .zshrc

# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git osx autojump)

source $ZSH/oh-my-zsh.sh

```

比如说添加 git 插件后，当你处于一个 git 受控的目录下时，Shell 会明确显示 「git」和 branch，如上图所示，另外对 git 很多命令进行了简化，例如 gco=’git checkout’、gd=’git diff’、gst=’git status’、g=’git’等等，熟练使用可以大大减少 git 的命令长度。

相关的插件文件在 ~/.oh-my-zsh/plugins 目录下，默认提供了几百种。

```
➜  plugins git:(master) pwd
/root/.oh-my-zsh/plugins
➜  plugins git:(master) ls | wc
    301     301    2379

```

每个插件都有相应的 README.md 说明文档，可以自行了解插件的功能和用法。

```
➜  plugins git:(master) cd git
➜  git git:(master) ll
total 44K
-rw-r--r--. 1 root root 9.4K Aug 24 11:13 git.plugin.zsh
-rw-r--r--. 1 root root  31K Aug 24 11:13 README.md
```

我大概看了几个，大部分主要时设置常用命令的别名，用户就可以不用输入全称了，比如 yum 的这个插件。

```
➜  yum git:(master) pwd
/root/.oh-my-zsh/plugins/yum
➜  yum git:(master) ll
total 8.0K
-rw-r--r--. 1 root root 1.4K Aug 24 11:13 README.md
-rw-r--r--. 1 root root  864 Aug 24 11:13 yum.plugin.zsh
➜  yum git:(master) vim README.md 
# Yum plugin

This plugin adds useful aliases for common [Yum](http://yum.baseurl.org/) commands.

To use it, add `yum` to the plugins array in your zshrc file:

```zsh
plugins=(... yum)
```

## Aliases

| Alias | Command                           | Description                  |
|-------|-----------------------------------|------------------------------|
| ys    | `yum search`                      | Search package               |
| yp    | `yum info`                        | Show package info            |
| yl    | `yum list`                        | List packages                |
| ygl   | `yum grouplist`                   | List package groups          |
| yli   | `yum list installed`              | Print all installed packages |
| ymc   | `yum makecache`                   | Rebuild the yum package list |
| yu    | `sudo yum update`                 | Upgrade packages             |
| yi    | `sudo yum install`                | Install package              |
| ygi   | `sudo yum groupinstall`           | Install package group        |
| yr    | `sudo yum remove`                 | Remove package               |
| ygr   | `sudo yum groupremove`            | Remove pagage group          |
| yrl   | `sudo yum remove --remove-leaves` | Remove package and leaves    |
| yc    | `sudo yum clean all`              | Clean yum cache              |

```


