
--- 
title:  Linux命令之lz4命令 
tags: []
categories: [] 

---
## 一、lz4命令简介

  LZ4是一种压缩格式，特点是压缩/解压缩速度超快(压缩率不如gzip)，如果你特别在意压缩速度，或者当前环境的CPU资源紧缺，可以考虑这种格式。lz4是一种非常快速的无损压缩算法，基于字节对齐LZ77系列压缩方案。lz4提供每核400 MB/s的压缩速度，可通过多核CPU线性扩展。它的特点是极快的解码器，每核速度可达多GB/s，通常在多核系统上达到RAM速度限制项目。lz4遵循上面说到的lz77思想理论，通过滑动窗口、hash表、数据编码等操作实现数据压缩。压缩过程以至少4字节为扫描窗口查找匹配，每次移动1字节进行扫描，遇到重复的就进行压缩。centos7默认安装了lz4命令，可以实现lz4格式文件的压缩和解压缩。

## 二、命令使用示例

### 1、查看命令版本

  lz4命令安装版本是1.7.5

>  
 [root@s76 ~]# lz4 -V *** LZ4 command line interface 64-bits v1.7.5, by Yann Collet *** 


### 2、获取命令帮助

  日常使用中如果忘记lz4命令语法格式，我们可以通过lz4 --help或者man lz4命令获取lz4命令的帮助信息。

>  
 [root@s76 ~]# lz4 --help [root@s76 ~]# man lz4 


### 3、命令安装

  centos7默认安装了lz4命令，如果没有安装，可以使用yum安装方式安装该命令。

>  
 [root@s76 ~]# yum install -y lz4 lz4-devel 


### 4、压缩单个文件

>  
 [root@s76 ~]# lz4 anaconda-ks.cfg test.lz4 Compressed 2927 bytes into 1825 bytes ==&gt; 62.35% 


### 5、压缩多个文件

  压缩多个文件使用参数-m，压缩后的文件名是源文件加上lz4后缀。lz4命令只可以将单个文件压缩，如果我们需要将多个文件压缩到一个文件，我们需要将lz4和tar命令结合使用。

>  
 [root@s76 ~]# lz4 -m anaconda-ks.cfg original-ks.cfg [root@s76 ~]# ll total 16 -rw-------. 1 root root 2927 Feb 8 15:19 anaconda-ks.cfg -rw-------. 1 root root 1825 Feb 8 15:19 anaconda-ks.cfg.lz4 -rw-------. 1 root root 2045 Feb 8 15:19 original-ks.cfg -rw-------. 1 root root 1216 Feb 8 15:19 original-ks.cfg.lz4 [root@s76 ~]# tar -cvf anaconda-ks.cfg original-ks.cfg |lz4 - 2.tar.lz4 Compressed 16 bytes into 35 bytes ==&gt; 218.75% 


### 6、压缩目录

  lz4只能压缩文件，如果需要压缩目录需要结合tar命令一起。

>  
 [root@s76 ~]# tar cvf - test | lz4 - 1.tar.lz4 test/ test/1.tar Compressed 20480 bytes into 325 bytes ==&gt; 1.59% <img src="https://img-blog.csdnimg.cn/856396384ffb47609288761194bd5242.png" alt="在这里插入图片描述"> 


### 7、压缩后删除源文件

>  
 [root@s76 ~]# lz4 --rm hi.txt hi.txt.lz4 Compressed 5 bytes into 24 bytes ==&gt; 480.00% [root@s76 ~]# ll total 24 -rw-r–r–. 1 root root 325 Feb 12 20:57 1.tar.lz4 -rw-------. 1 root root 10240 Feb 12 20:40 anaconda-ks.cfg -rw-r–r–. 1 root root 24 Feb 12 21:01 hi.txt.lz4 -rw-------. 1 root root 2045 Feb 8 15:19 original-ks.cfg drwxr-xr-x. 2 root root 19 Feb 12 20:38 test 


