
--- 
title:  shell超基础入门（超详细） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**努力不一定有回报，但一定会有收获加油！一起努力，共赴美好人生！** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 **♥️小刘私信可以随便问，只要会绝不吝啬，感谢CSDN让你我相遇！** 


**目录**

































哈喽好久不见！大家好我是小刘，因为一些缘故我没有更新博文，也有一个月了，分享我在学习shell的有趣问题，谢谢大家一路陪伴！

### 1.shell的由来

>  
 在 AT&amp;T 的 Dennis Ritchie 和 Ken Thompson 设计 UNIX™ 的时候，他们想要为用户创建一种与他们的新系统交流的方法。 
 那时的操作系统带有命令解释器。命令解释器接受用户的命令，然后解释它们，因而计算机可以使用这些命令。 
 但是 Ritchie 和 Thompson 想要的不只是这些功能，他们想提供比当时的命令解释器具备更优异功能的工具。这导致了 Bourne shell（通称为 sh）的开发，由 S.R. Bourne 创建。自从 Bourne shell 的创建，其它 shell 也被一一开发，如 C shell（csh）和 Korn shell（ksh）。 
 当自由软件基金会想寻求一种免费的 shell，开发者们开始致力于 Bourne shell 以及当时其它 shell 中某些很受欢迎的功能背后的语言。 


### 2.什么是shell

shell是一个命令解释器，它在接受应用程序/用户命令时候调用操作系统内核进行解释，从而达到执行我们所输入的命令，获得结果。另外shell还是一个功能强大的编程语言，易编写，易调试，灵活性高。

shell在硬件与用户之间充当翻译官，这就是他的作用

<img alt="" height="314" src="https://img-blog.csdnimg.cn/d72d7330667a428b9b1a2431a0ef214a.png" width="500">

### 3.shell可以干什么

shell是可以在我们生活或办公中实现自动化运维，自动化办公，编写脚本，等等

##### 补充：

（1）在Linux中我们所输入命令的地方为bash终端控制台如以下：.

<img alt="" height="313" src="https://img-blog.csdnimg.cn/8abfd51a17714cb3b4cc39d8fc789d9a.png" width="500">

（2）shell脚本格式

shell脚本开头#！/bin/bash                  //指定shell脚本中解析器

查看Linux提供的shell解析器命令：

```
cat /etc/shellsd
```

（3）shell脚本的执行方法

bash    shell脚本路径

sh        shell脚本路径

以上为要启动bash子程序中进行运行脚本

source   shell脚本路径

.             shell脚本路径

以上为不用启动子bash程序进行运行脚本

### 4.shell变量

##### 1）常用的系统环境变量

$HOME  $PWD   $SHELL  $VSER

##### 2） 变量中常用命令

echo    $变量               //查看系统变量的值

env                        //查看系统所有的全局变量

set                     //查看当前所有定义的变量

### 5.变量分类

变量中可分为系统变量和用户自定义变量

##### 1）自定义变量

基本语法：

                1.定义变量：变量=变量值           //注意=前后不可以有空格

                2.撤销变量：unset 变量名                

                3.声明静态变量：read  only  变量      //注意不能unset

#### 变量定义规则：

（1）变量名称可以由字母，数字和下划线组成，但是不能以数字开头，环境变量名建议大写

（2）等号两侧不可以有空格

（3）在bash中.变量默认类型都是字符串类型,无法直接进行数值运算

（4）变量的值如果有空格，需要使用双引号或单引号括起来

##### 2）全局变量与局部变量

变量又分全局变量与局部变量

全局变量：在子bash进程中也可以查看到

局部变量：在脱离创建变量的本控制台以后就无法查找到此变量

注意：在父bash中提升全局为全局可见，在子bash中改变量只在bash中生效退出子bash以后还原

exprot   局部变量             //局部变量前无需加$开头



**unset：**

unset     变量                 //将赋予变量的值撤销

**readonly：**

readonly                  //变量及赋值+

### 6.特殊变量

#### $n

1)语法 (功能描述:n 为数字，$0 代表该脚本名称，$1-$9 代表第一到第九个参数，十以$n上的参数，十以上的参数需要用大括号包含，如S$10

#### $#

2)语法 (功能描述:获取所有输入参数个数，常用于循环.判断参数的个数是否正确以及加强脚本的健壮性)。

#### $*、$@

1)本语法 $* (功能描述:这个变量代表命令行中所有的参数，$*把所有的参数看成一个整体)

$@ (功能描述:这个变量也代表命令行中所有的参数,不过$@把每个参数区分对待)

>  
 ♥️关注，就是我创作的动力 
 ♥️点赞，就是对我最大的认可 
 ♥️这里是小刘，励志用心做好每一篇文章，谢谢大家 

