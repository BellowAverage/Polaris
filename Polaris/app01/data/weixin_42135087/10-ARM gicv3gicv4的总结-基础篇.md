
--- 
title:  10-ARM gicv3/gicv4的总结-基础篇 
tags: []
categories: [] 

---
>  
 <font color="purple" size="5">**快速链接:**</font> .   
 -  <font color="red" size="3">**【购买须知】:**</font>- -  ----<font color="red" size="3">**联系方式-加入交流群**</font> 




#### 目录
- <ul><li><ul><li><ul><li>- - - - - - - 


<img src="https://img-blog.csdnimg.cn/20201226000841778.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

##### 1、gic的版本

GIC是一个为Cortex-A和Arm Cortex-R设计的标准的中断控制器 <img src="https://img-blog.csdnimg.cn/20201225234610376.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

##### 2、GICv3/gicv4的模型图

<img src="https://img-blog.csdnimg.cn/20201225234458869.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

##### 3、gic中断号的划分
-  Shared Peripheral Interrupt (SPI) -  Private Peripheral Interrupt (PPI) -  Software Generated Interrupt (SGI) -  Locality-specific Peripheral Interrupt (LPI) <img src="https://img-blog.csdnimg.cn/20201225234723213.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> （使用示例） <img src="https://img-blog.csdnimg.cn/20201225234752352.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 
##### 4、GIC连接方式

<img src="https://img-blog.csdnimg.cn/2020122523493281.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

##### 5、gic的状态

<img src="https://img-blog.csdnimg.cn/20201225235010894.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **中断的生命周期:** 对于电平触发的中断(level-sensitive interrupts)，一个上升沿输入，将中断变成pending，中断信号线保持高电平直到PE断言该中断信号. 对于边沿触发的中断(edge-sensitive interrupts)，一个上升沿输入，将中断变成pending，中断信号线不会保持高电平. <img src="https://img-blog.csdnimg.cn/20201225235117600.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

##### 6、gic框架

• Distributor interface • Redistributor interface • CPU interface <img src="https://img-blog.csdnimg.cn/20201225235259787.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

**Distributor (GICD_*) for SPIs** • Interrupt prioritization and distribution of SPIs • Enable and disable SPIs • Set the priority level of each SPI • Route information for each SPI • Set each SPI to be level-sensitive or edge-triggered • Generate message-signaled SPIs • Control the active and pending state of SPIs • Determine the programmer’s model that is used in each Security state: affinity routing or legacy

**Redistributors (GICR_*)** • Enable and disable SGIs and PPIs • Set the priority level of SGIs and PPIs • Set each PPI to be level-sensitive or edge-triggered • Assign each SGI and PPI to an interrupt group • Control the state of SGIs and PPIs • Control the base address for the data structures in memory that support the associated interrupt properties and pending state for LPIs • Provide power management support for the connected PE

**CPU interfaces (ICC_*_ELn)** • Provide general control and configuration to enable interrupt handling • Acknowledge an interrupt • Perform a priority drop and deactivation of interrupts • Set an interrupt priority mask for the PE • Define the preemption policy for the PE • Determine the highest priority pending interrupt for the PE

In Arm CoreLink GICv3, the CPU Interface registers are accessed as System registers: ICC_*_ELn.

##### 7、gic Configuring

**全局配置** GICD_CTLR.ARE: Enable Affinity routing (ARE bits), 1-使用gicv3 mode，0-使用legacy mode(gicv2 mode). 默认为1 GICD_CTLR.EnableGrp1S GICD_CTLR.EnableGrp1NS GICD_CTLR.EnableGrp0

注意在GIC-600 does not support legacy operation

**(Redistributor)Settings for each PE** Redistributor中包含了一个GICR_WAKER寄存器，用于记录connected PE的状态是onLine还是offline. 如果让PE变成online，软件则必需这样做： • Clear GICR_WAKER.ProcessorSleep to 0. • Poll GICR_WAKER.ChildrenAsleep until it reads 0

如果PE is offline (GICR_WAKER.ProcessorSleep==1)时，来了一个中断target到该PE上，将产一个wake request信号，这个信号连接PE的power controller，该controller将会打开PE。然后PE clear the ProcessorSleep bit <img src="https://img-blog.csdnimg.cn/20201225235534516.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

**CPU interfaces (ICC_*_ELn)**

SRE bit— enable cpu interface 注：有些处理器可能不支持legacy operation，SRE比特位也是固定为1，那么软件就不需要处理该比特了

