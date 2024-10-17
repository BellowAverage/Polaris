
--- 
title:  Computer：少儿编程—每个人都应该学习编程，它能教你如何思考—编程入门的简介(编程语言的特点&种类&开发工具&对比人类语言)、编程应用、编程意义之详细攻略 
tags: []
categories: [] 

---
Computer：少儿编程—每个人都应该学习编程，它能教你如何思考—编程入门的简介(编程语言的特点&amp;种类&amp;开发工具&amp;对比人类语言)、编程应用、编程意义之详细攻略



>  
 **导读**：乔布斯说，每个人都应该学习编程，因为他教会你思考的方式。因为程序就是对现实事物的抽象，而且，按照写好的逻辑运行。所以，编程能够锻炼我们的抽象思维能力和逻辑思维能力。 "Everyone should know how to program a computer, because it teaches you how to think."—Steve Jobs "You might not think that programmers are artists but programming is an extremely creative profession. It is logic-base creativity."—John Romero 你可能不认为程序员是艺术家，但编程是一个极具创造力的职业。它是基于逻辑的创造力。 "Most good programmers do programming not because they expect to get paid or get adulation by the public, but because it is fun."—Linus Torvalds 大多数优秀的程序员从事编程，不是因为他们希望得到报酬或受到公众的追捧，而是因为它很有趣。 "First, solve the problem. Then, write the code."—John Johnson 首先，解决问题。然后，编写代码。 




**目录**











































**相关文章**



## 电脑编程相关的基础知识

### 1、程序、脚本、软件执行原理

CPU可以执行二进制代码 这里是由硬件完成，是硬件固有的属性，是一切的开始。

****<strong><em>编译器：****</em></strong>以gcc 举例，gcc是一个程序。它可以将c语言代码变成二进制代码，这种变化的过程叫做编译，然后由CPU执行这些二进制代码。****<strong><em>解释器****</em></strong>：每一种脚本语言都有自己的解释器，它可以执行脚本。所谓的执行就是这个解释器，根据你的脚本执行逻辑，如果需要的话调用写好的函数(程序)。可简单的理解为解释器是一个高级的CPU，他可以执行脚本代码。

**程序和脚本最大的区别**：就是一个由CPU执行，一个由解释器执行。
<td style="vertical-align:top;width:41pt;"> ****<strong><em>程序****</em></strong> </td><td style="vertical-align:top;width:412pt;"> 有编译出来的二进制码才叫程序。 </td>

有编译出来的二进制码才叫程序。
<td style="vertical-align:top;width:41pt;"> ****<strong><em>脚本****</em></strong> </td><td style="vertical-align:top;width:412pt;"> 程序员使用； </td>

程序员使用；
<td style="vertical-align:top;width:41pt;"> ****<strong><em>软件****</em></strong> </td><td style="vertical-align:top;width:412pt;"> 客户使用，软件由程序构成。程序通过编译器编译源代码后由硬件直接执行二进制文件 </td>

客户使用，软件由程序构成。程序通过编译器编译源代码后由硬件直接执行二进制文件



### **<strong>2、认知操作系统OS**</strong>

操作系统的作用是管理和控制计算机系统中的硬件和软件资源，例如，它负责直接管理计算机系统的各种硬件资源，如对CPU、内存、磁盘等的管理，同时对系统资源所需的优先次序进行管理。操作系统还可以控制设备的输入、输出以及操作网络与管理文件系统等事务。同时，它也负责对计算机系统中各类软件资源的管理。 例如各类应用软件的安装、设置运行环境等。操作系统与计算机硬件软件关系图如下。合理组织计算机系统的工作流程，以便有效的利用这些资源为使用者提供一个功能强大、使用方便的操作及使用环境，从而在计算机系统（硬件）与使用者之间起到接口的作用。目前PC计算机（微机）上比较常见的操作系统由Windows、Linux、DOS、Unix。

<img alt="" height="194" src="https://img-blog.csdnimg.cn/173ff53427614671ae3743873235e8b2.png" width="400">

<img alt="" height="379" src="https://img-blog.csdnimg.cn/04216301730e4d0b8cfb2497f3f0217f.png" width="392">



#### (1)、常见操作系统简介

这些操作系统底层，对于文件系统的访问工作原理是不一样的，因此你可能就要针对不同的系统来考虑使用哪些文件系统模块，这样的做法是非常不友好，而且非常麻烦，因为这样就意味着当你的程序运行环境一改变，你就要相应的去修改大量的代码来应付。 1)、像Python这种跨平台的语言，同样的代码可以在不同的操作系统下运行得到同样的结果。
<td style="vertical-align:top;width:45px;"> **<strong>系统**</strong> </td><td style="vertical-align:top;width:67px;"> **<strong>时间**</strong> </td><td style="vertical-align:top;width:590px;"> **<strong>简介**</strong> </td>

