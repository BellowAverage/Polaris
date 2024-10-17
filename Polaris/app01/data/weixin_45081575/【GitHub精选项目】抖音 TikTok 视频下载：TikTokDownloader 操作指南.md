
--- 
title:  【GitHub精选项目】抖音/ TikTok 视频下载：TikTokDownloader 操作指南 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/5ff37e70767a47cab8cc08c1e0e35e2b.png" alt="在这里插入图片描述">

## 前言

>  
 本文为大家带来的是 `JoeanAmier` 开发的 `TikTokDownloader` 项目，这是一个高效的下载 抖音/ TikTok 视频的开源工具。特别适合用户们保存他们喜欢的视频或分享给其他人。 


`TikTokDownloader` 是一个专门设计用于下载 TikTok 视频的工具，旨在为用户提供一种快速且简便的方法来保存他们喜爱的 TikTok 内容。
- 它提供了直观的接口，如命令行，web 端，web_api 等；- 提供了多种下载功能，如**🔥 TikTok 主页/视频/图集/原声；抖音主页/视频/图集/收藏/直播/原声/合集/评论/账号/搜索/热榜** ；- 允许用户通过简单地输入视频链接来下载视频，而无需复杂的过程或技术知识；
接下来，本文将深入探讨 `TikTokDownloader` 项目的特点和使用方法，以帮助用户更好地了解如何充分利用这个工具。

作者还贴心的为 `Windows` 用户准备了编译好的 exe 程序。大大降低了上手的难度。实属非编程人员福音。

项目地址：

## 项目概览

看到项目的介绍，它的功能可谓是丰富十足。 作者还贴心的为 `Windows` 用户编译好 exe 程序。大大降低了上手的难度。

<img src="https://img-blog.csdnimg.cn/direct/900d52339d0947acbbbd04bd9b208882.png" alt="在这里插入图片描述">

## 克隆项目

### **git clone**

最简单的，在命令行工具数据以下命令即可，如下图所示：

```
git clone https://github.com/JoeanAmier/TikTokDownloader.git

```

<img src="https://img-blog.csdnimg.cn/direct/f02724583d4c4d5793c74267d9370c65.png" alt="在这里插入图片描述">

### **Download ZIP**

当然，使用 `Download ZIP` 也是个不错的下载方式。

<img src="https://img-blog.csdnimg.cn/direct/1646edf62e4b4fbf860c4b1729623faf.png" alt="在这里插入图片描述">

## 使用指南

该项目使用起来极其简单，只需简单配置即可。

下面做一些简单的介绍。

### step 1 配置环境

确保当前的 `Python` &gt;= 3.12.0，

去到项目目录下，安装所需要的库。在命令行执行以下命令即可。

```
pip install -r requirement.txt

```

### step 2 启动项目

运行 `main.py` ，

```
python mian.py

```

首次启动如下图，提示说需要设置 `Cookie` 然后重新运行程序；
- 会创建一个默认配置文件 `settings.json`
<img src="https://img-blog.csdnimg.cn/direct/e8deac418e33468687fada97faae4a78.png" alt="在这里插入图片描述">

### step 3 设置 Cookie

参考 ，

或者在重新运行时候，选择 **2** 扫码登录设置 `Cookie`

### step 4 下载视频

在设置好 `Cookie` 之后，重新启动程序，

（因为这里有多达4种运行模式，选择 `Web UI` 交互模式做展示）

这时候程序会调用系统默认的浏览器，去访问 `http://127.0.0.1:5000`

<img src="https://img-blog.csdnimg.cn/direct/9da2708cafbe44e4857f1c65b0dd1494.png" alt=""> 这时候我们可以先准备一个视频的链接，粘贴，然后点击，**获取下载链接**

<img src="https://img-blog.csdnimg.cn/direct/dbbea4c3936740adaad462f1ed5e50f5.png" alt="在这里插入图片描述">

来到下图，就可以成功下载啦！

<img src="https://img-blog.csdnimg.cn/direct/8d8a350aade44ed7b9e43f54b3432f45.png" alt="在这里插入图片描述">

## 注意事项

>  
 **Python 版本 &gt;= 3.12.0** 


参考这一份官方文档，。

因项目使用到了部分 `Python 3.12.0` 的新特性 ，而这些新特性没有向下兼容，所以在运行该项目时候，需要保证`Python` 版本大于等于`3.12.0`，下面简单说一下新特性。

具体会体现在以下两点，而只要使用上 &gt;= `Python 3.12.0`，就不会有以下问题出现。

**（1）shutil.which**

>  
 将在搜索路径的其他地方直接匹配之前返回 **cmd** 与来自 `PATHEXT` 的组件相匹配的路径。 


```
# shutil

def which(cmd, mode=os.F_OK | os.X_OK, path=None):
    ...

```

该项目会，

```
✅ 调用 ffmpeg 下载直播

```

而在项目初始化的过程中，会初始化 `settings.json` 文件，其中一个字段为 `ffmpeg`，值默认为空字符串，

```
# settings.json
{<!-- -->
    "accounts_urls": [],
    ...
    "ffmpeg": ""
}

```

这就到导致在使用下面代码时候，

```
import shutil
from pathlib import Path

# 默认为空字符串
ffmpeg_path = ""

shutil.which(Path(ffmpeg_path))

```

会引发一个异常，

```
AttributeError: 'WindowsPath' object has no attribute 'lower'. Did you mean: 'owner'?

```

**（2）引号重用**

>  
 **引号重用：** 新特性，即在 `f-字符串` 的使用中，支持了重用与标记 `f-字符串` 本身相同的引号。 


但是在 `Python 3.12.0` 之前，这样使用是会引出 `SyntaxError` 异常的。

如：

```
string = f"{"1 + 1"}"

```

运行会引发 `SyntaxError` 异常，

```
SyntaxError: f-string: expecting '}'

```

而在 `Python 3.12.0` 之后运行，`引号重用` 不会再引发 `SyntaxError` 异常。

## 总结

这个工具非常适合内容创作者和普通用户使用，因为它使他们能够轻松地保存重要的或有趣的内容，无论是用于个人回顾、好友分享、内容创作还是学术研究。

总之，`TikTokDownloader` 项目旨在为 TikTok 用户提供便捷的视频下载解决方案，帮助他们管理和享受 TikTok 上的优质内容。在合法和道德的前提下，这个工具为用户提供了更多选择，以便更好地利用 TikTok 平台上的视频资源。

## 后话

本次分享到此结束， 欢迎有质量的留言和评论， see you~~🎈🎈
