
--- 
title:  2024最新版Python 3.12.2安装使用指南 
tags: []
categories: [] 

---
## 2024最新版Python 3.12.2安装使用指南

### Installation and Usage Guide to the Latest Version - Python 3.12.2 for Windows in 2024

By Jackson@ML

#### 0. Python的受欢迎程度

据TechRepublic报道，截至2024年2月16日，全球最流行的编程语言之中，Python、C 和 C++ 在 2 月份最流行的编程语言 TIOBE Software 列表中保持了它们的领先优势（图 A）。

TIOBE专有的积分系统，会根据各种大型搜索引擎考虑了哪些编程语言最受欢迎。Python、C和C++的受欢迎程度同比有所下降，但Python仍保持了本月的头把交椅位置。此外，Go 编程语言首次在 TIOBE 的前 10 名名单中排名第八。 <img src="https://img-blog.csdnimg.cn/direct/ccbb3ae336ec4f1ab884ded6b2e282bd.png" alt="在这里插入图片描述"> 本文将在笔者前文的基础上，将2024年最新版Python 3.12.2安装使用指南快速上线，奉献给您。希望本文对学习Python编程的广大读者有所帮助。

#### 1. 安装最新版Python 3.12.2

为了进行Python应用程序开发，首先需要下载和安装Python软件包。

打开Chrome浏览器，直接访问官网：https://www.python.org。在主页上方导航栏，点击Downloads菜单，选择 **Download for Windows**，点击Python 3.12.2按钮开始下载，如下图所示。

<img src="https://img-blog.csdnimg.cn/direct/0ffc4882257841ca91e37eb857a1e03f.png" alt="在这里插入图片描述"> 随后，Chrome浏览器开始下载安装包，在新版Chrome浏览器中，下载进程如下图：

<img src="https://img-blog.csdnimg.cn/direct/08ab7a6dc769412aa3f80e5856d18b28.png" alt="在这里插入图片描述"> 下载完毕后，可以在Windows 10/11的Downloads(下载)文件夹里，找到该安装程序：python-3.12.2-amd64.exe文件，双击它就可以启动安装向导。如下图所示。

<img src="https://img-blog.csdnimg.cn/direct/a436319f578f4161afffe100737b2d5a.png" alt="在这里插入图片描述"> 如上图所示，在Install Python3.12.2（64-bit）对话框中，要注意：为了防止C:盘文件因系统故障或者无意丢失，选择点击Customize installation(定制安装)，以便接下来选硬盘其它分区来安装Python。

对于图形用户界面（GUI）显示的安装选项，作以下选择： 1） 保留默认勾选项“Use admin privileges when installing py.exe”(安装py.exe时使用管理员权限运行)。 2） 增加复选选项Add python.exe to PATH，即增加Python安装路径到PATH环境变量中。这有利于安装完毕直接启动Python命令行，进行交互式编程； 3） 按照前述要求，点击Customize Installation(定制安装)继续下一步。

在Optional Features（可选特征）对话框，保留默认勾选的五个选项，点击Next进入下一步。

<img src="https://img-blog.csdnimg.cn/direct/a12e664710244e23a7305d418006b59b.png" alt="在这里插入图片描述">

在上图**Advanced Options** (高级选项)对话框中，做以下选择：
- 保留选项Associate files with Python(关联Python文件)；- 保留选项Create shortcuts for installed applications(创建所安装应用程序的快捷方式)；- 保留选项Add Python to environment variables（添加Python安装路径到环境变量）；- 增加复选选项Install Python for all users(为所有用户安装Python)，这有助于使用同一台计算机的其它用户使用Python，而不需重新安装（当然，需确认不同用户身份，确保安全为前提）；- 保留选项Precompile standard library(预编译标准库)，这有助于安装完毕，就可以使用全部标准库（外挂库则需额外安装）；- 同时，修改”Customize Install Location”(定制安装路径)，将默认路径改到D:\Python312文件夹。
接下来，点击**Install** 开始安装。

进入**Setup Progress** (安装过程), 如下图：

<img src="https://img-blog.csdnimg.cn/direct/0990d4f3e85a4a48a0881a07f6c12457.png" alt="在这里插入图片描述">

安装过程中，安装向导会拷贝必要的可执行文件(Executables)，开发库(Development Libraries) 以及预编译Python标准库等。随着进度条状态更新，很快安装完成。

