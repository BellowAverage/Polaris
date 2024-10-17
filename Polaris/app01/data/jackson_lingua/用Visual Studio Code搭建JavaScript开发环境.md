
--- 
title:  用Visual Studio Code搭建JavaScript开发环境 
tags: []
categories: [] 

---
## 用Visual Studio Code搭建JavaScript开发环境

### Build a JavaScript Development Environment with Visual Studio Code

当代最流行的Web编程语言当属JavaScript，并且她经历了ECMAScript多个版本的迭代，每次都给人们全新的感觉，因为她不断带来新的改进和保持Web开发应有的强大功能。

>  
 用JavaScript作为编程语言的开发工具有很多，哪种可以作为敏捷开发的轻量级IDE（集成开发环境）呢？答案无疑是Visual Studio Code. 


>  
 微软开发的这款产品是开源的，免费的；但这丝毫不影响它的灵活度、可扩展性及强大功能。 Visual Studio Code 不仅是个集成开发工具，而且还包括内置的 JavaScript IntelliSense、调试、格式设置、代码导航、重构和许多其他高级语言功能。 


本文简要介绍如何快速安装配置Visual Studio Code，以便启动使你立刻萌发兴趣的JavaScript编程工作。

#### 1. 下载和安装Visual Studio Code

从微软官方链接，, 可以打开**Visual Studio Code**主页；点击页面上方或者中间的**Download for Windows**，即可进入Visual Studio Code下载页面。

<img src="https://img-blog.csdnimg.cn/a2354d97eb7a488db37f8e4509805359.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c70f51c58bf347b1ad94283540f36e2f.png" alt="在这里插入图片描述"> 由于目前是在Windows系统，故选择Windows 10, 11并点击对应**x64的User Installar**下载安装包。

接下来，跳转到感谢下载的页面，如下图： <img src="https://img-blog.csdnimg.cn/90c916cbb17040f186298dd785acdaf9.png" alt="在这里插入图片描述"> 下载完毕后，从Windows的**下载**文件夹，双击名为**VSCodeUserSetup-x64-1.84.0.exe**的可执行文件开始安装。

<img src="https://img-blog.csdnimg.cn/a83584d916c94a56ab7d947775e64d47.png" alt="在这里插入图片描述"> 点击选择**I accept the agreement**(我同意这份协议)，点击**Next**继续下一步。

<img src="https://img-blog.csdnimg.cn/efd424c89eb849f098d466ee2abd98d3.png" alt="在这里插入图片描述"> 默认选项**Add to PATH**（即添加到PATH环境变量）已被勾选；再选择**Create a desktop icon**，增加桌面的快捷方式。点击**Next**继续下一步。

<img src="https://img-blog.csdnimg.cn/fd94d22cd6fb4edcb7cb6c02cdeb082c.png" alt="在这里插入图片描述"> 点击**Install**开始安装。

<img src="https://img-blog.csdnimg.cn/4d8ce1789e554201a4607c24643e10b6.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2292ded5edc3490a889692b75b6f6fec.png" alt="在这里插入图片描述"> 安装完毕，点击**Finish**退出安装向导。此时，由于默认勾选**Launch Visual Studio Code**，于是，系统很快启动了Visual Studio Code应用程序，如下图：

<img src="https://img-blog.csdnimg.cn/05a24c83ee8b4db3a4869edfbc47e8fd.png" alt="在这里插入图片描述">

#### 2. 添加JavaScript扩展（extensions）

Visual Studio Code（简称VS Code）的大多数功能都是开箱即用的，而有些功能可能需要基本配置才能获得最佳体验。如果需要立刻开发JavaScript应用程序，则需要 VS Code 附带的 JavaScript 功能。

毫无疑问，VS Code 的力量来自市场。多亏了精彩的开源社区，VS Code开发工具现在能够支持几乎所有的编程语言、框架和开发技术。对库或框架的支持有多种方式，主要包括该特定技术的代码片段、语法突出显示、Emmet 和 IntelliSense 功能。

