
--- 
title:  5 分钟掌握 openpyxl 操作：Python 轻松处理 Excel 
tags: []
categories: [] 

---
来源：python中文社区

各种数据需要导入Excel？多个Excel要合并？目前，Python处理Excel文件有很多库，openpyxl算是其中功能和性能做的比较好的一个。接下来我将为大家介绍各种Excel操作。

**打开Excel文件**

新建一个Excel文件

```
    &gt;&gt;&gt; from openpyxl import Workbook
    &gt;&gt;&gt; wb = Workbook()

```

打开现有Excel文件

```
    &gt;&gt;&gt; from openpyxl import load_workbook
    &gt;&gt;&gt; wb2 = load_workbook('test.xlsx')

```

打开大文件时，根据需求使用只读或只写模式减少内存消耗。

```
wb = load_workbook(filename='large_file.xlsx', read_only=True)

wb = Workbook(write_only=True)

```

**获取、创建工作表**

获取当前活动工作表：

```
    &gt;&gt;&gt; ws = wb.active

```

创建新的工作表：

```
    &gt;&gt;&gt; ws1 = wb.create_sheet("Mysheet") # insert at the end (default)
    # or
    &gt;&gt;&gt; ws2 = wb.create_sheet("Mysheet", 0) # insert at first position
    # or
    &gt;&gt;&gt; ws3 = wb.create_sheet("Mysheet", -1) # insert at the penultimate position

```

使用工作表名字获取工作表：

```
    &gt;&gt;&gt; ws3 = wb["New Title"]

```

获取所有的工作表名称：

```
    &gt;&gt;&gt; print(wb.sheetnames)
    ['Sheet2', 'New Title', 'Sheet1']
使用for循环遍历所有的工作表：

    &gt;&gt;&gt; for sheet in wb:
    ...     print(sheet.title)

```

**保存**

保存到流中在网络中使用：

```
    &gt;&gt;&gt; from tempfile import NamedTemporaryFile
    &gt;&gt;&gt; from openpyxl import Workbook
    &gt;&gt;&gt; wb = Workbook()
    &gt;&gt;&gt; with NamedTemporaryFile() as tmp:
            wb.save(tmp.name)
            tmp.seek(0)
            stream = tmp.read()
保存到文件：

    &gt;&gt;&gt; wb = Workbook()
    &gt;&gt;&gt; wb.save('balances.xlsx')
保存为模板：

    &gt;&gt;&gt; wb = load_workbook('document.xlsx')
    &gt;&gt;&gt; wb.template = True
    &gt;&gt;&gt; wb.save('document_template.xltx')

```

**单元格**

单元格位置作为工作表的键直接读取：

```
    &gt;&gt;&gt; c = ws['A4']

```

为单元格赋值：

```
    &gt;&gt;&gt; ws['A4'] = 4
    &gt;&gt;&gt; c.value = 'hello, world'

```

多个单元格 可以使用切片访问单元格区域：

```
    &gt;&gt;&gt; cell_range = ws['A1':'C2']

```

使用数值格式：

```
    &gt;&gt;&gt; # set date using a Python datetime
    &gt;&gt;&gt; ws['A1'] = datetime.datetime(2010, 7, 21)
    &gt;&gt;&gt;
    &gt;&gt;&gt; ws['A1'].number_format
    'yyyy-mm-dd h:mm:ss'

```

使用公式：

```
    &gt;&gt;&gt; # add a simple formula
    &gt;&gt;&gt; ws["A1"] = "=SUM(1, 1)"

```

合并单元格时，除左上角单元格外，所有单元格都将从工作表中删除：

```
    &gt;&gt;&gt; ws.merge_cells('A2:D2')
    &gt;&gt;&gt; ws.unmerge_cells('A2:D2')
    &gt;&gt;&gt;
    &gt;&gt;&gt; # or equivalently
    &gt;&gt;&gt; ws.merge_cells(start_row=2, start_column=1, end_row=4, end_column=4)
    &gt;&gt;&gt; ws.unmerge_cells(start_row=2, start_column=1, end_row=4, end_column=4) 

```

**行、列**

可以单独指定行、列、或者行列的范围：

```
    &gt;&gt;&gt; colC = ws['C']
    &gt;&gt;&gt; col_range = ws['C:D']
    &gt;&gt;&gt; row10 = ws[10]
    &gt;&gt;&gt; row_range = ws[5:10]

```

可以使用`Worksheet.iter_rows()`方法遍历行：

```
    &gt;&gt;&gt; for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
    ...    for cell in row:
    ...        print(cell)
    &lt;Cell Sheet1.A1&gt;
    &lt;Cell Sheet1.B1&gt;
    &lt;Cell Sheet1.C1&gt;
    &lt;Cell Sheet1.A2&gt;
    &lt;Cell Sheet1.B2&gt;
    &lt;Cell Sheet1.C2&gt;

```

同样的`Worksheet.iter_cols()`方法将遍历列：