**<strong>时间**</strong>
<td style="vertical-align:top;width:45px;"> **<strong>Unix**</strong> </td><td style="vertical-align:top;width:67px;"> 1969年 </td><td style="vertical-align:top;width:590px;"> 在AT&amp;T的贝尔实验室诞生。 多用户、多任务操作系统 AIX：IBM的操作系统， HP NUIX：惠普公司 SUN OS：Sunny公司 SCO UNIX：最初是收费的，一套大概2万块左右 **<strong>Unix的五大优秀特性  **</strong> ****<strong><em>技术成熟，可靠性高****</em></strong>：使用Unix系统时，即时运行若干年也无需重启，它依然可以工作得非常好。毫不夸张地说，只要计算机硬件不坏，Unix就很难出问题。   ****<strong><em>极强的可伸缩性****</em></strong>：Unix支持的CPU处理器体系架构非常多，包括Intel/AMD及HP-PA、MIPS、PowerPC、UltraSPARC、ALPHA等RISC芯片，以及SMP、MPP等技术。   ****<strong><em>强大的网络功能****</em></strong>：Internet互联最重要的协议TCP/IP就是在Unix上开发和发展起来的。此外，Unix还支持非常多的常用网络通信协议，如NFS、DCE、IPX/SPX、SLIP、PPP等。   ****<strong><em>强大的数据库支持能力****</em></strong>：Oracle、DB2、Sybase、Informix等大型数据库，都把Unix作为其主要的数据库开发和运行平台，一直到目前为止，依然如此。   ****<strong><em>强大的开发功能****</em></strong>：正是Unix促使了C语言的诞生，并相互促进与发展，成为当时工程师的首选操作系统和开发环境。互联网早期有重大意义的软件新技术的出现几乎都在Unix上，例如：TCP/IP、WWW、JAVA、XML等。 <img alt="" height="164" src="https://img-blog.csdnimg.cn/3ab9075b0ecf4c58b38ecbd0c7aaeac3.png" width="327">  </td>

1969年

多用户、多任务操作系统

HP NUIX：惠普公司

SCO UNIX：最初是收费的，一套大概2万块左右

****<strong><em>技术成熟，可靠性高****</em></strong>：使用Unix系统时，即时运行若干年也无需重启，它依然可以工作得非常好。毫不夸张地说，只要计算机硬件不坏，Unix就很难出问题。  

****<strong><em>强大的网络功能****</em></strong>：Internet互联最重要的协议TCP/IP就是在Unix上开发和发展起来的。此外，Unix还支持非常多的常用网络通信协议，如NFS、DCE、IPX/SPX、SLIP、PPP等。  

****<strong><em>强大的开发功能****</em></strong>：正是Unix促使了C语言的诞生，并相互促进与发展，成为当时工程师的首选操作系统和开发环境。互联网早期有重大意义的软件新技术的出现几乎都在Unix上，例如：TCP/IP、WWW、JAVA、XML等。


<td style="vertical-align:top;width:45px;"> **<strong>DOS**</strong> </td><td style="vertical-align:top;width:67px;"> 1979年 </td><td style="vertical-align:top;width:590px;"> Disk Operating System 后代发展为Windows命令提示符 </td>

1979年

后代发展为Windows命令提示符
<td style="vertical-align:top;width:45px;"> **<strong>Mac**</strong> </td><td style="vertical-align:top;width:67px;"> 1984年 </td><td style="vertical-align:top;width:590px;"> 使用独立的macOS系统，最新的macOS系列基于NeXT系统开发，不支持兼容。是一套完备而独立的操作系统。 </td>

1984年
<td style="vertical-align:top;width:45px;"> **<strong>Windows**</strong> </td><td style="vertical-align:top;width:67px;"> 1985年11月20日 </td><td style="vertical-align:top;width:590px;"> Microsoft Windows是美国微软公司以图形用户界面为基础研发的操作系统，主要运用于计算机、智能手机等设备。 Win NT→Win Server 2000→ 最初微软打击Linux系统的，比如SQL Server、WEB、.NET等不支持Linux系统，两年前，才开始支持Linux。 </td>

1985年11月20日

Win NT→Win Server 2000→
<td style="vertical-align:top;width:45px;"> **<strong>Linux**</strong> </td><td style="vertical-align:top;width:67px;"> 1991年10月5日 </td><td style="vertical-align:top;width:590px;"> 免费、开源、可靠、高性能、安全、稳定、多平台。 Linux系统命令等同于UNIX，差别非常少。Linux操作系统的诞生、发展和成长过程始终依赖着五个重要支柱：Unix操作系统、MINIX操作系统、GNU计划、POSIX标准和Internet网络。Redhat <img alt="" height="123" src="https://img-blog.csdnimg.cn/f7eb77aa85fe43a8b23a559e4567aee7.png" width="123">  </td>

1991年10月5日

Linux系统命令等同于UNIX，差别非常少。Linux操作系统的诞生、发展和成长过程始终依赖着五个重要支柱：Unix操作系统、MINIX操作系统、GNU计划、POSIX标准和Internet网络。Redhat





#### (2)、Windows 对比Linux
<td style="background-color:#555555;width:30.15pt;"> **<strong>比较**</strong> </td><td style="background-color:#555555;width:282px;"> **<strong>Windows**</strong> </td><td style="background-color:#555555;width:347px;"> **<strong>Linux**</strong> </td>

**<strong>Windows**</strong>
<td style="background-color:#ffffff;width:30.15pt;"> **<strong>界面**</strong> </td><td style="background-color:#ffffff;width:282px;"> 界面统一，外壳程序固定所有Windows程序菜单几乎一致，快捷键也几乎相同 </td><td style="background-color:#ffffff;width:347px;"> 图形界面风格依发布版不同而不同，可能互不兼容。GNU/Linux的终端机是从UNIX传承下来，基本命令和操作方法也几乎一致。 </td>

界面统一，外壳程序固定所有Windows程序菜单几乎一致，快捷键也几乎相同
<td style="background-color:#f6f4f0;width:30.15pt;"> **<strong>驱动程序**</strong> </td><td style="background-color:#f6f4f0;width:282px;"> 驱动程序丰富，版本更新频繁。默认安装程序里面一般包含有该版本发布时流行的硬件驱动程序，之后所出的新硬件驱动依赖于硬件厂商提供。对于一些老硬件，如果没有了原配的驱动有时很难支持。另外，有时硬件厂商未提供所需版本的Windows下的驱动，也会比较头痛。 </td><td style="background-color:#f6f4f0;width:347px;"> 由志愿者开发，由Linux核心开发小组发布，很多硬件厂商基于版权考虑并未提供驱动程序，尽管多数无需手动安装，但是涉及安装则相对复杂，使得新用户面对驱动程序问题（是否存在和安装方法）会一筹莫展。但是在开源开发模式下，许多老硬件尽管在Windows下很难支持的也容易找到驱动。HP、Intel、AMD等硬件厂商逐步不同程度支持开源驱动，问题正在得到缓解。 </td>

