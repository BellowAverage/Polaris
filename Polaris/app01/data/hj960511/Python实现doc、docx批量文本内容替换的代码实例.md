
--- 
title:  Python实现doc、docx批量文本内容替换的代码实例 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解通过python及三方库实现doc、docx的批量文本内容替换的方法教程 日期：2023年5月10日 作者：任聪聪 python3.9版本 


### 前提准备

安装： docx、win32

```
pip install 包名

```

引入：

```
import win32com.client as win32
import docx

```

### 实际效果

可以修改doc、docx中包含图片、表格等多类型内容的文档，批量修改文本，且不乱码。

#### doc、docx文档修改前内容

<img src="https://img-blog.csdnimg.cn/091dbbf517dc4108935413eec5efad83.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/cec2d856a72a4383a1e726f10d03d4a7.png" alt="在这里插入图片描述">

#### doc、docx修改后效果如下，将2转换为成双成对


