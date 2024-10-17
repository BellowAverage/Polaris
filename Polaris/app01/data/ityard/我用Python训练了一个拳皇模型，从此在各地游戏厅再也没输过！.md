
--- 
title:  我用Python训练了一个拳皇模型，从此在各地游戏厅再也没输过！ 
tags: []
categories: [] 

---
从世界瞩目的围棋游戏 AlphaGo。

<img src="https://img-blog.csdnimg.cn/img_convert/fcdab216a564a1247630c6608b263b7f.png" alt="fcdab216a564a1247630c6608b263b7f.png">

<img src="https://img-blog.csdnimg.cn/img_convert/8d11cccacbb9afb92be2bc2a0918a69b.png" alt="8d11cccacbb9afb92be2bc2a0918a69b.png">

<img src="https://img-blog.csdnimg.cn/img_convert/aca858df1a109230fe333d1cf9e6d0ee.gif" alt="aca858df1a109230fe333d1cf9e6d0ee.gif">

突然袭来的回忆杀~

今天为大家介绍一个在街机游戏《街头霸王 3》中进行模拟来训练改进强化学习算法的工具包。不仅在 MAME 游戏模拟器中可以使用，这个 Python 库可以在绝大多数的街机游戏中都可以训练你的算法。

<img src="https://img-blog.csdnimg.cn/img_convert/5b7827cc087b0958b420d3758cd9804a.gif" alt="5b7827cc087b0958b420d3758cd9804a.gif">

<img src="https://img-blog.csdnimg.cn/img_convert/96b5c887d925bac62a4fcdd0a4d2b689.gif" alt="96b5c887d925bac62a4fcdd0a4d2b689.gif">

下面营长就从安装、设置到测试分步为大家介绍一下。

目前这个工具包支持在 Linux 系统，作为 MAME 的包装器来使用。通过这个工具包，你可以定制算法逐步完成游戏过程，同时接收每一帧的数据和内部存储器的地址值来跟踪游戏状态，以及发送与游戏交互的动作。

首先你需要准备的是：
- 操作系统：Linux- Python 版本：3.6+
▌安装

你可以使用 pip 来安装该库，运行下面的代码:

<img src="https://img-blog.csdnimg.cn/img_convert/ec55274a1b125ea085edc307d3ad686e.png" alt="ec55274a1b125ea085edc307d3ad686e.png">

▌《街头霸王3》示例

<img src="https://img-blog.csdnimg.cn/img_convert/8384250260b06536ba81ee2a0ae00bae.png" alt="8384250260b06536ba81ee2a0ae00bae.png">

下面的代码演示了如何在街头霸王的环境下编写一个随机智能体。

<img src="https://img-blog.csdnimg.cn/img_convert/5c7ee50a21c942c59b1a55f9c5fb0356.png" alt="5c7ee50a21c942c59b1a55f9c5fb0356.png">

此外，这个工具包还支持 hogwild 训练:

<img src="https://img-blog.csdnimg.cn/img_convert/f96b6081290e13310907b48967f55e68.png" alt="f96b6081290e13310907b48967f55e68.png">

<img src="https://img-blog.csdnimg.cn/img_convert/074697a941d895fb684ae6016d33010a.gif" alt="074697a941d895fb684ae6016d33010a.gif">

<img src="https://img-blog.csdnimg.cn/img_convert/e4be06479b5c4d79fc2df96aaa33a224.gif" alt="e4be06479b5c4d79fc2df96aaa33a224.gif">

▌游戏环境设置
- 游戏 ID
<img src="https://img-blog.csdnimg.cn/img_convert/5cd3922ad064fe8bbab31680ec5f6749.png" alt="5cd3922ad064fe8bbab31680ec5f6749.png">

你可以通过运行以下代码来查看游戏ID：

<img src="https://img-blog.csdnimg.cn/img_convert/0d36e2f40040efa63d06870eba5ab975.png" alt="0d36e2f40040efa63d06870eba5ab975.png">

