
--- 
title:  JDK下载、安装与配置 
tags: []
categories: [] 

---
Oracle官网：

进入官网点击 products，选择 Java。

<img src="https://img-blog.csdnimg.cn/38a8d91374ad4b4d9325404872eb76fa.png#pic_center" alt="在这里插入图片描述">

向下滑，选择Oracle JDK

```
Oracle JDK 和 Oracle OpenJDK 的区别
小插曲：https://www.yisu.com/zixun/136006.html 

```

<img src="https://img-blog.csdnimg.cn/e5b759d79a8746edb6aeabbfcf96c630.png#pic_center" alt="在这里插入图片描述">

向下滑找到JDK８，选择点击windows，再点击右边的64位下载。

<img src="https://img-blog.csdnimg.cn/0c87b062e924499ca45d179bf3fd6ba7.png#pic_center" alt="在这里插入图片描述">

会有一个弹窗，勾选同意，点击下载

<img src="https://img-blog.csdnimg.cn/b02a241e88b64270a51b935e70c4d89e.png#pic_center" alt="在这里插入图片描述">

会有一个登录提示，登录Oracle就可以进行下载了。 <img src="https://img-blog.csdnimg.cn/c7cf5a652697421c9cea0a1a27d0cf1e.png#pic_center" alt="在这里插入图片描述">

**JDK的安装如下：**

默认直接下一步

<img src="https://img-blog.csdnimg.cn/881e764530ba404e88a796e50fb9dc70.png#pic_center" alt="在这里插入图片描述">

安装路径：可以按照自身情况选择安装路径，一定要记得这个路径，后面的配置环境变量需要用到。

<img src="https://img-blog.csdnimg.cn/e2eed5f927ed4d5c99247e0b08c7f667.png#pic_center" alt="在这里插入图片描述">

这一步是安装Java的运行环境。

<img src="https://img-blog.csdnimg.cn/b30baeaee7904a0193988099afd5bda1.png#pic_center" alt="在这里插入图片描述">

显示已成功安装，点击关闭。

<img src="https://img-blog.csdnimg.cn/a74d87459f8d43a9b92c9c5e8bbedaa4.png#pic_center" alt="在这里插入图片描述">

验证是否安装成功 按键盘上的 win+r 调出运行窗口 输入 cmd 回车,输入 java -version

<img src="https://img-blog.csdnimg.cn/b00b2d8e53644bb999b967fc600b5e0f.png#pic_center" alt="在这里插入图片描述">

显示如上说明安装JDK完成。

**JDK配置文档：**

右键选择：属性

<img src="https://img-blog.csdnimg.cn/31a9a0748cbb42f0bb3c33e3171114f4.png#pic_center" alt="在这里插入图片描述">

左上角选择选择：高级系统属性

<img src="https://img-blog.csdnimg.cn/58eb0e515c61451a9579cf24cfbe0cd5.png#pic_center" alt="在这里插入图片描述">

选择：环境变量

<img src="https://img-blog.csdnimg.cn/5bf7a29650c4486d86585393344383eb.png#pic_center" alt="在这里插入图片描述">

在系统变量，点击新建 变量名：JAVA_HOME 变量值：为JDK安装目录

<img src="https://img-blog.csdnimg.cn/e2777f5169754a6eb331fb46b48a9dc0.png#pic_center" alt="在这里插入图片描述">

编辑PATH变量 变量名：Path – 这个已经存在，不需要创建。 变量值：;%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;

<img src="https://img-blog.csdnimg.cn/2dd03b3dad0f4601a948aa9a1f928af8.png#pic_center" alt="在这里插入图片描述">

编辑系统环境变量 变量名 CLASSPATH 变量值 .;%JAVA_HOME%\lib;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar; （注意：该值设置时， 一定要注意 前面的 . 符号）

<img src="https://img-blog.csdnimg.cn/309a8a42817c4703ac1c6870271e7281.png#pic_center" alt="在这里插入图片描述">

为什么添加JAVA_HOME ？？？

```
它指向JDK的安装路径，Eclipse/NetBeans/Tomcat等软件就是通过搜索JAVA_HOME变量来找到并使用安装好的JDK。

```

为什么添加Path？？？

```
作用是指定命令搜索路径，在cmd或者shell下面执行命令时，
它会到PATH变量所指定的路径中查找看是否能找到相应的命令程序。

```

为什么添加CLASSPATH ？？？

```
CLASSPATH是javac编译器的一个环境变量。它的作用与import、package关键字有关。
设置Classpath的目的，在于指定类搜索路径，要使用已经编写好的类，
前提当然是能够找到它们了，JVM就是通过CLASSPTH来寻找类的.class文件。
我们需要把jdk安装目录下的lib子目录中的dt.jar和tools.jar设置到CLASSPATH中，当然，当前目录“.”也必须加入到该变量中。


```