驱动程序丰富，版本更新频繁。默认安装程序里面一般包含有该版本发布时流行的硬件驱动程序，之后所出的新硬件驱动依赖于硬件厂商提供。对于一些老硬件，如果没有了原配的驱动有时很难支持。另外，有时硬件厂商未提供所需版本的Windows下的驱动，也会比较头痛。
<td style="background-color:#ffffff;width:30.15pt;"> **<strong>使用**</strong> </td><td style="background-color:#ffffff;width:282px;"> 使用非常简单，容易入门。图形化界面对没有计算机背景知识的用户，使用十分有利。 </td><td style="background-color:#ffffff;width:347px;"> 图形界面使用简单，容易入门。但是文字界面，需要学习才能掌握。 </td>

使用非常简单，容易入门。图形化界面对没有计算机背景知识的用户，使用十分有利。
<td style="background-color:#f6f4f0;width:30.15pt;"> **<strong>学习**</strong> </td><td style="background-color:#f6f4f0;width:282px;"> 系统构造复杂、变化频繁，且知识、技能淘汰快，深入学习困难。 </td><td style="background-color:#f6f4f0;width:347px;"> 系统构造简单、稳定，且知识、技能传承性好，深入学习相对容易。 </td>

系统构造复杂、变化频繁，且知识、技能淘汰快，深入学习困难。
<td style="background-color:#ffffff;width:30.15pt;"> **<strong>软件**</strong> </td><td style="background-color:#ffffff;width:282px;"> 每一种特定功能可能都需要商业软件的支持，需要购买相应的授权。 </td><td style="background-color:#ffffff;width:347px;"> 大部分软件都可以自由获取，同样功能的软件选择较少。 </td>

每一种特定功能可能都需要商业软件的支持，需要购买相应的授权。







## **编程是什么**

<img alt="" height="222" src="https://img-blog.csdnimg.cn/e0b26f1b59e843dfbac1fcb9e4bdbfb2.png" width="467">

        简而言之，编程是用代码指挥计算机做事，代码是给计算机的指令。         编程，即编定程序。就是让计算机代码解决某个问题，对某个计算体系规定一定的运算方式，使计算体系按照该计算方式运行，并最终得到相应结果的过程。         为了使计算机能够理解人的意图，人类就必须将需解决的问题的思路、方法和手段，通过计算机能够理解的形式告诉计算机，使得计算机能够根据人的指令一步一步去工作，完成某种特定的任务。这种人和计算体系之间交流的过程就是编程。





### **1、编程语言的三大种类(机器语言、汇编语言、高级语言)**

**<strong>A、面向机器**</strong>**<strong>(**</strong>**<strong>机器语言、汇编语言**</strong>**<strong>)：**</strong> 低级语言：机器语言(二级制语言)、汇编语言、符号语言。 汇编语言和机器语言实质是相同的，都是直接对硬件操作，只不过指令采用了英文缩写的标识符，容易识别和记忆。

**B、面向过程/面向问题/面向对象(<strong>高级语言**)：</strong> 高级语言，是绝大多数编程者的选择，包括了很多编程语言，如流行的vb、vc、foxpro、delphi等，这些语言的语法、命令格式都各不相同。 高级语言所编制的程序不能直接被计算机识别，必须经过转换才能被执行，按转换方式可将它们分为两类：****<strong><em>解释类****</em></strong>、****<strong><em>编译类****</em></strong>。但是，如今大多数的编程语言都是编译型的，例如VisualBasic、VisualC++、VisualFoxpro、Delphi等。



#### **(1)、****机器语言****—机器指令—占用内存少、通用性差**
<td style="vertical-align:top;width:42.45pt;"> **<strong>简介**</strong> </td><td style="vertical-align:top;width:283.8pt;"> 在计算机应用的初期，程序员使用机器的指令系统来编写计算机应用程序，这种程序称为机器语言程序。 </td>

在计算机应用的初期，程序员使用机器的指令系统来编写计算机应用程序，这种程序称为机器语言程序。
<td style="vertical-align:top;width:42.45pt;"> **<strong>原理**</strong> </td><td style="vertical-align:top;width:283.8pt;"> 在计算机系统中，一条机器指令规定了计算机系统的一个特定动作。 一个系列的计算机在硬件设计制造时就用了若干指令规定了该系列计算机能够进行的基本操作，这些指令一起构成了该系列计算机的指令系统。 </td>

在计算机系统中，一条机器指令规定了计算机系统的一个特定动作。
<td style="vertical-align:top;width:42.45pt;"> **<strong>特点**</strong> </td><td style="vertical-align:top;width:283.8pt;"> 使用机器语言编写的程序，由于每条指令都对应计算机一个特定的基本动作，所以程序占用内存少、执行效率高。 缺点也很明显，编程工作量大，容易出错；依赖具体的计算机体系，因而程序的通用性、移植性都很差。 </td>

使用机器语言编写的程序，由于每条指令都对应计算机一个特定的基本动作，所以程序占用内存少、执行效率高。



