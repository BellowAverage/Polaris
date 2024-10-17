
--- 
title:  2024最新版ANACONDA安装使用指南 
tags: []
categories: [] 

---
## 2024最新版Anaconda安装使用指南

### Installation and Usage Guide to Setup the Latest Anaconda in 2024

By Jackson@ML

#### 0. 什么是Anaconda?

>  
 Anaconda 是编程语言 Python 和 R 的免费开源发行版（可以通过查看相关 Python 和 R 语言的在线编程课程进一步了解）。该发行版附带了 Python 解释器以及与机器学习和数据科学相关的各种扩展包。 


事实上，Anaconda 开发者原本的想法是让对这些相关领域感兴趣的用户，可以通过一次安装轻松安装配置所有（或大部分）所需的软件包，而不需要一个一个费事费时地去琢磨。

由于AnaConda天生和Python有渊源，所以，安装好它之后，Python编程就可以开始大展拳脚了，尤其是对于数据科学和机器学习有帮助的交互式编程，在AnaConda实现起来，简直是a piece of cake! (意思是：超简单)

#### 1. Anaconda包含什么？

既然上文说，Anaconda十分易用和强大，那么它究竟包含什么呢？

Anaconda实际上包含以下重量级的应用（开源软件包，扩展库和笔记本等）：
- 一个名为 Conda 的开源包和环境管理系统，它使安装/更新包和创建/加载环境变得更加容易。- 机器学习库，如 TensorFlow、scikit-learn 和 Theano。- 数据科学库，如 pandas、NumPy 和 Dask。- 可视化库，如 Bokeh、Datashader、matplotlib 和 Holoviews。- Jupyter Notebook，一个可共享的笔记本，结合了实时交互代码、可视化效果和文本。
** 访问官网链接：，就可以知道Anaconda包含哪些要素。如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/5527b06fd78b4f83962a92f507e09438.png" alt="在这里插入图片描述">

#### 2. 下载Anaconda最新版

打开Chrome浏览器，输入Anaconda官网链接：, 点击进入主页面。

如下图所示： <img src="https://img-blog.csdnimg.cn/direct/3b02fb01b2a2426d88b6473dfb09078f.png" alt="在这里插入图片描述"> 将页面向下滚动，到 **Start Quickly with Open-source Tools** (采用开源工具快速启动)区域，选择 **Free download**按钮点击进入下载页面。

<img src="https://img-blog.csdnimg.cn/direct/64b6bcf1b6d54aa7ab7192e7e46cceda.png" alt="在这里插入图片描述"> 进入到下载页面，如下图；点击 **Download** 按钮随即下载。

<img src="https://img-blog.csdnimg.cn/direct/24809f5f77654e7b81538b01ecc9f50d.png" alt="在这里插入图片描述"> 当开始下载的时候，Chrome浏览器右上方出现隐藏的下载进度；

下载页面变成感谢词 – **Thank you for downloading!**

<img src="https://img-blog.csdnimg.cn/direct/5f42cc104acf499f99fd91408b62a0fd.png" alt="在这里插入图片描述"> 等下载完毕，在Windows的下载文件夹内，找到可执行安装包：**Anaconda3-2023.09-0-Windows-x86_64.exe** , 双击它开始安装。

#### 3. 安装Anaconda最新版

<img src="https://img-blog.csdnimg.cn/direct/0a1fee572474412a8bfefb2a54faa6f1.png" alt="在这里插入图片描述"> 点击 **Next** 进行下一步。

<img src="https://img-blog.csdnimg.cn/direct/7b4fe4912aaf4fb08c9c2d90cf9e03d9.png" alt="在这里插入图片描述"> 点击 **I Agree** 继续下一步。 <img src="https://img-blog.csdnimg.cn/direct/b35c26a1e88a45abb3cc98edc3abfd2e.png" alt="在这里插入图片描述"> 按照默认选项 Just Me (仅我使用)，点击 **Next** 进行下一步。

