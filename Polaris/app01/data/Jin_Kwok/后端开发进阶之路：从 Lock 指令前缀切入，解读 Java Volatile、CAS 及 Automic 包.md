
--- 
title:  后端开发进阶之路：从 Lock 指令前缀切入，解读 Java Volatile、CAS 及 Automic 包 
tags: []
categories: [] 

---
### 0.引言

Java 技术栈是一个庞大的体系，涉及Java语言、中间件、应用框架等等。在这个体系中，有很多“隐秘的角落”值得探寻。比如：
- <font color="red"> 你可能很了解堆内存，但你听说过堆外内存吗？</font>- <font color="red"> 你可能经常使用 volatile 关键字和 Automic 系列原子类，但你知道它们都是基于 LOCK 指令前缀实现的吗？</font>- <font color="red"> 你可能遇到过异常堆栈丢失的情况，但你清楚背后的原理吗？</font>- <font color="red"> 你可能很熟练地使用日志框架，但你了解它的前世今生吗？</font>- <font color="red"> 你可能经常使用分布式消息队列和缓存，但分布式系统的基本原理你是否了然呢？</font>
笔者闲暇时间写作了 <font color="red"> **“进阶之路”** </font> 系列文章，也许可以解答你的疑惑。

在并发编程中，我们通常会遇到以下三个问题：原子性问题，可见性问题，有序性问题。Java 语言为我们提供了解决上述问题的方法：
- **可见性：** volatile、final 以及锁（synchronized、lock）实现；- **原子性：** JUC 包提供了一些原子类（如AutomicInteger）、锁实现；- **有序性：** volatile、锁实现。
初见之下，锁如同一把“万能钥匙”，但其缺陷也很明显——较“重”，并不适合简单的应用场景，比如，多线程环境下保证共享变量 i++ 操作的原子性，加锁可以实现，但有点“牛刀杀鸡” 的味道。因此，Java 提供了更 “轻” 的方案：volatile、CAS 和 Automic 系列原子类。三者联系紧密，volatile 和 CAS 都是基于 LOCK 指令前缀实现的，Automic 系列原子类是基于 volatile 和 CAS 实现的。

本文主要内容：
1. 计算机和 JVM 内存模型简介；1. LOCK 指令介绍，“锁总线”、“锁缓存”实现原理；1. volatile 保证可见性、有序性的原理；1. CAS 原子性的实现原理；1. Automic 系列原子类实现原子操作的原理。
### 1.计算机和 JVM 内存模型简介

#### 1.1 计算机硬件架构

目前，即便是最普通的计算机，通常 CPU 也是多核的，双核处理器、四核处理器基本已经成为个人电脑的标配，企业级的计算机则更强大，通常具有多个多核 CPU。多核 CPU 支持计算机同时运行多个线程，可显著提升性能。同时，这也催生了一个新的问题——并发问题。下面是一个双 CPU 计算机硬件架构的简单示意图： <img src="https://img-blog.csdnimg.cn/9cb79833142a46468682a677909a0b8c.png#pic_center" alt="在这里插入图片描述" width="600" height="350">

每个 CPU 都包含一系列的寄存器，它们是 CPU 内内存的基础。由于 CPU 访问寄存器的速度远大于访问主存，因此，CPU 在寄存器上执行操作的速度也更快。

通常，CPU 还有一个缓存层，CPU 访问缓存层的速度快于访问主存的速度，但通常比访问内部寄存器的速度慢。严格的讲，CPU 的缓存也细分为多个级别，如1 级缓存、2 级缓存，为简化描述，在此统称为缓存。

<img src="https://img-blog.csdnimg.cn/a93cddc97a7b4a42a046e8b12ee113aa.png#pic_center" alt="在这里插入图片描述" width="600" height="250"> 计算机还包含一个主存，所有的 CPU 都可以访问主存，并且主存的容量比 CPU 的缓存大得多。如上图所示，主存（内存）高达 8G，缓存总共不超过 5M。

通常，为了加快处理速度，当一个 CPU 需要处理主存中的数据时，它会将数据从主存读到 CPU 缓存中。甚至可能将缓存中的部分内容读到它的内部寄存器中，然后在寄存器中执行处理操作。当 CPU 需要将结果写回到主存中去时，它会将内部寄存器的值刷新到缓存中，然后在某个时间点将值刷新回主存。CPU 缓存可以在某一时刻将数据局部写到内存中，也可在某一时刻局部刷新它的内存。但是，它不会在某一时刻读/写整个缓存。

