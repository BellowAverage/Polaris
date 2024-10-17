
--- 
title:  python包合集-argparse 
tags: []
categories: [] 

---
#### 一、argparse简介

argparse 是 python 自带的命令行参数解析包，可以用来方便的服务命令行参数，使用之前需要先导入包 import argparse

#### 二、简单案例

简单使用，创建一个名为test.py的文件

打印结果为：

再次验证：

解释说明

在上述代码  parser.add_argument("-n", "--name", default="Se7eN") 中，有两个参数 “-n”和“--name” 分别代表什么？其中-n 和 --name 都是我们自己自定的参数名。至于n和name ,你可以随便起个变量名都可以，但是要注意，前面的一个 “-”和“--”才是关键。

一个“-”的参数，例如：-n, 他其实相当于我们在liunx中使用的指令，一个自定义的指令。

两个“--”的参数，例如：--name 他就相当于在程序中，用来接收对对应指令值的变量，例如我们在控制台上输入 python3 test.py -n hou。 其中 -n 就代表使用的 -n 的指令，然后将后面的 hou 的值赋值给对应的变量， -n 对应的变量就是 --name 。所以我们使用print 打印的时候才显示的name = hou

简单理解：一个“-”的是指令，两个“--”的是接收指令内容的变量。

#### 三、ArgumentParser参数

ArgumentParse是解析器对象，在创建一个解析器对象的时候，是有很多参数可以配置，下面就演示一下这些参数的使用

1、prog: 程序的名称（默认值：sys.argv[0]）
