
--- 
title:  CUDA与cuDNN详细安装教程（最新） 
tags: []
categories: [] 

---
#### 写在前面：

#### 在深度学习中，我们常常要对图像数据进行处理和计算，而处理器CPU因为需要处理的事情多，并不能满足我们对图像处理和计算速度的要求，显卡GPU就是来帮助CPU来解决这个问题的，GPU特别擅长处理图像数据，而CUDA（Compute Unified Device Architecture），是显卡厂商NVIDIA推出的运算平台。CUDA™是一种由NVIDIA推出的通用并行计算架构，该架构使GPU能够解决复杂的计算问题。它包含了CUDA指令集架构（ISA）以及GPU内部的并行计算引擎，安装cuda之后，可以加快GPU的运算和处理速度。



#### 什么是显卡？

显卡（Video card，Graphics card）全称显示接口卡，又称显示适配器，是计算机最基本配置、最重要的配件之一。显卡作为电脑主机里的一个重要组成部分，是电脑进行数模信号转换的设备，承担输出显示图形的任务。显卡接在电脑主板上，它将电脑的数字信号转换成模拟信号让显示器显示出来，同时显卡还是有图像处理能力，可协助CPU工作，提高整体的运行速度。对于从事专业图形设计的人来说显卡非常重要。民用和军用显卡图形芯片供应商主要包括AMD(超微半导体)和Nvidia(英伟达)2家。现在的top500计算机，都包含显卡计算核心。在科学计算中，显卡被称为显示加速卡。

#### 什么是显存？

也被叫做帧缓存，它的作用是用来存储显卡芯片处理过或者即将提取的渲染数据。如同计算机的内存一样，显存是用来存储要处理的图形信息的部件。

#### 显卡、显卡驱动、CUDA之间的关系
-  显卡：（GPU），主流是NVIDIA的GPU，因为深度学习本身需要大量计算。GPU的并行计算能力，在过去几年里恰当地满足了深度学习的需求。AMD的GPU基本没有什么支持，可以不用考虑。 -  驱动：没有显卡驱动，就不能识别GPU硬件，不能调用其计算资源。但是呢，NVIDIA在Linux上的驱动安装特别麻烦，尤其对于新手简直就是噩梦。得屏蔽第三方显卡驱动。下面会给出教程。 -  CUDA：是显卡厂商NVIDIA推出的只能用于自家GPU的并行计算框架。只有安装这个框架才能够进行复杂的并行计算。主流的深度学习框架也都是基于CUDA进行GPU并行加速的，几乎无一例外。还有一个叫做cudnn，是针对深度卷积神经网络的加速库。 
**显卡驱动与cuda的关系**：NVIDIA的显卡驱动器与CUDA并不是一一对应的，CUDA本质上只是一个工具包而已，所以我可以在同一个设备上安装很多个不同版本的CUDA工具包，比如可以同时安装 CUDA 9.0、CUDA 9.2、CUDA 10.0三个版本。一般情况下，我只需要安装最新版本的显卡驱动，然后根据自己的选择选择不同CUDA工具包就可以了，但是由于使用离线的CUDA总是会捆绑CUDA和驱动程序，所以在使用多个CUDA的时候就不要选择离线安装的CUDA了，否则每次都会安装不同的显卡驱动，这不太好，我们直接安装一个最新版的显卡驱动，然后在线安装不同版本的CUDA即可。

**为什么GPU特别擅长处理图像数据呢？**

这是因为图像上的每一个像素点都有被处理的需要，而且每个像素点处理的过程和方式都十分相似，GPU就是用很多简单的计算单元去完成大量的计算任务，类似于纯粹的人海战术。GPU不仅可以在图像处理领域大显身手，它还被用来科学计算、密码破解、数值分析，海量数据处理（排序，Map-Reduce等），金融分析等需要大规模并行计算的领域。

**查看自己电脑是否可以使用GPU加速？**

想要使用GPU加速，则需要安装cuda,所以首先需要自己的电脑显卡是否支持cuda的安装，也就是查看自己的电脑里面有没有NVIDA的独立显卡，这里再说明一下，AMD的显卡不支持安装cuda来进行加速，具体查看步骤如下：

**第一步：**开始菜单输入框输入设备管理器，打开设备管理器，找到显示适配器后点击，查看电脑显卡型号

<img alt="" height="1144" src="https://img-blog.csdnimg.cn/direct/358965b3c23f4dee9647a3b472fe29de.png" width="1200">

