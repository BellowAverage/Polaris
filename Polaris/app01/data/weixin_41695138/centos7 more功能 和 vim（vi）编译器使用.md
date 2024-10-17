
--- 
title:  centos7 more功能 和 vim（vi）编译器使用 
tags: []
categories: [] 

---
### more功能
1. 最基本的指令就是按空白键（space）就往下一页显示，按b键就会往回（back）一页显示1. q 键退出
### vim编译器使用

<img src="https://img-blog.csdnimg.cn/fd9a4e3e7b6f4334a6b9d6ee83af6167.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
1. 直接打开文件并定位到第五行： vim a.txt +5 vi a.txt +5, 这两个命令都可以实现 <img src="https://img-blog.csdnimg.cn/e01a55e9432a462d9f0b1f236faec7ab.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">1. 命令模式下常用命令 dd 删除光标所在行 u 撤销上一次命令 yy 复制光标所在行 p 粘贴； 这两个命令结合使用，先 yy 后 p,则能实现复制当前行到下一行中。 gg 回到文件的顶部 G 回到文件的末尾 /XXX 查找 XXX 这样的字符串1. 底行模式下的常用指令 :w 保存 :q 退出 :wq 保存并退出 :q! 不保存退出 :set nu 设置行号