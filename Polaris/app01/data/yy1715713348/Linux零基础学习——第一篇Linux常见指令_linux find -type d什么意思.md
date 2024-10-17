
--- 
title:  Linux零基础学习——第一篇:Linux常见指令_linux find -type d什么意思 
tags: []
categories: [] 

---
##### 文章目录
- 系列文章目录- 前言- 一、Linux是什么- 二、Linux下基本指令<li> 
  <ul><li> 
    <ul>- 1.ls指令- 2.pwd指令- 3.cd指令- 4.touch指令- 5.mkdir指令- 6.rmdir指令- 7.rm指令- 8.man指令- 9.echo指令- 10.cp指令- 11.mv指令- 12.cat指令- 13.tac指令- 14.more指令- 15.less指令- 16.head指令- 17.tail指令- 18.时间相关的指令<li> 
      <ul><li> 
        <ul>- 1.data指令
### 前言

<img src="https://img-blog.csdnimg.cn/20210524162600119.png#pic_left" alt="在这里插入图片描述">

### 一、Linux是什么

Linux是一种自由和开放源代码的类UNIX操作系统，该操作系统的内核由林纳斯托瓦兹在1991年首次发布，之后，在加上用户空间的应用程序之后，就成为了Linux操作系统。严格来讲， Linux只是操作系统内核本身，但通常采用“Linux内核”来表达该意思。而Linux则常用来指基于Linux内核的完整操作系统，它包括GUI组件和许多其他实用工具。 <img src="https://img-blog.csdnimg.cn/20210524162942213.png" alt="在这里插入图片描述">

### 二、Linux下基本指令

##### 1.ls指令

语法： ls [选项][目录或文件] 功能：对于目录，该命令列出该目录下的所有子目录与文件。对于文件，将列出文件名以及其他信息。 <img src="https://img-blog.csdnimg.cn/20210524163209323.png" alt="在这里插入图片描述"> **常用选项：** **ls -a** 列出目录下的所有文件，包括以 . 开头的隐含文件。 <img src="https://img-blog.csdnimg.cn/20210524163316357.png" alt="在这里插入图片描述"> **ls -d** 将目录象文件一样显示，而不是显示其下的文件。 如： ls –d 指定目录 <img src="https://img-blog.csdnimg.cn/2021052416345356.png" alt="在这里插入图片描述"> **ls -i** 输出文件的 i 节点的索引信息。 如 ls –ai 指定文件 <img src="https://img-blog.csdnimg.cn/20210524163529593.png" alt="在这里插入图片描述"> **ls -l**列出文件的详细信息。 <img src="https://img-blog.csdnimg.cn/20210524163723248.png" alt="在这里插入图片描述"> **ls -al** 列出目录下的所有文件的详细信息，包括以 . 开头的隐含文件 <img src="https://img-blog.csdnimg.cn/20210524163830860.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **ls -k** 以 k 字节的形式表示文件的大小。 ls –alk 指定文件 **ls -n** 用数字的 UID,GID 代替名称。 （介绍 UID， GID） <img src="https://img-blog.csdnimg.cn/20210524164336230.png" alt="在这里插入图片描述"> -F 在每个文件名后附上一个字符以说明该文件的类型， “*”表示可执行的普通文件； “/”表示目录； “@”表示符号链接； “|”表示FIFOs； “=”表示套接字(sockets)。（目录类型识别） **ls -r** 对目录反向排序。 <img src="https://img-blog.csdnimg.cn/2021052416405730.png" alt="在这里插入图片描述"> **ls -t** 以时间排序。 <img src="https://img-blog.csdnimg.cn/20210524164029601.png" alt="在这里插入图片描述"> **ls -s** 在l文件名后输出该文件的大小。（大小排序，如何找到目录下最大的文件） <img src="https://img-blog.csdnimg.cn/20210524164010813.png" alt="在这里插入图片描述"> **ls -R** 列出所有子目录下的文件。 (递归) <img src="https://img-blog.csdnimg.cn/20210524164121266.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **ls -1** 一行只输出一个文件 <img src="https://img-blog.csdnimg.cn/20210524163929479.png" alt="在这里插入图片描述">

