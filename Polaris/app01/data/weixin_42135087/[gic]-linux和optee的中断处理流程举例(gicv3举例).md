
--- 
title:  [gic]-linux和optee的中断处理流程举例(gicv3举例) 
tags: []
categories: [] 

---
>  
 <font color="purple" size="5">**快速链接:**</font> .   
 -  <font color="red" size="3">**【购买须知】:**</font>- -  ----<font color="red" size="3">**联系方式-加入交流群**</font> 




#### 目录
- <ul><li><ul><li><ul><li>- - - <ul><li>- - - - 


本文转自 周贺贺，baron，代码改变世界ctw，Arm精选， armv8/armv9，trustzone/tee，secureboot，资深安全架构专家，11年手机安全/SOC底层安全开发经验。擅长trustzone/tee安全产品的设计和开发。

##### 环境配置:

在linux/optee双系统环境下, linux系统的SCR.IRQ=0、SCR.FIQ=1, optee系统的SCR.IRQ=0、SCR.FIQ=0

##### 说明:

group1是非安全中断、secure group1是安全中断

##### 举例

###### 1、当cpu处于REE，来了一个非安全中断

当cpu处于normal侧时，来了一个非安全中断，根据SCR.NS=1/中断在group1组，cpu interface将会给cpu一个IRQ，(由于SCR.IRQ=0，IRQ将被routing到EL1)，cpu跳转至linux的irq中断异常向量表， 处理完毕后再返回到normal(linux)侧.

###### 2、当cpu处于TEE，来了一个安全中断

当cpu处于secure侧时，来了一个安全中断，根据SCR.NS=0/中断在secure group1组，cpu interface将会给cpu一个IRQ，(由于SCR.IRQ=0，IRQ将被routing到EL1)，cpu跳转至optee的irq中断异常向量表， 处理完毕后再返回到secure(optee)侧. <img src="https://img-blog.csdnimg.cn/20200702112237501.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

###### 3、当cpu处于TEE，来了一个非安全中断

当cpu处于secure侧时，来了一个非安全中断，根据SCR.NS=0/中断在group1组，cpu interface将会给cpu一个FIQ，(由于SCR.FIQ=0，FIQ将被routing到EL1),跳转至optee的fiq中断异常向量表, 再optee的fiq处理函数中，直接调用了smc跳转到ATF， ATF再切换至normal EL1(linux)， 此时SCR.NS的状态发生变化，根据SCR.NS=1/中断在group1组，cpu interface会再给cpu发送一个IRQ异常， cpu跳转至linux的irq中断异常向量表，处理完毕后，再依次返回到ATF—返回到optee <img src="https://img-blog.csdnimg.cn/20200702112945962.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

###### 4、当cpu处于REE，来了一个安全中断

当cpu处于normal侧时，来了一个安全中断，根据SCR.NS=0/中断在group1组，cpu interface将会给cpu一个FIQ，(由于SCR.FIQ=1，FIQ将被routing到EL3),在EL3(ATF)中，判断该中断是需要optee来处理的，会切换到optee。 此时SCR.NS的状态发生变化，根据SCR.NS=0/中断在secure group1组，cpu interface会再给cpu发送一个IRQ异常,cpu跳转至optee的irq中断异常向量表， 处理完毕后再依次返回到ATF—返回到linux <img src="https://img-blog.csdnimg.cn/20200702112804594.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzNTA4Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

###### 答疑

 

##### 推荐
-  --博客专栏-  --大课程-  --入门课程