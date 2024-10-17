
--- 
title:  一文学会用Python操作Excel+Word+CSV 
tags: []
categories: [] 

---
>  
  作者：奈何缘浅wyj 
  https://juejin.im/post/6868073137263607821 
 

## Python 操作 Excel

### 常用工具

数据处理是 Python 的一大应用场景，而 Excel 又是当前最流行的数据处理软件。因此用 Python 进行数据处理时，很容易会和 Excel 打起交道。得益于前人的辛勤劳作，Python 处理 Excel 已有很多现成的轮子，比如 `xlrd &amp; xlwt &amp; xlutils` 、 `XlsxWriter` 、 `OpenPyXL` ，而在 Windows 平台上可以直接调用 Microsoft Excel 的开放接口，这些都是比较常用的工具，还有其他一些优秀的工具这里就不一一介绍，接下来我们通过一个表格展示各工具之间的特点：



|类型|xlrd&amp;xlwt&amp;xlutils|XlsxWriter|OpenPyXL|Excel开放接口
|------
|读取|支持|不支持|支持|支持
|写入|支持|支持|支持|支持
|修改|支持|不支持|支持|支持
|xls|支持|不支持|不支持|支持
|xlsx|高版本|支持|支持|支持
|大文件|不支持|支持|支持|不支持
|效率|快|快|快|超慢
|功能|较弱|强大|一般|超强大



以上可以根据需求不同，选择合适的工具，现在为大家主要介绍下最常用的 xlrd &amp; xlwt &amp; xlutils 系列工具的使用。

### xlrd &amp; xlwt &amp; xlutils 介绍

xlrd&amp;xlwt&amp;xlutils 是由以下三个库组成：
- `xlrd`：用于读取 Excel 文件；- `xlwt`：用于写入 Excel 文件；- `xlutils`：用于操作 Excel 文件的实用工具，比如复制、分割、筛选等；
### 安装库

安装比较简单，直接用 pip 工具安装三个库即可，安装命令如下：

```
$ pip install xlrd xlwt xlutils

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYUMzOEZFYUNsRzI5bkdJVjRpYnFwMmVwYkQ4YkxldTZnSGh6UXBvMmlheTRkYjNIR2tkT0ZFSkZRLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYURFbkk0aGFsZVRFSnBhbzBxM3lEVUNENTFqV3ZtdU5SUlRhMjNXUWNWZGdaa2RXamljQThxcUEvNjQw?x-oss-process=image/format,png">

### 写入 Excel

接下来我们就从写入 Excel 开始，话不多说直接看代码如下：

```
# 导入 xlwt 库
import xlwt

# 创建 xls 文件对象
wb = xlwt.Workbook()

# 新增两个表单页
sh1 = wb.add_sheet('成绩')
sh2 = wb.add_sheet('汇总')

# 然后按照位置来添加数据,第一个参数是行，第二个参数是列
# 写入第一个sheet
sh1.write(0, 0, '姓名')
sh1.write(0, 1, '专业')
sh1.write(0, 2, '科目')
sh1.write(0, 3, '成绩')

sh1.write(1, 0, '张三')
sh1.write(1, 1, '信息与通信工程')
sh1.write(1, 2, '数值分析')
sh1.write(1, 3, 88)

sh1.write(2, 0, '李四')
sh1.write(2, 1, '物联网工程')
sh1.write(2, 2, '数字信号处理分析')
sh1.write(2, 3, 95)

sh1.write(3, 0, '王华')
sh1.write(3, 1, '电子与通信工程')
sh1.write(3, 2, '模糊数学')
sh1.write(3, 3, 90)

# 写入第二个sheet
sh2.write(0, 0, '总分')
sh2.write(1, 0, 273)

# 最后保存文件即可
wb.save('test.xls')

```

运行代码，结果会看到生成名为 test.xls 的 Excel 文件，打开文件查看如下图所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYVhXdjNmTDJhbXBMb28zcXc2azdmTnV0SHBHOGd6NWxRWjJNMWZ5Qjg3UzNzaWNzczFCdzlObmcvNjQw?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYUFEbGliNlI1YjhPYkc1ME1RNXJXaWFqREhZNmxjd1VVR09aRDZVaWJpYVROcExUR2ljWXdiT2ljcURBUS82NDA?x-oss-process=image/format,png">

以上就是写入 Excel 的代码，是不是很简单，下面我们再来看下读取 Excel 该如何操作。

### 读取 Excel

读取 Excel 其实也不难，请看如下代码：

```
# 导入 xlrd 库
import xlrd