##### 2.pwd指令

语法: pwd 功能：显示用户当前所在的目录 常用选项：无 <img src="https://img-blog.csdnimg.cn/2021052416455285.png" alt="在这里插入图片描述">

##### 3.cd指令

**Linux系统中，磁盘上的文件和目录被组成一棵目录树，每个节点都是目录或文件。** <img src="https://img-blog.csdnimg.cn/20210524164924728.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 语法:cd 目录名 功能:改变工作目录,将当前工作目录改变到指定的目录下。 <img src="https://img-blog.csdnimg.cn/20210524164955758.png" alt="在这里插入图片描述"> 常用选项： **cd. .** ：返回上级目录 <img src="https://img-blog.csdnimg.cn/20210524165059263.png" alt="在这里插入图片描述"> **cd /home/yyw/test1/** : 绝对路径- -&gt;从根目录下开始的路径 <img src="https://img-blog.csdnimg.cn/20210524165209300.png" alt="在这里插入图片描述"> **cd …/…test1:** 相对路径 - -&gt;有很多种去往目录的路径 <img src="https://img-blog.csdnimg.cn/20210524165536594.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **cd ~**：进入用户家目 <img src="https://img-blog.csdnimg.cn/20210524165556587.png" alt="在这里插入图片描述"> **cd -** ：返回最近访问目录 <img src="https://img-blog.csdnimg.cn/20210524165618689.png" alt="在这里插入图片描述"> 如果你对网络安全入门感兴趣，那么你点击这里**👉**

##### 4.touch指令

语法:touch [选项]… 文件… 功能： touch命令参数可更改文档或目录的日期时间，包括存取时间和更改时间，或者新建一个不存在的文件 <img src="https://img-blog.csdnimg.cn/20210524165959499.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210524170058401.png" alt="在这里插入图片描述"> **常用选项：** -a 或–time=atime或–time=access或–time=use只更改存取时间。 -c 或–no-create 不建立任何文档。 -d 使用指定的日期时间，而非现在的时间。 -f 此参数将忽略不予处理，仅负责解决BSD版本touch指令的兼容性问题。 -m 或–time=mtime或–time=modify 只更改变动时间。 -r 把指定文档或目录的日期时间，统统设成和参考文档或目录的日期时间相同。 -t 使用指定的日期时间，而非现在的时间

##### 5.mkdir指令

<img src="https://img-blog.csdnimg.cn/20210524170651158.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 语法： mkdir [选项] dirname… 功能：在当前目录下创建一个名为 “dirname”的目录 <img src="https://img-blog.csdnimg.cn/20210524170420986.png" alt="在这里插入图片描述"> 常用选项： **mkdir -p a1/a2/a3/a4** 可以是一个路径名称。此时若路径中的某些目录尚不存在,加上此选项后,系统将自动建立好那些尚不存在的目录,即一次可以建立多个目录。 <img src="https://img-blog.csdnimg.cn/2021052417054398.png" alt="在这里插入图片描述">

##### 6.rmdir指令

**rmdir**是一个与**mkdir**相对应的命令。 mkdir是建立目录，而rmdir是删除目录。 语法： rmdir [-p][dirName] 适用对象：具有当前目录操作权限的所有使用者 功能：删除空目录 <img src="https://img-blog.csdnimg.cn/20210524171013764.png" alt="在这里插入图片描述"> **对于不是空目录，则不然删除** <img src="https://img-blog.csdnimg.cn/20210524171119778.png" alt="在这里插入图片描述">

##### 7.rm指令

