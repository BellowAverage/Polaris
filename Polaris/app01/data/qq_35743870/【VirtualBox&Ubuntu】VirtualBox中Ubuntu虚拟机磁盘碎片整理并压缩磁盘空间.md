
--- 
title:  【VirtualBox&Ubuntu】VirtualBox中Ubuntu虚拟机磁盘碎片整理并压缩磁盘空间 
tags: []
categories: [] 

---
>  
 在Oracle VM VirtualBox中，相信大部分人都会使用**动态分配存储空间大小**的方式配置虚拟机，但这种方式带来的一个问题就是，**只会自动动态的增大，而不会自动动态的减少**，即，随着虚拟机的使用越来越久或者虚拟机中安装的软件越来越多，VirtualBox软件会自动分配相应的存储空间到虚拟机，此时会发现，我们明明在虚拟机卸载了软件或者删除了大量无效文件，按理说该虚拟机占用本机存储空间应该会有所降低，也即，原本vdi文件占用30G，虚拟机中删了10G，vdi文件占用应该变为20G，**可VirtualBox软件本身并不会自动减少这部分存储空间的大小**，即仍然是30G，只不过你后续使用过程中只有超过30G后VirtualBox软件才会再分配新的存储空间。**如果需要回收已分配中未使用的存储空间，这里介绍一种简便的方法进行手动回收这部分空间。** 


<img src="https://img-blog.csdnimg.cn/5dbd3b0640bf4c069235ec9ea65d126e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="Oracle VM VirtualBox中" width="680">

##### 第一步：VirtualBox中虚拟机进行磁盘碎片整理

>  
 磁盘碎片整理是为了确保虚拟机中已使用的空间都是连续的，这更有利于能尽可能地压缩磁盘存储空间大小。 


**Ubuntu虚拟机磁盘碎片整理**

###### 1、确认当前磁盘的分区情况（重点在挂载点）

在进行磁盘碎片整理前，需要**确认当前磁盘的分区情况（重点在挂载点）**，压缩磁盘占用空间大小主要对当前磁盘中使用频繁或者占用存储空间较大的**挂载点**有明显的效果，例如：`/`，`/usr`或者`/usr/local`，`/home`，以及使用较多的自定义挂载目录。如果不了解自己的虚拟机磁盘分区情况，可以使用下面的命令进行查看：

```
$ df -h

```

<img src="https://img-blog.csdnimg.cn/4b41f010e9a148b78770754764e3b58c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="查看磁盘使用情况" width="680">

>  
 主要看`文件系统`栏中为`/dev/sdaN`的分区的挂载点，找到三个主要挂载点（这里的其它挂载点均为Linux系统自动挂载的），即：`/`，`/usr`，`/home`，所以这三个挂载点是下面进行磁盘碎片整理的目录 


这里的磁盘分区因人而异，有的只有`/`根目录和`linux-swap`交换空间。因此，**有就整理，没有就无需整理**，因为`/`根分区已经囊括了，而**独立分区出去的就需要单独整理**。

>  
 除了分配大小少于1G或2G的`/boot`,`/var`以及`linux-swap`这些分区没有必要进行磁盘整理外，其他的尽可能都进行磁盘碎片整理【主要的还是这些分区：`/`，`/usr`或者`/usr/local`，`/home`，以及使用较多的自定义分区】。 


这里介绍一种查看磁盘的分区情况的软件–**GParted分区编辑器：** 详细安装过程可查看博文： 下面提供安装命令：

```
$ sudo apt-get update
$ sudo apt-get install gparted

```

搜索GParted启动或者使用命令进行启动，命令如下：

```
$ sudo gparted

```

<img src="https://img-blog.csdnimg.cn/a21ce9f20cb045a590d3b6e0846232c4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="启动GParted" width="680">

>  
 由上图看出，该虚拟机中磁盘分区由三个分区(**挂载点**)使用占比较大，即：`/`，`/usr`，`/home`。 


**2、磁盘碎片整理** 下面是笔者在虚拟机中放置了两个大文件（共约4G），并移动了几次文件的位置后的虚拟机实际分配的空间，可以看到实际分配的空间已经由原来的16.70G增长到25.01G，增长了8.31G，说明虚拟机并不是按实际使用大小进行分配，会多分配一些。 <img src="https://img-blog.csdnimg.cn/a323637893674d028df667c149e2f80e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="压缩前" width="680">

>  
 这里把新增的两个大文件删除，模拟**删除大量文件并清空回收站**或者**卸载软件**后的情况。 


各挂载点的碎片整理命令如下，至于需要执行哪些命令，看上面： `/`

```
$ sudo dd if=/dev/zero of=/EMPTY bs=1M 
$ sudo rm -f /EMPTY

```

`/home`

```
$ sudo dd if=/dev/zero of=/home/EMPTY bs=1M 
$ sudo rm -f /home/EMPTY

```

`/usr`

```
$ sudo dd if=/dev/zero of=/usr/EMPTY bs=1M 
$ sudo rm -f /usr/EMPTY

```

`/自定义或其它挂载点`

```
$ sudo dd if=/dev/zero of=/改为自定义或其它挂载点/EMPTY bs=1M 
$ sudo rm -f /改为自定义或其它挂载点/EMPTY

```

###### 下面为执行的详细过程：

###### 碎片整理开始后：

>  
 碎片整理开始后会处于等待空白等待状态，此时已经开始运行的了，**碎片整理是可以同时进行的**，担心出问题的话可以单独进行碎片整理。若需要查看整理过程，可打开**新的终端执行**下面的命令，然后在执行碎片整理的终端就会输出内容： $ `sudo watch -n 5 pkill -USR1 -x dd` 这里整理的时长与磁盘各挂载点的磁盘分配空间大小有关，分配空间越大，耗时越久。 


