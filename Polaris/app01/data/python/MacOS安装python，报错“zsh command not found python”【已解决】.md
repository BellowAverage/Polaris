
--- 
title:  MacOS安装python，报错“zsh: command not found: python”【已解决】 
tags: []
categories: [] 

---
## 1. 问题

homebrew用以下命令安装python

```
brew install python3
```

然后用以下命令查看python安装版本

```
python --version

```

会出现报错：

>  
 **zsh: command not found: python** 


##  2. 解决方法

### 2.1 将python添加到zsh

添加`python`到 zsh 以便它在键入`python`命令时运行。可以通过在终端中运行以下命令来做到这一点：

```
echo "alias python=/usr/bin/python3" &gt;&gt; ~/.zshrc
```

>  
 这会将您的 zsh 配置文件配置为在运行`/usr/bin/python3`时`python`运行。如果您仍然遇到问题，请确保`python=$ `$ 符号应该等于`python`安装路径的位置 


### 2.2 重启终端

或者输入以下命令：

```
source ~/.zshrc
```

这时，`python`命令应该可以成功运行。

>  
  ~&gt; python --version                                                                                     Python 3.8.9 


 参考链接：
