
--- 
title:  14-ATF中对多核的支持 
tags: []
categories: [] 

---
讨论一个系统、一个软件或ATF对多核的支持，其实就是看这个软件，在启动阶段如何区分主核、从核的？ 在runtime阶段，是否能把不同核的CPU Data加以区分？是否能区分出cpuid?

### runtime阶段：主核和从核的区分

在启动阶段，会读取平台函数plat_is_my_cpu_primary来判单，当前是主核启动，还是从核启动。 <img src="https://img-blog.csdnimg.cn/direct/8ab72e18f4fe4c5fbdb89a4d4c3d550b.png" alt="在这里插入图片描述">

### runtime阶段：每个CPU都有独立的栈内存保存CPU数据

<img src="https://img-blog.csdnimg.cn/90bcfa54d66249f8a4881a8452ac4483.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

 - 编译的时候，定义了一个全局数组`percpu_data`，数组中的每一个元素代表一个cpu_data 初始化core的时候，将对应cpu_data写入到了该core的tpidr_el3寄存器中
 - 每个cpu_data中有两个cpu_context，[0]表示secure侧用的，[1]表示给non-secure侧用的
 - 使用类似如下这样的宏或函数，即可获取当前cpu、当前security的cpu_context
