
--- 
title:  Error: impossible constraint in ‘asm‘ 
tags: []
categories: [] 

---
### 错误如下：

我在windows下编译ffmpeg源码时，出现了如下的错误：

```
./libavcodec/x86/mathops.h:127:5: warning: 'asm' operand 1 probably does not match constraints
  127 |     __asm__ ("shrl %1, %0\n\t"
      |     ^~~~~~~
./libavcodec/x86/mathops.h:127:5: error: impossible constraint in 'asm'
make: *** [ffbuild/common.mak:60：libavformat/adtsenc.o] 错误 1
make: *** 正在等待未完成的任务....
CC      libavformat/anm.o
In file included from ./libavutil/common.h:488,
                 from ./libavutil/avutil.h:296,
                 from ./libavutil/samplefmt.h:24,
                 from ./libavcodec/avcodec.h:31,
                 from libavformat/avformat.h:319,
                 from libavformat/anm.c:28:


```

### 解决：

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

具体可查看下面这篇文章：
