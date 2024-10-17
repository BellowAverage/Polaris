
--- 
title:  200 个 Python 标准库汇总 
tags: []
categories: [] 

---
>  
  来源：Python与算法社区 
 

### 文本

string：通用字符串操作

re：正则表达式操作

difflib：差异计算工具

textwrap：文本填充

unicodedata：Unicode字符数据库

stringprep：互联网字符串准备工具

readline：GNU按行读取接口

rlcompleter：GNU按行读取的实现函数

struct：将字节解析为打包的二进制数据

codecs：注册表与基类的编解码器

### 数据类型

datetime：基于日期与时间工具

calendar：通用月份函数

collections：容器数据类型

collections.abc：容器虚基类

heapq：堆队列算法

bisect：数组二分算法

array：高效数值数组

weakref：弱引用

types：内置类型的动态创建与命名

copy：浅拷贝与深拷贝

reprlib：交替repr()的实现

### 数学

numbers：数值的虚基类

math：数学函数

cmath：复数的数学函数

decimal：定点数与浮点数计算

fractions：有理数

random：生成伪随机数

### 函数式编程

itertools：为高效循环生成迭代器

functools：可调用对象上的高阶函数与操作

operator：针对函数的标准操作

### 文件与目录

os.path：通用路径名控制

fileinput：从多输入流中遍历行

stat：解释stat()的结果

filecmp：文件与目录的比较函数

tempfile：生成临时文件与目录

glob：Unix风格路径名格式的扩展

fnmatch：Unix风格路径名格式的比对

linecache：文本行的随机存储

shutil：高级文件操作

macpath：MacOS 9路径控制函数

### 持久化

pickle：Python对象序列化

copyreg：注册机对pickle的支持函数

shelve：Python对象持久化

marshal：内部Python对象序列化

dbm：Unix“数据库”接口

sqlite3：针对SQLite数据库的API2.0

### 压缩

zlib：兼容gzip的压缩

gzip：对gzip文件的支持

bz2：对bzip2压缩的支持

lzma：使用LZMA算法的压缩

zipfile：操作ZIP存档

tarfile：读写tar存档文件

### 加密

hashlib：安全散列与消息摘要

hmac：针对消息认证的键散列

### 操作系统工具

os：多方面的操作系统接口

io：流核心工具

time：时间的查询与转化

argparser：命令行选项、参数和子命令的解析器

optparser：命令行选项解析器

getopt：C风格的命令行选项解析器

logging：Python日志工具

logging.config：日志配置

logging.handlers：日志处理器

getpass：简易密码输入

curses：字符显示的终端处理

curses.textpad：curses程序的文本输入域

curses.ascii：ASCII字符集工具

curses.panel：curses的控件栈扩展

platform：访问底层平台认证数据

errno：标准错误记号

ctypes：Python外部函数库

### 并发

threading：基于线程的并行

multiprocessing：基于进程的并行

concurrent：并发包

concurrent.futures：启动并行任务

subprocess：子进程管理

sched：事件调度

queue：同步队列

select：等待I / O完成

dummy_threading：threading模块的替代（当_thread不可用时）

_thread：底层的线程API（threading基于其上）

_dummy_thread：_thread模块的替代（当_thread不可用时）

### 进程间通信

socket：底层网络接口

ssl：socket对象的TLS / SSL填充器

asyncore：异步套接字处理器

asynchat：异步套接字命令 / 响应处理器

signal：异步事务信号处理器

mmap：内存映射文件支持

### 互联网

email：邮件与MIME处理包

json：JSON编码与解码

mailcap：mailcap文件处理

mailbox：多种格式控制邮箱

mimetypes：文件名与MIME类型映射

base64：RFC3548：Base16、Base32、Base64编码

binhex：binhex4文件编码与解码

binascii：二进制码与ASCII码间的转化

quopri：MIMEquoted - printable数据的编码与解码

uu：uuencode文件的编码与解码

### 互联网协议与支持

webbrowser：简易Web浏览器控制器

cgi：CGI支持

cgitb：CGI脚本反向追踪管理器

wsgiref：WSGI工具与引用实现

urllib：URL处理模块

urllib.request：打开URL连接的扩展库

urllib.response：urllib模块的响应类

urllib.parse：将URL解析成组件

urllib.error：urllib.request引发的异常类