#### **(2)、非机器语言的****执行原理****—借助转换才能识别**

        计算机，对除机器语言以外的源程序不能直接识别、理解和执行，都必须通过某种方式转换为计算机能够直接执行的。这种将高级程序设计语言编写的源程序转换到机器目标程序的方式有两种：编译方式和解释方式。**<strong>(1)、**</strong>**<strong>编译方式**</strong>：首先通过一个对应于所用程序设计语言的编译程序对源程序进行处理，经过对源程序的词法分析、语法分析、语意分析、代码生成和代码优化等阶段，将所处理的源程序转换为用二进制代码表示的目标程序，然后通过连接程序处理将程序中所用的函数调用、系统功能调用等嵌入到目标程序中，构成一个可以连续执行的二进制执行文件。调用这个执行文件，就可以实现程序员在对应源程序文件中所指定的相应功能。**<strong>(2)、**</strong>**<strong>解释方式**</strong>：计算机对高级语言书写的源程序一边解释一边执行，不能形成目标文件和执行文件。





#### **(3)、****汇编语言****—助记符号&amp;汇编程序翻译执行—仍然****低效率****、不可替代的特性(接控制硬件的程序上)**
<td style="vertical-align:top;width:42.45pt;"> **<strong>简介**</strong> </td><td style="vertical-align:top;width:283.8pt;"> 为了解决使用机器语言编写应用程序所带来的一系列问题，人们首先想到使用助记符号来代替不容易记忆的机器指令。 </td>

为了解决使用机器语言编写应用程序所带来的一系列问题，人们首先想到使用助记符号来代替不容易记忆的机器指令。
<td style="vertical-align:top;width:42.45pt;"> **<strong>原理**</strong> </td><td style="vertical-align:top;width:283.8pt;"> 这种助记符号来表示计算机指令的语言称为符号语言，也称汇编语言。 在汇编语言中，每一条用符号来表示的汇编指令与计算机机器指令一一对应；记忆难度大大减少了，不仅易于检查和修改程序错误，而且指令、数据的存放位置可以由计算机自动分配。 用汇编语言编写的程序称为源程序，计算机不能直接识别和处理源程序，必须通过某种方法将它翻译成为计算机能够理解并执行的机器语言，执行这个翻译工作的程序称为汇**<strong>编程序**</strong>。 </td>

这种助记符号来表示计算机指令的语言称为符号语言，也称汇编语言。

用汇编语言编写的程序称为源程序，计算机不能直接识别和处理源程序，必须通过某种方法将它翻译成为计算机能够理解并执行的机器语言，执行这个翻译工作的程序称为汇**<strong>编程序**</strong>。
<td style="vertical-align:top;width:42.45pt;"> **<strong>特点**</strong> </td><td style="vertical-align:top;width:283.8pt;"> 使用汇编语言编写计算机程序，程序员仍然需要十分熟悉计算机系统的硬件结构，所以从程序设计本身上来看仍然是低效率的、繁琐的。 但正是由于汇编语言与计算机硬件系统关系密切，在某些特定的场合，如对时空效率要求很高的系统核心程序以及实时控制程序等，迄今为止汇编语言仍然是十分有效的程序设计工具。 但它有不可替代的特性，比如一些单片机或者一些直接控制硬件的程序就一定要用汇编语言。 </td>

使用汇编语言编写计算机程序，程序员仍然需要十分熟悉计算机系统的硬件结构，所以从程序设计本身上来看仍然是低效率的、繁琐的。

但它有不可替代的特性，比如一些单片机或者一些直接控制硬件的程序就一定要用汇编语言。







#### **(4)、****高级语言****—近似人类语言&amp;两大类&amp;转换执行—相对简单、通用性好**
<td style="vertical-align:top;width:42.45pt;"> **<strong>简介**</strong> </td><td style="vertical-align:top;width:283.8pt;"> 高级语言是一类接近于人类的自然语言和数学语言的程序设计语言的统称。按照其程序设计的出发点和方式不同，高级语言分为了面向过程的语言和面向对象的语言： (1)、PHP同时支持面向对象和面向过程的开发，使用上非常灵活。 **<strong>面向过程的语言**</strong>：如C语言、Fortran语言、汉语程序设计语言等； **<strong>向对象的语言**</strong>：如C++、VB、C#、Java语言等为代表。支持“程序是相互联系的离散对象集合”，这样一种新的程序设计思维方式，具有封装性、继承性和多态性等特征。 </td>

高级语言是一类接近于人类的自然语言和数学语言的程序设计语言的统称。按照其程序设计的出发点和方式不同，高级语言分为了面向过程的语言和面向对象的语言：

**<strong>面向过程的语言**</strong>：如C语言、Fortran语言、汉语程序设计语言等；
<td style="vertical-align:top;width:42.45pt;"> **<strong>原理**</strong> </td><td style="vertical-align:top;width:283.8pt;"> 高级语言按照一定的语法规则，由表达各种意义的运算对象和运算方法构成。 用高级语言编写的程序称为源程序，计算机系统不能直接理解和执行，必须通过一个语言处理系统将其转换为计算机系统能够认识、理解的目标程序才能被计算机系统执行。 </td>

高级语言按照一定的语法规则，由表达各种意义的运算对象和运算方法构成。
<td style="vertical-align:top;width:42.45pt;"> **<strong>特点**</strong> </td><td style="vertical-align:top;width:283.8pt;"> 使用高级语言编写程序的优点是：编程相对简单、直观、易理解、不容易出错； 高级语言是独立于计算机的，因而用高级语言编写的计算机程序通用性好，具有较好的移植性。 </td>

使用高级语言编写程序的优点是：编程相对简单、直观、易理解、不容易出错；







