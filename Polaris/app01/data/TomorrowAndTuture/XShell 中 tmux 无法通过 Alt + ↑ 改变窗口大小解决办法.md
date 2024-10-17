
--- 
title:  XShell 中 tmux 无法通过 Alt + ↑ 改变窗口大小解决办法 
tags: []
categories: [] 

---
窗口和窗格操作细节可参考博客：

### 问题概述

最近在 XShell 中使用 tmux 的时候遇到了一个问题，就是使用 Ctrl + b， Alt + ← 和 Ctrl + b， Alt + → 可以进行左右调节窗格，但是 Ctrl + b， Alt + ↑ 和 Ctrl + b， Alt + ↓ 却不可以上下调节窗格（旧版的 XShell 有这个问题）：

<img alt="" height="421" src="https://img-blog.csdnimg.cn/d3e839461e5b471bb5a76a3b04642bf6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATG9vb29raW5n,size_20,color_FFFFFF,t_70,g_se,x_16" width="1051">

### 解决方案

在 XShell -&gt; file（文件） -&gt; Properties（属性） ： Terminal（终端） -&gt; keyboard（键盘） 中 勾选 Use ALT Key as Meta Key

## <img alt="" height="486" src="https://img-blog.csdnimg.cn/3e87eae9b718463781ff020e012bcb86.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATG9vb29raW5n,size_18,color_FFFFFF,t_70,g_se,x_16" width="574">

设置以后，即可正常使用 Ctrl + b， Alt + ↑ 和 Ctrl + b， Alt + ↓上下调节窗格：

<img alt="" height="421" src="https://img-blog.csdnimg.cn/b92bf65b1d1d4eef8a5c8c65a1af24df.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATG9vb29raW5n,size_20,color_FFFFFF,t_70,g_se,x_16" width="1051">

### 全屏问题

重新设置以后，你可能会发现，原先 XShell 默认的全屏快捷键 Alt + Enter 突然用不了了。

对于经常喜欢全屏工作的来说，这是不可接受的。

不过，我们可以新增全屏快捷键，来代替原先 Alt + Enter 的功能。

**新增全屏快捷键步骤：**

**工具 -&gt; 选项 -&gt; 键盘和鼠标 -&gt; 按键对应 -&gt; 新建 -&gt; 输入组合键（我自己设置的是 Ctrl + Alt + Enter）-&gt; 类型（菜单）-&gt; 操作（[查看]全屏）-&gt; 确定。**

### 快捷命令集

XShell 的快捷命令集也很好用哟，它最大的优点是你不需要在每台远程机器上去设置 alias，只需要在 XShell 上配置一次就可以一直使用。