#### 1.2 JVM 内存模型

关于 JVM 内存模型，相信读者应该很熟悉，在此简单介绍一下。如下图所示，JVM 内存模型分为两大部分：
- **线程私有部分**，包括程序计数器，虚拟机栈，本地方法栈；- **线程共有部分**，包括堆、方法区。
<img src="https://img-blog.csdnimg.cn/3df7dfbb120e4bd08f1876801680c4c2.png#pic_center" alt="在这里插入图片描述" width="600" height="300">

#### 1.3 JVM 内存模型与计算机硬件内存架构

事实上，JVM 内存模型与计算机硬件内存架构之间并没有一一对应关系。计算机硬件内存架构没有区分线程栈和堆。对于硬件，所有的线程栈和堆都分布在主内中。某些时候，部分线程栈和堆可能会出现在 CPU 缓存中和 CPU 内部的寄存器中。如下图所示： <img src="https://img-blog.csdnimg.cn/47a740f42eee48f3b6f46864e51bfcfb.png#pic_center" alt="在这里插入图片描述" width="600" height="300">

#### 1.4 多线程并发操作共享变量

如下图所示，一个简化的多线程并发操作共享变量的示意图。Java 线程在对主内存中的共享变量进行操作的时候，并不是直接操作主内存，那样速度太慢了，而是将主内存中的变量 “拷贝” 到线程工作内存中，执行操作完毕后，再将变量回写到主内存中。 <img src="https://img-blog.csdnimg.cn/4d13c234e2814c488041b7b6dbb2baf2.png#pic_center" alt="在这里插入图片描述" width="600" height="400">

不难想见，多 CPU、多线程的环境下，如果共享变量没有采用锁机制，那么，多个线程并发操作主内存的共享变量（如 int value=0），由于变量在线程间是不可见的，可能出现以下情形（举例）：
- A、B 线程分别将变量 value 从主内存读到各自的缓存中，此时，对于两个线程来说，value=0，缓存与主内存一致；- 线程A对变量 value 进行写操作，如 value=10，完成后回写到主内存，线程 B 中 value 仍然为 0，主内存与缓存出现不一致；- 线程 B 根据 “旧值” 完成对 value 的写操作，回写主内存，覆盖掉线程 A 写入的值；
### 2. LOCK 指令及“锁总线”、“锁缓存”实现原理

关于 LOCK 指令，Intel 手册的解释如下：

>  
 Causes the processor’s LOCK# signal to be asserted during execution of the accompanying instruction (turns the instruction into an atomic instruction). In a multiprocessor environment, the LOCK# signal insures that the processor has exclusive use of any shared memory while the signal is asserted. 


其意为：LOCK 指令会使紧跟在其后的指令变成原子操作（atomic instruction）。暂时的锁一下总线，指令执行完了，总线就解锁了！！！

#### 2.1 LOCK 指令前缀

LOCK 指令是一个汇编层面的指令，在一些特殊的场景下，作为前缀加在以下汇编指令之前，保证操作的原子性，这种指令形式被称为 “LOCK 指令前缀”。常见汇编指令如下：

```
ADD, ADC, AND, BTC, BTR, BTS, CMPXCHG, DEC, INC, NEG, NOT, OR, SBB, SUB, XOR, XADD, and XCHG.

```

LOCK 前缀导致处理器在执行指令时会置上 LOCK# 信号，于是该指令就被作为一个原子指令（atomic instruction）执行。在多处理器环境下，置上 LOCK# 信号可以确保任何一个处理器能独占使用任何共享内存。

#### 2.2 锁总线

LOCK 总线封锁信号，三态输出，低电平有效。LOCK 有效时表示CPU 不允许其它总线主控者占用总线（CPU 与内存等硬件之间的通信需要经过总线）。这个信号由软件设置，当指令前加上 LOCK 前缀时，在执行这条指令期间 LOCK 保持有效，阻止其它主控者使用总线。说白了就是 LOCK 前缀只保证对当前指令要访问的内存互斥。

换言之，在多处理器环境中，LOCK# 信号确保在声言该信号期间，处理器可以独占任何共享内存（通过锁住总线，避免其它处理器访问共享内存），当然，这种方式成本较高。

#### 2.3 锁缓存

