
--- 
title:  PYTHON语言程序设计基础 第2版第二版 嵩天答案 
tags: []
categories: [] 

---
大家好，小编来为大家解答以下问题，PYTHON语言程序设计基础 第2版第二版 嵩天答案，PYTHON语言程序设计基础 第2版第二版 嵩天，现在让我们一起来看看吧！

<img alt="" height="299" src="https://img-home.csdnimg.cn/images/20230724024159.png?origin_url=https%3A%2F%2Fgss0.bdstatic.com%2F9bA1vGfa2gU2pMbfm9GUKT-w%2Ftimg&amp;pos_id=HkDF2EHG" width="534">

Source code download: 

### Python程序设计

Python 是全球范围内最受欢迎的编程语言之一，学好Python将对个人职业生涯产生很大的助力，Python在机器学习、深度学习、数据挖掘等领域应用极为广泛。

掌握Python，高薪就业不是问题。在数据科学家/数据分析师、人工智能工程师、网络安全工程师、软件工程师/全栈工程师、自动化测试工程师等岗位，年入50w是很普遍的。

Python程序设计系列文章：























##### 第1章 初识Python
- - <li> 
    <ul>- - - - - - - - - - - 


### 1.1 Python简介

Python是当今`主流`的编程语言，应用领域非常广泛，比如：
- Web开发- 科学计算- 数据分析- 游戏开发- 机器学习- 爬虫- 计算机视觉
（1）`Web开发`。Python是Web开发的主流语言，与JS、PHP等广泛使用的语言相比，Python的类库丰富、使用方便，能够为一个需求提供多种方案；此外Python支持最新的XML技术，具有强大的数据处理能力，因此Python在Web开发中占有一席之地。Python为Web开发领域提供的框架有django、flask、tornado、web2py等。

（2）`科学计算`。Python提供了支持多维数组运算与矩阵运算的模块numpy、支持高级科学计算的模块scipy、支持2D绘图功能的模块matplotlib，又具有简单易学的特点，因此被科学家用于编写科学计算程序。

（3）`游戏开发`。很多游戏开发者先利用Python或Lua编写游戏的逻辑代码，再使用C++编写图形显示等对性能要求较高的模块。Python标准库提供了pygame模块，利用这个模块可以制作2D游戏。

（4）`自动化运维`。Python又是一种脚本语言，Python标准库又提供了一些能够调用系统功能的库，因此Python常被用于编写脚本程序，以控制系统，实现自动化运维。

（5）`多媒体应用`。Python提供了PIL、Piddle、ReportLab等模块，利用这些模块可以处理图像、声音、视频、动画等，并动态生成统计分析图表；Python的PyOpenGL模块封装了OpenGL应用程序编程接口，提供了二维和三维图像的处理功能。

（6）`爬虫开发`。爬虫程序通过自动化程序有针对性地爬取网络数据，提起可用资源。Python拥有良好的网络支持，具备相对完善的数据分析与数据处理库，又兼具灵活简洁的特点，因此被广泛应用于爬虫领域之中。

Python是非常`简单易学`的语言，而且`功能强大`，具有高效的数据结构，面向对象编程也很简单。所以很多公司在快速开发应用程序时、写脚本时，都是用的Python，`我本人也是Python的铁粉`。

#### 1.1.1 编程语言概述

我们人跟`人`交流，靠的是`自然语言`，比如：汉语、英语、法语等等 而人跟`计算机`打交道，靠的是`编程语言`,比如：Python、C/C++、Java、C#、Go等等。

计算机编程语言分为3类：`1、机器语言``2、汇编语言``3、高级语言`

**1、机器语言：** 机器语言是第一代编程语言，早期的计算机语言只有机器语言，但如今已很少有人学习和使用。

机器语言是由0、1组成的二进制代码表示的指令，这类语言可以被CPU直接识别，具有灵活、高效等特点。举例如下：<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/cf9983a240e5496684db22ae6a5e3ac2.png"> 但机器语言有个不可忽视的缺点：`可移植性差`。

