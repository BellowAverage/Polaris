
--- 
title:  Hadoop - YARN 
tags: []
categories: [] 

---
**目录**





















>  
 **Apache Hadoop YARN （Yet Another Resource Negotiator 另一种资源协调者）是一种新的Hadoop资源管理器** 
 **YARN是一个通用资源管理系统和调度平台，可为上层应用提供统一的资源管理和调度** 
 **它的引入为集群在利用率，资源统一管理和数据共享等方面带来了巨大好处** 


<img alt="" height="267" src="https://img-blog.csdnimg.cn/6826fc519fe046ffbc0363d23bf00e7e.png" width="794">

### 1、YARN是一个通用资源管理系统和调度平台

>  
 资源管理系统：集群的硬件资源，和程序运行无关，比如内存、CPU等 
 调度平台：多个程序同时申请计算资源如何分配，调度的规则（算法） 
 通用：不仅仅支持MapReduce程序，理论上支持各种计算程序，YARN不关心你干什么，只关心你要资源，在有的情况下给你，用完了以后还我。 


>  
 可以把Hadoop YARN理解为相当于一个分布式的操作系统平台，而MapReduce等计算程序则相当于运行于操作系统之上的应用程序，YARN为这些程序提供运算所需的资源（内存，CPU等）。 
 Hadoop能有今天的地位，YARN功不可没，因为有了YARN，更多计算框架可以接入到HDFS中，而不单单是MapReduce，正是因为YARN的包容，使得其他计算框架能专注于计算性能的提升。 
 HDFS可能不是最优秀的大数据存储系统，但却是应用最广泛的大数据存储系统， YARN功不可没 


** ###################################################**

### 2、YARN架构

<img alt="" height="476" src="https://img-blog.csdnimg.cn/0fefb1028fd143e4803ca321c0fe03e6.png" width="791">

#### ResourceManager(RM)

>  
 YARN集群的主角色，决定系统中所有应用程序之间资源分配的最终权限，即最终仲裁者 
 接收用户的作业提交，并通过NM分配，管理各个机器的计算资源 


#### NodeManager（NM）

>  
 YARN中的从角色，一台机器上一个，负责管理本机器上的计算资源 
 根据RM命令，启动Container容器，监视容器的资源使用功能情况，并且项RM主角色汇报资源使用情况 


#### ApplicationMaster（AM）

>  
 用户提交的每一个应用程序均包含一个AM 
 应用程序内的老大，负责程序内部各阶段资源申请，监督程序的执行情况。 


** ###################################################** 

### 3、程序提交YARN交互流程

>  
 当用户向YARN中提交一个应用程序后，YARN将分两个阶段运行该应用程序 
 第一个阶段是客户端申请资源启动本次程序的ApplicationMaster 
 第二个阶段是由ApplicationMaster根据本次程序内部具体情况，为它申请资源，并监控它的整个运行过程，直到运行完成。 


 <img alt="" height="466" src="https://img-blog.csdnimg.cn/9dc9e2ea5a87444884557811032b38d0.png" width="798">

 具体过程：

>  
 第一步：用户通过客户端向YARN中的ResourceManager提交应用程序（比如hadoop jar提交MR程序） 
 第二步：ResourceManager为该应用程序分配第一个Container（容器），并与对应的NodeManager通信，要求它在这个Container中启动这个应用程序的ApplicationMaster 
 第三步：ApplicationMaster启动成功之后，首先项ResourceManager注册，并保持通信，这样用户可以直接通过ResourceManager查看应用程序的运行状态（处理了百分之几） 
 第四步：ApplicationMaster为本次程序内部各个Task项ResourceManager申请资源，并监控它的运行状态 
 第五步：一旦ApplicationMaster申请到资源后，便与对应的NodeManager通信，要求它启动任务。 
 第六步：NodeManager为任务设置好运行环境后，将任务启动命令写到一个脚本中，并通过该脚本启动任务。 
 第七步：各个任务通过某个 RPC 协议向 ApplicationMaster 汇报自己的状态和进度，以让 ApplicationMaster 随时掌握各个任务的运行状态，从而可以在任务失败时重新启动任务。在应用程序运行过程中，用户可随时通过RPC 向 ApplicationMaster 查询应用程序的当前运行状态 
 第八步：应用程序运行完成后，ApplicationMaster向ResourceManager注销并关闭自己 


** ###################################################** 

### 4、YARN资源调度器Scheduler

>  
 在理想情况下，应用程序提出的请求将立即得到YARN批准。但是实际中，资源是有限的，并且在繁忙的群集上， 
 应用程序通常将需要等待其某些请求得到满足。YARN调度程序的工作是根据一些定义的策略为应用程序分配资源 
 在YARN中，负责给应用分配资源的就是Scheduler，它是ResourceManager的核心组件之一。Scheduler完全专 
 用于调度作业，它无法跟踪应用程序的状态。 
 一般而言，调度是一个难题，并且没有一个“最佳”策略，为此，YARN提供了多种调度器和可配置的策略供选择 
 FIFO Scheduler（先进先出调度器）、Capacity Scheduler（容量调度器）、Fair Scheduler（公平调度器）。 Apache版本YARN默认使用Capacity Scheduler。 如果需要使用其他的调度器，可以在yarn-site.xml中的yarn.resourcemanager.scheduler.class进行配置。 


