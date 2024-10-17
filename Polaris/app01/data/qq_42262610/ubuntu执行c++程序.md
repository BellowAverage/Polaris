
--- 
title:  ubuntu执行c++程序 
tags: []
categories: [] 

---
Linux系统中使用命令运行C++ 脚本进行编译首先要保证系统中包含编译工具（g++/gcc）和编辑工具（vim、），C语言和C++对应的编译器分别为gcc，g++。

在终端输入以下命令检查系统是否有g++编译器：

```
g++ -v
```

如果系统没有g++编译器需要先安装编译器，命令如下：

```
sudo apt-get install g++
```

首先先用Gedit（或vim）准备一个简单的C++脚本，或者使用vs编写c++脚本

保存脚本后然后在终端进行编译 ：

```
sudo g++ hello.cpp -o hello
```

将会生成hello的可执行文件，使用命令行就可以执行

> 
   ./hello 
 

执行成功会输出C++脚本的结果
