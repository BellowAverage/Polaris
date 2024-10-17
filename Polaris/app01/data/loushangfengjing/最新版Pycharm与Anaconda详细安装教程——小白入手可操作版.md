
--- 
title:  最新版Pycharm与Anaconda详细安装教程——小白入手可操作版 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/b993bf1033164daf86dc956f378b44ee.png" alt="在这里插入图片描述">

**摘要**：本教程旨在为初学者提供一个易于理解和操作的指南，详细介绍了如何在 Windows 11系统上安装最新版本的 PyCharm 和 Anaconda。通过一系列清晰的步骤解析和配套截图，本文逐步引导用户完成 PyCharm 和 Anaconda 的安装过程，确保即便是编程新手也能轻松上手。



#### 文章目录
- - <ul><li>- - - - 


## 1. PyCharm安装步骤

PyCharm是一个写Python代码、运行项目的IDE软件（简单说起来就这样）。PyCharm 是一款专为 Python 语言设计的集成开发环境（IDE），由 JetBrains 公司开发。它为 Python 开发者提供了诸如代码自动完成、错误高亮、项目管理等实用功能，旨在提高编程效率。PyCharm 分为免费的社区版和功能更全面的专业版。无论是学习 Python、进行小型项目开发，还是处理复杂的编程任务，PyCharm 都是一个不错的选择。

### 1.1 下载安装包

Pycharm的下载没啥好说的呀，到官网的下载地址点下载社区版就可以，那样可以下载最新的版本。可以看我下面的步骤一步步找到官网下载的链接，当然有的不想动的可以从下面我给的网盘下载，放的是当前最新的Pycharm和Anaconda的安装版，只不过时间久了可能就不是“最新”了。

**安装包网盘链接**： 提取码：6ro0

（1）PyCharm是Jetbrains公司旗下的一款产品，所以下载官方的最新版应该去它的官网：，从“Developer Tools”（开发工具）一栏，点击下去，然后从中找到“PyCharm”，点击它可以进入Pycharm页面；（官网是一直变化的，但找到Pycharm的方式类似）

<img src="https://img-blog.csdnimg.cn/direct/c1716345ae804889971d44364a7b8265.png#pic_center" alt="在这里插入图片描述" width="600"> （2）点进去后就是下面的，再点击这里的“Download”，这时候就跳转到下载链接了；

<img src="https://img-blog.csdnimg.cn/direct/d09f74894d6b41b1b31b1da6b202974a.png#pic_center" alt="在这里插入图片描述" width="600"> （3）这时候进入，这里有两个版本一个是“Professional”专业版，还有底下的“Community”社区版。前者收费后者免费，如无特别要求我们选择社区版即可。点击下面的下载按钮： <img src="https://img-blog.csdnimg.cn/direct/36c3bbe16ff34ffda7176da571add694.png#pic_center" alt="在这里插入图片描述" width="600">

### 1.2 Pycharm安装过程

（1）下载好后找到下载的文件，可以双击运行它。如果你是前面给的网盘下的也是一样找到下载的位置打开：

<img src="https://img-blog.csdnimg.cn/direct/8d550eeba48544c582709d6436c38421.png#pic_center" alt="在这里插入图片描述" width="600"> （2）双击运行安装文件后会弹出权限控制，选择“是”同意安装。然后进入选择安装位置的界面（右图），点击“浏览”会弹出文件夹选择框，**选择一个新建的空文件夹位置作为你的安装位置**（别装C盘了，在别的盘新建一个英文文件夹，选择它作为安装目录），选中后点击“下一步”：

<img src="https://img-blog.csdnimg.cn/direct/e9b49a80f4624ef2852334cb91e8ffe0.png#pic_center" alt="在这里插入图片描述" width="500"> （3）接下来弹出一个安装选项的窗口，在这里可以**勾选“创建桌面快捷方式”和“更新PATH变量”**，然后点击“下一步”：