rm命令可以同时删除文件或目录 语法： rm [-f-i-r-v][dirName/dir] 适用对象：所有使用者 功能：删除文件或目录 <img src="https://img-blog.csdnimg.cn/20210524171411983.png" alt="在这里插入图片描述"> **单独的rm不能删除目录** <img src="https://img-blog.csdnimg.cn/20210524171536909.png" alt="在这里插入图片描述"> 常用选项： **rm -rf** 即使文件属性为只读(即写保护)，亦直接删除,强制递归删除，**删库跑路的指针，慎用** <img src="https://img-blog.csdnimg.cn/20210524171731141.png" alt="在这里插入图片描述"> **rm -i** 删除前逐一询问确认 <img src="https://img-blog.csdnimg.cn/2021052417170883.png" alt="在这里插入图片描述"> **rm -r** 删除目录及其下所有文件，**递归删除文件** <img src="https://img-blog.csdnimg.cn/20210524171608305.png" alt="在这里插入图片描述">

##### 8.man指令

Linux的命令有很多参数，我们不可能全记住，我们可以通过查看联机手册获取帮助。访问Linux手册页的命令是man 语法: man [选项] 命令 **常用选项** -k 根据关键字搜索联机帮助 num 只在第num章节找 -a 将所有章节的都显示出来，比如 man printf 它缺省从第一章开始搜索，知道就停止，用a选项，当按下q退出，他会继续往后面搜索，直到所有章节都搜索完毕。 **解释一下,手册分为8章** 1 是普通的命令 2 是系统调用,如open,write之类的(通过这个，至少可以很方便的查到调用这个函数，需要加什么头文件) 3 是库函数,如printf,fread4是特殊文件,也就是/dev下的各种设备文件 4 特殊文件设备文件 5 是指文件的格式,比如passwd, 就会说明这个文件中各个字段的含义 6 是给游戏留的,由各个游戏自己定义 7 是附件还有一些变量,比如向environ这种全局变量在这里就有说明 8 是系统管理用的命令,这些命令只能由root使用,如ifconfi <img src="https://img-blog.csdnimg.cn/20210524172715364.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

##### 9.echo指令

echo命令的功能是在显示器上显示一段文字，一般起到一个提示的作用。 该命令的一般格式为： echo [ -n ] 字符串 **其中选项n表示输出文字后不换行；字符串能加引号，也能不加引号。用echo命令输出加引号的字符串时，将字符串原样输出；用echo命令输出不加引号的字符串时，将字符串中的各个单词作为字符串输出，各字符串之间用一个空格分割。** 功能说明：显示文字。 语法：echo [-ne][字符串]或 echo [–help][–version] <img src="https://img-blog.csdnimg.cn/20210524173145122.png" alt="在这里插入图片描述"> 输出字符重定向到另外一个文件 <img src="https://img-blog.csdnimg.cn/20210524173318974.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210524173337759.png" alt="在这里插入图片描述">

##### 10.cp指令

语法:cp [选项] 源文件或目录目标文件或目录 功能: 复制文件或目录 说明: cp指令用于复制文件或目录，如同时指定两个以上的文件或目录，且最后的目的地是一个已经存在的目录，则它会把前面指定的所有文件或目录复制到此目录中。若同时指定多个文件或目录，而最后的目的地并非一个已存在的目录，则会出现错误信息。 <img src="https://img-blog.csdnimg.cn/20210524185055214.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 常用选项： -f 或 --force 强行复制文件或目录， 不论目的文件或目录是否已经存在 -i 或 --interactive 覆盖文件之前先询问用户 -r递归处理，将指定目录下的文件与子目录一并处理。若源文件或目录的形态，不属于目录或符号链接，则一律视为普通文件处理 -R 或 --recursive递归处理，将指定目录下的文件及子目录一并处理 <img src="https://img-blog.csdnimg.cn/20210524185432285.png" alt="在这里插入图片描述"> 如果你对网络安全入门感兴趣，那么你点击这里**👉**

##### 11.mv指令