在 Pentium4、Inter Xeon 和 P6 系列以及之后的处理器中，LOCK＃ 信号一般不锁总线，而是锁缓存，毕竟锁总线开销的比较大。

在所有的 X86 CPU 上都具有锁定一个特定内存地址的能力，当这个特定内存地址被锁定后，它就可以阻止其它的系统总线读取或修改这个内存地址。这种能力是通过 LOCK 指令前缀加上具体操作（如ADD）的汇编指令来实现的。当使用 LOCK 指令前缀时，它会使 CPU 宣告一个 LOCK# 信号，这样就能确保在多处理器系统或多线程竞争的环境下互斥地使用这个内存地址。当指令执行完毕，这个锁定动作也就会消失。

#### 2.4 嗅探技术

处理器使用嗅探技术保证它的内部缓存、系统内存和其它处理器的缓存的数据在总线上保持一致。例如 CPU A 嗅探到 CPU B 打算写内存地址，且这个地址处于共享状态，那么正在嗅探的处理器将使它的缓存行置为无效，在下次访问相同内存地址时，强制执行缓存行填充（即回写缓存，更新自己的缓存）。

### 3. volatile 保证可见性、有序性的原理

关于 volatile 原理，首先要明白 JVM 的内存模型：共享变量是存在主内存中的，各个线程若要操作共享变量，则需创建一个共享变量的拷贝，这个拷贝存在于线程私有的内存中，操作完成后，再回写到主内存中。很明显，这个过程可能会导致不同线程中共享变量不一致。因此，Java 引入 volatile 关键字来保障共享变量在线程间的 “可见性”——volatile 修饰的变量的所有写操作都能立刻反应到其它线程中。

#### 3.1 volatile 如何保证可见性？

对 volatile 修饰的变量进行写操作（赋值），在生成汇编代码中，会有如下的情形：

```
// 写操作
0x01a3de1d: movb $0×0,0×1104800(%esi);
// 内存屏障
0x01a3de24: lock addl $0×0,(%esp);

```

其中，赋值后会再执行一个 lock addl $0×0,(%esp) 操作，这个操作相当于一个内存屏障（Memory Barrier），指令重排时，不能把后面的指令重排到内存屏障之前的位置，如果是单核 CPU 访问，则不需要内存屏障；但如果是多核 CPU 访问同一块内存，则需用内存屏障保障一致性。

多处理器、多线程环境下，若某个线程对声明了volatile 的变量进行写操作，JVM 会向处理器发送一条带有 LOCK 前缀的指令，将这个变量所在缓存行的数据写回主内存，LOCK 前缀指令通过 “锁缓存” 可以确保回写主内存的操作是原子性的。但是，其它处理器的缓存中存储的仍然是 “旧值-old value” ，并不能保证可见性，因此，还要借助缓存一致性协议：每个处理器通过嗅探在总线上传播的数据来检查自己的缓存值是否过期，当处理器发现自己缓存行对应的内存地址被修改时，就会设置当前缓存行为无效，需要对数据进行修改的时候就会重新从主内存中加载。如此，便保证了可见性。

#### 3.2 volatile 不能保证原子性！

为什么不能保证原子性呢？对于 volatile 修饰的变量，LOCK 指令前缀保证的是其写操作和回写主内存的操作是原子性的。什么是写操作？如：value=10，对变量 value 进行写，这是实实在在的写，是一个原子操作。

但是，“value++；”是单纯的写操作吗？不是！value++ 的时候会先将 value 赋值给另外一个临时变量（设为 tmp），tmp 属于工作内存的局部变量表，再将 tmp 写回到缓存，缓存再返回到主内存，这里需要一些寄存器运算的知识。形象一些，可以把 value++ 拆分成以下伪代码：

```
int tmp = value;    //1
tmp = tmp + 1;      //2
value = tmp;        //3

```

很明显，对于变量 value 而言，最后一步：value=temp 才是真正的写操作，LOCK 指令前缀可以保证写操作和回写主内存的操作是原子性的。而前面两步并没有对 value 进行任何写操作，JVM 不会做出反应，这就是为什么 volatile 不能保证原子性的根本原因。

有 Java 多线程编程经验的读者应该清楚，以下代码执行的结果是不稳定的，并且结果都是 &lt;=10000 的，其根因就是 value++ 并非原子性，volatile 无能为力。

