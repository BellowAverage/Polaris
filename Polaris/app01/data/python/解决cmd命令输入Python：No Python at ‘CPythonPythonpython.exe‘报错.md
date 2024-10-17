
--- 
title:  解决cmd命令输入Python：No Python at ‘C:\*******************\Python\Python\python.exe‘报错 
tags: []
categories: [] 

---
## 场景：

在win10/7系统中，删除了python3.9，换装python3.10版本以后。 在cmd.exe管理器输入python后报错

## 问题描述

win+r运行框输入cmd 在cmd窗口中输入python后确认报错： No Python at ‘C:\Users\Administrator\AppData\Local\Programs\Python\Python\python.exe’ <img src="https://img-blog.csdnimg.cn/adab09c74139488494879e636b4f7a5b.png" alt="在这里插入图片描述"> 换输入：py 3.10 能正常运行 <img src="https://img-blog.csdnimg.cn/f84b660160aa47b7b7d57d26dc89eaf5.png" alt="在这里插入图片描述"> 重新装回python3.9版本，后输入:python 发现问题解决。 <img src="https://img-blog.csdnimg.cn/a150a7f16376407198056a530156a0c8.png" alt="在这里插入图片描述"> 但是，为了了解3.10版本的最新语法，match case 需要3.10版本。

## 原因分析：

查看系统变量，发现没有python3.10的系统变量，但是3.9的系统变量还在。 因为系统变量的问题导致了cmd命令运行时候指向了python3.9版本

## 解决方案：

如图：

右键我的电脑&gt;选择属性&gt;高级系统设置&gt;高级&gt;环境变量&gt;系统变量&gt;双击Path环境变量打开&gt;新建 新增C:*********\Python310\Scripts\和C:********\Python310\两个属性，并且点击上移到最上方，然后确认保存。

<img src="https://img-blog.csdnimg.cn/44d6e893892f457090be9d1a6b2f136f.png" alt="在这里插入图片描述"> 再次回到cmd.exe界面，输入python验证 <img src="https://img-blog.csdnimg.cn/2eed1eaa8dde48b5b40ec682f79cfe4c.png" alt="在这里插入图片描述"> 出现python 3.10.2 完美解决。