**2、汇编语言：** 汇编语言中通过带`符号`或`助记符`的`指令`和`地址`代替二进制代码，因此`汇编`语言也被称为`符号`语言，例如： 汇编语言中的MOV指令：

```
MOV destination,source

```

等价于C 语言中的：

```
destination=source

```

**3、高级语言** 高级语言并非一种语言，而是诸多编程语言的`统称`。

常见的高级语言有Python、C、C++、Java、JavaScript、PHP、Basic、C#等等

从`机器语言`—&gt; `汇编语言`—&gt; `高级语言`的演变规律，其实就是越来越方便程序员开发程序的，越来越接近自然语言.

但是同时，效率就会越来越低，因为高级语言要一层层翻译为最终计算机可以执行的机器语言才可以运行。

#### 1.1.2 Python解释器

Python是一种解释型高级语言，Python代码的执行依靠的是解释器。其中包括`CPython`、IPython、PyPy、Jython、IronPython。其中：

`CPython`是官方版本的解释器，使用C语言开发的，也是使用最广泛的Python解释器。

`IPython`是基于CPython，但交互方式上比CPython强

`PyPy`是一种追求执行速度的Python解释器，对Python代码的执行速度有所提高

`Jython`运行在Java平台的Python解释器

`IronPython`运行在微软.NET平台上的Python解释器

#### 1.1.3 Python的特点

**优点：** （1）`简洁`。在实现相同功能时，Python代码的行数往往只有C、C++、Java代码数量的1/5~1/3。

（2）`语法优美`。Python语言是高级语言，它的代码接近人类语言，只要掌握由英语单词表示的助记符，就能大致读懂Python代码；此外Python通过强制缩进体现语句间的逻辑关系，任何人编写的Python代码都规范且具有统一风格，这增加了Python代码的可读性。

（3）`简单易学`。与其他编程语言相比，Python是一门简单易学的编程语言，它使编程人员更注重解决问题，而非语言本身的语法和结构。Python语法大多源自C语言，但它摒弃了C语言中复杂的指针，同时秉持“使用最优方案解决问题”的原则，使语法得到了简化，降低了学习难度。

（4）`开源`。Python自身具有足够多引人注目的优点，该优先吸引了大量的人使用和研究Python；Python是FLOSS（自由/开放源码软件）之一，用户可以自由地下载、拷贝、阅读、修改代码，并能自由发布修改后的代码，这使相当一部分用户热衷于改进与优化Python。

（5）`可移植`。Python作为一种解释型语言，可以在任何安装有Python解释器的平台中执行，因此Python具有良好的可移植性，使用Python语言编写的程序可以不加修改地在任何平台中运行。

（6）`扩展性良好`。Python从高层上可引入.py文件，包括Python标准库文件，或程序员自行编写的.py形式的文件；在底层可通过接口和库函数调用由其它高级语言编写的代码。

（7）`类库丰富`。Python解释器拥有丰富的内置类和函数库，世界各地的程序员通过开源社区又贡献了十几万个几乎覆盖各个应用领域的第三方函数库，使开发人员能够借助函数库实现某些复杂的功能。

（8）`通用灵活`。Python是一门通用编程语言，可被用于科学计算、数据处理、游戏开发、人工智能、机器学习等各个领域。Python语言又介于脚本语言和系统语言之间，开发人员可根据需要，将Python作为脚本语言来编写脚本，或作为系统语言来编写服务。

（9）`模式多样`。Python解释器内部采用面向对象模式实现，但在语法层面，它既支持面向对象编程，又支持面向过程编程，可由用户灵活选择。

（10）`良好的中文支持`。Python 3.x解释器采用UTF-8编码表达所有字符信息，该编码不仅支持英文，还支持中文、韩文、法文等各类语言，使得Python程序对字符的处理更加灵活与简洁。