```
public class App
{<!-- -->
    private static volatile int value = 0;
    public static void main(String[] args)
    {<!-- -->
        for (int i = 0; i &lt; 10; i++)
        {<!-- -->
            new MyThread().start();
        }
        System.out.println("value = " + value);
    }

    static class MyThread extends Thread
    {<!-- -->
        @Override
        public void run()
        {<!-- -->
            for (int i = 0; i &lt; 1000; i++)
            {<!-- -->
                value++;
            }
        }
    }
}

```

#### 3.3 Volatile 禁止指令重排序

volatile 关键字禁止指令重排序有两层意思（不完全禁止）：
- 当程序执行到 volatile 变量的读或写时，在其前面的操作肯定全部已经执行完毕，且结果已经对后面的操作可见；在其后面的操作肯定还没有执行；- 在进行指令优化时，不能将在 volatile 变量前面访问的语句放在其后面执行，也不能把 volatile 变量后面的语句放到其前面执行。
Lock 指令前缀相当于一个内存屏障（也称内存栅栏），内存屏障主要提供 3 个功能：
- 确保指令重排序时不会把其后面的指令排到内存屏障之前的位置，也不会把前面的指令排到内存屏障的后面；即在执行到内存屏障这句指令时，在它前面的操作已经全部完成；- 强制将对缓存的修改操作立即写入主存，利用缓存一致性机制，并且缓存一致性机制会阻止同时修改由两个以上 CPU 缓存的内存区域数据；- 如果是写操作，它会导致其它 CPU 中对应的缓存行无效。
### 4. CAS 原子性的实现原理

Java 中的 CAS 操作都是通过 SUN 包下 Unsafe 类实现，而 Unsafe 类中的方法都是 native 方法，由 JVM 本地实现，为了弄清楚真正的实现原理，以 AtomicInteger（需要 CAS 操作支持）为例，查看了 openJDK 的源码：

```
UNSAFE_ENTRY(jboolean, Unsafe_CompareAndSwapInt(JNIEnv *env, jobject unsafe, jobject obj, jlong offset, jint e, jint x))
  UnsafeWrapper("Unsafe_CompareAndSwapInt");
  oop p = JNIHandles::resolve(obj);
  // 根据偏移量，计算 value 的地址。这里的 offset 就是 AtomaicInteger 中的 valueOffset
  jint* addr = (jint *) index_oop_from_field_offset_long(p, offset);
  // 调用 Atomic 中的函数 cmpxchg，该函数声明于 Atomic.hpp 中
  return (jint)(Atomic::cmpxchg(x, addr, e)) == e;
UNSAFE_END

```

很明显，Unsafe_CompareAndSwapInt 函数实现的关键在于最后一句，使用了 cmpxchg 指令，进一步，我们来看看 Windows 平台下 Atomic::cmpxchg 函数：

```
// atomic_windows_x86.inline.hpp
#define LOCK_IF_MP(mp) __asm cmp mp, 0  \
                       __asm je L0      \
                       __asm _emit 0xF0 \
                       __asm L0:

inline jint Atomic::cmpxchg (jint exchange_value, volatile jint* dest, jint compare_value) {<!-- -->
  // alternative for InterlockedCompareExchange
  int mp = os::is_MP();
  __asm {<!-- -->
    mov edx, dest
    mov ecx, exchange_value
    mov eax, compare_value
    LOCK_IF_MP(mp)
    cmpxchg dword ptr [edx], ecx
  }
}

```

#### 4.1 LOCK 前缀

上面的代码由 LOCK_IF_MP 预编译标识符和 cmpxchg 函数组成。为了看到更清楚一些，我们将 cmpxchg 函数中的 LOCK_IF_MP 替换为实际内容。如下：