urllib.robotparser：robots.txt的解析器

http：HTTP模块

http.client：HTTP协议客户端

ftplib：FTP协议客户端

poplib：POP协议客户端

imaplib：IMAP4协议客户端

nntplib：NNTP协议客户端

smtplib：SMTP协议客户端

smtpd：SMTP服务器

telnetlib：Telnet客户端

uuid：RFC4122的UUID对象

socketserver：网络服务器框架

http.server：HTTP服务器

http.cookies：HTTPCookie状态管理器

http.cookiejar：HTTP客户端的Cookie处理

xmlrpc：XML - RPC服务器和客户端模块

xmlrpc.client：XML - RPC客户端访问

xmlrpc.server：XML - RPC服务器基础

ipaddress：IPv4 / IPv6控制库

### 多媒体

audioop：处理原始音频数据

aifc：读写AIFF和AIFC文件

sunau：读写Sun AU文件

wave：读写WAV文件

chunk：读取IFF大文件

colorsys：颜色系统间转化

imghdr：指定图像类型

sndhdr：指定声音文件类型

ossaudiodev：访问兼容OSS的音频设备

### 国际化

gettext：多语言的国际化服务

locale：国际化服务

### 编程框架

turtle：Turtle图形库

cmd：基于行的命令解释器支持

shlex：简单词典分析

### Tk图形用户接口

tkinter：Tcl / Tk接口

tkinter.ttk：Tk主题控件

tkinter.tix：Tk扩展控件

tkinter.scrolledtext：滚轴文本控件

### 开发工具

pydoc：文档生成器和在线帮助系统

doctest：交互式Python示例

unittest：单元测试框架

unittest.mock：模拟对象库

test：Python回归测试包

test.support：Python测试工具套件

venv：虚拟环境搭建

### 调试

bdb：调试框架

faulthandler：Python反向追踪库

pdb：Python调试器

timeit：小段代码执行时间测算

trace：Python执行状态追踪

### 运行时

sys：系统相关的参数与函数

sysconfig：访问Python配置信息

builtins：内置对象

main：顶层脚本环境

warnings：警告控制

contextlib：with状态的上下文工具

abc：虚基类

atexit：出口处理器

traceback：打印或读取一条栈的反向追踪

future：未来状态定义

gc：垃圾回收接口

inspect：检查存活的对象

site：址相关的配置钩子（hook）

fpectl：浮点数异常控制

distutils：生成和安装Python模块

### 解释器

code：基类解释器

codeop：编译Python代码

### 导入模块

imp：访问import模块的内部

zipimport：从ZIP归档中导入模块

pkgutil：包扩展工具

modulefinder：通过脚本查找模块

runpy：定位并执行Python模块

importlib：import的一种实施

### Python语言

parser：访问Python解析树

ast：抽象句法树

symtable：访问编译器符号表

symbol：Python解析树中的常量

token：Python解析树中的常量

keyword：Python关键字测试

tokenize：Python源文件分词

tabnany：模糊缩进检测

pyclbr：Python类浏览支持

py_compile：编译Python源文件

compileall：按字节编译Python库

dis：Python字节码的反汇编器

pickletools：序列化开发工具

### 其他

formatter：通用格式化输出

### Windows相关

msilib：读写Windows的Installer文件

msvcrt：MS VC + + Runtime的有用程序

winreg：Windows注册表访问

winsound：Windows声音播放接口

### Unix相关

posix：最常用的POSIX调用

pwd：密码数据库

spwd：影子密码数据库

grp：组数据库

crypt：Unix密码验证

termios：POSIX风格的tty控制

tty：终端控制函数

pty：伪终端工具

fcntl：系统调用fcntl()和ioctl()

pipes：shell管道接口

resource：资源可用信息

nis：Sun的NIS的接口

syslog：Unix 日志服务

以上就是对Python内置各个模块的简要总结，大家可收藏此文，后面做项目时再从中检索。希望此文能帮助到大家，欢迎补充还常用的Python内置模块。

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcGFPWnF1SzE4eGM0V2JIT05pYmVoZU9HTXNJMUdIR0Z1UmpycUxpY2lhNld1aWNxaWNNWTZuY2t2Y21pYUZaWUcxWnM4Zjd5bnBwRTJaR2JFQS82NDA?x-oss-process=image/format,png">

分享或在看是对我最大的支持
