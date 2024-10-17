
--- 
title:  python openpyxl库读写更新excel表格 
tags: []
categories: [] 

---
安装openpyxl库

```
pip install openpyxl -i https://pypi.tuna.tsinghua.edu.cn/simple # 清华镜像源

```

### 1.读取excel文件内容

```
def read_file(self):
        """
        读取表格文件
        :param file_path:
        :return:
        """
        f = openpyxl.load_workbook(self.file_path)
        # sheet_list = f.sheetnames
        sheet_platform = f.get_sheet_by_name(self.region)  # 获取第一个sheet内容
        log.logger.debug("sheet_platform:{}".format(sheet_platform))
        #
        # 获取sheet的最大行数和列数
        rows = sheet_platform.max_row
        cols = sheet_platform.max_column
        for r in range(1, rows):
            for c in range(1, cols):
                log.logger.debug(sheet_platform.cell(r, c).value)
            if r == 10:
                break

```

### 2.写入excel文件内容

```
def write_file(self, file_path):
        """
        创建并写入新文件
        :param file_path:
        :return:
        """
        outwb = openpyxl.Workbook()  # 打开一个将写的文件
        outws = outwb.create_sheet(title="测试", index=0)  # 在将写的文件创建sheet
        for row in range(1, 70000):
            for col in range(1, 4):
                outws.cell(row, col).value = row * 2  # 写文件
            log.logger.debug(row)
        outwb.save(file_path)  # 一定要记得保存

```

### 3.更新excel文件内容

```
def update_file(self, row, col, content):
        """
        :param row: 行
        :param clo: 列
        :param content: 写入内容
        :return: None
        """
        log.logger.debug("self.file_path:{}".format(self.file_path))
        f = openpyxl.load_workbook(self.file_path)
        f.template = True
        f.active.title = self.region
        result = f.active.cell(row, col, content)
        if content == "NO":
            result.font = self.red_font()
        elif content == "YES":
            result.font = self.green_font() # 设置字体方法
        result.alignment = self.alignment_config() # 设置对齐方式
        result.border = self.border_config() # 设置边框
        result = f.active.cell(row, 17, datetime.datetime.now())
        result.alignment = self.alignment_config()
        result.border = self.border_config()
        f.save(self.file_path)
        f.close()
	def red_font(self):
        """
        设置字体颜色为红色
        return:
        """
        return Font(color='cc0000', bold=True)

    def green_font(self):
        """
        设置字体颜色为绿色
        return:
        """
        return Font(color='66ff00', bold=True)
	def background_config(self):
        """
        设置单元格颜色
        return:
        """
        return PatternFill(patternType="solid", start_color="3399ff")

    def alignment_config(self):
        """
        设置对其方式
        return
        """
        return Alignment(horizontal='center', vertical='center', wrap_text=False)

    def border_config(self):
        """
        设置边框
        return
        """
        thin = Side(border_style="thin", color="000000")
        return Border(left=thin, right=thin, top=thin, bottom=thin)

```

### 4.设置excel表样式

#### 4.1Border 边框 Side 边线

```
from openpyxl.styles import Border, Side

border_type=Side(border_style=None, color='FF000000')
border = Border(left=border_type,
                right=border_type,
                top=border_type,
                bottom=border_type,
                diagonal=border_type,
                diagonal_direction=0,
                outline=border_type,
                vertical=border_type,
                horizontal=border_type
)
"""
常用的样式：
‘dashDot’,‘dashDotDot’,‘dashed’,‘dotted’,‘double’,
‘hair’,‘medium’,‘mediumDashDot’,‘mediumDashDotDot’,
‘mediumDashed’,‘slantDashDot’,‘thick’,‘thin’
"""

```

#### 4.2设置字体

```
from openpyxl.styles import Font

font = Font(name='Calibri',
            size=11,
            color='FF000000',
            bold=False,
            italic=False,
            vertAlign=None,
            underline='none',
            strike=False)
"""
字体名称、字体大小、字体颜色、加粗、斜体、
纵向对齐方式有三种：baseline，superscript， subscript）、
下划线、删除线，字体颜色可以用RGB 或 aRGB
"""

```

#### 4.3填充

```
from openpyxl.styles import PatternFill

# fill_type 的样式为 None 或 solid
fill = PatternFill(fill_type = None,start_color='FFFFFF',end_color='000000')


"""
fill_type类型有：'none'、'solid'、'darkDown'、'darkGray'、'darkGrid'、'darkHorizontal'、'darkTrellis'、'darkUp'、'darkVertical'、'gray0625'、
'gray125'、'lightDown'、'lightGray'、'lightGrid'、'lightHorizontal'、
'lightTrellis'、'lightUp'、'lightVertical'、'mediumGray'
"""

```

#### 4.4对齐方式

```
from openpyxl.styles import Alignment

align = Alignment(horizontal='left',vertical='center',wrap_text=True)
"""
horizontal代表水平方向，可以左对齐left，还有居中center和右对齐right，分散对齐distributed，跨列居中centerContinuous，两端对齐justify，填充fill，常规general
vertical代表垂直方向，可以居中center，还可以靠上top，靠下bottom，两端对齐justify，分散对齐distributed
自动换行：wrap_text，这是个布尔类型的参数，这个参数还可以写作wrapText
"""

```
