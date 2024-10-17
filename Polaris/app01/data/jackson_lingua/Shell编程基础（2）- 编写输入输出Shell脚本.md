
--- 
title:  Shell编程基础（2）- 编写输入输出Shell脚本 
tags: []
categories: [] 

---
## Shell编程基础（2）- 编写输入输出Shell脚本

### Shell Scripting Essentials (2) – Coding Input &amp; Output Shell Scripts

>  
 假如在Linux系统启动之后，输入每一条系统上需要运行的命令，那么很多工作将无法及时完成。这些命令无疑将影响工作效率。但如果可以将这些命令组合成若干个命令集，就可以更加有效地工作。 
 你可能想过，诸多的Linux命令，看起来很有用，但是需要输入多次去执行，如果能输入一条命令，就能完成所有的任务，那该有多好啊！那么，shell脚本就是你需要的工具。 


传统Linux系统在系统启动期间使用了系统初始化shell脚本，从而运行所需的命令启动相关服务。此外，根据上述的需求，用户还可以在Linux系统创建自己的shell脚本，以便定期自动完成一些任务。

本文简要介绍shell脚本实现输入输出，从而完成交互式脚本任务的过程。

#### 1. 登录Terminal

大多数Linux操作系统采用Bash(即Bourne Again Shell). 当Linux启动需要用户命令行登录时，**Bash shell**已经启动; 用户面对的就是**Terminal**（终端程序）。

```
[root@localhost ~]$

```

此时，以用户名和密码登录到用户账户时，映入眼帘的是这个带有$符号光标的字符串；这说明，用户登陆成功！

#### 2. 创建一个简单的Shell脚本

创建和编辑shell脚本的快捷方法，是使用Vi/Vim编辑器来完成。

关于Vi/Vim编辑器的使用方法，参见文章：

>  
 Shell脚本就像Windows最早开发的批处理文件(***.bat**)一样，可以在一个脚本里执行多条命令，使系统管理自动化。在登录到用户后，可以建立自己的目录（例如：**sh**目录），并且可以开始创建shell脚本。 


```
[root@localhost ~]$ mkdir sh

```

接下来，编写一个最简单的shell脚本（welcome.sh），并在屏幕输出一行欢迎词Welcome to China!

```
echo "Welcome to China!"

```

执行结果如下图所示。 <img src="https://img-blog.csdnimg.cn/01834196904040059d36d40edcd41e08.png" alt="在这里插入图片描述">

#### 3. 使用shell变量

在shell脚本里，通常需要重复使用某些数据（例如： 表示姓名的数据name），而在处理shell脚本过程中，表示该数据的名称或者值可能会不断变化。

因此，需要以一种可重复使用的方式存储shell脚本所使用的数据。

变量就是这样一个合适的选择。例如，声明一个name变量，并赋予它的名称为“Jackson”.

```
name = “Jackson”

```

Shell脚本中变量名称区分大小写，因此，name和NAME或者Name是不一样的。
- 变量的第一部分是变量名（例如：name）；- 变量的第二部分是为该变量名设置的值(例如：“Jackson”)。
变量字母、数字及下划线组成，中间没有空格。

#### 4. 变量包含其它变量的值

如果想要获取因计算机不同变化的信息或者获取日常的信息，使用变量是一个很好的方法。

除了给变量直接赋值外，将一个变量的命令、表达式输出设置到另一个变量，也是非常有用的方法。

如上示例，将uname -n命令的输出设置到MACHINE变量，然后使用括号将NUM_FILES变量设置为当前目录的文件数量，具体做法是将ls命令的输出发送( | )到单词计数命令(wc -l)

```
MACHINE = `uname -n`
NUM_FILES = $(bin/ls | wc -l)

```

变量还可以包含其它变量的值。但我们需要保存一个经常变化的值时，这个功能很有用，示例如下，将BALANCE设置为CurBalance变量的值。

```
BALANCE = “$CurBalance“

```

#### 5. 实训Shell脚本

学习了以上的shell脚本基本知识，我们尝试做一个酒店登记入住的程序，以shell脚本实现。

>  
 一个客人到达酒店后，前台要求客人登记并输入基本信息，包括客人的姓名、ID、年龄。根据这些信息设置变量为name, ID, age, 
 执行脚本时须屏幕输出上述信息，证明注册成功。 


编辑完毕后，将上述脚本保存为**register.sh**, 查看代码如下所示： <img src="https://img-blog.csdnimg.cn/7f930a7cf89649b98fee2ff1bbf6e2f7.png" alt="在这里插入图片描述"> 执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/12cb753036684caa8e2516df932cb452.png" alt="在这里插入图片描述"> 至此，shell脚本执行成功！仅用一行命令完成了酒店客人注册信息。

Linux Shell编程已经开启，喜欢就点赞吧。

技术好文陆续推出，敬请关注。😊

相关阅读：
1. 1. 