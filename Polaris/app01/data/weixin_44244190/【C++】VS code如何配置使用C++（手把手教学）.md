
--- 
title:  【C++】VS code如何配置使用C++（手把手教学） 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>VS code如何配置使用C++（手把手教学）</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - -  
  
  


## 1. 下载MinGW64

https://sourceforge.net/projects/mingw-w64/files/

<img src="https://img-blog.csdnimg.cn/6baf3e0248f44455b593c131faa7024e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/80ddbe0eebf74fb3bf47de6d81cead21.png" alt="在这里插入图片描述">

下载后，打开，解压：

<img src="https://img-blog.csdnimg.cn/1ffd5ab8536b4d80b574979dcea2e572.png" alt="在这里插入图片描述"> 解压到`D:\mingw64`路径路径下：

<img src="https://img-blog.csdnimg.cn/715caf9e5fce44e19b54b8707f11b943.png" alt="在这里插入图片描述">

## 2. 配置环境变量

将 `D:\mingw64\bin` 放置于环境变量中：

<img src="https://img-blog.csdnimg.cn/87364a14f60540d98f20fb292128299d.png" alt="在这里插入图片描述">

打开 `cmd` 输入` g++` 测试是否安装好，如果安装好会显示：

<img src="https://img-blog.csdnimg.cn/d4cd3dbfae31437d925a5564d091cdc7.png" alt="在这里插入图片描述">

## 3. vs code配置

创建一个空文件夹，确保这个文件夹所在的文件路径没有中文字符，使用vs code打开。

插件中输入C++ 选择C/C++插件，并安装： <img src="https://img-blog.csdnimg.cn/468b0ccade9d48a6a210c06924e680a1.png" alt="在这里插入图片描述">

安装完成之后，直接在VsCode中按 `ctrl+shift+p` 快捷键，并选择`C/C++: Edit configurations (UI)`：

<img src="https://img-blog.csdnimg.cn/5d6811667d414292aebb4dd3c7dc74df.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/cc48088fcbbe401bba043de865e43e21.png" alt="在这里插入图片描述">

创建一个text.cpp文件，输入如下代码进行测试：

```
#include &lt;iostream&gt;

int main(){<!-- -->
    std::cout &lt;&lt; "cout" &lt;&lt; std::endl;
}

```

<img src="https://img-blog.csdnimg.cn/4fb8d09a16f54271a2ba3234538da92f.png" alt="在这里插入图片描述">

点击`run`或者按住`ctrl+F5`调试代码。

<img src="https://img-blog.csdnimg.cn/0e6bd0c295804c28869d1d206a9eec16.png" alt="在这里插入图片描述"> 选择`C++ (GDB/LLDB)`

<img src="https://img-blog.csdnimg.cn/c962aafae1dc47a3af876161c06060a1.png" alt="在这里插入图片描述">

选择 ` g++` ：

<img src="https://img-blog.csdnimg.cn/a7b37755065e48dca796842066fa5759.png" alt="在这里插入图片描述">

可以看到会生成一个exe文件：

<img src="https://img-blog.csdnimg.cn/ea85c584d97d4406885965e3dfa27468.png" alt="在这里插入图片描述">

点击 Terminal ，输入./text.cpp，运行exe测试：

<img src="https://img-blog.csdnimg.cn/38ee84a4f1874047ac591be49771ff8f.png" alt="在这里插入图片描述">
