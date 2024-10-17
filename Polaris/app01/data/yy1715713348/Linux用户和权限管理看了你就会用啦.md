
--- 
title:  Linux用户和权限管理看了你就会用啦 
tags: []
categories: [] 

---
没想到上一篇能在知乎获得千赞呀，Linux也快期末考试了，也有半个月没有写文章了。这篇主要将Linux下的**用户和权限**知识点再整理一下。

那么接下来就开始吧，如果文章有错误的地方请大家多多包涵，不吝在评论区指正哦~

## 一、Linux下的用户

Linux是一个**多用户的系统**，我们可以多个用户同时登陆Linux~
- 账户**实质**上就是一个**用户在系统上的标识**。
Linux中的账户包括
<li>**用户账户** 
  <ul>- **普通用户账户**：在系统上的任务是进行普通工作- **超级用户账户**（或管理员账户）：在系统上的任务是对普通用户和整个系统进行管理。- 标准组：标准组可以容纳多个用户- 私有组：私有组中只有用户自己
当一个用户同**属于多个组**时，将这些组分为
- **主组**（初始组）：用户登录系统时的组。- **附加组**：登录后可切换的其他组
上面也说了，账户的实质上就是用户在系统上的标识，这些标识是用**文件保存**起来的：
- 用户名和 UID 被保存在`/etc/passwd`文件中，文件权限 `(-rw-r--r--)`- 组和GID 被保存在 `/etc/group`文件中，文件权限`(-r--------)`- 用户口令(密码)被保存在 `/etc/shadow`文件中 ，文件权限`(-rw-r--r-- )`- 组口令被保存在 `/etc/gshadow`文件中 ，文件权限 `(-r--------)`
也就是说：**我们创建的用户，这个用户的信息由不同的文件来保存着**。

<img src="https://img-blog.csdnimg.cn/img_convert/3eeaad292bb1e8aed7c8f1bc4cfcba0c.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/d2097101e0dd81859db15bbf2539a510.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/47afb3ebea158262831359e5e44bc2d0.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/9f470f58014effdac1683fb54931c56d.png" alt="">

有了上面的知识点，下面我来简述一下创建用户的时候会发生什么：
- 用户名和 UID 被保存在 `/etc/passwd` 这个文件中，用户的口令通常用`shadow passwords`保护- 当用户登录时，他们**被分配了一个主目录和一个运行的程序**（通常是 shell）- 若没有指定他所属于的组，RHEL/CentOS就建立一个和**该用户同名的私有组**，且用户被分配到这个私有组中
再来回顾一下：账户的实质上就是用户在系统上的标识，这些标识是用**文件保存**起来的。也就是说：我们是可以**直接编辑修改系统账户文件来维护账户**。
<li>但是**不建议这样做**，如果明确要这样做的话，最好使用命令检测一下你编辑的语法是否有问题： 
  <ul>- `pwck`：验证用户账号文件，认证信息的完整性。该命令检测文件`“/etc/passwd”`和`“/etc/shadow”` 的每行中字段的格式和值是否正确- `grpck`：验证组账号文件，认证信息的完整性。该命令检测文件`“/etc/group”`和`“/etc/gshadow”`的每行中字段的格式和值是否正确。
既然不建议我们直接编辑文件的方式来管理用户，那么Linux是肯定**有现成的命令**给我们使用的：

### 1.1管理Linux用户的命令

**用户管理**：
- `useradd`- `usermod`- `userdel`
**组管理**：
- `groupadd`- `groupmod`- `groupdel`
**批量管理用户**：
- 成批添加/更新一组账户：`newusers`- 成批更新用户的口令：`chpasswd`
**组成员管理**：
<li>向标准组中添加用户 
  <ul>- `gpasswd -a &lt;用户账号名&gt; &lt;组账号名&gt;`- `usermod -G &lt;组账号名&gt; &lt;用户账号名&gt;`- `gpasswd -d &lt;用户账号名&gt; &lt;组账号名&gt;`
