
--- 
title:  Java通过Rserve调用R脚本 
tags: []
categories: [] 

---
JAVA负责系统的构建，R用来做运算引擎，从而实现应用型和分析性相结合的系统。增强了系统的灵活性和健壮性。

## 一、方式介绍

### 1.1内嵌模式（使用JRI）

JRI，全名是Java/R Interface，是通过调用R的动态链接库从而利用R中的函数等。通过install.packages(“rJava”)安装rJava就行，在安装文件夹中，可以看到一个jri的子文件夹，里面有自带的例子可以用来测试。过程：
1.  配置JRI环境变量 1.  安装rJava。 install.packages(“rJava”) 1.  导入jar包。JRI.jar、REngine.jar和JRIEngine.jar 
### 1.2远程调用模式（使用Rserve）

Rserve是一个基于TCP/IP的服务器，通过二进制协议传输数据，可以提供远程连接，使得客户端语言能够调用R。在服务端计算机安装R之后可以直接使用install.packages(“Rserve”)进行安装。需要使用时在R控制台下加载该包，然后输入命令Rserve()，开启服务器就可以供客户端调用。过程：
1. 安装并配置了R语言1. 安装Rserve包： install.packages(“Rserve”)1. 自定义Rserve的配置文件。Rserve包被安装在R的安装目录的library文件夹下
>  
 配置项含义： 
         config file: Rserv.cfg 配置文件名称 
         working root: R运行时工作目录 /tmp/Rserv 
         port: 6311 通信端口 
         local socket: TCP/IP TCP/IP协议 
         authorization: 认证未开启 
         plain text password: 不允许明文密码 
         passwords file: 密码文件，未指定 
         allow I/O: 允许IO操作 
         allow remote access: 远程访问未开启 
         control commands: 命令控制未开启 
         interactive: 允许通信 
         max.input buffer size: 文件上传限制262mb 
 新建自定义Rserve配置文件Rserv.cfg(可先创建Rserv.txt添加内容后改后缀为cfg)，该配置文件会覆盖Rserve的默认配置，该自定义配置项包含了一个Rserve启动脚本start.R,该脚本可用于启动Rserve时输出提示信息，新建该脚本文件并输入内容： 
         cat("This is my Rserve!") 
         print(paste("Rserve Server start at ",Sys.time())) 

1. 加载Rserve包：library(Rserve)1. 导入jar包REngine.jar RserveEngine.jar Rserve.jar1. Rconnection()：连接R服务1. eval():执行R语句，返回REXP类型数据（其提供了asInteger(), asIntegers(), asString(), asDouble(), asDoubles(), asList()等方法将REXP类型数据转换成java相应类型的数据）1. assgin()：声明变量1. 关闭Rconnection连接用rc.close();
### 1.3对比

**Rserve**：

优点是javaWeb项目不需要去维护R的运行，通过TCP/IP协议直接进行通讯。

缺点是它对中文的支持很弱，尤其是在windows的环境中，基本不支持中文；在linux环境下，对中文的支持稍微好些。不是完全支持中文的话，不能用于返回值有中文或者输入有中文的系统。

**JRI**：

优点是对中文的支持较好。

缺点是使用JRI模式下很容易造成整个系统的崩溃，比如在java调用R的时候，中间出现了异常或者错误，导致java虚拟机崩溃，从而导致整个系统崩溃。

### 二、Rserve

### 2.1下载地址



```
install.packages("Rserve", repos = "https://mirror.lzu.edu.cn/CRAN/")


# 以服务方式启动Rserve,供Java调用，默认端口号6311,日志输出文件R.out,后台启动
 R CMD Rserve --RS-enable-remote --no-save&gt; R.out 2&gt;&amp;1 &amp;
```

<img alt="" height="694" src="https://img-blog.csdnimg.cn/8d059e60aed14e73b25386e3f0dc4ffb.png" width="1094">

### 2.2引入依赖 

```
&lt;dependency&gt;
    &lt;groupId&gt;org.rosuda.REngine&lt;/groupId&gt;
    &lt;artifactId&gt;Rserve&lt;/artifactId&gt;
    &lt;version&gt;1.8.1&lt;/version&gt;
&lt;/dependency&gt;
&lt;!-- https://mvnrepository.com/artifact/org.rosuda.REngine/REngine --&gt;
&lt;dependency&gt;
    &lt;groupId&gt;org.rosuda.REngine&lt;/groupId&gt;
    &lt;artifactId&gt;REngine&lt;/artifactId&gt;
    &lt;version&gt;2.1.0&lt;/version&gt;
&lt;/dependency&gt;

```

<img alt="" height="206" src="https://img-blog.csdnimg.cn/d50b1949f5ff4dbeb5ac9e50c403a259.png" width="1200">

 【路径不要出现中文】

####  三、tidyverse包

>  
 install.packages("tidyverse", dependencies = TRUE)  


**报错**：

<img alt="" height="594" src="https://img-blog.csdnimg.cn/6efd4f0ea70f418d874a2807d926deec.png" width="1028">

 **解决方法**：在这个目录下找到***readxl，然后删除它，重新install一下就行。可能是之前install的时候没有下载完就强制断开了。

>  
 library("tidyverse") 


<img alt="" height="209" src="https://img-blog.csdnimg.cn/49076b52f7e645c38a80d8383287b441.png" width="506">

>  
  capabilities() 


<img alt="" height="210" src="https://img-blog.csdnimg.cn/6b5daac63e8248a2a88343cfe95c580a.png" width="913">

 发现linux不支持这三种图片格式的画图板。

>  
 ./configure --enable-R-shlib --prefix=/etc/R  --with-readline=no --with-lib**png** --with-**jpeg**lib 


红字是不是很熟悉。

## 四、Java代码

```
RConnection rConnection = new RConnection("127.0.0.1", 6311);
        REXP rexp = rConnection.eval("R.version.string");//测试连接，方法是eval(String arg0)
        System.out.println(rexp.asString());// R version 3.1.2 (2014-10-31)
        // 服务器中R语言脚本路径
        String fileName = "D:/WorkSpace/R/template.R";
        // 指定要执行的R语言脚本,需要先指定脚本
        rConnection.assign("fileName", fileName);
        // 向脚本中进行参数传递,只需要和脚本中的参数名称保持一致即可
        rConnection.eval("myplot('data.csv','oo.pdf')");
        // 执行
        rConnection.eval("source(fileName)");
        rConnection.close();
```

大功告成！
