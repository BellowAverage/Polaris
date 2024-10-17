
--- 
title:  11-ATF初始化Normal cpu context 
tags: []
categories: [] 

---
ATF (Arm Trusted Firmware) 初始化 Normal CPU Context 的步骤主要涉及设置正常世界（Normal World）CPU的环境，确保在从安全世界（Secure World）切换到正常世界时，CPU能够正确执行正常世界的代码。以下是一般步骤的概述：

 -  CPU启动与初始化: 在系统启动时，CPU首先在安全世界（Secure World）下执行。ATF负责初始化系统的各个部分，包括内存、安全设置和其他硬件配置。 
 -  设置安全状态: ATF会设置CPU从安全世界（Secure World）到正常世界（Normal World）的切换。这包括配置安全配置寄存器，例如SCR（Secure Configuration Register），以允许正常世界访问。 
 -  上下文保存: 在切换到正常世界之前，ATF会保存当前的CPU上下文，包括寄存器和其他状态信息。这样，当从正常世界返回安全世界时，可以恢复这些状态。 
 -  配置正常世界环境: ATF配置正常世界的环境，这包括设置堆栈指针、程序计数器等。它确保当切换到正常世界时，CPU能够在正确的地址开始执行代码。 

以下是代码导读和介绍

<img src="https://img-blog.csdnimg.cn/direct/a072cce4f6554c5c8c0230052e0722d7.png" alt="在这里插入图片描述">

在
