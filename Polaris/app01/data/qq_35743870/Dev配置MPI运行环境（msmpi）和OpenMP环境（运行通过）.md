
--- 
title:  Dev配置MPI运行环境（msmpi）和OpenMP环境（运行通过） 
tags: []
categories: [] 

---


#### Dev Cpp配置MPI运行环境（msmpi）和OpenMP环境（运行通过）
- - <ul><li>- - - - - - <ul><li>- 


>  
 **软件包下载** **MSMPI(2个都需要安装)，Dev Cpp 5.11(含新版编译器，与教程相同目录下)**  `注意事项`：Dev软件好像不允许多版本共存，若使用提供的Dev，最好在原来的Dev的安装目录下执行uninstall.exe文件进行卸载原来的，否则在新的打开还是旧的，直接删除也会出现找不到原有编译器的情况。 <img src="https://img-blog.csdnimg.cn/direct/5d1a71cac55d444e90eeb2b78b410883.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_12,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述" width="250"> <img src="https://img-blog.csdnimg.cn/direct/c3227d432d0a42888d53802989b6cad2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_12,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述" width="250"> 


## 一、Dev Cpp配置新版本编译器

### 1、下载新版本编译器（若使用提供的软件包，可跳过）

Dev Cpp（这里是）自带的编译器版本太低，编译会出错，需要更换一个新版的MinGW编译器，可通过下面的链接下载，选择适合自己系统位数的下载即可（打开链接后需要等待几秒才可开始下载）。**下面主要介绍的是64位的** MinGW 8.1.0 seh 64-bit： MinGW 8.1.0 dwarf 32-bit： 自选版本请进入官网下载：-往下拉就可以看到各个版本

>  
 尽量不选择exe安装文件，安装慢，还有下载的压缩包如果没有bin是不可以的；x86_64表示64位，i686表示32位，posix表示Linux这类系统，win32表示Windows系统，sjlj或seh/dwarf自己选，一般选后者。 


### 2、解压到目录（若使用提供的软件包，可跳过）

