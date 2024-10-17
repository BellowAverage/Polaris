
--- 
title:  ffmpeg编译 Error: operand type mismatch for `shr‘ 
tags: []
categories: [] 

---
错误如下：

```
D:\msys2\tmp\ccUxvBjQ.s: Assembler messages:
D:\msys2\tmp\ccUxvBjQ.s:345: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:410: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:470: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:645: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:713: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:781: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:866: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:951: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:1036: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:1133: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:1405: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:1514: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:1638: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:1797: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:2137: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:2242: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:2368: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:2553: Error: operand type mismatch for `shr'
D:\msys2\tmp\ccUxvBjQ.s:2703: Error: operand type mismatch for `shr'
make: *** [ffbuild/common.mak:60: libavformat/adtsenc.o] Error 1
make 编译过程中的出现上面错误

```

### 分析：

这些错误是由于汇编代码中存在类型不匹配的错误，导致无法通过汇编阶段编译。 具体是因为什么我也不是太清楚，我是在Windows下的MSYS2中make编译，我猜测是gcc版本的问题，我的ffmpeg源码比较老，是2018年的，我通过MSYS2下载了 mingw64 编译工具链，其中的gcc版本为：13.2.0<img src="https://img-blog.csdnimg.cn/4d03e3781bec44208b18fe5ab888dc0a.png" alt="在这里插入图片描述">

### 解决方法一：

将ffmpeg源码中 mathops.h 中的如下代码做一个修改。

```
#define MULL MULL
static av_always_inline av_const int MULL(int a, int b, unsigned shift)
{<!-- -->
    int rt, dummy;
    __asm__ (
        "imull %3               \n\t"
        "shrdl %4, %%edx, %%eax \n\t"
        :"=a"(rt), "=d"(dummy)
        // :"a"(a), "rm"(b), "ci"((uint8_t)shift)
        :"a"(a), "rm"(b), "i"(shift &amp; 0x1F)
    );
    return rt;
}

```

```
#define NEG_SSR32 NEG_SSR32
static inline  int32_t NEG_SSR32( int32_t a, int8_t s){<!-- -->
    __asm__ ("sarl %1, %0\n\t"
         : "+r" (a)
        //  : "ic" ((uint8_t)(-s))
         : "i" (-s &amp; 0x1F)
    );
    return a;
}

#define NEG_USR32 NEG_USR32
static inline uint32_t NEG_USR32(uint32_t a, int8_t s){<!-- -->
    __asm__ ("shrl %1, %0\n\t"
         : "+r" (a)
        //  : "ic" ((uint8_t)(-s))
         : "i" (-s &amp; 0x1F)
    );
    return a;
}

```

参考链接：https://fftrac-bg.ffmpeg.org/ticket/10405

### 解决方法二：

将ffmpeg源码中 mathops.h 中的如下代码做一个修改，其实在新版本的ffmpeg中已经修复了这个问题，可以去查看一下最新版的ffmpeg中 libavcodec/x86/mathops.h 中的修改，然后将我们的mathops.h 修改为如下：

```
#define MULL MULL
static av_always_inline av_const int MULL(int a, int b, unsigned shift)
{<!-- -->
    int rt, dummy;
    __asm__ (
        "imull %3               \n\t"
        "shrdl %4, %%edx, %%eax \n\t"
        :"=a"(rt), "=d"(dummy)
        :"a"(a), "rm"(b), "c"((uint8_t)shift)
    );
    return rt;
}

```

```
#define NEG_SSR32 NEG_SSR32
static inline  int32_t NEG_SSR32( int32_t a, int8_t s){<!-- -->
    __asm__ ("sarl %1, %0\n\t"
         : "+r" (a)
         : "c" ((uint8_t)(-s))
    );
    return a;
}

#define NEG_USR32 NEG_USR32
static inline uint32_t NEG_USR32(uint32_t a, int8_t s){<!-- -->
    __asm__ ("shrl %1, %0\n\t"
         : "+r" (a)
         : "c" ((uint8_t)(-s))
    );
    return a;
}

```
