
--- 
title:  python卸载方法(教你一招干干净净卸载Python 
tags: []
categories: [] 

---
是认真的。我们在写怎么从hello world开始你的python之旅，本篇是说卸载python安装版，不是放弃python哦。

**为什么要卸载**

有的版本太旧。python3一改python2的旧习，成了名副其实的“版本帝”。
-  原有的python版本，能在现有基础上升级吗？ -  本地计算机装了python版本，配置了PATH环境。 -  又装了anaconda用于数据分析，两者有冲突吗，不想删除本地的python怎么办？ -  使用无数多个env创建了虚拟环境，有的要用3.7，有的要用3.5，管理起来很抓狂！ 
**按照步骤操作**

此文将教您如何从计算机中删除Python应用程序及其相关文件和文件夹。

您可以在Windows和Mac计算机上执行此操作。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/929f4361116308f916151ad3ff30e206.jpeg">



打开开始菜单。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/46b0bbac5550150b48baba95aa92bdc8.jpeg">



单击“开始”菜单左下角的“设置”图标。这将调出设置窗口。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/f407b8dcc89b0ebcdec8c79bb8b5b7d3.jpeg">



找出你想要卸载的python版本。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/05e04a9824c72f1af468719f341b461c.jpeg">



点击“Uninstall卸载”按钮并确定。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/18694db67650677b5126509ebce36c86.jpeg">



很大可能它会问一下你，确定卸载吗？非常确定。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/95b5bd36e1111b9bffe26bc98e888f2c.jpeg">



卸载有进度条。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/7a2e2a7d7a6a0273558d5bb620851ac9.jpeg">



还有一个python launcher也不能放过。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/83efb0eed3e6be114acb351e6616ef8d.jpeg">



到这儿，基本上python就从眼前消失了。

删除Python 2文件夹

虽然卸载Python 3会从您的计算机上删除Python 3文件夹，但即使您卸载了Python 2的程序，Python 2文件夹也会保留下来。要删除该文件夹，请执行以下操作：
-  打开这台电脑。 -  在“Devices and Drives(设备和驱动器)”部分双击您的硬盘。 -  在文件夹列表中找到“Python27”(或类似的)文件夹。 -  选择Python文件夹，然后右键单击它以提示下拉菜单。 -  单击下拉菜单中的删除。 
<img alt="" src="https://img-blog.csdnimg.cn/img_convert/6de54d5147dd3bbf13d802b2e7887e13.jpeg">



Mac苹果笔记本怎么卸载

mac是基于BSD的古老UNIX系统延伸来的，卸载方式与windows不同。

步骤是，先找到python安装文件夹。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/9f2327dc09a19c8c813dab31055a2e3b.jpeg">



使用Finder把Python的目录找到。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/e246ca8f1721c4f9ea1442ddc372584f.jpeg">



输入Python安装文件夹的地址。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/5e6728d8b85d3ec7f185c30f6cfd7949.jpeg">



根据安装的Python版本，将在“转到文件夹”文本框中键入以下地址之一。

对于Python3.6和更高版本，在此处输入 /Library/Frameworks/Python.framework/versions。

对于Python2.7，在此处输入 /Library/Python/Versions或/Library/Python。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/0ff65711bd893f62fb725935e4f0e98f.jpeg">



选中要删除的文件夹，然后删除。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/ec29c90af358ef4ebf6d538e36a6374b.jpeg">



<img alt="" src="https://img-blog.csdnimg.cn/img_convert/93138a2f96f11deb21d0090aa994bd96.jpeg">



这得提示你输入密码，得确认权限。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/57617a9c7fd1aafd8383223a55736e1b.jpeg">

写在最后

现在Anaconda的生态发展的比较全面，数据研究，机器学习的包库很完备。

嫌Anaconda太大而全，可以尝试一个miniconda，精简版。