**第二步：**在NVIDA官网列表中，地址：https://developer.nvidia.com/cuda-gpus，查看自己的显卡型号是否在NVIDA列表中，若存在则可以下载cuda实现GPU加速，这里可以看到我的显卡计算力为7.5，当然如果你的显卡运算能力在3.0以下，那没有适合你的cuda版本。

<img alt="" height="1055" src="https://img-blog.csdnimg.cn/direct/ced8c5db8dcc4ed199f0b4efbce36a4d.png" width="1066">

**查看自己电脑是否有nvidia显卡驱动****？**

点击设备管理器，鼠标右键点击显卡的名称，选择属性，然后点击“”，能看到驱动的详情说明驱动装好了。

<img alt="" height="1110" src="https://img-blog.csdnimg.cn/direct/87e1a745e4634e0fbac8e80326935bc0.png" width="950">

我这里电脑有显卡驱动，但没有显卡控制面板，可能是缺少相关组件，这里我直接安装适合本电脑显卡的NIVIDIA版本，**没有卸载原有驱动**，因为旧版本的NVIDIA驱动会被覆盖掉。

地址：https://www.geforce.cn/drivers，有两种安装方式，自动和手动，选择适合自己电脑的显卡驱动下载，安装很简单，直接下一步就可以，默认系统安装路径。

<img alt="" height="855" src="https://img-blog.csdnimg.cn/direct/eb88edd97de94b79a9c328ba331ce356.png" width="1200">

这里我选择自动更新驱动程序--&gt;立即下载；

下载以后自动覆盖了C:\Program Files\NVIDIA Corporation中的文件；文件中的修改日期变成当前时间。

下载完成后，打开Geforce Experience，点击检查更新文件，如图已拥有最新驱动程序即可。若检测到有可以安装的最新版本，进行下载安装即可。我安装时勾选了清洁安装，会自动卸载旧版本。

<img alt="" height="256" src="https://img-blog.csdnimg.cn/direct/ede92bcf7b9b434298f10db7a3951408.png" width="1200">

更新驱动完毕，桌面右键就出现NVIDIA控制面板了。

打开NVIDA控制面板，查看GPU显卡所支持的CUDA版本，具体开始菜单 -》NVIDIA控制面板-》帮助-》系统信息-》组件-》nvidia.dll后面的cuda参数，可以看到，我的显卡支持版本为12.4，所以我下载安装&lt;=12.4版本的cuda即可。

<img alt="" height="1050" src="https://img-blog.csdnimg.cn/direct/5891e0522a22419185340f9028350a2f.png" width="1135">

nvidia-smi显示的**CUDA Version是当前驱动的最高支持版本**，因为CUDA是向下兼容的，所以最高支持版本以下的CUDA版本都是支持的，如图，nvidia-smi显示最高版本支持为12.4，那12.4以及12.4一下的版本都是支持的。

<img alt="" height="803" src="https://img-blog.csdnimg.cn/direct/5765fa330dbf4ead871be0ba62a12d72.png" width="1200">

#### 安装CUDA必须安装VS吗？

CUDA是一种由NVIDIA开发的并行计算平台和编程模型，它可以通过GPU加速应用程序的执行速度。在安装CUDA的时候，很多人会疑惑是否需要安装VS（Visual Studio）。

事实上，安装CUDA并不一定需要安装VS。CUDA可以在支持的操作系统上独立安装，并且可以使用命令行编译和运行CUDA程序，而不依赖于VS。这对于一些用户来说是非常方便的，特别是对于那些只想使用CUDA库并不需要进行C/C++开发的用户。

然而，如果你打算在Windows系统中使用CUDA进行C/C++开发，那么安装VS是非常推荐的。VS提供了强大的集成开发环境（IDE），它可以简化代码编写、调试和构建过程。此外，VS还提供了与CUDA相集成的插件和工具，如CUDA模板和CUDA调试器，使得开发和调试CUDA程序更加简单高效。

此外，安装VS还可以为CUDA提供支持库和头文件，这些对于开发CUDA应用程序非常重要。VS提供了与CUDA版本相匹配的开发工具集（包括C/C++编译器和构建工具），确保了编译的兼容性和正确性。

这里我为了稳妥起见，还是选择安装了vs2017，安装教程如下文。

#### 查看pytorch与cuda的对应版本



由于我使用的deepke框架 ，支持的torch版本为torch&gt;=1.5,&lt;=1.11，我这里选择安装1.11版本的torch，点击上述网址，滑到v1.11.0部分，可以看到支持cuda11.3和10.2版本。

<img alt="" height="709" src="https://img-blog.csdnimg.cn/direct/02df208fb6e94f2fbd3e6c8ad3669095.png" width="1200">

