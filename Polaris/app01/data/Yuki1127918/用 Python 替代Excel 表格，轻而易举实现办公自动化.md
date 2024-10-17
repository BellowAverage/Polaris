
--- 
title:  用 Python 替代Excel 表格，轻而易举实现办公自动化 
tags: []
categories: [] 

---
过去，在很多金融、市场、行政的招聘中，面试官都会问一句：“你精通 EXCEL 吗？”

**但今天，他们可能更喜欢问：“你会 Python 吗？**”

越来越多的企业开始用 Python 处理数据，特别是金融、证券、商业、互联网等领域。**在顶级公司的高端职位中，Python 更是成为了标配：**

<img src="https://img-blog.csdnimg.cn/22d97cb25a2a47049411320091d493a4.jpeg#pic_center" alt="在这里插入图片描述">

**Python 究竟有什么法力能让大家如此青睐？**

举个例子：在过去，如果老板想要获取 A 股所有股票近 2 年的数据，你可能需要 **登录-查询-下载-记录到excel** 循环 500 多次，即使你是一个没有感情的复制机器人，也需要一两天的时间。

但如果你掌握了 Python，只需要写个脚本，**泡杯咖啡的功夫 **数据就全部下载好了。

再加上 Python 强大的绘图功能，你可以一次性完成 数据收集 — 整理 — 分析 — 绘图的过程，直接把分析结果用图表呈现出来。

<img src="https://img-blog.csdnimg.cn/1782633aa4584894a5403fb72d8ba987.jpeg#pic_center" alt="在这里插入图片描述">

**我们总结了一下利用 python 操作 Excel 文件的第三方库和方法。**

**内容出自课程——《OpenPyXL 处理 Excel 基础入门》，欢迎大家来实验边敲代码边学习～**

<img src="https://img-blog.csdnimg.cn/a2a8fba9656c411d8a258f4d99249d99.jpeg#pic_center" alt="在这里插入图片描述">

首先，我们来学习一下，如何 **用 Python 创建和保存 Excel 文档**。

对于经常与数据打交道的人来说，Excel 是经常使用的工具；对于与数据打交道的程序员来说，OpenPyXL 库是一个利器。Python 官方提供了这样一个库，让我们可以直接通过 Python 代码实现对 Excel 文件的操作，操作文件格式包括 xlsx、xlsm、xltx、xltm。

### 知识点
- 创建/打开工作簿- 访问工作表单元及其值- 保存工作表
让我们先来学习简单的创建和保存功能。

### 创建/打开工作簿

首先，下载实验所需 shiyanlou.xlsx 示例文件，同时安装指定版本的 openpyxl 库。

```
!wget -nc "https://labfile.oss.aliyuncs.com/courses/1585/shiyanlou.xlsx"
!pip install openpyxl==3.0.3

```

使用 openpyxl 不需要在文件系统上创建文件，只需导入 Workbook 类并开始工作：

教学代码：

```
from openpyxl import Workbook

wb = Workbook()  # 实例化一个工作簿对象

print(wb)

```

也可以打开本地已有的工作簿进行实验操作：

```
from openpyxl import load_workbook

wb = load_workbook(filename='shiyanlou.xlsx')

print(wb)

```

load_workbook 中可以使用以下几个参数：
- data_only：带有公式的单元格是否具有公式（默认具有）或上一次 Excel 读取工作表时存储的值。- keep_vba：设置是否保留任何 Visual Basic 元素（默认保留），可选择保留但是不支持编辑。
工作簿创建时总是会默认创建一个名为 Sheet 工作表，可以通过使用Workbook.active 属性获取:

```
ws = wb.active  # 获取当前活跃的工作表
print(ws)

```

也可以通过 Workbook.create_sheet() 创建工作表并命名，若不设置名字参数则默认命名为 sheet，sheet1，sheet2…创建的工作表位置默认总是插入到最后：

```
ws = wb.create_sheet() # sheet
ws1 = wb.create_sheet("Mysheet")  # 命名为 Mysheet
ws2 = wb.create_sheet("Mysheet1", 0)  # 新建 Mysheet1 工作表插入到第一个位置
ws3 = wb.create_sheet("Mysheet2", -1)  # 新建 Mysheet2 工作表插入到倒数第二个的位置
ws.title = "shiyanlou"  # 将上述 ws 工作表重命名为 shiyanlou

print("Success")

```

默认情况下，工作表的标签背景颜色为白色。我们可以通过 Worksheet.sheet_properties.tabColor 属性改变颜色：

```
ws.sheet_properties.tabColor = "1072BA"  # RGB 格式
print(ws.sheet_properties.tabColor)

```

<img src="https://img-blog.csdnimg.cn/f213173713f341e2ba10e9699853b337.jpeg#pic_center" alt="在这里插入图片描述">

