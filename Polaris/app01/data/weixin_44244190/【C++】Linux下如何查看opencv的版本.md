
--- 
title:  【C++】Linux下如何查看opencv的版本 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>Linux下如何查看opencv的版本</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - -  
  
  


## 1. 方法一（推荐）

直接再linux终端输入

```
opencv_version

```

<img src="https://img-blog.csdnimg.cn/1dc23c12934d462f8025662e7ce16452.png" alt="在这里插入图片描述">

## 2. 方法二（推荐）

```
pkg-config --modversion opencv4

```

## 2. 方法三

使用编写 ` test.cpp`代码测试：

```
#include &lt;iostream&gt;
#include &lt;opencv2/core/core.hpp&gt;

int main() {<!-- -->
    std::cout &lt;&lt; "OpenCV version: " &lt;&lt; CV_VERSION &lt;&lt; std::endl;
    return 0;
}

```

执行如下命令构建代码：

>  
 sudo g++ test.cpp -o check_version `pkg-config --cflags --libs opencv4` 


构建完成以后会生成一个`check_version`的可执行文件：

<img src="https://img-blog.csdnimg.cn/430f549782174659a634b352410667da.png" alt="
">

运行可执行文件：

```
./check_version 

```
