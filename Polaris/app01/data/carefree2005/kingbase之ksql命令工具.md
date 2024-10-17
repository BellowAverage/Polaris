
--- 
title:  kingbase之ksql命令工具 
tags: []
categories: [] 

---
## 一、ksql命令工具简介

  ksql是人大金仓提供给DBA的与KES数据库交互的命令行客户端程序。熟练使用ksql工具可以帮助DBA快速的操作和维护数据库。博文实验环境：
- 操作系统：centos7.6- kingbase版本：V008R006C006B0021
## 二、ksql使用示例

### 1、获取命令帮助

>  
 [kingbase@s166 bin]$ ./ksql --help 


### 2、指定用户登录test库

>  
 [kingbase@s166 bin]$ ./ksql -U system test ksql (V8.0) Type “help” for help.  test=# 


### 3、强制要求输入密码

  经实践测试，通过默认local socket登录不需要输入密码，及时使用-W参数强制要求输入密码，实际上任意输入值都可以完成验证。

>  
 [kingbase@s166 bin]$ ./ksql -U system -W test Password: ksql (V8.0) Type “help” for help.  test=# 


### 4、指定数据库地址登录

  指定了-h参数后，无论我们是否使用-W参数都要求输入用户名密码完成验证才可以登录数据库。

>  
 [kingbase@s166 bin]$ ./ksql -U system -h 192.168.0.166 test Password for user system: ksql (V8.0) Type “help” for help.  test=# 


### 5、指定数据库监听端口地址登录

  如果kingbase数据库实例配置了指定端口，则客户端连接的时候需要使用-p参数指定数据库端口，kingbase数据库服务默认监听端口54321。

>  
 [kingbase@s166 bin]$ ./ksql -U system -h localhost -p 54321 test Password for user system: ksql (V8.0) Type “help” for help.  test=# 


### 6、查看数据库版本

>  
 [kingbase@s166 bin]$ ./ksql -V ksql (Kingbase) V008R006C006B0021 


### 7、查看数据库列表

>  
 [kingbase@s166 bin]$ ./ksql -U system -l <img src="https://img-blog.csdnimg.cn/8abb2248963448febca02a9ca07f65f6.png" alt="在这里插入图片描述"> 


### 8、连接指定的数据库

>  
 [kingbase@s166 bin]$ ./ksql -U system -d booklist ksql (V8.0) Type “help” for help.  booklist=# 


### 9、执行指定的sql脚本

>  
 [kingbase@s166 bin]$ echo “select connections;” &gt;&gt; /tmp/test.sql [kingbase@s166 bin]$ ./ksql -U system -f /tmp/test.sql test connections ------------- 7 (1 row) 


### 10、显示执行的sql脚本中的命令

  使用-e参数显示执行的sql脚本中的命令 <img src="https://img-blog.csdnimg.cn/637b54bd322146b1b5ab90b06822fb95.png" alt="在这里插入图片描述">

### 11、不显示登录信息

>  
 [kingbase@s166 bin]$ ./ksql -U system -q test test=# 


### 12、显示内部生产的查询命令

  如果我们需要了解内部产生的查询命令，可以使用-E参数，如下示例我们执行-l参数打印数据库列表，实际上执行的命令是select d.datname as “Name”… <img src="https://img-blog.csdnimg.cn/326faccb04654ff68bc9f2c4a82f9a65.png" alt="在这里插入图片描述">

### 13、将会话日志存储到指定文件

  使用-L命令指定将会话日志存储到指定路径。连接数据库后所有的操作都将记录下来。 <img src="https://img-blog.csdnimg.cn/f2da3f81018c4886b702095eb681750d.png" alt="在这里插入图片描述">

### 14、将查询结果写入指定文件

>  
   使用-o命令将ksql命令执行的查询结果存储到指定文件中。 <img src="https://img-blog.csdnimg.cn/473ff736a6604599850a962019434be7.png" alt="在这里插入图片描述"> 


### 15、调整结果为纵向展示

  使用-x参数调整行列，展示样式调整为纵向展示。 <img src="https://img-blog.csdnimg.cn/2df9e63960114308964ba5fb3e08ea09.png" alt="在这里插入图片描述">

