
--- 
title:  Linux命令之dpkg命令 
tags: []
categories: [] 

---
## 一、dpkg命令简介

  “dpkg ”是“Debian Packager ”的简写。为 “Debian” 专门开发的套件管理系统，方便软件的安装、更新及移除。所有源自“Debian”的“Linux ”发行版都使用 “dpkg”，例如 “Ubuntu”、“Knoppix ”等。dpkg是Debian软件包管理器的基础，它被伊恩·默多克创建于1993年。dpkg与RPM十分相似，同样被用于安装、卸载和供给.deb软件包相关的信息。dpkg本身是一个底层的工具。上层的工具，如APT，被用于从远程获取软件包以及处理复杂的软件包关系。 “dpkg”字母分别是d：Debian，p：package，k：keeprule，g：generate，dpkg是“Debian Package Keeprule Generate”的简写。

## 二、命令使用示例

### 1、获取命令帮助

>  
 root@test:~# dpkg --help <img src="https://img-blog.csdnimg.cn/direct/2f2c407b11304c5d8d2640509437130c.png" alt="在这里插入图片描述"> 


### 2、查看命令版本

>  
 root@test:~# dpkg --version Debian dpkg 软件包管理程序 1.19.7 (amd64) 版。 本软件是自由软件；要获知复制该软件的条件，请参阅 GNU 公共许可证 第二版或其更新的版本。本软件【不】提供任何担保。 


### 3、-i安装deb包

  使用-i或者–install参数安装指定的deb软件包，dpkg命令与rpm包管理器一样，需要手动解决依赖，如果遇到依赖包未安装会报错并终止安装。

>  
 root@test:/opt# dpkg -i elpa-simple-httpd_1.5.1-5_all.deb <img src="https://img-blog.csdnimg.cn/direct/39ac8a1ac49f41d28c44fdeb65542c55.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/6578a515a4e34887b60aec8a58b94fbf.png" alt="在这里插入图片描述"> 


### 4、-l列出所有已安装软件包

  dpkg -l命令列出所有已安装的软件包，如果后面跟上包名则表示简明地列出软件包的状态。

>  
 root@test:/opt# dpkg -l <img src="https://img-blog.csdnimg.cn/direct/493c6412acd94900b6b27c27772d7a43.png" alt="在这里插入图片描述"> 


### 5、-L列出已安装软件包列表

>  
 root@test:/opt# dpkg -L vim <img src="https://img-blog.csdnimg.cn/direct/8a74d725087d4e06a7049c19a5491202.png" alt="在这里插入图片描述"> 


### 6、-s显示已安装软件包的详细信息

>  
 root@test:/opt# dpkg -s vim <img src="https://img-blog.csdnimg.cn/direct/0c68be9d5fa64ef6ae9470faad5af99e.png" alt="在这里插入图片描述"> 


### 7、-S查询一个文件属于哪个软件包

>  
 root@test:/opt# dpkg -S httpd <img src="https://img-blog.csdnimg.cn/direct/5fa1baef15dd4b3597fc2559f1295786.png" alt="在这里插入图片描述"> 


### 8、-r卸载一个软件包

>  
 root@test:/opt# dpkg -r wget <img src="https://img-blog.csdnimg.cn/direct/da234588f7034fba840f1bf430e84998.png" alt="在这里插入图片描述"> 


### 9、-P完成删除一个软件包及配置

>  
 root@test:/opt# dpkg -P elpa-simple-httpd (正在读取数据库 … 系统当前共安装有 231637 个文件和目录。) 正在卸载 elpa-simple-httpd (1.5.1-5) … 


### 10、-V验证软件包是否安装

  使用-V验证软件包是否被安装，这里要求包名是完整的，比如这里安装完成elpa-simple-httpd之后验证httpd还是会提示未安装。

>  
 root@test:/opt# dpkg -V elpa-simple-httpd dpkg: 软件包 elpa-simple-httpd 没有被安装 


## 三、使用语法及参数简介

### 1、使用语法

>  
 用法：dpkg [&lt;选项&gt; …] &lt;命令&gt; 


