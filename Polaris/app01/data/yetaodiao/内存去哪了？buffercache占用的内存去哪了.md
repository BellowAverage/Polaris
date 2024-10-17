
--- 
title:  内存去哪了？buffer/cache占用的内存去哪了 
tags: []
categories: [] 

---
**一、前言**

　　近几年开发了一些大型的应用程序，在程序性能调优或者解决一些疑难杂症问题的过程中，遇到最多的还是与内存相关的一些问题。例如glibc内存分配器ptmalloc，google的内存分配器tcmalloc都存在“内存泄漏”，即内存不归还操作系统的问题；ptmalloc内存分配性能低下的问题；随着系统长时间运行，buffer/cache被某些应用大量使用，几乎完整占用系统内存，导致其他应用程序内存申请失败等等问题。

　　之所以内存相关的问题层出不穷，关键还是它的地位太重要了。这次还是与内存相关，分享的是追踪buffer/cache占用的内存到底被谁（哪些应用程序）偷吃了！

　　有关buffer/cache的文章，大多提及的是如何释放并归还到系统的方法，但是分析buffer/cache内存消耗背后原因的相关文章却凤毛麟角。buffer/cache为什么会增长，它到底被哪些程序使用了，我相信这也是很多同行的疑惑，因此想通过本篇文章分享一些buffer/cache内存消耗问题的跟踪方法，为类似问题的优化和解决提供一些参考。

**二、问题描述**

　　如下图1和图2所示，buffer/cache已经占用了46GB的内存，达到了整个系统内存的37%，这个占比已经非常高了。buffer/cache长期占用不释放，同时供系统上其它进程使用的可用内存几乎快没了。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/a75ad3a95098b44bb68bb97e67c345ac.png">

图1

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/fa81df2b21a740a6c2cb31d81c0c888f.png">

图2

 　　长此以往，会出现什么问题呢？最直接的问题就是其他进程没法玩了，比如大一点的内存块就无法申请。之前分享过一次相关问题的定位，参见链接：，我在这篇文章里也详细介绍了buffer/cache的释放方法，解决了当时的燃眉之急。

　　为啥最近又开始与buffer/cache纠缠上了呢？

　　“echo 1 &gt; /proc/sys/vm/drop_caches”释放的是所有cache，这些cache是当前系统上所有程序在运行过程中加载到内存的一些文件信息，这些信息被当做缓存用，好处是CPU下次读取某个文件时就会比第一次从磁盘读取快多了。drop_caches执行时会清空所有cache，这样会带来一个问题：当某些程序需要读取之前加载到cache的信息时就需要重新从磁盘读取，这就会产生IO等待，或者IO竞争，从而拖累程序性能。在某些平台上，我们已经发现有高性能程序因为cache的粗暴清空产生了性能抖动。因此，我们就没法像以前一样回避buffer/cache到底被谁使用的问题，并且直接粗暴释放的策略在某些平台上也就失效了。

　　根据上面的描述，我们当前面临的问题就是：究竟是谁占用了buffer/cache，以及弄清是谁占用后，是否可以规避它对buffer/cache的大量使用。面对这个问题，老板最近又上火了。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/7a4a62ebadafcfa0688616f78b3ab88b.png">

**三、buffer/cache使用跟踪**

　　开始介绍一下调查buffer/cache占用的跟踪思路吧。

　　**1、hcache**

　　网上有一些帖子分享了hcache可以查看哪些文件使用了cache，那hache真的可以帮助我们对buffer/cache进行全面调查吗？我们一起来看看。

　　根据前面的问题描述，当前buffer/cache已经占用了46GB的内存。先使用hcache查看一下top100的cache占用，如下图所示（截取了Cached靠前的一部分）。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/619f56354e9ea5c8a864a9a57bbf8e16.png">

  图3

　　top100，即使top200的Size统计之和，也只有几个GB，离46GB相差甚远，结果说明hcache遗漏了很多cache的使用统计。

　　hcache还有一个能力，查看某个进程当前使用的cache。我们看看clickhouse的cache使用，结果如下图所示。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/cc60a290a47050349e8b43e4b15f7f20.png">

图4

　　正在运行的clickhouse，居然只能看到程序可执行文件本身当前的cache占用，程序运行过程中已打开的cache文件却没统计。不过这里有个小收获：程序加载进内存后，程序的可执行文件，依赖的库文件使用的内存都是在buffer/cache里。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/d3a3b2a206c2d0dc65429442ff9ef4e4.png">

图5

　　从上面的结果发现hcahce有很多缺点，只能粗略的看到一些可执行程序文件，或者一些库文件使用的cache大小，没有统计各程序运行态的cache使用，因此对cache占用问题的排查作用非常有限。

 　　**2、top + lsof + fincore**

　　找了很多资料，除了hcache确实没有其他方法可以统计当前运行程序消耗的cache大小了，但是hcache本身不可靠。没有直接的办法，那就只有围魏救赵了，这也是buffer/cache分布情况不便跟踪调查的原因。

　　该从哪里入手呢？当然是top命令给方向，哪些程序cpu使用率高，且使用了一定的内存，那就查它。因为只有它们才有可能在不断的使用cache，调查大方向有了。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/e7e07734190722b4c24aeeef0998b4e2.png">

图6

　　下一步呢？buffer/cache的使用肯定跟文件相关啊，还是那句话：linux一切皆文件。那有没有可以实时查看某个进程当前已打开的文件方法？lsof命令可以！我们用lsof查一下clickhouse，某时刻，clickhouse打开的文件如下图7图8所示，篇幅太长，图7只截取了前面部分。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/b96899a623b06ef678defc61fdbd305f.png">

图7

　　图8只截取了类型TYPE=REG（REG表示文件类型为普通，还有DIR为目录等等等），即截取了clickhouse当前打开，且正在使用的一部分类型为普通的文件。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/40cb6f682fb758af8202dbf06cca3f0d.png">

图8

　　不断的执行：lsof -p $(pidof clickhouse-server)，发现每次查看到的文件名都不一样。好了，这说明clickhouse会在运行过程中不断的大量打开，读写和关闭文件。嫌疑很重了。

　　下一步呢？有没有办法可以实时查看当前这些文件是不是使用了cache，以及各自使用cache的大小？还真有，fincore可以查看某个文件使用的cache大小，链接：。轮子就是齐全啊，要啥有啥。

　　**命令行：**lsof -p $(pidof clickhouse-server) | grep 'REG' | awk '{print $9}' | xargs ./fincore --pages=false --summarize --only-cached *