### 16、执行单行命令

  使用-c参数在ksql命令下直接执行命令并显示结果。 <img src="https://img-blog.csdnimg.cn/d416278e6ccc4bba8c323022b52728f3.png" alt="在这里插入图片描述">

### 17、指定输出格式

  我们可以使用-H,–csv等指定输出为样式为html或者csv。 <img src="https://img-blog.csdnimg.cn/727ee6138f964da5acb2f5fea1a8bcd7.png" alt="在这里插入图片描述">

## 三、ksql命令参数说明

### 1、命令语法

>  
 用法：ksql [OPTION]… [DBNAME [USERNAME]] 


### 2、通用参数

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-c, --command=COMMAND</td><td align="left">连接数据库后执行单行命令，执行完成后退出连接</td>
<td align="left">-d, --dbname=DBNAME</td><td align="left">指定连接的数据库名称</td>
<td align="left">-f, --file=FILENAME</td><td align="left">连接数据库时执行的脚本，执行完成后退出数据库连接</td>
<td align="left">-l, --list</td><td align="left">打印数据库列表</td>
<td align="left">-v, --set=, --variable=NAME=VALUE</td><td align="left">设置数据库参数变量</td>
<td align="left">-V, --version</td><td align="left">打印数据库版本信息</td>
<td align="left">-X, --no-ksqlrc</td><td align="left">不读取启动文件（~/.ksqlrc）</td>
<td align="left">-1 (“one”), --single-transaction</td><td align="left">作为单个事务执行（如果非交互式）</td>
<td align="left">-?, --help</td><td align="left">获取命令帮助，然后退出</td>

### 3、输入输出参数

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-a,–echo-all</td><td align="left">echo来自脚本的所有输入</td>
<td align="left">-b,–echo-errors</td><td align="left">echo失败的命令</td>
<td align="left">-e,–echo-queries</td><td align="left">发送到服务器的echo命令</td>
<td align="left">-E,–echo-hidden</td><td align="left">显示内部命令生成的查询</td>
<td align="left">-L,–log-file=FILENAME</td><td align="left">将会话日志发送到文件</td>
<td align="left">-n,–no-readline</td><td align="left">禁用增强的命令行编辑</td>
<td align="left">-o,–output=FILENAME</td><td align="left">将查询结果发送到文件（或</td>
<td align="left">-q,–quiet</td><td align="left">不输出登录提示信息</td>
<td align="left">-s,–single-step</td><td align="left">单步模式（确认每个查询）</td>
<td align="left">-S,–single-line</td><td align="left">单行模式（行尾终止SQL命令）</td>

### 4、输出格式参数

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-A, --no-align</td><td align="left">未对齐表输出模式</td>
<td align="left">–csv</td><td align="left">（逗号分隔值）表格输出模式</td>
<td align="left">-F, --field-separator=STRING</td><td align="left">设置未对齐输出的字段分隔符（默认值：“</td>
<td align="left">-H, --html</td><td align="left">html表格输出模式</td>
<td align="left">-P, --pset=VAR[=ARG]</td><td align="left">将打印选项VAR设置为ARG</td>
<td align="left">-R, --record-separator=STRING</td><td align="left">未对齐输出的记录分隔符（默认值：换行符）</td>
<td align="left">-t, --tuples-only</td><td align="left">不输出字段名</td>
<td align="left">-T, --table-attr=TEXT</td><td align="left">设置HTML表标记属性（例如，宽度、边框）</td>
<td align="left">-x, --expanded</td><td align="left">调整查询结果为纵向展示</td>
<td align="left">-z, --field-separator-zero</td><td align="left">将未对齐输出的字段分隔符设置为零字节</td>
<td align="left">-0, --record-separator-zero</td><td align="left">将未对齐输出的记录分隔符设置为零字节</td>

### 5、连接参数

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-h, --host=HOSTNAME</td><td align="left">连接数据库的主机地址或者socket路径，默认local socket</td>
<td align="left">-p, --port=PORT</td><td align="left">指定连接数据库端口，默认54321</td>
<td align="left">-U, --username=USERNAME</td><td align="left">连接数据库用户名，默认kingbase</td>
<td align="left">-w, --no-password</td><td align="left">允许不输入密码</td>
<td align="left">-W, --password</td><td align="left">强制要求输入密码</td>
