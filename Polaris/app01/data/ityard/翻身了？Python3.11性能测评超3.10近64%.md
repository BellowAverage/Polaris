
--- 
title:  翻身了？Python3.11性能测评超3.10近64% 
tags: []
categories: [] 

---
Python 这门编程语言的运行速度并不快，这早已不是什么秘密了。很多开发者期待这门语言的性能有所提升，这种情况或即将发生改变，或至少朝着正确的方向前进着，这也是Python的创始人重新出山后的决策结果之一。

5月7日，Python团队发布最新的 Python 版本 - Python 3.11。目前发布的是一个测试版本 (Beta1) ，供开发者们测试或实验时使用。

<img src="https://img-blog.csdnimg.cn/img_convert/e6cf16a385a8c8356624b38afc27ace6.png" alt="e6cf16a385a8c8356624b38afc27ace6.png">

按照开发团队的所定下规约，预计将于 2022 年 10 月正式版本将释出。

有好奇网友在自己的虚拟机上进行了测试，他在单独的 Docker 容器分别安装了 Python 3.10 和 3.11，并查看它们在一组基准测试中的比较。

在其中使用了pyperformance 包来完成这项工作，这个包会帮助开发者完成繁重的基准测试工作。

总结的数据，按平均数值来计算，Python 3.11 比 Python 3.10 快了 14%。3.11 新版本在某些基准测试上稍微慢了一点，但在大多数基准上，速度提高了 64%。

以下是在有着 10 核 CPU 的 M1 Pro MacBook Pro 16 上运行的基准测试。每个 Python 版本都安装在 Docker 中，它使用 5 个逻辑 CPU 内核。

以下是不同包的运行数据：

<img src="https://img-blog.csdnimg.cn/img_convert/dae0e7a830665ace6f7a9a9cc0f9dfe7.png" alt="dae0e7a830665ace6f7a9a9cc0f9dfe7.png">

目前Python 3.11 的正式版还未正式发布，需要等待一个完全稳定的版本，目前测试的仅是一个候选版本，也许正式版本发布后两者之间的差距会更大。

推荐阅读  点击标题可跳转
- - - - - - - - - 
<img src="https://img-blog.csdnimg.cn/img_convert/847129335c8fa0965e55067c15e43e2f.gif" alt="847129335c8fa0965e55067c15e43e2f.gif">
