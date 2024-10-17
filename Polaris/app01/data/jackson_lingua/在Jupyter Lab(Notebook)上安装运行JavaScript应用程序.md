
--- 
title:  在Jupyter Lab(Notebook)上安装运行JavaScript应用程序 
tags: []
categories: [] 

---
## 在Jupyter Lab(Notebook)上安装运行JavaScript应用程序

### Build and Run JavaScript Applications on Jupyter Lab or Jupyter Notebook

>  
 Jupyter Lab(或Jupyter Notebook)以它强大的功能和动态编程的风格而广受欢迎。 我们在平时写JS应用程序时，常常需要小模块的功能练习，或者函数及算法的动态交互，而不是一下子写一大段JavaScript代码。 因此，如果能在Jupyter Lab(或Notebook)平台上来做JavaScript编程，将事半功倍。 


本文将简要介绍在Jupyter Lab如何安装和实现JavaScript编程。

#### 1. 安装Jupyter

##### 1) 安装Jupyter Notebook分为以下几个主要步骤：

###### a) 安装最新版Python 3.12.0

这是搭建Jupyter Notebook的必要步骤；因为其它相关编程语言内核(kernel)，都需要这个框架作为支撑。

关于安装Python的详细步骤，本文不再详述。请参看笔者另一篇博客：

###### b) 验证Python安装

安装好Python 3后，进入Windows Command(命令行) 验证它的版本号

```
python –version

```

得到以下结果：

```
Python 3.12.0

```

证明Python安装成功！

###### c) 安装更新pip

pip是Python的包管理工具，用来安装各种扩展库(libraries). 为了确保它升级到的最新版本，需要执行pip的安装更新。

```
python -m pip install --upgrade pip

```

<img src="https://img-blog.csdnimg.cn/a56b8fdc233643db8469956c65b706b0.png" alt="在这里插入图片描述"> 显示当前版本已满足最新版**pip 23.3.1**。 于是，继续**下一步**。

##### 2) 安装及验证Jupyter Notebook

访问Python扩展包(Python Package)官网, 这里有数十万个适用于Python的扩展包。

<img src="https://img-blog.csdnimg.cn/eb309846f2844b118950d32c98a266ca.png" alt="在这里插入图片描述"> 搜索找到安装Jupyter(包含Notebook和其相关组件)安装命令：

```
pip3 install jupyter

```

<img src="https://img-blog.csdnimg.cn/f23ff8b810fc4e4d95a937617fb25ac2.png" alt="在这里插入图片描述"> Jupyter安装结束。 此时，如果运行基于Python内核的Jupyter Notebook, 可以执行以下命令：

```
jupyter notebook

```

**注：**如果之前安装过Jupyter Notebook, 则需要验证一下安装版本是否最新。

```
jupyter –version

```

可以看到本机Jupyter 相关组件及版本显示如下表，包含Jupyter Notebook及Jupyter Lab.

<img src="https://img-blog.csdnimg.cn/4dbfe08c97d7452fab79b877492e341a.png" alt="在这里插入图片描述">

#### 3. 安装Node.js和npm

为了在Jupyter Notebook平台使用JavaScript编程语言，需要安装IJavaScript组件。而这个组件行使功能的先决条件，是安装Node.js及npm包管理器。

##### 1） 在Windows 10/11系统安装Node.js

我们需要分以下两种情况安装Node.js：

###### a) Windows下载Node.js

打开Chrome浏览器,访问Node.js官网下载页，

<img src="https://img-blog.csdnimg.cn/f4a2059e92354fae890114a5c941492a.png" alt="在这里插入图片描述"> 选择**64-bit**的Windows Installer, 即64-bit的.msi文件，点击下载。

下载完毕，在Windows**下载**文件夹中，找到Node.js安装包文件 **node-v18.18.2-x64.msi**,双击该文件开始安装。

###### b) 安装Node.js

双击安装包后，启动安装向导，如下图所示； <img src="https://img-blog.csdnimg.cn/3afe49738f7c4a4494fcac1c1ee1dd70.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/65606c80682942ce97de48396f299d2e.png" alt="在这里插入图片描述"> 复选**I accept the terms in the License Agreement**(我接受许可证协议条款)，点击**Next**继续下一步。 <img src="https://img-blog.csdnimg.cn/78fe88cee6d3433890b15a9f1a126410.png" alt="在这里插入图片描述">

修改安装文件夹，位置为D:\nodejs <img src="https://img-blog.csdnimg.cn/915cb99e62d34f56a86d38eb2e2c0385.png" alt="在这里插入图片描述"> 按照默认选项，确认**Add to PATH**(增加到PATH环境变量)被选中，点击**Next**继续。

<img src="https://img-blog.csdnimg.cn/486828c3c38345bf9162c4a186328064.png" alt="在这里插入图片描述"> 复选**Automatically install the necessary tools**……， 安装**Chocolatey**.安装结束会弹出对话框。点击**Next**进行下一步。