<img src="https://img-blog.csdnimg.cn/direct/cf9180615cdb4c8085fb6134c253af92.png#pic_center" alt="在这里插入图片描述" width="400"> （4）然后在下面的窗口中点击“安装”，将开启正式安装进程：

<img src="https://img-blog.csdnimg.cn/direct/3f5992f0cb5e44928fb6454623143f3e.png#pic_center" alt="在这里插入图片描述" width="400"> （5）点击完成后，等待进度条结束，如下，这里可能要一段时间：

<img src="https://img-blog.csdnimg.cn/direct/1832f1a0f1f149108d81232889fe9782.png#pic_center" alt="在这里插入图片描述" width="400"> （6）等待安装进度条结束后，会显示安装程序结束，这时我们点击“完成”：

<img src="https://img-blog.csdnimg.cn/direct/d80f316703874bdcbf0af27e18260441.png#pic_center" alt="在这里插入图片描述" width="400">

（7）完成之后可以在桌面找到Pycharm的快捷方式，可以双击运行软件，也可以在开始菜单那里搜索“Pycharm”找到启动项打开：

<img src="https://img-blog.csdnimg.cn/direct/1498f2f6cd224142a7680e15d8bf072c.png#pic_center" alt="在这里插入图片描述" width="600">

（8）初次启动Pycharm一开始会有一个载入设置的窗口（如下图），这个地方选择“Do not import settings”，然后点“OK”就可以；

<img src="https://img-blog.csdnimg.cn/direct/af63a2acdf58490c88d200bbedbcced6.png#pic_center" alt="在这里插入图片描述" width="400"> （9）这时候进入到下面的窗口，点击“Open”，可以选择已有项目的文件夹打开；

<img src="https://img-blog.csdnimg.cn/direct/5685508f888c48fb9b9b95016e90fc67.png#pic_center" alt="在这里插入图片描述" width="600">

至此Pycharm的安装就完成了，关于这个软件的使用，我们在后面的博客中介绍怎么操作。现在可以关闭这个软件继续安装我们后续的Anaconda的安装。

## 2. Anaconda安装步骤

Anaconda 是一个流行的 Python 和 R 语言的发行版本，特别适用于科学计算、数据科学和机器学习领域。它包含了大量的预装库和工具，使得用户能够方便地管理项目、环境和包。Anaconda 通过其包管理器 Conda，允许用户轻松安装、运行和更新各种科学计算和数据分析所需的库。此外，Anaconda 还提供了虚拟环境管理功能，使得用户可以为不同的项目创建隔离的环境，以避免依赖冲突。Anaconda 的这些特性大大简化了数据处理和分析的工作流程，是数据科学家和研究人员的理想工具。

Anaconda的安装稍有点要注意的地方，这个软件的安装涉及到添加环境变量已经安装位置的设置。有的朋友安装的时候非常随意，选择默认安装的C盘临时位置，环境变量也鼓捣不动，最后装好后使用conda来创建环境的时候，问题就会很多。不过按照我这里的步骤可以帮你避过这些问题了，跟着我的步骤操作吧。

### 2.1 下载安装包

Anaconda的下载方式类似，也是到官网上找到下载链接下载，官网放的都是新版的，可以按照我下面的步骤下载。也可以从网盘下载，与上面的PyCharm都放在下面的网盘中了，有需要自取吧。

**安装包网盘链接**： 提取码：6ro0

（1）首先我们进入Anaconda的官网：，如果官网没有变化的话，右侧有一个“Free Download”，点击它进入下载页面：

<img src="https://img-blog.csdnimg.cn/direct/8aedaf67676c485c95d47b7f9195880d.png#pic_center" alt="在这里插入图片描述" width="600">

（2）然后你就能在上看到有个“Download”按钮，点击它可进行下载，注意自己下载的文件夹位置，方便后面找到它：