### **2、编程语言对比人类语言**

        相比人类的日常交流用语，代码语句的主要特点是简洁、无歧义。实际上，代码语句和军训指令很像，比如立正、向左转、齐步走。但是，计算机不接受歧义和不确定，比如最漂亮的人，如果要给出上面的指令，必须提前为计算机定义好—谁是最漂亮的人，或者给定计算机可以进行量化的属性，比如身高=1、眼睛半径=2、发量=3等等。         如果代码、语句真像军训指令一样种类有限，还贼简洁，那好像不能完成多少事情？         但实际上，并非如此，         第一个原因是，因为指令可以针对不同的对象产生不同的效果；         第二个原因是，指令组合起来，也能帮助达成目标。就像前进，朝某方向转、停下，三类指令组合起来，其实已经足够可以指挥到达2D平面上任意地点，         第三个原因是，也是更重要的是，计算机正常逻辑控制，包括条件判断、循环等，这样计算机能够执行更加复杂的任务。



### **3、逻辑控制语句的内容**

        一般来说，代码时按照先后顺序依次执行的，有了逻辑控制语句，可以让计算机根据不同条件，跳过执行或者重复执行。

**<strong>条件判断**</strong>：简单来说，就是如果某条件为真就执行某行动，不为则真就不执行。我们日常生活中，每天都在经历条件判断，比如外面下雨了，出门就带把伞，出门快迟到了，那就赶紧跑两步，

**<strong>循环**</strong>：就是如果某条件为真，则一直重复执行某行动，直至条件为假。就像现实中，你可以在老板心情好的时候，在他眼皮子底下一直打游戏，直到他心情被你整坏了，扣你工资。

        大部分编程语言，其实都有这些类似的语句，虽然长得可能有一点不一样，但逻辑都是相通的。





### **4、****各种语言简介及其对应开发工具**

<img alt="" height="351" src="https://img-blog.csdnimg.cn/a0903f180fa4401984ff1e00b48e6cb1.png" width="432">

 **<strong>visual c++ 6.0软件：**</strong>由微软推出的(IDE)。Visual C++ 6.0 是Visual Studio 6.0的一个组成部分,主要用于开发各种C++应用程序，Visual C++ 6.0 只支持C和C++。Visual Studio 6.0中还包括Visual Basic 6.0、Visual Foxpro 6.0和Visual J++ 6.0。编程工具软件对应Visual Stuido 2010、2012、2013 其实是10.0、11.0、12.0；**<strong>Visual Studio 201软件：**</strong>由微软公司推出的开发环境(IDE)，是目前最流行的Windows平台应用程序开发环境。Visual Studio 2010支持多种C++、C#、Visual Basic、Javascript、F#等多种语言。 当然，随着各家工具的发展，万能的开发工具也有很多……
<td style="vertical-align:top;width:59.25pt;"> **<strong>编程语言**</strong> </td><td style="vertical-align:top;width:70px;"> **<strong>时间**</strong> </td><td style="vertical-align:top;width:147px;"> **<strong>开发工具**</strong> </td><td style="vertical-align:top;width:390px;"> **<strong>特点**</strong> </td>

**<strong>时间**</strong>

**<strong>特点**</strong>
<td style="vertical-align:top;width:59.25pt;"> 汇编语言 Assembly Language </td><td style="vertical-align:top;width:70px;"> 1946 </td><td style="vertical-align:top;width:147px;"> VisualASM </td><td style="vertical-align:top;width:390px;"> 1946年世界上第一台电子计算机问世 </td>

Assembly Language

VisualASM
<td style="vertical-align:top;width:59.25pt;">B语言</td><td style="vertical-align:top;width:70px;">1969</td><td style="vertical-align:top;width:147px;">高级语言</td><td style="vertical-align:top;width:390px;">B语言是贝尔实验室开发的一种通用的程序设计语言，它是于1969年前后由美国贝尔实验室的电脑科学家肯尼斯·蓝·汤普森（Kenneth Lane Thompson）在丹尼斯·里奇（Dennis MacAlistair Ritchie）的支持下设计出来。后来，丹尼斯·里奇以B语言为基础开发出C语言——世界上最常用的高级语言之一。自从被C语言取代之后，B语言几乎已遭弃置。</td>
<td style="vertical-align:top;width:59.25pt;"> C语言 </td><td style="vertical-align:top;width:70px;"> 1972 </td><td style="vertical-align:top;width:147px;"> Turbo C 2 </td><td style="vertical-align:top;width:390px;"> C语言是一种古老而又经久不衰的计算机程序设计语言，大约诞生于上个世纪60年代。 C语言的编程方式是一种称为面向过程的开发方式。也就是说，解决问题的时候，程序员需要思考计算机应该如何一步一步完成这个问题，然后将相应过程转化为代码。 写出了Linux系统； **<strong>C语言**</strong>： 代码编译得到**<strong>机器码**</strong>，机器码在处理器上直接执行，每一条指令控制CPU工作。 **<strong>其他语言**</strong>：代码编译得到**<strong>字节码**</strong>，虚拟机执行**<strong>字节码**</strong>并转换成**<strong>机器码**</strong>再后在处理器上执行。 </td>

1972

C语言是一种古老而又经久不衰的计算机程序设计语言，大约诞生于上个世纪60年代。

写出了Linux系统；

**<strong>其他语言**</strong>：代码编译得到**<strong>字节码**</strong>，虚拟机执行**<strong>字节码**</strong>并转换成**<strong>机器码**</strong>再后在处理器上执行。
<td style="vertical-align:top;width:59.25pt;"> SQL </td><td style="vertical-align:top;width:70px;"> 1974 </td><td style="vertical-align:top;width:147px;"> SQL Server Oracle SQL Developer PL/SQL Developer </td><td style="vertical-align:top;width:390px;">  </td>

