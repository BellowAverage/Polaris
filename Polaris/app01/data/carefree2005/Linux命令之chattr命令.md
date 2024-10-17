
--- 
title:  Linux命令之chattr命令 
tags: []
categories: [] 

---
## 一、chattr命令简介

  chattr命令用于更改文件或目录的属性，包括不可修改属性、同步属性、追加属性、无尽属性、压缩属性、无尽属性、不可删除属性等。chattr命令只能由超级用户或文件的所有者使用。

## 二、chattr命令使用示例

### 1、给文件设置版本

  -v参数设置版本信息只在extX（ext4…）文件系统下支持，xfs文件系统设置文件版本时会报错对设备不适当的 ioctl 操作。

>  
 [root@s153 ~]# chattr -v 2 -V hi.txt chattr 1.41.12 (17-May-2010) hi.txt的标志被设为 -------------e- Version of hi.txt set as 2 [root@s152 test]# chattr -v 2 -V a.txt chattr 1.42.9 (28-Dec-2013) a.txt的标志被设为 ---------------- Version of a.txt set as 2 chattr: 对设备不适当的 ioctl 操作 while setting version on a.txt 


### 2、递归设置目录下文件属性

>  
 [root@s152 test]# chattr -R -a -V level1-1/ chattr 1.42.9 (28-Dec-2013) level1-1/的标志被设为 ---------------- level1-1//level2-1的标志被设为 ---------------- level1-1//level2-2的标志被设为 ---------------- level1-1//level2-2/ccc.txt的标志被设为 ---------------- level1-1//level2-3的标志被设为 ---------------- level1-1//bb.txt的标志被设为 ---------------- 


### 3、使用-V参数显示指令执行过程

>  
 [root@s152 test]# chattr -R -a -V level1-1 chattr 1.42.9 (28-Dec-2013) level1-1的标志被设为 ---------------- level1-1/level2-1的标志被设为 ---------------- level1-1/level2-2的标志被设为 ---------------- level1-1/level2-2/ccc.txt的标志被设为 ---------------- level1-1/level2-3的标志被设为 ---------------- level1-1/bb.txt的标志被设为 ---------------- 


### 4、增加一个属性

>  
 [root@s152 test]# lsattr a.txt ---------------- a.txt [root@s152 test]# chattr +i a.txt [root@s152 test]# lsattr a.txt ----i----------- a.txt 


### 5、删除一个属性

>  
 [root@s152 test]# chattr -i -V a.txt chattr 1.42.9 (28-Dec-2013) a.txt的标志被设为 ---------------- [root@s152 test]# lsattr a.txt ---------------- a.txt 


### 6、指定文件属性

  使用=指定文件的属性，实际上文件支持的各属性之间有部分是冲突的，所以很少用到=参数来指定属性，常用±参数来增加或者减少一个属性。

>  
 [root@s152 test]# chattr =iaA -V a.txt chattr 1.42.9 (28-Dec-2013) a.txt的标志被设为 ----ia-A-------- 


## 三、chattr命令语法及参数说明

### 1、命令语法

>  
 #chattr [参数] 文件或者目录 #chattr ±=[属性] 文件或者目录 #chattr [参数] [属性] 文件或者目录 


### 2、参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-R</td><td align="left">递归处理，将指令目录下的所有文件及子目录一并处理</td>
<td align="left">-v&lt;版本编号&gt;</td><td align="left">设置文件或目录版本，此参数只适用于extx文件系统</td>
<td align="left">-V</td><td align="left">显示指令执行过程</td>
<td align="left">-f</td><td align="left">抑制大多数错误信息</td>
<td align="left">+&lt;属性&gt;</td><td align="left">开启文件或目录的该项属性</td>
<td align="left">-&lt;属性&gt;</td><td align="left">关闭文件或目录的该项属性</td>
<td align="left">=&lt;属性&gt;</td><td align="left">指定文件或目录的该项属性</td>

### 3、属性说明

  当前主流Linux内核中实现的ext2、ext3和ext4文件系统不支持“c”、“s”和“u”属性。实际上这些属性中常用只有a和i，追加属性长用于日志文件，保证日志文件不会被删除，只允许追加日志记录；i属性用于锁定重要的配置文件，避免误删除或者修改等。

<th align="left">属性</th><th align="left">属性说明</th>
|------
<td align="left">a</td><td align="left">该属性只允许在文件末尾添加数据，不允许修改或删除文件的内容。</td>
<td align="left">A</td><td align="left">设置该属性时，文件atime时间不再更新。</td>
<td align="left">c</td><td align="left">默认将文件或目录进行压缩。</td>
<td align="left">C</td><td align="left">设置了“C”属性的文件将不会进行写时复制更新。只有在执行写时复制的文件系统上才支持此标志</td>
<td align="left">d</td><td align="left">当进行文件系统备份时，不备份该文件或目录。</td>
<td align="left">D</td><td align="left">当修改具有“D”属性集的目录时，更改将同步写入磁盘；这相当于应用于文件子集的“dirsync”装载选项。要求内核版本2.5.19以上</td>
<td align="left">i</td><td align="left">禁止对文件或目录进行任何修改操作，包括修改、删除、重命名等。</td>
<td align="left">j</td><td align="left">允许文件系统支持日志功能，只在ext3、ext4环境下支持。</td>
<td align="left">s</td><td align="left">当文件被删除时，将其内容清零。</td>
<td align="left">S</td><td align="left">当修改具有“S”属性集的文件时，更改将同步写入磁盘；这相当于应用于文件子集的“sync”装载选项</td>
<td align="left">t</td><td align="left">让文件系统支持尾部合并（tail-merging），只有ext2和ext3支持尾部合并</td>
<td align="left">T</td><td align="left">具有“T”属性的目录将被视为目录层次结构的顶部。这是对ext3和ext4使用的块分配器的一个提示。</td>
<td align="left">u</td><td align="left">删除具有“u”属性集的文件时，将保存其内容。这允许用户请求取消删除。</td>

## 四、chattr命令使用实践

### 1、使用i属性锁定/etc/shadow文件，保证系统用户安全

  使用i属性锁定文件后即使是root用户也无法直接删除、修改、更新，需要先解锁才可以对文件进行操作。编辑被i锁定的文件会提示是只读文件，即使使用wr!也无法完成保存，对文件的任何更新、修改操作都必须再解锁后执行。我们在完成操作系统用户等配置之后，可以锁定/etc/shadow文件，用于保障系统账户安全。 <img src="https://img-blog.csdnimg.cn/1afbbdfe6c9b42009a5fb48e54914a1e.png" alt="在这里插入图片描述">

>  
 [root@s152 test]# chattr +a a.txt [root@s152 test]# rm -rf a.txt rm: 无法删除"a.txt": 不允许的操作 [root@s152 test]# echo “This is add message test” &gt;&gt; a.txt -bash: a.txt: 权限不够 [root@s152 test]# vim a.txt 


### 2、使用a属性锁定/var/log/messages，防止日志文件被篡改

  使用a属性控制/var/log/messages文件只能追加，不允许删除、覆盖等操作，可以保证系统日志的的安全。 <img src="https://img-blog.csdnimg.cn/bfb9f78a43f54a4fb1f76fd6753cded0.png" alt="在这里插入图片描述">

>  
 [root@s152 test]# chattr +a /var/log/messages [root@s152 test]# lsattr /var/log/messages -----a---------- /var/log/messages 

