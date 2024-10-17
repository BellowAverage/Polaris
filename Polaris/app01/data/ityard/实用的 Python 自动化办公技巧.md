
--- 
title:  实用的 Python 自动化办公技巧 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/0141f7e5efed3bdc48cc37e30cb086ae.png">

>  
  平时在公司做数据分析的时候, 也会用python做些办公自动化的工作, 领导昨天说别人3个小时的活我们已经可以3分钟完成了 。O(∩_∩)O~ 
 

本文就给大家介绍几个我用到的办公室自动化技巧：

### 1、Word文档doc转docx

去年想参赛一个数据比赛, 里面的数据都是doc格式, 想用python-docx 读取word文件中的数据, 但是python-docx只支持docx格式, 所以研究了这两种格式的转换。

1.1 导入工具包

```
import os
from win32com import client as wc

```

1.2 获取文件夹下面所有doc文件明细

```
# 路径
path="C:/Users/yyz/Desktop/python办公技巧/data/doc转docx/"   # 根据自己电脑文件修改


# 定义空list,存放文件绝对路径
files = []
for file in os.listdir(path):
    if file.endswith(".doc"):
        files.append(path+file)
files

```

<img src="https://img-blog.csdnimg.cn/img_convert/ede676a1f63317465403b893bcf1da3d.png">1.3 转换文件

```
# 运行word程序
word = wc.Dispatch("Word.Application")
# for循环
i = 0
for file in files:
    try:
        doc = word.Documents.Open(file)    #打开word文件
        doc.SaveAs("{}x".format(file), 12)   #另存为后缀为".docx"的文件，其中参数12指docx文件
        doc.Close()  #关闭原来word文件
        print(file +':转换成功')
        i +=1
    except:
        print(file +':转换[不成功]')   
        files.append(file)  # 若读取文件报错, 则将文件名称添加到files列表中重新读取
        pass
print('转换文件%i个'%i)    
# 退出word    
word.Quit()

```

### 

### 2、文字地址批量转经纬度

工作中地址转经纬度会用在做地图可视化或者计算距离方面。

2.1 导入工具包

```
# 导入工具包
import pandas as pd
import json
from urllib.request import urlopen, quote
import requests

```

2.2 定义转换函数

```
# 定义函数
def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoding/v3/'
    output = 'json'
    ak = "自己申请的api"   # 百度地图API, 需要自己申请
    address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + address  + '&amp;output=' + output + '&amp;ak=' + ak  +'&amp;callback=showLocation%20'+'//GET%E8%AF%B7%E6%B1%82'
    res=requests.get(uri).text
    temp = json.loads(res) # 将字符串转化为json
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']
    return lng, lat   # 经度 longitude,纬度 latitude,

```

2.3 地址转换2.3.1 单个地址转换

```
# 单个地址转换
getlnglat('北京市朝阳区高碑店地区办事处高井村委会')
(116.52784003604923, 39.91806508560947)

```

2.3.2 批量地址转换

```
# 读取数据
data = pd.read_excel('C:/Users/yyz/Desktop/python办公技巧/data/地址信息.xlsx')
data

```

<img src="https://img-blog.csdnimg.cn/img_convert/90191b1631f17240d29ebaf1e5429b28.png">

```
data['经度'] = ''
data['纬度'] = ''
for i in range(data.shape[0]):
    try:
        data.iloc[i,2] = getlnglat(data.iloc[i,1])[0] # 经度 将第i行,第2列的地址(列索引为1)转换为经纬度,并将经度赋值给第i行,第3列(列索引为2)
        data.iloc[i,3] = getlnglat(data.iloc[i,1])[1] # 纬度
    except:
        pass
    #print(i)
data

```

<img src="https://img-blog.csdnimg.cn/img_convert/c433f51f869986c0c340d0b22c227616.png">

### 3、经纬度计算距离

安装工具包

```
pip install geopy

```

3.1 导入工具包

```
from geopy.distance import geodesic

```

3.2 读取数据

```
# 读取数据
data = pd.read_excel('C:/Users/yyz/Desktop/python办公技巧/data/经纬度计算距离.xlsx')
data

```

