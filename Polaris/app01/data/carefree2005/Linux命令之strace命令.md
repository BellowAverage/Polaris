
--- 
title:  Linux命令之strace命令 
tags: []
categories: [] 

---
## 一、命令简介

  strace是一个有用的诊断、指导和调试工具。系统管理员、诊断专家和故障解决人员将发现，对于解决源代码不易获得的程序的问题，这是非常宝贵的，因为它们不需要重新编译以跟踪它们。学生、黑客和过分好奇的人会发现，通过跟踪甚至是普通程序，可以了解到大量关于系统及其系统调用的信息。程序员会发现，由于系统调用和信号是发生在用户/内核界面上的事件，因此仔细检查该边界对于错误隔离、健全性检查和尝试捕获竞争条件非常有用。strace运行时它拦截并记录进程调用的系统调用和进程接收的信号。每个系统调用的名称、参数及其返回值都打印在标准错误上或打印到使用-o选项指定的文件中。

## 二、使用示例

### 1、命令安装

>  
 [root@s142 ~]# yum install -y strace 


### 2、查看命令版本

>  
 [root@s142 ~]# strace -V strace – version 4.24 … 


### 3、获取命令帮助

>  
 [root@s142 ~]# strace -h usage: strace [-CdffhiqrtttTvVwxxy] [-I n] [-e expr]… … 


### 4、strace跟踪ls -h命令

  直接在命令前面加上strace命令就可以跟踪命令的执行过程了，会详细的显示命令过程中执行的命令、系统调用、进程接收的信号等。 <img src="https://img-blog.csdnimg.cn/aa93e92ef357403297b39cb2671090c2.png" alt="在这里插入图片描述">

>  
 [root@s142 ~]# strace ls -h execve(“/usr/bin/ls”, [“ls”, “-h”], 0x7ffcb2bef228 /* 25 vars */) = 0 brk(NULL) 


### 5、strace命令跟踪统计结果简洁显示

  使用-c参数可以显示strace命令的统计结果，显示命令执行了哪些系统调用信号、耗时、各系统调用次数等。 <img src="https://img-blog.csdnimg.cn/44471865d72a41a49d0372a14bcabf4c.png" alt="在这里插入图片描述">

>  
 [root@s142 ~]# strace -c ls -h anaconda-ks.cfg % time seconds usecs/call calls errors syscall 


### 6、查看open调用类型

  strace默认查看所有调用信号，使用-e参数可以查看指定类型的调用，减少输出信息。支持的信号包括：trace, abbrev, verbose, raw, signal, read, write, fault, inject, kvm等。

>  
 [root@s142 ~]# strace -e open ls -h open(“/etc/ld.so.cache”, O_RDONLY|O_CLOEXEC) = 3 open(“/lib64/libselinux.so.1”, O_RDONLY|O_CLOEXEC) = 3 open(“/lib64/libcap.so.2”, O_RDONLY|O_CLOEXEC) = 3 open(“/lib64/libacl.so.1”, O_RDONLY|O_CLOEXEC) = 3 open(“/lib64/libc.so.6”, O_RDONLY|O_CLOEXEC) = 3 open(“/lib64/libpcre.so.1”, O_RDONLY|O_CLOEXEC) = 3 open(“/lib64/libdl.so.2”, O_RDONLY|O_CLOEXEC) = 3 open(“/lib64/libattr.so.1”, O_RDONLY|O_CLOEXEC) = 3 open(“/lib64/libpthread.so.0”, O_RDONLY|O_CLOEXEC) = 3 open(“/usr/lib/locale/locale-archive”, O_RDONLY|O_CLOEXEC) = 3 anaconda-ks.cfg +++ exited with 0 +++ 


### 7、显示时间戳

  strace输出默认是没有时间信息的，使用-t或者-tt参数我们可以打印命令执行的时间，精确到毫秒。 <img src="https://img-blog.csdnimg.cn/e6d97a0890f34c26a04291fd8cb46ba2.png" alt="在这里插入图片描述">

>  
 [root@s142 ~]# strace -t -e open ls -h 03:23:18 open(“/etc/ld.so.cache”, O_RDONLY|O_CLOEXEC) = 3 03:23:18 open(“/lib64/libselinux.so.1”, O_RDONLY|O_CLOEXEC) = 3 


### 8、将strace结果输出到指定文件

  如果希望保存strace命令执行的结果，我们可以使用-o参数将内容输出到指定文件。 <img src="https://img-blog.csdnimg.cn/d604b993b1964052a8f2ef31b538fb96.png" alt="在这里插入图片描述">

>  
 [root@s142 ~]# strace -t -o /tmp/strace-ls.log ls -h anaconda-ks.cfg [root@s142 ~]# cat /tmp/strace-ls.log 03:25:02 execve(“/usr/bin/ls”, [“ls”, “-h”], 0x7fff28de1af0 /* 25 vars */) = 0 


### 9、跟踪正在运行的进程

  如果是排查已经正在运行的进程的问题，我们可以使用-p参数跟踪指定进程的系统信号调用。 <img src="https://img-blog.csdnimg.cn/6d8760fc97d34a95831944d2eae8f3ca.png" alt="在这里插入图片描述">

>  
 [root@s142 ~]# sh test.sh &amp; [1] 5859 [root@s142 ~]# 开始测试  [root@s142 ~]# strace -t -e trace=process -f -p 5859 strace: Process 5859 attached 03:38:58 wait4(-1, [{WIFEXITED(s) &amp;&amp; WEXITSTATUS(s) == 0}], 0, NULL) = 5860 


