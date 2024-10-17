
--- 
title:  在Pycharm中使用离线依赖包安装Python环境——小白入手版图文教程 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/dedb92dc0ed242c8aa91a20a84fcc90d.png#pic_center" alt="在这里插入图片描述" width="700">

摘要：本篇博客专为初学者设计，旨在指导如何在PyCharm中使用离线依赖包进行安装，以避免在线下载时可能遇到的网络问题。使用离线包安装的方法不仅可以确保在网络不稳定或无网络环境下依旧能够进行依赖包的安装，还能保证根据作者提供的包列表准确无误地安装所需依赖，避免版本不兼容等问题。本教程将详细介绍如何准备和配置PyCharm以使用离线包，包括如何在没有网络连接的情况下下载离线包，如何将这些包导入到PyCharm项目中，以及如何配置虚拟环境以确保依赖包的正确安装。通过本文的指导，初学者可以轻松掌握使用离线包在PyCharm中安装和管理依赖的技巧，从而在任何网络环境下都能顺畅地运行Python程序。



#### 文章目录
- - - - - - - - 


## 引言

无论你是编程新手，还是对编程感兴趣的极客，学习Python都是一个不错的起点，人生苦短，我用Python。Python以其直观的语法、丰富的库支持和广泛的应用范围而受到初学者和专业人士的青睐。它不仅是学术和职业发展的重要工具，也是许多人用于自动化日常任务的首选语言。

然而，对于初学者来说，配置适合的Python开发环境往往是进入编程世界的第一大障碍。环境配置不当很可能导致代码无法正常运行，从而影响白嫖别人代码的进度和小白的开发效率。PyCharm是一款深受欢迎的Python集成开发环境（IDE），提供了诸如代码自动补全、语法高亮和强大的调试功能等，极大地提升了开发效率。在这篇博客中，我们将重点介绍如何在PyCharm中使用离线依赖包安装，避免因网络问题而影响到依赖管理和项目构建，即使在没有网络连接的情况下也能保证项目的顺利进行。

## 1. 安装PyCharm和Anaconda

在我们开始介绍如何使用PyCharm和Anaconda配置一个合适的Python开发环境之前，有必要先确保在你的电脑上已经安装了这两个重要工具。如果你还没有安装Anaconda和PyCharm，我之前已经发布了一篇详细的安装教程，可以通过以下链接访问：。

这篇博客详细介绍了如何在不同操作系统上安装Anaconda和PyCharm，包括常见问题的解决方案。强烈建议按照博客中的步骤进行操作，以确保安装过程顺利无误。成功安装了Anaconda和PyCharm，就可以继续我们后面的内容，用它们配置一个自己的Python开发环境。

## 2. 安装配置思路

由于本教程可能看的初学者比较多，我先说明一下思路。初学时差不多很多时候我们是先跑通别人的项目代码，然后自己运行调试去学习和积累经验。也就是先白嫖别人的代码，再尝试看懂和修改。在接手一个新的Python项目并准备在PyCharm中打开并运行它之前，有几个关键步骤需要注意：
1.  **检查项目推荐的Python版本**：在开始之前，先检查项目文档或`README`文件，了解开发者推荐的Python版本。这一步是确保项目运行环境与开发环境一致的前提。 1.  **查看项目依赖**：同样重要的是查看项目所需的依赖库及其版本。这些通常在`requirements.txt`文件或文档中明确列出。没有给出依赖版本的项目不是好的项目，如果没有就只能凭经验推断或装一个版本试试，不行再换版本试错。 1.  **创建专属Python环境**：基于上述信息，建议使用Conda为每个项目创建一个独立的Python环境。这样做可以避免不同项目间的依赖冲突，并确保环境的纯净性。 1.  **安装特定版本依赖**：在新创建的Python环境中，按照项目推荐的依赖版本进行安装。这一步确保了项目能够跟原作者一样的运行环境下运行，保证你运行代码时不会出错。这个地方我们使用离线依赖包直接安装，就不用再一边下载一边安装了。 
说白了就是看看作者有没有给指定Python版本和依赖版本，如果给了那就按照他那个来，版本和作者的一致出错概率应该最小，要知道配置好环境运行出来才是正道。（我见过很多初学者Python不熟悉，还喜欢弄些花里胡哨的，什么都装最新的，比如最新的Python版本整个12、13，依赖库都用最最新的，殊不知新版坑多没人蹚过，编程老手都不敢随便升级，也就是新手敢这么整，结果就是错误一大堆，自己根本无从下手。）