<img src="https://img-blog.csdnimg.cn/img_convert/436c30c5177c6f2bb50b9c004eedc35d.png">3.3 计算距离

```
# 将经纬度赋值给变量,简化
wd1 = data['纬度1'].tolist()
jd1 = data['经度1'].tolist()
wd2 = data['纬度2'].tolist()
jd2 = data['经度2'].tolist()


lis1 = []
for i in range(len(data)):
    j= geodesic((wd1[i],jd1[i]), (wd2[i],jd2[i])).km   # 纬度 经度  纬度 经度
    lis1.append(j)
    #print(i)


data['距离'] = lis1
data

```

### 

### 4、百度经纬度转高德经纬度

公司有2个系统,用的坐标系不一样, 有时候需要转换一下

4.1 工具包

```
# 导入工具包
import math
import pandas as pd

```

4.2 定义函数

```
# 定义转换函数
def bdToGaoDe(lon,lat):
    PI = 3.14159265358979324 * 3000.0 / 180.0
    x = lon - 0.0065
    y = lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * PI)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * PI)
    lon = z * math.cos(theta)
    lat = z * math.sin(theta)
    return lon,lat

```

4.3 单个转换

```
# 单个转换
bdToGaoDe(116.512885, 39.847469)
(116.50647396357492, 39.84120409781157)

```

4.4 批量转换

```
# 读取数据
data = pd.read_excel('C:/Users/yyz/Desktop/python办公技巧/data/百度经纬度转高德.xlsx')
data.head()

```

<img src="https://img-blog.csdnimg.cn/img_convert/9363382a4984caed061810d2b8f7ac0f.png">

```
wd = data['纬度'].tolist()
jd = data['经度'].tolist()
# 定义一个空列表
li1 = []
for i in range(len(data)):
    j  = bdToGaoDe(jd[i],wd[i])
    li1.append(j)
    
li1
data['经度_re'] = [i[0] for i in li1]
data['纬度_re'] = [i[1] for i in li1]
data.head()

```

<img src="https://img-blog.csdnimg.cn/img_convert/55ca179b2b7521c02adb6e1b2824dade.png">

### 5、Excel文件批量合并

5.1 工具包

```
# 导入工具包
import pandas as pd
import os

```

5.2 获取文件列表

```
# 设置文件路径
path = 'C:/Users/yyz/Desktop/python办公技巧/data/数据合并/'
# 空列表, 用于存放文件路径
files = []
for file in os.listdir(path):
    if file.endswith(".xlsx"):
        files.append(path+file)


# 查看列表
files

```

5.3 转换存储数据

```
# 定义一个空的dataframe
data = pd.DataFrame()  


# 遍历所有文件
for file in files:
    datai = pd.read_excel(file)
    datai_len = len(datai)
    data = data.append(datai)   # 添加到总的数据中
    print('读取%i行数据,合并后文件%i列, 名称：%s'%(datai_len,len(data.columns),file.split('/')[-1]))     
    # 查看是否全部读取，格式是否出错
# 重置索引    
data.reset_index(drop=True,inplace=True)

```

### 

### 6、Word文件批量转pdf

只能转docx文件,转doc文件会报错, 工具包安装

```
pip install docx2pdf

```

6.1 导入工具包

```
# 安装工具包:
#　导入工具包
from docx2pdf import convert
import os

```

6.2 单个转换

```
# 单个转换
convert("c:/users/yyz/desktop/魔方公式.docx", "c:/users/yyz/desktop/excel笔记.pdf")

```

6.3 批量转换

```
# 文件位置
path = 'C:/Users/yyz/Desktop/python办公技巧/data/word转pdf/'
# 定义空list,存放文件列表
files = []
for file in os.listdir(path):
    if file.endswith(".docx"):
        files.append(path+file)
files
for file in files:
   convert(file,file.split('.')[0]+'.pdf')
   print(file+'转换成功')

```

### 

### 7、批量读取word中表格数据

工具包安装

```
pip install python-docx

```