## 三、使用语法及参数说明

### 1、使用语法

>  
 用法：strace [参数] 命令 [命令参数] 


### 2、参数说明

<th align="left">参数</th><th align="left">参数类型</th><th align="left">参数说明</th>
|------
<td align="left">-a column</td><td align="left">输出格式参数</td><td align="left">用于打印系统调用结果的对齐列（默认为40）</td>
<td align="left">-i</td><td align="left">输出格式参数</td><td align="left">在系统调用时打印指令指针</td>
<td align="left">-k</td><td align="left">输出格式参数</td><td align="left">获取每个系统调用之间的堆栈跟踪</td>
<td align="left">-o file</td><td align="left">输出格式参数</td><td align="left">将跟踪输出发送到文件而不是stderr</td>
<td align="left">-q</td><td align="left">输出格式参数</td><td align="left">抑制有关附加、分离等的消息。</td>
<td align="left">-r</td><td align="left">输出格式参数</td><td align="left">打印相对时间戳</td>
<td align="left">-s strsize</td><td align="left">输出格式参数</td><td align="left">将打印字符串的长度限制为STRSIZE字符（默认为32）</td>
<td align="left">-t</td><td align="left">输出格式参数</td><td align="left">打印绝对时间戳</td>
<td align="left">-tt</td><td align="left">输出格式参数</td><td align="left">使用usecs打印绝对时间戳</td>
<td align="left">-T</td><td align="left">输出格式参数</td><td align="left">打印每个系统调用花费的时间</td>
<td align="left">-x</td><td align="left">输出格式参数</td><td align="left">以十六进制打印非ascii字符串</td>
<td align="left">-xx</td><td align="left">输出格式参数</td><td align="left">以十六进制打印所有字符串</td>
<td align="left">-X format</td><td align="left">输出格式参数</td><td align="left">设置打印命名常量和标志的格式</td>
<td align="left">-y</td><td align="left">输出格式参数</td><td align="left">与文件描述符参数关联的打印路径</td>
<td align="left">-yy</td><td align="left">输出格式参数</td><td align="left">打印与套接字文件描述符关联的协议特定信息</td>
<td align="left">-c</td><td align="left">统计参数</td><td align="left">统计每个系统调用的时间、调用和错误，并报告摘要</td>
<td align="left">-C</td><td align="left">统计参数</td><td align="left">像-c一样，也可以打印常规输出</td>
<td align="left">-O overhead</td><td align="left">统计参数</td><td align="left">将跟踪系统调用的开销设置为开销usecs</td>
<td align="left">-S sortby</td><td align="left">统计参数</td><td align="left">按以下方式对系统调用计数排序：时间、调用、名称、无（默认时间）</td>
<td align="left">-w</td><td align="left">统计参数</td><td align="left">统计系统调用延迟（默认为系统时间）</td>
<td align="left">-e expr</td><td align="left">过滤参数</td><td align="left">限定表达式，表达式值可以是trace, abbrev, verbose, raw, signal, read, write, fault, inject, kvm</td>
<td align="left">-P path</td><td align="left">过滤参数</td><td align="left">跟踪访问路径</td>
<td align="left">-b execve</td><td align="left">跟踪参数</td><td align="left">执行系统调用时分离</td>
<td align="left">-D</td><td align="left">跟踪参数</td><td align="left">将跟踪进程作为分离的子进程运行，而不是作为父进程运行</td>
<td align="left">-f</td><td align="left">跟踪参数</td><td align="left">跟着叉子走</td>
<td align="left">-ff</td><td align="left">跟踪参数</td><td align="left">跟随分叉，输出到单独的文件中</td>
<td align="left">-I interruptible</td><td align="left">跟踪参数</td><td align="left">可中断信号1： 没有信号被阻塞2： 解码系统调用时阻止致命信号（默认）3： 致命信号始终被阻止（默认情况下为“-o FILE PROG”）4： 致命信号和SIGTSTP（^Z）始终被阻止</td>
<td align="left">-E var</td><td align="left">启动参数</td><td align="left">从命令的环境中删除var</td>
<td align="left">-E var=val</td><td align="left">启动参数</td><td align="left">将var=val放在命令的环境中</td>
<td align="left">-p pid</td><td align="left">启动参数</td><td align="left">id为pid的pid跟踪进程，可以重复</td>
<td align="left">-u username</td><td align="left">启动参数</td><td align="left">处理setuid和/或setgid的用户名运行命令</td>
<td align="left">-d</td><td align="left"></td><td align="left">启用调试输出到stderr</td>
<td align="left">-v</td><td align="left"></td><td align="left">详细模式：打印未修改的argv、stat、termios等参数</td>
<td align="left">-h</td><td align="left"></td><td align="left">打印帮助信息</td>
<td align="left">-V</td><td align="left"></td><td align="left">打印版本信息</td>
<td align="left">-d</td><td align="left">其他参数</td><td align="left">启用调试输出到stderr</td>
<td align="left">-v</td><td align="left">其他参数</td><td align="left">详细模式：打印未修改的argv、stat、termios等参数</td>
<td align="left">-h</td><td align="left">其他参数</td><td align="left">打印帮助信息</td>
<td align="left">-V</td><td align="left">其他参数</td><td align="left">打印版本信息</td>