## 3. 创建Conda环境

在成功安装Anaconda之后，接下来的重要步骤是学会创建和管理Conda环境。Conda环境是一个隔离的空间，允许用户为不同的项目安装不同版本的软件包和Python，这样可以避免包之间的冲突和依赖问题。

下面以我自己的项目为例，打开项目文件夹之后会看到两个txt文件，分别是“环境配置.txt”和“requirements.txt”。其中“环境配置”中给了用Conda安装环境的步骤，而“requirements”中给了依赖包的版本。所以这里我们的目标是创建一个Python 3.10的环境，并且安装“requirements.txt”给定的依赖版本。

<img src="https://img-blog.csdnimg.cn/direct/f2d7dbf92a074edc92f5fc6e86119b16.png#pic_center" alt="在这里插入图片描述" width="700">

**（1）打开命令行界面**：首先，需要打开命令行界面。在Windows上，可以在开始菜单那里搜索并打开“**Anaconda Prompt**”（注意不是Anaconda Powershell Prompt ！），而在macOS或Linux上，可以直接使用标准的终端。

<img src="https://img-blog.csdnimg.cn/direct/453ff6f3352745d68ad5936cd82a356c.png#pic_center" alt="在这里插入图片描述" width="500">

如果这里你没有出现“Anaconda Prompt”，那可能你没有安装Anaconda，可以按照我上一篇博客：上面的步骤安装好，再进行这里后面的操作。

**（2）创建新的Conda环境**：通过以下命令来创建一个新的Conda环境，这里我们将环境命名为`env_rec`，同时指定Python版本为3.10。

```
conda create -n env_rev python=3.10

```

在这个命令中，`-n env_rec`定义了新环境的名称（我这里是`env_rec`），`python=3.10`确保在这个环境中安装了Python 3.10版本。

**操作步骤**：如下图所示，我们在Anaconda Prompt的命令行中输入“conda create -n env_rev python=3.10”（这里你可以复制），然后回车：

<img src="https://img-blog.csdnimg.cn/direct/ed0219dff79c4d1790e199fc0fa7ea98.png#pic_center" alt="在这里插入图片描述" width="700">

按下回车后，你会看到下面的让我们是否确认安装，输入英文“y”，然后回车：

<img src="https://img-blog.csdnimg.cn/direct/9afbfc5eb904498582b9712a381a6697.png#pic_center" alt="在这里插入图片描述" width="700">

这里创建环境完成之后，会是下面的样子：

<img src="https://img-blog.csdnimg.cn/direct/0c2c37993abf40629cb69831b6d9a2ab.png#pic_center" alt="在这里插入图片描述" width="700">

（3）**激活新的环境**：创建环境后，我们需要激活它才能开始使用。在命令行中输入以下命令：

```
conda activate env_rec

```

一旦环境被激活，的命令行提示符会变化，通常会包含环境的名称（在本例中为`env_rec`），这表明当前操作是在该环境中执行的。

**操作步骤**：如下图所示，输入“conda activate env_rec”然后回车，你会看到左侧的环境名被修改了，从原本的“base”变成了“env_rec”，这表示我们激活这个环境成功了，后面的操作是对这个环境进行的。如果你没有变化可能这步操作有问题，则需要检查。

<img src="https://img-blog.csdnimg.cn/direct/67b3e1668e284daca94952ff77c9d329.png#pic_center" alt="在这里插入图片描述" width="700">

**（4）验证环境和Python版本**：为了确认环境被正确创建并且Python版本符合我们预期，可以在激活的环境中运行以下命令：

```
python --version

```

这将显示Python的版本号，应该与您安装的版本（在本例中为3.10）相匹配。

**操作步骤**：在命令行继续输入“python --version”，然后回车，如下图所示，可以看到当前激活的环境的Python版本。这里我们显示的是`3.10`，说明是我们要装的版本（如果这里显示的和当初创建的不一样，那需要检查一下激活操作是否成功）：

