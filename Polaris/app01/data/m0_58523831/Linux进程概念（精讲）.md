
--- 
title:  Linux进程概念（精讲） 
tags: []
categories: [] 

---
#### 文章目录
- - <li> 
  <ul>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
## 基本概念

**课本概念：** 程序的一个执行实例，正在执行的程序等。 **内核观点：** 担当分配系统资源（CPU时间，内存）的实体。

只要写过代码的都知道，当你的代码进行编译链接后便会生成一个可执行程序，这个可执行程序本质上是一个文件，是放在磁盘上的。当我们双击这个可执行程序将其运行起来时，本质上是将这个程序加载到内存当中了，因为只有加载到内存后，CPU才能对其进行逐行的语句执行，而一旦将这个程序加载到内存后，我们就不应该将这个程序再叫做程序了，严格意义上将应该将其称之为进程。 <img src="https://img-blog.csdnimg.cn/56e3a1ee59f74884a7bb78bb414950e4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 描述进程-PCB

系统当中可以同时存在大量进程，使用命令ps aux便可以显示系统当中存在的进程。 <img src="https://img-blog.csdnimg.cn/b00c23ccdd304702a3f06e538a18ef5a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 而当你开机的时候启动的第一个程序就是我们的操作系统（即操作系统是第一个加载到内存的），我们都知道操作系统是做管理工作的，而其中就包括了进程管理。而系统内是存在大量进程的，那么操作系统是如何对进程进行管理的呢？ 这时我们就应该想到管理的六字真言：**先描述，再组织**。操作系统管理进程也是一样的，操作系统作为管理者是不需要直接和被管理者（进程）直接进行沟通的，当一个进程出现时，操作系统就立马对其进行描述，之后对该进程的管理实际上就是对其描述信息的管理。 进程信息被放在一个叫做进程控制块的数据结构中，可以理解为进程属性的集合，课本上称之为PCB（process control block）。

操作系统将每一个进程都进行描述，形成了一个个的进程控制块（PCB），并将这些PCB以双链表的形式组织起来。 <img src="https://img-blog.csdnimg.cn/2042fbf7827f4bcba7221c6f3153fca0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 这样一来，操作系统只要拿到这个双链表的头指针，便可以访问到所有的PCB。此后，操作系统对各个进程的管理就变成了对这条双链表的一系列操作。 例如创建一个进程实际上就是先将该进程的代码和数据加载到内存，紧接着操作系统对该进程进行描述形成对应的PCB，并将这个PCB插入到该双链表当中。而退出一个进程实际上就是先将该进程的PCB从该双链表当中删除，然后操作系统再将内存当中属于该进程的代码和数据进行释放或是置为无效。 总的来说，操作系统对进程的管理实际上就变成了对该双链表的增、删、查、改等操作。

### task_struct-PCB的一种

进程控制块（PCB）是描述进程的，在C++当中我们称之为面向对象，而在C语言当中我们称之为结构体，既然Linux操作系统是用C语言进行编写的，那么Linux当中的进程控制块必定是用结构体来实现的。
- PCB实际上是对进程控制块的统称，在Linux中描述进程的结构体叫做task_struct。- task_struct是Linux内核的一种数据结构，它会被装载到RAM（内存）里并且包含进程的信息。
### task_struct内容分类

task_struct就是Linux当中的进程控制块，task_struct当中主要包含以下信息：
- **标示符：** 描述本进程的唯一标示符，用来区别其他进程。- **状态：** 任务状态，退出代码，退出信号等。- **优先级：** 相对于其他进程的优先级。- **程序计数器(pc)：** 程序中即将被执行的下一条指令的地址。- **内存指针：** 包括程序代码和进程相关数据的指针，还有和其他进程共享的内存块的指针。- **上下文数据：** 进程执行时处理器的寄存器中的数据。- **I/O状态信息：** 包括显示的I/O请求，分配给进程的I/O设备和被进程使用的文件列表。- **记账信息：** 可能包括处理器时间总和，使用的时钟总和，时间限制，记账号等。- 其他信息。
## 查看进程

### 通过系统目录查看

在根目录下有一个名为proc的系统文件夹。 <img src="https://img-blog.csdnimg.cn/d6705fb404b242b4b9bb823364b8dcaf.png" alt="在这里插入图片描述"> 文件夹当中包含大量进程信息，其中有些子目录的目录名为数字。 <img src="https://img-blog.csdnimg.cn/7f7f20772520445a82c846e5053b3bfa.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 这些数字其实是某一进程的PID，对应文件夹当中记录着对应进程的各种信息。我们若想查看PID为1的进程的进程信息，则查看名字为1的文件夹即可。 <img src="https://img-blog.csdnimg.cn/363c117c115d4c5abdb8cfbf284eb0f3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 通过ps命令查看

单独使用ps命令，会显示所有进程信息。

```
[cl@VM-0-15-centos dir2]$ ps aux

```

<img src="https://img-blog.csdnimg.cn/990d164696f14c89b378f283fb06ce87.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> ps命令与grep命令搭配使用，即可只显示某一进程的信息。

```
[cl@VM-0-15-centos dir2]$ ps aux | head -1 &amp;&amp; ps aux | grep proc | grep -v grep

```

<img src="https://img-blog.csdnimg.cn/1bdef28c0b2140d789dc76829e57e3fa.png" alt="在这里插入图片描述">

