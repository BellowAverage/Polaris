
--- 
title:  2024最新版Python 3.12.1安装使用指南 
tags: []
categories: [] 

---
## 2024最新版Python 3.12.1安装使用指南

### Installation and Configuration Guide to the latest version Python 3.12.1 in 2024

By Jackson

>  
 Python编程语言，已经成为全球最受欢迎的编程语言之一；它简单易学易用，以标准库和功能强大且广泛外挂的扩展库，为用户提供包罗万象、无所不能的功能，以满足数据分析、数据处理、数据可视化、科学计算、数据科学及大数据、云计算、人工智能等多领域的应用。 


本文在笔者前文的基础上，将2024年最新版Python 3.12.1安装使用指南全面更新，奉献给您。希望对学习Python编程的广大读者有所帮助。

#### 1. 下载和安装最新版Python 3.12.1

进行Python程序开发，首先要下载和安装Python软件包。

打开Chrome浏览器，访问官网：

在主页上方导航栏，点击 **Downloads** 菜单，选择 **Download for Windows**，点击**Python 3.12.1**按钮开始下载，如下图所示。

<img src="https://img-blog.csdnimg.cn/direct/1c105101a68c4513b99ed0c7b3fdcac1.png" alt="在这里插入图片描述">

于是，Chrome浏览器开始下载安装包，在新版Chrome浏览器中，下载进程如下图：

<img src="https://img-blog.csdnimg.cn/direct/c6f439483fad4951ab503891765c29f3.png" alt="在这里插入图片描述"> 当下载完毕时，在Windows 10/11的 **Downloads** (下载)文件夹里，找到该安装程序：**python-3.12.1-amd64.exe** 文件，双击启动安装向导。

<img src="https://img-blog.csdnimg.cn/direct/1be3ae0fb85841b29e7537c04c47c1c6.png" alt="在这里插入图片描述"> 如上图所示，在 **Install Python3.12.1（64-bit）**对话框中，为了防止C:盘文件因系统故障或者无意丢失，选择点击 **Customize installation** (定制安装)，以便接下来选硬盘其它分区来安装Python。

对于安装选项，作以下选择：

1） 保留默认勾选项“**Use admin privileges when installing py.exe**”(安装py.exe时使用管理员权限运行)。

2） 增加选项**Add python.exe to PATH**，即增加Python安装路径到PATH环境变量中。这有利于安装完毕直接启动Python命令行，进行交互式编程。

<img src="https://img-blog.csdnimg.cn/direct/a32f659006c44e2cbccf3137bc6c114f.png" alt="在这里插入图片描述"> 在 **Optional Features**（可选特性）对话框，保留默认勾选的四个选项，点击 **Next** 进入下一步。

<img src="https://img-blog.csdnimg.cn/direct/179ae28ea09e440090e8920230274014.png" alt="在这里插入图片描述"> 在 **Advanced Options** (高级选项)对话框中，保留选项 **Add Python to environment variables**（即添加Python安装路径到环境变量）；同时，选择 **Customize Install Location** (定制安装位置)，修改默认路径到 **D:\Python312** 文件夹。

接下来，点击 **Install** 开始安装。

进入Setup Progress(安装过程), 如下图：

<img src="https://img-blog.csdnimg.cn/direct/42c37421698d4fe0b2018be0c7365165.png" alt="在这里插入图片描述"> 安装过程会拷贝必要的可执行文件(Executables)，以及预编译Python标准库等。随着进度条状态更新，很快安装完成。

<img src="https://img-blog.csdnimg.cn/direct/b871201c169648bab43191303bec9701.png" alt="在这里插入图片描述"> 安装完毕后，出现Setup was Successful(安装成功)对话框，点击Close关闭安装向导。 此刻，已经完成了Python 3.12 for Windows的安装过程。

#### 2. 验证Python安装

考虑到要运行Python, 安装完毕需要验证Python版本是否为最新版本。

