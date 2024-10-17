
--- 
title:  Python根据EXCEL自动生成固定格式WORD报告 
tags: []
categories: [] 

---
## 前言

根据客户需求，为节省日常工作量，将平常需要从EXCEL选择、拷贝、粘贴数据到WORD文档中的工作，通过Python程序自动进行EXCEL数据采集、数据分析、数据计算、智能文字拼接工作。

一、新建了一个DataToExcel.py

此文件主要通过与excel进行交互，获取excel中的数据，并对数据进行分析和计算，返回word文档中所需的数据信息。

#!/usr/bin/env python3

#-*- coding:utf-8 -*-

#author:BAGGIO

from openpyxl import load_workbook

from openpyxl import Workbook#导入excel包

from docx import Document#导入Docx包

from docx.shared import Cm,Inches,Pt#导入单位换算函数

from docx.oxml.ns import qn#docx中文字体模块

from docx.enum.text import WD_ALIGN_PARAGRAPH#导入对齐选项

from openpyxl.cell import MergedCell

import time#导入时间

import datetime

import os

引用了以上工具包

在获取excel文件时，由于文件名中有需要拼接的字符串，文件名是由固定名称+每周跨度日期组成，如销售量周报0528-0603.xlsx，前面的“销售周报”为固定文字，后面的“0528-0603”是根据用户所需要生成的报告周期而定，如果用户在屏幕输入日期周则优先拼接输入的日期周，如果用户不输入，则默认取当前日期的 上周日到本周六的日期（因为周报是每周日下午需要完成生成），故先做了一个去日期的函数如下：

```
#region 获取上周周末日期信息

def get_last_weekdate(date=None):

    if date:

        today = datetime.datetime.strptime(str(date), '%Y-%m-%d')

    else:

        today = datetime.datetime.today()

    #获取上周日日期

    end_time = today - datetime.timedelta(days=today.isoweekday())

    #转为0528格式

    str_endtime = end_time.strftime("%m")+end_time.strftime("%d")

    #获取本周六的日期

    start_time = end_time + datetime.timedelta(days=6)

    str_starttime = '-'+start_time.strftime("%m")+start_time.strftime("%d")

    return  str_endtime + str_starttime

#endregion

```

然后初始化文件名，并根据相对路径获取到excel文件

```
 str_name = input("请输入需要生成周报的日期(如0528-0603):")

    excelname = '' 

   #判断用户是否输入日期周，输入则直接采用，未输入则取上周日到本周六日期

    if str_name == '' or len(str_name.strip()) ==0:

        excelname = f'销售量周报' + get_last_weekdate() + '.xlsx'

    else:

        excelname = f'销售量周报' + str_name + '.xlsx'

    LoadPath = excelname  #加载excel路径(这里为相对路径，excel表与该程序在同一文件夹下就能识别，所以只用excel文件名即可)

    #excel表格初始化

    book=load_workbook(LoadPath, data_only=True)#加载已有Excel文档

```

**这里的data_only=True对于有计算公式的excel非常重要，如果excel的sheet页是有计算公式的，那么必须加上data_only=True，否则我们取到单元格里面的值将会是公式本身，而不是值。**

单个数据取值赋值

```
sheet_current_week_result=book['本周结果']#加载需要的工作簿（这里为excel表中的sheet工作簿）

#日均销售量赋值
        str_day_esales = str(round(float(sheet_current_week_result['C6'].internal_value)/7,2)) 

```

一组数据取值赋值，在C列从16行至35行 循环取此列中的值

```
gyindex = 16
        while gyindex &lt; 36:
            #工业本周销售量量数组
            strindex = str(gyindex)
            str_gy_week_sales.append(round(float(sheet_current_week_result['C'+strindex].internal_value),2))
           
            gyindex += 1

```

也可以将列定义，然后循环取一行里面每列的数据

```
last_weeklist = ['k','L','M','N','O','P','Q']

while user_index &lt;= maxrows:
            if sheet_user_result['C' + str(user_index)].internal_value == '1.膨化食品':
                cell = sheet_user_result['B' + str(user_index)]
                lastvalue = 0.00
                currentvalue = 0.00
                #判断是否为合并单元格
                if isinstance(cell, MergedCell):
                    cell = sheet_user_result['B' + str(user_index-1)]
                    
                #if user_index == 392 or user_index == 96:
                #    cell = sheet_user_result['B' + str(user_index-1)]
                user_list.append(cell.internal_value)
                for lastweek in last_weeklist:
                    lastvalue += round(float(sheet_user_result[lastweek + str(user_index)].internal_value),4)

```

