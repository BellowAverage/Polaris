
--- 
title:  SELinux系列（十八）—策略规则的开启和关闭（详解版） 
tags: []
categories: [] 

---
### 查询策略规则是否开启

先来看看如何知道哪些规则是启用的，哪些规则是关闭的。这时需要使用 getsebool 命令，命令格式如下：

```
[root@localhost ~]# getsebool [-a] [规则名]

-a 选项的含义是列出所有规则的开启状态。
```

 例如：

```
[root@localhost ~]# getsebool -a
abrt_anon_write --&gt; off
abrt_handle_event --&gt; off
allow_console_login --&gt; on
allow_cvs_read_shadow --&gt; off
allow_daemons_dump_core --&gt; on
allow_daemons_use_tcp_wrapper --&gt; off
```

 #getsebool命令明确地列出了规则的开启状态

除此之外，还可以使用 `semanage boolean -l` 命令（此命令需事先手动安装），

此命令的输出结构同 getsebool 命令相比，输出信息中多了默认状态、

当前状态以及相关描述等信息。感兴趣的读者，可以自己尝试运行，

观看输出结果。

### 修改规则的开启状态

>  
 能够查询到规则的开启状态，我们使用 setsebool 命令就可以开启和关闭某个规则。当然，我们先应该通过 sesearch 命令确认这个规则的作用。 sesearch 命令格式如下： 
 [root@localhost ~]# setsebool [-P] 规则名=[0|1] 


-P 选项的含义是将改变写
