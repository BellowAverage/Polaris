
--- 
title:  【CMake报错】报错：Flow control statements are not properly nested. 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>CMake报错及解决方案</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - <ul><li>-  
  </li></ul> 
  
  


## 1. 报错：Flow control statements are not properly nested.

### 1）报错内容

>  
 CMake Error at CMakeLists.txt:70 (else): Flow control statements are not properly nested. 
 – Configuring incomplete, errors occurred! 


### 2）解决方案

此错误是由于 CMake 的流控制语句（如 `if`、`else`、`elseif` 和 `endif`）没有正确嵌套导致的。

要解决这个问题，你需要确保每个 `if` 语句都有相应的 `endif` 语句，并确保所有的 `else` 和 `elseif` 语句都出现在 `if` 和 `endif` 之间，且顺序正确。

正确的使用方法：

```
if(CONDITION1)
  # Do something
elseif(CONDITION2)
  # Do something else
else()
  # Do yet another thing
endif()

```

错误的使用方法：

```
if(CONDITION1)
  # Do something
else()
  # Do something else
endif()
else()
  # This else doesn't have a matching if
endif()

```

为了解决你的问题，请检查 `CMakeLists.txt` 文件，确保所有的流控制语句都正确嵌套。
