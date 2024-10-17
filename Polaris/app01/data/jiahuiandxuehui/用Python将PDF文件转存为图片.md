
--- 
title:  用Python将PDF文件转存为图片 
tags: []
categories: [] 

---
## 案例

 -  因工作中的某些奇葩要求，需要将PDF文件的每页内容转存成按顺序编号的图片。用第三方软件或者在线转换也可以，但批量操作还是Python方便，所谓搞定办公自动化，Python出山，一统天下；Python出征，寸草不生~ O(∩_∩)O 
 -  不过这个需要用到PyMuPDF库，电脑运行cmd，输入“pip install PyMuPDF”安装即可。安装后通过import fitz导入模块。等等，为什么安装的是PyMuPDF，导入的是fitz？俺PyMuPDF就是这么任性，怎么的，爱用不用！哈哈，开个玩笑。其实是因为PyMuPDF曾用名fitz-python，所以只是fitz换了个马甲而已，呵呵。 

```
这里先导入fitz库，用于将PDF文件的页面提取成像素信息（图片）。再导入glob库，用于获取后缀为".pdf"的文件的文件名。os库可新建文件夹。

```

<img src="https://img-blog.csdnimg.cn/6b665511571c44158f11a81afd1b720d.png" alt="在这里插入图片描述">

```
#批量将PDF文件转为图片
import fitz
import glob

```