**mv**命令是move的缩写，可以用来移动文件或者将文件改名（move (rename) files），是Linux系统下常用的命令，经常用来备份文件或者目录。 语法: mv [选项] 源文件或目录 目标文件或目录 <img src="https://img-blog.csdnimg.cn/20210524190431744.png" alt="在这里插入图片描述"> 功能:
1. 视mv命令中第二个参数类型的不同（是目标文件还是目标目录）， mv命令将文件重命名或将其移至一个新的目录中。1. 当第二个参数类型是文件时， mv命令完成文件重命名，此时，源文件只能有一个（也可以是源目录名），它将所给的源文件或目录重命名为给定的目标文件名。1. 当第二个参数是已存在的目录名称时，源文件或目录参数可以有多个， mv命令将各参数指定的源文件均移至目标目录中。
<img src="https://img-blog.csdnimg.cn/20210524185824745.png" alt="在这里插入图片描述"> 常用选项： -f ： force 强制的意思，如果目标文件已经存在，不会询问而直接覆盖 <img src="https://img-blog.csdnimg.cn/20210524190359613.png" alt="在这里插入图片描述"> **mv -i copy test1**：若目标文件 (destination) 已经存在时，就会询问是否覆盖！ <img src="https://img-blog.csdnimg.cn/20210524190040339.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2021052419023317.png" alt="在这里插入图片描述">

##### 12.cat指令

语法： cat [选项][文件] 功能： 查看目标文件的内容 <img src="https://img-blog.csdnimg.cn/20210524190846916.png" alt="在这里插入图片描述"> 常用选项： **cat -b** 对非空输出行编号 <img src="https://img-blog.csdnimg.cn/20210524191037600.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **cat -n** 对输出的所有行编号 <img src="https://img-blog.csdnimg.cn/20210524190920218.png" alt="在这里插入图片描述"> **cat -s** 不输出多行空行 <img src="https://img-blog.csdnimg.cn/20210524191104150.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

##### 13.tac指令

语法： tac [选项][文件] 功能： 反向查看目标文件的内容 <img src="https://img-blog.csdnimg.cn/20210524191244760.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **tac没有-n选项** <img src="https://img-blog.csdnimg.cn/20210524191337291.png" alt="在这里插入图片描述">

##### 14.more指令

语法： more [选项][文件] 功能： more命令，功能类似 cat <img src="https://img-blog.csdnimg.cn/20210524191423982.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 常用选项： -n 对输出的所有行编号 q 退出more

##### 15.less指令
1. less 工具也是对文件或其它输出进行分页显示的工具，应该说是linux正统查看文件内容的工具，功能极其强大。1. less 的用法比起 more 更加的有弹性。在 more 的时候，我们并没有办法向前面翻， 只能往后面看但若使用了 less 时，就可以使用 [pageup][pagedown] 等按键的功能来往前往后翻看文件，更容易用来查看一个文件的内容。1. 除此之外，在 less 里头可以拥有更多的搜索功能，不止可以向下搜，也可以向上搜 <img src="https://img-blog.csdnimg.cn/20210524192316687.png" alt="在这里插入图片描述"> 语法： less [参数] 文件 功能： less与more类似，但使用less可以随意浏览文件，而more仅能向前移动，却不能向后移动，而且less在查看之前不会加载整个文件。 <img src="https://img-blog.csdnimg.cn/20210524192335369.png" alt="在这里插入图片描述"> 选项： -i 忽略搜索时的大小写 -N 显示每行的行号 /字符串：向下搜索“字符串”的功能 ?字符串：向上搜索“字符串”的功能 n：重复前一个搜索（与 / 或 ? 有关） N：反向重复前一个搜索（与 / 或 ? 有关） q:quit
##### 16.head指令

head 与 tail 就像它的名字一样的浅显易懂，它是用来显示开头或结尾某个数量的文字区块， head 用来显示档案的开头至标准输出中，而 tail 想当然尔就是看档案的结尾。 语法： head [参数]… [文件]… 功能： head 用来显示档案的开头至标准输出中，默认head命令打印其相应文件的开头10行 <img src="https://img-blog.csdnimg.cn/20210524193102548.png" alt="在这里插入图片描述"> 选项： **head -4 test.c**&lt;行数&gt; 显示的行数 <img src="https://img-blog.csdnimg.cn/20210524192913501.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

