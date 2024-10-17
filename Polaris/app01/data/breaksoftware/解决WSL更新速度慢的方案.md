
--- 
title:  解决WSL更新速度慢的方案 
tags: []
categories: [] 

---
在Windows上安装Docker Desktop时，如果选择使用WSL，则可能会出现在运行程序前要求升级WSL的步骤。程序会提示使用下面指令来升级

```
wsl.exe --update

```

<img src="https://img-blog.csdnimg.cn/direct/6c41076b7cfb4c3b9f728a9b946787d8.png" alt="请添加图片描述"> 但是升级速度特别慢，于是在网络不稳定的情况下经常会出现下载失败的情况。 百度里一直没搜到好的方案。 WSL的全称是Windows Subsystem for Linux 2。它是微软的产品，于是我就在微软旗下的bing.com上搜索，第一条搜索结果就给出了准确答案。 在中，有提供WSL 2.1.5的离线包地址（），然后通过迅雷下载它。 <img src="https://img-blog.csdnimg.cn/direct/ff55aeb4663442278db12873d1c7bf5f.png" alt="请添加图片描述"> 安装完之后docker就可以运行了。