**口令维护**(禁用、恢复和删除用户口令)：
<li>**设置用户口令**： 
  <ul>- `passwd [&lt;用户账号名&gt;]`- `passwd -l &lt;用户账号名&gt;`- `passwd -S &lt;用户账号名&gt;`- `passwd -u &lt;用户账号名&gt;`- `passwd -d &lt;用户账号名&gt;`
**口令时效设置**：
- 修改 `/etc/login.defs` 的相关配置参数
<img src="https://img-blog.csdnimg.cn/img_convert/149855cbf92d0aee2f35f877c152caf9.png" alt="">

设置**已存在用户的口令时效**：
- `chage`命令
**用户切换命令**：
<li>`su` 
  <ul>- 直接切换为超级用户- 直接使用 sudo 命令前缀执行系统管理命令。执行系统管理命令时无需知道超级用户的口令，使用普通用户自己的口令即可
更多资料查询：
- –linux权限之su和sudo的差别
**用户相关的命令**：
- `id`：显示用户当前的uid、gid和用户所属的组列表- `groups`：显示指定用户所属的组列表- `whoami`：显示当前用户的名称- `w/who`：显示登录用户及相关信息- `newgrp`：用于转换用户的当前组到指定的组账号，用户必须属于该组才可以正确执行该命令
### 1.2Linux用户的练习题

>  
 用cat命令，观察如下文件：/etc/passwd , /etc/shadow, /etc/group,/etc/gshadow；显示useradd命令添加用户参数的默认值 


<img src="https://img-blog.csdnimg.cn/img_convert/862ac1a38d056f42e9ddce35f960e7d5.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/ed5969cfc5d30c9f475b46fa07ea9479.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/47e32efdd7465cd5b23f3f4f4007e80d.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/7c7561d733eddd4152622386308c93af.png" alt="">

>  
 建立linux账户jkXX（XX为学生学号末两位），要求用户组为users，并设置密码；观察/etc/passwd和/etc/shadow文件的变化；退出root账户，用jkXX账户登录，在其主目录下建立一个myfirst文件，并用长格式列出myfirst文件 


<img src="https://img-blog.csdnimg.cn/img_convert/c8553646c26e70a5b7a6f058a8d732cc.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/fede0b4d82899b9728ad39c20cc10c87.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/7749c14c3cee86a0e4c7525712086aef.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/58ecfdf8ef4d2b8c456681fa7a263922.png" alt="">

>  
 用root账户登录；添加组jsj；设置用户jkXX为jsj组用户，观察/etc/passwd、/etc/group和/etc/gshadow文件变化 


<img src="https://img-blog.csdnimg.cn/img_convert/45d36ca4319f4d5a8d90920761797b6f.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/8aa13179286c175847b8c33c90e28b33.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/b5f21fe5e900a930e37e55435c402086.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/750757ecb610d1d2eaeed49c959b2086.png" alt="">

>  
 添加一个新用户airXX（XX为学生学号末两位），观察新用户airXX的用户id和组id；然后删除该用户，注意不要在命令中加选项，观察用户文件和组文件的变化；观察airXX用户的目录是否存在； 


<img src="https://img-blog.csdnimg.cn/img_convert/2b03628fe7e18861953935ffe5f68371.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/c0c539205cf493faf35f451263b1a850.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/1816cb673957584af1da30348bea9e46.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/6406def8213aed24f23a53077837da13.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/88a2bd82b7360713212368f77c9d24aa.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/f691c4e23e8bdd132bdbf2c9f0779b32.png" alt="">

>  
 shadow文件中密码为*号和！！代表什么？ 


答：`*`代表账户禁用；`！！`代表密码锁定。

>  
 airXX用户组id是多少？这个组是什么类型的组？这样做有什么好处？ 


答：air08用户组id是501，这个组属于私有组。每个未指定组的用户会建立一个同名的组，这样的组称为私有组，只有一个用户，既有利于防止信息泄露，也也有利于防止不合理的授权。总之，有利于安全管理。

