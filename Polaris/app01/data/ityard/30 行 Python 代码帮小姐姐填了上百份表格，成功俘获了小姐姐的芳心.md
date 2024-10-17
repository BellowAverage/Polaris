
--- 
title:  30 行 Python 代码帮小姐姐填了上百份表格，成功俘获了小姐姐的芳心 
tags: []
categories: [] 

---
<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6L0k0Z1luS1FnVjFWb2NaV3hGdE9VU0RPTVMyQjRVQnl2RzUzUzVQRVFNNnROQVA1WUhhSVJqcjgycVVGd2ZSUVR2bVZ3cWtHc2ljamRTOGhQVDFNVnhQdy82NDA?x-oss-process=image/format,png">

事情是这样的，昨天下班的时候，偶然发现秘书小姐姐情绪很不好，本着乐于助人的原则，我主动凑上前去献温暖

经过小姐姐的一番诉苦，原来是这样，马上要下班了，老板却突然发来一个表格，内容如下图：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9JNGdZbktRZ1YxVlhkU1AzeWhFVTk4VlAwRmliRUluekx3WTI4bVV1aWJLdXcxTWNVRUVmT2pUd1JzT1F0eGp0QnBoWHdqcGdOSmc1RGE5WFlINmNCeExnLzY0MA?x-oss-process=image/format,png">

大概有300名左右的人员信息，老板要求小姐姐将这些信息按照如下模板进行填写，每人1张表，今天弄完：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9JNGdZbktRZ1YxVlhkU1AzeWhFVTk4VlAwRmliRUluekxKUHRaMDhQQkRaQWZvdDkwSnZoZTZmTXlWTG04OW5tOGFnaWFuZXZoa2F1OTRpYU5nNWJ1R01LQS82NDA?x-oss-process=image/format,png">

就算1张表格半分钟，300张表格搞完也要2个半小时

咱怎么能让小姐姐受这罪呢，于是很豪爽的把这件事揽下来了，当时小姐姐看我的眼神都不一样了

最后我用30行python代码，然后花了5分钟把这些表格自动填好了，具体内容如下：

#### **1.用xlwings打开工作簿**

```
import xlwings as xw
app=xw.App(visible=True,add_book=False)
workbook=app.books.open(r'D:\数据分析\27.我用python帮小姐姐填了上百份表格\人员信息.xlsx')
sheet=workbook.sheets[0]  #选中第一个表格

```

#### **2.循环每行的数据**

```
info = sheet.used_range
for i in info.raw_value[1:]:
    print(i)

```

```
('张三', '男', 28.0, 177.0, 150.0, '本科', '否', '汉族', '北京', 8.0)
('李四', '男', 31.0, 165.0, 130.0, '本科', '是', '汉族', '上海', 5.0)
('王二', '男', 40.0, 182.0, 162.0, '研究生', '是', '汉族', '广东广州', 2.0)
('李洁', '女', 25.0, 163.0, 110.0, '研究生', '否', '汉族', '广东深圳', 8.0)
('张茹', '女', 36.0, 168.0, 120.0, '研究生', '是', '汉族', '江苏南京', 4.0)
('张五', '男', 35.0, 165.0, 120.0, '本科', '否', '汉族', '河南郑州', 2.0)
('李杰', '男', 36.0, 163.0, 142.0, '本科', '是', '汉族', '河北石家庄', 1.0)
('王帅', '男', 37.0, 161.0, 94.4, '研究生', '是', '汉族', '辽宁沈阳', 6.0)
('李一', '女', 38.0, 159.0, 86.4, '研究生', '否', '汉族', '山东济南', 5.0)
('张霞', '女', 39.0, 157.0, 78.4, '研究生', '是', '汉族', '湖南长沙', 4.0)
('王万利', '男', 40.0, 155.0, 70.4, '本科', '否', '汉族', '黑龙江哈尔滨', 1.0)
('李庆', '男', 41.0, 153.0, 62.4, '本科', '是', '汉族', '吉林长春', 6.0)
('王厚', '男', 42.0, 151.0, 54.4, '研究生', '是', '汉族', '湖北武汉', 5.0)
('曾梅', '女', 43.0, 149.0, 46.4, '研究生', '否', '汉族', '海南海口', 7.0)
```

我们可以发现，数据以元组方式输出，下一步利用就很方便了

#### **3.打开个人信息模板，将信息填入**

```
for i in info.raw_value[1:]:
    app=xw.App(visible=True,add_book=False)
    workbook=app.books.open(r'D:\数据分析\27.我用python帮小姐姐填了上百份表格\个人信息模板.xlsx')
    sheet=workbook.sheets[0]
    sheet['B1'].value=i[0]
    sheet['D1'].value=i[1]
    sheet['F1'].value=i[8]
    sheet['H1'].value=i[2]
    sheet['B2'].value=i[9]
    sheet['D2'].value=i[5]
    sheet['F2'].value=i[6]
    sheet['H2'].value=i[7]

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9JNGdZbktRZ1YxVlhkU1AzeWhFVTk4VlAwRmliRUluekxZZDFDUXBIWmpFTHAxWTRzNlhZaHpwWjdEMVBhUE5DNThjQWVYT3ZtdkJaRE1UaGljTndJNHdnLzY0MA?x-oss-process=image/format,png">

这一步也很好理解，就是把元组中的个人信息提取出来，放入个人信息模板相应单元格位置中，但是格式不太好看，需要完善一下

#### **4.设置单元格格式**

```
list_cell=['B1','D1','F1','H1','B2','D2','F2','H2']#单元格位置
for j in list_cell:
        sheet[j].api.Font.Name='楷体'   #设置字体
        sheet[j].api.Font.Size=14      #设置字号
        #设置文本水平对齐方式为居中
        sheet[j].expand('table').api.HorizontalAlignment=xw.constants.HAlign.xlHAlignCenter
        #设置文本水平对齐方式为居中
        sheet[j].expand('table').api.VerticalAlignment=xw.constants.VAlign.xlVAlignCenter

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9JNGdZbktRZ1YxVlhkU1AzeWhFVTk4VlAwRmliRUluekx6MlNUTzR5bDFjaGF4eXVrTWp0VWNzU0hkZGVNVjdNVFBCT1U0aWIwM2liZFFWMjRHamU1b1N3QS82NDA?x-oss-process=image/format,png">

分别设置字体、字号和单元格上下左右居中

#### **5.将表格另存重命名并关闭**

```
workbook.save(r'D:\数据分析\27.我用python帮小姐姐填了上百份表格\{}.xlsx'.format(i[0]))  #以名字命名
workbook.close()
app.quit()
```

```
大功告成，看一下效果：

源码在公号后台回复填表获取


```

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcGFPWnF1SzE4eGM0V2JIT05pYmVoZU9HTXNJMUdIR0Z1UmpycUxpY2lhNld1aWNxaWNNWTZuY2t2Y21pYUZaWUcxWnM4Zjd5bnBwRTJaR2JFQS82NDA?x-oss-process=image/format,png">

分享或在看是对我最大的支持
