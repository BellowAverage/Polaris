
--- 
title:  Windows + Ubuntu系统(Windows下安装Ubuntu系统已更) 
tags: []
categories: [] 

---
### 



 　　　　下载地址：

 　　　　(Ubuntu中国下载地址：)

 　　　　云盘下载地址：百度云盘：链接:  提取码: id6f

 　　➢启动U盘制作软件：

 　　　　下载地址：链接:  提取码: 3ywa

 　　　　（Ubuntu官网提供的页面：）

　　➢EasyBCD: 链接:   密码: z3r7

 　　**[注：下面的(二)、(三)两步请参照]**

#### （二）、分区---分出来一个磁盘，用于安装Ubuntu

#### （三）、制作启动U盘：



### 二、安装Ubuntu

(原本的图是我在电脑上边装边用手机拍的，效果不是很好，现在用的是虚拟机安装过程中截的图。)

**(1) ------ ****从****U****盘启动****: **将U盘插在电脑上，选择启动方式为U盘启动。(如果你的电脑有两个USB...选项可供选择，可能一个带有“USB..UEFI”,另一个没有“UEFI”，请选择没有“UEFI”的，选带有“UEFI”的可能会出现问题，我有一个同学就是的，或者可以都试一下)（关于如何从U盘启动，快速U盘启动什么的，还请根据自己的电脑型号自行百度），下面是我的选择U盘启动的截图：



<img alt="" src="https://img-blog.csdnimg.cn/img_convert/6cffff935f6112564a47231ac5f706b1.jpeg">

    



**(2) ------ ****欢迎界面****: **选择了U盘启动后，等待一小会儿，会出现如下“欢迎”界面（通过左侧的语言栏选择中文），选择中文后，点击“安装Ubuntu”;

 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/a01e26292da6e0ba287edecf8fe99892.png">



**(3) ------ ****准备安装****: **接下来会进入“准备安装Ubuntu”界面：这里勾选“为图形或无线硬件….”,然后点击“继续”。（这里会检测是否已经连网，没网的话，那个 "安装Ubuntu时下载更新" 的是不能选的，我的因为截图用的虚拟机，连网了所以可选，你安装的时候应该会是不可选的，点完继续后还需要等待一小会儿）:

 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/f0919869966e7821ceb40037b723d1c4.png">

 **(4) ------ ****选择安装类型****: **上步之后进入“安装类型”界面，选择**“****其他选项****”**，之后继续，如图：(这里我的是虚拟机，实际安装那些可选项可能会有差异，但是请选择**“****其他选项****”**,其他的我没试过，不保证能成功，个人觉得选择"其他选择"也是最佳选项)

 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/5006fb83a60a1b73de54b025a09fc1fd.png">

**(5) ------ ****安装位置的选择及磁盘分区****: **之后就进入了一个很重要的环节---选择安装位置，分配分区。【说明---最开始我只分了是三个分区：“/”、“/home”、“swap”, 其实还需要一个挺重要的分区，就是"/boot"分区，在此感谢@的建议。如果你的电脑只准备安装Ubuntu，个人感觉“/boot”不要也行，但是要是双系统的话，强烈建议分出一个"/boot"，这会在以后提供很大的便利。】

#### 关于分区，想在这里说一下：

分区的大小主要取决于个人的选择，以下内容可能会有一定帮助：
- **/boot** - 200 MB ； 实际需求大约 100 ~ 200MB，如果有多个内核/启动镜像同时存在，建议分配 200 或者 300 MB。(个人建议:200MB ~ 300MB)- **/** - 15-20 GB ； 15-20 GB 对于大多数用户来说是一个比较合适的取值。(个人建议：15G短时间用不完，长期使用的话，建议20GB~25GB)- **/home** - [不定] ； 通常用于存放用户数据，下载的文件和媒体文件。在桌面系统中，/home 通常是最大的文件系统。(个人建议: 多多益善)- **swap** - [不定] ；在拥有不足 512 MB 内存的机器上，通常为 swap 分区分配2倍内存大小的空间。如果有更大的内存（大于 1024 MB），可以分配较少的空间甚至不需要swap 分区。(个人建议：感觉现在电脑的配置可以不要swap，但是也会用的着的，所以还是建议多少分点)
**注意**: 使用虚拟机时建议使用 Swap。**如果你的磁盘空间实在是足够大的话，对上面的各个分区也可以酌情、适当地增大空间****(****这个自己体会吧****)****。当然如果磁盘空间不是很大的话，，也可以适当减小空间，但是尽量不要小于最小值（/boot 200MB）**