<img src="https://img-blog.csdnimg.cn/direct/5ca9b09f9a944762b2bf2a9fababdd62.png#pic_center" alt="在这里插入图片描述" width="700">

（3）我下载好后的文件如下，圈出的地方就是Anaconda的安装包，下面我们用它来进行安装：

<img src="https://img-blog.csdnimg.cn/direct/160fb26b40204cea881408826a2b3297.png#pic_center" alt="在这里插入图片描述" width="600">

### 2.2 安装过程

（1）找到刚刚下好的安装包，我们可以**双击运行**这个软件，出现下面的引导界面，点击“Next”：

<img src="https://img-blog.csdnimg.cn/direct/5dde02fe3bba4ee1a1f9650cbf653172.png#pic_center" alt="在这里插入图片描述" width="500"> （2）出现下面的是否同意协议，我们选择“**I Agree**”，然后继续：

<img src="https://img-blog.csdnimg.cn/direct/58bf8eed1c2d44198d9fd882642670e3.png#pic_center" alt="在这里插入图片描述" width="500">

（3）下面的界面是问我们选择为哪些用户安装，这个用户指的是你的电脑的用户账户，对于你的个人电脑来说勾选哪个都一样的，这里我们就默认的“Just Me”，如下，再点击“Next”：

<img src="https://img-blog.csdnimg.cn/direct/54fd090de66747c2860631b7526cc74a.png#pic_center" alt="在这里插入图片描述" width="500"> （4）下面这里比较重要，这是**选择安装Anaconda的安装位置**，这个位置非常重要！因为这个位置确定下来后，后面新建Python环境，切换环境，那些文件可都是默认放在这个文件夹下的（除非你特别指定）。

所以这里不要装在C盘，不要装在C盘，不要装在C盘！（除非你只有C盘）。

我们**在别的盘新建一个文件夹，这个文件夹你需要记得住的**，比如我这里的“F:\Anaconda”。如果图省事而瞎打一个，后面找不到非常麻烦，So，别给自己找事。

<img src="https://img-blog.csdnimg.cn/direct/66907d13e73b492d8718f3a5a6fc264d.png#pic_center" alt="在这里插入图片描述" width="500"> 我们点击这里的“Browser”按钮会弹出文件夹选择框，在框里面选择你刚刚新建好的文件夹，我这里是“F:\Anaconda”，点击“确定”：

<img src="https://img-blog.csdnimg.cn/direct/b8bfb8232ee042c4b1116acf942673b5.png#pic_center" alt="在这里插入图片描述" width="700"> 选择好安装位置后，点击“Next”：

<img src="https://img-blog.csdnimg.cn/direct/f86a992dcb2948a793bd2dbdcef6fcb1.png#pic_center" alt="在这里插入图片描述" width="500"> （5）接下来进入的设置界面更加重要，这里是一个安装选项，默认只勾选了其中两项。然后还有一项“**Add Anaconda3 to my PATH environment variable**”，也就是下图红色字体处，这个意思是帮我们添加Anaconda的环境变量到电脑的系统环境变量当中。

<img src="https://img-blog.csdnimg.cn/direct/22afe198d8bd47829a9571435dd13ce8.png#pic_center" alt="在这里插入图片描述" width="600"> PS：这个地方我解释一下，如果我们不添加环境变量，要想在电脑自带的终端cmd或powershell中，以命令“conda xxx”去使用conda时，会提示你找不到这个命令。如果此时不勾选，而又要在cmd中用conda，那么就要手动添加环境变量，容易出错也更加麻烦，还不如这里勾上让程序帮我们自动添加。当然，我们并非只能在系统带的cmd中使用，装好Anaconda后，这个软件提供了Anaconda Prompt终端工具，也可以在这里用conda命令，而不用管环境变量是否有添加。

不想看你就勾上就是了，有的版本的安装包运行下来没有添加环境变量的选项，那后面就直接用Anaconda Prompt终端工具吧。