>  
 FIFO Scheduler是Hadoop1.x中JobTracker原有的调度器实现，此调度器在YARN中保留了下来 
 FIFO Scheduler是一个先进先出的思想，即先提交的应用先运行。调度工作不考虑优先级和范围，适用于负载较低 
 的小规模集群。当使用大型共享集群时，它的效率较低且会导致一些问题。 
 FIFO Scheduler拥有一个控制全局的队列queue，默认queue名称为default，该调度器会获取当前集群上所有的 
 资源信息作用于这个全局的queue。 优势：     无需配置，先到先得，易于执行 坏处：     任务的优先级不会变高，因此高优先级的作业需要等待，不适合共享集群 


 <img alt="" height="484" src="https://img-blog.csdnimg.cn/d16c7c560b4f4bcf8b5cc4a7aa21bf29.png" width="640">

>  
 Capacity Scheduler容量调度是Apache Hadoop3.x默认调度策略。该策略允许多个组织共享整个集群资源，每个 
 组织可以获得集群的一部分计算能力。通过为每个组织分配专门的队列，然后再为每个队列分配一定的集群资源， 
 这样整个集群就可以通过设置多个队列的方式给多个组织提供服务了 


>  
 Capacity可以理解成一个个的资源队列，这个资源队列是用户自己去分配的。队列内部又可以垂直划分，这样一个 
 组织内部的多个成员就可以共享这个队列资源了，在一个队列内部，资源的调度是采用的是先进先出(FIFO)策略。 


 <img alt="" height="480" src="https://img-blog.csdnimg.cn/ee8b32cbb8764113bc9336328553be3e.png" width="748">

>  
 Capacity Scheduler调度器以队列为单位划分资源。简单通俗点来说，就是一个个队列有独立的资源，队列的结构 
 和资源是可以进行配置的。 


 <img alt="" height="270" src="https://img-blog.csdnimg.cn/f3bfca33254449a2966e088d980373e8.png" width="794">

** ###################################################** 

#### **Capacity Scheduler 特性优势**

>  
 层次化的队列设计（Hierarchical Queues） 
 层次化的管理，可以更容易、更合理分配和限制资源的使用。 
 容量保证（Capacity Guarantees） 
 每个队列上都可以设置一个资源的占比，保证每个队列都不会占用整个集群的资源。 
 安全（Security） 
 每个队列有严格的访问控制。用户只能向自己的队列里面提交任务，而且不能修改或者访问其他队列的任务。 
 弹性分配（Elasticity） 
 空闲的资源可以被分配给任何队列。 
 当多个队列出现争用的时候，则会按照权重比例进行平衡。 


>  
 Fair Scheduler叫做公平调度，提供了YARN应用程序公平地共享大型集群中资源的另一种方式。使所有应用在平 
 均情况下随着时间的流逝可以获得相等的资源份额。 
 Fair Scheduler设计目标是为所有的应用分配公平的资源（对公平的定义通过参数来设置）。 
 公平调度可以在多个队列间工作，允许资源共享和抢占 


 <img alt="" height="433" src="https://img-blog.csdnimg.cn/442b8a308b454759a6c319c8bdc2492e.png" width="707">

####  **如何理解公平共享**

>  
 有两个用户A和B，每个用户都有自己的队列。 
 A启动一个作业，由于没有B的需求，它分配了集群所有可用的资源。 
 然后B在A的作业仍在运行时启动了一个作业，经过一段时间，A,B各自作业都使用了一半的资源。 
 现在，如果B用户在其他作业仍在运行时开始第二个作业，它将与B的另一个作业共享其资源，因此B的每个作业将 
 拥有资源的四分之一，而A的继续将拥有一半的资源。结果是资源在用户之间公平地共享 


####  Fair Scheduler特性优势

>  
 分层队列：队列可以按层次结构排列以划分资源，并可以配置权重以按特定比例共享集群 
 基于用户或组的队列映射：可以根据提交任务的用户名或组来分配队列。如果任务指定了一个队列,则在该队列中 
 提交任务 
 资源抢占：根据应用的配置，抢占和分配资源可以是友好的或是强制的。默认不启用资源抢占 
 保证最小配额：可以设置队列最小资源，允许将保证的最小份额分配给队列，保证用户可以启动任务。当队列不能 
 满足最小资源时,可以从其它队列抢占。当队列资源使用不完时,可以给其它队列使用。这对于确保某些用户、组或 
 生产应用始终获得足够的资源 
 允许资源共享：即当一个应用运行时,如果其它队列没有任务执行,则可以使用其它队列,当其它队列有应用需要资源 
 时再将占用的队列释放出来。所有的应用都从资源队列中分配资源 
 默认不限制每个队列和用户可以同时运行应用的数量。可以配置来限制队列和用户并行执行的应用数量。限制并行 
 执行应用数量不会导致任务提交失败,超出的应用会在队列中等待。 

