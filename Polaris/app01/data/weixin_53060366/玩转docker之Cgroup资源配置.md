
--- 
title:  玩转docker之Cgroup资源配置 
tags: []
categories: [] 

---
## 玩转docker之Cgroup资源配置

博主为大家找到一篇比较不错的博客哦！有助于大家了解docker 中的cgroup中的资源配置。

对大家有帮助的话，就去关注一下原创哦！

转载地址：https://www.cnblogs.com/xuhao0705/p/14073525.html

**目录**
- - - <li> 
     <ul>- - - - - 
 

### 摘要

Docker通过Cgroup来控制容器使用的资源配额，包括CPU、内存、磁盘三大方面，基本覆盖了常见的资源配额和使用量控制。

### 一、Cgroup简介

Cgroup是Control Groups的缩写，是Linux内核提供的一种可以限制、记录、隔离进程组所使用的物理资源（如CPU、内存、磁盘IO等待）的机制，被LXC、docker等很多项目用于实现进程资源控制。Cgroup本身是提供将进程进行分组化管理的功能和接口的基础结构，I/O或内存的分配控制等具体的资源管理是通过该功能来实现的。这些具体的资源管理功能称为Cgroup子系统，有以下几大子系统实现：

blkio：设置限制每个块设备的输入输出控制。例如：磁盘，光盘以及usb等等

CPU：使用调度程序为cgroup任务提供CPU的访问

cpuacct：产生cgroup任务的CPU资源报告

cpuset：如果是多核心的CPU，这个子系统会为cgroup任务分配单独的CPU和内存

devices：允许或拒绝cgroup任务对设备的访问

freezer：暂停和恢复cgroup任务

memory：设置每个cgroup的内存限制以及产生内存资源报告

net_cls：标记每个网络包以供cgroup方便使用

ns：命名空间子系统

perf_event：增加了对每个group的监测跟踪的能力，可以监测属于某个特定的group的所有线程以及运行在特定CPU上的线程

下面开始使用stress压力测试工具来测试CPU和内存使用状况

### 二、安装stress工具

### 三、CPU资源分配

默认情况下，每个Docker容器的CPU份额都是1024。单独一个容器的份额是没有意义的。只有在同时运行多个容器时，容器的CPU加权的效果才能体现出来。例如，两个容器A、B的CPU份额分别为1000和500，在CPU进行时间片分配的时候，容器A比容器B多一倍的机会获得CPU的时间片。但分配的结果取决于当时主机和其他容器的运行状态，实际上也无法保证容器A一定能获得CPU时间片。比如容器A的进程一直时空闲的，那么容器B是可以获取比容器A更多的CPU时间片的，极端情况下，例如主机上只运行了一个容器，即使它的CPU份额只有50，它也可以独占整个主机的CPU资源

Cgroup只在容器分配的资源紧缺时，即在需要对容器使用的资源进行限制时，才会生效。因此，无法单纯根据某个容器的CPU份额来确定有多少CPU资源分配给它，资源分配结果取决于同时运行的其他容器的CPU分配和容器中进程运行情况。

可以通过cpu share可以设置容器使用CPU的优先级，比如，启动了两个容器及运行查看CPU使用百分比

#### 3.1、运行两个容器

 

 

#### 3.2、查看内存使用情况

**容器1000cpu使用情况如下**

<img src="https://img2020.cnblogs.com/blog/2090349/202012/2090349-20201202143740112-601383440.png" alt="" class="medium-zoom-image">

 

 

** 容器500cpu使用情况如下**

 

<img src="https://img2020.cnblogs.com/blog/2090349/202012/2090349-20201202143824947-69791432.png" alt="" class="medium-zoom-image">

 

 

**对比后可以得出cpu1000的容器cpu使用率大概是另一个的两倍**

### 四、CPU周期限制

Docker提供了--cpu-period、--cpu-quota两个参数控制容器可以分配到的CPU时钟周期。
- --cpu-period是用来指定容器对CPU的使用要在多长时间内做一次重新分配。- --cpu-quota是用来指定在这个周期内，最多可以有多少时间用来跑这个容器。- 与--cpu-shares不同的是，这种配置是指定一个绝对值，容器对CPU资源的使用绝对不会超过配置的值- cpu-period和cpu-quota的单位为微秒（μs）。cpu-period的最小值为1000微秒，最大值为1秒（10^6 μs），默认值为 0.1 秒（100000 μs）。- cpu-quota的值默认为-1，表示不做控制。cpu-period和cpu-quota参数一般联合使用
例如：容器进程需要每1秒使用单个CPU的0.2秒时间，可以将cpu-period设置为1000000（即1秒），cpu-quota 设置为 200000（0.2 秒）。当然，在多核情况下，如果允许容器进程完全占用两个CPU，则可以将cpu-period设置为100000（即0.1秒），cpu-quota设置为200000（0.2秒）。

