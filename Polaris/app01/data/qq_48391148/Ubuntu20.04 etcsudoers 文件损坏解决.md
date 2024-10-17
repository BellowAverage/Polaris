
--- 
title:  Ubuntu20.04 /etc/sudoers 文件损坏解决 
tags: []
categories: [] 

---
操作：对/etc/sudoers 添加了免密码配置，结果ubuntu里默认sudoers文件只读，修改以后sudo命令也用不了了，想将配置重新修改回去也失败，因为sudoers文件配置错误，sudo命令用不了

```
&gt;&gt;&gt; /etc/sudoers: 语法错误 near line 26 &lt;&lt;&lt;
sudo: /etc/sudoers 中第 26 行附近有解析错误
sudo: 没有找到有效的 sudoers 资源，退出
sudo: 无法初始化策略插件

```

解决方法:使用`pkexec visudo`命令

>  
 在Linux系统中，sudoers文件存储了关于哪些用户或用户组可以以超级用户（root）权限执行特定命令的配置信息。visudo是一个工具，用于编辑sudoers文件，它会对文件进行语法校验，以避免配置错误导致系统安全问题。 
 运行`pkexec visudo`命令后，系统将会提示您输入当前用户的密码进行验证，之后将以root权限打开sudoers文件供您进行编辑。 


```
pkexec visudo

```

将配置文件修改正确之后，ctrl + o 保存  ctrl +x 退出。
