
--- 
title:  网络工具之zenmap的安装和使用 
tags: []
categories: [] 

---
## 一、zenmap简介

  Zenmap是一个开源的网络扫描器，它是Nmap的图形用户界面（GUI）版本。Nmap是一个强大的网络扫描工具，用于发现网络上的主机、服务和开放端口。Zenmap通过提供一个直观的界面，使用户能够更容易地使用Nmap的功能。Zenmap提供了一些高级功能，如扫描配置文件管理、扫描配置文件导入和导出、扫描结果导出等。它还提供了一些可视化工具，如拓扑图和端口状态图，以帮助用户更好地理解扫描结果。Zenmap支持多种操作系统，包括Windows、Linux和Mac OS X。它是一个功能强大且易于使用的网络扫描工具，适用于网络管理员、安全专家和普通用户。环境说明：
- 操作系统：win7- zenmap版本：7.94- npcap版本：1.75
## 二、安装步骤

### 1、官网下载安装包

  访问nmap官网，下载对应操作系统环境下的软件包，当前最新稳定版是7.94，zenmap实际上就是nmap的图形化版本，所以安装包名还是nmap-7.94-setup.exe。 <img src="https://img-blog.csdnimg.cn/direct/2e01fbdbab05407ea10fdd9be84e944a.png" alt="在这里插入图片描述">

### 2、双机启动安装

<img src="https://img-blog.csdnimg.cn/direct/6d5a533642734794ba6196d99ed0f708.png" alt="在这里插入图片描述">

### 3、点击下一步直到安装完成

  window环境下exe文件安装比较简单，一直点击下一步即可完成安装，在选择组件这一步的时候我们可以看到安装nmap7.94的时候会安装依赖npcap，zenmap实际上就是nmap加上GUI组件。这个安装过程中会弹窗安装npcap软件包，如果已安装1.75以上新版本则不需要，如果是安装的npcap1.3x等旧版本则会卸载旧版本安装新版本npcap。 <img src="https://img-blog.csdnimg.cn/direct/d28ab1cae90b4ce2a9034efffbc662cd.png" alt="在这里插入图片描述">

### 4、安装完成

  安装完成我们在桌面就可以看到该启动快捷方式图标啦。 <img src="https://img-blog.csdnimg.cn/direct/7e163f700cac4fb4879aae606f80e21a.png" alt="在这里插入图片描述">

## 三、使用简介

### 1、启动zenmap

  双机桌面快捷方式图标或者启动栏点击图标启动程序，如果就是启动的界面。 <img src="https://img-blog.csdnimg.cn/direct/b3ab1483acf74f15a011db8125ca039c.png" alt="在这里插入图片描述">

### 2、配置下拉列表

  Profile下拉列表是扫描的配置选项，默认是Intense scan。 <img src="https://img-blog.csdnimg.cn/direct/28972ca7fbb6435f8d8d4b927a12a47e.png" alt="在这里插入图片描述">

### 3、快速扫描

  在Target输入框中输入目标IP地址或者地址段，Profile下拉框中选择扫描方式，Command输入框就自动完成了命令生成，点击Scan就可以开始扫描。Nmap Output中显示的扫描日志记录，Ports/Hosts页签中显示的是open的端口和主机IP信息，Host Details是详细的端口信息，Scans页签中是扫描记录。左侧Hosts是扫描到的主机列表，Services是根据服务类型进行的分类展示。 <img src="https://img-blog.csdnimg.cn/direct/432728fa7911414f8d3d2a55005ffdef.png" alt="在这里插入图片描述">

### 4、根据Services分类展示

  分类展示可以根据不同服务占用的固定端口类型分类展示，比如ftp、ssh、telnet、mysql等等。 <img src="https://img-blog.csdnimg.cn/direct/a6e8f592789e41d1a227f2652b535841.png" alt="在这里插入图片描述">

### 5、过滤主机

  扫描的是网段的情况下，活跃主机可能比较多，我们可以通过过滤主机功能过滤我们需要了解的主机的扫描结果。 <img src="https://img-blog.csdnimg.cn/direct/0002b8ba756248379bd90bdb358cd33f.png" alt="在这里插入图片描述">

### 6、比较扫描结果报错

  比较扫描结果，需要选择两次扫描记录，选中完成后程序奔溃报错。 <img src="https://img-blog.csdnimg.cn/direct/0ceba594b9f34d7fbb8ce57afba99c15.png" alt="在这里插入图片描述">

### 7、新建扫描规则

  新建或者编辑扫描规则profile文件都奔溃报错。博主已经根据提示反馈给了dev@nmap.org。 <img src="https://img-blog.csdnimg.cn/direct/671d09e83b584519acbcf5b5049bfd19.png" alt="在这里插入图片描述">

### 8、保存扫描记录

  点击Scan菜单可以选择打开或者保存扫描文件，保存的扫描文件格式可以选择.nmap或者xml，也可以一次保存当前所有的扫描结果到一个目录，这个设计还是非常方便的。安全工程师可以保存不同日期的扫描结果，根据需要进行对比，可以发现需要注意防护的安全变化和漏洞。 <img src="https://img-blog.csdnimg.cn/direct/a8dc354558a74020bb7d2da4f29611bc.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/5d44928b485141b589fda6d231802b6e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/9873af485b2b4d4ea73bc21ce015135b.png" alt="在这里插入图片描述">

## 四、总结

  Zenmap是官方的Nmap安全扫描程序GUI。它是一个多平台（Linux、Windows、Mac OS X、BSD等）的免费开源应用程序，旨在使Nmap易于初学者使用，同时为经验丰富的Nmap用户提供高级功能。经常使用的扫描可以保存为配置文件，以便重复运行。命令创建者允许交互式创建Nmap命令行。扫描结果可以保存并在以后查看。保存的扫描结果可以相互比较，以了解它们的差异。最近扫描的结果存储在可搜索的数据库中。Zenmap在windows环境下运行并不太稳定，尤其是扫描结果比较和新建扫描规则配置文件，博主在实验的时候选择之后就程序就奔溃了。