# 打开刚才我们写入的 test_w.xls 文件
wb = xlrd.open_workbook("test_w.xls")

# 获取并打印 sheet 数量
print( "sheet 数量:", wb.nsheets)

# 获取并打印 sheet 名称
print( "sheet 名称:", wb.sheet_names())

# 根据 sheet 索引获取内容
sh1 = wb.sheet_by_index(0)
# 或者
# 也可根据 sheet 名称获取内容
# sh = wb.sheet_by_name('成绩')

# 获取并打印该 sheet 行数和列数
print( u"sheet %s 共 %d 行 %d 列" % (sh1.name, sh1.nrows, sh1.ncols))

# 获取并打印某个单元格的值
print( "第一行第二列的值为:", sh1.cell_value(0, 1))

# 获取整行或整列的值
rows = sh1.row_values(0) # 获取第一行内容
cols = sh1.col_values(1) # 获取第二列内容

# 打印获取的行列值
print( "第一行的值为:", rows)
print( "第二列的值为:", cols)

# 获取单元格内容的数据类型
print( "第二行第一列的值类型为:", sh1.cell(1, 0).ctype)

# 遍历所有表单内容
for sh in wb.sheets():
    for r in range(sh.nrows):
        # 输出指定行
        print( sh.row(r))

```

输出如下结果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYWljOFF0bTE5YmljaWJKUllXQmg1eEJKN0I0VldGNWF5S3dJbWF5VGljZDlwYlhaUGowRnpYQW5mVFEvNjQw?x-oss-process=image/format,png">

细心的朋友可能注意到，这里我们可以获取到**单元格的类型**，上面我们读取类型时获取的是`数字1`，那1表示什么类型，又都有什么类型呢？别急下面我们通过一个表格展示下：



|数值|类型|说明
|------
|0|empty|空
|1|string|字符串
|2|number|数字
|3|date|日期
|4|boolean|布尔值
|5|error|错误



通过上面表格，我们可以知道刚获取单元格类型返回的数字1对应的就是字符串类型。

### 修改 excel

上面说了写入和读取 Excel 内容，接下来我们就说下更新修改 Excel 该如何操作，修改时就需要用到 xlutils 中的方法了。直接上代码，来看下最简单的修改操作：

```
# 导入相应模块
import xlrd
from xlutils.copy import copy

# 打开 excel 文件
readbook = xlrd.open_workbook("test_w.xls")

# 复制一份
wb = copy(readbook)

# 选取第一个表单
sh1 = wb.get_sheet(0)

# 在第五行新增写入数据
sh1.write(4, 0, '王欢')
sh1.write(4, 1, '通信工程')
sh1.write(4, 2, '机器学习')
sh1.write(4, 3, 89)

# 选取第二个表单
sh1 = wb.get_sheet(1)

# 替换总成绩数据
sh1.write(1, 0, 362)

# 保存
wb.save('test.xls')

```

从上面代码可以看出，这里的修改 Excel 是通过 xlutils 库的 copy 方法将原来的 Excel 整个复制一份，然后再做修改操作，最后再保存。看下修改结果如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYVlpYUFVMk8xTWZnZ0pNcmlhZ3VhVEdpYnhLdjQ0Z2N2ZFhrR0hUcmU5REQzY09DdHF0Rno4aE0yUS82NDA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYVJyQnBxUDk4ZjZiM0NjZHRsR0hVRnRqZXVSUks3WndxZjBVQUlGeDNrb3FpYW9HdGR5TDY3YWcvNjQw?x-oss-process=image/format,png">

### 格式转换操作

在平时我们使用 Excel 时会对数据进行一下格式化，或者样式设置，在这里把上面介绍写入的代码简单修改下，使输出的格式稍微改变一下，代码如下：

```
# 导入 xlwt 库
import xlwt

# 设置写出格式字体红色加粗
styleBR = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')

# 设置数字型格式为小数点后保留两位
styleNum = xlwt.easyxf(num_format_str='#,##0.00')

