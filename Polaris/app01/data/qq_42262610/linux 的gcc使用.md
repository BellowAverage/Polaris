
--- 
title:  linux 的gcc使用 
tags: []
categories: [] 

---
 首先使用gcc要在linux环境下（g++就是c++的使用）

在Linux系统中，可执行文件没有统一的后缀，系统从文件的属性来区分可执行文件和不可执行文件。而gcc则通过后缀来区别输入文件的类别，下面介绍gcc所遵循的部分约定规则。

.c后缀的文件，C语言源代码文件； .a为后缀的文件，是由目标文件构成的库文件； .h为后缀的文件，是程序所包含的头文件； .i 为后缀的文件，是已经预处理过的C源代码文件； .m为后缀的文件，是Objective-C源代码文件； .o为后缀的文件，是编译后的目标文件； .s为后缀的文件，是汇编语言源代码文件； .S为后缀的文件，是经过预编译的汇编语言源代码文件

1. 无选项编译链接 用法：gcc test.c（c++程序要用g++） 作用：将test.c预处理、汇编、编译并链接形成可执行文件。这里未指定输出文件，默认输出为a.out。

 2. 选项 -o 用法：gcc test.c -o test 作用：将test.c预处理、汇编、编译并链接形成可执行文件test。-o选项用来指定输出文件的文件名。

 3. 选项 -E 用法：gcc -E test.c -o test.i 作用：将test.c预处理输出test.i文件。

 4. 选项 -S 用法：gcc -S test.i  作用：将预处理输出文件test.i汇编成test.s文件。

5. 选项 -c 用法：gcc -c test.s 作用：将汇编输出文件test.s编译输出test.o文件。

 6. 无选项链接 用法：gcc test.o -o test 作用：将编译输出文件test.o链接成最终可执行文件test。

 7. 选项-O 用法：gcc -O1 test.c -o test

作用：使用编译优化级别1编译程序。级别为1~3，级别越大优化效果越好，但编译时间越长。

二. 多源文件的编译方法

 如果有多个源文件，基本上有两种编译方法： [假设有两个源文件为test.c和testfun.c]

 1. 多个文件一起编译 用法：gcc testfun.c test.c -o test 作用：将testfun.c和test.c分别编译后链接成test可执行文件。

 2. 分别编译各个源文件，之后对编译后输出的目标文件链接。

 用法： gcc -c testfun.c //将testfun.c编译成testfun.o gcc -c test.c //将test.c编译成test.o gcc -o testfun.o test.o -o test //将testfun.o和test.o链接成test

 以上两种方法相比较，第一中方法编译时需要所有文件重新编译，而第二种方法可以只重新编译修改的文件，未修改的文件不用重新编译。

运行程序 例如./a.out就可以运行程序