<img src="https://img-blog.csdnimg.cn/aca6d602e34047b7baf34a17b956b193.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16" alt="碎片整理开始时">

###### 碎片整理结束后：

>  
 碎片整理结束时有的会**提示空间不足**，选择`忽略`即可，终端输出的出错信息也无需关注，**此时一定要把生成的文件删了再关虚拟机** 


<img src="https://img-blog.csdnimg.cn/3f890fe9a6bd4e9892ffb141e11b97f8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 删除各碎片整理生成的文件：

>  
 这里一定一定一定要删除碎片整理生成的所有指定文件，【下图中没在对应终端删除，但也不是不能删除是吧，小失误，删除了即可 ^^】，所有都删除后即可关闭虚拟机 


<img src="https://img-blog.csdnimg.cn/4a81bdd980d44556b60309f906bae1ad.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16" alt="删除碎片整理生成的空文件">

##### 第二步：VirtualBox中压缩虚拟硬盘的磁盘空间

###### 1、找到虚拟机的虚拟硬盘所在位置

>  
 关闭虚拟机后点击`设置`－＞`存储`－&gt;点击需要压缩磁盘空间的虚拟硬盘（例如这里的`Ubuntu16.04.vdi`）－&gt;找到`属性`中的`位置`。 【**注：如果有多个虚拟硬盘，则需要分别对这些虚拟硬盘进行压缩操作。**】 这里发现磁盘分配的空间大小又有所增长，但增长的不是很多，问题不大 


<img src="https://img-blog.csdnimg.cn/dce8f09960024ecd9a3e3be108c09c88.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="找到虚拟机的虚拟硬盘所在位置" width="680">

>  
 这里的vdi所在目录（根据自己的而定，在属性`位置`那里一键复制即可）： `D:\PortableApps\VirtualBox VMS\Ubuntu16.04\Ubuntu16.04.vdi` 


###### 2、在命令提示符[cmd]执行压缩操作（已优化）

`以管理员身份运行命令提示符[cmd]`，在终端输入以下命令：

```
#1、进入Oracle VM VirtualBox软件的运行程序所在目录
cd/d D:\Program Files\Oracle VM VirtualBox
#2、将""中的路径改为上面的《1、找到虚拟机的虚拟硬盘所在位置》的自己的虚拟硬盘vdi的完整路径
VBoxManage modifyhd "D:\PortableApps\VirtualBox VMS\Ubuntu16.04\Ubuntu16.04.vdi" –compact

```

建议使用下面的模板在记事本里编辑好了再一键复制到cmd中右键即可粘贴执行 其中`cd/d`为cmd命令，与盘符无关

```
cd/d xxxVirtualBox软件目录
VBoxManage modifyhd "虚拟硬盘vdi的完整路径" –compact

```

**下面是详细操作过程：** **以管理员身份运行命令提示符** win10的话搜索cmd即可找到命令提示符，注意最好是**以管理员身份运行**。命令提示符怕找不到的话，建议把它`固定到开始屏幕` <img src="https://img-blog.csdnimg.cn/756c918b2d084afda54314885e0d42ab.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="查找cmd" width="680"> **如果不知道Oracle VM VirtualBox软件的运行程序所在目录，可通过下面的方法查看** <img src="https://img-blog.csdnimg.cn/e7ff97138cf7403199e7cbe7b1eca669.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="查找VirtualBox软件的位置" width="680"> **编辑命令**（以下两个命令均可用，推荐使用优化后的） <img src="https://img-blog.csdnimg.cn/2715c72ff1304f1d8ed8b939a8d97431.png" alt="编辑命令"> 以下是优化后的命令，其中`cd/d`为cmd命令，与盘符无关 <img src="https://img-blog.csdnimg.cn/630cebb505d94d399fd0becf1871267f.png" alt="编辑命令2">

**执行命令【复制命令，在cmd中右键粘贴即可】** <img src="https://img-blog.csdnimg.cn/cfe7e5ef7420494ba90fb9ab1591b381.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16" alt="执行命令">

>  
 等待压缩到100%即可，返回VirtualBox软件中查看压缩后的大小，需要注意的是，这里的压缩并非所有情况下都会带来减少分配空间的大小，个别情况下会出现比原来多的情况。但是如果是删除了大量文件后再压缩，还是会有所减少的。 


<img src="https://img-blog.csdnimg.cn/f1ef8e06168748daa9454df45ede2e22.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="压缩后" width="680">

>  
 可以发现压缩后，减少到了16.83G，至于为什么相比原本的16.70G多了那么一点，那个咱也不懂，反正减少了，哈哈。【如果有懂的小伙伴欢迎在下方评论区留言】 


**好了，到这里就结束了，最后提醒一下，别看这篇文章很长，这里因为需要介绍所以会偏长，但对于同一个虚拟机的命令其实都是一样的而且不多，大家可以按照下面的保存好自己的命令，下次使用起来就很方便啦。**

```
#虚拟机压缩内存
sudo dd if=/dev/zero of=/EMPTY bs=1M 
sudo rm -f /EMPTY

sudo dd if=/dev/zero of=/home/EMPTY bs=1M
sudo rm -f /home/EMPTY

sudo dd if=/dev/zero of=/usr/EMPTY bs=1M
sudo rm -f /usr/EMPTY

【sudo watch -n 5 pkill -USR1 -x dd】查看dd进度，一般无需执行

cd/d D:\Program Files\Oracle VM VirtualBox
VBoxManage modifyhd "D:\PortableApps\VirtualBox VMS\Ubuntu16.04\Ubuntu16.04.vdi" –compact

```

**大家多多支持，有什么不足之处，欢迎大家在下方留言讨论！**