**缺点：** （1）`执行效率不够高`，Python程序的效率只有C语言程序的1/10。

（2）`Python 3.x和Python 2.x不兼容`。

### 1.2 Python安装

Python在Windows、Linux、Mac系统均可以使用，但大多数学生都是Windows系统，所以下面仅以Windows操作系统为例，演示Python解释器的安装过程。

但是大家要清楚，工作以后就是Linux用的最多，因为你写好的程序最终要上线，供用户使用，此时需要放到Linux服务器中运行，因此Linux中也必定要有Python的解释器。

一般工作用Mac OS的，基本都是大厂程序猿、水平较高的程序猿，或者专门做Mac OS应用程序开发的程序猿。

#### 1.2.1 Windows下的安装

（1）访问Python官网的下载页面：

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a9c919b79c6b48aa8cff2f5d16efac87.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_16,color_FFFFFF,t_70,g_se,x_16"> （2）单击超链接“Windows”，进入Windows版本软件下载页面，根据你的操作系统版本选择相应软件包。例如：如果你的计算机使用的是Windows 7 64位操作系统，此处可选择3.7.2版本、.exe形式的安装包。 （这里需要注意：x86-x64指的是64位系统，而x86指的是32位系统。)<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1b4f15f2289d462cb49ef4d0489d15e2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_14,color_FFFFFF,t_70,g_se,x_16"> （3）下载完成后，双击安装包会启动安装程序。勾选“Add Python 3.7 to PATH”（将python安装路径添加到系统的环境变量，方便检索出python解释器），选择“Install Now”开始自动安装Python解释器、配置环境变量。片刻后安装完成。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/501bf1c4a52d4a64b84072f7661c01a5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_13,color_FFFFFF,t_70,g_se,x_16"> （4）在【开始】菜单栏中搜索“python”，找到并单击打开Python 3.7(64 bit)。

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/664254a0f8ac43c9b8307032de018684.png"> （5）用户亦可在控制台中进入Python环境，具体操作为：打开控制台窗口，在控制台的命令提示符“&gt;”后输入“python”，按下Enter键（回车键）<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/920837e032ae46fb9e5eeae4b3d89c5c.png">

#### 1.2.2 Linux下的安装

可自行百度，这里仅附上一篇链接：

#### 1.2.3 Mac OS下的安装



### 1.3 Python代码执行

Python程序的运行方式有两种：`交互式`和`文件式`:

**交互式**指Python解释器逐行接收Python代码并即时响应；

**文件式**也称批量式，指先将Python代码保存在文件中，再启动Python解释器批量解释代码。

#### 1.3.1 交互式模式下执行Python代码

`1.交互式` Python解释器或控制台都能以相同的操作通过交互方式运行Python程序，以控制台为例，进入Python环境后，在命令提示符“&gt;&gt;&gt;”后输入如下代码：

```
print("hello world")

```

按下回车键，控制台将立刻打印运行结果。运行结果如下所示：

```
hello world

```

#### 1.3.2 脚本模式下执行Python代码

`2.文件式` 创建文件，在其中写入Python代码，将该文件保存为.py形式的Python文件。 此处以代码“print(“hello world”)”为例，在文件中写入此行代码，并以文件名“hello.py”保存文件。 打开控制台窗口，在命令提示符“&gt;”后输入命令“python hello.py”运行Python程序。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f5ee594e6bd5498bbf919958eca78c60.png">

### 1.4 Python集成开发环境

所谓的集成开发环境就是在开发程序代码时，把很多能帮助提高代码开发效率的功能，封装在一个应用程序中，这个应用程序就是集成开发环境。

Python集成开发环境非常多，常见的有以下几种：
1. Eclipse + PyDev1. Sublime Text1. Atom1. GNU Emacs1. VI/VIM1. Visual Studio1. Visual Studio Code1. PyCharm1. Spyder1. Thonny
因为`PyCharm`功能齐全，使用的人非常多，所以我们选择PyCharm作为`python程序的开发工具`。

