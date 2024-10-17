
--- 
title:  2021 年情人节最新的表白神器（Python 制作，源码已开放） 
tags: []
categories: [] 

---
大家好，我是明哥。

关注得早的读者，应该还记得去年的今天，也就是情人节，明哥给大家整了一个 `表白神器`，这个神器是用 Python 写的一个小脚本，它可以将你女神的照片转换成由字符组成的另一张照片，大概的效果如下。

这是转换前的

<img src="https://img-blog.csdnimg.cn/img_convert/f8e2fb2e9d87d96f6dbbc4c129875004.png" alt="">

这是转换后的（**注意放大看**） <img src="https://img-blog.csdnimg.cn/20210214175540810.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjMzODIyNA==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

整个脚本的代码虽然只有 20 行左右，但是大家都知道 Python 脚本的运行是需要 Python 环境的，如果这个脚本中有使用第三方库的话，还需要额外安装一堆 Python 库。这也就意味着，对于一个毫无 Python 使用经验的同学来说，想要把脚本跑起来，还是比较困难的。

刚好今年的情人节，我还没有想到好的 idea，不如把去年的这个工具，使用 tkinter 封装成一个 exe 可执行文件，让所有人都可以使用起来~

先给大家看下这个 exe 程序的成品界面 <img src="https://img-blog.csdnimg.cn/20210214175627738.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjMzODIyNA==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

我把这个 exe 上传到网盘上了：https://wws.lanzous.com/igrjGlnxw9i

接下来，我会复述一下我是如何在完全没有 GUI 编程基础的情况下，在 2 个小时里把这个程序写出来的。

### 0. 准备工作

在开始真正写代码之前，需要大概去预研一下，要写出这样一个 GUI 界面，需要准备哪些东西？
1. **绘制原型**：想要把软件做成啥样子？找找看有没有工具可以画这种软件原型图的。1. **学习GUI编程**：了解 Python 的GUI编程框架有哪些，选一个最易上手的进行学习1. **打包成exe**：了解并学习如何把 Python 脚本打包成 exe 文件
### 1. 绘制模型

有写书经验的人就会知道，选好题后，并不是直接就开始写文章了。一般在写之前，要先把书的大纲给列出来。

写 GUI 软件界面也是如此，在真正开发界面之前，必然要先根据功能画出软件的模型图。

在这个原型图上，可以直观看出，软件要实现哪些功能，怎么实现？用下拉选择呢还是手动输入？

软件的原型图绘制，我使用的是之前一直在用的 `http://drao.io` 这个在线工具。

<img src="https://img-blog.csdnimg.cn/img_convert/2ca32ae85204204fcdd1b674ea7922a7.png" alt="">

从原型图上可以看出来，我这个软件要实现的一些基本功能
1. `开始制作`：把源图片转换成字符组成的目标图片1. `重新制作`：若初次制作不满意，可以点此重新制作，这样不用关闭再打开软件1. `放大预览`：转换完成后，会保存到指定目录，点这个按钮就可以直接进行预览1. `下载源码`：可能会有同学想学习这块代码，所以加了这个入口。
### 2. GUI编程

在今天之前，我都没有学习过 GUI 编程框架，经过简单的了解和对比之后，选择了最轻量的内置 GUI 框架 - `tkinter`。

是的，这玩意是内置的。

但是如果你在自己的电脑上 `import tkinter` 是有可能会报没有找到 tkinter 这个库的。

这是怎么回事呢？

原来，在你安装 Python 解释器的时候，就已经有这个选项，让你自行选择。

<img src="https://img-blog.csdnimg.cn/img_convert/8da2a71e25a781456b216a26ec7a7fac.png" alt="">

那如果你之前，忘了勾选上这个选项，要想重新安装，我有简单搜索了下，好像是比较麻烦的。

不过，好在我想到了一个非常方便快捷的方法，就是在你已经安装了 Python 解释器的情况下，再去双击 Python解释器安装文件，就会弹出这样一个界面，点击 `Modify`，就会再次进入上面让你选择 `tcl/tk` 的界面，勾选之后 ，一路 Next 就会重新在你电脑上安装上 tkinter。

<img src="https://img-blog.csdnimg.cn/2021021417581499.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjMzODIyNA==,size_16,color_FFFFFF,t_70" alt="">

tkinter 安装完成后，就可以根据原型图有针对性的去学习各个控件，经过简单的整理，我需要学习
- Label ：标签，用来显示文字- Button：按钮，用来触发事件- Combobox：下拉列表，用来选择字体- Canvas：画布，用来显示图片- filedialog：对话框，用于选择图片以及保存路径- messagebox：消息弹窗，用来给用户提示和警告
有了这个学习路径，靠着 Google 观察了几个 Demo 后，直接就可以上手代码了。 <img src="https://img-blog.csdnimg.cn/20210214175844303.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjMzODIyNA==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### 3. 打包成exe

打包工具，大家都知道使用 pyinstaller，对于单文件的脚本来说，这个工具还是比较好驾驭的。

使用下面这一条命令，就会生成一个 dist 目录，打开一看会有一个 love-tool.exe 的文件。

```
$ pyinstaller -F -w --hidden-import=tkinter -i ming.ico -y love_tool.py

```

其中几个参数的意思是：
- `-F`：制作独立的可执行程序- `-w`：运行exe时，不打开控制台窗口- `-i`：指定软件的图标- `--hidden-import=tkinter`：导入tkinter包
由于我的 Python 程序中，会引用两个本地的图片，因此生成 exe 后并不能立即执行，得先把我的两张图片先放入到 exe的同级目录。

<img src="https://img-blog.csdnimg.cn/20210214175910729.png" alt="在这里插入图片描述">

这个时候就再双击 `love-tool.exe` 就正常啦

<img src="https://img-blog.csdnimg.cn/20210214175919357.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjMzODIyNA==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### 4. 异常的处理

当用户还没有选择源图片的时候，是理论上是无法转换的，因此这种情况下点 `开始制作`，就要给了提示 <img src="https://img-blog.csdnimg.cn/20210214175749481.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjMzODIyNA==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

同样的，如果用户还没转换完成，也是不能进行 `放大预览` 的。 <img src="https://img-blog.csdnimg.cn/20210214175731159.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjMzODIyNA==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### 5. 写在最后

这个软件并没有对代码进行讲解，主要是对整个开发流程进行复述，有对代码感兴趣的同学，可以点这个链接（https://wws.lanzous.com/igrjGlnxw9i）下载 exe 后，点击 `下载源码` 就可以了。

最后，希望这个工具能给你和女神之间增添一点小乐趣~