>  
 默认情况下删除用户，但却保留了用户的主目录，这样做有什么好处？ 


答：保留用户目录，防止将用户目录下有价值的资料误删除。

>  
 用cat命令，观察文件/etc/passwd；仿照passwd文件的格式，用vi编辑一个新的文件，文件名为userXX（XX为学生学号末两位），文件包括3条记录，用户名分别为jkXX（XX为学生学号末两位），peter，jason，他们的用户id大于1000，组id大于1000，要求peter和jason同组；用命令newusers根据文件userXX的内容批量生成用户；观察/etc/passwd文件的变化。 


<img src="https://img-blog.csdnimg.cn/img_convert/e84ae2a0d1d03121c9c011a5542a7a65.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/1e4ed036cb278e1b15e9211693254516.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/3e54269c78f2124e1a0b5de4ebb6bbe4.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/29692693eee7e6ff45c70db80562ebe6.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/ab1bcf2d21b94c913dffafe2da0ebbad.png" alt="">

>  
 用cat命令，观察文件/etc/shadow；用vi编辑一个新文件，文件名为mimaXX（XX为学生学号末两位），文件包括3条记录，每条记录用户名与上一步骤要求相同，密码自行设置，用户名和密码用冒号：隔开；用命令chpasswd根据文件mimaXX的内容批量生成密码；观察文件/etc/shadow变化；用命令chpasswd -m再次批量生成密码，观察文件/etc/shadow变化； 


<img src="https://img-blog.csdnimg.cn/img_convert/459e5ab572dc53edbe4335dacacb1118.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/a89b54fcee87fa93bf15c8271725c761.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/7e53611eaa3657e62f309bc0654abfc3.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/e56a4779edc42dd42002164b65562b26.png" alt="">

>  
 退出root账户，用jkXX账户登录。退出jkXX账户，返回root账户，观察/etc/shadow文件;用passwd命令锁定用户jkXX，观察/etc/shadow文件变化；然后退出root账户，用jkXX账户登录，是否成功？ 


<img src="https://img-blog.csdnimg.cn/img_convert/d59475846db211951edc1ad9ac763417.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/ba700d73ac993daf31fe0b389f64587e.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/5ea9cec0f1f74a60b82bc0082079b58c.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/637bf1a1605886c1884a08188cbedecb.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/79b6a1f5ed319ee5042b3116efb456ba.png" alt="">

>  
 用chage命令查看peter账户的时间设置；重新设置peter账户的时间，要求两天内不能更改口令，且口令最长的存活期为 90 天，并在口令过期前 5 天通知用户，口令超期7天密码失效；用chage命令再次查看peter账户的时间设置 


<img src="https://img-blog.csdnimg.cn/img_convert/a2b358cbf40cc0410415a668630f2a85.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/a487417f16fc9c49573b01887a4e376f.png" alt="">

>  
 用root账户登录；用su切换到jason账户；用cd进入用户主目录；创建一个新文件abc，用长格式列出abc文件；观察文件的用户和组的属性 


<img src="https://img-blog.csdnimg.cn/img_convert/a01f48e40d6c34cebd7aaf19b96ad330.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/035b079d2cefd0ccca904652def4e590.png" alt="">

>  
 锁定账户后，shadow文件发生了什么变化？ 


答：锁定账户的密码之前会锁定标志！！

>  
 用su切换用户后，建立的新文件文件属于哪个用户？ 


答：新文件属于切换之后的用户。

>  
 两次执行chpasswd命令，结果是否相同？加密算法md5和sha512哪个更安全？ 


答：两次执行chpasswd命令结果不同，默认情况采用sha512加密算法；-m选项时，采用md5加密算法；sha512更安全，因为加密信息长度更长，破解计算量大。

>  
 建立三个普通用户账户，要求如下：用户名分别为jkXX（XX为学生学号末两位），peter，jason，其中jkXX和jason为相同普通组成员；观察/etc/passwd文件的变化。为jkXX账户添加root组； 