我们给工作表取名后，可以把它作为该工作簿的一个键，简化后续代码，例如：

```
ws = wb["shiyanlou"]
print(ws)

```

若想查看该工作簿下的所有工作表，可以通过函数 Workbook.sheetname：

```
print(wb.sheetnames)

```

也可以通过迭代的方式打印所有工作表

```
for sheet in wb:
    print(sheet.title)

```

我们可以通过 Workbook.copy_worksheet() 方法在单个工作簿中创建工作表的副本：

```
source = wb.active  # 获取活跃的工作表
target = wb.copy_worksheet(source)  # 上述获取的工作表为其创建副本

print(target)

```

### 访问工作表单元及其值

前面我们已经知道了如何创建获取工作簿及工作表，接下来我们将学习修改单元格的内容。以下操作基于 shiyanlou.xlsx 工作簿中的 shiyanlou 工作表进行。

单元格可以直接作为工作表的键进行访问赋值，用 value 属性进行值访问：

```
c = ws['A4']  # 将访问 A4 单元格
ws['A4'] = 4  # 对 A4 单元格进行赋值

c.value  # 访问 A4 单元格的值，同 ws['A4'].value

```

注意：在内存中创建工作表时，它不包含任何单元格，单元格都是在首次访问时自动创建的。

以上代码也可以通过更简便的代码实现：

```
d = ws.cell(row=4, column=2, value=10)  #  B4 进行赋值

ws['B4'].value  # 访问单元格的值

```

### 访问多个单元格

可以使用切片访问范围为 A1 到 C2 的所有单元格：

```
cell_range

```

行或列的范围可以类似地获得：

```
# 访问列
colC = ws['C']
col_range = ws['C:D']

# 访问行
row10 = ws[10]
row_range = ws[5:10]

print(col_range, row_range)

```

也可以使用 Worksheet.iter_rows() 返回行：

```
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
    for cell_row in row:
        print(cell_row)

```

使用 Worksheet.iter_cols() 返回列：

```
for col in ws.iter_cols(min_row=1, max_col=3, max_row=2):
    for cell_col in col:
        print(cell_col)

```

如果需要遍历工作表的所有行或列，则可以使用 Worksheet.rows 属性。出于性能原因，该属性在只读模式下不可用：

```
ws['C9'] = 'hello world'
tuple(ws.rows)

```

或者使用 Worksheet.columns 属性。出于性能原因，该属性在只读模式下不可用：

```
tuple(ws.columns)

```

### 访问值

如果只需要工作表中的值，则可以使用该 Worksheet.values 属性。遍历工作表中的所有行，但仅返回单元格值：

```
for row in ws.values:
    for value in row:
        print(value)

```

Worksheet.iter_rows() 和 Worksheet.iter_cols() 可以用 values_only 参数，只返回单元格的值：

```
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2, values_only=True):
    print(row)

```

### 保存工作表

将我们之前创建的工作簿保存格式为 xlsx 的文件，若已存在则覆盖：

```
wb.save("shiyanlou.xlsx")

```

### 关于Python技术储备

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

#### 一、Python所有方向的学习路线

Python所有方向路线就是把Python常用的技术点做整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。

<img src="https://img-blog.csdnimg.cn/img_convert/9f49b566129f47b8a67243c1008edf79.png" alt="">

#### 二、学习软件

工欲善其事必先利其器。学习Python常用的开发软件都在这里了，给大家节省了很多时间。

<img src="https://img-blog.csdnimg.cn/img_convert/8c4513c1a906b72cbf93031e6781512b.png" alt="">

#### 三、入门学习视频

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

<img src="https://img-blog.csdnimg.cn/afc935d834c5452090670f48eda180e0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56iL5bqP5aqb56eD56eD,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="">

#### 四、实战案例

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/img_convert/252731a671c1fb70aad5355a2c5eeff0.png" alt="">

#### 五、面试资料

我们学习Python必然是为了找到高薪的工作，下面这些面试题是来自阿里、腾讯、字节等一线互联网大厂最新的面试资料，并且有阿里大佬给出了权威的解答，刷完这一套面试资料相信大家都能找到满意的工作。

<img src="https://img-blog.csdnimg.cn/img_convert/6c361282296f86381401c05e862fe4e9.png" alt=""> <img src="https://img-blog.csdnimg.cn/img_convert/d2d978bb523c810abca3abe69e09bc1a.png" alt="">

###### 这份完整版的Python全套学习资料已经上传CSDN，朋友们如果需要可以微信扫描下方CSDN官方认证二维码免费领取【`保证100%免费`】

<img src="https://img-blog.csdnimg.cn/1d2a69f2d57e4d1cb444037b17af8607.png" alt="">
