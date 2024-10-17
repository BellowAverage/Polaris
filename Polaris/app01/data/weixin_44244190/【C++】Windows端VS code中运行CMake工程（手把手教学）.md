
--- 
title:  【C++】Windows端VS code中运行CMake工程（手把手教学） 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>Windows端VS code中运行CMake工程（手把手教学）</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  -  
  
  


#### 目录

下载在vscode中安装cmake和cmake tools插件

<img src="https://img-blog.csdnimg.cn/fef08602fca84bebaa2a6fb6cfa46129.png" alt="在这里插入图片描述">

在vscode中打开一个CPP文件和CMakeLists.txt所在的文件夹，按`Ctrl+Shift+P`调出命令输入界面，输入cq或cmake q，选择CMake:Quick Start，或直接按下回车键：

<img src="https://img-blog.csdnimg.cn/00e255e274bc439b845c2b7651c3220f.png" alt="在这里插入图片描述">

选择编译器，第一次运行可以选择让cmake扫描电脑上存在编译器（如果设置了环境变量的话），之后这里多出了GCC，：

<img src="https://img-blog.csdnimg.cn/8f7ab8aa617740648a484d57e30d353e.png" alt="在这里插入图片描述">

我这里选择了visual studio community 2022 Release-amd64

<img src="https://img-blog.csdnimg.cn/18c727599409486ca8acf9050637d2b7.png" alt="在这里插入图片描述">

构建+运行成功

<img src="https://img-blog.csdnimg.cn/5bf6105b03244b9f922d53a550ce3465.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/fd1f9457c77241f09cd9ffd2112ae68d.png" alt="在这里插入图片描述">
