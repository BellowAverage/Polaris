
--- 
title:  在Excel中按条件筛选数据并存入新的表 
tags: []
categories: [] 

---
## 案例

老板想要看去年每月领料数量大于1000的数据。手动筛选并复制粘贴出来，需要重复操作12次，实在太麻烦了，还是让Python来做吧。磨刀不误砍柴工，先整理一下思路：

>  
 1·读取原表，将数量大于1000的数据所对应的行整行提取（如同在excel表中按数字筛选大于1000的） 2·将提取的数据写入新的Excel表 


<img src="https://img-blog.csdnimg.cn/ee0dc869abd14b258831b48665ebd7d4.png" alt="在这里插入图片描述">

## 说干就干

```
#1.获取满足条件的数据
from openpyxl import load_workbook
wb = load_workbook("每月物料表.xlsx")
data = {
   <!-- -->} #储存所有工作表中满足条件的数据，以
```