##### 17.tail指令

tail 命令从指定点开始将文件写到标准输出.使用tail命令的-f选项可以方便的查阅正在改变的日志文件,tail -f filename会把filename里最尾部的内容显示在屏幕上,并且不但刷新,使你看到最新的文件内容. 语法： tail[必要参数][选择参数][文件] 功能： 用于显示指定文件末尾内容，不指定文件时，作为输入信息进行处理。常用查看日志文件。 <img src="https://img-blog.csdnimg.cn/20210524193229912.png" alt="在这里插入图片描述"> 选项: **less -f** 循环读取 **less -n**&lt;行数&gt; 显示行数 <img src="https://img-blog.csdnimg.cn/20210524193335551.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210524193614601.png" alt="在这里插入图片描述">

##### 18.时间相关的指令

###### 1.data指令

date 指定格式显示时间： date +%Y:%m:%d date 用法： date [OPTION]… [+FORMAT] <img src="https://img-blog.csdnimg.cn/20210524193654364.png" alt="在这里插入图片描述"> 1.在显示方面，使用者可以设定欲显示的格式，格式设定为一个加号后接数个标记，其中常用的标记列表如下 %H : 小时(00…23) %M : 分钟(00…59) %S : 秒(00…61) %X : 相当于 %H:%M:%S %d : 日 (01…31) %m : 月份 (01…12) %Y : 完整年份 (0000…9999) %F : 相当于 %Y-%m-%d <img src="https://img-blog.csdnimg.cn/20210524193804365.png" alt="在这里插入图片描述"> 2.在设定时间方面 date -s //设置当前时间，只有root权限才能设置，其他只能查看。 date -s 20080523 //设置成20080523，这样会把具体时间设置成空00:00:00 date -s 01:01:01 //设置具体时间，不会对日期做更改 date -s “01:01:01 2008-05-23″ //这样可以设置全部时间 date -s “01:01:01 20080523″ //这样可以设置全部时间 date -s “2008-05-23 01:01:01″ //这样可以设置全部时间 date -s “20080523 01:01:01″ //这样可以设置全部时间

3.时间戳

时间-&gt;时间戳： date +%s 时间戳-&gt;时间： date -d@1 --1970年1月1日8时零分零秒 <img src="https://img-blog.csdnimg.cn/20210524193919847.png" alt="在这里插入图片描述"> Unix时间戳（英文为Unix epoch, Unix time, POSIX time 或 Unix timestamp）是从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数，不考虑闰 <img src="https://img-blog.csdnimg.cn/20210524193838163.png" alt="在这里插入图片描述"> 如果你对网络安全入门感兴趣，那么你点击这里**👉**

##### 19.cal指令

cal命令可以用来显示公历（阳历）日历。公历是现在国际通用的历法，又称格列历，通称阳历。 “阳历”又名“太阳历”，系以地球绕行太阳一周为一年，为西方各国所通用，故又名“西历”。 命令格式： cal [参数][月份][年份] 功能： 用于查看日历等时间信息，如只有一个参数，则表示年份(1-9999)，如有两个参数，则表示月份和年份 <img src="https://img-blog.csdnimg.cn/20210524194150595.png" alt="在这里插入图片描述"> 常用选项： **cal -3** 显示系统前一个月，当前月，下一个月的月历 <img src="https://img-blog.csdnimg.cn/20210524194258767.png" alt="在这里插入图片描述"> **cal -j** 显示在当年中的第几天（一年日期按天算，从1月1号算起，默认显示当前月在一年中的天数） <img src="https://img-blog.csdnimg.cn/20210524194320342.png" alt="在这里插入图片描述"> **cal -y** 显示当前年份的日历 <img src="https://img-blog.csdnimg.cn/20210524194334559.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

