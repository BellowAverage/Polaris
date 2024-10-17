
--- 
title:  使用Python在Windows环境下切换输入法 
tags: []
categories: [] 

---


#### 文章目录

  - 
  <li>
   <ul>
    - 
    - 
   


## 1. 搭建环境

### 1.1 安装Python库

```
pip install pywin32

```

### 1.2 检查输入法是否正确安装

  要切换到想要的输入法，则首先需要安装好对应的输入法，比如系统自带的中文输入法、英文输入法或者其他常用的输入法(如搜狗输入法)。那么如何检查是否正确安装呢？

  键盘同时按下Windows+R，则弹出运行界面，输入regedit.exe并按下回车键，如下图所示： <img src="https://img-blog.csdnimg.cn/24e0885c58e3487b8935c9ea194f791f.png#pic_center" alt="在这里插入图片描述">

  打开注册表后，在注册表编辑器上找到位置：HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\ControlSet001\Control\Keyboard Layouts。可以看到该
