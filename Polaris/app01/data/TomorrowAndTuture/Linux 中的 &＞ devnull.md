
--- 
title:  Linux 中的 &＞ /dev/null 
tags: []
categories: [] 

---
**其实，简单理解的话：command &gt; /dev/null 2&gt;&amp;1 和 command &amp;&gt; /dev/null 是一样的。**

**专业点解释就是：将标准错误重定向到标准输出，然后将标准输出（标准错误和标准输出）重定向到 黑洞（/dev/null）！**

**简单点理解就是：把命令的标准输出和标准错误全都扔了！**

### **command &gt; /dev/null 2&gt;&amp;1**：

```
[root@master ~]# ll no_exist.txt
ls: cannot access no_exist.txt: No such file or directory
[root@master ~]# ll no_exist.txt &gt; /dev/null
ls: cannot access no_exist.txt: No such file or directory
[root@master ~]# ll no_exist.txt &gt; /dev/null 2&gt;&amp;1

```

### **command &amp;&gt; /dev/null**：

```
[root@master ~]# ll no_exist.txt
ls: cannot access no_exist.txt: No such file or directory
[root@master ~]# ll no_exist.txt &gt; /dev/null
ls: cannot access no_exist.txt: No such file or directory
[root@master ~]# ll no_exist.txt &amp;&gt; /dev/null

```

**当然，如果你想把标准输出和标准错误保存下来的话，/dev/null 也可以替换成具体的输出文件。**

### **在 python3 的 subprocess 里边对应的语法：**

**先贴个官网的链接：**

你可以把下面的 ”=“ 理解为重定向。

```
import subprocess

subprocess.run(['command', 'param1', 'param2', 'param...'],
               stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL)
```

像 subprocess.Popen 也是类似的：

```
popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
```

 

这样的话，你就不用再写 os.system() （**好多项目会觉得这个命令比较危险，写上的话基本上会被毙掉的！**）了：

```
import os

os.system('command param1 param2 param... &amp;&gt; /dev/null')


# import subprocess
# subprocess.getstatusoutput('command param1 param2 param... &amp;&gt; /dev/null')

```


