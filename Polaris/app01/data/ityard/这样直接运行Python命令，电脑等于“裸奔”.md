
--- 
title:  这样直接运行Python命令，电脑等于“裸奔” 
tags: []
categories: [] 

---
👆点击关注｜设为星标｜干货速递👆

Python已经成为全球最受欢迎的编程语言之一。原因当然是Python简明易用的脚本语法，只需把一段程序放入.py文件中，就能快速运行。

而且Python语言很容易上手模块。比如你编写了一个模块my_lib.py，只需在调用这个模块的程序中加入一行import my_lib即可。

<img src="https://img-blog.csdnimg.cn/img_convert/a0b2d952ed885c1eb4cf022b68f02e51.png" alt="a0b2d952ed885c1eb4cf022b68f02e51.png">

这样设计的好处是，初学者能够非常方便地执行命令。但是对攻击者来说，这等于是为恶意程序大开后门。

尤其是一些初学者将网上的Python软件包、代码下载到本地~/Downloads文件夹后，就直接在此路径下运行python命令，这样做会给电脑带来极大的隐患。

**别再图方便了**

为何这样做会有危险？首先，我们要了解Python程序安全运行需要满足的三个条件：
- 系统路径上的每个条目都处于安全的位置；- “主脚本”所在的目录始终位于系统路径中；- 若python命令使用-c和-m选项，调用程序的目录也必须是安全的。
如果你运行的是正确安装的Python，那么Python安装目录和virtualenv之外唯一会自动添加到系统路径的位置，就是当前主程序的安装目录。

<img src="https://img-blog.csdnimg.cn/img_convert/a3ad03bc57d0910aa979e5cb8bef03b7.png" alt="a3ad03bc57d0910aa979e5cb8bef03b7.png">

这就是安全隐患的来源，下面用一个实例告诉你为什么。

如果你把pip安装在/usr/bin文件夹下，并运行pip命令。由于/usr/bin是系统路径，因此这是一个非常安全的地方。

但是，有些人并不喜欢直接使用pip，而是更喜欢调用/path/to/python -m pip。

这样做的好处是可以避免环境变量$PATH设置的复杂性，而且对于Windows用户来说，也可以避免处理安装各种exe脚本和文档。

所以问题就来了，如果你的下载文件中有一个叫做pip.py的文件，那么你将它将取代系统自带的pip，接管你的程序。

**下载文件夹并不安全**

比如你不是从PyPI，而是直接从网上直接下载了一个Python wheel文件。你很自然地输入以下命令来安装它：

```
~$ cd Downloads
~/Downloads$ python -m pip install ./totally-legit-package.whl
```

这似乎是一件很合理的事情。但你不知道的是，这么操作很有可能访问带有XSS JavaScript的站点，并将带有恶意软件的的pip.py到下载文件夹中。

下面是一个恶意攻击软件的演示实例：

```
~$ mkdir attacker_dir
~$ cd attacker_dir
~/attacker_dir$ echo 'print("lol ur pwnt")' &gt; pip.py
~/attacker_dir$ python -m pip install requests
lol ur pwnt
```

看到了吗？这段代码生成了一个pip.py，并且代替系统的pip接管了程序。

**设置$PYTHONPATH也不安全**

前面已经说过，Python只会调用系统路径、virtualenv虚拟环境路径以及当前主程序路径

你也许会说，那我手动设置一下 $PYTHONPATH 环境变量，不把当前目录放在环境变量里，这样不就安全了吗？

非也！不幸的是，你可能会遭遇另一种攻击方式。下面让我们模拟一个“脆弱的”Python程序：

```
# tool.py
try:
    import optional_extra
except ImportError:
    print("extra not found, that's fine")
```

然后创建2个目录：install_dir和attacker_dir。将上面的程序放在install_dir中。然后cd attacker_dir将复杂的恶意软件放在这里，并把它的名字改成tool.py调用的optional_extra模块：

```
# optional_extra.py
print("lol ur pwnt")
```

我们运行一下它：

```
~/attacker_dir$ python ../install_dir/tool.py
extra not found, that's fine
```

到这里还很好，没有出现任何问题。

但是这个习惯用法有一个严重的缺陷：第一次调用它时，如果$PYTHONPATH以前是空的或者未设置，那么它会包含一个空字符串，该字符串被解析为当前目录。

让我们再尝试一下：

```
~/attacker_dir$ export PYTHONPATH="/a/perfectly/safe/place:$PYTHONPATH";
~/attacker_dir$ python ../install_dir/tool.py
lol ur pwnt
```

看到了吗？恶意脚本接管了程序。

为了安全起见，你可能会认为，清空$PYTHONPATH总该没问题了吧？

Naive！还是不安全！

```
~/attacker_dir$ export PYTHONPATH="";
~/attacker_dir$ python ../install_dir/tool.py
lol ur pwnt
```

这里发生的事情是，$PYTHONPATH变成空的了，这和unset是不一样的。

因为在Python里，os.environ.get(“PYTHONPATH”) == “”和os.environ.get(“PYTHONPATH”) == None是不一样的。

如果要确保$PYTHONPATH已从shell中清除，则需要使用unset命令处理一遍，然后就正常了。

设置$PYTHONPATH曾经是设置Python开发环境的最常用方法。但你以后最好别再用它了，virtualenv可以更好地满足开发者需求。如果你过去设置了一个$PYTHONPATH，现在是很好的机会，把它删除了吧。

如果你确实需要在shell中使用PYTHONPATH，请用以下方法：

```
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}new_entry_1"
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}new_entry_2"
```

在bash和zsh中，$PYTHONPATH变量的值会变成：

```
$ echo "${PYTHONPATH}"
new_entry_1:new_entry_2
```

如此便保证了环境变量$PYTHONPATH中没有空格和多余的冒号。

如果你仍在使用$PYTHONPATH，请确保始终使用绝对路径！

另外，在下载文件夹中直接运行Jupyter Notebook也是一样危险的，比如jupyter notebook ~/Downloads/anything.ipynb也有可能将恶意程序引入到代码中。

**预防措施**

最后总结一下要点。

1、如果要在下载文件夹~/Downloads中使用Python编写的工具，请养成良好习惯，使用pip所在路径/path/to/venv/bin/pip，而不是输入/path/to/venv/bin/python -m pip。

2、避免将~/Downloads作为当前工作目录，并在启动之前将要使用的任何软件移至更合适的位置。

<img src="https://img-blog.csdnimg.cn/img_convert/678aed84fdee16df4bbdee977500866b.png" alt="678aed84fdee16df4bbdee977500866b.png">

了解Python从何处获取执行代码非常重要。赋予其他人执行任意Python命令的能力等同于赋予他对你电脑的完全控制权！

推荐阅读  点击标题可跳转
- - - - - - - - - 