```
inline jint Atomic::cmpxchg (jint exchange_value, volatile jint* dest, jint compare_value) {<!-- -->
  // 判断是否是多核 CPU
  int mp = os::is_MP();
  __asm {<!-- -->
    // 将参数值放入寄存器中
    mov edx, dest    // 注意: dest 是指针类型，这里是把内存地址存入 edx 寄存器中
    mov ecx, exchange_value
    mov eax, compare_value

    // LOCK_IF_MP
    cmp mp, 0
    /*
     * 如果 mp = 0，表明是线程运行在单核 CPU 环境下。此时 je 会跳转到 L0 标记处，
     * 也就是越过 _emit 0xF0 指令，直接执行 cmpxchg 指令。也就是不在下面的 cmpxchg 指令
     * 前加 lock 前缀。
     */
    je L0
    /*
     * 0xF0 是 lock 前缀的机器码，这里没有使用 lock，而是直接使用了机器码的形式。至于这样做的
     * 原因可以参考知乎的一个回答：
     *     https://www.zhihu.com/question/50878124/answer/123099923
     */ 
    _emit 0xF0
L0:
    /*
     * 比较并交换。简单解释一下下面这条指令，熟悉汇编的朋友可以略过下面的解释:
     *   cmpxchg: 即“比较并交换”指令
     *   dword: 全称是 double word，在 x86/x64 体系中，一个 
     *          word = 2 byte，dword = 4 byte = 32 bit
     *   ptr: 全称是 pointer，与前面的 dword 连起来使用，表明访问的内存单元是一个双字单元
     *   [edx]: [...] 表示一个内存单元，edx 是寄存器，dest 指针值存放在 edx 中。
     *          那么 [edx] 表示内存地址为 dest 的内存单元
     *          
     * 这一条指令的意思就是，将 eax 寄存器中的值（compare_value）与 [edx] 双字内存单元中的值
     * 进行对比，如果相同，则将 ecx 寄存器中的值（exchange_value）存入 [edx] 内存单元中。
     */
    cmpxchg dword ptr [edx], ecx
  }
}

```

综上，可以发现，CAS 的实现离不开处理器的支持。以上这么多代码，其实核心代码就是一条带 LOCK 前缀的 cmpxchg 指令（注意：上面的代码中 LOCK 指令用机器码 “0xF0” 表示），即

```
lock cmpxchg dword ptr [edx], ecx

```

程序会根据当前处理器的类型来决定是否为 cmpxchg 指令添加 LOCK 前缀。如果程序是在多处理器上运行，就为 cmpxchg 指令加上 LOCK 前缀（LOCK cmpxchg）。反之，如果程序是在单处理器上运行，就省略 LOCK 前缀（单处理器自身会维护单处理器内的顺序一致性，不需要 LOCK 前缀提供的内存屏障效果）。

#### 4.2 LOCK 指令前缀的作用

在所有的 X86 CPU 上都具有锁定一个特定内存地址的能力，当这个特定内存地址被锁定后，它就可以阻止其它的系统总线读取或修改这个内存地址。这种能力是通过 LOCK 指令前缀再加上具体操作（如上面的 cmpxchg）的汇编指令来实现的。当使用 LOCK 指令前缀时，它会使 CPU 宣告一个 LOCK# 信号，这样就能确保在多处理器系统或多线程竞争的环境下互斥地使用这个内存地址。当指令执行完毕，这个锁定动作也就会消失。

处理器使用嗅探技术保证它的内部缓存、系统内存和其它处理器的缓存的数据在总线上保持一致。例如 CPU A 嗅探到 CPU B 打算写内存地址，且这个地址处于共享状态，那么正在嗅探的处理器将使它的缓存行无效，在下次访问相同内存地址时，强制执行缓存行填充（即重新从主内存中加载共享变量）。

如上所述，LOCK 指令前缀保障了cmpxchg（CAS）操作的原子性。

### 5. Automic 系列原子类实现原子操作的原理

Java 的 JUC（java.util.concurrent）包提供了一系列的原子类，如 AtomicInteger、AtomicLong、AtomicBoolean 等，它们的实现原理基本一致：基于 volatile 关键字和 CAS 原理。本节以 AtomicInteger 为例解读原子类的实现原理。

查看 AtomicInteger 的源码，其中有如下内容：

```
private volatile int value;

public final boolean compareAndSet(int expect, int update) 
{<!-- --> 
    return unsafe.compareAndSwapInt(this, valueOffset, expect, update); 
} 

```

结合前面几节内容，从上面的代码中不难分析出 AtomicInteger 大概的实现原理：通过声明一个 volatile （借助 LOCK 指令的 “内存锁定”，保证同一时刻只有一个线程可以修改内存值）修饰的变量 value，再加上 unsafe.compareAndSwapInt 的方法，来实现线程同步的。

#### 5.1 compareAndSwapInt 的方法

顾名思义，compareAndSwapInt 的方法其实就是 CAS 操作，它是一个 JNI（Java Native Interface）方法，其底层实现也用到了 LOCK 前缀指令，确保操作的原子性。