解压前面下载的新编译器的压缩包到一个喜欢的目录下，这里是解压后复制到Dev Cpp的自带编译器目录下(` ..\\Dev-Cpp\MinGW64\`)，修改新编译器解压后得到的文件夹的名称（`mingw64-8.1.0`）**【也可不改，看个人】**。

### 3、给Dev Cpp配置新编译器

① 打开Dev Cpp软件，选择`工具`—&gt;`编译选项`，打开`编译器选项 `界面 <img src="https://img-blog.csdnimg.cn/f8c7cea260ee495db4a904f63aa87b62.png#pic_center" alt="打开编译器选项界面" width="200" height="130"> ② 点击左手边数起`第三个的"+"图标`（由文件夹添加编译器设置） <img src="https://img-blog.csdnimg.cn/d4ab7060ab5d45a0b587e5e96f7e967a.png#pic_center" alt="由文件夹添加编译器设置" width="400" height="70">

③ 选择上面新编译器文件解压后的文件夹且其下一级必须是bin目录的，这里挨着`bin`目录的是`mingw64-8.1.0`(注意：其下一级必须是`bin`目录的，**即与bin最挨近的那个目录，不然会识别不到二进制和库文件**，但!!!`不要选到bin目录`,`不要选到bin目录`,`不要选到bin目录`!!!)–**注意：图片仅供参考，请选择自己的** <img src="https://img-blog.csdnimg.cn/1c8dffa2727f4574bad3e805420495ca.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="选择文件夹mingw64-8.1.0" width="400" height="350"> 如果选择正确，在`目录`那里是可以看到二进制和库的文件路径的。 <img src="https://img-blog.csdnimg.cn/d429cc581be2495992e7fe9366991ecc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="目录会有二进制文件路径" width="450" height="300"> 如果选择不正确就是空白的，后续编译就会出现 `在编译器设置"TDM-GCC XXX"中没有提供二进制目录。中止编译。` 的问题 <img src="https://img-blog.csdnimg.cn/45c3a5eacd3349fcaad122dcb6539c52.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" width="500" height="350">

>  
 再强调一次，每个人的解压缩路径可能会不一样，如果解压后多出一层文件夹，即像下图这样`mingw64-8.1.0`下面还是`mingw64-8.1.0`的，而第二个的`mingw64-8.1.0`目录下才到`bin`目录，就要选择到第二个`mingw64-8.1.0`目录，选择第一层的`mingw64-8.1.0`目录是不正确的。 <img src="https://img-blog.csdnimg.cn/34ac3518012e4eefbd5db645a419f4b7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" width="350" height="300"> 


④ 点击`第4个的箭头图标`给编译器起个名字（例如：`TDM-GCC 8.1.0 seh 64-bit MPI` 或`TDM-GCC 8.1.0 seh 64-bit OpenMP`）

>  
 Tips：这里建议创建两个编译器，即按相同方式再创建一个，一个用于配置MPI编译环境，一个用于配置OpenMP编译环境。当然，一器两用也是可以的。 


<img src="https://img-blog.csdnimg.cn/889771a97c1d40c39491f27f57e2655c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="给编译器起名字" width="400" height="350"> <img src="https://img-blog.csdnimg.cn/8d8d60cbe95e4fe59e6ac69c06b74ea6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="两个新编译器" width="400" height="350">

⑤ 此时新版本编译器已经配置完成，接下来的MPI环境配置需要继续在该界面操作，如果想先保存配置，则可点击`确认`进行保存，但下面的操作需要重新打开。

## 二、配置MPI运行环境（msmpi）和OpenMP环境

### 1、链接MPI的包路径

>  
 **!!!配置之前需要确保系统中已安装msmpi环境**，如未安装，，下载并安装两个文件【`msmpisetup.exe`和`msmpisdk.msi`】即可 


选择`工具`—&gt;`编译选项`，打开`编译器选项 `界面， 在`编译器`勾选`编译时加入以下命令`，然后在这个下方空白处添加以下内容,选择适合自己系统的位数，其中的路径为`MSMPI `的默认安装路径。如果安装在其他路径，请自行更换，【一般安装时在路径处将开头的C改为D即可】。： `64位`

```
-L "C:\Program Files (x86)\Microsoft SDKs\MPI\Lib\x64" -I "C:\Program Files (x86)\Microsoft SDKs\MPI\Include"

```

`32位`

```
-L "C:\Program Files (x86)\Microsoft SDKs\MPI\Lib\x86" -I "C:\Program Files (x86)\Microsoft SDKs\MPI\Include"

```

### 2、添加连接器命令

在`编译器`的`在连接器命令行加入以下命令`（默认是已勾选，如果取消了需要勾选回来）处在已有命令`-static-libgcc` 后加上下面的命令：

**MSMPI环境：** 在**原有命令**上打个`空格`然后加上`-l msmpi`

**OpenMP环境：** 在**原有命令**上打个`空格`然后加上`-fopenmp`

**完整命令：**

```
-static-libgcc -l msmpi -fopenmp

```

**一器两用版：** <img src="https://img-blog.csdnimg.cn/c8bcc90236974802bc87e20f08b8ce82.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="MPI和OpenMP环境配置" width="500" height="550"> 如果需要，则可以将OpenMP环境的`-fopenmp` 放置于一个新的编译器（如上面提到的`TDM-GCC 8.1.0 seh 64-bit OpenMP`）**这个主要看个人喜好** <img src="https://img-blog.csdnimg.cn/4a5a9c3c5af343b3ad028b7b4eeff6d0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" width="500" height="550">

>  
 **到这里，编译时选择新创建的编译器，就已经可以成功编译 MPI 和 OpenMP 程序了。** 


### 3、代码测试

#### a. MPI 程序（c语言）

**hello.c或hello.cpp**

```
#include "stdio.h"
#include "mpi.h"

int main()
{<!-- -->
    int myid, numprocs;
    int  namelen;
    char processor_name[MPI_MAX_PROCESSOR_NAME];
    MPI_Init(NULL,NULL);
    MPI_Comm_rank(MPI_COMM_WORLD,&amp;myid);
    MPI_Comm_size(MPI_COMM_WORLD,&amp;numprocs);
    MPI_Get_processor_name(processor_name,&amp;namelen);
    fprintf(stderr,"Hello World! Process %d of %d on %s\n",myid,numprocs,processor_name);
    MPI_Finalize();
    return 0; 
}

```

**对于MPI程序，编译后，点击Dev Cpp自带的运行工具是不能成功运行出并行效果的，** 因为它一次只能同时启动一个进程，自然没有并行可言，这时当然就需要在cmd命令行使用mpiexec来执行编译生成的exe可执行程序了** <img src="https://img-blog.csdnimg.cn/3f881f8386e54fe39901b4d3546fb7ea.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="编译运行">

>  
 **cmd命令：** `mpiexec -n 4 hello.exe` 需要进入hello.exe所在目录才能执行，否则会找不到程序 


<img src="https://img-blog.csdnimg.cn/6eeb0b67f26b488faaa598dca5be3bb1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_18,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="cmd执行mpi" width="400" height="200"> 每次都需要输入命令，当然是不爽的，主要是懒嘛。Dev Cpp也很友好，提供一个可以自定义工具的功能，那我们可以利用这个功能，虽说不能完全制作出Dev Cpp的运行工具，但我们可以创建一个工具来模拟上面输入命令的操作过程就好啦，这样点一下就可以执行了。（具体配置操作见下面的`三、 Dev Cpp自定义MPI执行工具`）

#### b. OpenMP程序（c语言）

**omptest.c或omptest.cpp**

```
#include &lt;stdio.h&gt;
#include "omp.h"
int main(){<!-- -->
	#pragma omp parallel for num_threads(6)
    for (int i = 0; i &lt; 12; i++)  
    {<!-- -->  
        printf("OpenMP Test, 线程编号为: %d\n", omp_get_thread_num());  
    }  
	return 0;
} 

```

**对于OpenMP，编译后可以直接点击Dev Cpp自带的运行工具运行程序。** <img src="https://img-blog.csdnimg.cn/39e5a31e26704da095522fcfbd780f25.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="编译运行OpenMP">

>  
 补充：对于大部分OpenMP程序，会要求在运行时传参指定启动线程数量，例如下面的程序，其中的`thread_count`就是需要传参的，Dev给的运行工具是不传参的，但即使不传参，OpenMP程序也会有默认的线程数（这里试了是4线程），需要传参怎么办，往下看 


```
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;omp.h&gt;
int main(int argc,char* argv[]){<!-- -->
	int thread_count;
	thread_count=strtol(argv[1],NULL,10);
	#pragma omp parallel num_threads(thread_count)
	printf("Hi, I'm thread number %d!\n",omp_get_thread_num());
		return 0;
}

```

<img src="https://img-blog.csdnimg.cn/3bce4040ba2448438abf606d18fdfcc0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="默认线程数" width="500">

>  
 给程序传参：在菜单栏选择`运行`—&gt;`参数`，在弹出的参数界面的`传递给主程序的参数:`框内输入参数即可（这里的是`线程数`）,再次运行就会得到8线程运行的结果。 **Tips：如果不需要传参了之后记得把输入的参数删除哦，不然在Dev关闭之前输入的参数都会一直存在的哦。** 还有提醒一下，在Dev上编译得到的OpenMP程序通常是不能直接在cmd上运行的哦（VS生成的是可以的），会提示三个线程库不存在（`libgomp-1.dll`，`libgcc_s_seh-1.dll`，`libwinpthread-1.dll`）,那想要在cmd运行怎么办呢？那就找到编译器的安装目录`..\mingw64-8.1.0`，在它的`bin`目录下可以找到这三个文件，把它复制到需要运行的exe文件所在目录下就可以了。但似乎没什么必要！！ <img src="https://img-blog.csdnimg.cn/732b7a4092c04d3d848b419946525fcd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_10,color_FFFFFF,t_70,g_se,x_16" alt="点击运行-参数" width="200"> <img src="https://img-blog.csdnimg.cn/143d00d9cbd94fd29fedd53ad9dc802f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_12,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述" width="200"><img src="https://img-blog.csdnimg.cn/19cc76988f614cf8bc0c3d6ac16a96cc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_12,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述" width="250"> 


## 三、 Dev Cpp自定义MPI执行工具（模拟cmd命令行操作）–新增参数命令
-  打开Dev Cpp软件，选择`工具`—&gt;`配置工具` <img src="https://img-blog.csdnimg.cn/f2294fd7b13a4039b466ba25741d58c8.png#pic_center" alt="选择配置工具"> -  点击`添加` <img src="https://img-blog.csdnimg.cn/17772419fe3d4cd1b33a816ff612e020.png#pic_center" alt="添加工具" width="300" height="80"> -  `标题`处填写一个喜欢的名字：例如 ：`MPI Run 4` **（表示启动4个进程…）** -  `程序`（复制粘贴即可）：`C:\Windows\System32\cmd.exe` -  `工作目录`（复制粘贴即可）：`C:\Windows\System32\` -  参数：有两种选择，主要区别是执行完成后，窗口暂停的方式， 第一种：**/c cd/d &lt;PROJECTPATH&gt; &amp; mpiexec -n 4 &lt;EXENAME&gt; &amp; “&lt;EXECPATH&gt;ConsolePauser.exe”** 第二种： **/k cd/d &lt;PROJECTPATH&gt; &amp; mpiexec -n 4 &lt;EXENAME&gt;** `第一种`是调用Dev Cpp的暂停程序，与Dev Cpp运行的类似，但不会统计执行时间，因为没有传参。**其中ConsolePauser.exe是Dev Cpp安装目录下的暂停程序。** 第二个子句（ cd/d &lt;PROJECTPATH&gt;）是为了确保程序中使用相对位置读取或输出文件时无法正确读取文件内容或输出文件到指定位置。 `第二种`是cmd的执行方式，执行完就还是cmd的窗口 <img src="https://img-blog.csdnimg.cn/ae559b48572d4e8aa774428d005ad585.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="配置并行运行工具-第一种" width="500"> <img src="https://img-blog.csdnimg.cn/95c12e6f75f84cc69e9108e3ba664c67.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="配置并行运行工具-第二种" width="500"> -  点击`确定`保存即可。 -  编译后，运行时不能选择Dev Cpp原本的运行按钮，需要使用上述新建的工具进行运行 -  点击`工具`，在最下方可以看到上面创建的自定义工具（`MPI Run 4`），点击即可。**（当然，如果想要启动不同的进程数，可以像下面那样编辑多个工具，只是其中的进程数不同）** <img src="https://img-blog.csdnimg.cn/3a19fcfecfb344e3ada8d7c57cd6631c.png#pic_center" alt="查看工具"> -  运行上面的`hello.c`，可以得到下面的结果（并行程序，运行结果不一定与图片一致的） <img src="https://img-blog.csdnimg.cn/0e03465a580c44dca6fad04b80f4e7f3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16" alt="运行mpi程序"> 
>  
 **到这里，就已经可以一键运行MPI程序了。** 

