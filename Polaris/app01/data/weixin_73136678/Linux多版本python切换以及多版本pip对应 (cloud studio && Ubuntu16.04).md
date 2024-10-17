
--- 
title:  Linux多版本python切换以及多版本pip对应 (cloud studio && Ubuntu16.04) 
tags: []
categories: [] 

---
linux &amp;&amp; cloud studio &amp;&amp; Ubuntu16.04

简单解决多版本python切换以及多版本pip对应问题

1.python2切换成python

多版本python: 更改前先查看版本号

>  
 <pre>$ python -V
Python 2.7.12</pre> 


>  
 <pre>$ python2 -V
Python 2.7.12</pre> 


>  
 <pre>$ python3 -V
Python 3.5.2</pre> 


通过下面的命令看到python3的很多可执行文件路径，留意 /usr/bin/python3.5，下面需要用来建立链接

>  
 <pre>$ whereis python3
python3: /usr/bin/python3.5-config /usr/bin/python3.5m-config /usr/bin/python3.5m 
/usr/bin/python3 /usr/bin/python3.5 /usr/lib/python3 /usr/lib/python3.5 /etc/python3 
/etc/python3.5 /usr/local/lib/python3.5 /usr/include/python3.5m /usr/include/python3.5 /usr/share/python3 /usr/share/man/man1/python3.1.gz</pre> 


查看python得到其可执行路径，把它删掉

>  
 <pre>$ which python
/usr/bin/python</pre> 


>  
 <pre>$ sudo rm /usr/bin/python</pre> 