## 通过系统调用获取进程的PID和PPID

通过使用系统调用函数，getpid和getppid即可分别获取进程的PID和PPID。 我们可以通过一段代码来进行测试。 <img src="https://img-blog.csdnimg.cn/7a40315708fb4ec19f56f8e93bdfdeb4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 当运行该代码生成的可执行程序后，便可循环打印该进程的PID和PPID。 <img src="https://img-blog.csdnimg.cn/6010f9c04e864b86965e6e0e10f21ec3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 我们可以通过ps命令查看该进程的信息，即可发现通过ps命令得到的进程的PID和PPID与使用系统调用函数getpid和getppid所获取的值相同。 <img src="https://img-blog.csdnimg.cn/147e106a7c3742bcb30ce8c6a1f41015.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 通过系统调用创建进程- fork初始

### fork函数创建子进程

fork是一个系统调用级别的函数，其功能就是创建一个子进程。 例如，运行以下代码： <img src="https://img-blog.csdnimg.cn/baf351903a6c46efa411baabefc981ba.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 若是代码当中没有fork函数，我们都知道代码的运行结果就是循环打印该进程的PID和PPID。而加入了fork函数后，代码运行结果如下： <img src="https://img-blog.csdnimg.cn/8ea761bed77c48dfb5b22b0aa1fee1eb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 运行结果是循环打印两行数据，第一行数据是该进程的PID和PPID，第二行数据是代码中fork函数创建的子进程的PID和PPID。我们可以发现fork函数创建的进程的PPID就是proc进程的PID，也就是说proc进程与fork函数创建的进程之间是父子关系。

每出现一个进程，操作系统就会为其创建PCB，fork函数创建的进程也不例外。 <img src="https://img-blog.csdnimg.cn/2e7f1f938e2d457c91084bb595265221.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 我们知道加载到内存当中的代码和数据是属于父进程的，那么fork函数创建的子进程的代码和数据又从何而来呢？ 我们看看以下代码的运行结果： <img src="https://img-blog.csdnimg.cn/26457f3f7f9b46c6866857be2b393cd0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 运行结果： <img src="https://img-blog.csdnimg.cn/ae905b7b0c404d9aaeb3e92e93f1bff1.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 实际上，使用fork函数创建子进程，在fork函数被调用之前的代码被父进程执行，而fork函数之后的代码，则默认情况下父子进程都可以执行。需要注意的是，父子进程虽然代码共享，但是父子进程的数据各自开辟空间（采用写时拷贝）。

**小贴士：** 使用fork函数创建子进程后就有了两个进程，这两个进程被操作系统调度的顺序是不确定的，这取决于操作系统调度算法的具体实现。

### 使用if进行分流

上面说到，fork函数创建出来的子进程与其父进程共同使用一份代码，但我们如果真的让父子进程做相同的事情，那么创建子进程就没有什么意义了。 实际上，在fork之后我们通常使用if语句进行分流，即让父进程和子进程做不同的事。

**fork函数的返回值：** 1、如果子进程创建成功，在父进程中返回子进程的PID，而在子进程中返回0。 2、如果子进程创建失败，则在父进程中返回 -1。

既然父进程和子进程获取到fork函数的返回值不同，那么我们就可以据此来让父子进程执行不同的代码，从而做不同的事。 例如，以下代码： <img src="https://img-blog.csdnimg.cn/f1fa79ecbed94422864619dc30afcf8a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> fork创建出子进程后，子进程会进入到 if 语句的循环打印当中，而父进程会进入到 else if 语句的循环打印当中。 <img src="https://img-blog.csdnimg.cn/14b2b825356247f4b6a24914186c8973.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## Linux进程状态

一个进程从创建而产生至撤销而消亡的整个生命期间，有时占有处理器执行，有时虽可运行但分不到处理器，有时虽有空闲处理器但因等待某个时间的发生而无法执行，这一切都说明进程和程序不相同，进程是活动的且有状态变化的，于是就有了进程状态这一概念。 <img src="https://img-blog.csdnimg.cn/30febc0073364567a883fa9490f666ec.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 这里我们具体谈一下Linux操作系统中的进程状态，Linux操作系统的源代码当中对于进程状态有如下定义：

```
/*
* The task state array is a strange "bitmap" of
* reasons to sleep. Thus "running" is zero, and
* you can test for combinations of others with
* simple bit tests.
*/
static const char *task_state_array[] = {<!-- -->
	"R (running)",       /*  0*/
    "S (sleeping)",      /*  1*/
    "D (disk sleep)",    /*  2*/
    "T (stopped)",       /*  4*/
    "T (tracing stop)",  /*  8*/
    "Z (zombie)",        /* 16*/
    "X (dead)"           /* 32*/
};

```

**小贴士：** 进程的当前状态是保存到自己的进程控制块（PCB）当中的，在Linux操作系统当中也就是保存在task_struct当中的。

在Linux操作系统当中我们可以通过 ps aux 或 ps axj 命令查看进程的状态。

```
[cl@VM-0-15-centos ~]$ ps aux

```

<img src="https://img-blog.csdnimg.cn/39e839b9fe8343ee84f59ab07a15a149.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
[cl@VM-0-15-centos ~]$ ps axj