1974

Oracle SQL Developer


<td style="vertical-align:top;width:59.25pt;"> C++ </td><td style="vertical-align:top;width:70px;"> 1979 </td><td style="vertical-align:top;width:147px;"> CFREE(初学者适用) VC++6.0 Visual C++ Dev-C++ Codeblock </td><td style="vertical-align:top;width:390px;"> C++包含了C语言，但在C++中又增加了面向对象的概念，但不是说C语言比不上C++，许多操作系统以及软件都是用C语言编程出来的，两者的编程思想不一样，应用的领域也不一样。在各自的领域，谁也不能替代谁。 写出了Microsoft Windows系统、Microsoft Office、Oracle、MySQL； #include&lt;iostream&gt; using namespace std;  int main() {<!-- --> cout&lt;&lt;"hello world!"; return 0; } </td>

1979

VC++6.0

Dev-C++

C++包含了C语言，但在C++中又增加了面向对象的概念，但不是说C语言比不上C++，许多操作系统以及软件都是用C语言编程出来的，两者的编程思想不一样，应用的领域也不一样。在各自的领域，谁也不能替代谁。

#include&lt;iostream&gt;



{<!-- -->

return 0;
<td style="vertical-align:top;width:59.25pt;">R语言</td><td style="vertical-align:top;width:70px;">1980</td><td style="vertical-align:top;width:147px;"></td><td style="vertical-align:top;width:390px;"> R是用于、的语言和操作环境。R是属于系统的一个自由、免费、源代码开放的软件，它是一个用于统计计算和统计制图的优秀。 </td>
<td style="vertical-align:top;width:59.25pt;">Matlab</td><td style="vertical-align:top;width:70px;">1984</td><td style="vertical-align:top;width:147px;"></td><td style="vertical-align:top;width:390px;"> MATLAB是matrix&amp;laboratory两个词的组合，意为**<strong>矩阵工厂**</strong>（矩阵实验室）。是由美国mathworks公司发布的主要面对科学计算、可视化以及交互式程序设计的高科技计算环境。它将数值分析、矩阵计算、科学数据可视化以及非线性动态系统的建模和仿真等诸多强大功能集成在一个易于使用的视窗环境中，为科学研究、工程设计以及必须进行有效数值计算的众多科学领域提供了一种全面的解决方案，并在很大程度上摆脱了传统非交互式程序设计语言（如C、Fortran）的编辑模式，代表了当今国际科学计算软件的先进水平。 应用领域：机器人、深度学习、计算机视觉、信号处理 </td>

应用领域：机器人、深度学习、计算机视觉、信号处理
<td style="vertical-align:top;width:59.25pt;"> Python </td><td style="vertical-align:top;width:70px;"> 1990 </td><td style="vertical-align:top;width:147px;"> IDLE PyCharm </td><td style="vertical-align:top;width:390px;"> Python计算机程序设计语言，具有丰富和强大的库。它常被昵称为，能够把用其他语言制作的各种模块（尤其是/）很轻松地联结在一起。常见的一种应用情形是，使用Python快速生成程序的原型（有时甚至是程序的最终界面），然后对其中有特别要求的部分，用更合适的语言改写，比如中的图形渲染模块，性能要求特别高，就可以用C/C++重写，而后封装为Python可以调用的扩展类库。需要注意的是在您使用扩展类库时可能需要考虑平台问题，某些可能不提供的实现。 </td>

1990

PyCharm
<td style="vertical-align:top;width:59.25pt;"> VB语言 </td><td style="vertical-align:top;width:70px;"> 1991 </td><td style="vertical-align:top;width:147px;"> visual basic 6.0 </td><td style="vertical-align:top;width:390px;"> VB语言，因其语言简单，容易理解，不复杂，适合初学者使用，但你也不要小看VB语言，只要用心，vb语言也是能写出很强大的程序的。 VB以及用VB写的程序只能在WINDOWS系统上使用，C无此限制（C最初是UNIX系统的工作语言）。 2020年3月11日，微软宣布不会再开发VB或增加功能。 </td>

1991

VB语言，因其语言简单，容易理解，不复杂，适合初学者使用，但你也不要小看VB语言，只要用心，vb语言也是能写出很强大的程序的。 VB以及用VB写的程序只能在WINDOWS系统上使用，C无此限制（C最初是UNIX系统的工作语言）。
<td style="vertical-align:top;width:68.65pt;"> Lua </td><td style="vertical-align:top;width:70px;"> 1993 </td><td style="vertical-align:top;width:147px;"></td><td style="vertical-align:top;width:390px;"> Lua语言：小的编程语言广泛运用在游戏、服务的配置。 (1)、类似Javascript的 动态语言，LuaJit 性能高于大多数的 脚本语言 (2)、结合C语言开发，非常简单，通过 LuaFFI直接调用C 编写的模块 </td>

1993

(1)、类似Javascript的 动态语言，LuaJit 性能高于大多数的 脚本语言
<td style="vertical-align:top;width:59.25pt;"> HTML </td><td style="vertical-align:top;width:70px;"> 1993 </td><td style="vertical-align:top;width:147px;"> Adobe Dreamweaver Visual Studio Code; </td><td style="vertical-align:top;width:390px;">  </td>

1993

Visual Studio Code;
<td style="vertical-align:top;width:59.25pt;"> PHP </td><td style="vertical-align:top;width:70px;"> 1995 </td><td style="vertical-align:top;width:147px;"> Dreamweaver_CS5 Notepad++ </td><td style="vertical-align:top;width:390px;">  </td>

1995

Notepad++
<td style="vertical-align:top;width:59.25pt;"> JavaScript </td><td style="vertical-align:top;width:70px;"> 1995 </td><td style="vertical-align:top;width:147px;"> Sublime Text VS Code WebStorm </td><td style="vertical-align:top;width:390px;"> ****<strong><em>JavaScript****</em></strong>是世界上最流行的编程语言之一，可广泛用于服务器、PC、笔记本电脑、平板电脑、智能手机等设备。一种直译式脚本语言即JS，是一种动态类型、弱类型、基于原型的语言，内置支持类型。它的解释器被称为JavaScript引擎，为浏览器的一部分，广泛用于客户端的脚本语言，最早是在（标准通用标记语言下的一个应用）网页上使用，用来给HTML网页增加动态功能，增加网页的交互功能，完成复杂的动态网页。 Java 和 JavaScript 是两门不同的编程语言。 在1995年时，由Netscape公司的Brendan Eich，在网景导航者浏览器上首次设计实现而成。因为Netscape与Sun合作，Netscape管理层希望它外观看起来像Java，因此取名为JavaScript。但实际上它的语法风格与Self及Scheme较为接近。 </td>

1995

VS Code

****<strong><em>JavaScript****</em></strong>是世界上最流行的编程语言之一，可广泛用于服务器、PC、笔记本电脑、平板电脑、智能手机等设备。一种直译式脚本语言即JS，是一种动态类型、弱类型、基于原型的语言，内置支持类型。它的解释器被称为JavaScript引擎，为浏览器的一部分，广泛用于客户端的脚本语言，最早是在（标准通用标记语言下的一个应用）网页上使用，用来给HTML网页增加动态功能，增加网页的交互功能，完成复杂的动态网页。
<td style="vertical-align:top;width:59.25pt;"> JAVA </td><td style="vertical-align:top;width:70px;"> 1995 </td><td style="vertical-align:top;width:147px;"> JBuilder Eclipse NetBeans IDE IntelliJ IDEA </td><td style="vertical-align:top;width:390px;"> 高级编程语言，面向对象，它是商业编程语言。因为C++开发的软件都是面向普通人的，而Java开发的软件大部分是面向事业单位、公司及企业的，它的功能同样强大，结构比C++清晰，学习起来比C++简单多了；并且是跨平台运行的程序，用Java开发出来的软件可以在世界几乎所有的系统上运行（包括Linux、掌上电脑、手机等），但正因为如此，使之运行时会比C++开发的软件要慢。 事实证明，Java不仅仅适于在网页上内嵌动画—它是一门极好的完全的软件编程的小语言。“虚拟机”机制、垃圾回收、没有指针等使它很容易实现，不易崩溃且不会泄漏资源的可靠程序。 虽然不是C++的正式续篇，Java从C++中借用了大量的语法。它丢弃了很多C++的复杂功能，从而形成一门紧凑而易学的语言。 应用：手机游戏、中间件、软件、网站，电脑游戏，以及现在流行的安卓手机app等 public class Main{<!-- --> public static void main(String[] args) {<!-- --> System.out.println("Hello World"); } } </td>

1995

Eclipse

IntelliJ IDEA

事实证明，Java不仅仅适于在网页上内嵌动画—它是一门极好的完全的软件编程的小语言。“虚拟机”机制、垃圾回收、没有指针等使它很容易实现，不易崩溃且不会泄漏资源的可靠程序。

应用：手机游戏、中间件、软件、网站，电脑游戏，以及现在流行的安卓手机app等

public static void main(String[] args)

System.out.println("Hello World");

}
<td style="vertical-align:top;width:59.25pt;"> C# </td><td style="vertical-align:top;width:70px;"> 2000 </td><td style="vertical-align:top;width:147px;"> Visual Studio Code MonoDevelop </td><td style="vertical-align:top;width:390px;"> 读C sharp；C#就是微软想要复制Java的成功，几乎就是Java的翻版。Java几乎被所有平台支持，而C#目前只被Windows和Linux支持，Windows下的支持当然是由微软自己开发的，而Linux下的支持则有MONO支持。实际上，MONO也是把转化为Java应用而已，所以本质上，C#仍然只是被微软自己的支持。应用平台受到限制，是它最大的缺点。 NET语言 C#是一种精确、简单、类型安全、面向对象的语言。其是.Net的代表性语言。什么是.Net呢？按照微软总裁兼首席执行官Steve Ballmer把它定义为：.Net代表一个集合，一个环境，它可以作为平台支持下一代Internet的可编程结构。 </td>

