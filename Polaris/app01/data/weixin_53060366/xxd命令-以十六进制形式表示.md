
--- 
title:  xxd命令-以十六进制形式表示 
tags: []
categories: [] 

---
## xxd命令-以十六进制形式表示

### xxd命令安装

最近因为业务频繁出错，问题反馈都是通过地市反馈，这导致问题解决的效率较低。于是我就对集群部署了一套zabbix监控系统，用于监控日志关键字，当出现问题时，能及时的通过邮箱与短信双渠道告警。

在编写短信告警脚本时，发现有些短信内容字符串要转成十六进制，于是想到了xxd命令。

```
MOBILE_NUMBER=$1    # 手机号码
MESSAGE_UTF8=$3        # 短信内容
XXD="/usr/bin/xxd"
CURL="/usr/bin/curl"
TIMEOUT=5
# 短信内容要经过URL编码处理，除了下面这种方法，也可以用curl的--data-urlencode选项实现。
MESSAGE_ENCODE=$(echo "$MESSAGE_UTF8" | ${<!-- -->XXD} -ps | sed 's/\(..\)/%\1/g' | tr -d '\n')


```

当我使用时，问题也随之出现了：

```
-bash: xxd: 未找到命令

```

唉，看来是革命尚未成功，同志仍需努力啊！

于是我尝试 yum安装，结果又没可用软件包，气人。

```
yum install -y xxd
已加载插件：fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirror.bit.edu.cn
 * epel: mirror01.idc.hinet.net
 * extras: mirror.bit.edu.cn
 * updates: mirror.bit.edu.cn
没有可用软件包 xxd。
错误：无须任何处理

```

接着就是使用 yum命令检查 xxd命令由哪些模块提供（可看到有两个vim-common安装包包含有xxd工具）

```
yum whatprovides '*bin/xxd'

已加载插件：fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.bupt.edu.cn
 * centos-sclo-rh: mirrors.aliyun.com
 * centos-sclo-sclo: mirrors.aliyun.com
 * extras: mirrors.aliyun.com
 * updates: mirrors.aliyun.com
base/7/x86_64/filelists_db                                                                                                        | 7.2 MB  00:00:00     
2:vim-common-7.4.629-7.el7.x86_64 : The common files needed by any version of the VIM editor
源    ：base
匹配来源：
文件名    ：/usr/bin/xxd



updates/7/x86_64/filelists_db                                                                                                     | 8.2 MB  00:00:06     
2:vim-common-7.4.629-8.el7_9.x86_64 : The common files needed by any version of the VIM editor
源    ：updates
匹配来源：
文件名    ：/usr/bin/xxd

```

选择一个安装包进行yum安装:

```
yum install -y vim-common-7.4.629-8.el7_9.x86_64 : The common files needed by any version of the VIM editor
......
已安装:
  vim-common.x86_64 2:7.4.629-8.el7_9                                                                                                                    
作为依赖被安装:
  vim-filesystem.x86_64 2:7.4.629-8.el7_9                                                                                                                
完毕！

```

现在可以用 xxd了

```
[root@ak204 ~]# xxd -h
Usage:
       xxd [options] [infile [outfile]]
    or
       xxd -r [-s [-]offset] [-c cols] [-ps] [infile [outfile]]
Options:
    -a          toggle autoskip: A single '*' replaces nul-lines. Default off.
    -b          binary digit dump (incompatible with -ps,-i,-r). Default hex.
    -c cols     format &lt;cols&gt; octets per line. Default 16 (-i: 12, -ps: 30).
    -E          show characters in EBCDIC. Default ASCII.
    -g          number of octets per group in normal output. Default 2.
    -h          print this summary.
    -i          output in C include file style.
    -l len      stop after &lt;len&gt; octets.
    -ps         output in postscript plain hexdump style.
    -r          reverse operation: convert (or patch) hexdump into binary.
    -r -s off   revert with &lt;off&gt; added to file positions found in hexdump.
    -s [+][-]seek  start at &lt;seek&gt; bytes abs. (or +: rel.) infile offset.
    -u          use upper case hex letters.
    -v          show version: "xxd V1.10 27oct98 by Juergen Weigert".


```

### xxd学习

xxd的作用就是将一个文件以十六进制的形式显示出来。它还可以将十六进制转储转换回其原始二进制形式。

常用参数：

-a 它的作用是自动跳过空白内容，默认是关闭的 -c 它的后面加上数字表示每行显示多少字节的十六进制数，默认是16字节 -g 设定以几个字节为一块，默认为2字节 -l 显示多少字节的内容  -s 后面接【±】和address.加号表示从地址处开始的内容，减号表示距末尾address开始的内容

使用-a参数，自动跳过空白，从0x200开始，输入文件:

```
[root@linuxcool ~]# xxd -a -s +0x200 linuxcool.txt

```

使用-a、-c参数，自动跳过空白，每行显示12字节，从0x200开始，输入文件:

```
[root@linuxcool ~]# xxd -a -c 12 -s +0x200 linuxcool.txt

```

使用-a、-c、-g参数，自动跳过空白，每行显示12字节，一个字节一块，显示512字节内容，从0x200开始，输入文件:

```
[root@linuxcool ~]# xxd -a -c 12 -g 1 -l 512 -s +0x200 linuxcool.txt

```

### 使用 xxd命令

xxd是二进制查看命令，默认将文件显示为16进制字符串表示形式。

```
[root@ambari dir]# cat t
31
[root@ambari dir]# xxd t
0000000: 3331 0a                                  31.
[root@ambari dir]# xxd -ps t
33310a
[root@ambari dir]# xxd -b t
0000000: 00110011 00110001 00001010                             31.

```

-ps 参数：以 postscript的连续16进制转储输出，也叫做纯16进制转储。 -b参数：以2进制字符串形式输出。

-r参数：逆向转换。将16进制字符串表示转为实际的数：

```
[root@ambari dir]# echo -n "0000000: 3331 0a                                  31." | xxd  -r
31
[root@ambari dir]# echo -n "0000000: 3331 0a" | xxd  -r
31
[root@ambari dir]# echo -n "33310a" | xxd  -r -ps
31
[root@ambari dir]# echo -n "33310A" | xxd  -r -ps
31

```
