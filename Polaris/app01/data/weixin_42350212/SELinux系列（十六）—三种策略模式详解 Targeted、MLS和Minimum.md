
--- 
title:  SELinux系列（十六）—三种策略模式详解 Targeted、MLS和Minimum 
tags: []
categories: [] 

---
对于 SELinux 来说，所选择的策略类型直接决定了使用哪种策略规则来执行主体（进程）可以访问的目标（文件或目录资源）。不仅如此，策略类型还决定需要哪些特定的安全上下文属性。通过策略类型，读者可以更精确地了解 SELinux 所实现的访问控制。

<img alt="" height="308" src="https://img-blog.csdnimg.cn/118e95a451ba480794f051a2f567267a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBATGV4U2FpbnRz,size_9,color_FFFFFF,t_70,g_se,x_16" width="296"> SELinux 提供 3 种不同的策略可供选择，分别是 Targeted、MLS 以及 MiNimum。每个策略分别实现了可满足不同需求的访问控制，因此，为了正确地选择一个满足特定安全需求的策略，就不得不先了解这些策略类型。

 

Target 策略

Target 策略主要对系统中的服务进程进程访问控制，同时，它还可以限制其他进程和用户。服务进程都被放入沙盒，在此环境中，服务进程会被严格限制，以便使通过此类进程所引发的恶意攻击不会影响到其他服务或 Linux 系统。 沙盒（sandbox）是一种环境，在此环境中的进程可以运行，但对其他进程或资源的访问会被严格控制。换句话说，位于沙盒中的各个进程，都只是运行在自己的域（进程所运行的区域被称为“域”）内，它们无法访问其他进程或资源（除非被授予特殊的权限）。 通过使用此策略，可