```

<img src="https://img-blog.csdnimg.cn/56d221de641641d9975aa3f5b5537352.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 运行状态-R

一个进程处于运行状态（running），并不意味着进程一定处于运行当中，运行状态表明一个进程要么在运行中，要么在运行队列里。也就是说，可以同时存在多个R状态的进程。

**小贴士：** 所有处于运行状态，即可被调度的进程，都被放到运行队列当中，当操作系统需要切换进程运行时，就直接在运行队列中选取进程运行。

### 浅度睡眠状态-S

一个进程处于浅度睡眠状态（sleeping），意味着该进程正在等待某件事情的完成，处于浅度睡眠状态的进程随时可以被唤醒，也可以被杀掉（这里的睡眠有时候也可叫做可中断睡眠（interruptible sleep））。

例如执行以下代码： <img src="https://img-blog.csdnimg.cn/8c906a2455fd4f879e0b1e98e0289211.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 代码当中调用sleep函数进行休眠100秒，在这期间我们若是查看该进程的状态，则会看到该进程处于浅度睡眠状态。

```
[cl@VM-0-15-centos stat]$ ps aux | head -1 &amp;&amp; ps aux | grep proc | grep -v grep

```

<img src="https://img-blog.csdnimg.cn/0e273aeb1a884f2ab3144e5b35609150.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 而处于浅度睡眠状态的进程是可以被杀掉的，我们可以使用kill命令将该进程杀掉。 <img src="https://img-blog.csdnimg.cn/b1c24eb06ef34e52943aed898c00a140.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 深度睡眠状态-D

一个进程处于深度睡眠状态（disk sleep），表示该进程不会被杀掉，即便是操作系统也不行，只有该进程自动唤醒才可以恢复。该状态有时候也叫不可中断睡眠状态（uninterruptible sleep），处于这个状态的进程通常会等待IO的结束。

例如，某一进程要求对磁盘进行写入操作，那么在磁盘进行写入期间，该进程就处于深度睡眠状态，是不会被杀掉的，因为该进程需要等待磁盘的回复（是否写入成功）以做出相应的应答。（磁盘休眠状态）

### 暂停状态-T

在Linux当中，我们可以通过发送SIGSTOP信号使进程进入暂停状态（stopped），发送SIGCONT信号可以让处于暂停状态的进程继续运行。

例如，我们对一个进程发送SIGSTOP信号，该进程就进入到了暂停状态。 <img src="https://img-blog.csdnimg.cn/b6c0d92f46f74f96b37436ec3d95b534.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 我们再对该进程发送SIGCONT信号，该进程就继续运行了。 <img src="https://img-blog.csdnimg.cn/9db69375b4ca481c8d215d9bd9708280.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> **小贴士：** 使用kill命令可以列出当前系统所支持的信号集。

```
[cl@VM-0-15-centos stat]$ kill -l

```

<img src="https://img-blog.csdnimg.cn/8ac880b5254c4b079e80184c79706ad2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 僵尸状态-Z

当一个进程将要退出的时候，在系统层面，该进程曾经申请的资源并不是立即被释放，而是要暂时存储一段时间，以供操作系统或是其父进程进行读取，如果退出信息一直未被读取，则相关数据是不会被释放掉的，一个进程若是正在等待其退出信息被读取，那么我们称该进程处于僵尸状态（zombie）。

首先，僵尸状态的存在是必要的，因为进程被创建的目的就是完成某项任务，那么当任务完成的时候，调用方是应该知道任务的完成情况的，所以必须存在僵尸状态，使得调用方得知任务的完成情况，以便进行相应的后续操作。 例如，我们写代码时都在主函数最后返回0。 <img src="https://img-blog.csdnimg.cn/7c75749e492942bca4bdb77c67dae84f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 实际上这个0就是返回给操作系统的，告诉操作系统代码顺利执行结束。在Linux操作系统当中，我们可以通过使用echo $?命令获取最近一次进程退出时的退出码。

```
[cl@VM-0-15-centos exitcode]$ echo $?

```

<img src="https://img-blog.csdnimg.cn/ae72f593670b45faa62d38d24c0dcf46.png" alt="在这里插入图片描述">

**小贴士：** 进程退出的信息（例如退出码），是暂时被保存在其进程控制块当中的，在Linux操作系统中也就是保存在该进程的task_struct当中。

### 死亡状态-X

死亡状态只是一个返回状态，当一个进程的退出信息被读取后，该进程所申请的资源就会立即被释放，该进程也就不存在了，所以你不会在任务列表当中看到死亡状态（dead）。

## 僵尸进程

前面说到，一个进程若是正在等待其退出信息被读取，那么我们称该进程处于僵尸状态。而处于僵尸状态的进程，我们就称之为僵尸进程。

例如，对于以下代码，fork函数创建的子进程在打印5次信息后会退出，而父进程会一直打印信息。也就是说，子进程退出了，父进程还在运行，但父进程没有读取子进程的退出信息，那么此时子进程就进入了僵尸状态。

```
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;
int main()
{<!-- -->
	printf("I am running...\n");
	pid_t id = fork();
	if(id == 0){<!-- --> //child
		int count = 5;
		while(count){<!-- -->
			printf("I am child...PID:%d, PPID:%d, count:%d\n", getpid(), getppid(), count);
			sleep(1);
			count--;
		}
		printf("child quit...\n");
		exit(1);
	}
	else if(id &gt; 0){<!-- --> //father
		while(1){<!-- -->
			printf("I am father...PID:%d, PPID:%d\n", getpid(), getppid());
			sleep(1);
		}
	}
	else{<!-- --> //fork error
	}
	return 0;
} 