#### 1.4.1 PyCharm的安装

PyCharm的下载安装 访问PyCharm官方网址，进入PyCharm的下载页面。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6cd59b936a474d5bb67f3ea16cf8966c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_15,color_FFFFFF,t_70,g_se,x_16"> 这里需要注意版本的区别，`专业版`（Professional）是`收费`的，`社区版`（Community）是`免费`的，不同版本的特点如下：

**Professional版本的特点：**
- 提供Python IDE的所有功能，支持Web开发- 支持Django、Flask、Google App引擎、Pyramid和web2py- 支持JavaScript、coffee、type、css、cython等、- 支持远程开发、python分析器、数据库和SQL语言
**Community版本特点：**
- 轻量级的Python IDE，只支持Python开发- 免费、开源、集成Apache2的许可证- 智能编辑器、调试器、支持重构和错误检查、集成VCS版本控制
**Windows环境下PyCharm的安装**

这里以Windows为例，讲解如何安装PyCharm。

**步骤1：** 双击下载好的exe安装文件（pycharm-community-2018.3.4.exe），打开PyCharm安装向导。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/fbc56c8e83fb4228b0606775452e8d19.png">

**步骤2：** 单击【Next &gt;】按钮，进入“Choose Install Location”界面，用户可在此界面设置PyCharm的安装路径。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/dd2af33b4ab64deb970bb341eb774858.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_10,color_FFFFFF,t_70,g_se,x_16">**步骤3：** 单击图1-21中的【Next &gt;】按钮，进入“Installation Options”的界面，在该界面可配置PyCharm的选项。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/5990c8304ae844c79467616951009719.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_10,color_FFFFFF,t_70,g_se,x_16">**步骤4：** 假如你使用的是64位操作系统，在`上图`界面中勾选`除`“32-bit launcher”外的所有选项，单击【Next &gt;】按钮，进入“Choose Start Menu Folder”界面。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/838a522467424083a7398aee1baa9c49.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_10,color_FFFFFF,t_70,g_se,x_16">**步骤5：** 单击【Install】按钮，开始下载JRE，安装PyCharm。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2663ef277c2a4ee28bbbb5400db50f39.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_8,color_FFFFFF,t_70,g_se,x_16">

**步骤6：** 片刻后PyCharm安装完成，单击【Finish】按钮结束安装 。

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1c847138754e49c6b263eef8af7ee773.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_8,color_FFFFFF,t_70,g_se,x_16">

#### 1.4.2 PyCharm的使用

（1）完成PyCharm的安装后，双击桌面的PC图标打开PyCharm。首次使用PyCharm时用户需先接受相关协议。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4fee525c500c416d9da63a1759ef1255.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_9,color_FFFFFF,t_70,g_se,x_16">

（2）单击【Continue】按钮，进入“Customize PyCharm”界面，选择PyCharm的UI主题，建议选择Darcula这种黑色主题（比较护眼，且黑色给人以高端的感觉）。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1ebb504450bf42699222187c87ce055d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_9,color_FFFFFF,t_70,g_se,x_16"> （3）启动完成后将进入欢迎界面。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/fd4f61bc78d14c4ebea6c05db33e3ea1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_10,color_FFFFFF,t_70,g_se,x_16">

>  
  （1）Creat New Project：创建新项目。 （2）Open：打开已经存在的项目。 （3）Check out from Version Control：从版本控制中检出项目。 
 

（4）创建项目。单击【Create New Project】进入【CreateProject】界面。这里设置项目存储路径为D:\PythonDemo，之后单击【Create】进入项目界面 。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f8b92966614a4db5a772026d391ebbdf.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_9,color_FFFFFF,t_70,g_se,x_16"><img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/44779f00ae2b4b2e91a32163fa351ad2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_10,color_FFFFFF,t_70,g_se,x_16"> （5）此时创建的项目是空项目，之后还需要在项目中创建Python文件。选中项目名称，单击鼠标右键，在弹出的快捷菜单中选择【New】→【Python File】，弹出“New Python file”窗口，在该窗口的Name文本框中设置Python文件名为“hello_world”，单击【OK】按钮后完成文件的创建。

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c30ce11602644991be632a18aca883da.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_20,color_FFFFFF,t_70,g_se,x_16"> （6）在hello_world.py文件中输入下列代码：