随即点击左下角搜索栏Type here to search,输入 **cmd**, 选择 **命令提示符 - 以管理员身份运行**，如下图。

<img src="https://img-blog.csdnimg.cn/direct/5d486a7c1c374ac79e82727566a5348d.png" alt="在这里插入图片描述"> 在Windows终端命令提示符，输入以下命令，验证当前安装Python版本是否为3.12.1：

```
&gt;&gt;&gt; python -V

```

或者

```
&gt;&gt;&gt; python –version

```

运行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/74e55f93e3114c39ad414231a74403c1.png" alt="在这里插入图片描述"> 接下来，输入python, 然后按Enter(回车)，进入Python程序命令行交互模式，出现“&gt;&gt;&gt;”提示符。

输入最简单的Python程序，如下命令：

```
&gt;&gt;&gt; print(“Hello, world!”)

```

打印到终端窗口，如下所示。 <img src="https://img-blog.csdnimg.cn/direct/bd42bcd616f4437ebf30026222b506b1.png" alt="在这里插入图片描述">

成功运行！ 这说明Python最新版3.12.1已经安装完毕，并成功搭载在Windows系统上。

这是交互式解释器。使用完毕，可以用以下命令退出：

```
&gt;&gt;&gt; exit()

```

#### 3. 使用IDLE交互式开发模式

Python安装完毕后，除了在命令行使用交互模式外，安装程序自带的交互式开发工具IDLE也随之安装完毕。

在搜索栏输入关键字“**IDLE**“，可以搜索到IDLE(Python 3.12 64-bit)交互开发工具，选择”**以管理员身份运行**“，

<img src="https://img-blog.csdnimg.cn/direct/4be3e7a2bb654eee8e700ad2a855638c.png" alt="在这里插入图片描述"> 这样，就打开了IDLE交互式开发程序。

如果需要执行最简单的”Hello world”程序，

```
&gt;&gt;&gt; print(“Hello, world!”)

```

在IDLE命令行输入，程序可以立刻运行成功！如下图所示。

<img src="https://img-blog.csdnimg.cn/direct/f6057f4d2ec0416b8863f324d4ad530c.png" alt="在这里插入图片描述">

至此，Python最新版安装程序就安装完毕了。使用Windows终端(cmd)或者IDLE开发工具，都可以启动Python编程工作了。

#### 4. 安装Python扩展库

众所周知，Python语言功能强大，甚至是无所不能。 有经验的程序员都知道，标准库包含的功能有限。

其实，Python更多的、丰富的功能来自于扩展库（或者叫外挂库），这一类有数十万个功能各异的库，被收集在Python扩展库官网。

安装任意扩展库，只需要访问该网站首页： <img src="https://img-blog.csdnimg.cn/direct/34d5a32805f549ffb4b6d8ae30fe60e8.png" alt="在这里插入图片描述"> 在搜索栏（即上图所示的 **Search projects** ）中，输入所想搜索的关键字，就会出现安装该扩展库的命令。比如：numpy, 这是Python数值计算常用的扩展库。

<img src="https://img-blog.csdnimg.cn/direct/dd801d57f6ae4ae5a85e53616fb1a395.png" alt="在这里插入图片描述"> 我们发现，最新版本的numpy 1.26.3发布于2024年1月2日。为了追求最新功能，就点击numpy 1.26.3, 如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/88d856e4ede34a35a6693ea7634283f9.png" alt="在这里插入图片描述"> 于是，得到安装命令。

让我们打开Windows命令行，并且以管理员身份运行，输入上图的命令：

```
pip install numpy

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/53aede72c0da40dcb2a1c46ad15756a4.png" alt="在这里插入图片描述"> 提示Requirement already satisfied,意思是numpy已经安装完毕，满足需求了。（如果未安装，那么也会提示安装成功！只要互联网保持畅通即可）

相关博文在后续发布。欢迎关注和点赞。😊 您的认可， 我的动力。😃

#### 相关阅读
1. 1. 1. 1. 1. 1. 1. 