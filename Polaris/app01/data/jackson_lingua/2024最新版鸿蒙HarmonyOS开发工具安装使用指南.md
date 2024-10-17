
--- 
title:  2024最新版鸿蒙HarmonyOS开发工具安装使用指南 
tags: []
categories: [] 

---
## 2024最新版鸿蒙HarmonyOS开发工具安装使用指南

By Jackson@ML

#### 0. 什么是鸿蒙Harmony OS？

华为鸿蒙系统（HUAWEI Harmony OS），是华为公司在2019年8月9日于东莞举行的华为开发者大会（HDC.2019）上正式发布的分布式操作系统。

华为鸿蒙系统是一款全新的面向全场景的分布式操作系统，创造一个超级虚拟终端互联的世界，将人、设备、场景有机地联系在一起，将消费者在全场景生活中接触的多种智能终端，实现极速发现、极速连接、硬件互助、资源共享，用合适的设备提供场景体验。

#### 1. 下载鸿蒙Harmony OS开发工具

打开Chrome浏览器，访问鸿蒙开发者官网：, 如下图所示： <img src="https://img-blog.csdnimg.cn/direct/976d02219e6e4a27b35e4d936802c931.png" alt="在这里插入图片描述"> 看到主页面显示的HUAWEI DevEco Studio，点击立即下载：

进入鸿蒙开发工具下载页面。看到排列在最上方的是鸿蒙开发工具IDE： DevEco Studio 3.11版本下载区域。

<img src="https://img-blog.csdnimg.cn/direct/57c379498c414144833911b3cfa9b597.png" alt="在这里插入图片描述"> 选择Windows(64-bit), 点击右侧Download进行下载；在Chrome浏览器上方，能够查看下载进度，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/6d42a485395d426e94ec21b228f46d24.png" alt="在这里插入图片描述"> 等到进度结束，则下载完成。

#### 2. 安装鸿蒙Harmony OS开发工具

下载完毕后，在Windows下载文件夹里，找到 **deveco-studio-3.1.0.501.exe**安装可执行文件。双击它开始安装向导。

<img src="https://img-blog.csdnimg.cn/direct/4f9c347c739648ed81f745d4091fda3e.png" alt="在这里插入图片描述"> 点击Next继续。

<img src="https://img-blog.csdnimg.cn/direct/9251ed2bdf8a47ef9cdc960ea32403f5.png" alt="在这里插入图片描述"> 点击Next继续。

<img src="https://img-blog.csdnimg.cn/direct/53662cfcfc324f9a8b8f24db813524e7.png" alt="在这里插入图片描述"> 在Installation Options(安装选项)中，复选三个选项，点击Next进行下一步。

<img src="https://img-blog.csdnimg.cn/direct/e2397b5d41b54f0dbcd4445f19b36a66.png" alt="在这里插入图片描述"> 点击Install开始安装。

<img src="https://img-blog.csdnimg.cn/direct/4725c84cb2254d2aa065f2bcbaaea474.png" alt="在这里插入图片描述"> 开始提取安装文件，很快安装结束，如下图所示。 <img src="https://img-blog.csdnimg.cn/direct/80f5e4a4e86f46889b38e6cd7210f61d.png" alt="在这里插入图片描述"> 按照默认选项， I want to manually reboot later (我想稍后手动重启)， 点击Finish退出安装向导。

#### 3. 创建Hello, world工程

在Windows搜索栏中，搜索关键字DevEco Studio, 点击 以管理员身份运行， 打开该程序，如下图：

<img src="https://img-blog.csdnimg.cn/direct/b6edf9f989a7453fa4743a21950a6071.png" alt="在这里插入图片描述"> 这是许可证协议对话框，点击Agree（同意）。 <img src="https://img-blog.csdnimg.cn/direct/3307a54802314d07ae5d09afbb51434e.png" alt="在这里插入图片描述"> 选择Do not import setings，点击OK。 随即出现Huawei EcoStudio欢迎画面，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/fcf79b11ecd143b3a57c679ff9c7bfa5.png" alt="在这里插入图片描述">

#### 4. 环境配置

进入DevEco Studio的环境配置，如下图：

<img src="https://img-blog.csdnimg.cn/direct/9b2615dea84941e2b8bb9b602eb37571.png" alt="在这里插入图片描述"> 复选从华为镜像网站安装Node.js, 并从默认安装路径安装Ohpm, 点击Next继续。

<img src="https://img-blog.csdnimg.cn/direct/00e9b9ad69c749baa26073ba5d03c3c0.png" alt="在这里插入图片描述"> 进入SDK Setup环节，点击Next继续。

<img src="https://img-blog.csdnimg.cn/direct/847b0cc4af274ce38dab23c2872a45e2.png" alt="在这里插入图片描述"> 在SDK License Agreement环节，点击Accept， 接受许可证协议条款，点击Next继续。

预览确认后，点击Next继续下一步。

<img src="https://img-blog.csdnimg.cn/direct/8a7f01d030fe4b388f77274fb946a9c7.png" alt="在这里插入图片描述"> 接下来，进入到下载安装过程，包括SDK以及功能工具链等，包括安装ArkTs dependencies(ArkTs依赖)， 如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/b87e3b73da13418abc95a51aef9be8e5.png" alt="在这里插入图片描述"> 安装完毕，配置结果成功！出现如下对话框： <img src="https://img-blog.csdnimg.cn/direct/77cc68be3d3d4239bba0b84d4a93389d.png" alt="在这里插入图片描述"> 点击Finish退出DevEco Studio安装配置向导。

