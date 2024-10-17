
--- 
title:  shell条件检查原理：command && echo ‘success‘ || echo ‘error‘ 
tags: []
categories: [] 

---
>  
 ls /xx &amp;&amp; echo 'success' || echo 'error' 
 如果第一个是true,则会检查&amp;&amp;符后面的,因为如果第二个是false会影响整体的值; 
 如果第一个是false,则不会检查&amp;&amp;符后面的, 
 因为无论and什么都是false,但是会检查||后面的,因为如果or true会引起整体值变化 


#### 

#### | 运算符

管道符号，是unix一个很强大的功能,符号为一条竖线:"|"。 用法:

command 1 | command 2

他的功能是把第一个命令command 1执行的结果作为command2的输入传给command 2，例如:



$ls -s|sort -nr (请注意不要复制$符号进去哦)  

-s 是file size，-n是numeric-sort，-r是reverse，反转

该命令列出当前目录中的文档(含size)，并把输出送给sort命令作为输入，sort命令按数字递减的顺序把ls的输出排序。

#### &amp;&amp; 运算符:

格式

```
command1  &amp;&amp; command2

```

&amp;&amp;左边的命令（命令1）返回真(即返回0，成功被执行）后，&amp;&amp;右边的命令（命令2）才能够被执行；换句话说，“如果这个命令执行成功&amp;&amp;那么执行这个命令”。 语法格式如下：

```
command1 &amp;&amp; command2 &amp;&amp;
```