```

运行该代码后，我们可以通过以下监控脚本，每隔一秒对该进程的信息进行检测。

```
[cl@VM-0-15-centos zombie]$ while :; do ps axj | head -1 &amp;&amp; ps axj | grep proc | grep -v grep;echo "######################";sleep 1;done

```

检测后即可发现，当子进程退出后，子进程的状态就变成了僵尸状态。 <img src="https://img-blog.csdnimg.cn/dac364ce33d74c89aa8b6e7c8d770d04.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 僵尸进程的危害
1. 僵尸进程的退出状态必须一直维持下去，因为它要告诉其父进程相应的退出信息。可是父进程一直不读取，那么子进程也就一直处于僵尸状态。1. 僵尸进程的退出信息被保存在task_struct(PCB)中，僵尸状态一直不退出，那么PCB就一直需要进行维护。1. 若是一个父进程创建了很多子进程，但都不进行回收，那么就会造成资源浪费，因为数据结构对象本身就要占用内存。1. 僵尸进程申请的资源无法进行回收，那么僵尸进程越多，实际可用的资源就越少，也就是说，僵尸进程会导致内存泄漏。
## 孤儿进程

在Linux当中的进程关系大多数是父子关系，若子进程先退出而父进程没有对子进程的退出信息进行读取，那么我们称该进程为僵尸进程。但若是父进程先退出，那么将来子进程进入僵尸状态时就没有父进程对其进行处理，此时该子进程就称之为孤儿进程。 若是一直不处理孤儿进程的退出信息，那么孤儿进程就会一直占用资源，此时就会造成内存泄漏。因此，当出现孤儿进程的时候，孤儿进程会被1号init进程领养，此后当孤儿进程进入僵尸状态时就由int进程进行处理回收。

例如，对于以下代码，fork函数创建的子进程会一直打印信息，而父进程在打印5次信息后会退出，此时该子进程就变成了孤儿进程。

```
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;
int main()
{<!-- -->
	printf("I am running...\n");
	pid_t id = fork();
	if(id == 0){<!-- --> //child
		int count = 5;
		while(1){<!-- -->
			printf("I am child...PID:%d, PPID:%d\n", getpid(), getppid(), count);
			sleep(1);
		}
	}
	else if(id &gt; 0){<!-- --> //father
		int count = 5;
		while(count){<!-- -->
			printf("I am father...PID:%d, PPID:%d, count:%d\n", getpid(), getppid(), count);
			sleep(1);
			count--;
		}
		printf("father quit...\n");
		exit(0);
	}
	else{<!-- --> //fork error
	}
	return 0;
} 

```

观察代码运行结果，在父进程未退出时，子进程的PPID就是父进程的PID，而当父进程退出后，子进程的PPID就变成了1，即子进程被1号进程领养了。 <img src="https://img-blog.csdnimg.cn/28933915744843caaf18ae3f43a4e94a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 进程优先级

### 基本概念

**什么是优先级？** 优先级实际上就是获取某种资源的先后顺序，而进程优先级实际上就是进程获取CPU资源分配的先后顺序，就是指进程的优先权（priority），优先权高的进程有优先执行的权力。

**优先级存在的原因？** 优先级存在的主要原因就是资源是有限的，而存在进程优先级的主要原因就是CPU资源是有限的，一个CPU一次只能跑一个进程，而进程是可以有多个的，所以需要存在进程优先级，来确定进程获取CPU资源的先后顺序。

### 查看系统进程

在Linux或者Unix操作系统中，用ps -l命令会类似输出以下几个内容：

```
[cl@VM-0-15-centos pri]$ ps -l

```

<img src="https://img-blog.csdnimg.cn/54cce9ae911646d2a2e58f10327b447b.png" alt="在这里插入图片描述"> 列出的信息当中有几个重要的信息，如下：
- UID：代表执行者的身份。- PID：代表这个进程的代号。- PPID：代表这个进程是由哪个进程发展衍生而来的，亦即父进程的代号。- PRI：代表这个进程可被执行的优先级，其值越小越早被执行。- NI：代表这个进程的nice值。
### PRI与NI
- PRI代表进程的优先级（priority），通俗点说就是进程被CPU执行的先后顺序，该值越小进程的优先级别越高。- NI代表的是nice值，其表示进程可被执行的优先级的修正数值。- PRI值越小越快被执行，当加入nice值后，将会使得PRI变为：PRI(new) = PRI(old) + NI。- 若NI值为负值，那么该进程的PRI将变小，即其优先级会变高。- 调整进程优先级，在Linux下，就是调整进程的nice值。- NI的取值范围是-20至19，一共40个级别。
**注意：** 在Linux操作系统当中，PRI(old)默认为80，即PRI = 80 + NI。

### 查看进程优先级信息

当我们创建一个进程后，我们可以使用ps -al命令查看该进程优先级的信息。

```
[cl@VM-0-15-centos pri]$ ps -al

