
--- 
title:  python+pyqt制作的可最小化到托盘的桌面图形应用代码实例 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解使用python、pyqt制作的可以最小化到托盘的桌面图形应用实例。 日期：2023年6月11日 作者：任聪聪 


### 效果演示

说明：实现桌面应用显示窗口，关闭窗口缩小到托盘，点击托盘显示窗口，邮件图标显示退出按钮，点击退出按钮即可关闭应用。

动态演示： <img src="https://img-blog.csdnimg.cn/f8211f011c29452a950ddf6b622e0425.gif#pic_center" alt="在这里插入图片描述"> 实际情况： <img src="https://img-blog.csdnimg.cn/7b33074aae854cf8b1c0f0af4abd10f1.png" alt="在这里插入图片描述">

### 环境准备

1.安装pyqt库

```
pip install pyqt5

```

如下提示是我已经安装，未安装会显示下载和安装进度，下图仅供展示用途。 <img src="https://img-blog.csdnimg.cn/b9990fe89f414a54887493e7cff39006.png" alt="在这里插入图片描述"> 2.引入包

```
import sys
from PyQt5.QtWidgets import QApplicatio
```
