
--- 
title:  【CMake报错】Cannot specify compile definitions for target “PRIVATE“ which is not built... 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>【CMake报错】Cannot specify compile definitions for target “PRIVATE” which is not built…</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - <ul><li>- - <ul><li>-  
   </li></ul> 
  </li></ul> 
  
  


## 报错：Cannot specify compile definitions for target “PRIVATE” which is not built by this project.

### 1）报错内容

>  
 CMake Error at CMakeLists.txt:72 (target_link_directories): Cannot specify link directories for target “PRIVATE” which is not built by this project. 
 CMake Error at CMakeLists.txt:73 (target_compile_definitions): Cannot specify compile definitions for target “PRIVATE” which is not built by this project. 
 CMake Error at CMakeLists.txt:80 (target_link_directories): Cannot specify link directories for target “PRIVATE” which is not built by this project. 


### 2）解决方案

这个错误提示的是在`CMakeLists.txt`文件中，试图为一个名为"PRIVATE"的目标设置属性，但是这个目标在项目中并不存在。 实际上，“PRIVATE”、"PUBLIC"和"INTERFACE"是`target_*`命令中的关键字，用于指定如何传递这些属性。

错误可能是因为没有正确地为`target_*`命令提供目标名称，或者目标名称和关键字的顺序被弄反了。

#### 错误情况一

如果存在以下代码：

```
target_include_directories(PRIVATE ${CMAKE_SOURCE_DIR}/include)

```

应该更正为：

```
target_include_directories(YourActualTargetName PRIVATE ${CMAKE_SOURCE_DIR}/include)

```

#### 错误情况二

如果存在以下代码：

```
target_link_directories(${ProjectName} PRIVATE ${RELEASE_LIB_DIR})

```

应该更正为：

```
target_link_directories(YourActualTargetName PRIVATE ${RELEASE_LIB_DIR})

```

其中，`YourActualTargetName`是你要设置属性的实际目标名称，
