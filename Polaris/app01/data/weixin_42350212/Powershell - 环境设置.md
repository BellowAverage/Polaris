
--- 
title:  Powershell - 环境设置 
tags: []
categories: [] 

---
PowerShell 图标可以在任务栏和开始菜单中找到。只需点击图标，它就会打开。

<img alt="" height="454" src="https://img-blog.csdnimg.cn/53df58dfb2b64c18b0f168f02e004a21.png" width="600">

 

要打开它，只需单击图标，然后将打开以下屏幕，这意味着 PowerShell 已准备好供你使用。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/c76934d16a6cc3baa6d9467330cc73d0.jpeg">

### 

最新版本的 PowerShell 是 5.0，为了检查我们服务器中安装的是什么，我们输入以下命令 - **：$ PSVersionTable**，如下面的屏幕截图所示，从屏幕上我们也知道我们有 PSVersion 4.0

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/e4b538069ca2956fb6d85df27960895c.jpeg">

要使用具有更多 Cmdlet 的最新版本进行更新，我们必须从以下链接下载 **Windows Management Framework 5.0** -  并安装它。

<img alt="" height="424" src="https://img-blog.csdnimg.cn/8bad5099b8d541fe8e5dc9ca6d514337.png" width="600">

 

### 

Windows PowerShell **集成脚本环境** （ISE）是 Windows PowerShell 的主机应用程序。在 Windows PowerShell ISE 中，你可以在单个基于 Windows 的图形用户界面中运行命令和编写，测试和调试脚本，具有多行编辑，选项卡完成，语法着色，选择性执行，上下文相关帮助以及对从左到右书写语言的支持。

你可以使用菜单项和键盘快捷方式执行许多与在 Windows PowerShell 控制台中执行的任务相同的任务。例如，在 Windows PowerShell ISE 中调试脚本时，要在脚本中设置行断点，请右键单击代码行，然后单击“ **切换断点”** 。

要打开它，只需转到“开始” - “搜索”，然后选择“类型” - `PowerShell`，如以下屏幕截图所示。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/0269585711523cf17d7b8e2afd417aae.jpeg">

然后单击 Windows PowerShell ISE。或者单击向下箭头，如以下屏幕截图所示。

<img alt="" height="214" src="https://img-blog.csdnimg.cn/a52a4868a5c24c91a106625d335a9cd1.png" width="322">

 

它将列出服务器上安装的所有应用程序，然后单击 Windows PowerShell ISE。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/eee1ef4661ab9d9b821ca39bf0322cfd.jpeg">

下表将开放 -

<img alt="" height="330" src="https://img-blog.csdnimg.cn/bb3ff666adbf420cbbaf5fc15cccf2d1.png" width="600">

 

它有三个部分，其中包括 - 编号为 1 的 **PowerShell 控制台**，然后是编号为 2 的**脚本文件**，第三部分是**命令模块**，你可以在其中找到该模块。

在创建脚本时，你可以直接运行并查看结果，如下例所示 -



### 

有很多 PowerShell 命令，在本教程中很难放入所有这些命令，我​​们将重点介绍 PowerShell 的一些最重要的命令和基本命令。

第一步是转到 Get-Help 命令，该命令为你提供有关如何提供命令及其参数的说明。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/916d799a24df865878111a979740247b.jpeg">

**要获取更新列表** -
- Get-HotFix 并安装热修复，如下所示- Get-HotFix -id kb2741530
<img alt="" height="298" src="https://img-blog.csdnimg.cn/cef0bb9882684b5198a74521a55f42fc.png" width="600">



 