我选择安装11.3版本，命令如下：

```
# CUDA 11.3
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113

```

#### 查看vs与cuda对应版本



<img alt="" height="291" src="https://img-blog.csdnimg.cn/direct/b18054d2be2b41f89750dc81fc7d0d67.png" width="1200">

如图，win10版本支持cuda11.3，如果系统是win11也可以支持。

<img alt="" height="273" src="https://img-blog.csdnimg.cn/direct/34db11638f374eae9d8c02eef18d0a50.png" width="902">

如图，vs2017可以支持cuda11.3

<img alt="" height="278" src="https://img-blog.csdnimg.cn/direct/a5194ca9dc674a61b7ceaa6599d414be.png" width="1200">

**<strong>下载**安装 Visual Studio</strong>

安装Visual Studio，因为CUDA在安装时，需要VS的里面的工具包来编译。VS这里我安装的是社区免费版VS2017，无需秘钥key就可以使用，也可以使用其它版本，但是需要key，请见第一张图的Table2，在安装过程中，会自动检测本机是否已经安装了配套的VS版本其中之一，如果VS版本和Cuda版本不匹配的话，安装无法进行。

**第一步：**到微软Visual Studio官方网站进行VS2017安装包下载，这里需要注册一个微软账号，如果没有的话按步骤进行注册、登录即可，地址：https://my.visualstudio.com/Downloads?q=Visual%20Studio%202017

<img alt="" height="1023" src="https://img-blog.csdnimg.cn/direct/99c708ddd5d8423b9ef4eeafaadf57d3.png" width="1200">

进入后发现2017版本无法下载，在网上找了部分解决方法后，在该篇博客的2017链接下，下载成功。

博客地址：

**第二步：**下载完安装包后双击，安装选项：工作负载处，勾选“C++的桌面开发（其他的可不勾选，若需要的话，后面可再次安装）

<img alt="" height="1132" src="https://img-blog.csdnimg.cn/direct/15d667fbba544d3ebf4894424fee6724.png" width="1200">

**第三步：**选择软件安装位置选择软件要安装到的地方，建议安装到专门放软件的盘，不要安装到系统盘C，然后点击开始进行安装

<img alt="" height="1156" src="https://img-blog.csdnimg.cn/direct/ab1cd949859743a7b9e5faf77b1ded44.png" width="1200">

**第四步：**选完后，点击安装，正式安装，这个过程需要等待一会儿时间

<img alt="" height="739" src="https://img-blog.csdnimg.cn/direct/35365fe6946a4defa8e200bf2be0b7ce.png" width="1200">

安装成功后的界面

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/247cea10f2be4f31a9c1f1d18c3f9669.png" width="1200">

#### **<strong>下载与安装<strong><strong>CUDA**</strong></strong></strong>

**第一步：**到官网下载CUDA安装包，前面我们已经查看到了电脑GPU显卡所支持的CUDA版本为&lt;=12.4,下载地址：https://developer.nvidia.com/cuda-toolkit-archive

<img alt="" height="1152" src="https://img-blog.csdnimg.cn/direct/93c4ca62fa0d413eada78015abe82a21.png" width="1200">

**第二步：**下载完后，双击

extraction path可以不用修改，默认路径即可。cuda安装完成后，该路径下的文件就自动删除了。

<img alt="" height="372" src="https://img-blog.csdnimg.cn/direct/916829420fa247d38496ac372754ae17.png" width="824">

一切正常，检查系统兼容性。

<img alt="" height="894" src="https://img-blog.csdnimg.cn/direct/1f0d7379e2b045869c3199a5f6b1eb7e.png" width="1200">

**第三步：**同意并继续后，选择自定义安装

<img alt="" height="894" src="https://img-blog.csdnimg.cn/direct/c84aeb4d2c974bb18b89a9137425ea36.png" width="1200">

**第四步：**安装组件，全部勾选，点击下一步

<img alt="" height="894" src="https://img-blog.csdnimg.cn/direct/dc802da62c2748ba91909de71a536f73.png" width="1200">

**第五步：**选择安装位置，这里建议默认安装，也可手动安装，但是要记得自己安装的位置，因为后面需要配置系统环境变量

<img alt="" height="894" src="https://img-blog.csdnimg.cn/direct/2dde68126f0e4e43bae77443458b9063.png" width="1200">

**第六步：**开始准备安装，等待安装完成，这需要等待一段时间

<img alt="" height="894" src="https://img-blog.csdnimg.cn/direct/7359b45e895043e48c470b48e29f67c5.png" width="1200">