<img src="https://img-blog.csdnimg.cn/direct/6c8fedd078414069b00f91109e077550.png" alt="在这里插入图片描述"> 安装完毕后，出现Setup was Successful(安装成功)对话框，点击Close关闭安装向导。 此刻，已经完成了Python 3.12.2 for Windows的安装过程。

#### 2. 验证Python 3.12.2版本

考虑到要运行Python, 安装完毕需要验证Python版本是否为最新版本。随即点击左下角搜索栏Type here to search,输入cmd, 选择命令行窗口，如下图。

<img src="https://img-blog.csdnimg.cn/direct/bc3f458c7e0746ebbe548bb81e68594b.png" alt="在这里插入图片描述">

点击“以管理员身份运行”，打开Windows终端。

在Windows终端命令行提示符，输入以下命令，验证当前安装Python版本是否为3.12.2：

```
python –version

```

运行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/f72fc760bae141928b413bf8b68e7f63.png" alt="在这里插入图片描述"> 说明Python安装成功！且为最新版本3.12.2。

#### 3. 验证Python功能

接下来，在命令行输入python, 然后按Enter(回车)，进入Python程序命令行交互模式，出现“&gt;&gt;&gt;”提示符。

输入最简单的Python程序，如下命令：

```
&gt;&gt;&gt; print(“Hello, world!”)

```

打印到终端窗口，如下所示。 <img src="https://img-blog.csdnimg.cn/direct/913be2bf6b5d42e189774d726df49711.png" alt="在这里插入图片描述"> 成功运行！

这说明Python最新版3.12.2已经安装完毕，并成功搭载在Windows系统上，Python应用程序也一切正常。

这是交互式解释器。使用完毕，可以用以下命令退出：

```
&gt;&gt;&gt;exit()

```

#### 4. 使用IDLE交互式开发模式

Python安装完毕后，除了在命令行使用交互模式外，安装程序自带的交互式开发工具IDLE也随之安装完毕。

在搜索栏输入关键字“IDLE“，可以搜索到IDLE(Python 3.12 64-bit)交互开发工具，选择”以管理员身份运行“，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/7caf7dd802ba4fb3bc5fa3c2a5ade646.png" alt="在这里插入图片描述"> 这样，就打开了IDLE交互式开发程序。

如果需要执行最简单的”Hello world”程序，

```
print(“Hello, world!”)

```

在IDLE命令行输入，程序可以立刻运行成功！如下图所示。

<img src="https://img-blog.csdnimg.cn/direct/c381fbcf6ba9459b9e17abb54b444376.png" alt="在这里插入图片描述"> 至此，Python最新版3.12.2安装程序全部过程就胜利完工了！

使用Windows终端(cmd)或者IDLE开发工具，都可以启动Python交互式编程工作了。

#### 5. 安装Python扩展库

众所周知，Python语言功能强大，甚至是无所不能。有经验的程序员都知道，标准库包含的功能有限。其实，Python语言更加强大的、丰富的功能来自于扩展库（或者叫外挂库），这一类有数十万个功能各异的库，被收集在Python扩展库官网。

安装任意扩展库，只需要访问该网站首页： ，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/4c3e7c245d8e435ab01cc83d9c6bc2c3.png" alt="在这里插入图片描述"> 在搜索栏（即上图所示的Search projects）中，输入所想搜索的关键字，就会出现安装该扩展库的命令。比如：numpy, 这是Python数值计算常用的扩展库。

<img src="https://img-blog.csdnimg.cn/direct/dc8104c0a66c4e61b2b68b3a2ada6297.png" alt="在这里插入图片描述"> 我们发现，最新版本的numpy 1.26.4发布于2024年2月6日。为了追求最新功能，就点击numpy 1.26.4, 如下图所示： <img src="https://img-blog.csdnimg.cn/direct/55c00a092eba4aefb71672bccccbe4f1.png" alt="在这里插入图片描述"> 于是，得到安装命令提示（在页面左上方）。

让我们打开Windows命令行(cmd)，并且以管理员身份运行，输入上图的命令：

```
pip install numpy

```

命令行会出现提示Requirement already satisfied,意思是numpy已经提前安装完毕，满足需求了。（如果未安装，那么也会提示安装成功！只要互联网保持畅通即可）

技术好文陆续推出，敬请关注。

您的认可，我的动力！😊

#### 相关阅读
1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 201. 1. 1. 