<img src="https://img-blog.csdnimg.cn/direct/1d901984468e4edab9d432c777fe3539.png#pic_center" alt="在这里插入图片描述" width="700"> 现在已经新建好合适版本的Python环境了，接下来安装依赖库，需要用到离线安装包，博主分享的代码后面都会给出离线依赖库安装包的下载链接，你可以直接在对应博客给的链接中先下载好这些文件，下面的步骤中会用到。

## 4. 下载离线依赖包

在平时的Python开发过程中，我们通常会使用`pip install`命令来安装所需的依赖包。这个过程往往包括从指定的源下载安装包，并在下载完成后立即进行安装。虽然这种方式对于大多数情况都非常高效和方便，但当我们遇到网络连接缓慢或不稳定时，这就可能成为一个问题。下载速度的不确定性不仅会延长安装时间，有时甚至可能导致安装过程中断，影响我们白嫖代码的进度。

为了解决这一问题，作者已经将所有需要的离线依赖包预先下载好，并打包上传到了网盘中。这样，你就可以直接从网盘下载整个包的压缩文件，无需担心网络速度或稳定性的问题。下载完成后，你将拥有所有需要的依赖包的本地副本，可以随时进行安装，而不再依赖网络连接。

**离线依赖包下载地址**： （提取码：mt8u）

**注意**：上面是博主后面分享项目用到的Python环境的离线依赖包，是用于特定项目的环境安装的，如果你不使用博主分享的项目代码则无需下载。

（1）我们从网盘下载后的文件如下图所示，打开“rec_lib”文件夹，可以看到里面都是whl文件，其实就是我们后面要安装依赖库的安装包，后面需要用到这些文件，安装时就无需再下载了。

<img src="https://img-blog.csdnimg.cn/direct/c2b7b4cc162846b5bd246b4763a82f64.png#pic_center" alt="在这里插入图片描述" width="700"> （2）找到你下载好的**代码项目文件**的位置，你可能下到的是一个zip压缩包文件，那么解压出来，这里我解压出来的项目文件夹是“F:\python\EmotionDetection\EmotionDetection”（你可能是别的项目名，这里是类似的）。我们需要把这个安装包文件夹（rec_lib文件夹）复制到你的项目文件夹中，就是如下图所示的样子：

<img src="https://img-blog.csdnimg.cn/direct/bfc39346bdf5486f8c5919e14fd0efd5.png#pic_center" alt="在这里插入图片描述" width="700">

在上面图中，“rec_lib”文件夹和项目的依赖版本文件“requirements.txt”是在同一个目录下，这一点比较重要，因为我们后面用离线依赖包安装时需要同时用到这两者，所以注意不要复制错了位置哦。

## 5. 安装离线依赖库

（1）因为我们下面要在命令行中用到你的项目文件夹目录，所以在这里复制一下这个路径，也就是你刚刚打开的项目文件夹（我的是“F:\python\EmotionDetection\EmotionDetection”），上面选中复制一下：

<img src="https://img-blog.csdnimg.cn/direct/2803c9edbfba4e1ca70aa0ee3f184594.png#pic_center" alt="在这里插入图片描述" width="700"> （2）还是回到前面的那个**命令行窗口**（第三节第（4）步的Anaconda Prompt窗口），你应该有注意到你每次输入命令前的都有个路径，我这里是“C:\Users\lab321-1”，这个表示你当前进行的操作是在这个目录下进行的。那如果我们要用到上面文件夹中的“requirements.txt”呢，它显然不在这个目录吧，所以我们需要切换目录！

<img src="https://img-blog.csdnimg.cn/direct/15852092b97143a090c8055263749d80.png#pic_center" alt="在这里插入图片描述" width="400">

那怎么切换目录呢，输入“cd F:\python\EmotionDetection\EmotionDetection”（看清楚了，这里的“F:\python\EmotionDetection\EmotionDetection”这是我的路径，你的应该是你复制的自己项目的文件夹路径！），所以**你输入时应该是先打cd，空格，然后Ctrl + V，粘贴你上面复制的路径**。这就是为啥上面要让你复制路径。

```
cd 你的路径

```

你可以看看下面的图我的输入，对应的应该是cd到你自己的路径： <img src="https://img-blog.csdnimg.cn/direct/421aa2c5e42e45239bff153c080d2984.png#pic_center" alt="在这里插入图片描述" width="600">