# 设置日期型格式显示为YYYY-MM-DD
styleDate = xlwt.easyxf(num_format_str='YYYY-MM-DD')

# 创建 xls 文件对象
wb = xlwt.Workbook()

# 新增两个表单页
sh1 = wb.add_sheet('成绩')
sh2 = wb.add_sheet('汇总')

# 然后按照位置来添加数据,第一个参数是行，第二个参数是列
sh1.write(0, 0, '姓名', styleBR)   # 设置表头字体为红色加粗
sh1.write(0, 1, '日期', styleBR)   # 设置表头字体为红色加粗
sh1.write(0, 2, '成绩', styleBR)   # 设置表头字体为红色加粗

# 插入数据
sh1.write(1, 0, '张三',)
sh1.write(1, 1, '2020-07-01', styleDate)
sh1.write(1, 2, 90, styleNum)
sh1.write(2, 0, '李四')
sh1.write(2, 1, '2020-08-02')
sh1.write(2, 2, 95, styleNum)

# 设置单元格内容居中的格式
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
style = xlwt.XFStyle()
style.alignment = alignment

# 合并A4,B4单元格，并将内容设置为居中
sh1.write_merge(3, 3, 0, 1, '总分', style)

# 通过公式，计算C2+C3单元格的和
sh1.write(3, 2, xlwt.Formula("C2+C3"))

# 对 sheet2 写入数据
sh2.write(0, 0, '总分', styleBR)
sh2.write(1, 0, 185)

# 最后保存文件即可
wb.save('test.xls')

```

输出结果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYWFkMEdabzlLdElDOFVsRGdRUEdUWGRha3BYajN2dWZhVDNKdWxmTXFpYWZpYTNQZ0pLWWdqRUhnLzY0MA?x-oss-process=image/format,png">

可以看出，使用代码我们可以对字体，颜色、对齐、合并等平时 Excel 的操作进行设置，也可以格式化日期和数字类型的数据。当然了这里只是介绍了部分功能，不过这已经足够我们日常使用了，想了解更多功能操作可以参考官网。

>  
  python-excel官网：www.python-excel.org/ 
 

## Python 操作 Word

### 安装 python-docx

处理 Word 需要用到 `python-docx` 库，目前版本为 `0.8.10` ，执行如下安装命令：

```
$ pip install python-docx
################# 运行结果 ################
C:\Users\Y&gt;pip install python-docx
Looking in indexes: https://pypi.doubanio.com/simple
Collecting python-docx
  Downloading https://pypi.doubanio.com/packages/e4/83/c66a1934ed5ed8ab1dbb9931f1779079f8bca0f6bbc5793c06c4b5e7d671/python-docx-0.8.10.tar.gz (5.5MB)
     |████████████████████████████████| 5.5MB 3.2MB/s
Requirement already satisfied: lxml&gt;=2.3.2 in c:\users\y\appdata\local\programs\python\python37\lib\site-packages (from python-docx) (4.5.0)
Building wheels for collected packages: python-docx
  Building wheel for python-docx (setup.py) ... done
  Created wheel for python-docx: filename=python_docx-0.8.10-cp37-none-any.whl size=184496 sha256=7ac76d3eec848a255b4f197d07e7b78ab33598c814d536d9b3c90b5a3e2a57fb
  Stored in directory: C:\Users\Y\AppData\Local\pip\Cache\wheels\05\7d\71\bb534b75918095724d0342119154c3d0fc035cedfe2f6c9a6c
Successfully built python-docx
Installing collected packages: python-docx
Successfully installed python-docx-0.8.10
复制代码

```

OK，如果提示以上信息则安装成功。

### 写入 Word

平时我们在操作 Word 写文档的时候，一般分为几部分：`标题`、`章节`、`段落`、`图片`、`表格`、`引用`以及`项目符号编号`等。下面我们就按这几部分如何用 Python 操作来一一介绍。

#### 标题

文档标题创建比较简单，通过 `Document()` 创建出一个空白文档，只要调用 `add_heading` 方法就能创建标题。

```
# 导入库
from docx import Document
from docx.shared import Pt
from docx.shared import Inches
from docx.oxml.ns import qn

# 新建空白文档
doc1 = Document()

# 新增文档标题
doc1.add_heading('如何使用 Python 创建和操作 Word',0)

