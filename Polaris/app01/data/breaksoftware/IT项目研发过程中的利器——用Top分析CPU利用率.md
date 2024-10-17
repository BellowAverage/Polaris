
--- 
title:  IT项目研发过程中的利器——用Top分析CPU利用率 
tags: []
categories: [] 

---


#### 大纲
- - - - - <ul><li>- - - - - - <ul><li>- 


top是linux程序员经常使用的分析机器运行状态的工具。但是并不是所有人都能清楚如何使用该工具对程序占用CPU资源的情况进行分析，比如图中us、sy、ni、id、wa和si等各是什么意思？高低都能说明什么问题？本文将抛砖引玉，讲解下该工具的使用。 <img src="https://img-blog.csdnimg.cn/direct/1f9a21bd49124f83bae82c18483e73de.png" alt="在这里插入图片描述">

## 被测试工具和环境

为了做好这些实验，我fork了，并在此基础上做了一些功能新增，以支持更多的测试。被测试的工具地址是。 编译的方法是

```
cd stress
sh build.sh

```

同时，测试环境我选用了hyper-V中安装ubuntu22 TLS，4核4G。由于后面会测试到物理内存和虚拟内存，于是我强制要求最大内存量是4G。否则hyper-V会在物理内存不够时，一直找系统要更多的物理内存，从而影响测试进度。 <img src="https://img-blog.csdnimg.cn/direct/078168dd9ec844229a86a9bb4cbb6ed6.png" alt="在这里插入图片描述">

## 确定CPU利用率

在top工具的%CPU(s)行，我们首先需要关注的是id的值。 id全称是idle，即空闲状态。 <img src="https://img-blog.csdnimg.cn/direct/b09a2c1dfee74c988c8f9c86635f62cb.png#pic_center" alt="在这里插入图片描述"> 上图表示CPU资源的99.9%处于idle（空闲）状态。那么CPU的利用率就是100%-99.9%=0.1%。 这个CPU利用率是很低的，一般我们需要将CPU利用率至少保持40%以上。比如一些环境要求，在机器实例数保持不变的情况下，可以多承载1倍的流量，则CPU利用率就不能高于50%，但是又不能太低，于是控制40%是合理的；而一些环境有负载均衡和动态扩缩容做的比较好，不需要一台机器扛住额外的压力，于是可以把CPU利用率控制在80%甚至更高。具体的做法可以有：
- 使用更低配置的实例。- 将实例通过容器化切割成更小的资源单元。- 混合部署CPU利用率高的程序。
一般我们更多遇到的是id比较低，即CPU利用率很高的情况。后面我们主要讲解us，sy、ni、wa和si比较高的情况。

## us

us表示CPU time spent in user space。这主要是一些我们代码中不涉及系统其他资源，只是单纯计算的逻辑对CPU的占用。比如我们计算一个数的平方根，或者做一些其他计算。 <img src="https://img-blog.csdnimg.cn/direct/32cdeaff9f244624b09fb2a6cdd8fd72.png#pic_center" alt="在这里插入图片描述"> 我们可以使用下面指令测试什么代码会导致us上涨。

```
stress -c 8 -t 30

```

<img src="https://img-blog.csdnimg.cn/direct/5aead9b508cb43a48ba01f665787de0b.png#pic_center" alt="在这里插入图片描述"> 上面指令是fork出8个子进程，然后在内部不停计算一个随机数的平方根。这会导致CPU在用户层消耗了全部资源，进而idle变成了0。

```
int
hogcpu (void)
{<!-- -->
    const int max = 1000000;
    while (1) {<!-- -->
        for (int i = 0; i &lt; max; i++)
            sqrt (rand ());
        global_count++;
    }
    return 0;
}

```

如果us比较，则需要关注代码中是否存在一些死循环。但是也有可能单纯是因为计算负责导致的。这就需要结合业务来看。如果希望知道问题出在哪儿，可以通过或者进行深入分析。

## sy

sy表示CPU time spent in kernel space。它主要是我们代码中涉及的一些被保护的资源的调用，而导致CPU消耗在内核层的资源量。比较常见的是内存分配和信号处理。

### 信号处理

比如下面指令会导致信号处理被频繁触发

```
stress --cpu-sys 8 -t 60

```

<img src="https://img-blog.csdnimg.cn/direct/14dcf83d090e47c08ecef11e0a0e4353.png" alt="在这里插入图片描述">

```
int hogcpu_sys(void)
{<!-- -->
    const int max = 1000000;
    while (1) 
    {<!-- -->
        for (int i = 0; i &lt; max; i++) 
            raise (SIGINT);
        global_count++;
    }
    return 0;
}

```

网上有些人说，信号（signal）处理会体现在si（software interrupt）的提升，但是经过试验，我发现主要提升在sy上。

### 内存分配和释放

```
stress -m 8 -t 60

```

<img src="https://img-blog.csdnimg.cn/direct/61e34689554d4355a597d9d6a979096f.png" alt="在这里插入图片描述"> 上面的指令会导致stress启动8个子进程，在子进程中频繁分配和释放内存。