代码中有一句非常关键的判断 if isinstance(cell, MergedCell):，这个就是判断当前单元格是否为合并单元格，因为很多计算类型的excel都有一些合并单元格的情形，如果直接取这个被合并的单元格，除非它是合并单元格中的第一个，否则其他所有被合并的单元格里面都没有值，比如一个大类A，下面有5中类a,b,c,d,e，当我们要取中类对应的大类名称，除了中类a能取到对应的大类A名称，其他b，c，d，e都只能取到空值，所以我们需要判断当前单元格是否为合并单元格，如果是则取上一行的单元格里面的值，当然这种只适合两个单元格合并的时候，如果出现多个单元格合并，就需要循环判断上一行是否为合并单元格，直到取到不是合并单元格的那个，然后获取到里面的值。

获取到excel里面的数据后，我们同样的方式打开相对路径下的word或者新建一个word文档，然后将对应的数据填充到word文档中

```
 #保存文件名更新：按获取的日期进行命名
    str_wordname = ''
    if DataToExcel.str_name == '' or len(DataToExcel.str_name.strip()) ==0:
        str_wordname = f'销售量周报' + DataToExcel.get_last_weekdate() + '.docx'
    else:
        str_wordname = f'销售量周报' + DataToExcel.str_name + '.docx'

    WordSavePath=(str_wordname)
    Word=Document()    #创建空Word

```

然后定义文档标题，以及添加相关内容

```
 #全局设置字体
    #Word.styles['Normal'].font.name=u'宋体'
    #Word.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')

    #设置页面布局为A4纸张
    section=Word.sections[0]
    section.page_width = Cm(21) # 设置A4纸的宽度
    section.page_height = Cm(29.7) # 设置A4纸的高度
    section.left_margin = Cm(2.8) #设置左页边距
    section.right_margin = Cm(2.8) #设置右页边距

    Word.add_picture(open('title1.png', mode='rb'),width=Inches(2.83), height=Inches(0.84))

    #圖片格式
    str0=Word.add_paragraph(style=None) #增加一个段落
    str_run0 = str0.add_run(' ') #增加文字块
    str_run0.font.size= Pt(60)   #字体大小
    str_run0.font.name = "华文行楷"
    str_run0._element.rPr.rFonts.set(qn('w:eastAsia'), '华文行楷')  # 设置中文是华文行楷

    #首段 標題  
    str1=Word.add_paragraph(style=None) #增加一个段落
    str1_run=str1.add_run('销售量周报') #增加文字块

    str1_run.afterLines = Pt(1)  # 段前1行
    str1_run.beforeLines = Pt(1) # 段后1行
    str1.paragraph_format.line_spacing_rule = WD_LINE_SPACING.EXACTLY  # 行距固定值
    str1.paragraph_format.line_spacing = Pt(58)  # 行间距，固定值56磅

    str1.alignment = WD_ALIGN_PARAGRAPH.CENTER#居中
    #str1_run.bold=True          #加粗
    str1_run.font.size= Pt(59)   #字体大小
    str1_run.font.color.rgb = RGBColor(255,0,0)  # 字体颜色
    str1_run.font.name = "华文行楷"
    str1_run._element.rPr.rFonts.set(qn('w:eastAsia'), '华文行楷')  # 设置中文是华文行楷
    
    strspace0=Word.add_paragraph(style=None) #增加一个段落
    strspace0 = strspace0.add_run(' ') #增加文字块
    strspace0.font.size= Pt(10)   #字体大小
    strspace0.font.name = "华文行楷"
    strspace0._element.rPr.rFonts.set(qn('w:eastAsia'), '华文行楷')  # 设置中文是华文行楷

```

如果文档中有许多的文字格式不同，这个就需要不断设置每一段文件的格式，虽然比较繁琐，但是非常灵活实用，只需要在一个段落里面添加不同的文字句，然后设置文字句的格式即可。

当然我们也可以在word中添加表格，并将excel里面的数据填充到表格当中

```
#region 标题表格
    #添加标题表格 一行两列
    table = Word.add_table(rows=1, cols=2,style=None)
    table.style.font.size = Pt(16)
    table.style.font.color.rgb = RGBColor(255,0,0)  # 字体颜色
    set_cell_border(
        table.cell(0,0),
        top={},
        bottom={"sz": 20, "val": "single", "color": "#FF0000", "space": "0"},
        left={},
        right={},
        insideH={},
        end={}
    )
    set_cell_border(
        table.cell(0,1),
        top={},
        bottom={"sz": 20, "val": "single", "color": "#FF0000", "space": "0"},
        left={},
        right={},
        insideH={},
        end={}
    )

    #设置行高为1.2厘米
    table.rows[0].height = Cm(1.2)
    table.cell(0,0).width = Cm(8.92)
    table.cell(0,1).width = Cm(7.14)

```

我们也可以通过对excel表格中的数值进行判断，从而根据数值的变化使用不同的文字拼接，使得word报告更加实用确切：