<img src="https://img-blog.csdnimg.cn/direct/a42506af62a444c2b9d07b546975c9cb.png" alt="在这里插入图片描述"> 此时，点击Create Project，来创建一个新项目。

<img src="https://img-blog.csdnimg.cn/direct/b1270a2d1514499598a7b5eabe3bc109.png" alt="在这里插入图片描述"> 选择第一个Empty Ability，点击Next继续下一步。

<img src="https://img-blog.csdnimg.cn/direct/7c741664a1b9480f9f7d824239f3a224.png" alt="在这里插入图片描述"> 修改默认选项，命名项目为Hello_World, 点击Finish结束对Hello World项目的程序配置。 <img src="https://img-blog.csdnimg.cn/direct/08638903cdec4410856e194c7e4f262e.png" alt="在这里插入图片描述"> 点击Finish结束配置。

<img src="https://img-blog.csdnimg.cn/direct/ad8840fdb79346b58c9d4905ef7b5475.png" alt="在这里插入图片描述">

进入DevEco Studio的IDE界面，又自动安装扩展等插件。 看到左侧有不同的文件列表呈树形结构，点击上方Project菜单，点击Ohos，使各项分分类显示如下：

<img src="https://img-blog.csdnimg.cn/direct/bb13375310794d9e8be1efd335a70560.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/36d34f3f64944793a76c015dcaf03616.png" alt="在这里插入图片描述">

#### 5. 运行Hello World应用程序

阅览界面会显示手机上的预览效果，点击右侧的Preview选项卡，此时Loading Preview需要几秒钟，如下图所示： <img src="https://img-blog.csdnimg.cn/direct/97b68797abdb477994c150d1ceb09319.png" alt="在这里插入图片描述"> 左侧的开发文件主要在ets文件夹，其下的/pages子文件夹存放页面，而index.ets是首页页面。

预览效果显示如下图：

<img src="https://img-blog.csdnimg.cn/direct/6ba303d59f3e4da68a4f2b8e48f2c82c.png" alt="在这里插入图片描述"> 右侧Hello World为手机模拟页面效果。

<img src="https://img-blog.csdnimg.cn/direct/66e9de432e164c44b9024c9580f55af2.png" alt="在这里插入图片描述"> 选择Tools菜单 &gt; Device Manager, 如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/e990da65cea84bdbaf3a87129d8abdb0.png" alt="在这里插入图片描述"> 点击Install， 来安装模拟器，类型是Phone（手机）：

<img src="https://img-blog.csdnimg.cn/direct/a2f7cf33570b40af94301a3521c0edc8.png" alt="在这里插入图片描述"> 于是开始SDK Components Setup(SDK组件安装)，点击右下角New Emulator(新模拟器)：

<img src="https://img-blog.csdnimg.cn/direct/f921b7d262e440508ab3fe75268f68de.png" alt="在这里插入图片描述"> 按照Select Hardware默认选项，即Huawei手机，点击Next。

<img src="https://img-blog.csdnimg.cn/direct/ed3f55b528c1458abac810d64616aa9b.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/a5de05de2e184cc4a3a1558132182b79.png" alt="在这里插入图片描述">选择第一个选项，即API 9版本，点击Next。 接下来，继续SDK Components Setup (SDK组件安装）环节。 <img src="https://img-blog.csdnimg.cn/direct/a7f38957181345a38dc7e6e7b3687eec.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/1e05e8189e9849e8865910f5c719d22b.png" alt="在这里插入图片描述">

进一步完成满足这个要求的SDK Components Setup, 点击Finish退出安装向导。

安装这个手机模拟器组件后，出现可选的界面，选择安装好的它，点击Next。

<img src="https://img-blog.csdnimg.cn/direct/7bc32788dcaa47b0beb4f704f3f4145b.png" alt="在这里插入图片描述"> 自定义新的手机模拟器为Jackson_Huawei_Phone, 点击 Finish。 <img src="https://img-blog.csdnimg.cn/direct/0fe24a280f4248af8f97c5d60f8ba6e1.png" alt="在这里插入图片描述"> 该手机被创建！它出现在对话框列表中，如下图： <img src="https://img-blog.csdnimg.cn/direct/36fcec2d122f44ab8322665cd718c9e6.png" alt="在这里插入图片描述"> 完成后，点击右侧的 **|&gt; Actions**按钮，运行该模拟器，等待手机开机。 <img src="https://img-blog.csdnimg.cn/direct/0479012d64b1414c8030fd94a219951d.png" alt="在这里插入图片描述"> 伴随着华为鸿蒙悦耳的声音，手机开机。

待HarmonyOS Logo出现后，开机完毕。

点击右上方运行按钮， 屏幕会成功显示Hello World！

#### 6. 查看ArkTS语言文档

用于鸿蒙系统编程语言是ArkTS语言。

<img src="https://img-blog.csdnimg.cn/direct/5d8dd3ef165a4d739d07ba2307d9ea78.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/da6380065f41478babdd12f403b70452.png" alt="在这里插入图片描述"> 技术好文陆续推出，敬请关注。

您的鼓励，我的动力! 😃