```
int
hogvm (long long bytes, long long stride, long long hang, int keep)
{<!-- -->
    long long i;
    char *ptr = 0;
    char c;
    int do_malloc = 1;

    while (1)
    {<!-- -->
        if (do_malloc)
        {<!-- -->
            dbg (stdout, "allocating %lli bytes ...\n", bytes);
            if (!(ptr = (char *) malloc (bytes * sizeof (char))))
            {<!-- -->
                err (stderr, "hogvm malloc failed: %s\n", strerror (errno));
                return 1;
            }
            if (keep)
                do_malloc = 0;
        }

        dbg (stdout, "touching bytes in strides of %lli bytes ...\n", stride);
        for (i = 0; i &lt; bytes; i += stride)
            ptr[i] = 'Z';           /* Ensure that COW happens.  */

        if (hang == 0)
        {<!-- -->
            dbg (stdout, "sleeping forever with allocated memory\n");
            while (1)
                sleep (1024);
        }
        else if (hang &gt; 0)
        {<!-- -->
            dbg (stdout, "sleeping for %llis with allocated memory\n", hang);
            sleep (hang);
        }

        for (i = 0; i &lt; bytes; i += stride)
        {<!-- -->
            c = ptr[i];
            if (c != 'Z')
            {<!-- -->
                err (stderr, "memory corruption at: %p\n", ptr + i);
                return 1;
            }
        }

        if (do_malloc)
        {<!-- -->
            free (ptr);
            dbg (stdout, "freed %lli bytes\n", bytes);
        }
    }

    return 0;
}

```

这段代码比较有意思是每隔stride字节，写入一个‘Z’。这是为了触发写时复制（COW）机制，同时可以保证GCC在编译时，不会将这种既申请又释放的逻辑优化成什么都不做。 一般情况下，sy比较高是不太正常的，因为它说明CPU陷入到内核层太多了。我们需要检查代码，或使用或者中介绍的工具进行分析。

## ni

ni表示CPU time spent on low priority processes，即CPU耗费在低优先级程序上的资源量。 <img src="https://img-blog.csdnimg.cn/direct/eb5da50597704648bf4372bc74559740.png#pic_center" alt="在这里插入图片描述"> 一般情况下，这个值接近0。 我们可以使用下面指令让该值上涨。

```
stress --cpu-nice 19 -c 8 -t 60

```

<img src="https://img-blog.csdnimg.cn/direct/eb3ee221ba5c4935bf80b1a18c9ae21a.png" alt="在这里插入图片描述"> 上面指令会导致stress创建出8个子进程，每个子进程最终会将自己的优先级调到19（最低）。

```
            case 0:            /* child */
                worker_init();
                if (do_cpu_nice) {<!-- -->
                    int ret = nice (do_cpu_nice);
                    if (ret == -1)
                    {<!-- -->
                        err (stderr, "nice failed: %s\n", strerror (errno));
                        return 1;
                    }
                }
                alarm (timeout);
                usleep (backoff);
                if (do_dryrun)
                    exit (0);
                exit (hogcpu ());

```

ni值很高说明系统中没有优先级高的程序在运行，于是CPU都被优先级低的程序给抢了。

### 试验

我们开两个终端，分别执行

```
stress --cpu-nice 19 -c 4 -t 60

```

```
stress -c 4 -t 60

```

前者启动了4个优先级最低的stress进程做sqrt计算；后者启动了4个正常优先级的stress也做sqrt计算。 可以看到CPU会被高优先级的stress抢走（19最低，-20最高，一般是0），于是ni的值也不高，但是us的值很高。 <img src="https://img-blog.csdnimg.cn/direct/6a477a3483e4464ea8de65a143aeec31.png" alt="在这里插入图片描述"> 然后再看计算量，可以看到高优先级的stress一共完成了22469次计算，而低优先级的只完成了1190次计算。这也符合CPU的占用率分布情况。

```
fangliang@fangliang:~/stress$ stress --cpu-nice 19 -c 4 -t 60
stress: info: [84362] dispatching hogs: 4 cpu, 0 io, 0 vm, 0 hdd, 0 cpu_sys 
stress: info: [84366] stress: info: [84364] stress: info: [84365] stress: info: [84362] pid: 84366, count: 291
stress: info: [84362] pid: 84364, count: 290
stress: info: [84362] pid: 84365, count: 305
stress: info: [84363] stress: info: [84362] pid: 84363, count: 304
stress: info: [84362] successful run completed in 60s.total count is 1190

```

```
fangliang@fangliang:~/stress$ stress -c 4 -t 60
stress: info: [84329] dispatching hogs: 4 cpu, 0 io, 0 vm, 0 hdd, 0 cpu_sys 
stress: info: [84331] stress: info: [84330] stress: info: [84333] stress: info: [84332] stress: info: [84329] pid: 84330, count: 5641
stress: info: [84329] pid: 84331, count: 5598
stress: info: [84329] pid: 84332, count: 5624
stress: info: [84329] pid: 84333, count: 5606
stress: info: [84329] successful run completed in 60s.total count is 22469

```

## wa

