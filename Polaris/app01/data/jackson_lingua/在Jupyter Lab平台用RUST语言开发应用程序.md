
--- 
title:  在Jupyter Lab平台用RUST语言开发应用程序 
tags: []
categories: [] 

---
## 在Jupyter Lab平台用RUST语言开发应用程序

### Develop RUST Applications on Jupyter Lab Platform

>  
 **“A language empowering everyone to build reliable and efficient software.“** 这句座右铭的意思是，“赋予每个人力量的，构建可靠且有效软件的语言“。 


RUST，听起来既有些陌生，又似曾相识；依据RUST编程语言在其官网的展示，它具备的三个核心特点：
- **高性能**- **高可靠**- **高产能**
本文简要介绍如何获取安装和使用RUST – 这一新生代的、功能强大的编程语言；同时，详细步骤引导如何使用Jupyter Lab(Notebook)平台，来实现RUST交互式应用程序开发。

#### 1. 安装RUST

打开浏览器Chrome, 访问RUST官网下载页面，

<img src="https://img-blog.csdnimg.cn/a83ddc3fe300499592133ac5e7949db4.png" alt="在这里插入图片描述"> 点击**GET STARTED**, 进入下载页面，如下图。

<img src="https://img-blog.csdnimg.cn/77b9b7f6bdb94070b6ed10db0e90f4f3.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f695523dd2ac4cf2b042c9f7ad54dc12.png" alt="在这里插入图片描述"> 由于笔者电脑是Windows 10 64位系统，故选择**DOWNLOAD RUSTUP-INIT.EXE(64-BIT)** 点击下载。

下载完毕后，在Windows的**下载**文件夹，找到可执行文件**rustup-init.exe**，双击开始安装。如下图：

<img src="https://img-blog.csdnimg.cn/295dfbb916d4437b8e2a210205806970.png" alt="在这里插入图片描述">

选择1）项，可以快速启动**Visual Studio Community installer**安装（对个人、学术和开源免费）向导；这对于个人、学术用途及开源是免费的，按**ENTER**（回车）继续。

<img src="https://img-blog.csdnimg.cn/ac96b555a8024396a5fe19931c3726c7.png" alt="在这里插入图片描述"> 随即启动**Visual Studio Installer**安装向导（如上图），点击**Continue**继续。

<img src="https://img-blog.csdnimg.cn/7bd789828bc14f8f9fea775a0c686c6c.png" alt="在这里插入图片描述"> 默认选项有两项，分别为MSVC v143 和 Windows 11 SDK(10.0.22000.0), 继续保持选择，点击Install开始安装。

<img src="https://img-blog.csdnimg.cn/9f9e3ea147d843df8dce98b256f93694.png" alt="在这里插入图片描述"> 安装向导开始下载和安装软件包。

<img src="https://img-blog.csdnimg.cn/2e6f9b80a34f4c1690081531c6b6f677.png" alt="在这里插入图片描述"> 安装向导完成，显示Visual Studio已经安装成功！点击**OK**退出。

随即，自动启动Microsoft Visual Studio的启动欢迎画面：

<img src="https://img-blog.csdnimg.cn/76af5758260a43d9a1dc58eecadbfde7.png" alt="在这里插入图片描述"> 很快进入到Visual Studio 2022的启动对话框。

<img src="https://img-blog.csdnimg.cn/26e0c3d0613f4fb3a07be06194993c98.png" alt="在这里插入图片描述"> 此时，已经启动了Visual Studio 2022版本；它支持多种语言开发（例如：C++、C#等），无论个人还是企业应用程序，都可以用到Visual Studio. 在这里不再赘述。

接下来，回到命令行安装窗口，执行默认选项，于是，RUST开始安装：

<img src="https://img-blog.csdnimg.cn/43e22506511e4620bb158638b509adf6.png" alt="在这里插入图片描述"> 安装完毕，出现**Rust is installed now. Great!** 的字样，按**Enter** （回车）键退出该窗口。

此时，执行以下命令，查看一下安装先后的RUST版本差异：

```
rustc --version

```

<img src="https://img-blog.csdnimg.cn/27d2fd4ce9fb4c84b10492cf0884d92e.png" alt="在这里插入图片描述"> 我们看到，rustc版本从1.73.0升级为1.75.0. 即当前版本位1.75.0-nightly.

另外，执行一下命令查看工具链管理器版本为1.26.0.

```
rustup --version

```

<img src="https://img-blog.csdnimg.cn/0b5b22c1b2fc46b5b99e4771ccd73638.png" alt="在这里插入图片描述">

#### 2. 安装MiniConda3

访问MiniConda官网： <img src="https://img-blog.csdnimg.cn/9235b8cf15f44969b69ee3195f7a55eb.png" alt="在这里插入图片描述"> 为了实现Conda的轻量级安装，于是选择**Download Miniconda - free**，点击进入下载页。

