
--- 
title:  输入www.baidu.com背后发生了什么？ 
tags: []
categories: [] 

---
>  
 **1、浏览器分析www.baidu.com 2、浏览器向DNS服务器请求解析ip地址         ****dns域名解析过程****：****                客户机首先查看自己浏览器的缓存，如果没有对应的dns解析，就去查看自己机器中的host文件                 如果都没有的话就会想本地dns服务器查询，本地dns服务器也是先查看自己的缓存，如果有就直接返回，如果没有，                 就会到根DNS服务器里面查询，根DNS服务器收到查询后发现是以.com结尾的，于是根dns服务器查询.com的域名服务器位置                 返回给本地dns服务器，本地域名服务器访问.com服务器，.com服务器返回baidu.com服务器ip给本地域名服务器，                 本地dns服务器访问baidu.com服务器，然后baidu.com返回www.baidu.com的ip给本地域名服务器，本地dns服务器返回给浏览器****3、dns将解析出来的ip地址返回给浏览器 4、浏览器与服务器之间进行tcp 三次握手连接 5、浏览器向服务器请求html文件 6、服务器返回html文件给浏览器 7、四次挥手，浏览器与服务器断开tcp请求 8、浏览器执行html文件，渲染页面** 


**########################################### **

<img alt="" height="682" src="https://img-blog.csdnimg.cn/35d3822abcb74557b9832a28bbbcc990.png" width="981">


