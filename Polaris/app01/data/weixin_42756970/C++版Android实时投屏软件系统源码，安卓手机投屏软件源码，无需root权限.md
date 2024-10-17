
--- 
title:  C++版Android实时投屏软件系统源码，安卓手机投屏软件源码，无需root权限 
tags: []
categories: [] 

---
## QtScrcpy

QtScrcpy 可以通过 USB / 网络连接Android设备，并进行显示和控制。无需root权限。

同时支持 GNU/Linux ，Windows 和 MacOS 三大主流桌面平台。 完整代码下载地址： 它专注于:
- **精致** (仅显示设备屏幕)- **性能** (30~60fps)- **质量** (1920×1080以上)- **低延迟** ()- **快速启动** (1s 内就可以看到第一帧图像)- **非侵入性** (不在设备上安装任何软件)
<img src="https://img-blog.csdnimg.cn/66c258e51bf84f67a979612b036147df.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/e58d5b9136f749408fccf6e500f93275.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/ff2988cbc9744e649cad42b763593fcc.png" alt="在这里插入图片描述">

### 自定义按键映射

可以根据需要，自己编写脚本将键盘按键映射为手机的触摸点击，编写规则在。

默认自带了针对和平精英手游和抖音进行键鼠映射的映射脚本，开启平精英手游后可以用键鼠像玩端游一样玩和平精英手游，开启抖音映射以后可以使用上下左右方向键模拟上下左右滑动，你也可以按照编写其他游戏的映射文件，默认按键映射如下：

<img src="https://img-blog.csdnimg.cn/447164a90f90430389d341321d2b47f1.jpeg" alt="在这里插入图片描述">



自定义按键映射操作方法如下：
- 编写自定义脚本放入 keymap 目录- 点击刷新脚本，确保脚本可以被检测到- 选择需要的脚本- 连接手机并启动服务之后，点击应用脚本- 按`~`（即脚本中定义的 SwitchKey）键切换为自定义映射模式即可启用- 再次按~键切换为正常控制模式- （对于和平精英等游戏）若想使用方向盘控制载具，记得在载具设置中设置为单摇杆模式
### 群控

你可以同时控制所有的手机

<img src="https://img-blog.csdnimg.cn/51b6e3a0d0cc406782f02ee6fb52c00c.gif" alt="在这里插入图片描述">

### 感谢

基于的项目进行复刻，重构，非常感谢。

### 比较

QtScrcpy 和 Scrcpy 区别如下：

|关键点<th align="center">scrcpy</th><th align="center">QtScrcpy</th>
|------
|界面<td align="center">sdl</td><td align="center">qt</td>
|视频解码<td align="center">ffmpeg</td><td align="center">ffmpeg</td>
|视频渲染<td align="center">sdl</td><td align="center">opengl</td>
|跨平台基础设施<td align="center">自己封装</td><td align="center">Qt</td>
|编程语言<td align="center">C</td><td align="center">C++</td>
|编程方式<td align="center">同步</td><td align="center">异步</td>
|按键映射<td align="center">不支持自定义</td><td align="center">支持自定义按键映射</td>
|编译方式<td align="center">Meson+Gradle</td><td align="center">CMake</td>
- 使用Qt可以非常容易的定制自己的界面- 基于Qt的信号槽机制的异步编程提高性能- 方便新手学习- 增加多点触控支持
### 要求

Android 部分至少需要 API 21（Android 5.0）。

您要确保在 Android 设备上。

### 运行

在你的电脑上接入Android设备，然后运行程序，点击 `一键USB连接` 或者 `一键WIFI连接`

#### 无线连接步骤
1. 将手机和电脑连接到同一局域网1. 安卓手机端在开发者选项中打开 USB 调试1. 通过 USB 连接安卓手机到电脑1. 点击刷新设备，会看到有设备号更新出来1. 点击获取设备 IP1. 点击启动 adbd1. 无线连接1. 再次点击刷新设备，发现多出了一个 IP 地址开头的设备，选择这个设备1. 启动服务
备注：启动 adbd 以后无需继续连接 USB 线，以后连接断开都不再需要，除非 adbd 停止运行

### 界面解释
<li> 启动配置：启动服务前的功能参数设置 分别可以设置本地录制视频的比特率、分辨率、录制格式、录像保存路径等。 
  <ul>- 仅后台录制：启动服务不显示界面，只录制 Android 设备屏幕- 窗口置顶：Android 设备显示窗口置顶- 自动息屏：启动服务以后，自动关闭 Android 设备屏幕以节省电量- 使用 Reverse：服务启动模式，出现服务启动失败报错 “more than one device” 可以去掉这个勾选尝试连接
刷新设备列表：刷新当前连接的设备

启动服务：连接到 Android 设备

停止服务：断开与 Android 设备的连接

停止所有服务：断开所有已连接的 Android 设备

获取设备ip：获取到 Android 设备的 IP 地址，更新到无线区域中，方便进行无线连接

启动adbd：启动 Android 设备的 adbd 服务，无线连接之前，必须要启动

无线连接：使用无线方式连接 Android 设备

无线断开：断开无线方式连接的 Android 设备

命令行：执行自定义 adb 命令（目前不支持阻塞命令，例如shell）