安装完成界面如下，点击下一步，就安装完成了

<img alt="" height="894" src="https://img-blog.csdnimg.cn/direct/77d610bf53994b199694c33758a97c71.png" width="1200">

**第七步：**安装完成后，就需要我们配置Cuda的环境变量了，我们在计算机上点右键，打开属性-&gt;高级系统设置-&gt;环境变量，可以看到系统中多了CUDA_PATH和CUDA_PATH_V11_3两个环境变量，安装好后，自动默认帮我们设置好了这2个环境变量：

<img alt="" height="83" src="https://img-blog.csdnimg.cn/direct/a10ade1fc97c4e8895405d4b5879b8ea.png" width="1053">

之后我们最好再手动添加以下5个环境变量，方便日后配置VS使用，在VS中使用CUDA加速。

```
CUDA_SDK_PATH = D:\CUDA\NVIDIA Corporation\CUDA Samples\v11.3
CUDA_LIB_PATH = %CUDA_PATH%\lib\x64
CUDA_BIN_PATH = %CUDA_PATH%\bin
CUDA_SDK_BIN_PATH = %CUDA_SDK_PATH%\bin\win64
CUDA_SDK_LIB_PATH = %CUDA_SDK_PATH%\common\lib\x64
```

提醒：%CUDA_PATH前面的%,作用其实就是加上CUDA_PATH的路径，也就是上图的D:\CUDA\NVIDIA GPU Computing ToolKit\CUDA\v11.3

配置成功之后的图：

<img alt="" height="420" src="https://img-blog.csdnimg.cn/direct/5019db84e8104d63ae16d1126600fcc0.png" width="1200">

**<strong>查看是CUDA是否安装成功**</strong>

配置完系统环境变量之后，我们就可以查看CUDA是否安装成功以及环境变量配置情况

查看安装版本：Win + R 打开cmd ，输入命令：nvcc --version

查看设置变量情况：输入命令：set cuda

<img alt="" height="593" src="https://img-blog.csdnimg.cn/direct/f6c600d72f304930877d942ae1c793a4.png" width="1200">

验证deviceQuery和bandwidthTest,在命令窗口运行测试文件，定位到 在cuda安装目录的 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\extras\demo_suite，分别输入deviceQuery，bandwidthTest并运行，两个地方的Result=PASS则说明通过，反之，Rsult=Fail 则需要重新安装。

<img alt="" height="989" src="https://img-blog.csdnimg.cn/direct/f90fe9152d324c9ebd6e9a72761e043a.png" width="1200">

如果以上都没问题，则说明CUDA安装成功，至于Cuda安装成功之后的使用，我们可以在Visual Studio中写C++代码使用，也可以在Anaconda和Pycharm中写Python代码使用，额外下载安装cudnn，CUDNN是一个常见的神经网络层加速库文件，能够很大程度把加载到显卡上的网络层数据进行优化计算，而CUDA就像一个很粗重的加速库，其主要依靠的是显卡。CUDNN需要在有CUDA的基础上进行，CUDNN可以在CUDA基础上加速2倍以上。

**Anaconda中使用**

在CUDA安装完之后，如果想要学习深度学习中的神经网络的话，则额外下载安装cuDNN，可帮助我们加快神经网络的运算，cuDNN是一个常见的神经网络层加速库文件，能够很大程度把加载到显卡上的网络层数据进行优化计算，而CUDA就像一个很粗重的加速库，其主要依靠的是显卡。cuDNN需要在有CUDA的基础上进行，可以在CUDA基础上加速2倍以上。

**下载安装之前，这里再简要介绍几个关键概念**

**NVIDIA的显卡驱动器与CUDA**

NVIDIA的显卡驱动程序和CUDA完全是两个不同的概念，CUDA是NVIDIA推出的用于自家GPU的并行计算框架，也就是说CUDA只能在NVIDIA的GPU上运行，而且只有当要解决的计算问题是可以大量并行计算的时候才能发挥CUDA的作用。

NVIDIA显卡驱动和CUDA工具包本身是不具有捆绑关系的，也不是一一对应的关系，CUDA本质上只是一个工具包而已，所以我可以在同一个设备上安装很多个不同版本的CUDA工具包，一般情况下，我只需要安装最新版本的显卡驱动，然后根据自己的选择选择不同CUDA工具包就可以了。

**CUDA和cuDNN关系**

