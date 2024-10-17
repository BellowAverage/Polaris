
--- 
title:  2024最新版Java Development Kit (JDK)安装使用指南 
tags: []
categories: [] 

---
## 2024最新版Java Development Kit (JDK)安装使用指南

### Installation and Configuration Guide of the latest version Java Development Kit (JDK) in 2024

By Jackson@ML

#### 0. 序言

>  
 **What is Java?** Java is a programming language and computing platform first released by Sun Microsystems in 1995. It has evolved from humble beginnings to power a large share of today’s digital world, by providing the reliable platform upon which many services and applications are built. New, innovative products and digital services designed for the future continue to rely on Java, as well. — from https://www.java.com/ 


Java诞生于1995年，走过二十八年的历程，她已发展成为健壮普及的企业级应用程序开发语言。随之而来的，是Java不停改进和升级，带给我们一系列宽广且深邃的强大功能。

无论是Sun公司发布的JDK1.0-JDK1.3，还是Oracle收购后发展日臻完善的JDK21，我们都伴随着她的成长，逐渐成熟。

本文简要介绍2024年初，Oracle公司最新版Java Development Kitchen（JDK，Java开发包）的安装使用步骤。希望对读者有所帮助。

#### 1. 下载JDK 21

打开 Chrome浏览器，访问Java官网链接：，如下图所示。

<img src="https://img-blog.csdnimg.cn/direct/b84b82fa395641f3ae7ac5c6c0e75e12.png" alt="在这里插入图片描述"> 点击主页面右上角的 **Download Java** 按钮，进入到下载页面。

<img src="https://img-blog.csdnimg.cn/direct/1c3093458e3844ea971126808e36c90e.png" alt="在这里插入图片描述"> 将鼠标滚轮向下移动，找到Windows选项卡对应的64位版本软件安装包 – **x64 MSI Installer**, 点击该链接下载，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/ca89e0a5959242e391280dbd1149515c.png" alt="在这里插入图片描述"> 同时，为了持续学习和参考，点击 **Documentation Download** 下载官方Java文档，这与操作系统无关，直接使用即可。

下载在Chrome浏览器快速进行，很快就会下载完毕。

#### 2. 安装JDK 21

JDK下载完毕后，在Windows的下载文件夹里，找到安装可执行文件 **jdk-21_windows-x64_bin.msi**, 双击该文件启动安装向导。

如下图所示： <img src="https://img-blog.csdnimg.cn/direct/631068ae54714713af31b017bce6b070.png" alt="在这里插入图片描述"> 点击 **Next** 继续安装。 <img src="https://img-blog.csdnimg.cn/direct/95b5794f2591495cbb58b00210621d5f.png" alt="在这里插入图片描述"> 点击Change，修改默认路径到 D:\JDK21，这是为了避免C:\ 分区文件过多而访问效率降低。点击 **Next** 继续下一步。

<img src="https://img-blog.csdnimg.cn/direct/040ef55068514f859bcc960444ffef28.png" alt="在这里插入图片描述"> 于是开始安装。

<img src="https://img-blog.csdnimg.cn/direct/e62e8f6c784e427bb14badfdd8476192.png" alt="在这里插入图片描述"> 安装成功！点击 **Close** 关闭安装向导。

#### 3. 设置环境变量

在Windows搜索栏，键入 **控制面板**，点击 **系统** 进入：

<img src="https://img-blog.csdnimg.cn/direct/8e07af34d8194f58ae2582636b7687fe.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/27acbc1ce6474206b0d519b1c7e12745.png" alt="在这里插入图片描述"> 点击高级设置，如下图：

<img src="https://img-blog.csdnimg.cn/direct/b50b65c210f740178d7fceadcb7dd727.png" alt="在这里插入图片描述"> 点击环境变量，找到系统变量的 **path**，点击编辑，如下图： <img src="https://img-blog.csdnimg.cn/direct/c26b8eaac02240a2b21643c7964d792c.png" alt="在这里插入图片描述"> 在编辑对话框中，新增一条记录，假如JDK21刚刚安装过的路径 D:\JDK21\bin, 点击确定。

<img src="https://img-blog.csdnimg.cn/direct/f721413af1a441208acf0a50dd961a32.png" alt="在这里插入图片描述">

这是，JDK21安装且环境变量配置完毕。

#### 4. 验证JDK21版本

打开命令行提示符(cmd), 使用以下命令：

```
java –version

```

<img src="https://img-blog.csdnimg.cn/direct/a5ad1abe9f4746ccbad36902898c3756.png" alt="在这里插入图片描述"> 经过验证，新安装的Java开发包版本为最新版21.0.2(发布于2024年1月16日)。

#### 5. 安装配置Visual Studio Code

我的Window系统率先安装好了Visual Studio Code最新版，现在，让我们一道来编写并运行第一个Java应用程序！

打开Visual Studio Code，选择打开创建的Java工作目录 D:\myJava\sample, 如下图所示： <img src="https://img-blog.csdnimg.cn/direct/837c8d8e9f524752ba18ed0553ee50f5.png" alt="在这里插入图片描述"> 点击左侧导航栏的Extension（扩展）按钮，接下来在上方Marketplace搜索栏，搜索 **Extension Pack for Java**, 点击 **Install** 进行安装。安装完毕后如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/9b32e862bfe443ef916cd11434129fdf.png" alt="在这里插入图片描述"> 与此同时，与之连贯的Debugger for Java, Test Runner for Java, Project Manager for Java和Maven for Java等四个扩展（或成为插件）也一道自动安装完成！

#### 6. 编写并运行第一个Java应用程序

在刚才打开的D:\myJava\sample目录中，创建一个新的Java文件hello_world.java, 编写代码如下图所示：

```
class hello_world {<!-- -->
    public static void main(String[] args) {<!-- -->
        System.out.println("Hello, world!");
    }
}

```

运行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/04657ae7ca43420f90d33d9b872ef0fb.png" alt="在这里插入图片描述"> 可以看到，运行结果为Hello, world! 第一个Java应用程序执行成功！

这意味着，2024最新版JDK21安装成功！

技术好文陆续推出，敬请关注。 您的认可，我的动力！ 😃

#### 相关阅读
1. 1. 1. 1. 1. 