### 功能
- 实时显示 Android 设备屏幕- 实时键鼠控制Android设备- 屏幕录制- 截图- 无线连接- 多设备连接与群控- 全屏显示- 窗口置顶- 安装 apk：拖拽apk到显示窗口即可安装- 传输文件：拖拽文件到显示窗口即可发送文件到 Android 设备- 后台录制：只录制屏幕，不显示界面<li>剪贴板同步: 在计算机和设备之间同步剪贴板： 
  <ul>- `Ctrl + c`将设备剪贴板复制到计算机剪贴板；- `Ctrl + Shift + v`将计算机剪贴板复制到设备剪贴板；- `Ctrl + v` 将计算机剪贴板作为一系列文本事件发送到设备（不支持非ASCII字符）
### 快捷键

|功能<th align="left">快捷键(Windows)</th><th align="left">快捷键 (macOS)</th>
|------
|切换全屏<td align="left">`Ctrl`+`f`</td><td align="left">`Cmd`+`f`</td>
|调整窗口大小为 1:1<td align="left">`Ctrl`+`g`</td><td align="left">`Cmd`+`g`</td>
|调整窗口大小去除黑边<td align="left">`Ctrl`+`w` | **左键双击**</td><td align="left">`Cmd`+`w` | **左键双击**</td>
|点击 `主页`<td align="left">`Ctrl`+`h` | **点击鼠标中键**</td><td align="left">`Ctrl`+`h` | **点击鼠标中键**</td>
|点击 `BACK`<td align="left">`Ctrl`+`b` | **右键双击**</td><td align="left">`Cmd`+`b` | **右键双击**</td>
|点击 `APP_SWITCH`<td align="left">`Ctrl`+`s`</td><td align="left">`Cmd`+`s`</td>
|点击 `MENU`<td align="left">`Ctrl`+`m`</td><td align="left">`Ctrl`+`m`</td>
|点击 `VOLUME_UP`<td align="left">`Ctrl`+`↑` **(上)**</td><td align="left">`Cmd`+`↑` **(上)**</td>
|点击 `VOLUME_DOWN`<td align="left">`Ctrl`+`↓` **(下)**</td><td align="left">`Cmd`+`↓` **(下)**</td>
|点击 `POWER`<td align="left">`Ctrl`+`p`</td><td align="left">`Cmd`+`p`</td>
|打开电源<td align="left">**右键双击**</td><td align="left">**右键双击**</td>
|关闭屏幕 (保持投屏)<td align="left">`Ctrl`+`o`</td><td align="left">`Cmd`+`o`</td>
|打开下拉菜单<td align="left">`Ctrl`+`n`</td><td align="left">`Cmd`+`n`</td>
|关闭下拉菜单<td align="left">`Ctrl`+`Shift`+`n`</td><td align="left">`Cmd`+`Shift`+`n`</td>
|复制到剪切板<td align="left">`Ctrl`+`c`</td><td align="left">`Cmd`+`c`</td>
|剪切到剪切板<td align="left">`Ctrl`+`x`</td><td align="left">`Cmd`+`x`</td>
|同步剪切板并粘贴<td align="left">`Ctrl`+`v`</td><td align="left">`Cmd`+`v`</td>
|注入电脑剪切板文本<td align="left">`Ctrl`+`Shift`+`v`</td><td align="left">`Cmd`+`Shift`+`v`</td>

鼠标左键双击黑色区域可以去除黑色区域

如果电源关闭，鼠标右键双击打开电源；如果电源开启，鼠标右键双击相当于返回

### 为什么开发 QtScrcpy？

综合起来有以下几个原因，比重从大到小排列：
1. 学习Qt的过程中需要一个项目实战一下1. 本身具有音视频相关技能，对音视频很感兴趣1. 本身具有 Android 开发技能，好久没用有点生疏，需要巩固一下1. 发现了 Scrcpy，决定用新的技术栈（C++ + Qt + Opengl + FFmpeg）进行复刻
### 编译

尽量提供了所有依赖资源，方便傻瓜式编译。

#### QtScrcpy

##### 非 Arch Linux
1. 使用官方 Qt Installer 或非官方工具（如 ）在目标平台上搭建Qt开发环境。 需要 5.12 以上版本 Qt（在 Windows 上使用 MSVC 2019）1. 克隆该项目：`git clone --recurse-submodules git@github.com:barry-ran/QtScrcpy.git`1. Windows 使用 QtCreator 打开项目下 CMakeLists.txt 并编译 Release1. Linux 用终端执行 `./ci/linux/build_for_linux.sh "Release"` 注：编译结果位于 `output/x64/Release` 中
##### Arch Linux
1. 安装以下包：`qt5-base qt5-multimedia qt5-x11extras`（推荐安装 `qtcreator`）1. 克隆该项目：`git clone --recurse-submodules git@github.com:barry-ran/QtScrcpy.git`1. 用终端执行 `./ci/linux/build_for_linux.sh "Release"` 注：编译结果位于 `output/x64/Release` 中
#### Scrcpy-Server
1. 目标平台上搭建 Android 开发环境1. 使用 Android Studio 打开项目根目录中的 server1. 第一次打开时，如果你没有对应版本的 Gradle，Studio 会提示找不到 Gradle，是否升级 Gradle 并创建，选择取消，取消后会提示选择 Gradle 的位置，同样取消即可。Studio 会随后自动下载。1. 按需编辑代码1. 编译出 apk 以后改名为 scrcpy-server 并替换 `third_party/scrcpy-server` 即可