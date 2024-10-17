
--- 
title:  Python 操作pdf(pdfplumber读取PDF写入Exce) 
tags: []
categories: [] 

---
<img alt="" src="https://img-blog.csdnimg.cn/img_convert/f1d7d247b7961a75528a2f18e4ff31fb.webp?x-oss-process=image/format,png">

## 1. Python 操作pdf(pdfplumber读取PDF写入Exce)

### 1.1 安装pdfplumber模块库:

```
安装pdfplumber: pip install pdfplumber
复制代码
```

**pdfplumber.PDF类**

pdfplumber.PDF类表示单个PDF ,并具有两个主要属性:

     |属性   |说明  
 |------
   |pdf.metadata   |从PDF的Info中获取元数据键/值对字典。通常包括"CreationDate，“ModDater"，"Producer"等  
   |pdf.pages   |返回一个包含pdfplumber. Page实例的列表,每一一个实例代表PDF每一页的信息  

**pdfplumber.Page类**

pdfplumber.Page类常用属性

     |属性page_ number   |说明  
 |------
   |.page_ number   |顺序页码,从1第一页开始,从第二页开始2 ,依此类推  
   |.width   |页面的宽度  
   |.height   |页面的高度  
   |.objects/ . chars/ .line  
