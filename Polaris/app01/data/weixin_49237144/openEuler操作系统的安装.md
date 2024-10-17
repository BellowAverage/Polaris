
--- 
title:  openEuler操作系统的安装 
tags: []
categories: [] 

---
## VMware Workstation上进行openEuler操作系统的安装

Hello小伙伴们，你们好啊~~ 又是日常get新技能的一天， 今天，咱们来整理一下如何使用VMware Workstation上进行openEuler操作系统的安装， 0基础入门，趁着热乎，快上车啦~~GOGOGO。

openEuler官方简介：openEuler是一款开源操作系统。当前openEuler内核源于Linux，支持鲲鹏及其它多种处理器，能够充分释放计算芯片的潜能，是由全球开源贡献者构建的高效、稳定、安全的开源操作系统，适用于数据库、大数据、云计算、人工智能等应用场景。 openEuler版本号计数规则由openEuler x.x变更为以年月为版本号，以便用户了解版本发布时间，例如openEuler 20.03表示发布时间为2020年3月。

### （1）openEuler镜像的下载

本作者电脑window10采用的是x86_64架构,读者可以选择相对应的架构。 如果是ARM架构的CPU就选择相对应的aarch64即可。 搜索：华为openEuler，点击： <img src="https://img-blog.csdnimg.cn/20210706133655121.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210706133718447.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2021070613372830.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210706133748112.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210706133800737.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210706133814109.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

|openEuler-20.03-LTS-SP1-x86_64-dvd.iso|x86_64 架构的基础安装 ISO，包含了运行最小系统的核心组件
|------
|openEuler-20.03-LTS-SP1-everything-x86_64-dvd.iso|x86_64 架构的全量安装 ISO，包含了运行完整系统所需的全部组件
|openEuler-20.03-LTS-SP1-debuginfo-x86_64-dvd.iso|x86_64 架构下 openEuler 的调试 ISO，包含了调试所需的符号表信息
|openEuler-20.03-LTS-SP1-netinst-x86_64-dvd.iso|x86_64 架构下 openEuler 的小型化 ISO，支持网络模式下的系统安装
|openEuler-20.03-LTS-SP1-source-dvd.iso|openEuler 源码 ISO

### （2）openEuler的安装

##### 2.1 点击创建新的虚拟机，选择自定义（多了虚拟内存、处理器、网络类型等等），选择下一步用于服务器的话选择ESXi版本，个人PC的话选择最高版本（兼容性好）

<img src="https://img-blog.csdnimg.cn/20210612143153986.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

##### 2.2 选择稍后安装操作系统，选择其他Linux4.x或更高版本内核64位

<img src="https://img-blog.csdnimg.cn/20210612143300141.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

##### 2.3 给虚拟机命名并指定存放路径，处理器数量与内核数是1：2

<img src="https://img-blog.csdnimg.cn/20210612143449318.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

##### 2.4 选择4G内存（根据自身情况而定，不是越多越好的），使用NAT模式（三种网络连接模式的区别）

<img src="https://img-blog.csdnimg.cn/20210612143638203.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

##### 2.5 默认下一步

<img src="https://img-blog.csdnimg.cn/20210612144100240.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

##### 2.6 选择创建新虚拟磁盘，最少给8G以上，这里我给了60G，下一步，点击完成。

<img src="https://img-blog.csdnimg.cn/20210612144302955.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

##### 2.7 编辑虚拟机设置，CD\DVD使用ISO镜像文件，点击确定

<img src="https://img-blog.csdnimg.cn/20210612144539165.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

##### 2.8 选择第一项： Install openeuler 20.03-LTS，按下回车键进行安装，第二项：是检查ISO的完整性并安装，耗时大。第三项：Test media 是用来进行文件完整性,防止 ISO 文件内容的缺失。通常情况下，选择第一项安装即可。

<img src="https://img-blog.csdnimg.cn/20210612144700347.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

**提示：** 然后进入安装信息摘要界面，针对 OS 环境进行一些配置： **本地化：** 语言代表着安装完成后的 OS 语言环境；时间和日期代表着时区，默认是上海。 **软件：** 安装源代表着光驱内的我们下载的 ISO 镜像，可以作为 自动安装介质使用；软件选择代表着当前环境附加的功能，一般我们选择默认的 最小安装，来保证拥有基本的核心功能。 **系统：** 安装位置代表着 openEuler 的安装磁盘对应位置，确认好磁盘，点击 完成将 自动分区；网络和主机名代表着网络的连接，我们需要确保以太网处于连接状态。

##### 2.9 选择语言，仅限安装过程，设置安装目的地和根密码，安装目的地有自动跟自定义，一般自定义。安装信息确认后，我们点击开始安装，可以看到 openEuler 的安装进度。

<img src="https://img-blog.csdnimg.cn/20210612144923131.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80OTIzNzE0NA==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

##### 到这就安装成功啦！

#### openEuler的UKUI图像化界面的安装



#### openEuler官方镜像：



#### openEuler官方文档：