wa表示CPU time spent in wait (on disk)，即CPU花在等待IO完成上的比例。 我们CPU处理速度和磁盘写入速度是不一致的，所以我们执行写入操作实际是CPU将内容从用户态交给内核态，内核态通知磁盘写入，然后等待其完成，于是就有wa的存在。 如果wa很高说明该系统上程序写入文件占比很高，没有充分利用CPU资源——因为等待占的时间太多了。 我们可以通过下面指令来测试

```
stress -d 8 -t 60

```

<img src="https://img-blog.csdnimg.cn/direct/3784cb6406d1469f9c419c66e2e907a5.png" alt="在这里插入图片描述"> 可以看到CPU主要处于wa状态，而此时磁盘已经满负荷运行了。

```
iostat -xdm 1

```

<img src="https://img-blog.csdnimg.cn/direct/e5c81925565f4754817eaca20ca7c98a.png" alt="在这里插入图片描述"> 如果wa比较高，我们则需要优化文件IO操作来提升CPU利用率。因为处于该等待状态的CPU实际是可以被利用的。后面有机会我会开篇博文讲下这块如何优化。

## si

si表示CPU time spent servicing/handling software interrupts，即处理软中断的时间。一种比较常见的软中断是物理内存不够时，系统申请虚拟内存。 我们可以通过下面指令进行测试

```
stress -m 2 --vm-bytes 1073741824 --vm-beginning 3221225472 -t 600

```

<img src="https://img-blog.csdnimg.cn/direct/db1f836db26a4caab02e8f38ebaee0c3.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/b9e77d264e7548b2a463f09704605f49.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/ae5929d8429f42668444249a87e3015c.png" alt="在这里插入图片描述"> 上面的指令–vm-beginning 3221225472会在主程序启动时，分配3G内存并占用不释放，然后-m 2 --vm-bytes 1073741824会启动2个子进程频繁申请释放1G内存。这样就会导致频繁的虚拟内存申请和释放，进而触发软中断，导致si的值上升。 如果si的值比较高，需要考虑诸如物理内存不够导致虚拟内存频繁申请和释放等问题。

## hi和st
- hi: hardware irq (or) % CPU time spent servicing/handling hardware interrupts- st: steal time - - % CPU time in involuntary wait by virtual cpu while hypervisor is servicing another processor (or) % CPU time stolen from a virtual machine
目前没有模拟出来这两种场景，现实中遇到的也比较少。

## 平均负载

下图中三个值是系统计算的CPU 1分钟、5分钟和15分钟的平均负载。 <img src="https://img-blog.csdnimg.cn/direct/d316a14372da47cbbe60a07e56f3c624.png" alt="在这里插入图片描述"> 这三个值横向比较，只能说明CPU负载的一个趋势。比如上图：1分钟平均负载（0.07）&lt; 5分钟平均负载（0.76）&lt; 15分钟平均负载（1.36），说明系统负载在降低，即系统变得空闲些。反之则说明系统越来越忙碌。 单个看每个值，则需要结合系统的CPU数量。

```
cat /proc/cpuinfo | grep "processor" | wc -l

```

比如我的测试系统是4核心，则上面指令返回4。 **要通过load average/cpu count来判断一段时间内CPU的状态。** 我们先做些试验。

### 满载运行

此时我们用下面指令把4个核心压满，且运行20分钟。

```
stress -c 4 -t 1200

```

<img src="https://img-blog.csdnimg.cn/direct/cb9e8add7a1d46ec9624f3ba837d8880.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/ee748da536b5458d9c8a2280e816ffc4.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/182f57c4e53b41eabd5af08cae28db9e.png" alt="在这里插入图片描述"> 可以发现在4核满负载运行接近20分钟时，5分钟和15分钟load average的值都不到4。1分钟的load average大概是在程序运行6分钟时才稳定在4。通过观察可以发现，这些数值在后期变化会越来越慢。

### 超负载运行

下面指令我们启动16个进程压4个核。

```
stress -c 16 -t 1200

```

<img src="https://img-blog.csdnimg.cn/direct/a3b9c4d982af4f83843c9576f41fcf43.png" alt="在这里插入图片描述"> 可以看到load average很快超过了启动4个程序时的值。1分钟、5分钟和15分钟的单个核心负载是14.81/4=3.7025，7.7/4=1.925，4.62/4=1.155。这些值大于1，说明CPU超负载了。

### 总结

#### load average横向对比

1、5、15分钟值基本相等，说明系统稳定运行； 哪个值和其他值对比出现偏离，说明产生了变化。
- 1分钟偏离，说明系统在变忙碌（值大），或者变空闲（值小）。- 5分钟偏离，说明中期系统出现抖动。- 15分钟偏离，说明系统在变空闲（值大），或者变忙碌（值小）。- <img src="https://img-blog.csdnimg.cn/direct/35584d6b019344749826e6e4205ec33d.png" alt="在这里插入图片描述"> 一般只要出现非平稳状态，就要定位原因，否则就是隐患。
#### load average和CPU核心数

load average/cpu count如果大于1，说明CPU超负载运行，即大家都要等待CPU空闲时才能被调度；反之不满载。根据经验，这个值控制在0.8附近比较合适。

## 参考资料
- - - 