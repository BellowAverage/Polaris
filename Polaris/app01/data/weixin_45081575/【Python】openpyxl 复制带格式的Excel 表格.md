
--- 
title:  【Python】openpyxl 复制带格式的Excel 表格 
tags: []
categories: [] 

---
>  
 记录一下关于 python 操作 excel表 


### 简单复制excel表

>  
 这个复制不了颜色之类的格式，但是边边框框可以带上 


```
import copy
import openpyxl


class SplitMultiSheet:
    """复制带格式"""

    def split_sheet(self, wb: openpyxl.Workbook, sn: str):
        """
        :param wb:  excel表格
        :param sn:  sheet_name
        :return:
        """
        # _sn: sheet_name, ws: Worksheet
        for _sn, ws in zip(wb.sheetnames, wb):
            if _sn != sn:
                wb.remove(ws)
        # 保存文件、关闭文件
        wb.save(f'{<!-- -->sn}.xlsx')
        wb.close()

    def main(self, file_path: str):
        wb = openpyxl.load_workbook(filename=file_path)
        for sn in wb.sheetnames:
            # 深拷贝
            new_wb = copy.deepcopy(wb)
            self.split_sheet(wb=new_wb, sn=sn)


if __name__ == '__main__':
    path = 'xxx.xlsx'
    sms = SplitMultiSheet()
    sms.main(file_path=path)


```

## 格式全复制

### 复制全表

>  
 这段代码用于复制整个excel表。 以下这段代码引用于  


```
import copy
import openpyxl
from openpyxl.utils import get_column_letter

path = "数据.xlsx"
save_path = "数据-复制.xlsx"

wb = openpyxl.load_workbook(path)
wb2 = openpyxl.Workbook()

sheetnames = wb.sheetnames
for sheetname in sheetnames:
    print(sheetname)
    sheet = wb[sheetname]
    sheet2 = wb2.create_sheet(sheetname)

    # tab颜色
    sheet2.sheet_properties.tabColor = sheet.sheet_properties.tabColor

    # 开始处理合并单元格形式为“(&lt;CellRange A1：A4&gt;,)，替换掉(&lt;CellRange 和 &gt;,)' 找到合并单元格
    wm = list(sheet.merged_cells)
    if len(wm) &gt; 0:
        for i in range(0, len(wm)):
            cell2 = str(wm[i]).replace('(&lt;CellRange ', '').replace('&gt;,)', '')
            sheet2.merge_cells(cell2)

    for i, row in enumerate(sheet.iter_rows()):
        sheet2.row_dimensions[i+1].height = sheet.row_dimensions[i+1].height
        for j, cell in enumerate(row):
            sheet2.column_dimensions[get_column_letter(j+1)].width = sheet.column_dimensions[get_column_letter(j+1)].width
            sheet2.cell(row=i + 1, column=j + 1, value=cell.value)

            # 设置单元格格式
            source_cell = sheet.cell(i+1, j+1)
            target_cell = sheet2.cell(i+1, j+1)
            target_cell.fill = copy.copy(source_cell.fill)
            if source_cell.has_style:
                target_cell._style = copy.copy(source_cell._style)
                target_cell.font = copy.copy(source_cell.font)
                target_cell.border = copy.copy(source_cell.border)
                target_cell.fill = copy.copy(source_cell.fill)
                target_cell.number_format = copy.copy(source_cell.number_format)
                target_cell.protection = copy.copy(source_cell.protection)
                target_cell.alignment = copy.copy(source_cell.alignment)

if 'Sheet' in wb2.sheetnames:
    del wb2['Sheet']
wb2.save(save_path)

wb.close()
wb2.close()

print('Done.')

```

### 带格式拆分多个sheet表

>  
 这段代码用于拆分多个sheet，是带格式的拆分！ 


```
# -*- coding: utf-8 -*-
# @Time     : 2022-04-13  11:36 
# @File     : split_format_excel.py
# @software : PyCharm

"""如何复用
    1. 修改 输入、输出的文件路径，19~20行
    2. 运行即可
"""



import copy
import openpyxl
from openpyxl.utils import get_column_letter as gcl

# 指定输入、输出文件路径
input_file_path = './split_format_excel_file/xxx.xlsx'
output_file_path = './output/'


class SplitMultiSheet:
    """复制带格式"""

    def split_sheet(self, wb: openpyxl.Workbook, sn: str):
        new_wb = openpyxl.Workbook()
        print('sheet_name：', sn)
        sheet = wb[sn]
        sheet2 = new_wb.create_sheet(sn)
        # tab颜色
        sheet2.sheet_properties.tabColor = sheet.sheet_properties.tabColor

        # 开始处理合并单元格形式为“(&lt;CellRange A1：A4&gt;,)，替换掉(&lt;CellRange 和 &gt;,)' 找到合并单元格
        wm = list(sheet.merged_cells)
        if len(wm) &gt; 0:
            for i in range(0, len(wm)):
                cell2 = str(wm[i]).replace('(&lt;CellRange ', '').replace('&gt;,)', '')
                sheet2.merge_cells(cell2)
        #
        for i, row in enumerate(sheet.iter_rows()):
            sheet2.row_dimensions[i + 1].height = sheet.row_dimensions[i + 1].height
            for j, cell in enumerate(row):
                sheet2.column_dimensions[gcl(j + 1)].width = sheet.column_dimensions[gcl(j + 1)].width
                sheet2.cell(row=i + 1, column=j + 1, value=cell.value)

                # 设置单元格格式
                source_cell = sheet.cell(i + 1, j + 1)
                target_cell = sheet2.cell(i + 1, j + 1)
                target_cell.fill = copy.copy(source_cell.fill)
                if source_cell.has_style:
                    target_cell._style = copy.copy(source_cell._style)
                    target_cell.font = copy.copy(source_cell.font)
                    target_cell.border = copy.copy(source_cell.border)
                    target_cell.fill = copy.copy(source_cell.fill)
                    target_cell.number_format = copy.copy(source_cell.number_format)
                    target_cell.protection = copy.copy(source_cell.protection)
                    target_cell.alignment = copy.copy(source_cell.alignment)
        # 第一个 Sheet 默认为 Sheet，可以选择删除
        if 'Sheet' in new_wb.sheetnames:
            del new_wb['Sheet']
        new_wb.save(f"{<!-- -->output_file_path}{<!-- -->sn}.xlsx")
        new_wb.close()

    def main(self):
        # 打开文件
        wb = openpyxl.load_workbook(filename=input_file_path)
        # 循环读取多个sheet，并拆分
        for sn in wb.sheetnames:
            self.split_sheet(wb=wb, sn=sn)


if __name__ == '__main__':
    sms = SplitMultiSheet()
    sms.main()
    print('Done.')


```
