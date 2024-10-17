
--- 
title:  【删库不跑路】—Linux系统自杀实验 rm -rf /* 及如何抢救和预防 
tags: []
categories: [] 

---
#### 事情是这样的

想必大家都听说过一个笑话：一个程序员去公司面试，面试官让他随便写个shell脚本看看

结果程序员在公司机器上写了个简单的 rm -rf  /* 

<img alt="" height="200" src="https://img-blog.csdnimg.cn/20210428220340487.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="231">

今天博主好奇到无聊，想看看到底会有什么效果呢。

就拿了一台不用的废弃虚拟机系统玩了一把。

在这里跟大家，汇报一下战果：

<img alt="" height="247" src="https://img-blog.csdnimg.cn/20210428220421874.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="227">

大家一定注意谨慎：玩完之后，绝大部分数据无法恢复，系统会基本完全崩溃状态，

建议在废弃的机器上玩可以，正式环境千万不要，另外大家写删除命令的时候，也一定要小心

#### Linux机器准备

首先找了台好久不用的虚拟机，回到根目录下，直接执行rm -rf * ；

<img alt="" height="213" src="https://img-blog.csdnimg.cn/2021042822053948.png" width="214">

然后就开始看到系统开始从根目录开始删除

开始报一些无法删除的错误

<img alt="" class="has" height="161" src="https://img-blog.csdn.net/20180908105540432?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="687">

因为一些正在运转的misc net等硬件文件 无法删除

当我们误操作的时候，发现这些rm： cannot remove...，就赶紧中止还有得救

#### 相关路径解读

boot：启动路径，部分文件，正在运行删不掉。

misc net：硬件相关运行中，不允许删除。

dev/shm：

`/dev`:目录下一般都是一些设备硬件文件，例如磁盘、内存、摄像头、网卡等等。`/dev/shm: `这个目录是linux下一个利用内存虚拟出来的一个目录，这个目录中的文件都是保存在内存中，而不是磁盘上。

其大小是非固定的，即不是预先分配好的内存来存储的。(shm == shared memory)

dev/pts/ptmx

ptmx 虚拟终端相关文件 系统不让删除

<img alt="" height="80" src="https://img-blog.csdnimg.cn/202104141643162.png" width="375">

**Linux终端：**

另外sys目录下的一些系统文件包括，

挂载的磁盘信息等，root也是没有权限删除的，

其余的文件夹 opt mnt home root等等 统统被删除  

<img alt="" class="has" height="454" src="https://img-blog.csdn.net/20180908105600766?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="770">

Linux挣扎了一下：sys/block的块设备不让删除、

nfs文件系统的缓存、挂载记录、锁等不让删除

#### rm -rf /* 运行完之后

删除完成之后，我们在根目录下看一下：

ls 命令已经没有了，这是因为存放命令的/bin目录下的所有二进制命令文件都被删除了，

包括 yum pwd 等等统统没有了，只有cd命令还在，

这是因为cd命令并不在/bin下

whereis cd :查看一下，cd在/usr/bin目录下

<img alt="" height="75" src="https://img-blog.csdnimg.cn/20210414165840145.png" width="630">

<img alt="" class="has" height="417" src="https://img-blog.csdn.net/20180908105634502?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="761">

可以看到根目录下 只剩下/boot的启动文件夹。

硬件相关的misc net dev

sys系统相关文件夹

这是给我们下次启动时 进行启动牵引，牵引到grub界面 之后，由

于系统中所有的东西都被我们删除了，所以就卡死在grub界面 无法进内核。

<img alt="" class="has" height="415" src="https://img-blog.csdn.net/20180908105705144?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="1076">



### 抢救及预防措施

这个命令是极其危险的，所以一旦误操作

#### 1、中止命令

首先，在意识到命令执行时，立即按Ctrl+C 终止命令。尽可能的保护系统文件。

#### 2、不要退出当前shell，不要重启

因为，我们不清楚，到底有哪些文件被删除了。

我们总会下意识的觉得，重启下就好了。这个时候千万不要重启，因为一重启，你可能无法再进入系统，连最后抢救的机会都没有了。

#### 3、系统文件夹迁移

系统根目录下，大体就是这几个文件夹。

<img alt="" height="124" src="https://img-blog.csdnimg.cn/20210428171438103.png" width="778">

像/bin /sbin :主要是存储一些命令的文件夹。如果被删除了，我们可以通过从其他的服务器，将/bin目录，压缩，拷到当前服务器解压，进行替换。

#### 4、系统快照

这是一个非常实用的方法。我们可以定时做系统快照，例如：每天凌晨2点，对系统做一个快照；也可以每逢比较重大的系统更新或者服务搭建之后，做一个快照。

这样，当我们误操作之后，就会有一个回退的备份。

#### 5、命令重写

可以将rm -rf 重写，构造一个回收站，可以参考博主的这篇博文：



###  推荐阅读

#### 【资源推荐】
-  <h4 id="%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%93%E7%94%A8%E7%B3%BB%E7%BB%9F">**渗透测试专用系统**</h4> - kali-linux-e17-2019.1a-amd64.iso系统镜像- - kali-linux-2018.4-amd64 操作系统- - manjaro-xfce-17.1.7-stable-x86_64.iso系统镜像- - WiFi专用渗透系统 nst-32-11992.x86_64.iso操作系统镜像- - Parrot-security-4.1_amd64.iso 操作系统镜像- - manjaro-xfce-17.1.7-stable-x86_64 操作系统- - cyborg-hawk-linux-v-1.1 操作系统- - <li> <h4 id="%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E7%9B%B8%E5%85%B3%E5%B7%A5%E5%85%B7">渗透测试相关工具</h4> - ****- 【kali常用工具】上网行为监控工具       - - 【kali常用工具】抓包工具Charles Windows64位 免费版- - 【kali常用工具】图印工具stamp.zip- - 【kali常用工具】brutecrack工具[WIFIPR中文版]及wpa/wpa2字典- - 【kali常用工具】EWSA 5.1.282-破包工具- - 【kali常用工具】Realtek 8812AU KALI网卡驱动及安装教程- - 【kali常用工具】无线信号搜索工具_kali更新- - 【kali常用工具】inssider信号测试软件_kali常用工具- - 【kali常用工具】MAC地址修改工具 保护终端不暴露- - 【kali常用工具】脚本管理工具 php和jsp页面 接收命令参数 在服务器端执行- 
#### 渗透测试相关工具


- **Java实现照片GPS定位【完整脚本】**- - **Python实现照片GPS定位【完整脚本】**- - **女神忘记相册密码 python20行代码打开【完整脚本】**- - ****- 
**python实战**
- ****- ****- **...**- ****- ****- ****
**【pygame开发实战开发30例 完整源码】**
- 
**【pygame游戏开发专栏，获取完整源码+教程】**
- ****- ****- ****- ****- ** **- ****
#### CSDN官方学习推荐 ↓ ↓ ↓
- **CSDN出的Python全栈知识图谱，太强了，推荐给大家！**
<img alt="" height="625" src="https://img-blog.csdnimg.cn/20210607120133619.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="351">