CAS 指令在 Intel CPU 上称为 CMPXCHG 指令，它的作用是将指定内存地址的内容与所给的某个值相比，如果相等，则将其内容替换为指令中提供的新值，如果不相等，则更新失败。这一比较并交换的操作是原子的，不可以被中断。CAS 包含了读取、比较（这也是种操作）和写入这三个操作，通过硬件保证了原子性，运行速度快。从另一个角度看，虽然 CAS 包含了多个操作，但是，其运算是固定的(就是个比较)，因此锁定开销很小。

如果从锁的角度来审视，CAS 是一种乐观锁，因为它在对共享变量更新之前会先比较当前值是否与更新前的值一致，如果是，则更新，如果不是，则无限循环（称为自旋），直到当前值与更新前的值一致为止，才执行更新。

简单的来说，CAS 有三个操作数，内存值 Current，旧的预期值 Expect，要修改的新值 Update。当且仅当预期值 Expect 和内存值 Current 相同时，将内存值 Current 修改为 Update，否则返回 Current 。这是一种乐观锁的思路，它相信在它修改之前，没有其它线程去修改它；而 Synchronized 是一种悲观锁，它认为在它修改之前，一定会有其它线程去修改它，悲观锁效率很低。

#### 5.2 AtomicInteger 是如何利用 CAS 实现原子性操作的？

##### 5.2.1 volatile 变量

```
private volatile int value;  

```

AtomicInteger 首先声明了一个 volatile 变量 value，通过前面内容的学习，读者应该知道，volatile 关键字保证了变量 value 的内存可见性，也就是所有工作线程中同一时刻都可以得到一致的值。

##### 5.2.2 Compare And Set

比较并设置，这里利用 Unsafe 类的 JNI 方法实现，使用 CAS 指令，可以保证读-改-写是一个原子操作。compareAndSwapInt 有 4 个参数：
- this - 当前 AtomicInteger 对象，- Offset - value 属性在内存中的位置（需要注意的是，Offset 不是value 值 在内存中的位置），- expect - 预期值，- update - 新值，
根据上面的 CAS 操作过程，当内存中的 value 值等于 expect 值时，则将内存中的 value 值更新为 update 值，并返回 true，否则返回 false。在这里我们有必要对 Unsafe 有一个简单点的认识，从名字上来看，“不安全”，但并不是它本身不安全，这个类用于执行偏底层的、不安全操作的方法集合，这个类中的方法大部分是对内存的直接操作，如果使用不当，可能存在 “不安全”。事实上，在我们使用反射机制、并发包、直接内存时，都间接的用到了 Unsafe 类。

```
public class AtomicInteger extends Number implements java.io.Serializable {<!-- -->
    private static final long serialVersionUID = 6214790243416807050L;

    // setup to use Unsafe.compareAndSwapInt for updates
    private static final Unsafe unsafe = Unsafe.getUnsafe();
    private static final long valueOffset;

    static {<!-- -->
            // 反射获取value属性，获取其在内存中的位置
        try {<!-- -->
            valueOffset = unsafe.objectFieldOffset
                (AtomicInteger.class.getDeclaredField("value"));
        } catch (Exception ex) {<!-- --> throw new Error(ex); }
    }

    private volatile int value;

    /**
     * Creates a new AtomicInteger with the given initial value.
     *
     * @param initialValue the initial value
     */
    public AtomicInteger(int initialValue) {<!-- -->
        value = initialValue;
    }

    public final boolean compareAndSet(int expect, int update) 
    {<!-- --> 
        return unsafe.compareAndSwapInt(this, valueOffset, expect, update); 
    } 

    // 其它代码略
}

```

##### 5.2.3 循环尝试

volatile 可以保证可见性，但不能保证原子性，CAS 操作虽然是原子性，但保证的是比较&amp;替换的原子性，那么，AutomicInteger 如何实现原子性呢？——二者结合即可！