<img src="https://img-blog.csdnimg.cn/img_convert/fc54def6dd815e71462eb483b3af2132.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/0dfd354ec12af3277f4b4b80435cf172.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/fc624a2786aee55a1a0cd94a311378e4.png" alt="">

>  
 分别练习id，groups，whoami，who命令，显示当前账户的信息；用su命令切换到jkXX账户，分别练习id，groups，whoami，who命令，显示当前账户的信息。用newgrp切换jkXX账户的组，分别练习id，groups，whoami，who命令，显示当前账户的信息 


<img src="https://img-blog.csdnimg.cn/img_convert/bbdccf71a6f116a606363c4d09b81673.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/b7adb00c5a48f0aea449bcd4ad3f7202.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/7443a1a9dc1557a3e3132def673e522a.png" alt="">

## 二、权限管理

Linux是多用户的操作系统，允许多个用户同时在系统上登录和工作。 为了**确保**系统和用户的**安全**，Linux自然就有自己一套的权限管理机制了！

相信用过Linux的同学在检索文件夹文件的时候常常用到`ls -l`的命令，会出来一大串的数据。这些数据你能读懂了吗？

例如：

```
 drwxr-xr-x   3  osmond   osmond    4096  05-16 13:32   nobp 

```

其实很简单：

<img src="https://img-blog.csdnimg.cn/img_convert/76570e258c8438a275b875a27827e7e6.png" alt="">

其实我们看权限就是看`drwxr-xr-x`这么一串东西，看起来很复杂，但不是的，一下就可以理解了。我们来分解一下：

<img src="https://img-blog.csdnimg.cn/img_convert/7ab745dbaf0812e55a7b5e163ff0e42b.png" alt="">

这9个字符**每3个一组**，组成 3 套 权限控制
- 第一套控制文件**所有者**的访问权限- 第二套控制所有者**所在用户组**的其他成员的访问权限- 第三套控制**系统其他用户**的访问权限
**rwx**分别代表的意思：

<img src="https://img-blog.csdnimg.cn/img_convert/2bdecd2f5049eb7e6102d969cd4cca18.png" alt="">

看到这里来，如果前面的你看懂了，那`drwxr-xr-x`这么一串东西我觉得你很容易就能理解了：
<li>d是文件夹，后面还有9个字母，每3个分成一组，`-`号表示没有。那么这个文件夹的权限就是： 
  <ul>- **对当前用户是可读可写可执行，对同组的用户是可读可执行，对其他的用户是可读可执行**
是不是很简单？？`r-read,w-write,x-execute`，很好理解的。

对于这些rwx命令为了方便还可以换成八进制的数据来表示，我相信大家看完下面的demo也知道其实就这么一回事了：

<img src="https://img-blog.csdnimg.cn/img_convert/553be73919679f0e58fa3ebedb7f2ae8.png" alt="">

**权限的优先顺序**：
- 如果UID匹配，就应用用户属主（user）权限- 否则，如果GID匹配，就应用组（group）权限- 如果都不匹配，就应用其它用户（other）权限- **超级用户root具有一切权限**，无需特殊说明
### 2.1管理Linux权限的常用命令
<li>`chmod` 
  <ul>- 改变文件或目录的权限- 改变文件或目录的属主（所有者）- 改变文件或目录所属的组- 设置文件的缺省生成掩码
例子：

<img src="https://img-blog.csdnimg.cn/img_convert/112d84c36fcff0dcb601509217090d28.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/2a45f65e68b9cac5b915f72c415b417d.png" alt="">

### 2.2权限扩展知识

上面提到了umask属性，它用来做这样的东西的：默认生成掩码告诉系统当创建一个文件或目录时**不应该赋予其哪些权限**。
- 默认的umask的值是022，我们看一下下面的例子应该就能懂了：
<img src="https://img-blog.csdnimg.cn/img_convert/5cc69032d85e2aed628b19cfc6e83b55.png" alt="">