```
    &gt;&gt;&gt; for col in ws.iter_cols(min_row=1, max_col=3, max_row=2):
    ...     for cell in col:
    ...         print(cell)
    &lt;Cell Sheet1.A1&gt;
    &lt;Cell Sheet1.A2&gt;
    &lt;Cell Sheet1.B1&gt;
    &lt;Cell Sheet1.B2&gt;
    &lt;Cell Sheet1.C1&gt;
    &lt;Cell Sheet1.C2&gt;

```

遍历文件的所有行或列，可以使用`Worksheet.rows`属性：

```
    &gt;&gt;&gt; ws = wb.active
    &gt;&gt;&gt; ws['C9'] = 'hello world'
    &gt;&gt;&gt; tuple(ws.rows)
    ((&lt;Cell Sheet.A1&gt;, &lt;Cell Sheet.B1&gt;, &lt;Cell Sheet.C1&gt;),
    (&lt;Cell Sheet.A2&gt;, &lt;Cell Sheet.B2&gt;, &lt;Cell Sheet.C2&gt;),
    (&lt;Cell Sheet.A3&gt;, &lt;Cell Sheet.B3&gt;, &lt;Cell Sheet.C3&gt;),
    (&lt;Cell Sheet.A4&gt;, &lt;Cell Sheet.B4&gt;, &lt;Cell Sheet.C4&gt;),
    (&lt;Cell Sheet.A5&gt;, &lt;Cell Sheet.B5&gt;, &lt;Cell Sheet.C5&gt;),
    (&lt;Cell Sheet.A6&gt;, &lt;Cell Sheet.B6&gt;, &lt;Cell Sheet.C6&gt;),
    (&lt;Cell Sheet.A7&gt;, &lt;Cell Sheet.B7&gt;, &lt;Cell Sheet.C7&gt;),
    (&lt;Cell Sheet.A8&gt;, &lt;Cell Sheet.B8&gt;, &lt;Cell Sheet.C8&gt;),
    (&lt;Cell Sheet.A9&gt;, &lt;Cell Sheet.B9&gt;, &lt;Cell Sheet.C9&gt;))

```

或`Worksheet.columns`属性：

```
    &gt;&gt;&gt; tuple(ws.columns)
    ((&lt;Cell Sheet.A1&gt;,
    &lt;Cell Sheet.A2&gt;,
    &lt;Cell Sheet.A3&gt;,
    &lt;Cell Sheet.A4&gt;,
    &lt;Cell Sheet.A5&gt;,
    &lt;Cell Sheet.A6&gt;,
    ...
    &lt;Cell Sheet.B7&gt;,
    &lt;Cell Sheet.B8&gt;,
    &lt;Cell Sheet.B9&gt;),
    (&lt;Cell Sheet.C1&gt;,
    &lt;Cell Sheet.C2&gt;,
    &lt;Cell Sheet.C3&gt;,
    &lt;Cell Sheet.C4&gt;,
    &lt;Cell Sheet.C5&gt;,
    &lt;Cell Sheet.C6&gt;,
    &lt;Cell Sheet.C7&gt;,
    &lt;Cell Sheet.C8&gt;,
    &lt;Cell Sheet.C9&gt;))

```

使用`Worksheet.append()`或者迭代使用`Worksheet.cell()`新增一行数据：

```
    &gt;&gt;&gt; for row in range(1, 40):
    ...     ws1.append(range(600))

    &gt;&gt;&gt; for row in range(10, 20):
    ...     for col in range(27, 54):
    ...         _ = ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))

```

插入操作比较麻烦。可以使用`Worksheet.insert_rows()`插入一行或几行：

```
     &gt;&gt;&gt; from openpyxl.utils import get_column_letter
     &gt;&gt;&gt; ws.insert_rows(7) 
     &gt;&gt;&gt; row7 = ws[7]
     &gt;&gt;&gt; for col in range(27, 54):
    ...         _ = ws3.cell(column=col, row=7, value="{0}".format(get_column_letter(col)))

```

`Worksheet.insert_cols()`操作类似。`Worksheet.delete_rows()`和`Worksheet.delete_cols()`用来批量删除行和列。

**只读取值**

使用`Worksheet.values`属性遍历工作表中的所有行，但只返回单元格值：

```
    for row in ws.values:
       for value in row:
         print(value)

```

`Worksheet.iter_rows()`和`Worksheet.iter_cols()`可以设置`values_only`参数来仅返回单元格的值：

```
    &gt;&gt;&gt; for row in ws.iter_rows(min_row=1, max_col=3, max_row=2, values_only=True):
    ...   print(row)
    (None, None, None)
    (None, None, None)
```

作者：Sinchard，主攻Python库文档翻译，开发代码片段，源码分析

Blog：zhihu.com/people/aiApple

<img src="https://img-blog.csdnimg.cn/img_convert/2812cc3afa9b832c4c98c53ace2a0deb.png">