##### 20.find指令
1. Linux下find命令在目录结构中搜索文件，并执行指定的操作。1. Linux下find命令提供了相当多的查找条件，功能很强大。由于find具有强大的功能，所以它的选项也很多，其中大部分选项都值得我们花时间来了解一下。1. 即使系统中含有网络文件系统( NFS)， find命令在该文件系统中同样有效，只你具有相应的权限。1. 在运行一个非常消耗资源的find命令时，很多人都倾向于把它放在后台执行，因为遍历一个大的文件系统可能会花费很长的时间(这里是指30G字节以上的文件系统)。
语法： find pathname -options 功能： 用于在文件树种查找文件，并作出相应的处理（可能访问磁盘） 常用选项： -name 按照文件名查找文件。 <img src="https://img-blog.csdnimg.cn/2021052419462884.png" alt="在这里插入图片描述">

##### 21.grep指令

语法： grep [选项] 搜寻字符串 文件 功能： 在文件中搜索字符串，将找到的行打印出来 代码如下（示例）： <img src="https://img-blog.csdnimg.cn/2021052419490697.png" alt="在这里插入图片描述"> 常用选项： -i ：忽略大小写的不同，所以大小写视为相同 -n ：顺便输出行号 <img src="https://img-blog.csdnimg.cn/20210524195050513.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> -v ：反向选择，亦即显示出没有 ‘搜寻字符串’ 内容的那一行 <img src="https://img-blog.csdnimg.cn/20210524194955445.png" alt="在这里插入图片描述">

##### 22.which&amp;&amp;whoami指令

**whoami**:查看当前的用户是root用户还是普通用户 <img src="https://img-blog.csdnimg.cn/20210524195225944.png" alt="在这里插入图片描述"> **which +指令**：查看当前指令怎么构成的 <img src="https://img-blog.csdnimg.cn/20210524195401131.png" alt="在这里插入图片描述"> **alias给指令起别名:** <img src="https://img-blog.csdnimg.cn/20210524195432713.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0OTE4MDkw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

##### 23.zip/unzip指令

语法： zip 压缩文件.zip 目录或文件 功能： 将目录或文件压缩成zip格式 常用选项： -r 递 归处理，将指定目录下的所有文件和子目录一并处理 **黄色箭头指的特别重要，如果没有的话只会打包目录，目录里面的文件不会打包** **gzip：** <img src="https://img-blog.csdnimg.cn/20210524200241640.png" alt="在这里插入图片描述"> **unzip:** <img src="https://img-blog.csdnimg.cn/20210524200608104.png" alt="在这里插入图片描述">

##### 24.tar指令

****tar指令（重要）：打包/解包，不打开它，直接看内容**** <img src="https://img-blog.csdnimg.cn/20210524201421458.png" alt="在这里插入图片描述"> tar [-cxtzjvf] 文件与目录 … 参数： -c ：建立一个压缩文件的参数指令(create 的意思)； -x ：解开一个压缩文件的参数指令！ -t ：查看 tarfile 里面的文件！ -z ：是否同时具有 gzip 的属性？亦即是否需要用 gzip 压缩？ -j ：是否同时具有 bzip2 的属性？亦即是否需要用 bzip2 压缩？ -v ：压缩的过程中显示文件！这个常用，但不建议用在背景执行过程！ -f ：使用档名，请留意，在 f 之后要立即接档名喔！不要再加参数！ -C ： 解压到指定目录

##### 25.bc指令

bc命令可以很方便的进行浮点运算 <img src="https://img-blog.csdnimg.cn/20210524200903646.png" alt="在这里插入图片描述">

##### 26.uname -r指令