```
# 读取word文件
doc = docx.Document('C:/Users/yyz/Desktop/python办公技巧/data/word信息.docx')
# 获取文档中所有表格对象的列表
biaoges = doc.tables 

```

<img src="https://img-blog.csdnimg.cn/img_convert/b9bfd011d688c2f39d188b69be9c27ae.png">

7.2 不规范的表格

```
cells = biaoges[1]._cells
cells_lis = [[cell.text for cell in cells]]

```

<img src="https://img-blog.csdnimg.cn/img_convert/f1dc0385a58aa2ed57130dd0f3060606.png">

```
import pandas as pd
import numpy as np
datai = pd.DataFrame(cells_lis)
datai = datai[[1,3,7,9,14,16,19,21]]
datai.columns = ['姓名','年龄','籍贯','住址','工作单位','电话','是否党员','出生日期']
datai

```

<img src="https://img-blog.csdnimg.cn/img_convert/3498e20ae6e9d3f2f45f1e9382164549.png">7.3 规范数据

```
# 获取第1个表格行丨
rowi = len(biaoges[0].rows)
rowi

```

```
# 定义空列表
lis1 = []
# for循环获取第一个表的数据
for i in range(1,rowi):  # 从第2行开始循环
    lis1.append([biaoges[0].cell(i,0).text,
                 biaoges[0].cell(i,1).text,
                 biaoges[0].cell(i,2).text,
                 biaoges[0].cell(i,3).text,
                 biaoges[0].cell(i,4).text])

```

```
# 创建一个dataframe
data1 = pd.DataFrame(lis1,columns=['日期','品类','数量','价格','金额'])
data1

```

<img src="https://img-blog.csdnimg.cn/img_convert/c0ee28b13c60f72a07ab3557b5cf08ca.png">

7.4 批量读取

```
import pandas as pd
import os
os.chdir('C:/Users/yyz/Desktop/python办公技巧/data/word信息/')

```

```
lis1=[]
for file in os.listdir('.'):
    if file.endswith('.docx'):
        doc = docx.Document('./'+file)
        biaoges = doc.tables
        rowi = len(biaoges[0].rows)
        for i in range(1,rowi):
            lis1.append([biaoges[0].cell(i,0).text,
                     biaoges[0].cell(i,1).text,
                     biaoges[0].cell(i,2).text,
                     biaoges[0].cell(i,3).text,
                     biaoges[0].cell(i,4).text])

```

```
# 创建dataframe            
data1 = pd.DataFrame(lis1,columns=['日期','品类','数量','价格','金额'])
data1

```

<img src="https://img-blog.csdnimg.cn/img_convert/2924fa8b812d78ef740cb35a6157c1ca.png">

### 8 用outlook批量发邮件

8.1 导入工具包

```
import win32com.client as win32
import pandas as pd

```

8.2 读取数据

```
# 读取数据
data1 = pd.read_excel('C:/Users/yyz/Desktop/python批量发送邮件.xlsx',sheet_name='发送邮件')
data1.fillna('',inplace=True)

```

8.3 发送邮件

```
# 运行outlook
outlook = win32.Dispatch("outlook.Application")   
# for循环发送文件
for i in range(data1.shape[0]):   
    mail = outlook.CreateItem(0)   # 创建一个邮件对象  win32.constants.olMailItem
    mail.To = data1.iloc[i,0]      #收件人
    mail.CC = data1.iloc[i,1]      #抄送人
    mail.Subject = data1.iloc[i,2]    #邮件主题
    mail.HTMLBody = data1.iloc[i,3]           # 邮件正文 html格式
   # mail.Body = data1.iloc[i,3]              # 邮件正文
    mail.Attachments.Add(data1.iloc[i,4])     # 附件
    mail.Send() #发送
    i +=1
print('发送邮件%i份'%i)

```

python办公自动化的技巧还有很多, python好掌握，能帮助我们提升工作效率，这也是很多非编程人员学习python的原因之一。

>  
  版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。  
  本文链接： 
  blog.csdn.net/muyashui/article/details/116306877 
 

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/2b6438a8261f7652306189d441d34b3f.gif">

微信扫码关注，了解更多内容
