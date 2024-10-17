
--- 
title:  在Jupyter Lab平台搭建Ruby编程环境 
tags: []
categories: [] 

---
## 在Jupyter Lab平台搭建Ruby编程环境

### Build A Ruby Programming Environment on Jupyter Lab

今天是一个特别的日子。因此，我要写一篇特别有用的文章，奉献给各位。

>  
 Ruby编程语言，以其易用性和雅致的风格，为大家周知；同时，Jupyter平台对于多语言（例如Python、Rust、JavaScript、Ruby等）支持的交互式编程，也展现出强大的功能和巨大的魅力。 
 如何将二者有机地结合到一起，即使用Jupyter Lab平台来进行Ruby编程是本文探讨的话题。 但是，这个看似简单的问题，实施起来却有点复杂。 


将 Jupiter Lab/Notebook 与 Python 结合使用非常简单，用iPython内核加载到Jupyter即可使用；但 Ruby 并不常见，而且搜遍全网，可用文档也很少。

参照相关专业文档，可能需要一些依赖项(dependencies)和 iruby。 然后尝试将 iruby 注册为新内核并运行Jupyter Lab或Notebook。

究竟能否成功呢？ 眼见为实！让我们一起来做实验。

#### 1. 安装Ruby for Windows

打开Chrome浏览器，访问Ruby官网链接： ，

<img src="https://img-blog.csdnimg.cn/78d43e99c1294894986dcef207c69f88.png" alt="在这里插入图片描述"> 在主页中间，点击**Download Ruby**按钮，重定向到下载页面。

<img src="https://img-blog.csdnimg.cn/ea9457c23f9e49d1b385de6ed539ee79.png" alt="在这里插入图片描述"> 点击文中Installation链接，转到安装页面。这里有可供选择的安装方法。 

<img src="https://img-blog.csdnimg.cn/b7bb0d94ce7a499cb7a86f2d30b74fa9.png" alt="在这里插入图片描述"> 在页面下方，看到可以使用不同操作系统的特定的**包管理器(package manager)**或第三方工具，因此有多个选项来通过命令安装及管理Ruby：

**1） 在RHEL、CentOS或Fedora的Linux发行版系统** 可用以下命令来安装Ruby：

```
$ sudo yum install ruby

```

**2） 在Debian或者Ubuntu的Linux发行版系统** 可用以下命令安装Ruby：

```
$ sudo apt-get install ruby-full

```

**3） 在macOS系统** 可用Hombrew包管理器来安装Ruby：

```
$ brew install ruby

```

**4） 在Windows系统** 可用Windows包管理器CLI来安装Ruby:

```
&gt; winget install RubyInstallerTeam.Ruby.{<!-- -->MAJOR}.{<!-- -->MINOR}
&gt; winget install RubyInstallerTeam.Ruby.3.2
&gt; winget search RubyInstallerTeam.Ruby
&gt; winget install RubyInstallerTeam.RubyWithDevKit.3.2

```

用Windows系统的Chocolatey包管理器安装

```
&gt; choco install ruby

```

此类安装过后，可以用以下命令验证Ruby所安装版本。

```
ruby -v 

```

或者

```
ruby --version

```

除了命令行安装外， 如果想用**RubyInstaller**的安装向导快捷安装，则须跳转到RubyInstaller官网：**https://rubyinstaller.org/**

>  
 *注：如果第一次或者重新安装Ruby，也可以参照以下文档链接： 




#### 2. 获取和安装Ruby

##### 1) 下载Ruby

在浏览器中，访问RubyInstaller官网镜像下载地址：**https://rubyinstaller.org/downloads/**

<img src="https://img-blog.csdnimg.cn/5464ce4544004df396092ec7bdb20f48.png" alt="在这里插入图片描述"> 选择**WITHOUT DEVKIT**（即不含开发工具的软件包），在下方点击**Ruby 3.2.2-1(x64)**进行64位安装程序下载。