如上图，输入那个cd命令后回车，你会发现没啥变化，有的电脑这么输入左边那个路径提示会直接变成切换后的，有的就像我这里一样没反应。这就**需要再输入盘符，这里我的是F盘，所以输入**“**F:**”，如下图就切换到我们需要的路径了：

<img src="https://img-blog.csdnimg.cn/direct/378c7faf420b4ea98a138cc092f80488.png#pic_center" alt="在这里插入图片描述" width="600">

（3）**安装离线依赖**： 在命令行中，使用`pip`命令和`-r`选项来指定`requirements.txt`文件，同时使用`--no-index`选项告诉pip不要使用Python包索引，因为我们希望pip只搜索本地文件夹。使用`--find-links`选项来指定本地`.whl`文件所在的目录，这样pip就知道从哪里寻找这些文件。命令如下：

```
pip install --no-index --find-links=rec_lib -r requirements.txt

```

这条命令告诉pip根据`requirements.txt`文件中列出的依赖，去`rec_lib`文件夹中寻找对应的`.whl`文件进行安装。通过这种方式，pip将不会尝试从外部源下载任何东西，从而避免了因网络问题导致的安装失败。

**操作步骤**：复制上面的代码“pip install --no-index --find-links=rec_lib -r requirements.txt”到命令行中，然后回车，这样就会帮我们安装所有的依赖库了，如下图所示

<img src="https://img-blog.csdnimg.cn/direct/8b3d57ab068147fcbc6d06ece7994033.png#pic_center" alt="在这里插入图片描述" width="600">

这个过程将会比较快，因为不用再下载了，只需要等到所有依赖库都装完，如下图所示，这样我们需要安装的环境依赖就完成了：

<img src="https://img-blog.csdnimg.cn/direct/1d38076535234c2e9b1ced542d0ca3ad.png#pic_center" alt="在这里插入图片描述" width="600">

## 5. 配置PyCharm解释器

刚刚上面装好的是Python的环境，要想运行代码，我们应该用PyCharm打开这个项目，但PyCharm并不知道用哪个Python环境去运行你这个项目，所以还需要在里面设置一下，指定这个环境为我们刚刚创建好的。故有以下的步骤，设置环境然后好运行。

（1）**打开PyCharm项目**：可以从File–&gt;Open–&gt;选择你的项目文件夹–&gt;OK，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/c38be2d67a704fa6843c7aa08d7a15bb.png#pic_center" alt="在这里插入图片描述" width="600">

点击Ok后可能有下面的弹窗，选择“Trust Project”即可，然后选择“New Window”打开项目：

<img src="https://img-blog.csdnimg.cn/direct/0b2340eccb61441581d036a4cf93ed1e.png#pic_center" alt="在这里插入图片描述" width="400"> <img src="https://img-blog.csdnimg.cn/direct/eee4ae1e18e6436786657177e32ac5c3.png#pic_center" alt="在这里插入图片描述" width="400">

打开项目后的样子如下，目前为止只是把项目打开了，下面要开始选择Python环境。

<img src="https://img-blog.csdnimg.cn/direct/b55312009ee343e29287eb73a4a8aa72.png#pic_center" alt="在这里插入图片描述" width="700">

（3）**设置和选择Python环境**：我们在PyCharm中以此选择File–&gt;Settings–&gt;Project–&gt;Python Inerpreter，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/72d4a24b9198492ab7c7b9bdc71f33e0.png#pic_center" alt="在这里插入图片描述" width="700"> 在弹出的设置窗口中，点击左侧的“Python Inerpreter”，然后点击右侧的展开下拉框，滚动到下面有个“Show All”，点击它进到环境配置窗口：

<img src="https://img-blog.csdnimg.cn/direct/2ceb089c15dc43be8f97d59e70ac7913.png#pic_center" alt="在这里插入图片描述" width="700"> 这时候的窗口如下，左边有个加号，点一下它，就会变成右边的窗口，这里选择“System Interpreter”，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/26fb9446c08744fa9e1a815619b1cb92.png#pic_center" alt="在这里插入图片描述" width="700"> 点击窗口右侧的三个点按钮，这里选择我们配置好的Python环境的目录，注意这个地方新手很容易出错，不知道选什么，我解释一下：

