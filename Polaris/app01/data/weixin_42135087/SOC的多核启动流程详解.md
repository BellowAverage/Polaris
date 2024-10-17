
--- 
title:  SOC的多核启动流程详解 
tags: []
categories: [] 

---
>  
 <font color="purple" size="5">**快速链接:**</font> .   
 -  <font color="red" size="3">**【购买须知】:**</font>- -  ----<font color="red" size="3">**联系方式-加入交流群**</font> 




#### 目录
- <ul><li><ul><li><ul><li>- - - - <ul><li>- - - - 


>  
 **思考：** 1、 SOC一上电，只有一个核启动，还是所有核都启动？ 2、如果SOC一上电，如果只有一个核启动，那么从核启动的时候，从核的入口是哪里？ 3、啥是cold boot？ 啥时warm boot? 在哪些场景下会使用warm boot? 4、啥是cold reset/warm reset/primary boot/senondary boot？  <font color="red" size="3">**说明：**</font> 1、本文以为armv8-aarch64、armv9为例、TF-A代码为例，不讨论其它硬件架构和固件软件中的设计。 2、重点讲述cold reset/warm reset/primary boot/senondary boot之间的流程和概念。 


##### 1、基础概念

请先自行理解以下4个概念：
- cold boot- warm boot- Primary boot- Secondary boot
另外还两种配置：
- 你的reset地址是可编程的，则会配置`PROGRAMMABLE_RESET_ADDRESS=1`，与之对立的则是你的reset地址是不可编程的。- 你在SOC启动的时候，首先只启动一个core，则会配置`COLD_BOOT_SINGLE_CPU=1`，与之对立的则是你的SOC启动的时候，所有core都上电了。
##### 2、启动流程

我们就假定<font color="blue" size="4"> reset地址是可编程的、SOC启动的时候只启动一个core</font>，来讲解我们的boot流程：

(1)、SOC一上电，SOC给ARM Core的signal configuration会改变RVBAR_EL3，这里一般就是就是bootrom的首地址。即CPU一上电，Primary core的PC指向的就是RVBAR_EL3的地址，机器就开始启动了。

(2)、当需要Secondary Core启动的时候，例如会走PSCI协议，【主核】进入ATF会将bl31_warm_entrypoint（或平台自定义的地址）写入到SOC寄存器，改变reset地址(改变RVBAR_EL3的值)，然后此时SOC的PMIC给Secondary Core上电，此时Secondary Core也就发生了cold reset，PC从RVBAR_EL3(bl31_warm_entrypoint或平台自定义函数)处开始执行.

**总结**(针对本文示例情况：reset地址是可编程的、cold boot的时候只启动一个cpu)：
- 开机一上电只有Primary Core再跑，从RVBAR_EL3处开始跑，属于cold boot- 从核启动时，会修改reset的值，影响到RVBAR_EL3的值，然后给从核上电，此时属于Secondary boot，仍然是cold boot.- 一般会将bl31_warm_entrypoint设置为reset地址，即Secondary Core的启动地址;- 这个示例中没有用到warm boot
##### 3、ATF(TF-A)代码的剖析

以BL1代码为例分析，该代码适配支持cold reset/warm reset/primary boot/senondary boot等诸多场景。 <img src="https://img-blog.csdnimg.cn/b75b8b70c743482c9edf0c32d16c4537.png" alt="在这里插入图片描述">
- 如果reset是可编程的，`PROGRAMMABLE_RESET_ADDRESS=1`， 则`_warm_boot_mailbox = 0`，则下面这段代码不会被编译，无论cold boot还是warm boot都不会走`_warm_boot_mailbox `。- 如果reset是**不**可编程的，`PROGRAMMABLE_RESET_ADDRESS=0`， 则`_warm_boot_mailbox = 1`，则下面这段代码会被编译，但cold boot走`do_cold_boot `流程，warm boot需要走`br x0 `流程
```
	.if \_warm_boot_mailbox
		/* -------------------------------------------------------------
		 * This code will be executed for both warm and cold resets.
		 * Now is the time to distinguish between the two.
		 * Query the platform entrypoint address and if it is not zero
		 * then it means it is a warm boot so jump to this address.
		 * -------------------------------------------------------------
		 */
		bl	plat_get_my_entrypoint
		cbz	x0, do_cold_boot
		br	x0
do_cold_boot:
.endif /* _warm_boot_mailbox */

```
- 如果SOC启动的时候只启动一个core， `COLD_BOOT_SINGLE_CPU=1`，`_secondary_cold_boot = 0`，则下面代码不被编译， 则无论主核还是从核都不需要走`_secondary_cold_boot`流程- 如果SOC启动的时候启动多个core， `COLD_BOOT_SINGLE_CPU=0`，`_secondary_cold_boot = 1`， 则下面代码会被编译，则主核走`do_primary_cold_boot`流程， 从核需要走`plat_secondary_cold_boot_setup`流程
```
	.if \_secondary_cold_boot
		/* -------------------------------------------------------------
		 * Check if this is a primary or secondary CPU cold boot.
		 * The primary CPU will set up the platform while the
		 * secondaries are placed in a platform-specific state until the
		 * primary CPU performs the necessary actions to bring them out
		 * of that state and allows entry into the OS.
		 * -------------------------------------------------------------
		 */
		bl	plat_is_my_cpu_primary
		cbnz	w0, do_primary_cold_boot

		/* This is a cold boot on a secondary CPU */
		bl	plat_secondary_cold_boot_setup
		/* plat_secondary_cold_boot_setup() is not supposed to return */
		bl	el3_panic

	do_primary_cold_boot:

```

