
--- 
title:  Shell编程基础 – for循环 
tags: []
categories: [] 

---
## Shell编程基础 – for循环

#### Shell Scripting Essentials - for Loop

大多数编程语言都有循环的概念和语句。如果想重复一个任务数十次，无论是输入数十次，还是输出数十次，对用户来说都不现实。

因此，我们考虑如何用好Bash Shell编程，挖掘它的力量来促成循环，并高效完成任务。我们知道，在Bourne Shell中拥有For, While循环，可能这个功能比其它语言少，但没有人声称Shell编程具有C语言的强大功能。

本文简要介绍for循环在shell编程过程的应用，希望对您有所帮助。

#### 1. For循环

For循环遍历一组值，直到列表耗尽为止。 以下示例为非嵌套的单循环，代码如下。

##### 1) 示例一：

```
#!/bin/bash
for I in 1 2 3 4 5
do 
  echo “Looping … number $i”
done

```

运行结果如下图： <img src="https://img-blog.csdnimg.cn/direct/638084a7ad2046eab5ef6baba2916145.png" alt="在这里插入图片描述">

##### 2) 示例二

尝试用以下代码运行：

```
#!/bin/sh
for i in hello 1 * 2 goodbye 
do
  echo "Looping ... i is set to $i"
done

```

于是，运行代码结果如下图：

<img src="https://img-blog.csdnimg.cn/direct/7bffebc277b747fba86f7c946ad5a025.png" alt="在这里插入图片描述"> 调试这段代码，看看它有什么作用。请注意，这些值可以是任意值。

这非常值得一试。确保您了解这里发生的事情。
- 尝试不带 * 并掌握这个想法，然后重新阅读通配符部分并在 * 到位的情况下再次尝试。- 也可以在不同的目录中尝试它，并用双引号将 * 括起来，并尝试在它前面加上反斜杠 （*）
上述脚本的运行结果已经看到了。在变量序列里，位于1和2之间的…（省略号）输出元素，代表着当前目录的第一个文件名for1.sh，和当前目录的第二个文件名for2.sh。

##### 3) 示例三：

输出从1至20之间的偶数。

```
#!/bin/bash

for I in {<!-- -->0..20..2}
do
   echo “The even number is: $i”
done

```

<img src="https://img-blog.csdnimg.cn/direct/21bfd180df9a42d9b24fbeb86d69989e.png" alt="在这里插入图片描述">

##### 4) 示例四：

变换一下上述题的规则，例如：我们想要输出从零到100的，并且能被7整除的数字。

```
#!/bin/bash
for i in {<!-- -->0..100..7}
do 
   echo “The number divided by 7 is: $i”
done

```

执行结果如下图： <img src="https://img-blog.csdnimg.cn/direct/8768934597de48abba43b9bd8b8713b0.png" alt="在这里插入图片描述">

##### 5) 示例五

下面让我们一起完成九九乘法表吧。 根据乘法公式推算，这必须符合被乘数与乘数相乘，然后得出结果。

```
#！/bin/bash

for((i=1; i&lt;=9; i++))
do
  dor((j=1;j&lt;=I;J++))
  do 
     echo -en “$i * $j = $[i*j]\t”
  done
  echo -e “\r”
done

```

执行结果如下图： <img src="https://img-blog.csdnimg.cn/direct/e1dea0710d4a4b9a8b6642c96d191b00.png" alt="在这里插入图片描述"> 好了，九九乘法表就打印结束了。

技术好文陆续推出，请关注我的博文。 您的兴趣，我的动力！

Jackson@ML
