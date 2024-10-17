
--- 
title:  k8s 使用bash -c报错 
tags: []
categories: [] 

---
#### 问题描述：
- 使用了kubecl exec -it – grep报错- 普通的ls或者ps -ef能够成功执行，但是其他的命令有概率无法正常执行，提前报错退出- 报错信息为
>  
 command terminated with exit code 1 command terminated with exit code 127 


#### 解决方案

使用管道替换标准bash

```
echo “&lt;实际需要执行的命令&gt;;exit”|kubecl exec -i  &lt;容器的名称&gt; --bash

```

细节：
- 当不加入exit的时候，命令并不会正常退出，而是一直等待。当执行完成命令后需要加入一个exit让命令结束释放链接- 不能使用 exec -it，而是使用-i，-t会提示无法获取到tty失败