<img src="https://img-blog.csdnimg.cn/direct/6bbada420d5c4136945419feb51a0faf.png" alt="在这里插入图片描述"> 按照默认路径安装，点击 **Next** 进行下一步。

<img src="https://img-blog.csdnimg.cn/direct/c6baa4de58e44ac586e6ac8d7d2ce8ec.png" alt="在这里插入图片描述"> 按照默认选项，点击 **Install** 开始安装。

<img src="https://img-blog.csdnimg.cn/direct/4dc82906f453429eb2c4802392495f1a.png" alt="在这里插入图片描述"> 安装完毕，显示以下对话框。

<img src="https://img-blog.csdnimg.cn/direct/096ab88c0cd5430680c672429a3cffa1.png" alt="在这里插入图片描述"> 点击 **Next** 以完成安装。

<img src="https://img-blog.csdnimg.cn/direct/2d3bfd9e8a8049e3b7b3c748ea96999b.png" alt="在这里插入图片描述"> 点击Next继续下一步。

<img src="https://img-blog.csdnimg.cn/direct/aa66fb45a51a484c92f73af5838823e7.png" alt="在这里插入图片描述"> 点击 **Finish** 结束安装。

此时，按照默认选项，将启动 AnaConda Navigator, 如下图：

<img src="https://img-blog.csdnimg.cn/direct/59ea662c998247728b5b9002d3c1a19e.png" alt="在这里插入图片描述">

提示是否需要更新为AnaConda Navigator 2.5.2，选择 **Yes** 继续。 接下来，系统会自动更新到最新版本2.5.2.

#### 4. 启动Anaconda及其应用

在Windows搜索栏中，搜索关键字AnaConda Navigator，出现开始菜单，选择点击以管理员身份运行，如下图所示： <img src="https://img-blog.csdnimg.cn/direct/3ebb63b4d34f41e2a7aa8a375841844a.png" alt="在这里插入图片描述"> 随后马上启动AnaConda Navigator，类似于启动一个集成开发平台，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/cb272cc7e73845f18c27e23b234fb295.png" alt="在这里插入图片描述"> 可以看到很多可用的已安装应用模块，例如：DataSpelll, Anaconda Toolbox, Anaconda Cloud Notebooks, CMD.exe Prompt, Jupyter Lab, Notebook, PowerShell Prompt, PyCharm Community, QT Console, Spyder, VS Code, Anaconda on AWS Graviton, Datalore, IBM Wasonx等。

接下来，如果我们需要使用Jupyter Lab, 则可以将鼠标滚轮向下滚动，选择**Jupyter Lab**，点击 **Launch** 按钮启动，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/2dea98f3c10e4b019f678e97c990bea7.png" alt="在这里插入图片描述"> 这是，系统会打开Juypter Lab交互式控制台，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/7fdd84504c314ece81ab38fb3f8b2111.png" alt="在这里插入图片描述"> 由于之前笔者安装过一些编程语言内核，因此可以看到不少模块，例如iPython, Bash， R，Julia, Ruby, Rust, Java等。

现在，我们需要演示一下Python交互式编程，于是点击Python 3(iPykernel)按钮，如下图： <img src="https://img-blog.csdnimg.cn/direct/b6d5c0ab228e488897f117c859490d4d.png" alt="在这里插入图片描述"> 输入Python最简单的程序语句，

```
print(“Hello, world!”)

```

然后，按组合键 Ctrl + Enter，进行解释。出现Hello, world!字样，说明程序交互运行成功！

#### 5. 小结

本文简要介绍了Anaconda 3的安装步骤，以及启动和使用Anaconda Navigator及其组件Jupyter Lab的过程。

Anaconda的功能强大，对于数据科学和机器学习而言，有非常重要的地位。今后有机会，我们再探讨其它课题。希望对各位读者有所帮助。

技术好文陆续推出，敬请关注。

您的认可，我的动力！😊

#### 相关阅读
1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 