你看到的我选的目录“F:\Anaconda\envs\env_rec\python.exe”，可以分成两段：
1. F:\Anaconda\，这个是Anaconda的安装目录；1. envs\env_rec\python.exe，这表示用Conda创建的名为“env_rec”的环境，后面的Python.exe表示用这个Python程序；
现在你明白了吧，这个目录是“你的Anaconda安装目录+环境名+python.exe”这种组织方式，“env_rec”是我们第三节步骤里面新建的python环境名。这里就是要选那个前面创建并装好依赖库的环境位置。

**操作步骤**：如下图所示，点击窗口右侧的三个点按钮，这里选择我们配置好的Python环境的目录，选中你的环境位置的python.exe，然后点击OK：

<img src="https://img-blog.csdnimg.cn/direct/cc38fd61ba3f4a66b7f5ea9f61f778b0.png#pic_center" alt="在这里插入图片描述" width="600"> 选择好exe文件，然后可以点击“OK”，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/1062b0b34b62464bb2c1b0c425c0d144.png#pic_center" alt="在这里插入图片描述" width="600">

然后应该是下面这个确认窗口，点击“OK”：

<img src="https://img-blog.csdnimg.cn/direct/8c21a16e0cd649019117749c84745860.png#pic_center" alt="在这里插入图片描述" width="600"> 选中后就会出现下面的依赖库界面，显示了依赖包名称和版本，这时只需要点击“OK”

<img src="https://img-blog.csdnimg.cn/direct/ee7ca84f6f8a400d9dcf8a7d781bcc76.png#pic_center" alt="在这里插入图片描述" width="600"> 选好环境后底下有个进度条，这是在加载资源，我们等它进度条走完：

<img src="https://img-blog.csdnimg.cn/direct/84ccb10264d645ff8a5d2f2b0e83fed3.png#pic_center" alt="在这里插入图片描述" width="600">

等资源加载完成，我们双击打开项目里面的“run_main_web.py”，然后在代码编辑区域右击，选择“Run ‘run_main_web’”，便可以运行主程序了。

<img src="https://img-blog.csdnimg.cn/direct/49899ebbf84540b98e03db4331e84d84.png#pic_center" alt="在这里插入图片描述" width="700">

点击运行后启动程序，这个地方由于我的项目是一个Web项目，使用的streamlit这里第一次运行时会有以下的验证，你只需要在下面那个“Email: ”后面敲一个回车就可以了。

<img src="https://img-blog.csdnimg.cn/direct/eaea4c80fe4143d7b836f661fecc3a8d.png#pic_center" alt="在这里插入图片描述" width="800">

然后会跳出下面的信息，稍等一会应该会自动打开浏览器，启动Web应用。

<img src="https://img-blog.csdnimg.cn/direct/e34e160b7cba4b4b9bdd60ee01fde654.png#pic_center" alt="在这里插入图片描述" width="600"> 如下图所示，启动后的界面如下：

<img src="https://img-blog.csdnimg.cn/direct/7976f1a320ff4adca6aced234e22cefd.png#pic_center" alt="在这里插入图片描述" width="700">

选择一张图片上传，识别的效果如下，看上去还不错，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/38a7e1d8d98c479196d9444eb31298b3.png#pic_center" alt="在这里插入图片描述" width="700"> 至此这个项目的环境配置和运行就完成了。

## 写在最后

随着我们完成了离线依赖包的安装步骤，现在你应该已经成功配置了自己的Python开发环境，并且准备好开始探索和开发Python项目了。采用离线安装的方式确保了即使在没有网络连接的情况下，项目的依赖也能准确无误地被安装，使得项目能够在一个干净、一致的环境中运行。

虽然在线安装依赖是最常见的方式，但在某些特定情况下，如网络限制、速度慢或者安全政策等原因，直接从互联网下载依赖可能并不可行。正因如此，掌握使用离线依赖包进行安装的技巧变得尤为重要。这不仅能够帮助你在没有稳定网络连接的环境中顺利进行开发工作，也为确保项目的依赖管理提供了一个可靠的解决方案。感谢看到这里，希望这篇文章能够帮助顺利开始你的Python编程之旅吧，比心。