CUDA看作是一个工作台，上面配有很多工具，如锤子、螺丝刀等。cuDNN是基于CUDA的深度学习GPU加速库，有了它才能在GPU上完成深度学习的计算。它就相当于工作的工具，比如它就是个扳手。但是CUDA这个工作台买来的时候，并没有送扳手。想要在CUDA上运行深度神经网络，就要安装cuDNN，就像你想要拧个螺帽就要把扳手买回来。这样才能使GPU进行深度神经网络的工作，工作速度相较CPU快很多。

**注意：**cuDNN是一个SDK，是一个专门用于神经网络的加速包，它跟我们的CUDA没有一一对应的关系，即每一个版本的CUDA可能有好几个版本的cuDNN与之对应，但一般有一个最新版本的cuDNN版本与CUDA对应更好。

**CuDNN支持的算法**
-  卷积操作、相关操作的前向和后向过程 -  pooling的前向后向过程 -  softmax的前向后向过程 -  激活函数的前向后向过程,如（Relu、Sigmoid、Tanh ）等 
**cuDNN的下载与安装**

**第一步：**官网下载cuDNN的安装包,地址：https://developer.nvidia.com/cudnn，这里需要你注册一个账号，按照要求注册完就可以下载安装包了，这里我的CUDA安装的是11.3版本的，我就安装与我CUDA对应的cuDNN了。

<img alt="" height="577" src="https://img-blog.csdnimg.cn/direct/b928d55aa853474f969eb0813da825ca.png" width="1200">

<img alt="" height="1145" src="https://img-blog.csdnimg.cn/direct/e53c2955744a41378afeedc7fe94803c.png" width="1200">

**第二步：**下载好安装包后，利用解压软件解压出来

<img alt="" height="561" src="https://img-blog.csdnimg.cn/direct/7429c11c55ca4e268719b103fbe72547.png" width="1110">

**第三****步****：**复制粘贴 bin、include、lib三个文件到CUDA的安装目录进行覆盖替换

<img alt="" height="698" src="https://img-blog.csdnimg.cn/direct/e7b791a3d7bc454a9fc6a2373e33dddb.png" width="1200">

cuDNN到此安装成功！

**下载安装Pytorch-GPU--conda安装**

**第一步：**首先我们来到Pytorch-GPU的官网，浏览pytorch对应版本下cuda支持版本的相应命令。如1.11版本的pytorch对应11.3版本的cuda下载命令如下：

<img alt="" height="965" src="https://img-blog.csdnimg.cn/direct/99c886bbd3514d03afe720a87a6b6d09.png" width="1200">

```
# CUDA 11.3
conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 cudatoolkit=11.3 -c pytorch
```

但是这里下载速度极慢，很容易出现CondaHTTPError，因为默认的镜像是官方的，由于官网的镜像在境外,访问太慢或者不能访问，为了能够加快访问的速度，我们更改Conda下载安装包的镜像源.

**第二步：**这里我们首先设置一下Conda下载安装包的镜像源，输入以下命令：

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --set show_channel_urls yes
```

<img alt="" height="547" src="https://img-blog.csdnimg.cn/direct/c2af6ba6b6404d71b1196f3c7fdefd10.png" width="1200">

**第三步：**添加完后，在用户目录下，如：C:\Users\19096 ，找到 .condarc 文件，使用记事本打开，删除里面的 defaults，这样能快点，或者在其前面加#号注释掉。

<img alt="" height="534" src="https://img-blog.csdnimg.cn/direct/748f8d7ecb1b429a91535be06ae5b61f.png" width="1200">

**注意：**

用conda安装包的标准语法格式为：conda install -c &lt;channel&gt;&lt;packagename&gt;，

而pytorch官网中conda给的命令行是上图那样的，有-c选项，就说明已经指定了官方下载源，所以自己配置的镜像源不管用， 所以应该把-c pytorch去掉，就可以从镜像源下载文件了。

<img alt="" height="472" src="https://img-blog.csdnimg.cn/direct/b6f3cdf8c1d4402483d7565154f78b88.png" width="1200">

输入y，即正式下载和安装.

**友情提示：**

如果你想再次换源安装，需要使用以下命令conda config --remove-key channels恢复默认源的命令，否则会报错，然后再次配置你想要的镜像源.

其余安装方式请参考该文章：

**最后我们检测Pytorch-GPU是否安装完成**

先使用命令pip list查看已安装的包列表，再输入命令python，然后 torch.cuda.is_available()，输出True,即安装成功

<img alt="" height="453" src="https://img-blog.csdnimg.cn/direct/f79052f9ee534aed8744f59f0a2270c0.png" width="613">

<img alt="" height="311" src="https://img-blog.csdnimg.cn/direct/62204dc09d2248b4ba10608700657e95.png" width="1200">


