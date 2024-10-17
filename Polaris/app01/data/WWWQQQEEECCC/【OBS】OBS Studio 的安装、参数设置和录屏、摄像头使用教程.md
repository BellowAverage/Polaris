
--- 
title:  【OBS】OBS Studio 的安装、参数设置和录屏、摄像头使用教程 
tags: []
categories: [] 

---
>  
 ✌ 作者简介：神奇的汪同学，一名在读的电子信息工程专业大学生. 📑 个人主页： 📫 如果文章知识点有错误的地方，请指正！和大家一起学习，一起进步👀 🔥 如果感觉博主的文章还不错的话，还请不吝👍关注、点赞、收藏三连支持👍一下博主哦 




#### 文章目录
- - - - <ul><li>- - - 


## 前言

`提示：这里可以添加本文要记录的大概内容：`

**OBS Studio功能介绍**

1、高性能实时视频/音频捕获和混合。创建由多个源组成的场景，包括窗口捕获、图像、文本、浏览器窗口、网络摄像头、捕获卡等。

2、设置无限数量的场景，您可以通过自定义转换无缝切换。

3、直观的混音器，每个源都带有滤波器，例如噪声门、噪声抑制和增益。完全控制与 VST 插件支持。

4、使用X264进行编码

5、无限数量的场景和来源

6、基于GPU的高性能游戏串流游戏抓拍

7、OBS Studio中文版支持DirectShow采集设备(相机、采集卡等)

8、强大且易于使用的配置选项。添加新源、复制现有源并轻松调整其属性。

## 一、OBS Studio 是什么？

OBS 或 Open Broadcaster Software，是一种免费的开源视频录制和视频实时流媒体软件。 占用资源少、配置要求相对较低，录音格式为MP4；它为用户提供了视频、文本、图像等的捕获录制功能，软件操作简单，界面清晰，能够自定义高质量的媒体推送和视频录制。

## 二、安装步骤

### 1.获取安装包

大家可以去OBS官网，然后选择自己电脑的系统版本去下载。

<img src="https://img-blog.csdnimg.cn/95242f3da20a40babbae883fb7043a7b.bmp#pic_center" alt="在这里插入图片描述"> 由于下载速度较慢，博主给大家下载好了，**链接在下面：** 「OBS-Studio-27.2.4-Full-Installer-x64.exe」https://www.aliyundrive.com/s/vhnNMJZttTH 提取码: y0l3

### 2.安装软件

下载完之后会显示这个图标，**双击安装**，如下图：

<img src="https://img-blog.csdnimg.cn/ea318ef5db4246c587a971a00f1f01f5.png" alt="在这里插入图片描述">

双击后出现如下界面，**点击Next**：

<img src="https://img-blog.csdnimg.cn/2b336466086543f78b0a57fa67b422a6.bmp#pic_center" alt="在这里插入图片描述"> 出现如下界面，**点击Next**：

<img src="https://img-blog.csdnimg.cn/e79d194c4c3e400e868cdb101ffe96af.bmp#pic_center" alt="在这里插入图片描述"> 选择好**安装路径**后，点击**Install**，

<img src="https://img-blog.csdnimg.cn/888915ec2d264935a6af75ec01e84cda.bmp#pic_center" alt="在这里插入图片描述"> 出现下面这个界面后等待几分钟，就安装好了。

<img src="https://img-blog.csdnimg.cn/f2029b75e078434eb245eb62f7b361b3.bmp#pic_center" alt="在这里插入图片描述"> 点击**Finish**。

<img src="https://img-blog.csdnimg.cn/754d5d15fa3c40db9f53906670e4c981.bmp#pic_center" alt="在这里插入图片描述">

## 二、使用步骤

### 1.参数设置

在桌面双击打开应用，点击**设置**：

<img src="https://img-blog.csdnimg.cn/ff6989d0e963498a90e649c8242e67e9.bmp#pic_center" alt="在这里插入图片描述">

**通用设置**如下：可以设置主题啥的大家可以自行设置。