软件包下载完毕，可在Windows的下载文件夹中找到该可执行文件，双击文件开始安装。

<img src="https://img-blog.csdnimg.cn/eb3bc944ce084992b7a193a00d7d8033.png" alt="在这里插入图片描述"> 选择**I accept the License**, 点击Next进行下一步。 <img src="https://img-blog.csdnimg.cn/d2d9aa2385184935ad1e5a3c2e03cf7b.png" alt="在这里插入图片描述"> 对话框显示默认复选了**Ruby RI and HTML documentation**点击Next进行下一步。

<img src="https://img-blog.csdnimg.cn/04738698e57048e28d3054a248e85fa4.png" alt="在这里插入图片描述"> 进入安装进程。如果先前安装过Ruby，那么安装向导会先进行卸载，再安装完整的Ruby。 <img src="https://img-blog.csdnimg.cn/260935fa5c39454da4ad468fc418193c.png" alt="在这里插入图片描述"> 随着文件拷贝，很快完成了安装。 <img src="https://img-blog.csdnimg.cn/4dfe66a0761c49b7bec9b50fcce152ca.png" alt="在这里插入图片描述"> 点击**Finish**结束安装。根据默认复选项，将运行**ridk install**，用来安装MSYS2和开发工具链。 <img src="https://img-blog.csdnimg.cn/205eb867d9eb4464b0a98557f050be95.png" alt="在这里插入图片描述"> 自动打开命令行窗口，有三个选项。

**选择：** 1进行基本安装(Base installation), 2系统更新(System update)

随之而来的，是安装包括**clang, mingw, gem, wget**等很多工具……数不胜数。安装完毕后，第3项不必选择，因为前两项已经满足安装。如果非得选择，那么会提示很多项目已安装，随机也会退出安装，回到命令行。

既然不再安装，按照屏幕提示，按**ENTER**退出该命令行窗口。

#### 3. 安装Python3最新版本

Jupyter Notebook/Lab提供了Python内核(Kernel)进行编程的交互式编程模式，对于数据科学等非常友好，可逐行进行编写和编辑，也能实时保存代码，非常适用。

但是，基于Pythong的Jupyter Notebook如果加载Ruby，需要加载Ruby的内核(Kernel)，因此系统须安装Python.

访问Python官网(www.python.org)，下载和安装Python 3.12.0最新版；适当配置安装目录，以便存放程序文件；安装过程中，选择**添加PATH环境变量**，这样，安装完毕，就可以直接使用Python3了。 选择**Customize installation**(定制安装)，将安装目录修改为D:\python312 <img src="https://img-blog.csdnimg.cn/354b90efb42e42a3b60cd0c1be62a870.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b28344663c3d42e0a78e5537ecc63113.png" alt="在这里插入图片描述"> 从上图可以看到，安装向导默认选择了Documentation(文档)、pip（包管理工具）、tkinter and(GUI工具)、Python test suite(Python测试套件)及py文件关联，且for all users（满足系统所有用户），点击Next进入下一步。

修改安装文件夹到D:\Python312, 其它默认选项不变，注意到有个默认选项**Add Python to environment variables**(添加Python到环境变量)，即向导自动添加安装目录到PATH环境变量。

<img src="https://img-blog.csdnimg.cn/a4ed64c132f2410ebb9fc7558742c11d.png" alt="在这里插入图片描述"> 点击Install开始安装。

当显示Setup was successful, 证明Python安装完毕，在命令行可以验证Python当前版本为3.12.0. <img src="https://img-blog.csdnimg.cn/aa5ff47f88104e9c8114688cdc33151a.png" alt="在这里插入图片描述"> *注：具体安装Python 3.12.0的详细步骤，参见安装2023最新版Python 3.12.0安装使用指南，

#### 4. 安装iPython和Jupyter平台

###### 1) 确保Python最新版安装完毕后，通过上述步骤，检查Python版本，证明安装Python为最新版本后，进行下一步；