```

<img src="https://img-blog.csdnimg.cn/079085aa6dca44719d7d08e8623793a9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> **注意：** 在Linux操作系统中，初始进程一般优先级PRI默认为80，NI默认为0。

### 通过top命令更改进程的nice值

top命令就相当于Windows操作系统中的任务管理器，它能够动态实时的显示系统当中进程的资源占用情况。 <img src="https://img-blog.csdnimg.cn/be9c85668c534e83bdd3f27f18ad3390.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 使用top命令后按“r”键，会要求你输入待调整nice值的进程的PID。 <img src="https://img-blog.csdnimg.cn/b1c9fd8fd597453db148fd0d2a8d6620.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 输入进程PID并回车后，会要求你输入调整后的nice值。 <img src="https://img-blog.csdnimg.cn/4f265665065b40988e2ef644aa9f5e50.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 输入nice值后按“q”即可退出，如果我们这里输入的nice值为10，那么此时我们再用ps命令查看进程的优先级信息，即可发现进程的NI变成了10，PRI变成了90（80+NI）。 <img src="https://img-blog.csdnimg.cn/d7dd469c25f5457db4a1f9102e6d7a46.png" alt="在这里插入图片描述"> **注意：** 若是想将NI值调为负值，也就是将进程的优先级调高，需要使用sudo命令提升权限。

### 通过renice命令更改进程的nice值

使用renice命令，后面跟上更改后的nice值和进程的PID即可。 <img src="https://img-blog.csdnimg.cn/1a2c211dbb90495b8b8b64c575737c59.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 之后我们再用ps命令查看进程的优先级信息，也可以发现进程的NI变成了10，PRI变成了90（80+NI）。 <img src="https://img-blog.csdnimg.cn/586e6e97cf7a4689aea71ca79047a87d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> **注意：** 若是想使用renice命令将NI值调为负值，也需要使用sudo命令提升权限。

### 四个重要概念

**竞争性：** 系统进程数目众多，而CPU资源只有少量，甚至1个，所以进程之间是具有竞争属性的。为了高效完成任务，更合理竞争相关资源，便有了优先级。

**独立性：** 多进程运行，需要独享各种资源，多进程运行期间互不干扰。

**并行：** 多个进程在多个CPU下分别同时进行运行，这称之为并行。

**并发：** 多个进程在一个CPU下采用进程切换的方式，在一段时间之内，让多个进程都得以推进，称之为并发。

## 环境变量

### 基本概念

环境变量（environment variables）一般是指在操作系统中用来指定操作系统运行环境的一些参数。

>  
 例如，我们编写的C/C++代码，在各个目标文件进行链接的时候，从来不知道我们所链接的动静态库在哪里，但是照样可以链接成功，生成可执行程序，原因就是有相关环境变量帮助编译器进行查找。 


环境变量通常具有某些特殊用途，并且在系统当中通常具有全局特性。

### 常见环境变量
- **PATH：** 指定命令的搜索路径。- **HOME：** 指定用户的主工作目录（即用户登录到Linux系统中的默认所处目录）。- **SHELL：** 当前Shell，它的值通常是/bin/bash。
### 查看环境变量的方法

我们可以通过echo命令来查看环境变量，方式如下：

>  
 echo $NAME //NAME为待查看的环境变量名称 


例如，查看环境变量PATH。

```
[cl@VM-0-15-centos ENV]$ echo $PATH

```

<img src="https://img-blog.csdnimg.cn/244cc170635a49448137954426ad509c.png" alt="在这里插入图片描述">

### 测试PATH

大家有没有想过这样一个问题：为什么执行ls命令的时候不用带./就可以执行，而我们自己生成的可执行程序必须要在前面带上./才可以执行？ <img src="https://img-blog.csdnimg.cn/67676373678d4da9b24a2bfb19719a93.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 容易理解的是，要执行一个可执行程序必须要先找到它在哪里，既然不带./就可以执行ls命令，说明系统能够通过ls名称找到ls的位置，而系统是无法找到我们自己的可执行程序的，所以我们必须带上./，以此告诉系统该可执行程序位于当前目录下。

而系统就是通过环境变量PATH来找到ls命令的，查看环境变量PATH我们可以看到如下内容： <img src="https://img-blog.csdnimg.cn/31d068acb6fd4b9b973b381e829a6cd0.png" alt="在这里插入图片描述"> 可以看到环境变量PATH当中有多条路径，这些路径由冒号隔开，当你使用ls命令时，系统就会查看环境变量PATH，然后默认从左到右依次在各个路径当中进行查找。 而ls命令实际就位于PATH当中的某一个路径下，所以就算ls命令不带路径执行，系统也是能够找到的。 <img src="https://img-blog.csdnimg.cn/135ecd05d397457a97d834537856d2fe.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

>  
 那可不可以让我们自己的可执行程序也不用带路径就可以执行呢？ 


当然可以，下面给出两种方式：

**方式一：将可执行程序拷贝到环境变量PATH的某一路径下。** 既然在未指定路径的情况下系统会根据环境变量PATH当中的路径进行查找，那我们就可以将我们的可执行程序拷贝到PATH的某一路径下，此后我们的可执行程序不带路径系统也可以找到了。

```
[cl@VM-0-15-centos ENV]$ sudo cp proc /usr/bin

```

<img src="https://img-blog.csdnimg.cn/b8858aeb1a524a2985c03c90cc447e8d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> **方式二：将可执行程序所在的目录导入到环境变量PATH当中。** 将可执行程序所在的目录导入到环境变量PATH当中，这样一来，没有指定路径时系统就会来到该目录下进行查找了。

```
[cl@VM-0-15-centos ENV]$ export PATH=$PATH:/home/cl/dirforproc/ENV