### 8、解压lz4文件

>  
 [root@s76 ~]# lz4 -d hi.txt.lz4 Decoding file hi.txt hi.txt.lz4 : decoded 5 bytes [root@s76 ~]# ll total 28 -rw-r–r–. 1 root root 325 Feb 12 20:57 1.tar.lz4 -rw-------. 1 root root 10240 Feb 12 20:40 anaconda-ks.cfg -rw-r–r–. 1 root root 5 Feb 12 21:01 hi.txt -rw-r–r–. 1 root root 24 Feb 12 21:01 hi.txt.lz4 -rw-------. 1 root root 2045 Feb 8 15:19 original-ks.cfg drwxr-xr-x. 2 root root 19 Feb 12 20:38 test 


### 9、解压并删除压缩文件

>  
 [root@s76 ~]# lz4 --rm -d hi.txt.lz4 Decoding file hi.txt hi.txt.lz4 : decoded 5 bytes [root@s76 ~]# ll total 24 -rw-r–r–. 1 root root 325 Feb 12 20:57 1.tar.lz4 -rw-------. 1 root root 10240 Feb 12 20:40 anaconda-ks.cfg -rw-r–r–. 1 root root 5 Feb 12 21:01 hi.txt -rw-------. 1 root root 2045 Feb 8 15:19 original-ks.cfg drwxr-xr-x. 2 root root 19 Feb 12 20:38 test 


### 10、高压缩比方式压缩

>  
 [root@s76 ~]# lz4 -9 hi.txt hi.txt.lz4 Compressed 5 bytes into 24 bytes ==&gt; 480.00% 


### 11、压缩并覆盖文件

>  
 [root@s76 ~]# lz4 hi.txt.lz4 hi.txt hi.txt already exists; do you wish to overwrite (y/N) ? y Compressed 24 bytes into 43 bytes ==&gt; 179.17% [root@s76 ~]# lz4 -f hi.txt.lz4 hi.txt Compressed 24 bytes into 43 bytes ==&gt; 179.17% 


### 12、解压并输出文件

>  
 [root@s76 ~]# cat hi.txt hi,wuhs [root@s76 ~]# lz4 -dc hi.txt.lz4 hi,wuhs 


### 13、解压速度测试

  1个22G的文件解压花费时间5分18秒，解压后的大小为45G。 <img src="https://img-blog.csdnimg.cn/e7509f788fc9494e9c0683f89982f7b8.png" alt="在这里插入图片描述">

## 三、lz4命令使用语法及参数说明

### 1、命令格式

>  
 #lz4 [arg] [input] [output] 


### 2、参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-1</td><td align="left">快速压缩（默认）</td>
<td align="left">-9</td><td align="left">高压缩</td>
<td align="left">-d</td><td align="left">解压缩（默认为.lz4扩展名）</td>
<td align="left">-z</td><td align="left">强制压缩</td>
<td align="left">-f</td><td align="left">覆盖输出而不提示</td>
<td align="left">-k</td><td align="left">保留源文件（默认）</td>
<td align="left">–rm</td><td align="left">成功地解除/压缩后删除源文件</td>
<td align="left">-h/-H</td><td align="left">显示帮助/长帮助和退出</td>
<td align="left">-V</td><td align="left">显示版本号并退出</td>
<td align="left">-v</td><td align="left">详细模式</td>
<td align="left">-q</td><td align="left">取消警告；指定两次也可以取消错误</td>
<td align="left">-c</td><td align="left">强制写入标准输出，即使它是控制台</td>
<td align="left">-t</td><td align="left">测试压缩文件完整性</td>
<td align="left">-m</td><td align="left">多个输入文件（表示自动输出文件名）</td>
<td align="left">-r</td><td align="left">在目录上递归操作（也设置为-m）</td>
<td align="left">-l</td><td align="left">使用旧格式压缩（Linux内核压缩）</td>
