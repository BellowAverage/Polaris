
--- 
title:  Linux命令之tree命令 
tags: []
categories: [] 

---
## 一、tree命令简介

  tree命令是一个用于显示目录结构的命令。它可以以树状图的形式展示指定目录下的所有文件和子目录。这个命令并不是很常用，但是在我们统计某个目录下的目录结构还是非常有用的，如果我们需要完整的复制某个目录的目录结构，但是不负责目录下的文件的时候就需要使用到这个命令。

## 二、tree命令使用示例

### 1、查看命令版本

>  
 [root@s152 ~]# tree --version tree v1.6.0 © 1996 - 2011 by Steve Baker, Thomas Moore, Francesc Rocher, Kyosuke Tokoro 


### 2、获取命令帮助

>  
 [root@s152 ~]# tree --help 


### 3、查看目录test目录结构

>  
 [root@s152 ~]# tree test test ├── level1-1 │ ├── level2-1 │ ├── level2-2 │ └── level2-3 ├── level1-2 │ ├── level2-1 │ ├── level2-2 │ └── level2-3 └── level1-3 ├── level2-1 ├── level2-2 └── level2-3  12 directories, 0 files 


### 4、仅显示目录完整路径

  如果我们需要递归获取目录下的整个目录结构，就可以使用如下命令，-f表示打印完整路径;-d表示只打印目录，不打印文件；-i表示省略前面的横线。

>  
 [root@s152 ~]# tree -fid test test test/level1-1 test/level1-1/level2-1 … test/level1-3/level2-3  12 directories 


### 5、不打印统计信息

>  
 [root@s152 ~]# tree --noreport test test ├── a.txt ├── level1-1 │ ├── bb.txt │ ├── level2-1 │ ├── level2-2 │ │ └── ccc.txt │ └── level2-3 … 


### 6、打印inode信息

  inodes参数可以用于打印文件和目录的inodes编号，inodes编号一般用于文件名显示乱码的情况下删除文件使用。可以使用命令#find -inum ****inodes_number**** -delete 命令删除乱码文件。

>  
 [root@s152 ~]# tree --inodes test test ├── [8576899] a.txt ├── [16851797] level1-1 │ ├── [16878307] bb.txt │ ├── [25166001] level2-1 │ ├── [ 303089] level2-2 │ │ └── [ 323552] ccc.txt │ └── [8422822] level2-3 … 12 directories, 3 files 


### 7、打印时过滤空目录

>  
 [root@s152 ~]# tree --prune test <img src="https://img-blog.csdnimg.cn/9d225be8b88e41f0b8a8c18180de1286.png" alt="在这里插入图片描述"> 


### 8、打印展示时打印文件属性、属主、属组

<img src="https://img-blog.csdnimg.cn/602cbfb52b75479e8eb1b18b834d9bc2.png" alt="在这里插入图片描述">

### 9、先打印目录后打印文件

>  
 [root@s152 ~]# tree --dirsfirst test test ├── level1-1 │ ├── level2-1 │ ├── level2-2 │ │ └── ccc.txt │ ├── level2-3 │ └── bb.txt ├── level1-2 … 12 directories, 3 files 


## 三、使用语法及常用参数说明

### 1、使用语法

>  
 #tree [选项] [目录] #tree [选项] [目录] -o filename 


### 2、展示参数说明

  如下表格中的

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-a</td><td align="left">列出所有文件。</td>
<td align="left">-d</td><td align="left">仅列出目录。</td>
<td align="left">-l</td><td align="left">遵循像目录这样的符号链接。</td>
<td align="left">-f</td><td align="left">打印每个文件的完整路径前缀。</td>
<td align="left">-x</td><td align="left">仅停留在当前文件系统上。</td>
<td align="left">-L level</td><td align="left">仅向下级别目录深。</td>
<td align="left">-R</td><td align="left">达到最大目录级别时重新运行树。</td>
<td align="left">-P pattern</td><td align="left">只列出那些与给定模式匹配的文件。</td>
<td align="left">-I pattern</td><td align="left">不列出与给定模式匹配的文件。</td>
<td align="left">--noreport</td><td align="left">关闭树列表末尾的文件/目录计数。</td>
<td align="left">--charset X</td><td align="left">将charset X用于终端/HTML和缩进行输出。</td>
<td align="left">--filelimit #</td><td align="left">目录中的文件数不要超过#。</td>
<td align="left">--timefmt </td><td align="left">根据＜f＞格式打印和格式化时间。</td>
<td align="left">-o filename</td><td align="left">输出到文件而不是stdout。</td>
<td align="left">--du</td><td align="left">打印目录大小。</td>
<td align="left">--prune</td><td align="left">从输出中删除空目录。</td>