（6）**勾上这里的添加环境变量**，然后我们点击“**Install**”，开始正式安装：

<img src="https://img-blog.csdnimg.cn/direct/733f5d00e1b84caeabed9633961dbdda.png#pic_center" alt="在这里插入图片描述" width="500"> （7）这个地方等待进度条结束，然后点击“Next”：

<img src="https://img-blog.csdnimg.cn/direct/7c87121443ec476ca113b86f92c4029b.png#pic_center" alt="在这里插入图片描述" width="500">

（8）如下图所示，点击“Next”，点击“Finish”这部分安装就完成了。

<img src="https://img-blog.csdnimg.cn/direct/ca85dd219bf14ddaae348f2f6cd3995b.png#pic_center" alt="在这里插入图片描述" width="700"> （9）OK安装完成，要是弹出运行了Anaconda会是下面这个样子，我们关掉它就好了。

<img src="https://img-blog.csdnimg.cn/direct/3cb266ed8fa34b7eb4db283576ea4cf8.png#pic_center" alt="在这里插入图片描述" width="700">

### 2.3 测试安装是否成功

我们在前面几步中安装好了Anaconda，这里还是测试一下看看是否操作成功。

（1）我们在开始菜单那里点搜索框，搜索“cmd”，在结果那里找到“命令提示符”，点击打开这个工具：

<img src="https://img-blog.csdnimg.cn/direct/2b18a94499a44d7f8ed8ea2b7bdaa7c5.png#pic_center" alt="在这里插入图片描述" width="500">

（2）我们在打开的cmd命令行中输入“conda --version”，然后回车，可以看到conda的版本。

这表面conda已经安装好，并且环境变量是添加好的，后面我们可以直接使用cmd的命令行来做创建环境、激活、安装等操作了。

<img src="https://img-blog.csdnimg.cn/direct/bcd5d35580304ee49b3fda115eb38483.png#pic_center" alt="在这里插入图片描述" width="700"> （3）接下来我们再用Anaconda Prompt来测试一下，同样的我们在开始栏搜索“Anaconda Prompt”，可以在结果中找到如下，点击它打开这个工具界面；

<img src="https://img-blog.csdnimg.cn/direct/2d601394d81343dab3b0228510bd3593.png#pic_center" alt="在这里插入图片描述" width="500"> （4）这时我们在下面的窗口输入“conda --version”，同样会得到conda的版本，表示conda命令是有效的。至此我们已经验证过了Anaconda安装没有问题了，可以愉快开始后面的环境管理操作。

<img src="https://img-blog.csdnimg.cn/direct/d33d6434376e431fbfe06eab70b24204.png#pic_center" alt="在这里插入图片描述" width="700">

## 3. 写在最后

以上我们顺利完成了 **PyCharm** 和 **Anaconda** 的安装，算是已迈开了成为 Python 开发者旅程的第一步。请记住，本教程仅覆盖了软件安装的部分，而学习如何充分利用这些强大工具进行编程和项目管理的精彩内容，我们将在后续的教程中徐徐展开。

接下来，我们会深入讲解如何借助 **PyCharm** 的高级功能提升编程效率，以及如何使用 **Anaconda** 来管理依赖关系和创建独立的环境，确保我们的开发过程井井有条、高效流畅。无论是着手于数据分析还是深度学习项目，这些技巧都将极大地优化我们的工作流程。

需要注意的是，随着官方网站的更新，软件及其安装包的版本可能会发生变化。我们会保证本教程中的内容保持最新，以便您随时都能使用到最新版本的软件。因此，建议您定期查看本教程，获取最新的安装信息和使用技巧。

最后，博主鼓励在安装或使用过程中遇到任何问题时，积极寻找解决方案并与社区分享您的经验。在编程与科研的世界里，面对并解决问题是成长的重要一环。保持乐观的心态，享受编程之旅带给你的乐趣吧！