<img src="https://img-blog.csdnimg.cn/c83f716472704761b2aee11f2f2d3796.png" alt="在这里插入图片描述"> 此时，选择Windows平台，点击**Miniconda3 Windows 64-bit**版本，点击下载。

#### 注：在Windows 64位操作系统下，可以使用命令行来快捷安装。执行以下命令：

```
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" miniconda.exe /S
del miniconda.exe

```

#### 3. 安装Darn

```
conda create -n darn python=3

```

<img src="https://img-blog.csdnimg.cn/54cd383764ab44cc8f6d858d0dd4e40a.png" alt="在这里插入图片描述"> 命令执行以下步骤：

```
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate darn
#
# To deactivate an active environment, use
#
#     $ conda deactivate

```

#### 4. 用conda激活Darn

执行以下命令：

```
conda activate darn

```

#### 5. 用conda安装 Cmake

```
conda install -c anaconda cmake -y

```

<img src="https://img-blog.csdnimg.cn/e98f97324d174b1584b99c1afd9d3e4d.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d12319ee2fc648dab8dd1c52ad802bc4.png" alt="在这里插入图片描述">

#### 6. 安装EvCxR Jupyter Kernel

##### 1） 执行命令安装evcxr_jupyter

```
cargo install evcxr_jupyter

```

<img src="https://img-blog.csdnimg.cn/be4857e803774515afe4d1557fea0b04.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f8eea81fcf6d44c1bebe0ed9042a84f3.png" alt="在这里插入图片描述">

##### 2） 执行命令：evcxr_jupyter –install

<img src="https://img-blog.csdnimg.cn/02d9cbf88fb74e4abfbe89a969916210.png" alt="在这里插入图片描述">

##### 3） 安装RUST标准库

如果你已在使用rust-analyzer，你可能已经安装过；否则，需要使用rustup来安装，如下命令：

```
rustup component add rust-src

```

#### 7. 重构Jupyter Lab

安装完毕后，为了稳妥起见，需要运行以下命令，来重构Jupyter Lab(或者Notebook):

```
jupyter lab build

```

#### 8. 验证已安装RUST的内核(Kernel)

在启动前，可以尝试验证Jupyter平台是否已经安装了RUST的内核，执行命令：

```
juyter kernelspec list

```

<img src="https://img-blog.csdnimg.cn/82b41dcfac06472399b4dc4eccf9e210.png" alt="在这里插入图片描述"> 可以看到，在列表中存在rust的可用内核（ **Available Kernel** ）.

#### 9. 启动Jupyter notebook

执行以下命令，可以启动Jupyter Notebook:

```
jupyter notebook

```

启动后，创建新的notebook文件，选择Rust内核即可开始Rust编程。

下面的例子，是如何在Jupyter Lab平台启动Rust内核并进行交互式开发。

#### 10. 启动Jupyter Lab平台

>  
 与Jupyter Notebook相比，Jupyter Lab 是最新的基于 Web 的交互式开发平台，兼容适用于notebook、代码和数据。 Jupyter Lab具备灵活的交互界面，允许用户配置和安排数据科学、科学计算、复杂计算旅程和机器学习工作流。它具有模块化设计，可灵活扩展及丰富各项功能。 


由于已经安装了Jupyter各个组件，启动Jupyter Lab用以下命令：

```
jupyter lab

```

<img src="https://img-blog.csdnimg.cn/aec5ce835d334701801f7102074fd11e.png" alt="在这里插入图片描述"> 选择Rust内核后，进入notebook交互式页面。

#### 11. 在Jupyter Lab上编写第一个RUST应用程序

启动Jupyter Lab后，需选择安装的RUST内核；点击File &gt; New &gt; Notebook, 即在Jupyter Lab创建了一个新的notebook, 选择**kernel** (内核)为Rust, 如下图：

<img src="https://img-blog.csdnimg.cn/c899557685d441f9a1500d849fc652ce.png" alt="在这里插入图片描述"> 点击**Select** (选择)确定启用Rust内核。

在编辑栏中，编写第一个RUST应用程序：

```
fn main(){<!-- -->
	println!(“Hello, world!”);
}
main();

```

执行交互式界面如下图： <img src="https://img-blog.csdnimg.cn/8e9e141333b44c8f85c6740a5c659aae.png" alt="在这里插入图片描述"> 代码运行成功！输出结果为：**Hello, world!**

至此，在Jupyter Lab（或者Notebook）平台已经能够编写RUST应用程序了。让我们一起继续前行吧！ 😊

喜欢就点赞哈。

技术好文陆续推出，欢迎关注。

（All rights reserved @ 2023. 版权所有，侵权必究）