```
print("Hello World!")

```

（7）右键单击HelloWorld.py文件，在弹出的快捷菜单中选择【Run ‘hello_world’】运行程序。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c67165b030c54bc4ad8458dc27deaefe.png">

#### 1.4.3 PyCharm的插件

这一节初学者可跳过，后续有需要的时候再回头来看。

(1) 如何安装Pycharm插件

在正式介绍插件之前，先来简单看下Pycharm的插件安装方法。

打开file——settings——plugings，在右侧的文本框中输入想要查看的插件名称，在下方就会罗列出已安装的相关的插件，点击Install就可以安装:<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/61a63d29ad0c4fdea693807819a91b69.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5biD6KGj5Lmm55SfLVB5dGhvbg==,size_20,color_FFFFFF,t_70,g_se,x_16"> （2）常用插件 01.插件：`Mongo Plugin` 02.插件：`Statistic` 03.插件：` wakatime` 04.插件：`markdown support ` 05.插件：`IdeaVim ` 06.插件：`Material Theme UI `

### 1.5 Python2.x与Python3.x的区别

本节，建议初学者直接跳过，因为目前大多数项目都已经是用Python 3.x做的了。以前需要学习区别是因为当时很多项目都是Python 2.x做的，我们要了解区别，然后才能把老版本的代码升级为新的去运行，但现在市场上基本没有这种需求了，所以建议初学者直接跳过！

Python 3.x不兼容Python 2.x，但这两个系列在语法层面的差别不大，Python 3.x移除了部分混淆的表达方式，但大体语法与Python 2.x相似，Python 3.x的使用者可以轻松阅读Python 2.x编写的代码。

下面列举Python 3.x和Python 2.x的部分区别，以帮助大家了解它们之间的差异。

**（1）编码方式。** Python 3.x默认采用utf-8编码，对中文和英文都有良好的支持； Python 2.x默认采用ASCII编码，对中文支持不够良好，为了防止因程序包含中文而报错，一般在Python 2.x文件首行将编码格式设置为utf-8，设置方式如下：

```
# -*- coding:utf-8 -*-

```

除需在程序首行添加以上代码外，Python 2.x编写的程序中需要使用decode()方法和encode()方法对接收和输出的字符格式进行转换。**（2）print语句。** Python 3.x中用print()函数取代了python 2.x中的print语句，两者功能相同，格式不同。举例：**--------------------------------------------------------Python2.x版本----------------------------------**

```
&gt;&gt;&gt;print 3,4

```

输出结果：

```
3 4

```

**--------------------------------------------------------Python3.x版本----------------------------------**

```
&gt;&gt;&gt;print(3,4)

```

输出结果：

```
3 4

```

**（3）除法运算** Python 3.x中两个整数相除（使用运算符“/”）返回一个浮点数，不再返回整数； 新增运算符“//”实现整除。**--------------------------------------------------------Python2.x版本----------------------------------**`整数除：`

```
&gt;&gt;&gt;1 / 2

```

输出结果：

```
0

```

`浮点数除：`

```
&gt;&gt;&gt;1.0 / 2.0

```

输出结果：

```
0.5

```

**--------------------------------------------------------Python3.x版本----------------------------------**

`普通除：`

```
&gt;&gt;&gt;1 / 2

```

输出结果：

```
0.5

```

`整除：`

```
&gt;&gt;&gt;1 // 2

```

输出结果：

```
0

```

**（4）八进制表示** Python 3.x中只使用“`0o`”开头以表示`八进制`，删除了Python 2.x中使用“0”开头的表示方法。