Set Priority Mask and Binary Point registers ICC_PMR_EL1、ICC_BPRn_EL1

Set EOI mode （EOI:End of interrupt） ICC_CTLR_EL1 and ICC_CTLR_EL3

Enable signaling of each interrupt group ICC_IGRPEN1_EL1 (banked by Security state) ICC_IGRPEN0_EL1

**PE configuration**
- Routing controls - SCR_EL3 、 HCR_EL2- Interrupt masks - PSTATE- Vector table - VBAR_ELn <img src="https://img-blog.csdnimg.cn/20201225235701217.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20201225235723412.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20201225235730468.png" alt="在这里插入图片描述">
**interrupt sources configuration**
- SPIs are configured through the Distributor, using the GICD_* registers.- PPIs and SGIs are configured through the individual Redistributors, using the GICR_* registers<li>
对于每一个中断，软件必需配置的：
- Priority: GICD_IPRIORITYn, GICR_IPRIORITYn- Group: GICD_IGROUPn, GICD_IGRPMODn, GICR_IGROUPn, GICR_IGRPMODn- Edge-triggered or level-sensitive: GICD_ICFGRn, GICR_ICFGRn- Enable: GICD_ISENABLERn, GICD_ICENABLER, GICR_ISENABLERn, GICR_ICENABLERn
<img src="https://img-blog.csdnimg.cn/20201225235856985.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **Setting the target PE for SPIs**
- GICD_IROUTERn.Interrupt_Routing_Mode == 0 rounting到制定的PE- GICD_IROUTERn.Interrupt_Routing_Mode == 1 Distributor硬件会自动选择一个PE，可以是0-n A PE can opt out of receiving 1-of-N interrupts. This is controlled by the DPG1S, DPG1NS and DPG0 bits in GICR_CTLR.
<img src="https://img-blog.csdnimg.cn/20201226000207594.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20201226000201423.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

**Routing a pending interrupt to a PE**
- Check that the group associated with the interrupt is enabled- Check that the interrupt is enabled- Check the routing controls to decide which PEs can receive the interrupt. routing is controlled by GICD_IROUTERn，An SPI can target one specific PE, or any one of the connected PEs- Check the interrupt priority and priority mask to decide which PEs are suitable to handle the interrupt Each PE has a Priority Mask register, ICC_PMR_EL1, in its CPU interface- Check the running priority to decide which PEs are available to handle the interrup Only an interrupt with a higher priority than the running priority can preempt the current interrupt
**软件读取中断号** <img src="https://img-blog.csdnimg.cn/20201226000324592.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **中断优先级** <img src="https://img-blog.csdnimg.cn/20201226000353328.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

**中断结束End of interrupt**
- Priority drop - 将中断优先级降到中断产生之前的值- Deactivation - 将中断从active变成inactive
在gicv3中，drop和deactivation通常是一起打开的。

ICC_CTLR_ELn.EOImode = 1: 通过写ICC_EOIR0_EL1、ICC_EOIR1_EL1让drop and deactivation同时生效 ICC_CTLR_ELn.EOImode = 0: 通过写ICC_EOIR0_EL1、ICC_EOIR1_EL1让drop生效，写ICC_DIR_EL1让deactivation生效，这在虚拟化中会用到.

大多数的软件系统中 EOIMode<mark>0，而下hypervisor的系统中 EOIMode</mark>1

**中断号的状态** <img src="https://img-blog.csdnimg.cn/20201226000525876.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **产生SGI中断** <img src="https://img-blog.csdnimg.cn/20201226000549280.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> PE在secure执行时，可以产生secure和non-secure的SGI; PE在non-secure执行时，也是可以产生secure的SGI，但是取决于GICR_NSACR寄存器的配置，该寄存器只能在secure中读写 <img src="https://img-blog.csdnimg.cn/20201226000624734.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

**比较GICv3和GICv2** 在gicv2中，SGI INTIDs对于originating PE和the target PE是banked 在gicv3中，SGI仅仅对target PE是banked

在gicv2中同时收到两个SGI=5中断，两个中断都会被PE处理。 而在gicv3上，由于originating不是banked，所有前一个SGI=5中断将会丢失。PE只能收到一个

**Legacy operation**
- When ARE==0, affinity routing is disabled (legacy operation)- When ARE==1, affinity routing is enabled (GICv3 operation)
<img src="https://img-blog.csdnimg.cn/direct/42df5de3f46646eeb4485183f01a6624.png" alt="在这里插入图片描述">

##### 推荐
-  --博客专栏-  --大课程-  --入门课程