### 2、参数简介

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-i</td><td align="left">安装软件包。</td>
<td align="left">-r</td><td align="left">删除软件包。</td>
<td align="left">-P</td><td align="left">完全删除软件包，包括配置文件。</td>
<td align="left">-l</td><td align="left">列出已安装的软件包。</td>
<td align="left">-s</td><td align="left">显示软件包的详细信息。</td>
<td align="left">-L</td><td align="left">列出软件包的文件列表。</td>
<td align="left">-S</td><td align="left">查找指定文件属于哪个软件包。</td>
<td align="left">-c</td><td align="left">显示软件包的内容列表。</td>
<td align="left">-G</td><td align="left">忽略版本早于已安装软件版本的的软件包。</td>
<td align="left">-I</td><td align="left">显示软件包的详细信息，包括依赖关系。</td>
<td align="left">-C</td><td align="left">检查是否有软件包残损。</td>
<td align="left">-l</td><td align="left">列出软件包的状态。</td>
<td align="left">-R</td><td align="left">重新配置软件包。</td>
<td align="left">-V</td><td align="left">验证软件包的完整性。</td>
<td align="left">-B</td><td align="left">构建二进制软件包。</td>
<td align="left">-b</td><td align="left">构建源代码软件包。</td>
<td align="left">–get-selections</td><td align="left">把已选中的软件包列表打印到标准输出。</td>
<td align="left">–set-selections</td><td align="left">从标准输入里读出要选择的软件。</td>
<td align="left">–clear-selections</td><td align="left">取消选中所有不必要的软件包。</td>
<td align="left">–update-avail</td><td align="left">替换现有可安装的软件包信息。</td>
<td align="left">–merge-avail</td><td align="left">把文件中的信息合并到系统中。</td>
<td align="left">–clear-avail</td><td align="left">清除现有的软件包信息。</td>
<td align="left">–forget-old-unavail</td><td align="left">忘却已被卸载的不可安装的软件包。</td>
<td align="left">–yet-to-unpack</td><td align="left">列出标记为待解压的软件包。</td>
<td align="left">–predep-package</td><td align="left">列出待解压的预依赖。</td>
<td align="left">–add-architecture &lt;体系结构&gt;</td><td align="left">添加 &lt;体系结构&gt; 到体系结构列表。</td>
<td align="left">–remove-architecture &lt;体系结构&gt;</td><td align="left">从架构列表中移除 &lt;体系结构&gt;。</td>
<td align="left">–print-architecture</td><td align="left">显示 dpkg 体系结构。</td>
<td align="left">–print-foreign-architectures</td><td align="left">显示已启用的异质体系结构。</td>
<td align="left">–assert-&lt;特性&gt;</td><td align="left">对指定特性启用断言支持。</td>
<td align="left">–validate-&lt;属性&gt; &lt;字符串&gt;</td><td align="left">验证一个 &lt;属性&gt;的 &lt;字符串&gt;。</td>
<td align="left">–compare-vesions &lt;a&gt; &lt;关系&gt; &lt;b&gt;</td><td align="left">比较版本号 - 见下。</td>
<td align="left">–force-help</td><td align="left">显示本强制选项的帮助信息。</td>
<td align="left">-Dh</td><td align="left">–debug=help</td>
<td align="left">-?, --help</td><td align="left">显示本帮助信息。</td>
<td align="left">–version</td><td align="left">显示版本信息。</td>

## 四、总结

  dpkg命令参数很多，实际运维工作中我们很少使用dpkg命令安装软件包，更多使用的是apt-get命令安装，apt可以自动解决依赖包的问题。dpkg命令主要用安装/etc/apt/sources.list源中找不到的软件包，比如安全厂商的vpn、系统厂商自研的软件包等。dpkg命令我们只需要记住常用的dpkg -i安装软件包，dpkg -r卸载软件包，dpkg -l列出软件包，dpkg -S查找软件包即可。另外还有一个就是dpkg -i前先确认包是否已经安装，如果已经安装执行了该命令之后如果出现错误可能导致包无法使用。这个时候我们可以使用apt --fix-broken install修复已经安装的软件包。 <img src="https://img-blog.csdnimg.cn/direct/57132ce1290e4fada3cee1405154a444.png" alt="在这里插入图片描述">