# 保存文件
doc1.save('word1.docx')

```

这样就完成了创建文档和文章标题的操作，下面运行程序，会生成名为 word1.docx 的文档，打开文章显示如下图所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYWhRMHM4QzdGREpzaWE1eEtKaFhlaWNDZ3RWM1JFMEtJQW5yRzFCQUhESHRtT1pwQVduRFRTZlBBLzY0MA?x-oss-process=image/format,png">

#### 章节与段落

有了文章标题，下面我们来看章节和段落是怎么操作的，在上面代码后面增加章节和段落操作的代码如下：

```
# 导入库
from docx import Document
from docx.shared import Pt
from docx.shared import Inches
from docx.oxml.ns import qn

# 新建空白文档
doc1 = Document()

# 新增文档标题
doc1.add_heading('如何使用 Python 创建和操作 Word',0)

# 创建段落描述
doc1.add_paragraph(' Word 文档在我们现在的生活和工作中都用的比较多，我们平时都使用 wps 或者 office 来对 Word 进行处理，可能没想过它可以用 Python 生成，下面我们就介绍具体如何操作……')

# 创建一级标题
doc1.add_heading('安装 python-docx 库',1)

# 创建段落描述
doc1.add_paragraph('现在开始我们来介绍如何安装 python-docx 库，具体需要以下两步操作：')

# 创建二级标题
doc1.add_heading('第一步：安装 Python',2)

# 创建段落描述
doc1.add_paragraph('在python官网下载python安装包进行安装。')

# 创建三级标题
doc1.add_heading('第二步：安装 python-docx 库',3)

# 创建段落描述
doc1.add_paragraph('window下win+R输入CMD打开命令行，输入pip install python-docx即可下载。')

# 保存文件
doc1.save('word2.docx')

```

上面我们说了 add_heading 方法用来增加文章标题，不过通过上面代码我们能知道，这个方法的**第二个参数为数字**，其实这个就是用**来标示几级标题的**，在我们平时就用来标示章节。add_paragraph 方法则是用来在文章中增加段落的， 运行程序看下效果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYXZoVTZpYURpYUl0SHF4Q3VINmh6aWEyNkFCc3piVnZLcDcyR3lIU2FvRDM3bjdmVXd4NXFzUE1Idy82NDA?x-oss-process=image/format,png">

#### 字体和引用

前面我们通过 add_paragraph 方法增加了三个段落，现在我们就看下如何对段落中字体如何操作，以及引用段落的操作。继续修改以上代码，**增加对文章字体字号、加粗、倾斜等操作**，具体代码如下：

```
# 导入库
from docx import Document
from docx.shared import Pt
from docx.shared import Inches
from docx.oxml.ns import qn
from docx.shared import RGBColor

# 新建空白文档
doc1 = Document()

# 新增文档标题
doc1.add_heading('如何使用 Python 创建和操作 Word',0)

# 创建段落描述
doc1.add_paragraph(' Word 文档在我们现在的生活和工作中都用的比较多，我们平时都使用 wps 或者 office 来对 Word 进行处理，可能没想过它可以用 Python 生成，下面我们就介绍具体如何操作……')

# 创建一级标题
doc1.add_heading('安装 python-docx 库',1)

# 创建段落描述
doc1.add_paragraph('现在开始我们来介绍如何安装 python-docx 库，具体需要以下两步操作：')

# 创建二级标题
doc1.add_heading('第一步：安装 Python',2)

# 创建段落描述
doc1.add_paragraph('在python官网下载python安装包进行安装。')

# 创建三级标题
doc1.add_heading('第二步：安装 python-docx 库',3)

# 创建段落描述
doc1.add_paragraph('window下win+R输入CMD打开命令行，输入pip install python-docx即可下载。')

# 创建段落，添加文档内容
paragraph = doc1.add_paragraph('这是第二步的安装描述！')

# 段落中增加文字，并设置字体字号
run = paragraph.add_run('(注意：这里设置了字号为20)')
run.font.size = Pt(20)

# 设置英文字体
run = doc1.add_paragraph('这里设置英文字体：').add_run('This Font is Times New Roman ')
run.font.name = 'Times New Roman'