如下代码（摘录自 AutomicInteger 类），采用了循环设置的策略：
- 首先读取主内存中 value 的当前值 pre；- 基于当前值 pre 进行操作（可以是很复杂的操作，不必保证原子性），得到新的值 next；- 基于 CAS 操作，尝试将新值 next 写入主内存；- 由于其它线程可能已经先行操作了主内存中的共享变量 value，造成 value 与 pre 不相等，那么 CAS 操作将失败，返回 false，循环条件成立，将继续尝试，直到成功；
```
/**
     * Gets the current value.
     *
     * @return the current value
     */
    public final int get() {<!-- -->
        return value;
    }

    /**
     * Atomically updates the current value with the results of
     * applying the given function, returning the previous value. The
     * function should be side-effect-free, since it may be re-applied
     * when attempted updates fail due to contention among threads.
     *
     * @param updateFunction a side-effect-free function
     * @return the previous value
     * @since 1.8
     */
    public final int getAndUpdate(IntUnaryOperator updateFunction) {<!-- -->
        int prev, next;
        do {<!-- -->
            prev = get();
            next = updateFunction.applyAsInt(prev);
        } while (!compareAndSet(prev, next));
        return prev;
    }

    /**
     * Atomically updates the current value with the results of
     * applying the given function, returning the updated value. The
     * function should be side-effect-free, since it may be re-applied
     * when attempted updates fail due to contention among threads.
     *
     * @param updateFunction a side-effect-free function
     * @return the updated value
     * @since 1.8
     */
    public final int updateAndGet(IntUnaryOperator updateFunction) {<!-- -->
        int prev, next;
        do {<!-- -->
            prev = get();
            next = updateFunction.applyAsInt(prev);
        } while (!compareAndSet(prev, next));
        return next;
    }

```

### 6. 推荐一本书

最近读了一本书——**《服务端开发：技术、方法与实用解决方案》**，大为受用，在此推荐给大家。该书作者曾获得<font color="#dd0000">阿里第二届技术讲师课程大赛年度冠军</font>（由阿里 CPO 和 CSDN CEO 共同颁奖），在阿里和蚂蚁内部所授技术课程口碑甚好。全书分 14 章，约 30 万字，正文 373 页，共 389 页，由机械工业出版社出版发行。内容分为上下两篇。上篇 1～6 章，主题为技术和方法；下篇 7～14章，主题为解决方案。书中列举了大量实用案例，为了便于读者理解，作者还绘制了超过 200 幅插图，可谓图文并茂。 <img src="https://img-blog.csdnimg.cn/e84687ceb157470db6946fb9513a36ab.png#pic_center" alt="在这里插入图片描述" width="400" height="450">

#### 6.1 读者对象

这本书体系化地解读了服务端开发的方方面面，特别提供了针对高并发、高可用、高性能、数据一致性等重难点的行业经典解决方案，极具价值。
- **IT 从业人员**：服务端开发工程师、客户端开发工程师、产品经理、测试开发工程师等。- **高校学生**：计算机、软件、自动化、电气、通信等专业有志于进入 IT 行业的在校学生。- **求职面试**：不同于一般的“面试宝典”仅仅侧重对某种语言、框架、中间件等进行解读，本书立足于服务端开发的全局视角，体系化解读服务端开发的大厂规范流程和重难点，面试必备。
#### 6.2 该书特色

无论技术如何演进，其背后的方法往往大同小异，经典解决方案历久弥新。因此，掌握方法和实用解决方案尤为必要。不同于一般的 IT 技术书籍，这本书不局限于任何一种具体的编程语言、框架、容器、中间件或编程思想，而是致力于全景式、体系化地解读服务端开发的流程和重难点。

该书共 14 章，内容从逻辑上可以分为两大部分。

**第一部分为第 1～6 章，主题是技术和方法**。首先概述服务端开发的职责、技术栈、核心流程和进阶路径，然后从需求分析、抽象建模、系统设计、数据设计、非功能性设计 5 个方面逐一展开，结合案例深入解读服务端开发的实操方法和重难点，为读者清晰呈现服务端开发的全景图。通过学习本篇内容，读者可以快速、体系化地掌握服务端开发的相关知识和方法。

**第二部分为第 7～14 章，主题是解决方案**。针对高并发、高可用、高性能、缓存、幂等、数据一致性等服务端开发的典型问题，结合业务场景进行系统性分析并给出解决方案。此外，就接口设计、日志打印、异常处理、代码编写、代码注释等实施细节给出行业案例和规范。本篇内容如同一本服务端开发问题手册，当读者在实践中遇到问题时，可以从中查找解决方案。

目前，本书已经在**京东、淘宝、当当、拼多多**等电商平台发售。在电商 APP 搜索关键词 **“服务端开发”、“服务端开发技术”**，即可搜索到该书。

### 7.引用

本文由原作者授权发表，原文发表于公众号 “互联网技术人进阶之路”，特此声明。