```

<img src="https://img-blog.csdnimg.cn/16228e68666b412995d68b32f97cee73.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 将可执行程序所在的目录导入到环境变量PATH当中后，位于该目录下的可执行程序也就可以在不带路径的情况下执行了。 <img src="https://img-blog.csdnimg.cn/29eb96c3e7394d27ae015c3cc202e160.png" alt="在这里插入图片描述">

### 测试HOME

任何一个用户在运行系统登录时都有自己的主工作目录（家目录），环境变量HOME当中即保存的该用户的主工作目录。

普通用户示例： <img src="https://img-blog.csdnimg.cn/fd0eecd2ee804a7089de38a45d45007e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 超级用户示例： <img src="https://img-blog.csdnimg.cn/8e62a1c53a7d45178bd8c503ee622d44.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 测试SHELL

我们在Linux操作系统当中所敲的各种命令，实际上需要由命令行解释器进行解释，而在Linux当中有许多种命令行解释器（例如bash、sh），我们可以通过查看环境变量SHELL来知道自己当前所用的命令行解释器的种类。 <img src="https://img-blog.csdnimg.cn/e642b58d58e84f8e88f1c7662674dc52.png" alt="在这里插入图片描述"> 而该命令行解释器实际上是系统当中的一条命令，当这个命令运行起来变成进程后就可以为我们进行命令行解释。 <img src="https://img-blog.csdnimg.cn/19b49b793dc14075869cec8e7fdf5195.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 和环境变量相关的命令

1、echo：显示某个环境变量的值。 <img src="https://img-blog.csdnimg.cn/4268523195104dbeb04cb49826efad40.png" alt="在这里插入图片描述"> 2、export：设置一个新的环境变量。 <img src="https://img-blog.csdnimg.cn/16228e68666b412995d68b32f97cee73.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 3、env：显示所有的环境变量。 <img src="https://img-blog.csdnimg.cn/981248f1f99646b7bfe3e7194c88e632.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 部分环境变量说明：

|环境变量名称|表示内容
|------
|PATH|命令的搜索路径
|HOME|用户的主工作目录
|SHELL|当前Shell
|HOSTNAME|主机名
|TERM|终端类型
|HISTSIZE|记录历史命令的条数
|SSH_TTY|当前终端文件
|USER|当前用户
|MAIL|邮箱
|PWD|当前所处路径
|LANG|编码格式
|LOGNAME|登录用户名

4、set：显示本地定义的shell变量和环境变量。<img src="https://img-blog.csdnimg.cn/1c764ffd2f94422eb345202de5b02829.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 5、unset：清除环境变量。 <img src="https://img-blog.csdnimg.cn/fb581f92b28c4a09829aefe1737fbf1d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 环境变量的组织方式

在系统当中，环境变量的组织方式如下： <img src="https://img-blog.csdnimg.cn/e9c4ae373a8240f8aff745e871ddd343.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 每个程序都会收到一张环境变量表，环境表是一个字符指针数组，每个指针指向一个以’\0’结尾的环境字符串，最后一个字符指针为空。

### 通过代码获取环境变量

你知道main函数其实是有参数的吗？ main函数其实有三个参数，只是我们平时基本不用它们，所以一般情况下都没有写出来。 我们可以在Windows下的编译器进行验证，当我们调试代码的时候，若是一直使用逐步调试，那么最终会来到调用main函数的地方。 <img src="https://img-blog.csdnimg.cn/277e8dd5f3644450acad41ff505b90a8.png" alt="在这里插入图片描述"> 在这里我们可以看到，调用main函数时给main函数传递了三个参数。

>  
 我们先来说说main函数的前两个参数。 


在Linux操作系统下，编写以下代码，生成可执行程序并运行。 <img src="https://img-blog.csdnimg.cn/6df17d2384524dea8fdd86576ba6587e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 运行结果如下： <img src="https://img-blog.csdnimg.cn/b58a1f68a6a14fa5900cf029a27193c9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 现在我们来说说main函数的前两个参数，main函数的第二个参数是一个字符指针数组，数组当中的第一个字符指针存储的是可执行程序的位置，其余字符指针存储的是所给的若干选项，最后一个字符指针为空，而main函数的第一个参数代表的就是字符指针数组当中的有效元素个数。 <img src="https://img-blog.csdnimg.cn/4d441c9ef664495da999b50ca2ebca17.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 下面我们可以尝试编写一个简单的代码，该代码运行起来后会根据你所给选项给出不同的提示语句。

```
#include &lt;stdio.h&gt;                                                                                                                         
#include &lt;string.h&gt;
int main(int argc, char *argv[], char* envp[])
{<!-- -->
	if(argc &gt; 1)
	{<!-- -->
		if(strcmp(argv[1], "-a") == 0)
		{<!-- -->
			 printf("you used -a option...\n");
		}
		else if(strcmp(argv[1], "-b") == 0)
		{<!-- -->
			printf("you used -b option...\n");
		}
		else
		{<!-- -->
			printf("you used unrecognizable option...\n");
		}
	}
	else
	{<!-- -->
		printf("you did not use any option...\n");
	}
	return 0;
}