根据以上的代码规则，这里也画了两张图： (1)、BL2 at EL3的场景 <img src="https://img-blog.csdnimg.cn/0011b64f26454e2281e753b96a318e93.png" alt="在这里插入图片描述">

(2)、BL2 at S-EL1的场景 <img src="https://img-blog.csdnimg.cn/91ccbf2d7e544772851a85c7bd7783fe.png" alt="在这里插入图片描述">

##### 5、软件如何判断当前是cold reset/warm reset/primary boot/senondary boot

TF-A中定义了多核的启动框架，如上一节框图所示，在启动的过程中会进行一些判断，是cold reset还是warm reset，是primary boot还是secondary boot？那么代码中是怎么知道这些状态的呢？

###### 5.1 cold reset和warm reset

这种判断方法由平台实现，其实就是读取mailbox的值。 在第一个核cold boot时，会写mailbox内存（magic，entrypoint…） 在第二个核启动时、或第一个核再次启动时(有可能是resume唤醒时)，会读取mailbox内存，如果读取到了符合期望的magic的值，则走warm流程，否则走cold流程。 注意这里所说的warm流程，只是软件上的warm流程，并非说当前是warm reset。

###### 5.2 primary boot和secondary boot

这种判断方法由平台实现，看似也很简单，一般而言就说读取mpidr寄存器进行判断。

```
(trusted-firmware-a/plat/marvell/armada/a8k/common/aarch64/plat_helpers.S)

func plat_is_my_cpu_primary
	mrs	x0, mpidr_el1
	and	x0, x0, #(MPIDR_CLUSTER_MASK | MPIDR_CPU_MASK)
	cmp	x0, #MVEBU_PRIMARY_CPU
	cset	w0, eq
	ret
endfunc plat_is_my_cpu_primary

```

##### 6、mailbox的介绍

###### 6.1 mailbox是什么

mailbox就说一块内存，所有的core都能访问这块内存。 第一次启动时，core会填充mailbox，将其下次resume时的地址、secondary core的启动地址、warm reset的地址写入到mailbox内存中，这几个地址其实是一个地址。同时也会将这个地址写入到SOC PMIC寄存器中，影响到RVBAR_EL3的值。

当SOC一上电所有core都启动的这种情况下，主核会继续跑，从核会在SOC一上电就进入wfi状态。 当从核需要继续启动时，该core从BL1 BL2 BL31正常流程启动时，会在BL1、BL2 at EL3、BL31中，强制跳转到mailbox的地址，跳过主核已经初始化的部分；

当SOC一上电，只有一个core上电的情况下，主核继续跑，从核未上电。当从核需要启动时，相当于cold reset，从核会直接从RVBAR_EL3处开始跑，也就是你设置的entrypoint。

###### 6.2 mailbox的作用

mailbox中定义了entrypoint地址，当core从BL1 BL2 BL31正常流程启动时，会在BL1、BL2 at EL3、BL31中，强制跳转到mailbox的地址，以跳过已初始化的部分。 <img src="https://img-blog.csdnimg.cn/3ee82edda78849d4aff08ca94a8e307a.png" alt="在这里插入图片描述">

###### 6.3 mailbox的示例

其实就是定义了一块内存，主核第一次跑时，会填充该内存。 主核第二次跑时或从和跑时，检测该内存已经填充过了，则走warm启动流程，即强制跳转到mailbox中的address地址。 <img src="https://img-blog.csdnimg.cn/e21782e023af428aac3d0bdcadc02d0b.png" alt="在这里插入图片描述">

##### 7、具体场景的总结
- **串口中断中敲击reboot命令、或系统panic时导致的机器重启** ：在一些的SOC厂商设计中，应该是code reboot。比如在Linux Kernel中敲击reboot，到底层还是写的一些寄存器控制pmic(或PMU)，直接给cpu下电了。然后再上电，SOC还是会给Core发送signal configuration，此时RVBAR_EL3又会变成ASIC设置的值.- **Suspend和Resume** ： 比如我在看ATF中的海思平台，在ATF的suspend函数，将bl31_warm_entrypoint地址写入到了SOC PMIC的一个寄存器中(上电时，该寄存器会影响的是RVBARADDR信号)。 此时系统深睡的时候，应该是Linux Kernel调用到ATF，将bl31_warm_entrypoint地址写入到了pmu/pmic相关的寄存器中，在下一次reset时，会影响到signal configuration继而改变RVBAR_EL3的值。 然后还会给各个模块下电(给哪些模块下电是SOC的设计和逻辑)，最后再给ARM Core下电， 这就算是深睡了。 Resume的时候，也是有一些SOC的硬件行为，然后再给Core上电，那给Core上电后，一上电执行的是哪里？ PC还是指向RVBAR_EL3中的地址，当然这是我们suspend的时候更改过的，其实就是bl31_warm_entrypoint- **RMR_EL3** ：本文中都没有提到RMR_EL3。 那么RMR_EL3是干啥的呢？ 这是ARM的一个feature，怎么用？是你自己的设计，随便你。你写RMR_EL3中的bit，就可以触发warm reset. 一般的kernel dump、或者一些工具，就可以主动触发RMR_EL3，然后去干一些活. 还有在csdn上看到一篇高通soc的启动流程的博客，他们正常的启动流程中，某一个镜像跳转到另外一个镜像时，竟然就是写了一些RMR_EL3，触发warm_reset，另外一个镜像的地址恰好就是warm reset的跳转地址。
##### 推荐
-  --博客专栏-  --大课程-  --入门课程