除了上面所说的权限之外，Linux还提供了**三种特殊的权限**：
- SUID：使用命令的**所属用户的权限来运行**，而不是命令执行者的权限- SGID：使用命令的**组权限来运行**。- Sticky-bit：目录中的文件**只能被文件的所属用户和root用户删除**。
它们是这样表示的：
- SUID和SGID用s表示；Sticky-bit用t表示- SUID是占用属主的x位置来表示- SGID是占用组的x位置来表示- sticky-bit是占用其他人的x位置来表示
例如：`drwxrwxrwt 5 root root 4096 06-18 01:01 /tmp`它就拥有sticky-bit权限。`-rwsr-xr-x 1 root root 23420 2010-08-11 /usr/bin/passwd`它就拥有SUID权限

SUID，SGID，sticky-bit同样也有数字的表示法：

<img src="https://img-blog.csdnimg.cn/img_convert/2b1aefe587be8e18e971b7a708ba8cb9.png" alt="">

使用的例子：

<img src="https://img-blog.csdnimg.cn/img_convert/166624b8d511b12bc34711fe5d257a38.png" alt="">

Linux内核中有大量安全特征。EXT2/3/4**文件系统的扩展属性**（Extended Attributes）可以在某种程度上保护系统的安全

**常见的扩展属性：**
<li>A（Atime）：告诉系统不要修改对这个文件的最后访问时间。 
  <ul>- **使用A属性可以提高一定的性能**。- **使用S属性能够最大限度的保障文件的完整性**。- **a属性和i属性对于提高文件系统的安全性和保障文件系统的完整性有很大的好处**。
**常用命令**：
- 显示扩展属性：`lsattr [-adR] [文件|目录]`- 修改扩展属性：`chattr [-R] [[-+=][属性]] &lt;文件|目录&gt;`
### 2.3权限管理练习题

>  
 用root账户登录，创建一个文件aaaXX（XX为学生学号末两位），用长格式查看文件权限；用chmod命令，文字设定法，给aaaXX文件同组增加写属性，观察结果；用chmod命令，数字设定法，给aaaXX文件设置权限为766，观察结果； 


<img src="https://img-blog.csdnimg.cn/img_convert/477d5adf441e6d90188ae35b620b35e8.png" alt="">

>  
 切换到peter账户，查看当前umask是多少，观察结果；创建一个目录foldXX（XX为学生学号末两位），查看其权限；创建一个新文件bbb，查看其权限；改变unmask为066，创建一个新文件ccc，查看其权限 


<img src="https://img-blog.csdnimg.cn/img_convert/8f1c76181fb5de4ecd130bd7045d68e4.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/b719bcced378a8aaa8fb65c0b01f2ba8.png" alt="">

>  
 切换到jkXX账户；创建一个文件myfile，观察其属性；用chgrp改变文件myfile组属性为root；试着去改变文件myfile主属性为root，可以吗？切换到root账户，改变文件myfile主属性为root，观察结果 


<img src="https://img-blog.csdnimg.cn/img_convert/12427c07e5dbaa16fe58440cd39e4136.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/5c2b24ae2dd30b2678f43e81798a71b3.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/2eea1b4aa4b608dc2d156100a389d54e.png" alt="">

>  
 数字设定766代表文件权限是什么？ 


答：766代表文件权限为`rwx-rw-rw-`

>  
 为什么用jkXX账户改变文件myfile的属主失败？ 


答：因为chown只有root账户才可以使用

>  
 Umask为022和066对新创建的文件属性影响一样吗？为什么？ 


答：影响当然不一样，umask定义的是默认不应该获得的权限，066比022转换成为二进制数后，多了两个限制比特位。

>  
 以root账户登录，复制/usr/bin/dir文件到用户主目录，用长格式列出，设置文件的suid和sguid为1,用长格式列出；切换帐号为jkXX，运行复制过来的文件dir（注意运行当前路径下的文件要带上路径，例如./dir）； 


<img src="https://img-blog.csdnimg.cn/img_convert/b7c10405348209618768b9cbee1deb8f.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/b6e1c6ec10d785a886c605aaebf97bce.png" alt="">

