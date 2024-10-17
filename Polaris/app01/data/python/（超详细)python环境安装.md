
--- 
title:  （超详细)python环境安装 
tags: []
categories: [] 

---
>  
 耀风也是python初学者，文章可能会有不严谨的地方，如有发现希望帮我指正 


## 1.python环境的安装

### （1）为什么要安装python环境？

python是一个解释性语言，所谓解释性语言就是代码不会进行预编译，而是在运行时，编译一句执行一句。（这和C/C++这类编译性语言先编译后执行的机制相比效率会慢很多，但是现在电脑的主频很高，所以完全可以忽略解释性语言的这种编译机制所带来的执行效率的降低。）因此在我们写好python代码想要运行时，就得有一个编译器，把python代码编译成机器码供CPU执行，而这个编译器和传统意义的编译器不同，所以在解释性语言中编译器被称为解释器。我们安装的python环境其实就是python的解释器。

### （2）从哪下载python环境安装包？

当然是官网啦！

（浏览时有点慢，耐心等下）

<img alt="" height="974" src="https://img-blog.csdnimg.cn/8184663ea1874ebc9dc5bca744e3182a.png" width="1200">





### （3）这么多版本我选哪个呢？

看网上的说法是越新越好，但是这个说法有点就绝对，用哪个版本得取决于你项目中支持的python版本。如果没有项目什么的就单纯的想学个python，那么就python3.0版本以上任选一个。



### （4）该选哪个安装包呢？ 

<img alt="" height="687" src="https://img-blog.csdnimg.cn/3e764f80eada4744b8357252d77122eb.png" width="1200">

选那个Windows installer！！！因为它可以根据你的选择自动帮你添加**环境变量**（懒人福利！），然后根据你计算机的版本看选32/64位的。（环境变量是什么后面会解释）

### （5）什么是环境变量？在哪看到它？

环境变量简单来说就是一个程序重要文件的路径，配置环境变量就是在告诉操作系统这个程序的重要文件的路径，这样在我们想运行程序时，操作系统就可以找到它，然后运行它。

可以通过方法找到python环境变量的配置的地方：

a.右击 此电脑 选择里面的 属性

b.点击 高级系统设置

c.点击 环境变量

d.双击path

<img alt="" height="427" src="https://img-blog.csdnimg.cn/0d92314d61434643b96d966448292c35.png" width="500">

e.画红框的就是python的环境变量（因为我安装了3.6和3.8两个版本的python，所以这里多出两条环境变量）

<img alt="" height="468" src="https://img-blog.csdnimg.cn/401bed5000cc462cad2d8600276313e4.png" width="500">

 

###  （6）为什么python的环境变量有两条？

因为python解释器有两个重要文件，一个是主文件(放没有版权等问题的函数库），另一个是主文件中的Scripts文件（放有版权等其他问题的函数库）

### （7）为什么安装包下载的这么慢？怎么解决呢？

因为python官网服务器布置在国外，所以因为科学上网的问题，就比较慢。解决的话，要么有科学上网的工具（会收取一定的费用），要么就是复制下载链接到迅雷中下载（强烈推荐！）

<img alt="" height="353" src="https://img-blog.csdnimg.cn/7e20c2c773dd44d5bad90314afae2d65.png" width="500">

 <img alt="" height="153" src="https://img-blog.csdnimg.cn/218935adbb724a459dc7f79b7a0e8062.png" width="535">

###  （8）选哪个选项会自动配置环境变量呢？

**画红框的，一定要选！！！！！！！**

<img alt="" height="308" src="https://img-blog.csdnimg.cn/77fa86ac8c304a32844e27380ed19414.png" width="500">

### （9）然后点击Install Now就可以安装了

### （10）python环境安装到哪了？

这个地方呀！

<img alt="" height="143" src="https://img-blog.csdnimg.cn/e6af0b4500304c35a3de88e1ddfc1e28.png" width="500">

###  （11）可以自定义安装路径吗？

可以的，完全可以，但是也一定要选择自动添加python环境变量，不然就得手动添加！

首先，

 <img alt="" height="396" src="https://img-blog.csdnimg.cn/e91d85aef06c42d8a77af1ac67c84588.png" width="500">

 然后，

<img alt="" height="379" src="https://img-blog.csdnimg.cn/e22dc9e3ed6a4747b1453b27a29fed72.png" width="500">

再然后，

改成你想安装的地方，然后点击Install安装

<img alt="" height="395" src="https://img-blog.csdnimg.cn/5a47aef94ddd4c88addfbd2a18be4a51.png" width="500">

 

###  （12）呀！忘了点自动添加环境变量怎么办？怎么手动添加呢？

a.根据（5）中的方法进入python环境变量一般放置的地方

b.复制python安装的路径

<img alt="" height="386" src="https://img-blog.csdnimg.cn/a63986ad5ee941a98a4efb02b9a3692d.png" width="500">

c.新建，添加复制的路径

<img alt="" height="464" src="https://img-blog.csdnimg.cn/0f8abe98be6f4342a174ec66b7fadc22.png" width="500">

d.复制python安装的路径下Scripts文件的路径，再执行上述新建，添加操作

e.成功

### （12）怎么看有没有成功安装python环境呢？

在键盘上敲win（就是有四个方块那个按键）+R ,一定要一起按下！！！

然后输入cmd，

<img alt="" height="246" src="https://img-blog.csdnimg.cn/d2ec91fa4db04c1e8fe847ed5819c40c.png" width="500">

点击确定，进入DOS界面

<img alt="" height="349" src="https://img-blog.csdnimg.cn/59fc6caeae974e3989354448f35fccbd.png" width="700">

输入python，如果出现如下结果就成功安装

<img alt="" height="113" src="https://img-blog.csdnimg.cn/4883b6e87ede4b00a642bf88946d0e98.png" width="700">

 

 

 