# 设置中文字体
run = doc1.add_paragraph('这里设置中文字体：').add_run('当前字体为黑体')
run.font.name='黑体'
r = run._element
r.rPr.rFonts.set(qn('w:eastAsia'), '黑体')

# 设置斜体
run = doc1.add_paragraph('这段设置：').add_run('文字的是斜体 ')
run.italic = True

# 设置粗体
run = doc1.add_paragraph('这段再设置：').add_run('这里设置粗体').bold = True

# 设置字体带下划线
run = doc1.add_paragraph('这段为下划线：').add_run('这里设置带下划线').underline = True

# 设置字体颜色
run = doc1.add_paragraph('这段字体为红色：').add_run('这里设置字体为红色')
run.font.color.rgb = RGBColor(0xFF, 0x00, 0x00)

# 增加引用
doc1.add_paragraph('这里是我们引用的一段话：用Python改变人生，改变世界，FIGHTING。', style='Intense Quote')

# 保存文件
doc1.save('word2.docx')

```

上面代码主要是针对段落字体的各种设置，每段代码都标有注释应该比较容易理解， 运行程序看下效果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYVZvbm5zOGQwd2lhcnp0VUZpYmRhVk5XNGFUWWs3OVYwaExkaWJsM0J6Q1M4VDVkT25BN0U0MVJ0QS82NDA?x-oss-process=image/format,png">

#### 项目列表

我们平时在使用 Word 时，为了能展示更清晰，会用到项目符号和编号，将内容通过列表的方式展示出来，下面我们新建一个文件 word1.py 并编写如下代码：

```
# 导入库
from docx import Document
from docx.shared import Pt
from docx.shared import Inches
from docx.oxml.ns import qn

# 新建文档
doc2 = Document()

doc2.add_paragraph('哪个不是动物：')

# 增加无序列表
doc2.add_paragraph(
    '苹果', style='List Bullet'
)
doc2.add_paragraph(
    '喜洋洋', style='List Bullet'
)
doc2.add_paragraph(
    '懒洋洋', style='List Bullet'
)
doc2.add_paragraph(
    '沸洋洋', style='List Bullet'
)
doc2.add_paragraph(
    '灰太狼', style='List Bullet'
)

doc2.add_paragraph('2020年度计划：')
# 增加有序列表
doc2.add_paragraph(
    'CSDN达到博客专家', style='List Number'
)
doc2.add_paragraph(
    '每周健身三天', style='List Number'
)

doc2.add_paragraph(
    '每天学习一个新知识点', style='List Number'
)
doc2.add_paragraph(
    '学习50本书', style='List Number'
)
doc2.add_paragraph(
    '减少加班时间', style='List Number'
)

# 保存文件
doc2.save('word1.docx')

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYUwyVkxSbU9DQnpHVG9VSkE3Y004RURYUThpYWlhTVZUV0l1N2RDaWFTQUs4aEEyVlVPeVV6VHhHUS82NDA?x-oss-process=image/format,png">

#### 图片和表格

我们平时编辑文章时，插入图片和表格也是经常使用到的，那用 Python 该如何操作插入图片和表格？首先我们随便找了个图片，我这用了 Python的logo 标志图，文件名为 python-logo.png，利用`add_picture`添加图片；利用`add_table`添加表格，然后在 word1.py 文件中增加如下代码：

