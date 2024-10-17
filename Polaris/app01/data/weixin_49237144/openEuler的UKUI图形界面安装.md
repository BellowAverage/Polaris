
--- 
title:  openEuler的UKUI图形界面安装 
tags: []
categories: [] 

---
## openEuler的UKUI图形界面安装

Hello小伙伴们，你们好啊~~ 又是日常get新技能的一天， 今天，咱们来整理一下如何使用VMware Workstation上进行openEuler操作系统的安装， 0基础入门，趁着热乎，快上车啦~~GOGOGO。

（1）UKUI的安装 目前 UKUI 可以通过在终端上直接输入 yum install ukui 进行安装。

<img src="https://img-blog.csdnimg.cn/20210612150047432.png#pic_center" alt="在这里插入图片描述">

一直y回车就行了 <img src="https://img-blog.csdnimg.cn/20210612150511144.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

一直y回车就行了 <img src="https://img-blog.csdnimg.cn/20210612150556383.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

显示如下图则下载成功 <img src="https://img-blog.csdnimg.cn/20210612150645554.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

（2）然后安装字体库 yum groupinstall fonts <img src="https://img-blog.csdnimg.cn/20210612150742917.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 显示如下图则下载成功 <img src="https://img-blog.csdnimg.cn/20210612150847567.png#pic_center" alt="在这里插入图片描述">

（3）在确认正确安装后，输入systemctl设置默认图形开机 systemctl set-default graphical.target <img src="https://img-blog.csdnimg.cn/20210612150933139.png#pic_center" alt="在这里插入图片描述">

（4）重启之后即可看到图形界面。 reboot <img src="https://img-blog.csdnimg.cn/2021061215103460.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> （5）Vmware Tools 的安装 在虚拟机上找到我的计算机，然后右键虚拟机选择安装Vmware Tools，进入虚拟机双击计算机会看到Vmware Tools双击进去， <img src="https://img-blog.csdnimg.cn/20210612151917437.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

复制一份到其它任何地方，然后解压它，找到文件vmware-install.pl右键选择在终端运行（一直yes或者回车都行，一定要重启）。 <img src="https://img-blog.csdnimg.cn/20210612151952856.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 到这里我们的图像化界面就安装成功啦！