>  
 切换到jkXX账户，进入/tmp目录，建立文件夹myfold，设置文件夹myfold权限为777，并且sgid和sticky-bit为1，用长格式列出，观察myfold的属性；进入myfold，创建新文件aaa，设置属性为任何人可读可写，用长格式列出；切换到jason账户，进入/tmp/myfold目录，删除aaa文件，是否可以删除？ 


<img src="https://img-blog.csdnimg.cn/img_convert/3efe7e92a6f14a5c5fbcd96d815235b7.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/97d13bed3b64cc06da7f6abf7fdf9ee8.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/a580d130e587eacf3ad67c4226fd6a3b.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/8129a76d72c32a7799a4a41ae05ff954.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/a5c33e0e7c894071d07bf17836041fe7.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/119548455c39daccc38fc4e8a437619c.png" alt="">

>  
 root账户，进入用户主目录；创建一个文件bbb文件，查看文件的扩展属性；给文件bbb添加扩展属性i，然后试着删除该文件，是否成功，怎样才能删除；创建一个ccc文件，给文件ccc添加扩展属性a，用长格式列表/bin目录并重定向输出到ccc文件，观察ccc文件长度的变化，用长格式列表/etc目录，并重定向输出到ccc文件，是否成功 


<img src="https://img-blog.csdnimg.cn/img_convert/ad36aa822fab735c086403988b9c3b0f.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/067338d2561abc64a3b1c085ad4522f5.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/2657f806489768c67b81fdf7f71149b9.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/4c0c97187b777dd7eb9134f8dccd98fd.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/c04abb3b94ac68a4cdc0cec5349b2f36.png" alt="">

>  
 切换到jkXX账户，在/tmp目录下创建一个目录myshare，用getfacl查看myshare目录文件访问控制表；设置myshare文件夹对于jason用户权限为rwx，查看文件访问控制表的变化；切换到jason账户，进入myshare文件创建文件yyy，是否成功；切换到peter账户，进入myshare文件创建文件zzz，是否成功，为什么？ 


<img src="https://img-blog.csdnimg.cn/img_convert/70ce6bac13168cb5efc90c9ca6809f17.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/1ab12464e4829b1863a6db875eb6445d.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/22d0a5e294e865d83944257e6ae2756b.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/789d3fd9c4524f97e75ff0ab7dfba18c.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/6491bd3bd4e0346691d0c57957b626b3.png" alt="">

>  
 myfold目录下，为什么jason账户不能删除一个任何人都可读可写的文件？ 


答：因为文件所在的文件夹myfold被它的所属者jk08设置了stickybit位，该文件夹下面的所有文件，只有文件所属者，以及root用户才能删除。

>  
 为什么peter账户在在myshare文件夹里面不能创建文件？ 


答：因为myshare文件夹，属于jk08用户，只有jk08对该目录具备rwx权限。此外，采用facl的方式，给jason用户开放了该目录的rwx访问权限；peter既不是文件夹的拥有者，也没有在facl中开放rwx权限；依据权限设置情况，peter只有该文件夹的rx权限。因此，不能创建文件。

>  
 添加扩展属性a后，用重定向将输出内容给ccc文件，可能会失败，怎样才能输出成功？ 


答：应该采用追加方式的重定向&gt;&gt;，可以在文件末尾添加内容，这样才符合文件扩展属性a的安全规定。

## 三、总结

本文主要是总结了Linux下操作用户和权限的知识~~~这两个知识点在Linux下也是很重要的，是学习Linux的基础~

**继续完善上一次的思维导图**：

<img src="https://img-blog.csdnimg.cn/img_convert/da0a35b821aa8a6ddabb333fcecc949d.png" alt="">

如果文章有错的地方欢迎指正，大家互相交流。习惯在微信看技术文章，想要获取更多的Java资源的同学，可以关注微信公众号:Java3y

**文章的目录导航**：
- 
>  
 <blockquote> 
  ，可以在文件末尾添加内容，这样才符合文件扩展属性a的安全规定。 
 

## 三、总结

