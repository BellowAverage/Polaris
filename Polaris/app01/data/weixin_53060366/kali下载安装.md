
--- 
title:  kali下载安装 
tags: []
categories: [] 

---
#### 一、前期准备

：http://mirrors.ustc.edu.cn/kali-images/

<img src="https://img-blog.csdnimg.cn/02c8ccf3c2f844b89ea074314c6bcafa.png" alt="在这里插入图片描述">

#### 二、VMware虚拟机配置

**1、打开vmware，点击创建新的虚拟机** <img src="https://img-blog.csdnimg.cn/6612e41eebde4374bfb342e69d88ddad.png" alt="在这里插入图片描述"> **2、选择自定义(高级)选项，点击下一步** <img src="https://img-blog.csdnimg.cn/29199033f9774631b5621218bb029c5d.png" alt="在这里插入图片描述"> **3、继续下一步** <img src="https://img-blog.csdnimg.cn/2418d1d46c8d4648b776b2d2253bb4e3.png" alt="在这里插入图片描述"> **4、选择【稍后安装操作系统】，然后点击下一步** <img src="https://img-blog.csdnimg.cn/9be04a1bc437457392128b5e553f9f41.png" alt="在这里插入图片描述"> **5、客户机操作系统选择【Linux】，版本选择【Debian】，至于64位还是32位我们根据镜像选择对应的版本，当然也可以直接选择64位，毕竟可以向下兼容。其次之所以选的Debian是因为Kali Linux是基于Debian的Linux发行版，所以我们选择Debian，选择完成之后继续点击下一步** <img src="https://img-blog.csdnimg.cn/2b71e6311ed9453297a32f5e617136e6.png" alt="在这里插入图片描述"> **6、命名虚拟机：关于虚拟机名称可根据自己喜好去改。位置选择C盘以外最好。完成之后点击下一步** <img src="https://img-blog.csdnimg.cn/4a9bb3c5f678478dac859653658e992b.png" alt="在这里插入图片描述"> **7、处理器配置：根据自己的需求以及电脑的硬件限制合理进行配置，这里处理器数量和每个处理器的内核数量我都给的2个，也就是处理器内核总数给了4个。完成之后继续点击下一步** <img src="https://img-blog.csdnimg.cn/f6c563427c6146919ab210c59affed29.png" alt="在这里插入图片描述"> **8、虚拟机的内存：这里同样根据自己的需求进行分配。然后点击下一步** <img src="https://img-blog.csdnimg.cn/ea79ef987d654d86bb61e480beca3bb5.png" alt="在这里插入图片描述"> **9、网络类型：这里先选择第二项【使用网络地址转换(NAT)】，后期也可以更改，然后点击下一步** <img src="https://img-blog.csdnimg.cn/5f602b62bca44350a349fb90dbca386f.png" alt="在这里插入图片描述"> **10、默认点击下一步** <img src="https://img-blog.csdnimg.cn/9af412bfbb654d3680e8cab406c6dcf4.png" alt="在这里插入图片描述"> **11、继续点击下一步** <img src="https://img-blog.csdnimg.cn/32b88cae2b294af08d71bef64c945d23.png" alt="在这里插入图片描述"> **12、选择磁盘：这里选择创建新的虚拟磁盘，然后点击下一步** <img src="https://img-blog.csdnimg.cn/9d77be559b0e4e349c8ec718be3a4b7b.png" alt="在这里插入图片描述"> **13、指定磁盘容量：同样这里根据自己的需求按需分配，分配好之后选择最下面一项【将虚拟磁盘拆分成多个文件】，然后下一步** <img src="https://img-blog.csdnimg.cn/01717a6c975b4d389c5adadd9e47a645.png" alt="在这里插入图片描述"> **14、默认点击下一步** <img src="https://img-blog.csdnimg.cn/b59897b77e314667bb7ad9371342cf78.png" alt="在这里插入图片描述"> **15、点击自定义硬件** <img src="https://img-blog.csdnimg.cn/8c4bf4a5d73f4926a36327c146c15ccb.png" alt="在这里插入图片描述"> **16、在硬件里先选择左边的【CD/DVD(IDE)】，然后点击使用ISO映像文件，选择浏览，然后选择提前下载好的ISO镜像文件，然后点击关闭** <img src="https://img-blog.csdnimg.cn/75815f22a7ca4e50ae01b6f845ecba55.png" alt="在这里插入图片描述"> **17、然后点击完成** <img src="https://img-blog.csdnimg.cn/04fbc41c9b384709990746d94b0fe934.png" alt="在这里插入图片描述">

#### 三、这时虚拟机配置完成了，接下来就可以直接安装Kali操作系统