```

代码运行结果如下： <img src="https://img-blog.csdnimg.cn/93f241359c6940d7ac872876d9175f64.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

>  
 现在我们来说说main函数的第三个参数。 


main函数的第三个参数接收的实际上就是环境变量表，我们可以通过main函数的第三个参数来获取系统的环境变量。 例如，编写以下代码，生成可执行程序并运行。 <img src="https://img-blog.csdnimg.cn/5ff5ea00deeb48f281129f1f312aa52e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 运行结果就是各个环境变量的值： <img src="https://img-blog.csdnimg.cn/a610e9d25c6d40a19d6ed6d43006231d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 除了使用main函数的第三个参数来获取环境变量以外，我们还可以通过第三方变量environ来获取。 <img src="https://img-blog.csdnimg.cn/e4350163f1664a5e89816cf5ecd4ac05.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 运行该代码生成的可执行程序，我们同样可以获得环境变量的值： <img src="https://img-blog.csdnimg.cn/3c66a6ce76cd42acbfe2ada012929943.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> **注意：** libc中定义的全局变量environ指向环境变量表，environ没有包含在任何头文件中，所以在使用时要用extern进行声明。

### 通过系统调用获取环境变量

除了通过main函数的第三个参数和第三方变量environ来获取环境变量外，我们还可以通过系统调用getenv函数来获取环境变量。 getenv函数可以根据所给环境变量名，在环境变量表当中进行搜索，并返回一个指向相应值的字符串指针。

例如，使用getenv函数获取环境变量PATH的值。 <img src="https://img-blog.csdnimg.cn/18c71775c45445afb9705bd5f26920b8.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 运行结果： <img src="https://img-blog.csdnimg.cn/e3da3fda15884d98aead4483864be834.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 程序地址空间

下面这张空间布局图相信大家都见过： <img src="https://img-blog.csdnimg.cn/a0d27fbf4c9f4f05a24eb780933a4739.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_14,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 在Linux操作系统中，我们可以通过以下代码对该布局图进行验证： <img src="https://img-blog.csdnimg.cn/15c0dd2dc7fb4edc9f43610a5e2363f8.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 运行结果如下，与布局图所示是吻合的： <img src="https://img-blog.csdnimg.cn/1d103c05c1f343c29fe9313586b47e5d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

>  
 下面我们来看一段奇怪的代码： 


<img src="https://img-blog.csdnimg.cn/98540b501236496e90fdd09f1166c0f5.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 代码当中用fork函数创建了一个子进程，其中让子进程相将全局变量g_val该从100改为200后打印，而父进程先休眠3秒钟，然后再打印全局变量的值。 按道理来说子进程打印的全局变量的值为200，而父进程是在子进程将全局变量改后再打印的全局变量，那么也应该是200，但是代码运行结果如下： <img src="https://img-blog.csdnimg.cn/5757657ba11a42519e111ab965ad7773.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 可以看到父进程打印的全局变量g_val的值仍为之前的100，更奇怪的是在父子进程中打印的全局变量g_val的地址是一样的，也就是说父子进程在同一个地址处读出的值不同。

如果说我们是在同一个物理地址处获取的值，那必定是相同的，而现在在同一个地址处获取到的值却不同，这只能说明我们打印出来的地址绝对不是物理地址！！！

实际上，我们在语言层面上打印出来的地址都不是物理地址，而是虚拟地址。物理地址用户一概是看不到的，是由操作系统统一进行管理的。

所以就算父子进程当中打印出来的全局变量的地址（虚拟地址）相同，但是两个进程当中全局变量的值却是不同的。 <img src="https://img-blog.csdnimg.cn/fedfa572998e475faa1062b594a81ff4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> **注意：** 虚拟地址和物理地址之间的转化由操作系统完成。

## 进程地址空间

我们之前将那张布局图称为程序地址空间实际上是不准确的，那张布局图实际上应该叫做进程地址空间，进程地址空间本质上是内存中的一种内核数据结构，在Linux当中进程地址空间具体由结构体mm_struct实现。

进程地址空间就类似于一把尺子，尺子的刻度由0x00000000到0xffffffff，尺子按照刻度被划分为各个区域，例如代码区、堆区、栈区等。而在结构体mm_struct当中，便记录了各个边界刻度，例如代码区的开始刻度与结束刻度，如下图所示： <img src="https://img-blog.csdnimg.cn/0a1d68eaa4034064b4e9a85cf0a343fd.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 在结构体mm_struct当中，各个边界刻度之间的每一个刻度都代表一个虚拟地址，这些虚拟地址通过页表映射与物理内存建立联系。由于虚拟地址是由0x00000000到0xffffffff线性增长的，所以虚拟地址又叫做线性地址。

>  
 扩展知识： 1、堆向上增长以及栈向下增长实际就是改变mm_struct当中堆和栈的边界刻度。 2、我们生成的可执行程序实际上也被分为了各个区域，例如初始化区、未初始化区等。当该可执行程序运行起来时，操作系统则将对应的数据加载到对应内存当中即可，大大提高了操作系统的工作效率。而进行可执行程序的“分区”操作的实际上就算编译器，所以说代码的优化级别实际上是编译器说了算。 


每个进程被创建时，其对应的进程控制块（task_struct）和进程地址空间（mm_struct）也会随之被创建。而操作系统可以通过进程的task_struct找到其mm_struct，因为task_struct当中有一个结构体指针存储的是mm_struct的地址。 例如，父进程有自己的task_struct和mm_struct，该父进程创建的子进程也有属于其自己的task_struct和mm_struct，父子进程的进程地址空间当中的各个虚拟地址分别通过页表映射到物理内存的某个位置，如下图： <img src="https://img-blog.csdnimg.cn/2bcf03a63f334b8a85f13ceb4d09fced.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 而当子进程刚刚被创建时，子进程和父进程的数据和代码是共享的，即父子进程的代码和数据通过页表映射到物理内存的同一块空间。只有当父进程或子进程需要修改数据时，才将父进程的数据在内存当中拷贝一份，然后再进行修改。

例如，子进程需要将全局变量g_val改为200，那么此时就在内存的某处存储g_val的新值，并且改变子进程当中g_val的虚拟地址通过页表映射后得到的物理地址即可。 <img src="https://img-blog.csdnimg.cn/dd3c1b9e18224e6bb0f8c05d6cc9e246.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 这种在需要进行数据修改时再进行拷贝的技术，称为写时拷贝技术。

>  
 1、为什么数据要进行写时拷贝？ 


进程具有独立性。多进程运行，需要独享各种资源，多进程运行期间互不干扰，不能让子进程的修改影响到父进程。

>  
 2、为什么不在创建子进程的时候就进行数据的拷贝？ 


子进程不一定会使用父进程的所有数据，并且在子进程不对数据进行写入的情况下，没有必要对数据进行拷贝，我们应该按需分配，在需要修改数据的时候再分配（延时分配），这样可以高效的使用内存空间。

>  
 3、代码会不会进行写时拷贝？ 


90%的情况下是不会的，但这并不代表代码不能进行写时拷贝，例如在进行进程替换的时候，则需要进行代码的写时拷贝。

>  
 为什么要有进程地址空间？ 


1、有了进程地址空间后，就不会有任何系统级别的越界问题存在了。例如进程1不会错误的访问到进程2的物理地址空间，因为你对某一地址空间进行操作之前需要先通过页表映射到物理内存，而页表只会映射属于你的物理内存。总的来说，虚拟地址和页表的配合使用，本质功能就是包含内存。 2、有了进程地址空间后，每个进程都认为看得到都是相同的空间范围，包括进程地址空间的构成和内部区域的划分顺序等都是相同的，这样一来我们在编写程序的时候就只需关注虚拟地址，而无需关注数据在物理内存当中实际的存储位置。 3、有了进程地址空间后，每个进程都认为自己在独占内存，这样能更好的完成进程的独立性以及合理使用内存空间（当实际需要使用内存空间的时候再在内存进行开辟），并能将进程调度与内存管理进行解耦或分离。

>  
 对于创建进程的现阶段理解： 


一个进程的创建实际上伴随着其进程控制块（task_struct）、进程地址空间（mm_struct）以及页表的创建。

## Linux2.6内核进程调度队列

<img src="https://img-blog.csdnimg.cn/c1ef9c7faad0473a94092bfa9e2847c9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMjAyMWRyYWdvbg==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 一个CPU拥有一个runqueue

如果有多个CPU就要考虑进程个数的父子均衡问题。

### 优先级

queue下标说明：
- 普通优先级：100~139。- 实时优先级：0~99。
我们进程的都是普通的优先级，前面说到nice值的取值范围是-20~19，共40个级别，依次对应queue当中普通优先级的下标100~139。

**注意：** 实时优先级对应实时进程，实时进程是指先将一个进程执行完毕再执行下一个进程，现在基本不存在这种机器了，所以对于queue当中下标为0~99的元素我们不关心。

### 活动队列

时间片还没有结束的所有进程都按照优先级放在活动队列当中，其中nr_active代表总共有多少个运行状态的进程，而queue[140]数组当中的一个元素就是一个进程队列，相同优先级的进程按照FIFO规则进程排队调度。

调度过程如下：
1. 从0下标开始遍历queue[140]。1. 找到第一个非空队列，该队列必定为优先级最高的队列。1. 拿到选中队列的第一个进程，开始运行，调度完成。1. 接着拿到选中队列的第二个进程进行调度，直到选中进程队列当中的所有进程都被调度。1. 继续向后遍历queue[140]，寻找下一个非空队列。
bitmap[5]：queue数组当中一共有140个元素，即140个优先级，一共140个进程队列，为了提高查找非空队列的效率，就可以用5 × \times × 32个比特位表示队列是否为空，这样一来便可以大大提高查找效率。

**总结：** 在系统当中查找一个最合适调度的进程的时间复杂度是一个常数，不会随着进程增多而导致时间成本增加，我们称之为进程调度的O(1)算法。

### 过期队列
- 过期队列和活动队列的结构相同。- 过期队列上放置的进程都是时间片耗尽的进程。- 当活动队列上的进程被处理完毕之后，对过期队列的进程进行时间片重新计算。
### active指针和expired指针
- active指针永远指向活动队列。- expired指针永远指向过期队列。
由于活动队列上时间片未到期的进程会越来越少，而过期队列上的进程数量会越来越多（新创建的进程都会被放到过期队列上），那么总会出现活动队列上的全部进程的时间片都到期的情况，这时将active指针和expired指针的内容交换，就相当于让过期队列变成活动队列，活动队列变成过期队列，就相当于又具有了一批新的活动进程，如此循环进行即可。

<img src="https://img-blog.csdnimg.cn/img_convert/01a83c6d3984b0712afdade4d6a6dc26.gif" alt="">
