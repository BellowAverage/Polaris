
--- 
title:  使用Pycharm和Anaconda配置Python环境图文详解教程——小白逐步操作版 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/dedb92dc0ed242c8aa91a20a84fcc90d.png#pic_center" alt="在这里插入图片描述" width="700">

摘要：新建特定版本的Python环境并在PyCharm中进行设置是一项常用技能，本篇博客为初学者提供了非常详尽的教程，介绍了如何使用PyCharm和Anaconda配置Python开发环境。文章首先介绍了安装Anaconda和PyCharm的步骤，然后深入讲解了如何创建和管理Conda虚拟环境，包括如何为特定项目创建一个指定Python版本，以及如何在项目中安装特定依赖。最后介绍了在PyCharm中配置Python解释器，确保开发环境与项目需求相匹配。



#### 文章目录
- - - - - - - 


## 引言

无论你是深度学习爱好者、 aspiring data scientist，还是简单地对自动化日常任务感兴趣，掌握Python都一项宝不错的技能，即便不是技能也可能是完成课业、工作不得不用的工具。Python以其简洁的语法、强大的库支持和广泛的应用场景著称，成为了初学者和专业开发人员的首选编程语言。

怎么说呢，开始学习Python之旅的第一步往往是配置开发环境，这对许多初学者来说可能真是一大挑战。很多人刚学的人不说写代码，可能拿到一份代码都难以跑通，很大部分原因是环境的影响。选择合适的工具和配置确实可以大大提高开发效率，使学习过程更加顺畅。在这篇教程中，将引导你通过使用PyCharm和Anaconda来搭建一个强大且灵活的Python开发环境。

简单说一下吧，PyCharm是一款广受欢迎的Python IDE，以其丰富的功能和易用性著称。它提供了代码自动完成、错误高亮、强大的调试工具等功能，帮助开发人员提高编码效率。Anaconda是一个开源的Python发行版，它包括了科学计算和数据科学中常用的许多库，其包管理器和环境管理器使得包的安装和环境的控制变得轻而易举。

通过结合PyCharm和Anaconda的优势，我们可以创建一个功能全面、适应性强的Python开发环境，为各种项目和研究提供支持。无论你是Python新手，还是希望优化现有的工作流程，本教程应该都能有点作用的。

## 1. 安装PyCharm和Anaconda

在我们开始介绍如何使用PyCharm和Anaconda配置一个合适的Python开发环境之前，有必要先确保在你的电脑上已经安装了这两个重要工具。如果你还没有安装Anaconda和PyCharm，我之前已经发布了一篇详细的安装教程，可以通过以下链接访问：。

这篇博客详细介绍了如何在不同操作系统上安装Anaconda和PyCharm，包括常见问题的解决方案。强烈建议按照博客中的步骤进行操作，以确保安装过程顺利无误。成功安装了Anaconda和PyCharm，就可以继续我们后面的内容，用它们配置一个自己的Python开发环境。

## 2. 安装配置思路

由于本教程可能看的初学者比较多，我先说明一下思路。初学时差不多很多时候我们是先跑通别人的项目代码，然后自己运行调试去学习和积累经验。在接手一个新的Python项目并准备在PyCharm中打开并运行它之前，有几个关键步骤需要注意：
1.  **检查项目推荐的Python版本**：在开始之前，先检查项目文档或`README`文件，了解开发者推荐的Python版本。这一步是确保项目运行环境与开发环境一致的前提。 1.  **查看项目依赖**：同样重要的是查看项目所需的依赖库及其版本。这些通常在`requirements.txt`文件或文档中明确列出。没有给出依赖版本的项目不是好的项目，如果没有就只能凭经验推断或装一个版本试试，不行再换版本试错。 1.  **创建专属Python环境**：基于上述信息，建议使用Conda为每个项目创建一个独立的Python环境。这样做可以避免不同项目间的依赖冲突，并确保环境的纯净性。 1.  **安装特定版本依赖**：在新创建的Python环境中，按照项目推荐的依赖版本进行安装。这一步确保了项目能够跟原作者一样的运行环境下运行，保证你运行代码时不会出错。 
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
conda create -n env_rec python=3.10

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

