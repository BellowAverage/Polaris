
--- 
title:  Active Directory 基础 —— 如何理解group的类型 
tags: []
categories: [] 

---


<img alt="" height="663" src="https://img-blog.csdnimg.cn/2e12c674e0ad463ba45cb35a1fc9f93c.png" width="1200">

 



因为创建一个跨域的组，重新温习了一下最基本的AD知识，所谓温故而知新，把温习的结果整理了一下。AD里面的group类型从范围来说分为global, universal 和 local domain, 从类型来分分为security和distribution。后面的类型理解很容易，security就是纯粹用来权限访问的，而distribution主要是用来设定群发邮件。前面的类型就稍微复杂一些了。

 根据论坛上微软讲师的推荐记忆，可以按照以下方式理解

A-&gt; G -&gt; U -&gt; LD -&gt; P

A就是账户，G是global group，U是universal group, LD 是local domain group，P代表权限划分

前者可以是后者的成员，但是不能倒过来；同时因为同样类型的组也可以是同类型组的成员，上面的链接可以扩展成

A-&gt;G-&gt;G-&gt;U-&gt;U-&gt;LD-&gt;LD-&gt;P

 对于G而已，他的成员范围只能是同一个域；U的成员可以扩展到整个森；而LD的成员可以是任何的域或者森；

 比如说我有A域和B域，A域试图访问B域的资源，那么常见的做法，可以在A创建一个Global或者Universal的组，然后B创建一个Local domain的组，把A创建的组作为B组的成员，那么A组的成员即可访问B组的资源。

 为了验证这个理论&amp;#