**1、先点击【开启此虚拟机】** <img src="https://img-blog.csdnimg.cn/f758157dc3c54c91b89bb79841f66b21.png" alt="在这里插入图片描述">**2、点击【我已经完成安装】，将底下的黄色栏框消除** <img src="https://img-blog.csdnimg.cn/c4ca4628c4db4d06b34318a937408038.png" alt="在这里插入图片描述"> **3、选择Graphical install(图形化安装)** <img src="https://img-blog.csdnimg.cn/ba04836e2fa94fe297059c29ad92aee3.png" alt="在这里插入图片描述"> **4、选择【Chinese(Simplified)-中文(简体)】，然后点击Continue** <img src="https://img-blog.csdnimg.cn/743c1c3e83f14ac68cef346cc63dfcfa.png" alt="在这里插入图片描述"> **5、选择中国然后继续** <img src="https://img-blog.csdnimg.cn/7ac92e241d5045f5993d5f8f016b5560.png" alt="在这里插入图片描述"> **6、选择语言然后继续** <img src="https://img-blog.csdnimg.cn/310a99b319154b99baae5667521abac8.png" alt="在这里插入图片描述"> **7、稍等片刻** <img src="https://img-blog.csdnimg.cn/935c9fb9b7c24aedbeac76d5905ccce3.png" alt="在这里插入图片描述"> **8、【配置网络】这里输入一个主机名，然后继续** <img src="https://img-blog.csdnimg.cn/1854bb5d32474686853796c18991ee2b.png" alt="在这里插入图片描述"> **9、【设置用户名和密码】这里输入一个普通用户账号的用户名，然后继续** <img src="https://img-blog.csdnimg.cn/c8dcc3eee2534441a0bb4e1581677f1b.png" alt="在这里插入图片描述"> **10、【设置用户名和密码】这里输入一个账号的用户名，并且记住该用户名，然后继续** <img src="https://img-blog.csdnimg.cn/daff958eec44472f99f4db3e7dd47cfa.png" alt="在这里插入图片描述"> **11、【设置用户名和密码】这里为刚刚的用户设置一个密码，然后继续** <img src="https://img-blog.csdnimg.cn/f0c3dc8eb860493aa153461d74b779f1.png" alt="在这里插入图片描述"> **12、【磁盘分区】这里选择【向导-使用整个磁盘】，然后继续** <img src="https://img-blog.csdnimg.cn/8a8aadb78be1457db964e9c6d4abea1a.png" alt="在这里插入图片描述"> **13、【磁盘分区】这一步保持默认继续就行** <img src="https://img-blog.csdnimg.cn/6883971f519d40a2be27309c8eaee93d.png" alt="在这里插入图片描述"> **14、【对磁盘进行分区】这里分区方案选择推荐的第一个【将所有文件放在同一个分区中(推荐新手使用)】，然后继续** <img src="https://img-blog.csdnimg.cn/995aeb33e3064074af94fbe1f88f4e9b.png" alt="在这里插入图片描述"> **15、【对磁盘进行分区】这里我们选择【结束分区设定并将修改写入磁盘】这个选项，然后点击继续** <img src="https://img-blog.csdnimg.cn/3f3d001302bc468fa7f76bf69f3b631d.png" alt="在这里插入图片描述"> **16、【对磁盘进行分区】这里我们选【是】然后继续** <img src="https://img-blog.csdnimg.cn/0d37419629a44702b8f5972d7d97a1fb.png" alt="在这里插入图片描述"> **17、这里保持默认，直接点击继续** <img src="https://img-blog.csdnimg.cn/596cfc0dbf8143aa89bd5a0990d9b6d9.png" alt="在这里插入图片描述"> **18、耐心等待，时间会有点儿长** <img src="https://img-blog.csdnimg.cn/156a642aeede4a7c9b923f4a4eaaaf97.png" alt="在这里插入图片描述"> **19、安装GRUB启动引导器】选【是】然后点击继续** <img src="https://img-blog.csdnimg.cn/a06ca259f765439e8b5433d5196ed8f6.png" alt="在这里插入图片描述"> **20、【安装GRUB启动引导器】这里一定得选择/dev/sda，然后继续** <img src="https://img-blog.csdnimg.cn/68b5ef77a9b7427689413a2adee82893.png" alt="在这里插入图片描述"> **21、安装完成，点击继续** <img src="https://img-blog.csdnimg.cn/1e1ac6772e4b43ada0eb575dc8de251d.png" alt="在这里插入图片描述">

#### 四、进入Kali系统

**1、输入刚刚的用户名和密码点击登录就可以进入到桌面** <img src="https://img-blog.csdnimg.cn/e636711ba9884964a1dc3b6527298bea.png" alt="在这里插入图片描述"> **2、进入到桌面，即可使用Kali** <img src="https://img-blog.csdnimg.cn/c6b9272af068482fb773aaad27368c00.png" alt="在这里插入图片描述">