<img src="https://img-blog.csdnimg.cn/direct/1d901984468e4edab9d432c777fe3539.png#pic_center" alt="在这里插入图片描述" width="700">

## 4. 安装特定依赖库

为了确保能够顺利地运行和调试新接触的Python项目，特别是对于初学者来说，重要的一步是正确安装项目所需的依赖。这通常通过项目根目录中的`requirements.txt`文件来指定。

（1）找到你下载好的项目文件的位置，你可能下到的是一个压缩包，那么解压出来，点进“requirements.txt”这个文件所在的文件夹，因为我们下面要用到这个路径，所以在这里复制一下，我们下面命令行中要用到：

<img src="https://img-blog.csdnimg.cn/direct/2803c9edbfba4e1ca70aa0ee3f184594.png#pic_center" alt="在这里插入图片描述" width="700"> （2）还是上面那个命令行窗口，你应该有注意到你每次输入命令前的都有个路径，我这里是“C:\Users\lab321-1”，这个表示你当前进行的操作是在这个目录下进行的，比如要读取一个文件你不指定位置就默认从这个地方读取。那如果我们要用到上面文件夹中的“requirements.txt”呢，它显然不在这个目录吧，所以我们需要切换目录！

<img src="https://img-blog.csdnimg.cn/direct/15852092b97143a090c8055263749d80.png#pic_center" alt="在这里插入图片描述" width="400">

怎么切换目录呢，输入“cd F:\python\EmotionDetection\EmotionDetection”（看清楚了，这里的“F:\python\EmotionDetection\EmotionDetection”这是我的路径，你的应该是你复制的自己项目的文件夹路径！），所以**你输入时应该是先打cd，空格，然后Ctrl + V，粘贴你上面复制的路径**。这就是为啥上面要让你复制路径。

```
cd 你的路径

```

<img src="https://img-blog.csdnimg.cn/direct/421aa2c5e42e45239bff153c080d2984.png#pic_center" alt="在这里插入图片描述" width="600">

如上图，输入那个cd命令后回车，你会发现没啥变化，有的电脑这么输入左边那个路径提示会直接变成切换后的，有的就像我这里一样没反应。这就**需要再输入盘符，这里我的是F盘，所以输入**“**F:**”，如下图就切换到我们需要的路径了：

<img src="https://img-blog.csdnimg.cn/direct/378c7faf420b4ea98a138cc092f80488.png#pic_center" alt="在这里插入图片描述" width="600">

（3）**安装依赖**：在我们切换到项目目录下之后，我们就可以使用命令行读取`requirements.txt`文件，运行以下命令以根据`requirements.txt`文件安装所有依赖。这里使用了清华大学的PyPI镜像源来加速下载，这在中国大陆地区特别有用。

```
pip install -r requirements.txt --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple

```

此命令会读取`requirements.txt`文件中列出的所有包及其版本，然后从指定的镜像源下载并安装它们。`--no-cache-dir`选项的作用是禁用缓存，确保总是下载最新的包。

**操作步骤**：复制上面的代码“pip install -r requirements.txt --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple”到命令行中，然后回车，这样就会帮我们安装所有的依赖库了，如下图所示

<img src="https://img-blog.csdnimg.cn/direct/5a4bf202930a4bdb89e70951dcdf8e2f.png#pic_center" alt="在这里插入图片描述" width="600"> 这个过程会耗费一段时间，需要等到所有依赖库都装完，如下图所示，这样我们需要安装的环境依赖就完成了：

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

随着我们完成了通过上面在线方式安装依赖的步骤，现在应该已经成功配置了自己的Python开发环境，并且准备好开始探索和开发Python项目了。这种方式确保了项目依赖的准确性，使得项目能够在一个干净、一致的环境中运行。

不过在某些情况下，直接从互联网下载依赖可能并不可行。这可能是由于网络限制、速度慢或者安全政策等原因。为了解决这些情况，我将在下一篇博客中介绍如何使用我提供的离线依赖包进行安装。这也是一个非常有用的技巧，特别是在没有稳定网络连接的环境中工作的时候。感谢看到这里，希望这篇文章能够帮助顺利开始你的Python编程之旅吧，比心。