点击**Install**开始安装复制文件，如下图。 <img src="https://img-blog.csdnimg.cn/9a07741a69e4429f9bfb6f3c42779ff1.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b67d3acea7034c12af266d587993b879.png" alt="在这里插入图片描述"> 很快，安装结束，点击**Finish**完成安装。接下来，会自动启动命令行安装，如下图。 <img src="https://img-blog.csdnimg.cn/84cca18d92b549e784852f1655cea2ac.png" alt="在这里插入图片描述"> 提示将安装Node.js原生模块，包括安装Python和Visual Studio Build Tools, 这些是编译Node.js远程模块的必要工具。（也可以选择关闭这个窗口即刻停止安装进程；之后可以从https://github.com/nodejs/node-gyp#on-windows链接手动完成安装）

按任意键继续安装。

<img src="https://img-blog.csdnimg.cn/a127ad5b222a40ff91234fdb3a491f0d.png" alt="在这里插入图片描述"> 此时，显示用此脚本下载第三方软件 – Chocolatey安装包。

按任意键继续。

这时，会弹出Windows Powershell窗口，继续完成安装。 <img src="https://img-blog.csdnimg.cn/fa7329e856a64128a89fa7007ed77da0.png" alt="在这里插入图片描述"> 安装完毕，提示按ENTER（回车键）退出；这时，Chocolatey也安装更新完毕。

#### 4. 在Windows安装ijavascript

我们已安装Node.js，具备了npm包管理器，首先验证一下它的版本：

```
npm –version

```

<img src="https://img-blog.csdnimg.cn/81de1401ab4c47718911186b497770fb.png" alt="在这里插入图片描述"> 看到npm版本为9.8.0. 接下来，就可以执行以下命令，安装ijavascript：

```
npm install ijavascript

```

<img src="https://img-blog.csdnimg.cn/2cd10968983542c9ad18133e785ac142.png" alt="在这里插入图片描述"> *注：如果提示npm版本过期，则需要升级到版本7或者更高。 <img src="https://img-blog.csdnimg.cn/1b2c21462063477a89100e98604d8f1d.png" alt="在这里插入图片描述"> 系统提示，有更新的版本9.8.0，于是，根据提示，运行以下命令安装最新版。

```
npm install -g npm@9.8.0

```

最后，单独运行以下命令，完成安装：

```
ijsinstall

```

#### 参考一： 在Linux系统安装

使用命令在Linux系统平台安装Node.js, 步骤相对简单，以ubuntu 18以上版本为例：

```
sudo apt-get install nodejs npm jupyter
npm config set prefix $HOME
npm install -g ijavascript
ijsinstall

```

#### 参考二：在macOS系统安装

在macOS系统，Homebrew和Pip可被用来安装iJavaScript所需的组件。执行以下系列命令：

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install pkg-config node zeromq
sudo easy_install pip
pip install --upgrade pyzmq jupyter
npm install -g ijavascript
ijsinstall

```

#### 5. 检查验证安装过的Jupyter内核

在Windows中安装完Jupyter的iJavaScript内核，可执行以下命令查看验证Jupyter相应的内核列表：

```
jupyter kernelspec list

```

<img src="https://img-blog.csdnimg.cn/37123e8a510c43d59309f39c39594126.png" alt="在这里插入图片描述"> 此时，证明JavaScript内核已经安装到Jupyter平台（可以启动Jupyter Lab或者Jupyter Notebook）

#### 6. Jupyter Lab应用JavaScript示例

**Jupyter Lab** 是最新的、基于 Web 的Notebook、代码和数据交互式开发环境。其灵活的界面允许用户配置和安排数据科学、科学计算、以及机器学习的工作流程。模块化设计赋予丰富的扩展功能。

除了Jupyter Notebook的功能之外，Jupyter Lab类似一个更加强大的综合平台，便于部署各类编程语言（例如：Python, JavaScript, Java, Ruby, Rust, Go, Kotlin以及Bash等）进行交互式开发。

因此，如果使用Jupyter Lab, 可以用以下命令安装：

```
pip install jupyter lab

```

<img src="https://img-blog.csdnimg.cn/f0cb23c35a1542ae9a9ab14a96af0232.png" alt="在这里插入图片描述"> 安装完毕后，使用以下命令启动Jupyter Lab.

```
jupyter lab

```

<img src="https://img-blog.csdnimg.cn/3d2e279aaf02402595209bf81338e408.png" alt="在这里插入图片描述"> 启动**Jupyter Lab**后，点击**File &gt; New &gt; Notebook**, 打开新的Notebook. <img src="https://img-blog.csdnimg.cn/d9f89565b09d46aa86931b8b9b74c04e.png" alt="在这里插入图片描述"> 选定JavaScript(Node.js)选项后，创建搭载JavaScript内核的、新的应用程序，执行以下示例代码：

```
let s = “Hello, world!”;
console.log(s);

```

<img src="https://img-blog.csdnimg.cn/95b920231db6414a85c1832c1c7aa0c9.png" alt="在这里插入图片描述">

代码执行成功！

这样，我们可以大踏步地利用Jupyter Lab平台来开发JavaScript程序了！

感谢点赞，敬请关注。😊

开发与运维好文不断，陆续推出。
