
--- 
title:  用Python构建一个电子表格应用程序的，以使数据科学变得更容易 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/8ab4555543cab66cb96824a03ad5d817.png">

<img src="https://img-blog.csdnimg.cn/img_convert/3633029768f49a3240c030afc6418811.png">

今天我是开源的“网格演播室 ", 一个完全集成Python编程语言的基于web的电子表格应用程序。

<img src="https://img-blog.csdnimg.cn/img_convert/5ec19da84bc4103f2c9b28a6de977e5c.gif">

大约一年前，我开始修改构建我一直想要的数据科学IDE的想法。在与MicrosoftExcel、R(Studio)和Python广泛合作之后，我设想了一些集成版本将如何使我的生活更轻松

为什么？

我与Gridstudio一起着手解决的主要问题是，在处理数据科学项目时，我在多个工具(如R Studio和Excel)之间来回往返时所经历的零散工作流。

导出CSV文件时，目瞪口呆碰上冻结应用程序窗口当我的行数太高或者想做的时候简单明了的事情，如在JSON文件中读取我受够了。现有的工具没有为我提供环境和相关的工作流，从而使我能够高效地工作。

这就是为什么我决定构建一些东西，将我的工作流程集成到一个单一的、现代的、易于使用的、适合我的数据科学需求的应用程序中。

它怎麽工作?

Gridstudio是一个基于web的应用程序，看起来非常类似于普通的电子表格程序，如GoogleSheet或MicrosoftExcel。然而，它的致命特性是Python语言的深度集成。

在表格结构中查看数据并直接操作它，对于几乎所有使用过计算机的人来说都是很自然的。

将这个简单的UI与成熟的编程语言(如Python)的功能结合起来，确实使它脱颖而出。

使用Python编写脚本是尽可能简单的：只需编写几行代码并直接执行即可。

<img src="https://img-blog.csdnimg.cn/img_convert/2d849ead44ce1624327c642a6bb4fa2c.png">

核心集成：对纸张的读写

Python集成的核心是电子表格的读写接口。Python过程中工作表的数据和数据之间的高性能连接。

只需写在纸上，如下所示：

```
sheet("A1:A3", [1, 2, 3])

```

从纸上读到：

```
my_matrix = sheet("A1:A3")

```

有了这个简单而强大的功能，您就可以直接读写表单，从而实现数据输入、提取、可视化等自动化。

编写自定义电子表格函数

虽然读写通过简单的界面提供了很大的灵活性，但有时编写可以直接在电子表格中调用的自定义函数很有意义。

常见的电子表格功能，如平均值、和、if等，在默认情况下已经可用。但如果你需要更多呢？

只需编写所需的函数即可！

```
def UPPERCASE(a):
 return str(a).uppercase()

```

现在，在电子表格中调用此函数，就像调用常规函数一样。

利用Python生态系统

通过利用Python生态系统的强大功能，您可以立即访问最先进的数据科学工具：

<img src="https://img-blog.csdnimg.cn/img_convert/57f1922a834f5a184d711e317ca81ebd.png">

这样就可以简单地访问功能强大的模型，例如线性回归和支持向量机为你的数据建模。

码头运行时

该应用程序运行在一个Docker容器中，它使您可以轻松地访问一个完全打包和隔离的UNIX环境(甚至在Windows上！)一切准备就绪：Python，Scikit-Learning，Numpa，熊猫，终端，wget，zip等等。

这使得安装Gridstudio就像下载预构建的码头映像和运行一个命令一样简单。

数据可视化

数据科学中的一个常见任务是可视化您的数据。鉴于其重要性，Gridstudio通过集成交互式绘图库Plotly.js和Python的标准Matplotlib，构建了对高级绘图的支持。这为您提供了矢量锐利格式的高级绘图功能。

<img src="https://img-blog.csdnimg.cn/img_convert/c2ae93f957529d40eacd50431e4c1f09.png">

为了给您提供一些关于如何使用Gridstudio功能的想法，我们将展示如何将它们与一些具体的示例结合起来。

例句：刮网