### 3、文件参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-q</td><td align="left">将不可打印的字符打印为“？”。</td>
<td align="left">-N</td><td align="left">按原样打印不可打印的字符。</td>
<td align="left">-Q</td><td align="left">用双引号引用文件名。</td>
<td align="left">-p</td><td align="left">打印每个文件的保护。</td>
<td align="left">-u</td><td align="left">显示文件所有者或UID编号。</td>
<td align="left">-g</td><td align="left">显示文件组所有者或GID编号。</td>
<td align="left">-s</td><td align="left">打印每个文件的大小（以字节为单位）。</td>
<td align="left">-h</td><td align="left">以更便于阅读的方式打印尺寸。</td>
<td align="left">--si</td><td align="left">类似-h，但使用国际单位制（1000的幂）。</td>
<td align="left">-D</td><td align="left">打印上次修改或（-c）状态更改的日期。</td>
<td align="left">-F</td><td align="left">根据ls-F追加“/”、“=”、“*”、“@”、“</td>
<td align="left">--inodes</td><td align="left">打印每个文件的inode编号。</td>
<td align="left">--device</td><td align="left">打印每个文件所属的设备ID号。</td>

### 4、排序参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-v</td><td align="left">按版本对文件进行字母数字排序。</td>
<td align="left">-r</td><td align="left">按字母数字的相反顺序对文件进行排序。</td>
<td align="left">-t</td><td align="left">按上次修改时间对文件进行排序。</td>
<td align="left">-c</td><td align="left">按上次状态更改时间对文件进行排序。</td>
<td align="left">-U</td><td align="left">保持文件未排序。</td>
<td align="left">--dirsfirst</td><td align="left">在文件之前列出目录（-U禁用）。</td>

### 5、图形选项参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-i</td><td align="left">不打印缩进线。</td>
<td align="left">-A</td><td align="left">打印ANSI线条图形缩进线条。</td>
<td align="left">-S</td><td align="left">使用ASCII图形缩进线打印。</td>
<td align="left">-n</td><td align="left">始终关闭着色（-C覆盖）。</td>
<td align="left">-C</td><td align="left">始终启用着色。</td>

### 6、XML/HTML选项参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-X</td><td align="left">打印树的XML表示形式。</td>
<td align="left">-H baseHREF</td><td align="left">打印出以baseHREF为顶部目录的HTML格式。</td>
<td align="left">-T字符串</td><td align="left">用字符串替换默认的HTML标题和H1标题。</td>
<td align="left">--nolinks</td><td align="left">关闭HTML输出中的超链接。</td>

## 四、基于tree命令复制目录结构实践

  假设某系统完成集成测试，需要上线部署到生产环境。该系统有一个用于存储文件的大目录，下面包含子目录若干，测试期间产生了大量数据，总数据量超过了5个G。生产环境部署只需要存储文件的目录结构，不需要里面存储的测试文件，这个时候怎么办？这里我们将介绍使用tree命令编写脚本实现此需求。
- 查看此文件夹大小
>  
 [root@s152 data]# du -sh * <img src="https://img-blog.csdnimg.cn/98a5a1a8d20b4586bbab8eb19bbb01af.png" alt="在这里插入图片描述"> 

- 复制目录结构到文本文档
>  
 [root@s152 data]# tree -fid --noreport datafiles -o datafiles.txt 

- 将文本文档拷贝到生产服务器待存储目录路径下
>  
 [root@s152 data]# scp datafiles.txt 192.168.0.152:/tmp/ #这里只是模拟测试，将IP地址改为你真是需要拷贝到的主机和目录下即可。 

- 使用mkdir -p命令创建目录
>  
 [root@s152 tmp]# mkdir -p `cat datafiles.txt` <img src="https://img-blog.csdnimg.cn/e4211af27e8247eeae8b9b6e82e669b2.png" alt="在这里插入图片描述"> 

- 对比目录数量
>  
 [root@s152 tmp]# tree /tmp/datafiles |grep directories 235 directories, 0 files [root@s152 tmp]# tree /data/datafiles |grep directories 235 directories, 3138 files <img src="https://img-blog.csdnimg.cn/c98159ac576d44d7b75e4f07b64337c5.png" alt="在这里插入图片描述"> 

