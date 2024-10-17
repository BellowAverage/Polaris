
--- 
title:  [Excel] vlookup函数 
tags: []
categories: [] 

---
## VLOOKUP用法

```
VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])

```

其中：
- `lookup_value`是你要查找的值- `table_array`是你要在其中进行查找的表格区域- `col_index_num`是你要返回的在`table_array`中列索引号- `range_lookup`是一个可选参数，用于指定查找方式，通常设为FALSE以确保精确匹配。
## 案例

在sheet1中`name` 为空

<img src="https://img-blog.csdnimg.cn/direct/43f0974bcf0f46e09e53f4f1e729da0e.png" alt="在这里插入图片描述">

**需要在sheet2中根据id找到对应的值**

<img src="https://img-blog.csdnimg.cn/direct/0c068905270146dca5e5e20559817284.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/direct/6ca5897c20c843899aeb3fe7a76a4c46.png" alt="在这里插入图片描述">

在Excel中，你可以使用`VLOOKUP`函数来实现在Sheet1中的B列填入对应的Sheet2中B列的值。VLOOKUP函数的语法如下： 所以，你可以在Sheet1的C列中输入以下公式：

```
=VLOOKUP(A2, Sheet2!A:B, 2, FALSE)

```
-  `A2` 这个公式会根据Sheet1中A列的值， -  `Sheet2!A:B` 从Sheet2中的A列到B列的区域中查找对应的值 -  `2` 并返回`Sheet2!A:B`中第2列的值, 即B列 
最后将公式拖动填充到B列的其他单元格即可。
