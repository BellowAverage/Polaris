
--- 
title:  干货文：在 Mac 中卸载 Python 的方式 
tags: []
categories: [] 

---
Mac 原本有预装了 Python，直接可以用。你也可以自己从官网下载相应的版本进行安装。但如果说，你现在不想用了，想卸载它也是可以的，几种方式吧，一个个来看。

首先，是直接在「应用程序」直接找到它，然后「移到废纸篓」：

打开查找器，然后单击应用程序； 找到 Python 文件夹并右键单击它； 右键点击移至废纸篓。 如果要卸载内置的 Python，则需要使用终端。以下是指南：

第 1 步：打开活动监视器并在“内存”选项卡中关闭与 Python 相关的所有进程； 第 2 步： 打开终端并从根目录导航到您的库文件夹。您可以使用 cd 库命令。然后，您可以使用 ls 命令列出库中的当前文件夹。查找名为 Python 的文件夹； 第 3 步：使用命令“rm -rf Python”删除 Python。然后，移回根用户目录并使用以下命令删除其他 Python 文件：
- rm -rf /Applications/Python- rm -rf /Library/Frameworks/Python.framework- rm -rf /usr/local/bin/python