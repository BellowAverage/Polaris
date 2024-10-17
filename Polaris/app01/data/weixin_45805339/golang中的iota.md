
--- 
title:  golang中的iota 
tags: []
categories: [] 

---
go语言中我们在定义常量的时候，经常会用到iota，它比较特殊，可以被认为是一个可被编译器修改的常量，在每一个const关键字出现时被重置为0，然后在下一个const出现之前，每出现一次iota，其所代表的数字会自动增1，用法如下：

```
const ( // iota被重设为0
 c0 = iota // c0 == 0 
 c1 = iota // c1 == 1 
 c2 = iota // c2 == 2 
) 
const ( 
 a = 1 &lt;&lt; iota // a == 1 (iota在每个const开头被重设为0) 
 b = 1 &lt;&lt; iota // b == 2 
 c = 1 &lt;&lt; iota // c == 4 
) 
// （&lt;&lt; 表示左移的意思,&lt;&lt;n==*(2^n)）
const ( 
 u = iota * 42 // u == 0 
 v float64 = iota * 42 // v == 42.0
 w = iota * 42 // w == 84 
)

```
