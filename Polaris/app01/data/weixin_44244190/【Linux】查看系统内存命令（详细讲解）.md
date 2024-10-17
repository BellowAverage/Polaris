
--- 
title:  【Linux】查看系统内存命令（详细讲解） 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>查看系统内存命令（详细讲解）</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - -  
  
  


在Linux系统中，有多种方法可以监控内存使用情况。以下是一些常用的方法和工具：

## Linux内存查看命令
1. **free命令** `free` 命令是最常用的显示系统内存使用情况的命令之一。
```
free -h

```

这将以人类可读的方式（如MB、GB）显示内存使用情况。
1. **/proc/meminfo** `/proc/meminfo` 文件包含了系统的内存信息。你可以使用 `cat` 命令来查看它。
```
cat /proc/meminfo

```
1. **top和htop命令** `top` 是一个实时的系统状态观察器。启动 `top` 后，它会在屏幕顶部显示总体内存使用情况。
```
top

```

`htop` 是 `top` 的一个增强版本，它提供了一个彩色的界面以及更多的功能。你可能需要先安装 `htop` 才能使用它：

```
sudo apt install htop    # Debian/Ubuntu系统
sudo yum install htop    # Red Hat/CentOS系统

```

然后，运行：

```
htop

```
1. **vmstat命令** `vmstat` 命令提供了关于进程、内存、分页、块IO、中断和CPU活动的信息。
```
vmstat

```
1. **sar命令** `sar` 命令用于收集和报告系统活动信息。你可以使用以下命令查看内存使用情况：
```
sar -r

```

要使用 `sar`，你可能需要首先安装 `sysstat` 软件包。
1. **使用监控工具** 有一些外部的监控工具（如 Nagios、Zabbix、Prometheus、Grafana）也可以帮助你监控系统的内存使用情况。
以上只是Linux内存监控的一些基础方法，还有许多高级工具和技术可以更详细地分析系统的内存使用情况。

## shell脚本监控内存

要使用shell脚本编写一个简单的实时监控功能，通常会结合 `watch` 命令或者使用无限循环 (`while true`) 并使用 `sleep` 命令来实现间隔监控。
1. 使用 `watch` 命令：
```
watch free -h

```

`watch` 命令会每2秒执行一次 `free -h`，所以你会看到内存使用情况每2秒更新一次。
1. 使用 shell 脚本和 `while true` 循环：
```
#!/bin/bash

while true; do
    clear
    free -h
    sleep 2   # 休眠2秒
done

```

保存上述内容到一个文件，例如 `memory_monitor.sh`，然后赋予其执行权限，并执行它：

```
chmod +x memory_monitor.sh
./memory_monitor.sh

```

这个脚本会无限循环，每2秒刷新并显示内存的当前使用情况。

请注意：在生产环境中，对于长时间或复杂的监控任务，建议使用专门的监控工具（如 Nagios、Zabbix、Prometheus 等）进行处理，因为它们提供了更加完善和高级的功能。
