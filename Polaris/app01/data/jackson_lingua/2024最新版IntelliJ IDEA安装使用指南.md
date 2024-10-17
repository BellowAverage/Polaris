
--- 
title:  2024最新版IntelliJ IDEA安装使用指南 
tags: []
categories: [] 

---
## 2024最新版IntelliJ IDEA安装使用指南

### Installation and Usage Guide to the Latest JetBrains IntelliJ IDEA Community Editionn in 2024

By Jackson@ML

>  
 JetBrains公司开发的IntelliJ IDEA一经问世，就受到全球Java/Kotlin开发者的热捧。这款集成开发环境（Integrated Development Environment, 简称IDE）融合了几乎所有强大功能，以其高度集成和高效协同工作的特点，在软件业界快速推进敏捷开发。 


#### 1. 下载JetBrains IntelliJ IDEA Community Edition

打开Chrome浏览器，访问IntelliJ IDEA官网链接： ， 如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/79babf11c66c49019c68d5b2f0c7809d.png" alt="在这里插入图片描述"> 点击上方导航栏菜单 **Developer Tools** (开发工具)， 选择**IntelliJ IDEA**，点击进入产品页面。

<img src="https://img-blog.csdnimg.cn/direct/05fdc805b961480eabf42ece15d900c0.png" alt="在这里插入图片描述">

进入下载页面，点击页面正中的 **Download** 按钮，进行下载。

<img src="https://img-blog.csdnimg.cn/direct/7af72bacd84449a2903ed9db3ae54e58.png" alt="在这里插入图片描述"> 进入到下载页面，选择需要下载的版本。可以看到，上方是IntelliJ IDEA Ultimate, 这是专业付费版；下方是 **IntelliJ IDEA Community Edition**, 这是社区版，可免费使用。

当前，我们就下载这款社区版。

<img src="https://img-blog.csdnimg.cn/direct/ab5ecc0e37b24e10a33f8bcfd12b6626.png" alt="在这里插入图片描述"> 点击社区版下方的 Download按钮，开始下载。

<img src="https://img-blog.csdnimg.cn/direct/77ba505fce1746aca048d7d9f87ad880.png" alt="在这里插入图片描述"> 出现收集Email的表单， 如果需要在评估期内收到提示和文档，那么可以注册Email地址并订阅消息；如果不需要评估和收到提示及文档，就等待下载提示。

此时，如果没有按照预期下载，则点击页面中的 direct link 强制开始下载。IDEA的最新版本为2023.3.3版本。

#### 2. 安装最新版IDEA

Chrome浏览器下载结束后，在Windows的下载文件夹，找到该可执行安装文件 **ideaIC-2023.3.3.exe**, 双击启动安装向导。如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/cc83cc53a34e4805bc7149d5f21b1550.png" alt="在这里插入图片描述"> 点击 **下一步** 继续安装。

<img src="https://img-blog.csdnimg.cn/direct/863127fb499d49a49be713bf143f1d1c.png" alt="在这里插入图片描述"> 由于先前安装过，因此，需要先删除老的版本，点击 **下一步** 继续安装。

<img src="https://img-blog.csdnimg.cn/direct/8cb0b0f7ebb547d7a38429f48056ddcb.png" alt="在这里插入图片描述"> 复选两项，删除之气版本的IDEA社区版缓冲区和本地历史，以及相关设置和插件。点击 **Uninstall** (卸载)。

卸载完毕后，继续安装。

<img src="https://img-blog.csdnimg.cn/direct/633b9cedbdc64184bbc9a6d4a97f9247.png" alt="在这里插入图片描述"> 按照默认安装路径，点击 **下一步** 继续安装。

<img src="https://img-blog.csdnimg.cn/direct/2daeaa4832ba41fbb6ffcad2da806162.png" alt="在这里插入图片描述"> 复选两个选项： 1） 创建桌面快捷方式：IntelliJ IDEA Community Edition; 2） 添加“bin”文件夹到PATH环境变量中。

点击 **下一步** 继续安装。 选择开始菜单目录，确认名称无误，点击 **安装**。

<img src="https://img-blog.csdnimg.cn/direct/83bd64b939594512b3d54301e8e0d5bf.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/18005cdbe1844702b632e7e21f4f90c0.png" alt="在这里插入图片描述">

开始复制安装文件，很快就会完成。

<img src="https://img-blog.csdnimg.cn/direct/1c62d173ebaf4b4192eaf50884042f4c.png" alt="在这里插入图片描述"> 安装向导结束任务，点击完成退出。

#### 3. 创建和运行Java应用程序

在搜索栏中，找到 **IntelliJ IDEA Community Edition**，点击打开，启动该集成开发环境。

<img src="https://img-blog.csdnimg.cn/direct/a7d953cb694b4150856667814e3fe639.png" alt="在这里插入图片描述"> 出现对话框，按默认选项 **Do not import settings**（不输入设置），点击OK进入。

<img src="https://img-blog.csdnimg.cn/direct/7d9ad0d4c60c4622b8d2cacfd21fcc2a.png" alt="在这里插入图片描述"> 启动后，出现欢迎画面，然后来到IDE启动对话框。可以点击New Project以创建新的项目，系统自动检测JDK版本，检测完毕，会回到IDE界面。

命名新项目为hello_world, 然后点击确定启动新的Java项目，如下图：

<img src="https://img-blog.csdnimg.cn/direct/0494a396986e468bb3aa775205439098.png" alt="在这里插入图片描述"> 右键单击，在右键菜单中，选择 New &gt; Java Class，输入文件名称Hello_World.java, 如下图：

<img src="https://img-blog.csdnimg.cn/direct/0e2159f9b3ef4b6f9cccf9fbb61a2f6c.png" alt="在这里插入图片描述"> 在新建的文件中，写入Java代码：

```
public class Hello_World {<!-- -->
    public static void main(String[] args) {<!-- -->
        System.out.println("Hello, world!");
    }
}

```

在IDEA导航栏中，点击运行按钮.<img src="https://img-blog.csdnimg.cn/direct/718d6cc76c5f4b8fbe929bbbaf29ad3e.png" alt="在这里插入图片描述"> 执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/ee80f2a91b1d49cb87ec4a38f605014f.png" alt="在这里插入图片描述"> 在IntelliJ IDEA编写的第一个Java程序运行成功！

至此，可以使用2024最新版IntelliJ IDEA来开发各种Java应用程序啦！

技术好文陆续推出，敬请关注。 您的认可，我的动力！ 😊

#### 相关阅读
1. 1. 1. 1. 1. 1. 