语法： uname [选项] 功能： uname用来获取电脑和操作系统的相关信息。 补充说明： uname可显示linux主机所用的操作系统的版本、硬件的名称等基本信息。 <img src="https://img-blog.csdnimg.cn/20210524200957741.png" alt="在这里插入图片描述"> 常用选项： -a或–all 详细输出所有信息，依次为内核名称，主机名，内核版本号，内核版本，硬件名，处理器类型，硬件平台类型，操作系统名称 <img src="https://img-blog.csdnimg.cn/20210524201029281.png" alt="在这里插入图片描述">

##### 27.重要的几个热键

[Tab]按键—具有『命令补全』和『档案补齐』的功能 **[Ctrl]-c**按键—让当前的程序『停掉』 **[Ctrl]-d**按键—通常代表着：『键盘输入结束(End Of File, EOF 戒 End OfInput)』的意思；另外，他也可以用来取代exit

##### 28.关机

语法： shutdown [选项] ** 常见选项： ** -h ： 将系统的服务停掉后，立即关机。 -r ： 在将系统的服务停掉之后就重新启动 -t sec ： -t 后面加秒数，亦即『过几秒后关机』的意思 <img src="https://img-blog.csdnimg.cn/20210524201259165.png" alt="在这里插入图片描述">

##### 29.扩展命令

以下命令作为扩展: **◆ 安装和登录命令**： login、 shutdown、 halt、 reboot、 install、 mount、 umount、 chsh、 exit、 last； **◆ 文件处理命令**： file、 mkdir、 grep、 dd、 find、 mv、 ls、 diff、 cat、 ln； **◆ 系统管理相关命令**： df、 top、 free、 quota、 at、 lp、 adduser、 groupadd、 kill、 crontab； **◆ 网络操作命令**： ifconfig、 ip、 ping、 netstat、 telnet、 ftp、 route、 rlogin、 rcp、 finger、 mail、 nslookup； **◆ 系统安全相关命令**： passwd、 su、 umask、 chgrp、 chmod、 chown、 chattr、 sudo ps、 who； **◆ 其它命令**： tar、 unzip、 gunzip、 unarj、 mtools、 man、 unendcode、 uudecode。

##### 30.shell命令以及运行原理

Linux严格意义上说的是一个操作系统，我们称之为“核心（kernel） “ ，但我们一般用户，不能直接使用kernel。而是通过kernel的“外壳”程序，也就是所谓的shell，来与kernel沟通。**如何理解？为什么不能直接使用kernel？**

**从技术角度**， Shell的最简单定义：命令行解释器（command Interpreter）主要包含：将使用者的命令翻译给核心（kernel）处理。同时，将核心的处理结果翻译给使用者。

**对比windows GUI**，我们操作windows 不是直接操作windows内核，而是通过图形接口，点击，从而完成我们的操作（比如进入D盘的操作，我们通常是双击D盘盘符.或者运行起来一个应用程序）。

**shell 对于Linux**，有相同的作用，主要是对我们的指令进行解析，解析指令给Linux内核。反馈结果在通过内核运行出结果，通过shell解析给用户。

**帮助理解：如果说你是一个闷骚且害羞的程序员，那shell就像媒婆，操作系统内核就是你们村头漂亮的且有让你心动的MM小花。你看上了小花，但是有不好意思直接表白，那就让你你家人找媒婆帮你提亲，所有的事情你都直接跟媒婆沟通，由媒婆转达你的意思给小花，而我们找到媒婆姓王，所以我们叫它王婆，它对应我们常使用的bash**。

### 总结

以上就是今天要讲的内容，本文仅仅简单介绍了Linux中一些简单的指令的使用，而这些指令提供了大量能使我们快速便捷地处理数据，我们务必掌握。另外如果上述有任何问题，请懂哥指教，不过没关系，主要是自己能坚持，更希望有一起学习的同学可以帮我指正，但是如果可以请温柔一点跟我讲，爱与和平是永远的主题，爱各位了。 <img src="https://img-blog.csdnimg.cn/20210524202006430.png#pic_center" alt="在这里插入图片描述">

如果你对网络安全入门感兴趣，那么你点击这里**👉**<img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">