在VS Code **Marketplace** 中的大量扩展(extensions)可以增强或更改其中的大多数内置功能。 本文摘选了笔者常用的一些扩展如下：

##### 1） IntelliSense

IntelliSense 显示智能代码完成(即代码补全)、悬停信息和签名信息，以便你可以更快、更正确地编写代码。VS Code 在 JavaScript 项目中提供 IntelliSense;对于许多 npm 库，例如 React、lodash 和 express;以及节点、无服务器或 IoT 等其他平台。

##### 2） JavaScript Snippets（代码片段）

JavaScript （ES6） 代码片段，作者：Charalampos Karypidis。这是目前最流行的 javaScript 片段扩展，迄今为止安装量超过300多万次。此扩展为 JavaScript、TypeScript、HTML、React 和 Vue 提供 ES6 语法。所有代码段都包含最后一个分号。 有许多扩展提供了额外的代码段，包括流行框架（如 Redux 或 Angular）的代码段。您甚至可以定义自己的代码段。

##### 3） Babel JavaScript

由迈克尔·麦克德莫特 （Michael McDermott）开发。迄今为止，该扩展已安装超过 550k+，为 ES201x JavaScript、React、FlowType 和 GraphQL 代码提供语法高亮显示。

##### 4） JSHint

作者：Dirk Baeumer。有超过一百二十万次的安装，此扩展支持使用 JSHint 库进行 linting。扩展需要 .jshintrc 配置文件才能对代码进行 lint 检查。

##### 5） npm IntelliSense

作者：Christian Kohler。有超过190万次的安装，此扩展在 import 语句中提供自动完成 npm 模块。

##### 6） Prettier Code Formatter

作者：Esben Petersen。这是最流行的扩展，提供更加漂亮的代码格式化功能；支持使用 Prettier 来格式化 JavaScript、TypeScript 和 CSS。迄今为止，它的安装量已超过 570 万次。建议在本地安装 prettier 作为开发依赖项。

##### 7） Preview on Web Server

作者：YuichiNukiyama。它提供了 Web 服务器和 HTML 的实时预览。可以从上下文菜单或编辑器菜单调用这些功能。迄今为止，它有 120k+ 的安装量。

##### 8） Vue.js Extension Pack

由Muhammad Ubaid Raza撰写。这是 Vue 和 JavaScript 扩展的集合。它目前包含大约 12 个 VS Code 扩展，其中一些未在此处提及，例如 auto-rename-tag 和 auto-close-tag。迄今为止，它的安装量已超过 156k。

<img src="https://img-blog.csdnimg.cn/8912b8a4378f4829b497b3773206d6e8.png" alt="在这里插入图片描述"> 在Visual Studio Code中，点击左侧导航栏的**Extension图标**，然后在上方搜索栏输入关键字，就能找到上述任何需要的extension (扩展)，然后点击**Install**进行安装, 即可完成相应扩展的安装。

#### 3. 开始JavaScript编程

安装完扩展后，重新打开Visual Studio Code，准备开始JavaScript编程吧！ 根据笔者经历，可以安装一个**Live Server**扩展，可以模拟浏览器演示Javascript运行结果。 <img src="https://img-blog.csdnimg.cn/446fd21d73b14a87a41922b786d671c6.png" alt="在这里插入图片描述"> 在Extension搜索到**Live Server**后，点击右侧软件区**Install**即可安装；安装完毕后，不需要的话，可以选择**Disable**(禁用)或者**Uninstall**(卸载)，如上图。

接下来编写一段最简单的“你好，世界！“控制台程序代码，保存为index.js文件，如下所示：

```
console.log(“Hello, world!”);

```

点击运行，执行成功！如下图所示。 <img src="https://img-blog.csdnimg.cn/d1ed395d59ee4a22b0ac60f208ddf357.png" alt="在这里插入图片描述"> 成功！接下来，我们可以利用Visual Studio Code做各种JavaScript开发啦。

欢迎关注；喜欢就点赞哈！😊 更多好文陆续推出。……