```
# 导入库
from docx import Document
from docx.shared import Pt
from docx.shared import Inches
from docx.oxml.ns import qn

# 新建文档
doc2 = Document()

doc2.add_paragraph('哪个不是动物：')

# 增加无序列表
doc2.add_paragraph(
    '苹果', style='List Bullet'
)
doc2.add_paragraph(
    '喜洋洋', style='List Bullet'
)
doc2.add_paragraph(
    '懒洋洋', style='List Bullet'
)
doc2.add_paragraph(
    '沸洋洋', style='List Bullet'
)
doc2.add_paragraph(
    '灰太狼', style='List Bullet'
)

doc2.add_paragraph('2020年度计划：')
# 增加有序列表
doc2.add_paragraph(
    'CSDN达到博客专家', style='List Number'
)
doc2.add_paragraph(
    '每周健身三天', style='List Number'
)

doc2.add_paragraph(
    '每天学习一个新知识点', style='List Number'
)
doc2.add_paragraph(
    '学习50本书', style='List Number'
)
doc2.add_paragraph(
    '减少加班时间', style='List Number'
)

doc2.add_heading('图片',2)

# 增加图像
doc2.add_picture('C:/Users/Y/Pictures/python-logo.png', width=Inches(5.5))

doc2.add_heading('表格',2)

# 增加表格，这是表格头
table = doc2.add_table(rows=1, cols=4)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = '编号'
hdr_cells[1].text = '姓名'
hdr_cells[2].text = '职业'

# 这是表格数据
records = (
    (1, '张三', '电工'),
    (2, '张五', '老板'),
    (3, '马六', 'IT'),
    (4, '李四', '工程师')
)

# 遍历数据并展示
for id, name, work in records:
    row_cells = table.add_row().cells
    row_cells[0].text = str(id)
    row_cells[1].text = name
    row_cells[2].text = work

# 手动增加分页
doc2.add_page_break()

# 保存文件
doc2.save('word1.docx')

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYVVxaWJpY2liWlVyYnFtNmFXak5zYVk5ZlRHQ0diYklic0hWY1dWMGg2bnBPZVJpY2pXaWNpYlFPQ3dRUS82NDA?x-oss-process=image/format,png">

### 读取 Word 文件

上面写了很多用 Python 创建空白 Word 文件格式化字体并保存到文件中，接下来我们再简单介绍下如何读取已有的 Word 文件，请看如下代码：

```
# 引入库
from docx import Document

# 打开文档1
doc1 = Document('word1.docx')

# 读取每段内容
pl = [ paragraph.text for paragraph in doc1.paragraphs]

print('###### 输出word1文章的内容 ######')
# 输出读取到的内容
for i in pl:
    print(i)

# 打开文档2
doc2 = Document('word2.docx')

print('\n###### 输出word2文章内容 ######')

pl2 = [ paragraph.text for paragraph in doc2.paragraphs]

# 输出读取到的内容
for j in pl2:
    print(j)

# 读取表格材料，并输出结果
tables = [table for table in doc2.tables]
for table in tables:
    for row in table.rows:
        for cell in row.cells:
            print (cell.text,end='  ')
        print()
    print('\n')

```

以上代码是将之前我们输出的两个文档内容都读取出来，当然这里只是打印到控制台，并没有做其他处理。现在我们执行看下结果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYVBkRnFCNWd6a1Nac3V3NkdpYncxdVFvWjA3SlBhMXg0RXFoaWJ1UWVZZHNwdlpPZ2FTQW8zU2lidy82NDA?x-oss-process=image/format,png">

## Python 操作 CSV

### 简介

#### CSV

`CSV` 全称 `Comma-Separated Values`，中文叫逗号分隔值或字符分隔值，它**以纯文本形式存储表格数据（数字和文本）**，其本质就是一个**字符序列**，可以由任意数目的记录组成，记录之间以某种换行符分隔，每条记录由字段组成，通常所有记录具有完全相同的字段序列，字段间常用逗号或制表符进行分隔。CSV 文件格式简单、通用，在现实中有着广泛的应用，其中使用最多的是**在程序之间转移表格数据**。

#### CSV 与 Excel

因为 CSV 文件与 Excel 文件默认都是用 Excel 工具打开，那他们有什么区别呢？我们通过下表简单了解一下。



|CSV|Excel
|------
|文件后缀为 .csv|文件后缀为 .xls 或 .xlsx
|纯文本文件|二进制文件
|存储数据不包含格式、公式等|不仅可以存储数据，还可以对数据进行操作
|可以通过 Excel 工具打开，也可以通过文本编辑器打开|只能通过 Excel 工具打开
|只能编写一次列标题|每一行中的每一列都有一个开始标记和结束标记
|导入数据时消耗内存较少|数据时消耗内存较多



### 基本使用

Python 通过 **csv 模块**来实现 CSV 格式文件中数据的读写，该模块提供了兼容 Excel 方式输出、读取数据文件的功能，这样我们无需知道 Excel 所采用 CSV 格式的细节，同样的它还可以定义其他应用程序可用的或特定需求的 CSV 格式。

csv 模块中使用 `reader 类`和 `writer 类`读写序列化的数据，使用 `DictReader 类`和 `DictWriter 类`以字典的形式读写数据，下面来详细看一下相应功能。首先来看一下 csv 模块常量信息，如下所示：



|属性|说明
|------
|QUOTE_ALL|指示 writer 对象给所有字段加上引号
|QUOTE_MINIMAL|指示 writer 对象仅为包含特殊字符（如：定界符、引号字符、行结束符等）的字段加上引号
|QUOTE_NONNUMERIC|指示 writer 对象为所有非数字字段加上引号
|QUOTE_NONE|指示 writer 对象不使用引号引出字段



#### writer(csvfile, dialect=’excel’, **fmtparams)

返回一个 `writer 对象`，该对象负责**将用户的数据在给定的文件类对象上转换为带分隔符的字符串**。
- `csvfile` 可以是具有 write() 方法的任何对象，如果 csvfile 是文件对象，则使用 newline=’’ 打开；- 可选参数 `dialec`t 是用于不同的 CSV 变种的特定参数组；- 可选关键字参数 `fmtparams` 可以覆写当前变种格式中的单个格式设置。
看下示例：

```
import csv

