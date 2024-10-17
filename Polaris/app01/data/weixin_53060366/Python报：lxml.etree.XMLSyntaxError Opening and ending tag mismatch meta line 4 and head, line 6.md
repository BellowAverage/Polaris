
--- 
title:  Python报：lxml.etree.XMLSyntaxError Opening and ending tag mismatch meta line 4 and head, line 6 
tags: []
categories: [] 

---
### 【Python】报：lxml.etree.XMLSyntaxError: Opening and ending tag mismatch: meta line 4 and head, line 6, column 8

>  
 **python报错：lxml.etree.XMLSyntaxError: Opening and ending tag mismatch: meta line 4 and head, line 6, column 8** 


<img src="https://img-blog.csdnimg.cn/f3a455bc4b2d4d3a87805ac3edd56a50.png#pic_center" alt="在这里插入图片描述">

##### 问题在 b.html 的第四行上，在web中所有的标签最好都用 / 结束，所以修改：

<img src="https://img-blog.csdnimg.cn/c496ea4f7c9e43bfad09fddd4e456bdd.png#pic_center" alt="在这里插入图片描述">

##### 改好后在运行，不报错了。

<img src="https://img-blog.csdnimg.cn/d9d883f441e247ddaf9701ea0bd00123.png#pic_center" alt="在这里插入图片描述">
