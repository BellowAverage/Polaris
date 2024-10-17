
--- 
title:  Python 进阶（六）： Excel 基本操作 
tags: []
categories: [] 

---


#### 目录
- - - <ul><li>- 


## 1. 概述

在现实中，很多工作都需要与数据打交道，Excel 作为常用的数据处理工具，一直备受人们的青睐，而大部分人都是手动操作 Excel，如果数据量较小且是一些简单的操作还好说，但如果数据量较大或是一些复杂的操作，工作量可想而知，因此，我们需要掌握一种简单、高效的方法来操作 Excel。

在数据处理方面，Python 一直扮演着重要的角色，对于 Excel 操作，它有着完整且成熟的第三方库，使用也较为简单。

Python 中常用 Excel 操作库如下：
-  **xlrd**：从 Excel 中读取数据，支持 xls、xlsx。 -  **xlwt**：向 Excel 中写入数据，支持 xls。 -  **xlutils**：提供了一些 Excel 的实用操作，比如复制、拆分、过滤等，通常与 xlrd、xlwt 一起使用。 -  **XlsxWriter**：向 Excel 中写入数据，支持 xlsx。 -  **openpyxl** ：用于读写 Excel，支持 xlsx。 
## 2. 写入

我们向 Excel 中写入一些数据。

### 2.1 使用 xlwt

通过 `pip install xlwt` 命令安装。

```
import xlwt

# 创建工作簿
wb = xlwt.Workbook()
# 创建表单
sh = wb.add_sheet('test')
# 创建字体对象
font = xlwt.Font()
# 字体加粗
font.bold = True
alm = xlwt.Alignment()
# 设置左对齐
alm.horz = 0x01
# 创建样式对象
style1 = xlwt.XFStyle()
style2 = xlwt.XFStyle()
style1.font = font
style2.alignment = alm
# write 方法参数1：行，参数2：列，参数3：内容
sh.write(0, 1, '姓名', style1)
sh.write(0, 2, '年龄', style1)
sh.write(1, 1, '张三')
sh.write(1, 2, 50, style2)
sh.write(2, 1, '李四')
sh.write(2, 2, 30, style2)
sh.write(3, 1, '王五')
sh.write(3, 2, 40, style2)
sh.write(4, 1, '赵六')
sh.write(4, 2, 60, style2)
sh.write(5, 0, '平均年龄', style1)
# 保存
wb.save('test.xls')

```

执行结果： <img src="https://img-blog.csdnimg.cn/20200223141121565.PNG#pic" alt="" width="300">

### 2.2 使用 XlsxWriter

通过 `pip install XlsxWriter` 命令安装。

```
import xlsxwriter

# 创建工作簿
workbook = xlsxwriter.Workbook('test.xlsx')
# 创建表单
sh = workbook.add_worksheet('test')
fmt1 = workbook.add_format()
fmt2 = workbook.add_format()
# 字体加粗
fmt1.set_bold(True)
# 设置左对齐
fmt2.set_align('left')
# 数据
data = [
    ['', '姓名', '年龄'],
    ['', '张三', 50],
    ['', '李四', 30],
    ['', '王五', 40],
    ['', '赵六', 60],
    ['平均年龄', '', ]
]
sh.write_row('A1', data[0], fmt1)
sh.write_row('A2', data[1], fmt2)
sh.write_row('A3', data[2], fmt2)
sh.write_row('A4', data[3], fmt2)
sh.write_row('A5', data[4], fmt2)
sh.write_row('A6', data[5], fmt1)
chart = workbook.add_chart({<!-- -->'type': 'line'})
workbook.close()

```

XlsxWriter 可以很方便的生成图表。

```
import xlsxwriter

# 创建工作簿
wk = xlsxwriter.Workbook('test.xlsx')
# 创建表单
sh = wk.add_worksheet('test')
fmt1 = wk.add_format()
fmt2 = wk.add_format()
# 字体加粗
fmt1.set_bold(True)
# 设置左对齐
fmt2.set_align('left')
# 数据
data = [
    ['', '姓名', '年龄'],
    ['', '张三', 50],
    ['', '李四', 30],
    ['', '王五', 40],
    ['', '赵六', 60],
    ['平均年龄', '', ]
]
sh.write_row('A1', data[0], fmt1)
sh.write_row('A2', data[1], fmt2)
sh.write_row('A3', data[2], fmt2)
sh.write_row('A4', data[3], fmt2)
sh.write_row('A5', data[4], fmt2)
sh.write_row('A6', data[5], fmt1)
'''
area：面积图
bar：直方图
column：柱状图
line：折线图
pie：饼图
doughnut：环形图
radar：雷达图
'''
chart = wk.add_chart({<!-- -->'type': 'line'})
# 创建图表
chart.add_series(
    {<!-- -->
        'name':'=test!$B$1',
        'categories':'=test!$B$2:$B$5',
        'values':   '=test!$C$2:$C$5'
    }
)
chart.set_title({<!-- -->'name':'用户年龄折线图'})
chart.set_x_axis({<!-- -->'name':'姓名'})
chart.set_y_axis({<!-- -->'name':'年龄'})
sh.insert_chart('A9', chart)
wk.close()

```

执行结果： <img src="https://img-blog.csdnimg.cn/20200223163358274.PNG#pic" alt="" width="500">

## 3. 读取

我们使用 xlrd 读取之前写入的数据，使用 `pip install xlrd` 命令安装。

```
import xlrd

# 打开
wb = xlrd.open_workbook('test.xlsx')
print( 'sheet名称:', wb.sheet_names())
print( 'sheet数量:', wb.nsheets)
# 根据 sheet 索引获取 sheet
sh = wb.sheet_by_index(0)
# 根据 sheet 名称获取 sheet
# sh = wb.sheet_by_name('test')
print( u'sheet %s 有 %d 行' % (sh.name, sh.nrows))
print( u'sheet %s 有 %d 列' % (sh.name, sh.ncols))
print('第二行内容:', sh.row_values(1))
print('第三列内容:', sh.col_values(2))
print('第二行第三列的值为:', sh.cell_value(1, 2))
print('第二行第三列值的类型为:', type(sh.cell_value(1, 2)))

```

## 4. 修改

之前写入的数据还有一个平均年龄是空着的，我们先读取之前写入的数据，再计算出平均值，最后将平均值写入。这里要用到 xlutils 模块，使用 `pip install xlutils` 安装。

```
import xlrd, xlwt
from xlutils.copy import copy

def avg(list):
    sumv = 0
    for i in range(len(list)):
        sumv += list[i]
    return int(sumv / len(list))
# formatting_info 为 True 表示保留原格式
wb = xlrd.open_workbook('test.xls', formatting_info=True)
# 复制
wbc = copy(wb)
sh = wb.sheet_by_index(0)
age_list = sh.col_values(2)
age_list = age_list[1:len(age_list)-1]
avg_age = avg(age_list)
sh = wbc.get_sheet(0)
# 设置左对齐
alm = xlwt.Alignment()
alm.horz = 0x01
style = xlwt.XFStyle()
style.alignment = alm
sh.write(5, 2, avg_age, style)
wbc.save('test.xls')

```

执行结果： <img src="https://img-blog.csdnimg.cn/20200223183016862.PNG#pic" alt="" width="300">

<img src="https://img-blog.csdnimg.cn/20200215093746977.png#pic_center" alt="" width="500">