以上只是个人的建议，从我现在的磁盘使用情况来给你们说明一下。(在此又想多絮叨几句，本博客第一次写于16年4月份吧因为换了固态硬盘，Ubuntu又重装了，大概是16年10月份，当时对各个分区并不是很了解，分的不是很合理)。当时我为Ubuntu系统总共分了大概120GB的空间， **这是我的不怎么合理的分区，不要照着下面分区**，其中：

 　　**/boot** ---- 2GB------&gt; 结果只用了100多MB，白白浪费了 1.8GB

 　　**/** ------ 50GB-------&gt; 结果到现在也就才用了，14GB不到，有36GB的空间在那里“呵呵”

 　　**/home** ---- 60GB ------&gt; 不是我省着用，都不敢怎么存东西，早就用完了，文件都清过几次了，现在主要是一些来编程、学习的东西( 搞 Android 开发 那些东西 就将近20个GB啊...)，其他东西都不敢乱存了。

 　　**swap** ------8GB ------&gt; 平时也是在那闲着，不过不一定某一天心血来潮在Ubuntu上装个Mac 或 Win 虚拟机，那就用得着了，所以这也是我上面建议多少分点儿的原因。(现在主要用的是Ubuntu，但是为了交作业有时还得切换到Windows去写word文档，虽然Ubuntu也有office软件，不过和微软的office在一些格式上会存在不兼容，出现排版错误，作业还是得用微软office写，所以在Ubuntu里装一个Win系统的虚拟机装上office，就不用来回切换系统了。)

**好了，啰嗦了一大堆，下面看分区吧：**

 又要啰嗦了，我的虚拟机中只有一块完全空白的磁盘，大概120GB吧（在安装的过程中你会发现，磁盘显示的大小可能不止120GB，会有点出入，这个不要太纠结，想要了解的自己去查下资料吧）。

　　**/boot** 分区:  ------ 300MB

                这里又要多说几句，虽然啰嗦，不过请先看完这些...下面的图中/boot分区类型选择的是"逻辑分区",由于要把Ubuntu引导安装到/boot中，所以到后面"安装启动引导器的设备"要选择"/boot"分区，不过我在多次安装的过程中，遇到了以下的一些情况：
|安装设备|/boot分区类型|引导器|结果
|电脑(组成双系统)|逻辑分区　　|/boot|成功
|虚拟机|逻辑分区|/boot|可以正常安装，但是不能启动
|虚拟机|主分区|/boot|成功

 网上有这样的说法，双系统--原本电脑已经有了一个是主分区类型的引导器，这里的/boot选择"逻辑分区"就行了；完全空白的一整块磁盘-- /boot 要选择"主分区"。我也没有都试过，不过应该是对的。所以，**总结一句话，装双系统，****/boot ****选择****"****逻辑分区****"****就行了**，我自己的电脑也是这样的

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/957e9269821f2203975abd59566af230.png">

　　**/** 分区　------ 30GB

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/bb640a83f275099741ec5b90e35d898c.png">

　　**/home **分区　------ 90GB　（安装后感觉 /home 有点大了，觉得可以再分给上面的 / 5GB，即 /home 85GB，/ 35GB）

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/c91f639bff395d822c0de5195627183a.png">

　　**swap(****交换空间****)** :　------ 5GB多吧（上面剩下的都给它了）

 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/744b6c877ceca770a027ade6925c60ba.png">

 　　**"****安装启动引导器的设备****"****选择****/boot****对应的分区**

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/05f0dbee1f7f5c465486516eafc7fb61.png">

 选择之后，检查无误，点击"现在安装"...

**(6) ------ ****检查分区****:**

 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/7b789943f716623d2d893b9e00c820e9.png">

 检查无误后，选择继续...

**(7) ------ ****选择地域**(默认上海，直接"继续"就行，安装完之后可以设置精确的位置):

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/9fca64c76e7a1bd9ff28ff4258b9caf4.png">

**(8) ------ ****选择键盘**(汉语,或根据个人喜好^_^):

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/c42ca876b93ffa01639b26625a69b1b3.png">

 **(9) ------ ****设置用户**:

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/8a38d83c821edb9f54e1e45c25f18831.png">

 设置完之后，选择"继续"...

**(10) ------ ****正在安装，请等待**:

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/ebc43d9cb13dddf0d08cd8df949a58d1.png">

**(11) ------ ****安装成功，请重启**:

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/93a8e0cff271b601faffa859ce50280a.png">

 如果你是按照此过程安装的，上步重启之后会发现，没有Ubuntu的选择项，依旧直接进入Windows，别急，往下看。

**(12) ------ ****设置启动项**:

　　进入Windows 后，安装 EasyBCD ，之后运行(直接上图了)

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/d44473c29fb9663bfc815b5300ba8d9f.png">



<img alt="" src="https://img-blog.csdnimg.cn/img_convert/38c211259f27f3c967050dbca1c380b7.png">

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/e0dd741c854b91b902dde1074c7bdb63.png">

 上面的所有都做完之后，重启，你会发现多了一个启动项，选择刚才添加的那个(自己想的名字)，然后会进入以下界面:(**请选择第一项**)

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/83e1642d91b18aa425384f3d4909881e.jpeg">

 输入用户密码:

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/67e2521d37ffcc08e200385696cb0df8.png">

接下来就开始折腾吧！

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/c94e02a77875e41b4634cc117f01bc57.png">



<img alt="" src="https://img-blog.csdnimg.cn/img_convert/f4aa2646aab23d11a67e8d66c93ee879.png">

 