<img src="https://img-blog.csdnimg.cn/ed853bf7748c4cfc8589484eb280e824.bmp#pic_center" alt="在这里插入图片描述"> **输出设置**：选择好自己的录屏的地址，以方便寻找（一般都在D盘）。其他设置可以按照下图设置。

<img src="https://img-blog.csdnimg.cn/2a368a1e2b04475f9019025d30693904.bmp#pic_center" alt="在这里插入图片描述">

**音频设置**如下：桌面音频和麦克风开一个就行选默认就可以了。（不需要开那么多）

<img src="https://img-blog.csdnimg.cn/d7d8fc838f1a46f699c3aadc66ea16a9.bmp#pic_center" alt="在这里插入图片描述"> **视屏设置**可以按照如下设置：

<img src="https://img-blog.csdnimg.cn/06468baf94eb48c8b90be8613be8f323.bmp#pic_center" alt="在这里插入图片描述">

### 2.场景设置

在**场景**里面右击点击**添加**，也可以点击左下角的加号：

<img src="https://img-blog.csdnimg.cn/d2722cbe42584ff8affce46318c96d29.png#pic_center" alt="在这里插入图片描述">

可以设置一个**场景名称**，然后点击**确定**，**场景**就建好了：

<img src="https://img-blog.csdnimg.cn/03ec39fae76047cb918ad29f2d904905.png#pic_center" alt="在这里插入图片描述"> 新建好的**场景**如下，来源框里面空白：

<img src="https://img-blog.csdnimg.cn/45186bf6126f422da114eed1cdac6cc9.png#pic_center" alt="在这里插入图片描述"> 在**来源**里面右击点击**添加**，也可以点击左下角的加号：

<img src="https://img-blog.csdnimg.cn/9ae8e655bfe74286a384302222898d1a.png#pic_center" alt="在这里插入图片描述"> 点击**显示器采集**后，出现如下界面点击**确定**：

<img src="https://img-blog.csdnimg.cn/e1bcd188f53d413090338b6742cc7c0a.png#pic_center" alt="在这里插入图片描述"> 出现下面这个界面，**点击确定**：

<img src="https://img-blog.csdnimg.cn/e870f97cdd7c428bb6f5b4129c8bcf69.png#pic_center" alt="在这里插入图片描述"> 就会出现下面这个界面，这样我们的显示器就设置好了！

<img src="https://img-blog.csdnimg.cn/f1309fcf52324d9694476e62bc5d7898.png#pic_center" alt="在这里插入图片描述"> 接下来我们设置摄像头，同理点击加号，点击**视屏采集设备**：

<img src="https://img-blog.csdnimg.cn/5205d1fbea274d17bedb8ace14aebf3d.png#pic_center" alt="在这里插入图片描述"> 出现下面这个界面，**点击确定**：

<img src="https://img-blog.csdnimg.cn/249aff99149b4393a163688fc44cf3e9.png#pic_center" alt="在这里插入图片描述"> 出现下面这个界面，**点击确定**：

<img src="https://img-blog.csdnimg.cn/c6a6966e1e534e40bef1b33562c8b32e.png#pic_center" alt="在这里插入图片描述">

就会出现下面这个界面，这样我们的**视屏采集器**就设置好了！

<img src="https://img-blog.csdnimg.cn/191f2dca85db4974b4faa15d71475d89.png#pic_center" alt="在这里插入图片描述"> 我们再把摄像头的画面调到合适的大小就可以了！

<img src="https://img-blog.csdnimg.cn/6da24e4b1e0041359d0560e92035e174.png#pic_center" alt="在这里插入图片描述">

**大家如果想具体去学习使用这个软件的话可以去看看这个up主，讲的特别详细！**



史上最强obs教学、傻瓜式教学（下载、直播、降噪、插件、分轨等）助你成为一个优秀的视频创作者！



## 总结

🔥 如果感觉博主的文章还不错的话，还请不吝关注、点赞、收藏三连支持👍一下博主哦！
