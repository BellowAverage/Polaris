
--- 
title:  下完安装好python后，想查看python的安装位置的几种方法 
tags: []
categories: [] 

---
查看python的路径

基于windows系统，按下win+r（也就是命令提示符），输入cmd ，进入

<img alt="" height="110" src="https://img-blog.csdnimg.cn/1a96a4281ff345acb5edb187859a65fb.png" width="477">

<img alt="" height="52" src="https://img-blog.csdnimg.cn/8591f33f7fa64d14b327493cce9a85d7.png" width="357">

 查看当前的python的版本的话输入python -V



<img alt="" height="56" src="https://img-blog.csdnimg.cn/83b2c7871a00453480ef56395f51510c.png" width="219">

1， 查看当前下载的python类型和路径则可以输入 py -0 (加 * 的是你使用python的默认版本)

<img alt="" height="93" src="https://img-blog.csdnimg.cn/2bcb588ec7a444cda4f86f8d1fae52e5.png" width="514">

 2，还可以使用命令 where python 查看路径（这样就不会显示你python默认使用的是哪个）

<img alt="" height="96" src="https://img-blog.csdnimg.cn/164704365afc4e34aae072919f44e428.png" width="607">

 小技巧：如果想清除命令行的话可以输入命令  cls 然后 enter(回车)

3，还有一个比较繁琐的方法：在cmd中输入如下命令  /  或者在IDLE中输入第2，3步也会得到这样的结果

        先输入python

        再输入import sys

        最后再输入print(sys.path)

画横线这样的即为安装路径

<img alt="" height="149" src="https://img-blog.csdnimg.cn/9904dc5bdb1847a6b2fd64bf565fc10d.png" width="1200">

 总结一下：python如果是按正常下载步骤，基本上都可以借助这几种方法找到安装位置