本文主要是总结了Linux下操作用户和权限的知识~~~这两个知识点在Linux下也是很重要的，是学习Linux的基础~

**继续完善上一次的思维导图**： **题外话**

随着信息技术的快速发展和互联网的普及，IT行业 成为一个非常热门的领域，也是目前就业前景非常广阔的领域之一。

IT行业是一个非常庞大和多样化的行业，包括软件开发、网络安全、数据分析、云计算等等领域。因此，就业前景也是非常广泛和多样化的，不同的领域和职位都具有不同的就业前景和发展机会。

在软件开发领域，由于软件已经成为现代社会不可或缺的一部分，因此对软件开发人才的需求也越来越大。特别是在移动应用、大数据、人工智能等领域，软件开发人才的需求更是迅速增长。因此，软件开发人才的就业前景非常广阔，尤其是那些熟练掌握多种编程语言和技术的人才。

有幸看到一篇这样一组数据。

<img src="https://img-blog.csdnimg.cn/c3114b9c3bf947adb177b7aaf91e1be5.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/d5f06d6b9945fd6e8a5f92a0198e5446.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/9cf857398f52a97ff49d437ac5fe690a.png" alt="">

根据这些我不得总结，it行业确实人才紧缺，

##### 行业发展空间大，岗位非常多

网络安全行业产业以来，随即新增加了几十个网络安全行业岗位︰网络安全专家、网络安全分析师、安全咨询师、网络安全工程师、安全架构师、安全运维工程师、渗透工程师、信息安全管理员、数据安全工程师、网络安全运营工程师、网络安全应急响应工程师、数据鉴定师、网络安全产品经理、网络安全服务工程师、网络安全培训师、网络安全审计员、威胁情报分析工程师、灾难恢复专业人员、实战攻防专业人员…

##### 职业增值潜力大

网络安全专业具有很强的技术特性，尤其是掌握工作中的核心网络架构、安全技术，在职业发展上具有不可替代的竞争优势。

随着个人能力的不断提升，所从事工作的职业价值也会随着自身经验的丰富以及项目运作的成熟，升值空间一路看涨，这也是为什么受大家欢迎的主要原因。

从某种程度来讲，在网络安全领域，跟医生职业一样，越老越吃香，因为技术愈加成熟，自然工作会受到重视，升职加薪则是水到渠成之事。

## 学习资料分享

当然，**只给予计划不给予学习资料的行为无异于耍流氓**，### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

**👉网安（嘿客）全套学习视频👈**

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

#### 

#### <img src="https://img-blog.csdnimg.cn/img_convert/d1c617b78ee48eda7601e5b803e69276.png" alt="img">

#### **👉网安（嘿客红蓝对抗）所有方向的学习路线****👈**

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

#### <img src="https://img-blog.csdnimg.cn/img_convert/de55dfd737dae0cf88e416d0454b17a8.png" alt="img">

#### 学习资料工具包

压箱底的好资料，全面地介绍网络安全的基础理论，包括逆向、八层网络防御、汇编语言、白帽子web安全、密码学、网络安全协议等，将基础理论和主流工具的应用实践紧密结合，有利于读者理解各种主流工具背后的实现机制。

<img src="https://img-blog.csdnimg.cn/9609a53465cf4253b492a5185896fa71.png" alt="在这里插入图片描述">

**面试题资料**

独家渠道收集京东、360、天融信等公司测试题！进大厂指日可待！ <img src="https://img-blog.csdnimg.cn/f5f267c281c543fb9cc9af53b9003a37.png" alt="在这里插入图片描述">

#### **👉<strong><strong>嘿客必备开发工具**</strong>👈</strong>

工欲善其事必先利其器。学习**嘿**客常用的开发软件都在这里了，给大家节省了很多时间。

#### 这份完整版的网络安全（**嘿**客）全套学习资料已经上传至CSDN官方，朋友们如果需要点击下方链接**也可扫描下方微信二v码获取网络工程师全套资料**【保证100%免费】

#### <img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**
