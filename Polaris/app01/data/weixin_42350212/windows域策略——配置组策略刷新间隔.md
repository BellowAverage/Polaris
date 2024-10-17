
--- 
title:  windows域策略——配置组策略刷新间隔 
tags: []
categories: [] 

---
>  
 默认情况下，域中的计算机会在后台每隔 90 分钟更新一次计算机策略和用户策略，并将时间作 0 到 30 分钟的随机调整。除了后台更新之外，在系统启动时总会更新计算机的组策略。 6.5.1示例：配置“计算机配置”刷新频率 


以下操作将会为培训部计算机指定组策略中“计算机配置”刷新频率。

设置计算机组策略的更新频率，指定当计算机正在使用时计算机组策略的更新频率(在后台)。此设置只为“计算机配置”文件夹中的组策略指定后台更新频率。

**1. 如图6-119所示，在DCServer上，打开组策略管理工具，右击培训部组织单元下的eduGPO，点击“编辑”。**

**2. 如图6-120所示，在出现的组策略管理编辑器对话框，点中计算机配置下组策略，双击“计算机组策略刷新间隔”。**

<img alt="" height="546" src="https://img-blog.csdnimg.cn/95f578ca5bc4409b9965b88f4e077550.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBATGV4U2FpbnRz,size_19,color_FFFFFF,t_70,g_se,x_16" width="592">