**（5）比较行为** Python 3.x只使用“`!=`”表示不等运算，删除了Python 2.x中的“&lt;&gt;”表示方法。

Python 3.x中的&lt;、&lt;=、&gt;、&gt;=运算符被用于比较两个不存在有意义顺序的元素时不再返回布尔值，而是抛出异常。**--------------------------------------------------------Python2.x版本----------------------------------**

```
&gt;&gt;&gt;1&lt;'a'

```

输出结果：

```
False

```

**--------------------------------------------------------Python3.x版本----------------------------------**

```
&gt;&gt;&gt;1&lt;'a'

```

输出结果：

```
Traceback (most recent call last):
  File "D:\anaconda3\lib\site-packages\IPython\core\interactiveshell.py", line 3437, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "&lt;ipython-input-2-126e4c86ad85&gt;", line 1, in &lt;module&gt;
    1&lt;'a'
TypeError: '&lt;' not supported between instances of 'int' and 'str'

```

**（6）整数类型** Python 3.x中的整型不再区分整型和长整型，`只保留int类型`，且int类型的长度只与计算机的内存有关，内存足够大，整数就能足够长；同时sys.maxint常量也被删除。

**（7）关键字** Python 3.x中增加了关键字`as`、`with`、`True`、`False`、`None`。

**（8）input()函数** Python 3.x中使用`input()`函数取代了`raw_input()`函数。

**（9）range()函数** Python 3.x中使用`list()`函数对`range()`函数的返回值进行转换，以实现2.x中`range()`返回列表的功能。**--------------------------------------------------------Python2.x版本----------------------------------**

```
&gt;&gt;&gt;range(5)

```

输出结果：

```
[0,1,2,3,4]

```

**--------------------------------------------------------Python3.x版本----------------------------------**`不用list:`

```
&gt;&gt;&gt;range(5)

```

输出结果：

```
range(0,5)

```

`用list:``````````

```
&gt;&gt;&gt;list(range(5))

```

输出结果：

```
[0,1,2,3,4]

```

**（10）异常** Python 3.x中使用as关键字标识异常信息。**--------------------------------------------------------Python2.x版本----------------------------------**

```
&gt;&gt;&gt;try:
	  raise TypeError,"类型错误"
   except TypeError,err:
      print err.message
	

```

输出结果：

```
类型错误

```

**--------------------------------------------------------Python3.x版本----------------------------------**

```
&gt;&gt;&gt;try:
	  raise TypeError("类型错误")
   except TypeError as err:
      print(err)
	

```

输出结果：

```
类型错误

