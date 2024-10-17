
--- 
title:  CentOS 7 服务器配置篇(一):JDK安装与配置 
tags: []
categories: [] 

---
背景:      CentOS 7.3 + JDK_1.8+XShell（没有相关软件资源，可看另一篇博客，所有资源都已通过百度网盘分享）

时间:      2019/5/9,以下步骤，亲测有效！

前言:     可通过可视化工具FileZilla Client上传文件或者通过命令行上传文件，我认为作为一名程序员，最好通过命令行进行操                   作！下面两种方法都会涉及到，以帮助在配置路上迷茫的你们。

## JDK安装与配置:

    1.进入--oracle官网下载Linux对应版本的jdk：

资源：​​​​​​​

<img alt="" class="has" height="70" src="https://img-blog.csdnimg.cn/20190312125843236.png" width="547">

2(可视化工具).将此压缩包上传至云端，该怎么上传？这个网上资料很多，我是通过一个**FileZilla Client.exe**,这个是开源的而且很方便（支持拖拽），直接拉到云端文件的某个指定目录即可。

<img alt="" class="has" height="73" src="https://img-blog.csdnimg.cn/20190312130424780.PNG" width="555">

2(命令行):首先创建一个目录(服务器存放Jdk的目录，不用创建也行，只要你能记住就行，因为后续还设置环境变量)我在/usr/share下创建一个 java文件夹（mkdir -p java），执行 rz(报错的，) ，选定文件上传

<img alt="" class="has" height="169" src="https://img-blog.csdnimg.cn/20190509180006486.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="232">

3.解压

  cd 进入到jdk压缩包存放路径，通过**tar -zxvf 压缩包名 进行解压**

<img alt="" class="has" height="408" src="https://img-blog.csdnimg.cn/20190509180525264.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="373">

4.jdk环境配置

   cd /etc

   vi profile ,在最后行，添加一下代码，即你的jdk路径 (vi 命令详解，)

   export JAVA_HOME=/usr/share/java/jdk1.8.0_201    export JRE_HOME=/usr/share/java/jdk1.8.0_201/jre

   export PATH=${JAVA_HOME}/bin:$PATH    export CLASSPATH=./:${JAVA_HOME}/lib:${JARE_HOME}/lib

>  
 export JAVA_HOME= "jdk解压后的文件完整路径" export JRE_HOME=${JAVA_HOME}/jre export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib:$CLASSPATH export JAVA_PATH=${JAVA_HOME}/bin:${JRE_HOME}/bin export PATH=$PATH:${JAVA_PATH} 


   按ESC -&gt; :wq -&gt; shutdown -r now -&gt; java -version

<img alt="" class="has" height="93" src="https://img-blog.csdnimg.cn/20190509185316702.PNG" width="481">

看是否，jdk安装成功，这里和Windows一样。

  可执行 echo $JAVA_HOME;  //查看安装路径

6.进入jdk 的bin目录，新建Test.java文本文档

     touch Test.java

     vi Test.java   编写代码、保存退出

     cat Test.java  查看文档内容

      <img alt="" class="has" height="93" src="https://img-blog.csdnimg.cn/20190509193029598.PNG" width="370">



    javac Test.java

    java Test

    <img alt="" class="has" height="47" src="https://img-blog.csdnimg.cn/20190509193145524.PNG" width="254">

    看运行结果是否一致

7.若以上都已验证成功，恭喜，您以安装成功！

#### (如有问题，可加我QQ：935135239，支持远程调试)