该命令会打开 MAME 模拟器，你可以从游戏列表中选择你所要的那款游戏。游戏的 ID 通常位于标题后面的括号中。
- 内存地址
<img src="https://img-blog.csdnimg.cn/img_convert/4191013ec3de11dfaf510eabb62a67ac.png" alt="4191013ec3de11dfaf510eabb62a67ac.png">

可以使用以下命令运行 Debugger：

<img src="https://img-blog.csdnimg.cn/img_convert/6de77a7e5db2a74027472e66f6086fb4.png" alt="6de77a7e5db2a74027472e66f6086fb4.png">

> 
   更多关于该调试工具的使用说明请参考此教程：https://www.dorkbotpdx.org/blog/skinny/use_mames_debugger_to_reverse_engineer_and_extend_old_games 
 

当你确定了所要跟踪的内存地址后可以执行以下命令进行模拟：

<img src="https://img-blog.csdnimg.cn/img_convert/be026f1df6b069d7fd04a443d2b073a2.png" alt="be026f1df6b069d7fd04a443d2b073a2.png">

该命令会启动模拟器，并在工具包导入到模拟器进程时暂停。
- 分步模拟
在工具包导入完成后，你可以使用 step 函数分步进行模拟：

<img src="https://img-blog.csdnimg.cn/img_convert/077a52839824eef6a3b88ced6152c260.png" alt="077a52839824eef6a3b88ced6152c260.png">

step 函数将以 Numpy 矩阵的形式返回 frame 和 data 的值，同时也会返回总时间步长的所有内存地址整数值。
- 发送输入
如果要向仿真器输入动作，你还需要确定游戏支持的输入端口和字段。例如，在街头霸王游戏中需要执行以下代码进行投币：

<img src="https://img-blog.csdnimg.cn/img_convert/6829bc32d906bbd8cf365ff62cf81938.png" alt="6829bc32d906bbd8cf365ff62cf81938.png">

可以使用 list actions 命令查看所支持的输入端口，代码如下：

<img src="https://img-blog.csdnimg.cn/img_convert/1329931338d5501d4363287c7e52b04b.png" alt="1329931338d5501d4363287c7e52b04b.png">

以下返回的列表就包含了街头霸王游戏环境中可用于向 step 函数发送动作的所有端口和字段：

<img src="https://img-blog.csdnimg.cn/img_convert/f5e02ecee7cb1d9f6edc4b2c2ddb3af8.png" alt="f5e02ecee7cb1d9f6edc4b2c2ddb3af8.png">

模拟器还有一个 frame_ratio 参数，可以用来调整你的算法帧率。在默认设置下，NAME 每秒能生成 60 帧。当然，如果你觉得这样太多了，你也能通过以下代码将其改为每秒 20 帧：

<img src="https://img-blog.csdnimg.cn/img_convert/f1e6bc78e36463fe1cbc0af016f5a361.png" alt="f1e6bc78e36463fe1cbc0af016f5a361.png">

<img src="https://img-blog.csdnimg.cn/img_convert/7208ce521eb5ba4c8d176e4c9a521927.gif" alt="7208ce521eb5ba4c8d176e4c9a521927.gif">

▌性能基准测试

<img src="https://img-blog.csdnimg.cn/img_convert/d474ac117d9629c5389ddd4b238dccac.png" alt="d474ac117d9629c5389ddd4b238dccac.png">

▌简单的 ConvNet 智能体

<img src="https://img-blog.csdnimg.cn/img_convert/54c50366e2292e8ed1d9e075b494c259.png" alt="54c50366e2292e8ed1d9e075b494c259.png">

<img src="https://img-blog.csdnimg.cn/img_convert/ce62664be573f573a02ad7edcad8862a.png" alt="ce62664be573f573a02ad7edcad8862a.png">

<img src="https://img-blog.csdnimg.cn/img_convert/460ac3266aa628003807d46f55c560c6.gif" alt="460ac3266aa628003807d46f55c560c6.gif">

声明：本文于网络整理，版权归原作者所有。

<img src="https://img-blog.csdnimg.cn/img_convert/ffbe7089e448485c4faf38cf87014cde.png" alt="ffbe7089e448485c4faf38cf87014cde.png">