2000

MonoDevelop

NET语言
<td style="vertical-align:top;width:59.25pt;">Scala</td><td style="vertical-align:top;width:70px;">2001</td><td style="vertical-align:top;width:147px;"></td><td style="vertical-align:top;width:390px;"> Scala相对Java语法更丰富，更简洁，写起来更像脚本，能够提高开发效率。Scala是一门多范式的编程语言，一种类似的编程语言，设计初衷是实现可伸缩的语言、并集成和的各种特性。Scala是最轻松的语言，因为大家都欣赏其类型系统。Scala在JVM上运行，基本上成功地结合了函数范式和面向对象范式，目前它在金融界和需要处理海量数据的公司企业中取得了巨大进展。但Scala编译器运行起来有点慢。 Spark 平台是在  语言中实现的，它将 Scala 用作其应用程序框架。与 Hadoop 不同，Spark 和 Scala 能够紧密集成，其中的 Scala 可以像操作本地集合对象一样轻松地操作分布式数据集。 </td>

Spark 平台是在  语言中实现的，它将 Scala 用作其应用程序框架。与 Hadoop 不同，Spark 和 Scala 能够紧密集成，其中的 Scala 可以像操作本地集合对象一样轻松地操作分布式数据集。
<td style="vertical-align:top;width:59.25pt;"> Go </td><td style="vertical-align:top;width:70px;"> 2009 </td><td style="vertical-align:top;width:147px;"> Go Reviverevive Goland IntelliJ + Go </td><td style="vertical-align:top;width:390px;">  </td>

