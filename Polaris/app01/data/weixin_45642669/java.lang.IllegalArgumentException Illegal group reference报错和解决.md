
--- 
title:  java.lang.IllegalArgumentException: Illegal group reference报错和解决 
tags: []
categories: [] 

---
查询了一下，发现：
- repaceAll和repaceFirst使用的是正则表达式- replace使用的是普通的kmp
传入的参数是不同的 <img src="https://img-blog.csdnimg.cn/808c05527010458cbb7049629e21378a.png" alt="在这里插入图片描述">* regex是正则表达式的表达式，会进行转义
- oldchar、newchar是标准的字符串，并不会进行转义
在正则表达式里面:

```
* . ? + ^ $ | \ / [ ] ( ) { }

```

这几个字符是必须进行转义的。   如果直接用字符串作为正则表达式的参数会导致正则表达式解析失败，从而抛出java.lang.IllegalArgumentException: Illegal group reference