```
#环比
    str_zw4 = '环比'
    str_zw4_desc = ''

    if DataToExcel.str_day_esales_ratio &lt; 0:
        str_zw4_desc = '下降'
    else:
        str_zw4_desc = '增长'

    str_zw4 = str_zw4 + str_zw4_desc + str(abs(DataToExcel.str_day_esales_ratio))+'%，' 
    str_zw4_run=str_zw2.add_run(str_zw4) #增加文字块
    str_zw4_run.font.size= Pt(16)   #字体大小
    str_zw4_run.font.name = "方正仿宋_GBK"
    str_zw4_run._element.rPr.rFonts.set(qn('w:eastAsia'), '方正仿宋_GBK')  # 设置中文是华文行楷

    #增速
    str_zw5 = '增速较上周'
    str_zw5_desc = ''

    if DataToExcel.str_day_esales_increase &lt; 0:
        str_zw5_desc = '下降'
    else:
        str_zw5_desc = '增长'

    str_zw5 = str_zw5 + str_zw5_desc + str(abs(DataToExcel.str_day_esales_increase))+'个百分点。'
    str_zw5_run=str_zw2.add_run(str_zw5) #增加文字块
    str_zw5_run.bold=True          #加粗
    str_zw5_run.font.size= Pt(16)   #字体大小
    str_zw5_run.font.name = "方正仿宋_GBK"
    str_zw5_run._element.rPr.rFonts.set(qn('w:eastAsia'), '方正仿宋_GBK')  # 设置中文是华文行楷

```

当然我们在word中添加表格时，不可避免的会需要设置表格的边框样式，这里我们单独新建了一个函数来设置边框样式

```
#region 设置表格的边框
def set_cell_border(cell, **kwargs): 
    """
    Set cell`s border
    Usage:
    set_cell_border(
        cell,
        top={"sz": 12, "val": "single", "color": "#FF0000", "space": "0"},
        bottom={"sz": 12, "color": "#00FF00", "val": "single"},
        left={"sz": 24, "val": "dashed", "shadow": "true"},
        right={"sz": 12, "val": "dashed"},
    )
    """
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()

    # check for tag existnace, if none found, then create one
    tcBorders = tcPr.first_child_found_in("w:tcBorders")
    if tcBorders is None:
        tcBorders = OxmlElement('w:tcBorders')
        tcPr.append(tcBorders)

    # list over all available tags
    for edge in ('left', 'top', 'right', 'bottom', 'insideH', 'insideV'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = 'w:{}'.format(edge)

            # check for tag existnace, if none found, then create one
            element = tcBorders.find(qn(tag))
            if element is None:
                element = OxmlElement(tag)
                tcBorders.append(element)

            # looks like order of attributes is important
            for key in ["sz", "val", "color", "space", "shadow"]:
                if key in edge_data:
                    element.set(qn('w:{}'.format(key)), str(edge_data[key]))
#endregion 

```

表格里面的单元格，我们也可以像操作excel一样，合并单元格

```
 # 往合并单元格中写入
    cell3 = table_ddfhyc1.cell(0, 5)
    cell4 = table_ddfhyc1.cell(0, 8)
    cell4.merge(cell3)

```

最后所有的赋值、拼接完成后，我们需要保存word文档

```
Word.save(WordSavePath)

```

**-END-**

<mark>**读者福利：如果大家对Python感兴趣，这套python学习资料一定对你有用**</mark>

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以根据这些资料规划好学习计划和方向。 


<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习、Python量化交易等习教程。带你从零基础系统性的学好Python！</mark>

## 零基础Python学习资源介绍

① Python所有方向的<mark>学习路线图</mark>，清楚各个方向要学什么东西

② 600多节<mark>Python课程视频</mark>，涵盖必备基础、爬虫和数据分析

③ 100多个<mark>Python实战案例</mark>，含50个超大型项目详解，学习不再是只会理论

④ 20款主流手游迫解 <mark>爬虫手游逆行迫解教程包</mark>

⑤ <mark>爬虫与反爬虫攻防</mark>教程包，含15个大型网站迫解

⑥ <mark>爬虫APP逆向实战</mark>教程包，含45项绝密技术详解

⑦ 超<mark>300本Python电子好书</mark>，从入门到高阶应有尽有

⑧ 华为出品独家<mark>Python漫画教程</mark>，手机也能学习

⑨ 历年互联网企业<mark>Python面试真题</mark>,复习时非常方便

<img src="https://img-blog.csdnimg.cn/7c1055f9bb6e41af9262556bdf20e084.png#pic_center" alt="在这里插入图片描述">

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取哈）**</mark> <img src="https://img-blog.csdnimg.cn/9f969354b48f4e3ab0253e89203deca2.png#pic_center" alt="在这里插入图片描述">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉实战案例👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/6cf364e7eeb64b0da07021bce5a59ec6.png#pic_center" alt="在这里插入图片描述">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

## 资料领取

<mark>上述这份完整版的Python全套学习资料已经上传网盘，朋友们如果需要可以微信扫描下方二维码输入“领取资料” 即可自动领取</mark> <font color="red" size="3"> **或者**</font> 【】领取
