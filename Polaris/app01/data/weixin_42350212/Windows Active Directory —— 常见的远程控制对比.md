
--- 
title:  Windows Active Directory —— 常见的远程控制对比 
tags: []
categories: [] 

---
<img alt="" height="374" src="https://img-blog.csdnimg.cn/fe4471738fea4b7580b225409c139df7.png" width="942">





在windows环境中，需要远程访问的时候很多，使用的工具和命令也各式各样，我把自己常用的命令和工具总结一下

 远程访问方式：

1）对服务器而言，RDP这个绝对是最常见的方式，mstsc /v:remoteserver 即可打开

 2）winrs和winrm，这个可以允许我们通过命令行来远程访问，远程服务器上winrm quickconfig,会自动配置listener并打开对应的防火墙端口。例如 从服务器A访问B，那么直接 winrs -r:serverB ipconfig 就可以看见服务器B的IP了

 3）powershell 这个我觉得就是winrs和winrm的升级版，比如在2012里面，远程服务器上运行enable-psremoting，他会自动调用了 Set-WSManQuickConfig这个命令（等同于上面的winrm quickconfig），然后客户端使用Enter-pssession -computername server就可以建立远程的powershell的会话了。如果只是运行一个命令，也可以使用invoke-command -ComputerName server -ScriptBlock {ipconfig} 执行一次性的操作，效果类似上面的winrs -r:server ipconfig

 4）还有一个常见的命令行的工具是psexec, 这个属于pstool里面的一个，pstool压缩包可以从sysinternal官网下载。这个工具
