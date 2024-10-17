
--- 
title:  python环境变量配置 
tags: []
categories: [] 

---
python现在的版本，主要是python2和python3两个大版本，这两个版本有很大的不同。

当我们在自己电脑上同时安装了python2.x和python3.x版本的解释器的时候，就需要对环境变量的配置进行一定的修改。

【大概解释一下，我对环境变量的理解】

1、配置环境变量，就是让我们在cmd的任何一个目录下都访问到相应的程序。

2、如：配置了mysql环境变量后，我们要使用mysql的时候，在cmd中任何目录下，执行mysql -uroot -p 密码，就可以登录到本地mysql数据库。

3、对于python解释器，我们在cmd目录下输入python，就是先从环境变量中的目录下去找，是否有python.exe程序存在，有就是操作该程序【如果环境变量中的目录下有多个python.exe,只会找第一个，这就是为什么要设置python2和python3来区分的原因了。】

具体操作：

一、修改python.exe程序

1、找你的python2.x解释器安装的位置。<img alt="" src="https://img-blog.csdnimg.cn/da54b79e123a4b0cacd9b8dfb71069de.png">

将python.exe复制一份，改名成python2.exe，原来python.exe一般不需要删除。

把文件路径保存下来：c:/apps/python/python2

2、找到python3.x解释器安装的位置。

<img alt="" src="https://img-blog.csdnimg.cn/16b01f5695154213bc14f43c94e91189.png">

 

将python.exe复制一份，改名为python3.exe 原来的python.exe也不要删除。

把此文件路径保存下来：假设是c:/apps/python/python39



二、添加环境变量

1、在电脑搜索框：搜索环境变量

 <img alt="" src="https://img-blog.csdnimg.cn/0bcfdc784dcb471c96fde98aa866ad52.png">

  2、点击进入

 <img alt="" src="https://img-blog.csdnimg.cn/1f6127c090eb4b5b8ea70eca5ad2bcee.png">

3、直接给系统变量加

<img alt="" src="https://img-blog.csdnimg.cn/6a3db4c4a4004193a58159e2c396b894.png">

4、点击新建

<img alt="" src="https://img-blog.csdnimg.cn/b294cc05a964411185f3181c3fe7f672.png">

  5、python2的路径： c:/apps/python/python2  python3路径： c:/apps/python/python3

<img alt="" src="https://img-blog.csdnimg.cn/1b7edc88a4b844318ddbec90435fc5b1.png">

6、把路径添加进去后，点击确认。

三、检测：

进入cmd中：

1、输入  python2    查看版本是不是pyhton2.x版本

2、输入 python3  查看版本是不是python3.x版本

拓展：如果电脑中同时安装python3.79和python3.9.0版本的解释器，该如何设置？【未配置虚拟环境】

你只要记住，当你在cmd输入python的时候，电脑是进行如下操作的。

1、电脑会在当前目录下中找python.exe程序，找到就执行该python.exe程序。

2、当前路径没有，电脑会先到配置好的环境变量中从到尾去遍历每个目录，如果在某个目录中找到了python.exe程序后，就不会去找下一个目录了，直接就执行第一个找到的python.exe程序。如果遍历了环境变量中所有目录都没有找到python.exe程序，，如果当前没有就会报错。

具体操作：

1、找到python3.7.9 安装路径，找到该路径下的python.exe 复制一份，将复制的名字改成python37.

2、找到python3.9.0安装路径，找到该路径下的python.exe，复制一份，将复制的名字改成python39.

3、将上面两个版本的路径添加到环境变量中

测试：

1、在cmd下输入：python37

2、在cmd下输入: python39

3、查看版本号，就能验证是否成功。

扩展知识：配置python的虚拟环境。

所谓虚拟环境，就像是你刚下载好的python解释器的镜像一样，里面没有安装多余的包。

1、之所以需要虚拟环境，是为在不同项目下，需要的python版本不一样，需要使用到的包也不一样，这样就不能把所有项目都使用一个python解释器了。

2、虚拟环境就是纯净版的python解释器，上面没有其他人安装过的包，你可以根据项目需求去安装包。  

 

 

 
