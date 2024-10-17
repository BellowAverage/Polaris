
--- 
title:  JupyterLab 3.0，极其强大的下一代notebook！ 
tags: []
categories: [] 

---
## 

**机器之心编译**

>  
  **超强下一代 Jupyter Notebook ：JupyterLab 3.0 已经发布了，新版本为用户带来了许多新特性，并对扩展系统进行了实质性的改进。** 
 

JupyterLab 是广受欢迎的 Jupyter Notebook「新」界面。它是一个交互式的开发环境，可用于 notebook、代码或数据，因此它的扩展性非常强。用户可以使用它编写 notebook、操作终端、编辑 markdown 文本、打开交互模式、查看 csv 文件及图片等。除此以外，JupyterLab 还具有灵活而强大的用户界面。就在近日，这款好用的工具发布了新版本 JupyterLab 3.0。

<img src="https://img-blog.csdnimg.cn/img_convert/99a75b3aec5d56ef8fcb3ab265aa6eb0.png">

JupyterLab 3.0 在以下几个方面进行了改进：
- 可视化调试器；- 支持多种显示语言；- notebook 目录；- 扩展系统。
**3 种安装方式**

JupyterLab 3.0 的安装方式有 3 种，第一种采用 pip 方式进行安装，代码如下：

```
pip install jupyterlab==3

```

第 2 种采用 mamba（快速跨平台软件包管理器）方式进行安装，代码如下：

```
mamba install -c conda-forge jupyterlab=3
```

第 3 种采用 conda 方式进行安装，代码如下：

```
conda install -c conda-forge jupyterlab=3
```

需要注意，为了兼容 JupyterLab 3.0，许多第三方扩展仍在更新中，所以用户需要检查自己使用的扩展，必要时也可以更新这些扩展。接下来详细介绍 JupyterLab 3.0 在面向用户使用方面的一些主要改进。

**JupyterLab 3.0 新特性**

**可视化调试器**

JupyterLab 3.0 现在具备**可视化调试器**功能了。为了使用可视化调试器，用户首先需要一个支持调试器的内核。Xeus-Python 内核是第一个支持 Python 代码调试的 Jupyter 内核。展示如下：

<img src="https://img-blog.csdnimg.cn/img_convert/a4fed6d64574ac4032febba5ccf141f3.gif">

**在 JupyterLab 3.0 中使用可视化调试器进入 Python 程序。**

更多详细文档请参阅：https://jupyterlab.readthedocs.io/en/stable/user/debugger.html

**目录扩展**

现在 JupyterLab 3.0 提供了**目录扩展**，使得用户更方便地查看和浏览文档结构。展示如下：

<img src="https://img-blog.csdnimg.cn/img_convert/ef61052d2f448edec2e9004e24e7b6b2.gif">

**在 JupyterLab 3.0 使用目录功能。**

**支持多种语言显示**

JupyterLab 3.0 提供了**设置用户界面显示语言**的功能。若要使用这种功能，用户需要将语言包作为单独的 Python 包安装。语言包在 GitHub 项目中已经分组，采用 pip 的方式就可以安装。例如，使用以下代码可以安装简体中文语言包：

```
pip install jupyterlab-language-pack-zh-CN

```

<img src="https://img-blog.csdnimg.cn/img_convert/4b68874d0f68291bbf74ecf5f6497c56.png">

**以简体中文显示的 JupyterLab 3.0 界面。**

关于添加新语言包请参考：https://jupyterlab.readthedocs.io/en/stable/user/language.html

**简单交互界面模式的改进**

JupyterLab 3.0 对简单交互界面模式（即以往的单文档显示模式）进行了更新，使交互界面模式更流畅、更能面向文档。用户可以使用状态栏中的开关切换简单交互界面模式，也可以从视图菜单或命令面板中切换或者使用默认快捷键「Ctrl/Cmd+Shift+D」。

<img src="https://img-blog.csdnimg.cn/img_convert/9cfb1479cce020d9754fe2833da6de79.gif">

**启用和禁用简单交互界面模式。**

JupyterLab 3.0 对移动设备的支持也得到了很大的改进。用户可以对窗口进行缩展，使布局更加紧凑。当窗口缩小时，JupyterLab 自动切换到简单交互界面模式。

<img src="https://img-blog.csdnimg.cn/img_convert/fb4ae22f3a43c124333befdb2bf58aec.gif">

**JupyterLab 在屏幕缩小时自动切换到简单交互界面模式。**

目前这项功能正在不断的迭代更新，使得这个交互界面在移动设备上更容易访问。

**使用 pip 和 conda/mamba 方式安装新的扩展**

JupyterLab 扩展现在可以作为预构建的扩展进行分发，而不需要用户重新构建 JupyterLab 或安装 Node.js。用户可以使用熟悉的包管理器（如 pip、conda 和 mamba）将预构建的扩展作为 Python 包分发，从而使得安装和使用扩展更快更方便。

<img src="https://img-blog.csdnimg.cn/img_convert/85e24eb29f5d92bd002b7bc1b6dc3eef.gif">

**采用 pip 方式安装新的扩展。**

预构建的扩展可以作为单独的包发布到 PyPI 和 conda-forge 中，或者捆绑到带有 Jupyter 服务器扩展和 Classic Notebook 扩展的包中。这些有助于整个系统的一致性。

例如：使用 pip 或 conda 方式安装新的 ipywidgets 7.6.0，以在典型的 Jupyter Notebook 和 JupyterLab3.0 中自动启用 ipywidgets—无需额外的步骤或者重建 JupyterLab。

<img src="https://img-blog.csdnimg.cn/img_convert/7d857584e7451b20767ab862b1f5ed17.gif">

**在 JupyterLab 3.0 中自动安装 ipywidgets。**

**改进 Extension Author 的工作流程**

新的预构建扩展对于 Extension Author 来说开发起来非常方便。TypeScript 扩展 cookiecutter 已经更新为默认情况下开发预构建的扩展，并提供了所有必要的工具来快速从头开始创建新的扩展。

关于扩展的更多信息，请参考：
- https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html- https://jupyterlab.readthedocs.io/en/latest/extension/extension_migration.html
如果你正在寻找示例来学习如何制作自己的扩展，请查看 GitHub 上的扩展示例库。这些示例已经更新兼容 JupyterLab 3.0，并提供了开发扩展的手动方法。

扩展示例库地址：https://github.com/jupyterlab/extension-examples

**变更日志**

上述内容仅仅概述了 JupyterLab 3.0 的新功能。如果你想要浏览更完整的变更列表，包括错误修复等，请查看详细变更日志。
- 详细变更日志地址：https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v3-0- JupyterLab 3.0 测试地址：https://mybinder.org/v2/gh/jupyterlab/jupyterlab-demo/3818244?urlpath=lab
**原文链接：https://blog.jupyter.org/jupyterlab-3-0-is-out-4f58385e25bb**

```
&lt; END &gt;

微信扫码关注，了解更多内容

```
