
--- 
title:  动态分析C语言代码生成函数调用关系的利器——perf 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>- - - - - - 


perf是一套linux操作系统上分析工具集，分析函数调用关系只是其一个子集功能。它并不像中介绍的需要在被分析程序的编译指令中插入新的选项（-pg），而是直接对原始编译结果进行分析。

## 环境准备

### 安装

perf工具集并不默认安装在系统中，需要进行安装。（找到你系统匹配的版本，我的是linux-tools-5.15.0-91-generic）

```
sudo apt install linux-tools-common linux-tools-5.15.0-91-generic

```

### 开启监控

```
sudo sysctl kernel.perf_event_paranoid=-1

```

否则会报以下错误

>  
 Error: Access to performance monitoring and observability operations is limited. Consider adjusting /proc/sys/kernel/perf_event_paranoid setting to open access to performance monitoring and observability operations for processes without CAP_PERFMON, CAP_SYS_PTRACE or CAP_SYS_ADMIN Linux capability. More information can be found at ‘Perf events and tool security’ document: https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html perf_event_paranoid setting is 4: -1: Allow use of (almost) all events by all users Ignore mlock limit after perf_event_mlock_kb without CAP_IPC_LOCK = 0: Disallow raw and ftrace function tracepoint access = 1: Disallow CPU event access = 2: Disallow kernel profiling To make the adjusted perf_event_paranoid setting permanent preserve it in /etc/sysctl.conf (e.g. kernel.perf_event_paranoid = ) 


## 分析

我们以中libevent的test-time为例。这次我们只要直接编译出可执行程序即可。

```
gcc `find . -regextype posix-extended -regex '^./[^/]*\.c$' ! -name 'wepoll.c' ! -name 'win32select.c' ! -name 'evthread_win32.c' ! -name 'buffer_iocp.c' ! -name 'bufferevent_async.c' ! -name 'arc4random.c' ! -name 'event_iocp.c' ! -name 'bufferevent_mbedtls.c'` \
 ./test/test-time.c \
 -I./build/include/ -I./include -I./ \
 -L./build/lib/ -lcrypto -lssl \
 -DLITTLE_ENDIAN -D__clang__ \
 -UD_WIN32 -UDMBEDTLS_SSL_RENEGOTIATION \
 -o test-time

```

### 采集

```
sudo perf record -g -- ./test-time

```

-g 指令是用于开启记录调用关系。

>  
 [ perf record: Woken up 12 times to write data ] [ perf record: Captured and wrote 4.786 MB perf.data (34448 samples) ] 


### 解析

script工具将上步采集的信息转换成文本。

```
sudo perf script &gt; test-time-perf.output

```

## 可视化处理

### 环境准备

```
sudo apt-get install graphviz

```

### 转换成dot

然后使用中的脚本构建虚拟环境，并安装gprof2dot

```
source env.sh init
source env.sh enter
source env.sh install gprof2dot

```

执行下面指令将文本转换成dot格式

```
gprof2dot test-time-perf.output -f perf&gt; test-time-per.dot

```

### 转换为图片

```
dot test-time-perf.dot -Tpng -o test-time-perf.png

```

<img src="https://img-blog.csdnimg.cn/direct/dae3a185640c41f29ae000c1511b6f9a.png" alt="请添加图片描述">

## 参考资料
- - - 