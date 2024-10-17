
--- 
title:  C语言编程入门 – 编写第一个Hello, world程序 
tags: []
categories: [] 

---
## C语言编程入门 – 编写第一个Hello, world程序

### C Programming Entry - Write the first application called “Hello, world!”

By Jackson@ML

>  
 C语言编程很容易！ 


本文开始，将带领你走过C语言编程之旅，通过实例使你对她颇感兴趣，一步步地跟着走。 好吧，让我们开始吧！😊

#### 1. 选择开发工具IDE

除了在命令行下编译C程序之外，在Windows可以安装集成开发环境(Integrated Development Environment， 即IDE)。 本次选用的是Visual Studio Code, 为了在其下顺利运行C程序，需要安装Extension（扩展插件）。

**1） 安装Code Runner** 这个名为Code Runner的扩展，专门为运行C，C++，Java，JS，PHP，Ruby等语言设计，目的是推广通用模型框架。 <img src="https://img-blog.csdnimg.cn/direct/8561f57db0b3454782f56c49c47113b9.png" alt="在这里插入图片描述">

##### 2） C/C++微软官方扩展插件

<img src="https://img-blog.csdnimg.cn/direct/a6f0235e77f34fc1a9558d1f39df0679.png" alt="在这里插入图片描述">

##### 3） 编写第一个应用程序：”Hello, world!”

在Visual Studio Code环境下，创建一个后缀名为*.c的文件。然后，打开Visual Studio Code. 代码如下：

```
# include &lt;stdio.h&gt;

int main() {<!-- -->
    printf("Hello, world!");
    return 0;
}

```

首先，导入 **stdio.h** 这个非常必要的输入输出模块，才能运行其它部分的程序。在main()函数中，打印语句printf()相较其他打印软件，更加清晰快捷。

运行成功！

#### 相关阅读：
1. 1. 