这个例子向您展示了将Python放在指尖的强大功能。通常需要在工具和文件之间来回切换的东西现在可以集成到单个脚本中。

<img src="https://img-blog.csdnimg.cn/img_convert/ebeb754d0ea27e96bed23d99240c6e7b.png">

上面，您可以看到一个简短的脚本如何轻松地将来自Hacker News的新闻文章直接加载到表单中。

资料来源：刮皮

示例：估计正态分布

这个例子展示了一个用Plotly.js可视化的更高保真度估计正态分布的有点傻的用例。在这里，你可以看到交互式的绘图是如何让你对正在发生的事情有一种感觉的。

<img src="https://img-blog.csdnimg.cn/img_convert/756a4784eb267f35db99fed221d57797.png">

资料来源：估计正常值

我该怎么用呢？

在本地安装Grid studio非常简单：

```
(Make sure you have Docker installed)
1. Clone the repository with this command:
git clone https://github.com/ricklamers/gridstudio
2. Run the bash script (on Windows use e.g. Git Bash) with this command:
cd gridstudio &amp;&amp; ./run.sh
3. Go to http://127.0.0.1:8080 in your browser

```

吉特巴什对于Windows-码头安装

注意：如果遇到问题，请随意打开发行在GitHub上，我将尽可能快地帮助/修复。

注意：在Linux上，您可能需要运行(对于步骤2)：

```
cd gridstudio &amp;&amp; sudo ./run.sh

```

因为Docker需要sudo访问才能运行。

发行+未来发展

如前所述，今天的Grid studio将通过GitHub储存库 .

如果您在这里，您非常欢迎您自己尝试，并提交任何反馈和/或贡献的项目上的GitHub。

对于将来可以添加哪些功能或特性来改进Gridstudio，我有一些想法。但是，由于该项目现在是开源的，我认为在GitHub上跟踪这些项目并根据所有相关人员查看哪些项目具有最高优先级是明智的。

-扩展电子表格中可用的“本机”函数的数量(如平均值、和、如果等)，甚至可能与一些现有的包(如Libre Office的Calc或Excel)达到奇偶校验(和一致性)

-在电子表格中键入公式时，语法突出显示/函数工具提示

-电子表格中的高级排序和筛选

-与Plotly.js交互绘图的扩展控件

-更容易共享工作区/代码(即导出工作区)

-实时协作的形式(这可能太困难了)

-一些用于外接程序/扩展的API/接口

-将公式解析器升级为真正的基于语法的解析器

-Python自动完成

-性能优化

-核心Python/工作表集成健壮性(没有字符/序列损坏)

开源动机

虽然这个项目最初是为商业发布而设计的，但我认为，作为一个开放源码项目，每个人都可以尝试使用它，并有可能由一个有兴趣的小型社区进行开发。

原因在于，在项目的最初开发过程中，我发现了许多项目，这些项目提供了与Gridstudio类似的功能。

首先，有一个直接将Python集成到microsoft excel中的开源插件木翅..尽管它并没有真正地将电子表格和Python集成到一个连贯的产品中，但它确实提供了让用户访问他们已经熟悉的“真实”满载Excel环境的优势。

第二，Python是从IPython到木星笔记本到木星实验室..它非常受欢迎，因此，它为数据科学家提供了一个非常好的工作环境，特别强调通过长形式笔记本编写可解释的代码。虽然，它缺乏任何一种电子表格功能，在我看来，是如此吸引新手数据科学家，因为它的非导向性行为。

总的来说，这样的项目意味着网格工作室的商业化将意味着与这些产品替代品竞争，这些产品可以极其低廉的免费价格获得。

无论如何，我真诚地相信Gridstudio确实有一些独特的东西可以提供现有的替代方案，并且可以成为相当多的用例的选择工具。

通过GitHub储存库 .

*声明：本文于网络整理，版权归原作者所有，如来源信息有误或侵犯权益，请联系我们删除或授权事宜。

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/2cf9d83c31a01b7e1d898341b3bb0ae9.gif">

微信扫码关注，了解更多内容
