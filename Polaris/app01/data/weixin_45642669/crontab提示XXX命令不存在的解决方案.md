
--- 
title:  crontab提示XXX命令不存在的解决方案 
tags: []
categories: [] 

---
## 环境变量有问题
- 在一个新的ssh接入的时候，需要加载一个配置文件。 但是crontab执行的时候不导入这个配置文件，导致环境变量和实际crontab环境变量不同，导致出现类似： XXX命令不存在。- 工作目录不一致，导致无法进入程序
  解决方案：
- 导入Java的时候不用java 而是 /usr/bin/java,使用绝对地址而不是相对地址,不依赖env + path进行查找
whereis查询命令，然后将代码里面所有的相对地址转化为绝对地址
- 在写crontab的时候绑定cd /&lt;你的工作目录的绝对地址&gt;；
或者：
- 将自身的依赖的环境变量 + 工作目录导出到source，然后启动之前加载这个source