###### 2) 安装ipython。在Power Shell命令行输入命令，安装ipython:

<img src="https://img-blog.csdnimg.cn/185881ecc6874d9d89513c42f24d39dd.png" alt="在这里插入图片描述"> 如上图，Ipython安装完毕。

###### 3) 安装Jupyter

输入以下命令，

```
pip install jupyter

```

完成安装Jupyter，如下图：

<img src="https://img-blog.csdnimg.cn/3d76135c3d744767992270641f036205.png" alt="在这里插入图片描述"> 安装完毕后，可输入以下命令，

```
jupyter –version

```

看到所有Jupyter核心包显示如下图，也验证了Jupyter Lab最新版本为3.6.5, 而Jupyter Notebook最新版本号为6.5.4。（如下图）

<img src="https://img-blog.csdnimg.cn/27e5d3e2e1454d789004260ca3323385.png" alt="在这里插入图片描述">

#### 5. 安装Ruby在Jupyter Notebook的内核IRuby

安装IRuby有以下先决条件： 1） 安装Jupyter. 前述步骤已经介绍，也即Jupyter Notebook(或Jupyter Lab)须安装完成； 2） 安装ffi-rzmq (用gem包管理器安装)：

```
gem install cztop rbczmq ffi-rzmq iruby  

```

<img src="https://img-blog.csdnimg.cn/157755625f7d4955aad31ff40dc1b386.png" alt="在这里插入图片描述"> 安装过程中，提示RubyGems有新的版本可用：

<img src="https://img-blog.csdnimg.cn/fb26467325034b2b985ef21b988321aa.png" alt="在这里插入图片描述">

#### 6. 更新gem须运行以下命令：

```
gem update --system

```

或指明具体版本：

```
gem update --sytem 3.4.21

```

<img src="https://img-blog.csdnimg.cn/c893ab4e13294eb0bf73bd89521a2203.png" alt="在这里插入图片描述"> 上图所示，RubyGems更新完毕。

#### 7. 注册IRuby到Jupyter的内核(Kernel)

执行以下命令进行注册：

```
iruby register --force  

```

<img src="https://img-blog.csdnimg.cn/cc682211611548e980944d1aaae1950d.png" alt="在这里插入图片描述"> 关闭窗口。重新以Administrator身份，打开cmd命令行窗口，执行以下命令：

```
gem install iruby

```

运行成功，安装iruby完成！ <img src="https://img-blog.csdnimg.cn/2f4814cfc17a4c29946e28721eeea12a.png" alt="在这里插入图片描述">

```
iruby register --force 

```

注册iruby成功！

为确保Jupyter Lab组件安装完整无误，须运行以下命令：

```
Jupyter lab build

```

<img src="https://img-blog.csdnimg.cn/8443d9818f824e77a5179a6e415e720e.png" alt="在这里插入图片描述"> 用以下命令启动Jupyter Lab

```
Jupyter lab

```

<img src="https://img-blog.csdnimg.cn/f6314eddcb694550a65994cf6e919865.png" alt="在这里插入图片描述"> 此时，打开Jupyter Labd的File菜单 --&gt; New – Notebook.

<img src="https://img-blog.csdnimg.cn/7d84d2815ddc489693d1e7861e8fb3f4.png" alt="在这里插入图片描述"> 选择内核如 ‘Ruby 3.2.2’, 然后单击"Select". 然后输入基本Ruby编程代码如下：

<img src="https://img-blog.csdnimg.cn/8f5fd7bfb952474a8925ded91641cb24.png" alt="在这里插入图片描述"> 看到图中，它们运行正常。

>  
 恭喜！祝贺你有效遏制了谋反大纲的代码。:~) 


这下，我们可以开始在Jupyter Lab平台工作了。唯一不同的是，仍然需要贵国和我们建立互信的网络连接，以期寻常人家出行便利。

喜欢就点赞哈！欢迎关注，畅聊！😃

#### 
