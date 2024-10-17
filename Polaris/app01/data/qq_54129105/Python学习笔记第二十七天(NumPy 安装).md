
--- 
title:  Python学习笔记第二十七天(NumPy 安装) 
tags: []
categories: [] 

---


#### Python学习笔记第二十七天
- - - - - <ul><li>- - 


## NumPy 安装

Python 官网上的发行版是不包含 NumPy 模块的。

我们可以使用以下几种方法来安装。

## 使用已有的发行版本

对于许多用户，尤其是在 Windows 上，最简单的方法是下载以下的 Python 发行版，它们包含了所有的关键包（包括 NumPy，SciPy，matplotlib，IPython，SymPy 以及 Python 核心自带的其它包）：
- Anaconda: 免费 Python 发行版，用于进行大规模数据处理、预测分析，和科学计算，致力于简化包的管理和部署。支持 Linux, Windows 和 Mac 系统。- Enthought Canopy: 提供了免费和商业发行版。持 Linux, Windows 和 Mac 系统。- Python(x,y): 免费的 Python 发行版，包含了完整的 Python 语言开发包 及 - Spyder IDE。支持 Windows，仅限 Python 2 版本。- WinPython: 另一个免费的 Python 发行版，包含科学计算包与 Spyder IDE。支持 Windows。- Pyzo: 基于 Anaconda 的免费发行版本及 IEP 的交互开发环境，超轻量级。 支持 Linux, Windows 和 Mac 系统。
## 使用 pip 安装

安装 NumPy 最简单的方法就是使用 pip 工具：

pip3 install --user numpy scipy matplotlib –user 选项可以设置只安装在当前的用户下，而不是写入到系统目录。

默认情况使用国外线路，国外太慢，我们使用清华的镜像就可以:

pip3 install numpy scipy matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple

## Linux 下安装

### Ubuntu &amp; Debian

```
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

```

### CentOS/Fedora

```
sudo dnf install numpy scipy python-matplotlib ipython python-pandas sympy python-nose atlas-devel

```

### Mac 系统

Mac 系统的 Homebrew 不包含 NumPy 或其他一些科学计算包，所以可以使用以下方式来安装：

```
pip3 install numpy scipy matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple

```

## 安装验证

测试是否安装成功：

```
&gt;&gt;&gt; from numpy import *
&gt;&gt;&gt; eye(4)
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])
from numpy import * 为导入 numpy 库。

```

eye(4) 生成对角矩阵。

## 结束语

今天学习的是PythonNumPy 安装学会了吗。 今天学习内容总结一下：
1. NumPy 安装1. 使用已有的发行版本1. 使用 pip 安装1. Linux 下安装1. 安装验证