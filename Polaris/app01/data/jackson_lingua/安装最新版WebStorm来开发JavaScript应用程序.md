
--- 
title:  安装最新版WebStorm来开发JavaScript应用程序 
tags: []
categories: [] 

---
## 安装最新版WebStorm来开发JavaScript应用程序

### Install the Latest Version of JetBrains WebStorm to Develop JavaScript Applications

By Jackson@ML 2023-11-25

#### 1. 系统要求

WebStorm是个跨平台集成开发环境（IDE）。按照JetBrains官网对WebStorm软件运行的基本要求，计算机至少要达到以下配置：
- **CPU**，现代任意款CPU（包含i3, i5, i7或ARM64等）；- **RAM**，至少2GB空闲内存；建议8GB内存。- **磁盘空间**，至少3.5GB可用磁盘空间；建议5GB固态硬盘空间。- **显示器分辨率**，至少1024x768；建议1920x1080分辨率。- **操作系统**，最少需要微软Windows 10 1809或更新版/macOS 10.15或更新版/Linux操作系统支持Gnome, KDE或Unity DE；建议最新的Windows 11, macOS或Linux发行版(Debian, Ubuntu或RHEL)
#### 2. 下载JetBrains WebStorm

打开Chrome浏览器，访问WebStorm官网链接： 如下图所示： <img src="https://img-blog.csdnimg.cn/e0c96bdc8296439a981e59e22fba07a1.png" alt="在这里插入图片描述"> 点击页面或右上角的**Download**，进入到下载页面。

<img src="https://img-blog.csdnimg.cn/890ae258bd604cfc9f7e74014ba7560f.png" alt="在这里插入图片描述"> 在下载页面，含有支持三个操作系统(Windows, masOS和Linux)的WebStorm应用程序。 但是，没有可供学习的免费社区版，只有30天试用版。可以先下载试用，然后根据情况购买该专业版。

点击 **Download** 下载。 <img src="https://img-blog.csdnimg.cn/87843c26921d4bb79d11fc9911f00491.png" alt="在这里插入图片描述">

下载页面中出现**Thank you for downloading WebStorm！**的感谢下载字样，Chrome也开始下载该软件；此时，如果浏览器不能正常下载，可以点击页面中的 **direct link** 进行直接下载。

#### 3. 独立安装WebStorm

WebStorm是JetBrains开发套件的一员，可以通过JetBrains Toolbox安装，也可以独立安装。本文仅介绍独立安装的步骤。

软件下载完毕后，在Windows 10/11下载文件夹，找到最新版安装包可执行文件 **WebStorm-2023.2.5.exe**，双击启动安装向导。

<img src="https://img-blog.csdnimg.cn/99b2bf8dd236415787ccfe4111df2d7f.png" alt="在这里插入图片描述"> 点击 **Next** 进行下一步。

<img src="https://img-blog.csdnimg.cn/ce4d28dd21894116940485e289d85b46.png" alt="在这里插入图片描述"> 按照默认安装 **Destination Folder**(目标文件夹)，点击 **Nex**t 进行下一步。

<img src="https://img-blog.csdnimg.cn/057c725973854f1bad1e19149bb355af.png" alt="在这里插入图片描述"> 在Installation Options(安装选项)对话框中，复选选择以下几项：
- **Create Desktop Shortcut**(创建桌面快捷方式)的 **WebStorm**- **Update Context Menu**(更新上下文菜单)中的 **Add”Open Folder as Project”**(添加打开文件夹作为项目)- **Create Associations**(创建关联)中的 **.js** (关联.js文件到程序)- 以及**Update PATH Variable**(更新PATH变量)的 **Add “bin” folder to the PATH**(增加bin文件夹到PATH环境变量)，都选好之后，点击 **Next** 继续下一步。
<img src="https://img-blog.csdnimg.cn/d0245f4445a14798bcdacb23b260aa65.png" alt="在这里插入图片描述"> 在**Choose Start Menu Folder** (选择开始菜单文件夹)对话框中，按默认选项，点击 **Install** 开始安装。

<img src="https://img-blog.csdnimg.cn/228f846ac9cb4bdbb861e02d9f692db0.png" alt="在这里插入图片描述"> 安装开始，向导进行系统设置和拷贝必要的文件等；很快安装完成。

<img src="https://img-blog.csdnimg.cn/c118cd38fd234740b36267a7b414ad32.png" alt="在这里插入图片描述"> 完成安装，按照默认选项 **I want to manually reboot later** (我想稍后手动重启计算机)，点击 **Finish** 结束安装。

#### 4. 启动并使用WebStorm

>  
 WebStorm 是一个集成开发环境，用于使用 JavaScript 及其相关技术进行软件开发，包括 TypeScript、React、Vue、Angular、Node.js、HTML 和CSS。就像 IntelliJ IDEA 和其它JetBrains IDE 一样，WebStorm 使您的开发体验更加愉快，可以自动执行日常工作并帮助您轻松处理复杂的任务。 


在Windows搜索栏，输入关键字 WebStorm，打开**WebStorm 2023.2.5**快捷菜单，选择**以管理员身份运行**，点击启动该程序。 <img src="https://img-blog.csdnimg.cn/730cd457f4c948e391453181383a6e91.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/046e597ed32c48c0b7b19eaf710ea81e.png" alt="在这里插入图片描述"> 点击 **New Project** 来创建一个新的项目，选择项目所在文件夹，在本文中，假设选择D:\myJavaScript\Projects 作为项目文件夹，如下图:

<img src="https://img-blog.csdnimg.cn/947db4e105db4d66ac6f26c3f976b378.png" alt="在这里插入图片描述"> 点击 **Create** 创建。 <img src="https://img-blog.csdnimg.cn/00ab4866e951473cb5b167be4fa18626.png" alt="在这里插入图片描述"> 用鼠标选择**File菜单**，点击**New – JavaScript File**, 创建一个JavaScript文件，命名为**hello_world.js**.

<img src="https://img-blog.csdnimg.cn/3f56a67e68844b3bb5e1917eeb42dc40.png" alt="在这里插入图片描述"> 为新程序文件编写第一个简单的JavaScript代码，如下图：

```
let wd = "world!";
console.log("Hello,", wd);

```

点击上方运行按钮，执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/fc4f29648e424186aafccb1bb073feb7.png" alt="在这里插入图片描述"> JavaScript程序运行成功！

接下来，就可以利用WebStorm来开发一系列JavaScript应用程序，并体验强大的集成开发功能了。

技术好文陆续推出，敬请关注。

喜欢就点赞哈！**您的认可，我的动力**。😊

#### 相关阅读：
1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 