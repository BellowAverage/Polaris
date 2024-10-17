
--- 
title:  Linux 使用 fish shell 
tags: []
categories: [] 

---
每个 Linux 管理员都可能听到过 shell 这个词。你知道什么是 shell 吗? 你知道 shell 在 Linux 中的作用是什么吗？ Linux 中有多少个 shell 可用？

shell 是一个程序，它是提供用户和内核之间交互的接口。

内核是 Linux 操作系统的核心，它管理用户和操作系统之间的所有内容。Shell 可供所有用户在启动终端时使用。终端启动后，用户可以运行任何可用的命令。当 shell 完成命令的执行时，你将在终端窗口上获取输出。

Bash（全称是 Bourne Again Shell）是运行在今天的大多数 Linux 发行版上的默认的 shell，它非常受欢迎，并具有很多功能。但今天我们将讨论 Fish Shell 。

#### 什么是 Fish Shell?

 是友好的交互式 shell ，是一个功能齐全，智能且对用户友好的 Linux 命令行 shell ，它带有一些在大多数 shell 中都不具备的方便功能。

这些功能包括自动补全建议、Sane Scripting、手册页补全、基于 Web 的配置器和 Glorious VGA Color 。你对它感到好奇并想测试它吗？如果是这样，请按照以下安装步骤继续安装。

#### 如何在 Linux 中安装 Fish Shell ？

它的安装非常简单，除了少数几个发行版外，它在大多数发行版中都没有。但是，可以使用以下  轻松安装。

对于基于 Arch Linux 的系统, 使用  来安装 fish shell。

```
sudo pacman -S fish
```

对于 Ubuntu 16.04/18.04 系统来说，请使用  或者  安装 fish shell。

```
sudo apt-add-repository ppa:fish-shell/release-3
sudo apt-get update
sudo apt-get install fish
```

对于 Fedora 系统来说，请使用  安装 fish shell。

```
sudo dnf install fish
```

对于 Debian 系统来说，请使用  或者  安装 fish shell。

```
apt-get install fish
```

对于 RHEL/CentOS 系统来说，请使用  安装 fish shell。

```
sudo yum install fish
```

当然有些系统你可能没法直接 yum install fish，这个时候你可以下载相应的 repo 或者安装  epel-release 之类的扩展仓，再进行 yum install fish 即可正常安装上了。

```
cd /etc/yum.repos.d/
wget https://download.opensuse.org/repositories/shells:fish:release:2/CentOS_7/shells:fish:release:2.repo
yum install fish
```

 安装示例（以 centos7 为例）：

```
[root@master ~]# yum install fish
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
epel/x86_64/metalink                                                                                          | 3.7 kB  00:00:00     
 * base: mirrors.aliyun.com
 * epel: mirrors.bfsu.edu.cn
 * extras: mirrors.aliyun.com
 * updates: mirrors.aliyun.com
base                                                                                                          | 3.6 kB  00:00:00     
docker-ce-stable                                                                                              | 3.5 kB  00:00:00     
epel                                                                                                          | 4.7 kB  00:00:00     
extras                                                                                                        | 2.9 kB  00:00:00     
updates    

...

Total                                                                                                2.2 MB/s | 1.6 MB  00:00:00     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : bc-1.06.95-13.el7.x86_64                                                                                          1/2 
  Installing : fish-2.3.1-2.el7.x86_64                                                                                           2/2 
  Verifying  : fish-2.3.1-2.el7.x86_64                                                                                           1/2 
  Verifying  : bc-1.06.95-13.el7.x86_64                                                                                          2/2 

Installed:
  fish.x86_64 0:2.3.1-2.el7                                                                                                          

Dependency Installed:
  bc.x86_64 0:1.06.95-13.el7                                                                                                         

Complete!

```

#### 如何使用 Fish Shell ？

一旦你成功安装了 fish shell 。只需在你的终端上输入 `fish` ，它将自动从默认的 bash shell 切换到 fish shell 。