#### 五、添加root用户及密码

**1、打开终端，在里面输入【sudo -i】这个命令**
- 1
<img src="https://img-blog.csdnimg.cn/4d67f469fb5c4e9090cb15daa3d45e4a.png" alt="在这里插入图片描述"> **2、输入登录用户的登录密码，然后回车，紧接着输入【passwd root】这个命令**
- 1
<img src="https://img-blog.csdnimg.cn/4221a68ce6bf414d92b888e1f673e023.png" alt="在这里插入图片描述"> **3、然后输入新的root密码，接着回车，注意的是输入的密码不会显示。然后再重新输入新的root密码，然后回车就可以将root用户的密码给修改了** <img src="https://img-blog.csdnimg.cn/ce000f3053694fe982f890e098496b61.png" alt="在这里插入图片描述"> **4、重新启动** <img src="https://img-blog.csdnimg.cn/a19934f929ed4a8987bf126b09388b92.png" alt="在这里插入图片描述"> **5、输入用户名root，以及密码，就可以使用超级管理员身份进入到系统中** <img src="https://img-blog.csdnimg.cn/3a1dce48a1eb42309fa028781182e33d.png" alt="在这里插入图片描述">

#### 六、设置快照

**1、先关闭虚拟机，然后在该虚拟机的启动前界面上点击下图一个类似表下面有个扳手一样的图标，点击它** <img src="https://img-blog.csdnimg.cn/cb3d04d9dd0e4c83b9e5ee6f58c6dc26.png" alt="在这里插入图片描述"> **2、先选择当前位置，再点击拍摄快照** <img src="https://img-blog.csdnimg.cn/0c47b557c8f742c6a83be6fbe28d001a.png" alt="在这里插入图片描述"> **3、然后填入快照名称以及描述，这里需要强调一下描述里面建议写上该系统的用户名和密码，以防止后期遗忘。填写完成后点击拍摄快照，这样快照就设置好了** <img src="https://img-blog.csdnimg.cn/b59b2fda1dfc41d49130dc67b88f113c.png" alt="在这里插入图片描述"> **4、当你想要返回到之前的某个状态的时候，只需要选择需要回到的状态，然后点击转到，然后确认是就可以恢复到之前所保存的某一个状态点上了** <img src="https://img-blog.csdnimg.cn/1b33f3f281e64ef196f9b04499c759d5.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/015d490018bb449681dfcd42d592394e.png" alt="在这里插入图片描述"> 这样的好处是，避免后期系统出现问题需要重新再安装，省去了重装系统的步骤以及时间。

#### 七、apt 更新及操作

<img src="https://img-blog.csdnimg.cn/dfa37ebaebf44661843dd1f5b637f3ad.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/106cac35921d4eb8ad8abfa84d921aa8.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/8d572151c7004d7fb86de801103dc240.png" alt="在这里插入图片描述"> **进入超级管理员用户：** <img src="https://img-blog.csdnimg.cn/fce597e6dd8e4d72a63bf251f6922b8e.png" alt="在这里插入图片描述">
- 1
<img src="https://img-blog.csdnimg.cn/858a834064964fd68a16dcb60561ff2f.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/404116c91d6a4bfbba069f49a4a9281a.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/b505e76dc68c4034b6898bb9354d1e5e.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/1629735600324d0d987e657a21ffa617.png" alt="在这里插入图片描述">

#### 八、更改kali的源仓库

**因为kali官方源是国外的会比较慢；此处建议改用的是清华源**

>  
   deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-freedeb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free 
  
- 1
<img src="https://img-blog.csdnimg.cn/7eaec62a57784472bbaa9e2d7f93ca15.png" alt="在这里插入图片描述">

#### 九、kali Linux的文件如何共享到物理机

**1、在物理机建立一个共享文件夹** <img src="https://img-blog.csdnimg.cn/9af1e4463cd04a88882d46e562cf13d0.png" alt="在这里插入图片描述"> 2、启动kali系统，打开 菜单栏中 —虚拟机----设置----选项---- <img src="https://img-blog.csdnimg.cn/90b1912d6e4d453795a7ad1ee212808c.png" alt="在这里插入图片描述"> **3、选择共享的路径** <img src="https://img-blog.csdnimg.cn/635d333d57b14d128a36625b7dd5ea0f.png" alt="在这里插入图片描述"> **4、 启用此共享** <img src="https://img-blog.csdnimg.cn/546774ff080249d5b88bff460ca2cdc9.png" alt="在这里插入图片描述"> **5、然后可以在kali系统中验证有此文件** <img src="https://img-blog.csdnimg.cn/523c5ed17b1c45999093c368fbc58bcf.png" alt="在这里插入图片描述"> **6、vmware中/mnt/hgfs目录下没有share共享文件夹的解决办法**