### 五、CPU Core控制

对多核 CPU 的服务器，Docker 还可以控制容器运行使用哪些 CPU 内核，即使用--cpuset-cpus 参数。这对具有多 CPU 的服务器尤其有用，可以对需要高性能计算的容器进行性能最优的配置。

#### 5.1、进行CPU Core控制配置

#### 5.2、CPU内核绑定

通过下面指令可以看到容器中进程与 CPU 内核的绑定关系，达到绑定 CPU 内核的目的

#### 5.3、压力测试

### <img src="https://img2020.cnblogs.com/blog/2090349/202012/2090349-20201202151505842-1691032952.png" alt="" class="medium-zoom-image">六、CPU配额参数的混合使用

通过 cpuset-cpus 参数指定容器 A 使用 CPU 内核 1，容器 B 只是用 CPU 内核 3。在主机上只有这两个容器使用对应 CPU 内核的情况，它们各自占用全部的内核资源，cpu-shares 没有明显效果。

cpuset-cpus、cpuset-mems 参数只在多核、多内存节点上的服务器上有效，并且必须与实际的物理配置匹配，否则也无法达到资源控制的目的。

在系统具有多个 CPU 内核的情况下，需要通过 cpuset-cpus 参数为设置容器 CPU 内核才能方便地进行测试

**cpu3容器cpu使用情况**

**<img src="https://img2020.cnblogs.com/blog/2090349/202012/2090349-20201202152752403-423927632.png" alt="" class="medium-zoom-image">**

 

**<strong>cpu4容器cpu使用情况**</strong>

**<strong><img src="https://img2020.cnblogs.com/blog/2090349/202012/2090349-20201202152816855-779514767.png" alt="" class="medium-zoom-image">**</strong>

 

 

 

总结：上面的 centos:stress 镜像安装了 stress 工具，用来测试 CPU 和内存的负载。通过 在两个容器上分别执行 stress -c 1 命令，将会给系统一个随机负载，产生 1 个进程。这 个进程都反复不停的计算由 rand() 产生随机数的平方根，直到资源耗尽。观察到宿主机上的 CPU 使用率，第三个内核的使用率接近 100%， 并且一批进程的 CPU 使用率明显存在 2:1 的使用比例的对比。

### 七、内存限额

与操作系统类似，容器可使用的内存包括两部分：物理内存和Swap，Docker通过下面两组参数来控制容器内存的使用量
- -m或--memory：设置内存的使用限额，例如100M、1024M。- --memory-swap：设置内存+swap的使用限额
执行如下命令允许该容器最多使用200M的内存和300M的内存+swap

### 八、Block IO的限制

默认情况下，所有容器能平等地读写磁盘，可以通过设置--blkio-weight参数来改变容器block IO的优先级。--blkio-weight与--cpu-shares类似，设置的是相对权重值，默认为500。

在下面的例子中，容器A读写磁盘的带宽是容器B的两倍

### 九、bps和iops的限制

bps是byte per second，每秒读写的数据量

iops是io per second，每秒IO的次数

可通过以下参数控制容器的bps和iops：
- --device-read-bps，限制读某个设备的bps- --device-write-bps，限制写某个设备的bps- --device-read-iops，限制读某个设备的iops- --device-write-iops，限制写某个设备的iops 
下面的示例是限制容器写/dev/sda的速率为5MB/s

通过dd命令测试在容器中写磁盘的速度。因为容器的文件系统是在host /dev/sda上的，在容器中写文件相当于对host /dev/sda进行写操作。另外，oflag=direct指定用direct IO方式写文件，这样 --device-write-bps才能生效

结果表明限速5MB/s左右。作为对比测试，如果不限速，结果如下：

 

<img src="https://img-blog.csdnimg.cn/8366a0adcce1433d88c4e1f347b9bb8e.png#pic_center" alt="在这里插入图片描述">