with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    # 写入多行
    data = [('1001', '张三', '21'), ('1002', '李四', '31')]
    writer.writerows(data)

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYWhpY0xXcTZTT1lDcFhSNm1OblhoQUZaRTFLbWZYTjJISDN5UktUZ2hVYWJuazNXSWtrd0p2ZFEvNjQw?x-oss-process=image/format,png">

reader(csvfile, dialect=’excel’, **fmtparams)

返回一个 `reader 对象`，该对象将逐行遍历 csvfile，csvfile 可以是文件对象和列表对象，如果是文件对象要使用 newline=’’ 打开。看下示例：

```
import csv

with open('test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        print(', '.join(row))

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQmtXcnduSnNPaWNpY3JOeGpjMElRMFBpYXBCY295SnFzVThrenFweTJ6V3VMUXE1RDNLWU9KVFRlN2IxU1doUTNQdklPYWNZSzRmdmdaZy82NDA?x-oss-process=image/format,png">

#### Sniffer 类

用于**推断 CSV 文件的格式**，该类提供了如下两个方法：

##### sniff(sample, delimiters=None)

分析给定的 sample，如果给出可选的 delimiters 参数，则该参数会被解释为字符串，该字符串包含了可能的有效定界符。

##### has_header(sample)

分析示例文本（假定为 CSV 格式），如果第一行很可能是一系列列标题，则返回 True。

该类及方法使用较少，了解即可，下面通过一个示例简单了解一下。

```
import csv

with open('test.csv', newline='') as csvfile:
     dialect = csv.Sniffer().sniff(csvfile.read(1024))
     csvfile.seek(0)
     reader = csv.reader(csvfile, dialect)
     for row in reader:
         print(row)

```

#### Reader 对象

Reader 对象指 DictReader 实例和 reader() 函数返回的对象，下面看一下其公开属性和方法。

##### next()

返回 reader 的可迭代对象的下一行，返回值可能是列表或字典。

##### dialect

dialect 描述，只读，供解析器使用。

##### line_num

源迭代器已经读取了的行数。

##### fieldnames

字段名称，该属性为 DictReader 对象属性。

#### Writer 对象

Writer 对象指 DictWriter 实例和 writer() 函数返回的对象，下面看一下其公开属性和方法。

##### writerow(row)

将参数 row 写入 writer 的文件对象。

##### writerows(rows)

将 rows_（即能迭代出多个上述_ row 对象的迭代器）中的所有元素写入 writer 的文件对象。

##### writeheader()

在 writer 的文件对象中，写入一行字段名称，该方法为 DictWriter 对象方法。

##### dialect

dialect 描述，只读，供 writer 使用。

#### 写读追加状态

```
'r'：读
'w'：写
'a'：追加
'r+' == r+w（可读可写，文件若不存在就报错(IOError)）
'w+' == w+r（可读可写，文件若不存在就创建）
'a+' ==a+r（可追加可写，文件若不存在就创建）
对应的，如果是二进制文件，就都加一个b就好啦：
'rb'  'wb'  'ab'  'rb+'  'wb+'  'ab+
```

```
PS：如果觉得分享内容有一些帮助，欢迎大家随手分享、点赞、在看。
&lt; END &gt;


```