```
[root@master ~]# fish
Welcome to fish, the friendly interactive shell
Type help for instructions on how to use fish
root@master ~# 

```

#### 自动补全建议

当你在 fish shell 中键入任何命令时，它会在输入几个字母后以浅灰色自动建议一个命令。

<img alt="" height="94" src="https://img-blog.csdnimg.cn/20210413161218372.png" width="535">

一旦你得到一个建议然后按下向右光标键就能完成它而不是输入完整的命令。

<img alt="" height="80" src="https://img-blog.csdnimg.cn/20210413161345216.png" width="685">

你可以在键入几个字母后立即按下向上光标键检索该命令以前的历史记录。它类似于 bash shell 的 `CTRL+r` 选项。

#### 通过关键字查找历史命令

这个是我一直心心念念的功能，比如说你很久之前输入了一个比较长的命令：

```
rpm -qpR pkgship-2.1.0-7.oe1.noarch.rpm
```

当你想再次找到这个命令时，你可以先输入 rpm ，然后再继续按 ↑，它就会自动把与 rpm 相关的命令给你找出来（bash 中就只能按照 history 历史一个个去翻了）。

<img alt="" height="37" src="https://img-blog.csdnimg.cn/20210413165828324.png" width="584">

**如果它阴影部分提示的命令就是你想要输入的，可以直接用 → 将提示部分直接补全：**

<img alt="" height="31" src="https://img-blog.csdnimg.cn/20210422165519761.png" width="547">

<img alt="" height="29" src="https://img-blog.csdnimg.cn/20210422165555964.png" width="552">

#### Tab 补全

如果你想查看给定命令是否还有其他可能性，那么在键入几个字母后，只需按一下 `Tab` 键即可。

<img alt="" height="92" src="https://img-blog.csdnimg.cn/202104131614487.png" width="773">

再次按 `Tab` 键可查看完整列表并从第一个选项开始轮选。

<img alt="" height="72" src="https://img-blog.csdnimg.cn/20210413161539127.png" width="777">

<img alt="" height="75" src="https://img-blog.csdnimg.cn/20210413161619476.png" width="764">

#### 语法高亮

fish 会进行语法高亮显示，你可以在终端中键入任何命令时看到。无效的命令被着色为 `RED color` 。

<img alt="" height="36" src="https://img-blog.csdnimg.cn/20210413163701650.png" width="426">

<img alt="" height="31" src="https://img-blog.csdnimg.cn/20210413163715997.png" width="425">

同样的，有效的命令以不同的颜色显示。此外，当你键入有效的文件路径时，fish 会在其下面加下划线，如果路径无效，则不会显示下划线。

<img alt="" height="37" src="https://img-blog.csdnimg.cn/20210413163752166.png" width="552">

<img alt="" height="31" src="https://img-blog.csdnimg.cn/20210413163804944.png" width="552">

#### 如何将 Fish 设置为默认 shell

如果你想测试 fish shell 一段时间，你可以将 fish shell 设置为默认 shell，而不用每次都切换它。

要这样做，首先使用以下命令获取 Fish Shell 的位置。

```
root@master ~# whereis fish
fish: /usr/bin/fish /etc/fish /usr/share/fish /usr/share/man/man1/fish.1.gz

```

通过运行以下命令将默认 shell 更改为 fish shell 。

```
root@master ~# chsh -s /usr/bin/fish
Changing shell for root.
Shell changed.

```

提示：只需验证 Fish Shell 是否已添加到 `/etc/shells` 目录中。如果不是，则运行以下命令以附加它。

```
root@master ~# echo /usr/bin/fish | sudo tee -a /etc/shells
/usr/bin/fish
```

完成测试后，如果要返回 bash shell ，请使用以下命令。

暂时返回：

```
bash
```

永久返回：

```
chsh -s /bin/bash
```

注意：因为与 bash 兼容性的问题，建议还是不要把  fish 设置为默认 shell (有部分 bash 支持的语法 fish 可能不支持)，你可以在需要使用的用 fish 进入 fish shell，不用的话 exit 退出到默认 shell。