2009

Goland











## **编程的应用——逻辑控制语句的应用—****解决一个迷宫**

        逻辑控制语句的应用，比如你要计算机去解决一个迷宫。

### **1、基于问题设计解决方案**

方案一，你可以先自己找到正确路径，然后一步步用代码给出方向指令，这个有点麻烦，要是自己能够解决出来，要计算机何用？

方案二，你可以选择配合判断和循环，写出更灵活的指令，让计算机根据自己是否会撞墙，这个条件去调整下一步。比如，如果前面是墙，无法前进，就换一个当前位置没有去过的方向，继续前进；如果当前位置的所有方向全部试过走不通，就回到更之前的点，尝试新的方向；一直循环，直到找出这一套指令，能让计算机靠自己解出任何带出口的迷宫；

对于方案二，只涉及基本的逻辑控制，像判断、循环，其实没有任何的人工智能。如果不能完全理解这个逻辑，非常正常，不必因此而从入门到放弃，因为背后的思路是回溯法，属于比较高级的算法。

### **2、选择合适的编程语言实现**

        当然有了思路以后，要写出实际能够指挥的代码，还是要学习某个具体编程语言的语法，写出对应的语句。另外，也不必担心代码执行时尝试不同方向，因而会花很长时间，因为计算机运算速度远超人类，这些一秒内，解决出来也不在话下。





## **编程的意义**

### **1、教你如何思考问题**
<td style="vertical-align:top;width:59.25pt;"> **锻炼大脑****重塑问题的能力** </td><td style="vertical-align:top;width:306pt;"> 编程是一种对人的思考进行再思考的行为。我们不需要把每件事情想清楚，就可以在现实社会中生存。对某些从事机械性操作的职业来说，甚至完全不需要进行思考。 但是，在编程时，我们只有在想清楚之后，才能把程序写出来。在编写正确、高效、优雅的程序的同时，我们也在塑造自己的大脑，让它能思考得更清楚、运转得更高效。 </td>

编程是一种对人的思考进行再思考的行为。我们不需要把每件事情想清楚，就可以在现实社会中生存。对某些从事机械性操作的职业来说，甚至完全不需要进行思考。
<td style="vertical-align:top;width:59.25pt;"> **解决事情—理解事物****拆分****需求的****能力** </td><td style="vertical-align:top;width:306pt;"> 编程要求我们能够对事物和流程进行拆分，并在不同的抽象层次上进行完整自洽的思考，这使我们有可能去解决那些规模无比庞大的问题。在实现一个稍具规模的需求时，我们不太可能同时考虑主体流程和操作细节，也不太可能同时从多个角度进行思考。经过合理拆分后的需求细粒度需求简单明了，实现难度大大降低的同时，还可以分配给多人来共同进行。 在一个成熟的软件或互联网公司，上千名工程师一起开发同一款产品是很常见的，而你能想象这么多人一起去写一本书么？ </td>

在一个成熟的软件或互联网公司，上千名工程师一起开发同一款产品是很常见的，而你能想象这么多人一起去写一本书么？
<td style="vertical-align:top;width:59.25pt;"> **提供快速解决问题的方法—****抽丝剥茧的能力** </td><td style="vertical-align:top;width:306pt;"> 编程要求我们客观地去思考事物的本质，将注意力放在事物本身，而不是事物与我们的关系上。当古代的妇女在河边洗脏衣服时，她可能在想："河水好冷啊……这衣服颜色真漂亮……我家孩子为啥这么调皮……" 而当我们在为洗衣机设计程序时，只会想："哦，这有一堆脏衣服需要洗"。其实很多原本困扰你许久的问题，只要跳出"我"的范畴，进行"忘我"的思考，就变得特别简单和容易解决。 </td>

而当我们在为洗衣机设计程序时，只会想："哦，这有一堆脏衣服需要洗"。其实很多原本困扰你许久的问题，只要跳出"我"的范畴，进行"忘我"的思考，就变得特别简单和容易解决。
<td style="vertical-align:top;width:59.25pt;"> **解决事情****落地****时的****系统性思考能力** </td><td style="vertical-align:top;width:306pt;"> 编程是将人的想法"实体化"的过程，这要求我们进行更深入、更细致、更全面地思考。为了实现一个需求，你必须对其原理和运转流程了解得十分透彻，否则就无法用编程语言精确地描述出来让机器去执行。 在实体化的过程中，想法的结构缺陷和逻辑漏洞会自然凸显出来，你总会发现存在没有考虑到的可能性，以及需要进一步思考的细节。 </td>

在实体化的过程中，想法的结构缺陷和逻辑漏洞会自然凸显出来，你总会发现存在没有考虑到的可能性，以及需要进一步思考的细节。

**<strong>参考文章**</strong>：







### **2、解决实际问题—提高做事效率**

        通过编程，我们能够很容易的处理大量重复性、低效率的工作，从而节省时间。而工作中很多地方都用到了编程来提高生产力，比如 Excel 中的宏，很多 Adobe 的产品（如 Photoshop, Illustrator,）都能使用 JavaScrpt 来自动化工作。         再比如，如果遇到一个使用 Excel 处理大量数据的需求，不会编程就只能买别人开发好的脚本，或者自己花大量时间做大量重复性的工作，如果学习了编程，可以更好地满足我们这些私人订制化的需求。