```

### 1.6 小结

`首先`简单介绍了Python语言、编程语言、Python解释器、语言特点以及应用领域。

`之后`介绍了在Windows系统中安装和配置Python开发环境、运行Python程序的方法。

`然后`简单介绍了程序开发流程与编写方式，然后介绍了集成开发环境PyCharm的安装和使用

`最后`介绍了2.x版本和3.x之间的区别。

通过本文的学习，希望大家能够Python有个大致的了解，建立起学习的兴趣和信心，能够熟练搭建Python开发环境以及运行Python程序，并熟悉程序设计的流程与编写程序的基本方法。

### 1.7 拓展：常见Python集成开发环境(IDE)

[1] IDLE: Python解释器默认工具

[2] VS Code:  (被各大高校和科研院所青睐)

[3] PyCharm:  （本课程推荐）

[4] Anaconda: 

### 1.8 拓展：初学者常见问题

**Q1：Python语言、C语言、Java语言、VB语言……到底哪种适合作为入门编程语言呢？**

A1：Python是最好的程序设计入门语言、也是最先进的程序设计语言。如果只想学一门程序设计语言，请学Python；如果想学一门最先进的程序设计语言，请学Python。

**Q2：Python 2.x 和Python 3.x，该学习哪个版本？**

A2：Python 3.x，本教程的所有内容只讲授这个版本

与传统软件升级不同，3.x版本与2.x版本并不兼容，3.x版本2008年发布，至今，所有Python主流功能库都可以稳定且更高效地运行在Python 3.x版本下，专业Python程序员都已经使用Python 3.x版本，无可争议。

**Q3：Python语言是跨平台的吗？**

A3：Python语言所编写程序可以无需修改在Windows、Linux、UNIX、Mac等操作系统上使用。（严谨些：如果Python程序所调用的库是平台无关的，则可以跨平台。）

**Q4：Python语言是面向对象语言吗？**

A4：面向对象是程序设计方法的一种，Python语言并不局限于此。你可以学习面向对象程序设计方法，并利用Python语言实现，也可以仅仅用面向过程的基本方式，甚至，你可以没有任何风格的写几行代码，Python语言都是支持的。它就是这么任性！

**Q5：全国计算机等级考试二级Python科目有什么用？需要参加吗？**

A5：全国计算机等级考试二级（简称：等考）由教育部考试中心（高考、四六级和研究生考试也是这个官方部门组织的哦！）组织，主要面向高校学生及社会学习者开展的水平性考试，其中Python语言课目于2018年9月首次开考，每年3月和9月两次大考。等考对计算机专业学生没有太大意义，毕竟专业学生需要很专业；但对于非计算机专业学生证明计算机尤其是编程水平非常权威也比较有用。据说上海市落户的积分政策中有对计算机水平及等级考试的要求。

### 1.9 拓展：个人感悟

最近我在追一个电视剧，是改编自`烽火戏诸侯`写的《`雪中悍刀行`》(央视网可直接观看)，其中有一句话惊艳到我了

就是男主徐凤年问剑神李淳罡的剑术到底啥水平，李淳罡说了一句话：`“天不生我李淳罡，剑道万古如长夜”` （这句话实际上是改编自“天不生仲尼，万古如长夜”，仲尼就是万世师表：孔子）

为什么会被惊艳到呢？不知道从什么时候起，自己的生活开始变得波澜不惊，平静如一滩死水。

我记得大二的时候，参加电子设计大赛，在实验室奋战了4天3夜，中间休息了有两三个小时，比赛结束后就在实验室门口的废弃桌子上睡了整整一天。

研二的时候，连续作战60多个小时，就为了发表一篇二区SCI，在实验室，一抬头天黑了，再一抬头天又亮了，这种状态持续3天，中间实在熬不住，就睡了半小时，最终顺利发表了一篇二区SCI。

`当你为一件事下的劲越大，努力的时间越长，做成时的快乐，也是你刷多少抖音，赢多少游戏都享受不到的。`

我在想，我是从什么时候开始就没了那种年轻人的自负，骄傲，能打硬仗，敢打硬仗的豪情？

我已经快30岁了，慢慢失去这些东西也算是有点借口，但是看到我的学生，18岁左右，正是大好的青春年华，却没见到哪个同学有“老子天下第一“的豪气！，也没见哪个同学非常能吃学习的苦。

你们总是要毕业的，总是要走向社会的，这个世界，你不吃学习的苦，就要吃身体的苦，脑力劳动和体力劳动总要选择一个。

这篇文章是为我的学生写的，用了我大概四个多小时的时间，希望你们看到这，能激起你心底的自负出来，不要自信，就要自负，就是要”天不生我李淳罡，剑道万古如长夜“的自负。

不逼自己一把，永远不知道自己到底能多优秀！ 像张雪峰说的：`”你努努力，看看将来会发生什么！“`

很多学生说自己起点太低了，没有信心，但是我却见过很多惊才绝艳之人，起点更低。

命运确实给了你很低的起点，但是不是让你抱怨和颓废的，而是让你去奋斗出一个绝地反击的故事！人生只有走出来的美丽，没有等出来的辉煌，行动起来吧，python就是你精彩故事的开始！
