
--- 
title:  熬夜整理了90个Pandas案例 
tags: []
categories: [] 

---
文章很长，建议收藏。
<li> 如何使用列表和字典创建 Series 
   <ul>-  使用列表创建 Series -  使用 name 参数创建 Series -  使用简写的列表创建 Series -  使用字典创建 Series 
如何使用 Numpy 函数创建 Series

如何获取 Series 的索引和值

如何在创建 Series 时指定索引

如何获取 Series 的大小和形状

如何获取 Series 开始或末尾几行数据
-  Head() -  Tail() -  Take() 
使用切片获取 Series 子集

如何创建 DataFrame

如何设置 DataFrame 的索引和列信息

如何重命名 DataFrame 的列名称

如何根据 Pandas 列中的值从 DataFrame 中选择或过滤行

在 DataFrame 中使用“isin”过滤多行

迭代 DataFrame 的行和列

如何通过名称或索引删除 DataFrame 的列

向 DataFrame 中新增列

如何从 DataFrame 中获取列标题列表

如何随机生成 DataFrame

如何选择 DataFrame 的多个列

如何将字典转换为 DataFrame

使用 ioc 进行切片

检查 DataFrame 中是否是空的

在创建 DataFrame 时指定索引和列名称

使用 iloc 进行切片

iloc 和 loc 的区别

使用时间索引创建空 DataFrame

如何改变 DataFrame 列的排序

检查 DataFrame 列的数据类型

更改 DataFrame 指定列的数据类型

如何将列的数据类型转换为 DateTime 类型

将 DataFrame 列从 floats 转为 ints

如何把 dates 列转换为 DateTime 类型

两个 DataFrame 相加

在 DataFrame 末尾添加额外的行

为指定索引添加新行

如何使用 for 循环添加行

在 DataFrame 顶部添加一行

如何向 DataFrame 中动态添加行

在任意位置插入行

使用时间戳索引向 DataFrame 中添加行

为不同的行填充缺失值

append, concat 和 combine_first 示例

获取行和列的平均值

计算行和列的总和

连接两列

过滤包含某字符串的行

过滤索引中包含某字符串的行

使用 AND 运算符过滤包含特定字符串值的行

查找包含某字符串的所有行

如果行中的值包含字符串，则创建与字符串相等的另一列

计算 pandas group 中每组的行数

检查字符串是否在 DataFrme 中

从 DataFrame 列中获取唯一行值

计算 DataFrame 列的不同值

删除具有重复索引的行

删除某些列具有重复值的行

从 DataFrame 单元格中获取值

使用 DataFrame 中的条件索引获取单元格上的标量值

设置 DataFrame 的特定单元格值

从 DataFrame 行获取单元格值

用字典替换 DataFrame 列中的值

统计基于某一列的一列的数值

处理 DataFrame 中的缺失值

删除包含任何缺失数据的行

删除 DataFrame 中缺失数据的列

按降序对索引值进行排序

按降序对列进行排序

使用 rank 方法查找 DataFrame 中元素的排名

在多列上设置索引

确定 DataFrame 的周期索引和列

导入 CSV 指定特定索引

将 DataFrame 写入 csv

使用 Pandas 读取 csv 文件的特定列

Pandas 获取 CSV 列的列表

找到列值最大的行

使用查询方法进行复杂条件选择

检查 Pandas 中是否存在列

为特定列从 DataFrame 中查找 n-smallest 和 n-largest 值

从 DataFrame 中查找所有列的最小值和最大值

在 DataFrame 中找到最小值和最大值所在的索引位置

计算 DataFrame Columns 的累积乘积和累积总和

汇总统计

查找 DataFrame 的均值、中值和众数

测量 DataFrame 列的方差和标准偏差

计算 DataFrame 列之间的协方差

计算 Pandas 中两个 DataFrame 对象之间的相关性

计算 DataFrame 列的每个单元格的百分比变化

在 Pandas 中向前和向后填充 DataFrame 列的缺失值

在 Pandas 中使用非分层索引使用 Stacking

使用分层索引对 Pandas 进行拆分

Pandas 获取 HTML 页面上 table 数据

### 1如何使用列表和字典创建 Series

#### 使用列表创建 Series

```
import pandas as pd
 
ser1 = pd.Series([1.5, 2.5, 3, 4.5, 5.0, 6])
print(ser1)
```

Output:

```
0    1.5
1    2.5
2    3.0
3    4.5
4    5.0
5    6.0
dtype: float64
```

#### 使用 name 参数创建 Series

```
import pandas as pd
 
ser2 = pd.Series(["India", "Canada", "Germany"], name="Countries")
print(ser2)
```

Output:

```
0      India
1     Canada
2    Germany
Name: Countries, dtype: object
```

#### 使用简写的列表创建 Series

```
import pandas as pd
 
ser3 = pd.Series(["A"]*4)
print(ser3)
```

Output:

```
0    A
1    A
2    A
3    A
dtype: object
```

#### 使用字典创建 Series

```
import pandas as pd
 
ser4 = pd.Series({"India": "New Delhi",
                  "Japan": "Tokyo",
                  "UK": "London"})
print(ser4)
```

Output:

```
India    New Delhi
Japan        Tokyo
UK          London
dtype: object
```

### 2如何使用 Numpy 函数创建 Series

```
import pandas as pd
import numpy as np
 
ser1 = pd.Series(np.linspace(1, 10, 5))
print(ser1)
 
ser2 = pd.Series(np.random.normal(size=5))
print(ser2)
```

Output:

```
0     1.00
1     3.25
2     5.50
3     7.75
4    10.00
dtype: float64
0   -1.694452
1   -1.570006
2    1.713794
3    0.338292
4    0.803511
dtype: float64
```

### 3如何获取 Series 的索引和值

```
import pandas as pd
import numpy as np
 
ser1 = pd.Series({"India": "New Delhi",
                  "Japan": "Tokyo",
                  "UK": "London"})
 
print(ser1.values)
print(ser1.index)
 
print("\n")
 
ser2 = pd.Series(np.random.normal(size=5))
print(ser2.index)
print(ser2.values)
```

Output:

```
['New Delhi' 'Tokyo' 'London']
Index(['India', 'Japan', 'UK'], dtype='object')
 
 
RangeIndex(start=0, stop=5, step=1)
[ 0.66265478 -0.72222211  0.3608642   1.40955436  1.3096732 ]
```

### 4如何在创建 Series 时指定索引

```
import pandas as pd
 
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
 
code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]
 
ser1 = pd.Series(values, index=code)
 
print(ser1)
```

Output:

```
IND        India
CAN       Canada
AUS    Australia
JAP        Japan
GER      Germany
FRA       France
dtype: object
```

### 5如何获取 Series 的大小和形状

```
import pandas as pd
 
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
 
code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]
 
ser1 = pd.Series(values, index=code)
 
print(len(ser1))
 
print(ser1.shape)
 
print(ser1.size)
```

Output:

```
6
(6,)
6
```

### 6如何获取 Series 开始或末尾几行数据

#### Head()

```
import pandas as pd
 
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
 
code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]
 
ser1 = pd.Series(values, index=code)
 
print("-----Head()-----")
print(ser1.head())
 
print("\n\n-----Head(2)-----")
print(ser1.head(2))
```

Output:

```
-----Head()-----
IND        India
CAN       Canada
AUS    Australia
JAP        Japan
GER      Germany
dtype: object
 
 
-----Head(2)-----
IND     India
CAN    Canada
dtype: object
```

#### Tail()

```
import pandas as pd
 
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
 
code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]
 
ser1 = pd.Series(values, index=code)
 
print("-----Tail()-----")
print(ser1.tail())
 
print("\n\n-----Tail(2)-----")
print(ser1.tail(2))
```

Output:

```
-----Tail()-----
CAN       Canada
AUS    Australia
JAP        Japan
GER      Germany
FRA       France
dtype: object
 
 
-----Tail(2)-----
GER    Germany
FRA     France
dtype: object
```

#### Take()

```
import pandas as pd
 
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
 
code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]
 
ser1 = pd.Series(values, index=code)
 
print("-----Take()-----")
print(ser1.take([2, 4, 5]))
```

Output:

```
-----Take()-----
AUS    Australia
GER      Germany
FRA       France
dtype: object
```

### 7使用切片获取 Series 子集

```
import pandas as pd
 
num = [000, 100, 200, 300, 400, 500, 600, 700, 800, 900]
 
idx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
 
series = pd.Series(num, index=idx)
 
print("\n [2:2] \n")
print(series[2:4])
 
print("\n [1:6:2] \n")
print(series[1:6:2])
 
print("\n [:6] \n")
print(series[:6])
 
print("\n [4:] \n")
print(series[4:])
 
print("\n [:4:2] \n")
print(series[:4:2])
 
print("\n [4::2] \n")
print(series[4::2])
 
print("\n [::-1] \n")
print(series[::-1])
```

Output

```
[2:2]
 
C    200
D    300
dtype: int64
 
 [1:6:2]
 
B    100
D    300
F    500
dtype: int64
 
 [:6]
 
A      0
B    100
C    200
D    300
E    400
F    500
dtype: int64
 
 [4:]
 
E    400
F    500
G    600
H    700
I    800
J    900
dtype: int64
 
 [:4:2]
 
A      0
C    200
dtype: int64
 
 [4::2]
 
E    400
G    600
I    800
dtype: int64
 
 [::-1]
 
J    900
I    800
H    700
G    600
F    500
E    400
D    300
C    200
B    100
A      0
dtype: int64
```

### 8如何创建 DataFrame

```
import pandas as pd

employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp00'],
    'Name': ['John Doe', 'William Spark'],
    'Occupation': ['Chemist', 'Statistician'],
    'Date Of Join': ['2018-01-25', '2018-01-26'],
    'Age': [23, 24]})

print(employees)
```

Output:

```
Age Date Of Join EmpCode           Name    Occupation
0   23   2018-01-25  Emp001       John Doe       Chemist
1   24   2018-01-26   Emp00  William Spark  Statistician
```

### 9如何设置 DataFrame 的索引和列信息

```
import pandas as pd
 
employees = pd.DataFrame(
    data={'Name': ['John Doe', 'William Spark'],
          'Occupation': ['Chemist', 'Statistician'],
          'Date Of Join': ['2018-01-25', '2018-01-26'],
          'Age': [23, 24]},
    index=['Emp001', 'Emp002'],
    columns=['Name', 'Occupation', 'Date Of Join', 'Age'])
 
print(employees)
```

Output

```
Name    Occupation Date Of Join  Age
Emp001       John Doe       Chemist   2018-01-25   23
Emp002  William Spark  Statistician   2018-01-26   24
```

### 10如何重命名 DataFrame 的列名称

```
import pandas as pd

employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp00'],
    'Name': ['John Doe', 'William Spark'],
    'Occupation': ['Chemist', 'Statistician'],
    'Date Of Join': ['2018-01-25', '2018-01-26'],
    'Age': [23, 24]})

employees.columns = ['EmpCode', 'EmpName', 'EmpOccupation', 'EmpDOJ', 'EmpAge']

print(employees)
```

Output:

```
EmpCode     EmpName EmpOccupation         EmpDOJ        EmpAge
0       23  2018-01-25        Emp001       John Doe       Chemist
1       24  2018-01-26         Emp00  William Spark  Statistician
```

### 11如何根据 Pandas 列中的值从 DataFrame 中选择或过滤行

```
import pandas as pd
 
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})
 
print("\nUse == operator\n")
print(employees.loc[employees['Age'] == 23])
 
print("\nUse &lt; operator\n")
print(employees.loc[employees['Age'] &lt; 30])
 
print("\nUse != operator\n")
print(employees.loc[employees['Occupation'] != 'Statistician'])
 
print("\nMultiple Conditions\n")
print(employees.loc[(employees['Occupation'] != 'Statistician') &amp;
                    (employees['Name'] == 'John')])
```

Output:

```
Use == operator
 
   Age Date Of Join EmpCode  Name Occupation
0   23   2018-01-25  Emp001  John    Chemist
 
Use &lt; operator
 
   Age Date Of Join EmpCode   Name    Occupation
0   23   2018-01-25  Emp001   John       Chemist
1   24   2018-01-26  Emp002    Doe  Statistician
3   29   2018-02-26  Emp004  Spark  Statistician
 
Use != operator
 
   Age Date Of Join EmpCode  Name  Occupation
0   23   2018-01-25  Emp001  John     Chemist
4   40   2018-03-16  Emp005  Mark  Programmer
 
Multiple Conditions
 
   Age Date Of Join EmpCode  Name Occupation
0   23   2018-01-25  Emp001  John    Chemist
```

### 12在 DataFrame 中使用“isin”过滤多行

```
import pandas as pd
 
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})
 
print("\nUse isin operator\n")
print(employees.loc[employees['Occupation'].isin(['Chemist','Programmer'])])
 
print("\nMultiple Conditions\n")
print(employees.loc[(employees['Occupation'] == 'Chemist') |
                    (employees['Name'] == 'John') &amp;
                    (employees['Age'] &lt; 30)])
```

Output:

```
Use isin operator
 
   Age Date Of Join EmpCode  Name  Occupation
0   23   2018-01-25  Emp001  John     Chemist
4   40   2018-03-16  Emp005  Mark  Programmer
 
Multiple Conditions
 
   Age Date Of Join EmpCode  Name Occupation
0   23   2018-01-25  Emp001  John    Chemist
```

### 13迭代 DataFrame 的行和列

```
import pandas as pd
 
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})
 
print("\n Example iterrows \n")
for index, col in employees.iterrows():
    print(col['Name'], "--", col['Age'])
 
 
print("\n Example itertuples \n")
for row in employees.itertuples(index=True, name='Pandas'):
    print(getattr(row, "Name"), "--", getattr(row, "Age"))
```

Output:

```
Example iterrows
 
John -- 23
Doe -- 24
William -- 34
Spark -- 29
Mark -- 40
 
 Example itertuples
 
John -- 23
Doe -- 24
William -- 34
Spark -- 29
Mark -- 40
```

### 14如何通过名称或索引删除 DataFrame 的列

```
import pandas as pd
 
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})
 
print(employees)
 
print("\n Drop Column by Name \n")
employees.drop('Age', axis=1, inplace=True)
print(employees)
 
print("\n Drop Column by Index \n")
employees.drop(employees.columns[[0,1]], axis=1, inplace=True)
print(employees)
```

Output:

```
Age Date Of Join EmpCode     Name    Occupation
0   23   2018-01-25  Emp001     John       Chemist
1   24   2018-01-26  Emp002      Doe  Statistician
2   34   2018-01-26  Emp003  William  Statistician
3   29   2018-02-26  Emp004    Spark  Statistician
4   40   2018-03-16  Emp005     Mark    Programmer
 
 Drop Column by Name
 
  Date Of Join EmpCode     Name    Occupation
0   2018-01-25  Emp001     John       Chemist
1   2018-01-26  Emp002      Doe  Statistician
2   2018-01-26  Emp003  William  Statistician
3   2018-02-26  Emp004    Spark  Statistician
4   2018-03-16  Emp005     Mark    Programmer
 
 Drop Column by Index
 
      Name    Occupation
0     John       Chemist
1      Doe  Statistician
2  William  Statistician
3    Spark  Statistician
4     Mark    Programmer
```

### 15向 DataFrame 中新增列

```
import pandas as pd
 
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})
 
employees['City'] = ['London', 'Tokyo', 'Sydney', 'London', 'Toronto']
 
print(employees)
```

Output:

```
Age Date Of Join EmpCode     Name    Occupation     City
0   23   2018-01-25  Emp001     John       Chemist   London
1   24   2018-01-26  Emp002      Doe  Statistician    Tokyo
2   34   2018-01-26  Emp003  William  Statistician   Sydney
3   29   2018-02-26  Emp004    Spark  Statistician   London
4   40   2018-03-16  Emp005     Mark    Programmer  Toronto
```

### 16如何从 DataFrame 中获取列标题列表

```
import pandas as pd
 
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})
 
print(list(employees))
 
print(list(employees.columns.values))
 
print(employees.columns.tolist())
```

Output:

```
['Age', 'Date Of Join', 'EmpCode', 'Name', 'Occupation']
['Age', 'Date Of Join', 'EmpCode', 'Name', 'Occupation']
['Age', 'Date Of Join', 'EmpCode', 'Name', 'Occupation']
```

### 17如何随机生成 DataFrame

```
import pandas as pd
import numpy as np
 
np.random.seed(5)
 
df_random = pd.DataFrame(np.random.randint(100, size=(10, 6)),
                         columns=list('ABCDEF'),
                         index=['Row-{}'.format(i) for i in range(10)])
 
print(df_random)
```

Output:

```
A   B   C   D   E   F
Row-0  99  78  61  16  73   8
Row-1  62  27  30  80   7  76
Row-2  15  53  80  27  44  77
Row-3  75  65  47  30  84  86
Row-4  18   9  41  62   1  82
Row-5  16  78   5  58   0  80
Row-6   4  36  51  27  31   2
Row-7  68  38  83  19  18   7
Row-8  30  62  11  67  65  55
Row-9   3  91  78  27  29  33
```

### 18如何选择 DataFrame 的多个列

```
import pandas as pd
 
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})
 
df = employees[['EmpCode', 'Age', 'Name']]
print(df)
```

Output:

```
EmpCode  Age     Name
0  Emp001   23     John
1  Emp002   24      Doe
2  Emp003   34  William
3  Emp004   29    Spark
4  Emp005   40     Mark
```

### 19如何将字典转换为 DataFrame

```
import pandas as pd
 
data = ({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   })
print(data)
 
df = pd.DataFrame(data)
 
print(df)
```

Output:

```
{'Height': [165, 70, 120, 80, 180, 172, 150], 'Food': ['Steak', 'Lamb', 'Mango',
 'Apple', 'Cheese', 'Melon', 'Beans'], 'Age': [30, 20, 22, 40, 32, 28, 39], 'Sco
re': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2], 'Color': ['Blue', 'Green', 'Red', 'Whi
te', 'Gray', 'Black', 'Red'], 'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX'
]}
   Age  Color    Food  Height  Score State
0   30   Blue   Steak     165    4.6    NY
1   20  Green    Lamb      70    8.3    TX
2   22    Red   Mango     120    9.0    FL
3   40  White   Apple      80    3.3    AL
4   32   Gray  Cheese     180    1.8    AK
5   28  Black   Melon     172    9.5    TX
6   39    Red   Beans     150    2.2    TX
```

### 20使用 ioc 进行切片

```
import pandas as pd
 
df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])
 
print("\n -- Selecting a single row with .loc with a string -- \n")
print(df.loc['Penelope'])
 
print("\n -- Selecting multiple rows with .loc with a list of strings -- \n")
print(df.loc[['Cornelia', 'Jane', 'Dean']])
 
print("\n -- Selecting multiple rows with .loc with slice notation -- \n")
print(df.loc['Aaron':'Dean'])
```

Output:

```
-- Selecting a single row with .loc with a string --
 
Age          40
Color     White
Food      Apple
Height       80
Score       3.3
State        AL
Name: Penelope, dtype: object
 
 -- Selecting multiple rows with .loc with a list of strings --
 
          Age Color    Food  Height  Score State
Cornelia   39   Red   Beans     150    2.2    TX
Jane       30  Blue   Steak     165    4.6    NY
Dean       32  Gray  Cheese     180    1.8    AK
 
 -- Selecting multiple rows with .loc with slice notation --
 
          Age  Color    Food  Height  Score State
Aaron      22    Red   Mango     120    9.0    FL
Penelope   40  White   Apple      80    3.3    AL
Dean       32   Gray  Cheese     180    1.8    AK
```

### 21检查 DataFrame 中是否是空的

```
import pandas as pd
 
df = pd.DataFrame()
 
if df.empty:
    print('DataFrame is empty!')
```

Output:

```
DataFrame is empty!
```

### 22在创建 DataFrame 时指定索引和列名称

```
import pandas as pd
 
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
 
code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]
 
df = pd.DataFrame(values, index=code, columns=['Country'])
 
print(df)
```

Output:

```
Country
IND      India
CAN     Canada
AUS  Australia
JAP      Japan
GER    Germany
FRA     France
```

### 23使用 iloc 进行切片

```
import pandas as pd

df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print("\n -- Selecting a single row with .iloc with an integer -- \n")
print(df.iloc[4])

print("\n -- Selecting multiple rows with .iloc with a list of integers -- \n")
print(df.iloc[[2, -2]])

print("\n -- Selecting multiple rows with .iloc with slice notation -- \n")
print(df.iloc[:5:3])
```

Output:

```
-- Selecting a single row with .iloc with an integer --
 
Age           32
Color       Gray
Food      Cheese
Height       180
Score        1.8
State         AK
Name: Dean, dtype: object
 
 -- Selecting multiple rows with .iloc with a list of integers --
 
           Age  Color   Food  Height  Score State
Aaron       22    Red  Mango     120    9.0    FL
Christina   28  Black  Melon     172    9.5    TX
 
 -- Selecting multiple rows with .iloc with slice notation --
 
          Age  Color   Food  Height  Score State
Jane       30   Blue  Steak     165    4.6    NY
Penelope   40  White  Apple      80    3.3    AL
```

### 24iloc 和 loc 的区别
-  loc 索引器还可以进行布尔选择，例如，如果我们想查找 Age 小于 30 的所有行并仅返回 Color 和 Height 列，我们可以执行以下操作。我们可以用 iloc 复制它，但我们不能将它传递给一个布尔系列，必须将布尔系列转换为 numpy 数组 -  loc 从索引中获取具有特定标签的行（或列） -  iloc 在索引中的特定位置获取行（或列）（因此它只需要整数） 
```
import pandas as pd
 
df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])
 
print("\n -- loc -- \n")
print(df.loc[df['Age'] &lt; 30, ['Color', 'Height']])
 
print("\n -- iloc -- \n")
print(df.iloc[(df['Age'] &lt; 30).values, [1, 3]])
```

Output:

```
-- loc --
 
           Color  Height
Nick       Green      70
Aaron        Red     120
Christina  Black     172
 
 -- iloc --
 
           Color  Height
Nick       Green      70
Aaron        Red     120
Christina  Black     172
```

### 25使用时间索引创建空 DataFrame

```
import datetime
import pandas as pd
 
todays_date = datetime.datetime.now().date()
index = pd.date_range(todays_date, periods=10, freq='D')
 
columns = ['A', 'B', 'C']
 
df = pd.DataFrame(index=index, columns=columns)
df = df.fillna(0)
 
print(df)
```

Output:

```
A  B  C
2018-09-30  0  0  0
2018-10-01  0  0  0
2018-10-02  0  0  0
2018-10-03  0  0  0
2018-10-04  0  0  0
2018-10-05  0  0  0
2018-10-06  0  0  0
2018-10-07  0  0  0
2018-10-08  0  0  0
2018-10-09  0  0  0
```

### 26如何改变 DataFrame 列的排序

```
import pandas as pd

df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print("\n -- Change order using columns -- \n")
new_order = [3, 2, 1, 4, 5, 0]
df = df[df.columns[new_order]]
print(df)

print("\n -- Change order using reindex -- \n")
df = df.reindex(['State', 'Color', 'Age', 'Food', 'Score', 'Height'], axis=1)
print(df)
```

Output:

```
-- Change order using columns --
 
           Height    Food  Color  Score State  Age
Jane          165   Steak   Blue    4.6    NY   30
Nick           70    Lamb  Green    8.3    TX   20
Aaron         120   Mango    Red    9.0    FL   22
Penelope       80   Apple  White    3.3    AL   40
Dean          180  Cheese   Gray    1.8    AK   32
Christina     172   Melon  Black    9.5    TX   28
Cornelia      150   Beans    Red    2.2    TX   39
 
 -- Change order using reindex --
 
          State  Color  Age    Food  Score  Height
Jane         NY   Blue   30   Steak    4.6     165
Nick         TX  Green   20    Lamb    8.3      70
Aaron        FL    Red   22   Mango    9.0     120
Penelope     AL  White   40   Apple    3.3      80
Dean         AK   Gray   32  Cheese    1.8     180
Christina    TX  Black   28   Melon    9.5     172
Cornelia     TX    Red   39   Beans    2.2     150
```

### 27检查 DataFrame 列的数据类型

```
import pandas as pd
 
df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])
 
print(df.dtypes)
```

Output:

```
Age         int64
Color      object
Food       object
Height      int64
Score     float64
State      object
dtype: object
```

### 28更改 DataFrame 指定列的数据类型

```
import pandas as pd
 
df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])
 
print(df.dtypes)
 
df['Age'] = df['Age'].astype(str)
 
print(df.dtypes)
```

Output:

```
Age         int64
Color      object
Food       object
Height      int64
Score     float64
State      object
dtype: object
Age        object
Color      object
Food       object
Height      int64
Score     float64
State      object
dtype: object
```

### 29如何将列的数据类型转换为 DateTime 类型

```
import pandas as pd
 
df = pd.DataFrame({'DateOFBirth': [1349720105, 1349806505, 1349892905,
                                   1349979305, 1350065705, 1349792905,
                                   1349730105],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])
 
print("\n----------------Before---------------\n")
print(df.dtypes)
print(df)
 
df['DateOFBirth'] = pd.to_datetime(df['DateOFBirth'], unit='s')
 
print("\n----------------After----------------\n")
print(df.dtypes)
print(df)
```

Output:

```
----------------Before---------------
 
DateOFBirth     int64
State          object
dtype: object
           DateOFBirth State
Jane        1349720105    NY
Nick        1349806505    TX
Aaron       1349892905    FL
Penelope    1349979305    AL
Dean        1350065705    AK
Christina   1349792905    TX
Cornelia    1349730105    TX
 
----------------After----------------
 
DateOFBirth    datetime64[ns]
State                  object
dtype: object
                  DateOFBirth State
Jane      2012-10-08 18:15:05    NY
Nick      2012-10-09 18:15:05    TX
Aaron     2012-10-10 18:15:05    FL
Penelope  2012-10-11 18:15:05    AL
Dean      2012-10-12 18:15:05    AK
Christina 2012-10-09 14:28:25    TX
Cornelia  2012-10-08 21:01:45    TX
```

### 30将 DataFrame 列从 floats 转为 ints

```
import pandas as pd
 
df = pd.DataFrame({'DailyExp': [75.7, 56.69, 55.69, 96.5, 84.9, 110.5,
                                58.9],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])
 
print("\n----------------Before---------------\n")
print(df.dtypes)
print(df)
 
df['DailyExp'] = df['DailyExp'].astype(int)
 
print("\n----------------After----------------\n")
print(df.dtypes)
print(df)
```

Output:

```
----------------Before---------------
 
DailyExp    float64
State        object
dtype: object
           DailyExp State
Jane          75.70    NY
Nick          56.69    TX
Aaron         55.69    FL
Penelope      96.50    AL
Dean          84.90    AK
Christina    110.50    TX
Cornelia      58.90    TX
 
----------------After----------------
 
DailyExp     int32
State       object
dtype: object
           DailyExp State
Jane             75    NY
Nick             56    TX
Aaron            55    FL
Penelope         96    AL
Dean             84    AK
Christina       110    TX
Cornelia         58    TX
```

### 31如何把 dates 列转换为 DateTime 类型

```
import pandas as pd
 
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],                   
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])
 
print("\n----------------Before---------------\n")
print(df.dtypes)
  
df['DateOfBirth'] = df['DateOfBirth'].astype('datetime64')
  
print("\n----------------After----------------\n")
print(df.dtypes)
```

Output:

```
----------------Before---------------
 
DateOfBirth    object
State          object
dtype: object
 
----------------After----------------
 
DateOfBirth    datetime64[ns]
State                  object
dtype: object
```

### 32两个 DataFrame 相加

```
import pandas as pd
 
df1 = pd.DataFrame({'Age': [30, 20, 22, 40], 'Height': [165, 70, 120, 80],
                    'Score': [4.6, 8.3, 9.0, 3.3], 'State': ['NY', 'TX',
                                                             'FL', 'AL']},
                   index=['Jane', 'Nick', 'Aaron', 'Penelope'])
 
df2 = pd.DataFrame({'Age': [32, 28, 39], 'Color': ['Gray', 'Black', 'Red'],
                    'Food': ['Cheese', 'Melon', 'Beans'],
                    'Score': [1.8, 9.5, 2.2], 'State': ['AK', 'TX', 'TX']},
                   index=['Dean', 'Christina', 'Cornelia'])
 
df3 = df1.append(df2, sort=True)
 
print(df3)
```

Output:

```
Age  Color    Food  Height  Score State
Jane        30    NaN     NaN   165.0    4.6    NY
Nick        20    NaN     NaN    70.0    8.3    TX
Aaron       22    NaN     NaN   120.0    9.0    FL
Penelope    40    NaN     NaN    80.0    3.3    AL
Dean        32   Gray  Cheese     NaN    1.8    AK
Christina   28  Black   Melon     NaN    9.5    TX
Cornelia    39    Red   Beans     NaN    2.2    TX
```

### 33在 DataFrame 末尾添加额外的行

```
import pandas as pd
 
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})
 
print("\n------------ BEFORE ----------------\n")
print(employees)
 
employees.loc[len(employees)] = [45, '2018-01-25', 'Emp006', 'Sunny',
                                 'Programmer']
 
print("\n------------ AFTER ----------------\n")
print(employees)
```

Output:

```
------------ BEFORE ----------------
 
   Age Date Of Join EmpCode     Name    Occupation
0   23   2018-01-25  Emp001     John       Chemist
1   24   2018-01-26  Emp002      Doe  Statistician
2   34   2018-01-26  Emp003  William  Statistician
3   29   2018-02-26  Emp004    Spark  Statistician
4   40   2018-03-16  Emp005     Mark    Programmer
 
------------ AFTER ----------------
 
   Age Date Of Join EmpCode     Name    Occupation
0   23   2018-01-25  Emp001     John       Chemist
1   24   2018-01-26  Emp002      Doe  Statistician
2   34   2018-01-26  Emp003  William  Statistician
3   29   2018-02-26  Emp004    Spark  Statistician
4   40   2018-03-16  Emp005     Mark    Programmer
5   45   2018-01-25  Emp006    Sunny    Programmer
```

### 34为指定索引添加新行

```
import pandas as pd
 
employees = pd.DataFrame(
    data={'Name': ['John Doe', 'William Spark'],
          'Occupation': ['Chemist', 'Statistician'],
          'Date Of Join': ['2018-01-25', '2018-01-26'],
          'Age': [23, 24]},
    index=['Emp001', 'Emp002'],
    columns=['Name', 'Occupation', 'Date Of Join', 'Age'])
 
print("\n------------ BEFORE ----------------\n")
print(employees)
 
employees.loc['Emp003'] = ['Sunny', 'Programmer', '2018-01-25', 45]
 
print("\n------------ AFTER ----------------\n")
print(employees)
```

Output:

```
------------ BEFORE ----------------
 
                 Name    Occupation Date Of Join  Age
Emp001       John Doe       Chemist   2018-01-25   23
Emp002  William Spark  Statistician   2018-01-26   24
 
------------ AFTER ----------------
 
                 Name    Occupation Date Of Join  Age
Emp001       John Doe       Chemist   2018-01-25   23
Emp002  William Spark  Statistician   2018-01-26   24
Emp003          Sunny    Programmer   2018-01-25   45
```

### 35如何使用 for 循环添加行

```
import pandas as pd
 
cols = ['Zip']
lst = []
zip = 32100
 
for a in range(10):
    lst.append([zip])
    zip = zip + 1
 
df = pd.DataFrame(lst, columns=cols)
 
print(df)
```

Output:

```
Zip
0  32100
1  32101
2  32102
3  32103
4  32104
5  32105
6  32106
7  32107
8  32108
9  32109
```

### 36在 DataFrame 顶部添加一行

```
import pandas as pd
 
employees = pd.DataFrame({
    'EmpCode': ['Emp002', 'Emp003', 'Emp004'],
    'Name': ['John', 'Doe', 'William'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26'],
    'Age': [23, 24, 34]})
 
print("\n------------ BEFORE ----------------\n")
print(employees)
 
# New line
line = pd.DataFrame({'Name': 'Dean', 'Age': 45, 'EmpCode': 'Emp001',
                     'Date Of Join': '2018-02-26', 'Occupation': 'Chemist'
                     }, index=[0])
 
# Concatenate two dataframe
employees = pd.concat([line,employees.ix[:]]).reset_index(drop=True)
 
print("\n------------ AFTER ----------------\n")
print(employees)
```

Output:

```
------------ BEFORE ----------------
 
   Age Date Of Join EmpCode     Name    Occupation
0   23   2018-01-25  Emp002     John       Chemist
1   24   2018-01-26  Emp003      Doe  Statistician
2   34   2018-01-26  Emp004  William  Statistician
 
------------ AFTER ----------------
 
   Age Date Of Join EmpCode     Name    Occupation
0   45   2018-02-26  Emp001     Dean       Chemist
1   23   2018-01-25  Emp002     John       Chemist
2   24   2018-01-26  Emp003      Doe  Statistician
3   34   2018-01-26  Emp004  William  Statistician
```

### 37如何向 DataFrame 中动态添加行

```
import pandas as pd
 
df = pd.DataFrame(columns=['Name', 'Age'])
 
df.loc[1, 'Name'] = 'Rocky'
df.loc[1, 'Age'] = 23
 
df.loc[2, 'Name'] = 'Sunny'
 
print(df)
```

Output:

```
Name  Age
1  Rocky   23
2  Sunny  NaN
```

### 38在任意位置插入行

```
import pandas as pd
 
df = pd.DataFrame(columns=['Name', 'Age'])
 
df.loc[1, 'Name'] = 'Rocky'
df.loc[1, 'Age'] = 21
 
df.loc[2, 'Name'] = 'Sunny'
df.loc[2, 'Age'] = 22
 
df.loc[3, 'Name'] = 'Mark'
df.loc[3, 'Age'] = 25
 
df.loc[4, 'Name'] = 'Taylor'
df.loc[4, 'Age'] = 28
 
print("\n------------ BEFORE ----------------\n")
print(df)
 
line = pd.DataFrame({"Name": "Jack", "Age": 24}, index=[2.5])
df = df.append(line, ignore_index=False)
df = df.sort_index().reset_index(drop=True)
 
df = df.reindex(['Name', 'Age'], axis=1)
print("\n------------ AFTER ----------------\n")
print(df)
```

Output:

```
------------ BEFORE ----------------
 
     Name Age
1   Rocky  21
2   Sunny  22
3    Mark  25
4  Taylor  28
 
------------ AFTER ----------------
 
     Name Age
0   Rocky  21
1   Sunny  22
2    Jack  24
3    Mark  25
4  Taylor  28
```

### 39使用时间戳索引向 DataFrame 中添加行

```
import pandas as pd
 
df = pd.DataFrame(columns=['Name', 'Age'])
 
df.loc['2014-05-01 18:47:05', 'Name'] = 'Rocky'
df.loc['2014-05-01 18:47:05', 'Age'] = 21
 
df.loc['2014-05-02 18:47:05', 'Name'] = 'Sunny'
df.loc['2014-05-02 18:47:05', 'Age'] = 22
 
df.loc['2014-05-03 18:47:05', 'Name'] = 'Mark'
df.loc['2014-05-03 18:47:05', 'Age'] = 25
 
print("\n------------ BEFORE ----------------\n")
print(df)
 
line = pd.to_datetime("2014-05-01 18:50:05", format="%Y-%m-%d %H:%M:%S")
new_row = pd.DataFrame([['Bunny', 26]], columns=['Name', 'Age'], index=[line])
df = pd.concat([df, pd.DataFrame(new_row)], ignore_index=False)
 
print("\n------------ AFTER ----------------\n")
print(df)
```

Output:

```
------------ BEFORE ----------------
 
                      Name Age
2014-05-01 18:47:05  Rocky  21
2014-05-02 18:47:05  Sunny  22
2014-05-03 18:47:05   Mark  25
 
------------ AFTER ----------------
 
                      Name Age
2014-05-01 18:47:05  Rocky  21
2014-05-02 18:47:05  Sunny  22
2014-05-03 18:47:05   Mark  25
2014-05-01 18:50:05  Bunny  26
```

### 40为不同的行填充缺失值

```
import pandas as pd
 
a = {'A': 10, 'B': 20}
b = {'B': 30, 'C': 40, 'D': 50}
 
df1 = pd.DataFrame(a, index=[0])
df2 = pd.DataFrame(b, index=[1])
 
df = pd.DataFrame()
df = df.append(df1)
df = df.append(df2).fillna(0)
 
print(df)
```

Output:

```
A   B     C     D
0  10.0  20   0.0   0.0
1   0.0  30  40.0  50.0
```

### 41append, concat 和 combine_first 示例

```
import pandas as pd
 
a = {'A': 10, 'B': 20}
b = {'B': 30, 'C': 40, 'D': 50}
 
df1 = pd.DataFrame(a, index=[0])
df2 = pd.DataFrame(b, index=[1])
 
d1 = pd.DataFrame()
d1 = d1.append(df1)
d1 = d1.append(df2).fillna(0)
print("\n------------ append ----------------\n")
print(d1)
 
d2 = pd.concat([df1, df2]).fillna(0)
print("\n------------ concat ----------------\n")
print(d2)
 
d3 = pd.DataFrame()
d3 = d3.combine_first(df1).combine_first(df2).fillna(0)
print("\n------------ combine_first ----------------\n")
print(d3)
```

Output:

```
------------ append ----------------
 
      A   B     C     D
0  10.0  20   0.0   0.0
1   0.0  30  40.0  50.0
 
------------ concat ----------------
 
      A   B     C     D
0  10.0  20   0.0   0.0
1   0.0  30  40.0  50.0
 
------------ combine_first ----------------
 
      A     B     C     D
0  10.0  20.0   0.0   0.0
1   0.0  30.0  40.0  50.0
```

### 42获取行和列的平均值

```
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5, 5, 0, 0]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])
 
df['Mean Basket'] = df.mean(axis=1)
df.loc['Mean Fruit'] = df.mean()
 
print(df)
```

Output:

```
Apple  Orange  Banana       Pear  Mean Basket
Basket1     10.000000    20.0    30.0  40.000000         25.0
Basket2      7.000000    14.0    21.0  28.000000         17.5
Basket3      5.000000     5.0     0.0   0.000000          2.5
Mean Fruit   7.333333    13.0    17.0  22.666667         15.0
```

### 43计算行和列的总和

```
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5, 5, 0, 0]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])
 
df['Sum Basket'] = df.sum(axis=1)
df.loc['Sum Fruit'] = df.sum()
 
print(df)
```

Output:

```
Apple  Orange  Banana  Pear  Sum Basket
Basket1       10      20      30    40         100
Basket2        7      14      21    28          70
Basket3        5       5       0     0          10
Sum Fruit     22      39      51    68         180
```

### 44连接两列

```
import pandas as pd
 
df = pd.DataFrame(columns=['Name', 'Age'])
 
df.loc[1, 'Name'] = 'Rocky'
df.loc[1, 'Age'] = 21
 
df.loc[2, 'Name'] = 'Sunny'
df.loc[2, 'Age'] = 22
 
df.loc[3, 'Name'] = 'Mark'
df.loc[3, 'Age'] = 25
 
df.loc[4, 'Name'] = 'Taylor'
df.loc[4, 'Age'] = 28
 
print('\n------------ BEFORE ----------------\n')
print(df)
 
df['Employee'] = df['Name'].map(str) + ' - ' + df['Age'].map(str)
df = df.reindex(['Employee'], axis=1)
 
print('\n------------ AFTER ----------------\n')
print(df)
```

Output:

```
------------ BEFORE ----------------
 
     Name Age
1   Rocky  21
2   Sunny  22
3    Mark  25
4  Taylor  28
 
------------ AFTER ----------------
 
      Employee
1   Rocky - 21
2   Sunny - 22
3    Mark - 25
4  Taylor - 28
```

### 45过滤包含某字符串的行

```
import pandas as pd
 
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])
print(df)
 
print("\n---- Filter with State contains TX ----\n")
df1 = df[df['State'].str.contains("TX")]
 
print(df1)
```

Output:

```
DateOfBirth State
Jane       1986-11-11    NY
Nick       1999-05-12    TX
Aaron      1976-01-01    FL
Penelope   1986-06-01    AL
Dean       1983-06-04    AK
Christina  1990-03-07    TX
Cornelia   1999-07-09    TX
 
---- Filter with State contains TX ----
 
          DateOfBirth State
Nick       1999-05-12    TX
Christina  1990-03-07    TX
Cornelia   1999-07-09    TX
```

### 46过滤索引中包含某字符串的行

```
import pandas as pd
 
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])
print(df)
print("\n---- Filter Index contains ane ----\n")
df.index = df.index.astype('str')
df1 = df[df.index.str.contains('ane')]
 
print(df1)
```

Output:

```
DateOfBirth State
Jane       1986-11-11    NY
Pane       1999-05-12    TX
Aaron      1976-01-01    FL
Penelope   1986-06-01    AL
Frane      1983-06-04    AK
Christina  1990-03-07    TX
Cornelia   1999-07-09    TX
 
---- Filter Index contains ane ----
 
      DateOfBirth State
Jane   1986-11-11    NY
Pane   1999-05-12    TX
Frane  1983-06-04    AK
```

### 47使用 AND 运算符过滤包含特定字符串值的行

```
import pandas as pd
 
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])
print(df)
 
print("\n---- Filter DataFrame using &amp; ----\n")
 
df.index = df.index.astype('str')
df1 = df[df.index.str.contains('ane') &amp; df['State'].str.contains("TX")]
 
print(df1)
```

Output:

```
DateOfBirth State
Jane       1986-11-11    NY
Pane       1999-05-12    TX
Aaron      1976-01-01    FL
Penelope   1986-06-01    AL
Frane      1983-06-04    AK
Christina  1990-03-07    TX
Cornelia   1999-07-09    TX
 
---- Filter DataFrame using &amp; ----
 
     DateOfBirth State
Pane  1999-05-12    TX
```

### 48查找包含某字符串的所有行

```
import pandas as pd
 
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])
print(df)
 
print("\n---- Filter DataFrame using &amp; ----\n")
 
df.index = df.index.astype('str')
df1 = df[df.index.str.contains('ane') | df['State'].str.contains("TX")]
 
print(df1)
```

Output:

```
DateOfBirth State
Jane       1986-11-11    NY
Pane       1999-05-12    TX
Aaron      1976-01-01    FL
Penelope   1986-06-01    AL
Frane      1983-06-04    AK
Christina  1990-03-07    TX
Cornelia   1999-07-09    TX
 
---- Filter DataFrame using &amp; ----
 
          DateOfBirth State
Jane       1986-11-11    NY
Pane       1999-05-12    TX
Frane      1983-06-04    AK
Christina  1990-03-07    TX
Cornelia   1999-07-09    TX
```

### 49如果行中的值包含字符串，则创建与字符串相等的另一列

```
import pandas as pd
import numpy as np
 
df = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Accountant', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})
 
df['Department'] = pd.np.where(df.Occupation.str.contains("Chemist"), "Science",
                               pd.np.where(df.Occupation.str.contains("Statistician"), "Economics",
                               pd.np.where(df.Occupation.str.contains("Programmer"), "Computer", "General")))
 
print(df)
```

Output:

```
Age Date Of Join EmpCode     Name    Occupation Department
0   23   2018-01-25  Emp001     John       Chemist    Science
1   24   2018-01-26  Emp002      Doe    Accountant    General
2   34   2018-01-26  Emp003  William  Statistician  Economics
3   29   2018-02-26  Emp004    Spark  Statistician  Economics
4   40   2018-03-16  Emp005     Mark    Programmer   Computer
```

### 50计算 pandas group 中每组的行数

```
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5, 5, 0, 0],
                   [6, 6, 6, 6], [8, 8, 8, 8], [5, 5, 0, 0]],
                  columns=['Apple', 'Orange', 'Rice', 'Oil'],
                  index=['Basket1', 'Basket2', 'Basket3',
                         'Basket4', 'Basket5', 'Basket6'])
 
print(df)
print("\n ----------------------------- \n")
print(df[['Apple', 'Orange', 'Rice', 'Oil']].
      groupby(['Apple']).agg(['mean', 'count']))
```

Output:

```
Apple  Orange  Rice  Oil
Basket1     10      20    30   40
Basket2      7      14    21   28
Basket3      5       5     0    0
Basket4      6       6     6    6
Basket5      8       8     8    8
Basket6      5       5     0    0
 
 -----------------------------
 
      Orange       Rice        Oil
        mean count mean count mean count
Apple
5          5     2    0     2    0     2
6          6     1    6     1    6     1
7         14     1   21     1   28     1
8          8     1    8     1    8     1
10        20     1   30     1   40     1
```

### 51检查字符串是否在 DataFrme 中

```
import pandas as pd
 
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])
 
if df['State'].str.contains('TX').any():
    print("TX is there")
```

Output:

```
TX is there
```

### 52从 DataFrame 列中获取唯一行值

```
import pandas as pd
 
df = pd.DataFrame({'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])
 
print(df)
print("\n----------------\n")
 
print(df["State"].unique())
```

Output:

```
State
Jane         NY
Nick         TX
Aaron        FL
Penelope     AL
Dean         AK
Christina    TX
Cornelia     TX
 
----------------
 
['NY' 'TX' 'FL' 'AL' 'AK']
```

### 53计算 DataFrame 列的不同值

```
import pandas as pd
 
df = pd.DataFrame({'Age': [30, 20, 22, 40, 20, 30, 20, 25],
                    'Height': [165, 70, 120, 80, 162, 72, 124, 81],
                    'Score': [4.6, 8.3, 9.0, 3.3, 4, 8, 9, 3],
                    'State': ['NY', 'TX', 'FL', 'AL', 'NY', 'TX', 'FL', 'AL']},
                   index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Jaane', 'Nicky', 'Armour', 'Ponting'])
 
print(df.Age.value_counts())
```

Output:

```
20    3
30    2
25    1
22    1
40    1
Name: Age, dtype: int64
```

### 54删除具有重复索引的行

```
import pandas as pd

df = pd.DataFrame({'Age': [30, 30, 22, 40, 20, 30, 20, 25],
                   'Height': [165, 165, 120, 80, 162, 72, 124, 81],
                   'Score': [4.6, 4.6, 9.0, 3.3, 4, 8, 9, 3],
                   'State': ['NY', 'NY', 'FL', 'AL', 'NY', 'TX', 'FL', 'AL']},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])

print("\n -------- Duplicate Rows ----------- \n")
print(df)

df1 = df.reset_index().drop_duplicates(subset='index',
                                       keep='first').set_index('index')

print("\n ------- Unique Rows ------------ \n")
print(df1)
```

Output:

```
-------- Duplicate Rows -----------
 
          Age  Height  Score State
Jane       30     165    4.6    NY
Jane       30     165    4.6    NY
Aaron      22     120    9.0    FL
Penelope   40      80    3.3    AL
Jaane      20     162    4.0    NY
Nicky      30      72    8.0    TX
Armour     20     124    9.0    FL
Ponting    25      81    3.0    AL
 
 ------- Unique Rows ------------
 
          Age  Height  Score State
index
Jane       30     165    4.6    NY
Aaron      22     120    9.0    FL
Penelope   40      80    3.3    AL
Jaane      20     162    4.0    NY
Nicky      30      72    8.0    TX
Armour     20     124    9.0    FL
Ponting    25      81    3.0    AL
```

### 55删除某些列具有重复值的行

```
import pandas as pd
 
df = pd.DataFrame({'Age': [30, 40, 30, 40, 30, 30, 20, 25],
                   'Height': [120, 162, 120, 120, 120, 72, 120, 81],
                   'Score': [4.6, 4.6, 9.0, 3.3, 4, 8, 9, 3],
                   'State': ['NY', 'NY', 'FL', 'AL', 'NY', 'TX', 'FL', 'AL']},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])
 
print("\n -------- Duplicate Rows ----------- \n")
print(df)
 
df1 = df.reset_index().drop_duplicates(subset=['Age','Height'],
                                       keep='first').set_index('index')
 
print("\n ------- Unique Rows ------------ \n")
print(df1)
```

Output:

```
-------- Duplicate Rows -----------
 
          Age  Height  Score State
Jane       30     120    4.6    NY
Jane       40     162    4.6    NY
Aaron      30     120    9.0    FL
Penelope   40     120    3.3    AL
Jaane      30     120    4.0    NY
Nicky      30      72    8.0    TX
Armour     20     120    9.0    FL
Ponting    25      81    3.0    AL
 
 ------- Unique Rows ------------
 
          Age  Height  Score State
index
Jane       30     120    4.6    NY
Jane       40     162    4.6    NY
Penelope   40     120    3.3    AL
Nicky      30      72    8.0    TX
Armour     20     120    9.0    FL
Ponting    25      81    3.0    AL
```

### 56从 DataFrame 单元格中获取值

```
import pandas as pd

df = pd.DataFrame({'Age': [30, 40, 30, 40, 30, 30, 20, 25],
                   'Height': [120, 162, 120, 120, 120, 72, 120, 81],
                   'Score': [4.6, 4.6, 9.0, 3.3, 4, 8, 9, 3],
                   'State': ['NY', 'NY', 'FL', 'AL', 'NY', 'TX', 'FL', 'AL']},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])

print(df.loc['Nicky', 'Age'])
```

Output:

```
30
```

### 57使用 DataFrame 中的条件索引获取单元格上的标量值

```
import pandas as pd

df = pd.DataFrame({'Age': [30, 40, 30, 40, 30, 30, 20, 25],
                   'Height': [120, 162, 120, 120, 120, 72, 120, 81],
                   'Score': [4.6, 4.6, 9.0, 3.3, 4, 8, 9, 3],
                   'State': ['NY', 'NY', 'FL', 'AL', 'NY', 'TX', 'FL', 'AL']},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])

print("\nGet Height where Age is 20")
print(df.loc[df['Age'] == 20, 'Height'].values[0])

print("\nGet State where Age is 30")
print(df.loc[df['Age'] == 30, 'State'].values[0])
```

Output:

```
Get Height where Age is 20
120
 
Get State where Age is 30
NY
```

### 58设置 DataFrame 的特定单元格值

```
import pandas as pd
 
df = pd.DataFrame({'Age': [30, 40, 30, 40, 30, 30, 20, 25],
                   'Height': [120, 162, 120, 120, 120, 72, 120, 81]},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])
print("\n--------------Before------------\n")
print(df)
 
df.iat[0, 0] = 90
df.iat[0, 1] = 91
df.iat[1, 1] = 92
df.iat[2, 1] = 93
df.iat[7, 1] = 99
 
print("\n--------------After------------\n")
print(df)
```

Output:

```
--------------Before------------
 
          Age  Height
Jane       30     120
Jane       40     162
Aaron      30     120
Penelope   40     120
Jaane      30     120
Nicky      30      72
Armour     20     120
Ponting    25      81
 
--------------After------------
 
          Age  Height
Jane       90      91
Jane       40      92
Aaron      30      93
Penelope   40     120
Jaane      30     120
Nicky      30      72
Armour     20     120
Ponting    25      99
```

### 59从 DataFrame 行获取单元格值

```
import pandas as pd
 
df = pd.DataFrame({'Age': [30, 40, 30, 40, 30, 30, 20, 25],
                   'Height': [120, 162, 120, 120, 120, 72, 120, 81]},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])
 
 
print(df.loc[df.Age == 30,'Height'].tolist())
```

Output:

```
[120, 120, 120, 72]
```

### 60用字典替换 DataFrame 列中的值

```
import pandas as pd
 
df = pd.DataFrame({'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])
 
print(df)
 
dict = {"NY": 1, "TX": 2, "FL": 3, "AL": 4, "AK": 5}
df1 = df.replace({"State": dict})
 
print("\n\n")
print(df1)
```

Output:

```
State
Jane         NY
Nick         TX
Aaron        FL
Penelope     AL
Dean         AK
Christina    TX
Cornelia     TX
 
 
 
           State
Jane           1
Nick           2
Aaron          3
Penelope       4
Dean           5
Christina      2
Cornelia       2
```

### 61统计基于某一列的一列的数值

```
import pandas as pd
 
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],                   
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])
 
print(df.groupby('State').DateOfBirth.nunique())
```

Output:

```
State
AK    1
AL    1
FL    1
NY    1
TX    3
Name: DateOfBirth, dtype: int64
```

### 62处理 DataFrame 中的缺失值

```
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5,]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])
 
print("\n--------- DataFrame ---------\n")
print(df)
 
print("\n--------- Use of isnull() ---------\n")
print(df.isnull())
 
print("\n--------- Use of notnull() ---------\n")
print(df.notnull())
```

Output:

```
--------- DataFrame ---------
 
         Apple  Orange  Banana  Pear
Basket1     10    20.0    30.0  40.0
Basket2      7    14.0    21.0  28.0
Basket3      5     NaN     NaN   NaN
 
--------- Use of isnull() ---------
 
         Apple  Orange  Banana   Pear
Basket1  False   False   False  False
Basket2  False   False   False  False
Basket3  False    True    True   True
 
--------- Use of notnull() ---------
 
         Apple  Orange  Banana   Pear
Basket1   True    True    True   True
Basket2   True    True    True   True
Basket3   True   False   False  False
```

### 63删除包含任何缺失数据的行

```
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5,]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])
 
print("\n--------- DataFrame ---------\n")
print(df)
 
print("\n--------- Use of dropna() ---------\n")
print(df.dropna())
```

Output:

```
--------- DataFrame ---------
 
         Apple  Orange  Banana  Pear
Basket1     10    20.0    30.0  40.0
Basket2      7    14.0    21.0  28.0
Basket3      5     NaN     NaN   NaN
 
--------- Use of dropna() ---------
 
         Apple  Orange  Banana  Pear
Basket1     10    20.0    30.0  40.0
Basket2      7    14.0    21.0  28.0
```

### 64删除 DataFrame 中缺失数据的列

```
import pandas as pd

df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5,]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])

print("\n--------- DataFrame ---------\n")
print(df)

print("\n--------- Drop Columns) ---------\n")
print(df.dropna(1))
```

Output:

```
--------- DataFrame ---------
 
         Apple  Orange  Banana  Pear
Basket1     10    20.0    30.0  40.0
Basket2      7    14.0    21.0  28.0
Basket3      5     NaN     NaN   NaN
 
--------- Drop Columns) ---------
 
         Apple
Basket1     10
Basket2      7
Basket3      5
```

### 65按降序对索引值进行排序

```
import pandas as pd
 
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])
 
print(df.sort_index(ascending=False))
```

Output:

```
DateOfBirth State
Penelope   1986-06-01    AL
Pane       1999-05-12    TX
Jane       1986-11-11    NY
Frane      1983-06-04    AK
Cornelia   1999-07-09    TX
Christina  1990-03-07    TX
Aaron      1976-01-01    FL
```

### 66按降序对列进行排序

```
import pandas as pd
 
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})
 
 
print(employees.sort_index(axis=1, ascending=False))
```

Output:

```
Occupation     Name EmpCode Date Of Join  Age
0       Chemist     John  Emp001   2018-01-25   23
1  Statistician      Doe  Emp002   2018-01-26   24
2  Statistician  William  Emp003   2018-01-26   34
3  Statistician    Spark  Emp004   2018-02-26   29
4    Programmer     Mark  Emp005   2018-03-16   40
```

### 67使用 rank 方法查找 DataFrame 中元素的排名

```
import pandas as pd

df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5, 5, 0, 0]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])

print("\n--------- DataFrame Values--------\n")
print(df)

print("\n--------- DataFrame Values by Rank--------\n")
print(df.rank())
```

Output:

```
--------- DataFrame Values--------
 
         Apple  Orange  Banana  Pear
Basket1     10      20      30    40
Basket2      7      14      21    28
Basket3      5       5       0     0
 
--------- DataFrame Values by Rank--------
 
         Apple  Orange  Banana  Pear
Basket1    3.0     3.0     3.0   3.0
Basket2    2.0     2.0     2.0   2.0
Basket3    1.0     1.0     1.0   1.0
```

### 68在多列上设置索引

```
import pandas as pd
 
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})
 
print("\n --------- Before Index ----------- \n")
print(employees)
 
print("\n --------- Multiple Indexing ----------- \n")
print(employees.set_index(['Occupation', 'Age']))
```

Output:

```
Date Of Join EmpCode     Name
Occupation   Age
Chemist      23    2018-01-25  Emp001     John
Statistician 24    2018-01-26  Emp002      Doe
             34    2018-01-26  Emp003  William
             29    2018-02-26  Emp004    Spark
Programmer   40    2018-03-16  Emp005     Mark
```

### 69确定 DataFrame 的周期索引和列

```
import pandas as pd
 
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
 
pidx = pd.period_range('2015-01-01', periods=6)
 
df = pd.DataFrame(values, index=pidx, columns=['Country'])
 
print(df)
```

Output:

```
Country
2015-01-01      India
2015-01-02     Canada
2015-01-03  Australia
2015-01-04      Japan
2015-01-05    Germany
2015-01-06     France
```

### 70导入 CSV 指定特定索引

```
import pandas as pd
 
df = pd.read_csv('test.csv', index_col="DateTime")
print(df)
```

Output:

```
Wheat    Rice     Oil
DateTime
10/10/2016  10.500  12.500  16.500
10/11/2016  11.250  12.750  17.150
10/12/2016  10.000  13.150  15.500
10/13/2016  12.000  14.500  16.100
10/14/2016  13.000  14.825  15.600
10/15/2016  13.075  15.465  15.315
10/16/2016  13.650  16.105  15.030
10/17/2016  14.225  16.745  14.745
10/18/2016  14.800  17.385  14.460
10/19/2016  15.375  18.025  14.175
```

### 71将 DataFrame 写入 csv

```
import pandas as pd
 
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])
 
df.to_csv('test.csv', encoding='utf-8', index=True)
```

Output:

```
检查本地文件
```

### 72使用 Pandas 读取 csv 文件的特定列

```
import pandas as pd
 
df = pd.read_csv("test.csv", usecols = ['Wheat','Oil'])
print(df)
```

### 73Pandas 获取 CSV 列的列表

```
import pandas as pd

cols = list(pd.read_csv("test.csv", nrows =1))
print(cols)
```

Output:

```
['DateTime', 'Wheat', 'Rice', 'Oil']
```

### 74找到列值最大的行

```
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])
 
print(df.ix[df['Apple'].idxmax()])
```

Output:

```
Apple     55
Orange    15
Banana     8
Pear      12
Name: Basket3, dtype: int64
```

### 75使用查询方法进行复杂条件选择

```
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])
 
print(df)
 
print("\n ----------- Filter data using query method ------------- \n")
df1 = df.ix[df.query('Apple &gt; 50 &amp; Orange &lt;= 15 &amp; Banana &lt; 15 &amp; Pear == 12').index]
print(df1)
```

Output:

```
Apple  Orange  Banana  Pear
Basket1     10      20      30    40
Basket2      7      14      21    28
Basket3     55      15       8    12
 
 ----------- Filter data using query method -------------
 
         Apple  Orange  Banana  Pear
Basket3     55      15       8    12
```

### 76检查 Pandas 中是否存在列

```
import pandas as pd

df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])

if 'Apple' in df.columns:
    print("Yes")
else:
    print("No")


if set(['Apple','Orange']).issubset(df.columns):
    print("Yes")
else:
    print("No")
```

### 77为特定列从 DataFrame 中查找 n-smallest 和 n-largest 值

```
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
 
print("\n----------- nsmallest -----------\n")
print(df.nsmallest(2, ['Apple']))
 
print("\n----------- nlargest -----------\n")
print(df.nlargest(2, ['Apple']))
```

Output:

```
----------- nsmallest -----------
 
         Apple  Orange  Banana  Pear
Basket6      5       4       9     2
Basket2      7      14      21    28
 
----------- nlargest -----------
 
         Apple  Orange  Banana  Pear
Basket3     55      15       8    12
Basket4     15      14       1     8
```

### 78从 DataFrame 中查找所有列的最小值和最大值

```
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
 
print("\n----------- Minimum -----------\n")
print(df[['Apple', 'Orange', 'Banana', 'Pear']].min())
 
print("\n----------- Maximum -----------\n")
print(df[['Apple', 'Orange', 'Banana', 'Pear']].max())
```

Output:

```
----------- Minimum -----------
 
Apple     5
Orange    1
Banana    1
Pear      2
dtype: int64
 
----------- Maximum -----------
 
Apple     55
Orange    20
Banana    30
Pear      40
dtype: int64
```

### 79在 DataFrame 中找到最小值和最大值所在的索引位置

```
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
 
print("\n----------- Minimum -----------\n")
print(df[['Apple', 'Orange', 'Banana', 'Pear']].idxmin())
 
print("\n----------- Maximum -----------\n")
print(df[['Apple', 'Orange', 'Banana', 'Pear']].idxmax())
```

Output:

```
----------- Minimum -----------
 
Apple     Basket6
Orange    Basket5
Banana    Basket4
Pear      Basket6
dtype: object
 
----------- Maximum -----------
 
Apple     Basket3
Orange    Basket1
Banana    Basket1
Pear      Basket1
dtype: object
```

### 80计算 DataFrame Columns 的累积乘积和累积总和

```
import pandas as pd

df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n----------- Cumulative Product -----------\n")
print(df[['Apple', 'Orange', 'Banana', 'Pear']].cumprod())

print("\n----------- Cumulative Sum -----------\n")
print(df[['Apple', 'Orange', 'Banana', 'Pear']].cumsum())
```

Output:

```
----------- Cumulative Product -----------
 
           Apple  Orange  Banana     Pear
Basket1       10      20      30       40
Basket2       70     280     630     1120
Basket3     3850    4200    5040    13440
Basket4    57750   58800    5040   107520
Basket5   404250   58800    5040   860160
Basket6  2021250  235200   45360  1720320
 
----------- Cumulative Sum -----------
 
         Apple  Orange  Banana  Pear
Basket1     10      20      30    40
Basket2     17      34      51    68
Basket3     72      49      59    80
Basket4     87      63      60    88
Basket5     94      64      61    96
Basket6     99      68      70    98
```

### 81汇总统计

```
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
 
print("\n----------- Describe DataFrame -----------\n")
print(df.describe())
 
print("\n----------- Describe Column -----------\n")
print(df[['Apple']].describe())
```

Output:

```
----------- Describe DataFrame -----------
 
           Apple     Orange     Banana       Pear
count   6.000000   6.000000   6.000000   6.000000
mean   16.500000  11.333333  11.666667  16.333333
std    19.180719   7.257180  11.587349  14.555640
min     5.000000   1.000000   1.000000   2.000000
25%     7.000000   6.500000   2.750000   8.000000
50%     8.500000  14.000000   8.500000  10.000000
75%    13.750000  14.750000  18.000000  24.000000
max    55.000000  20.000000  30.000000  40.000000
 
----------- Describe Column -----------
 
           Apple
count   6.000000
mean   16.500000
std    19.180719
min     5.000000
25%     7.000000
50%     8.500000
75%    13.750000
max    55.000000
```

### 82查找 DataFrame 的均值、中值和众数

```
import pandas as pd

df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n----------- Calculate Mean -----------\n")
print(df.mean())

print("\n----------- Calculate Median -----------\n")
print(df.median())

print("\n----------- Calculate Mode -----------\n")
print(df.mode())
```

Output:

```
----------- Calculate Mean -----------
 
Apple     16.500000
Orange    11.333333
Banana    11.666667
Pear      16.333333
dtype: float64
 
----------- Calculate Median -----------
 
Apple      8.5
Orange    14.0
Banana     8.5
Pear      10.0
dtype: float64
 
----------- Calculate Mode -----------
 
   Apple  Orange  Banana  Pear
0      7      14       1     8
```

### 83测量 DataFrame 列的方差和标准偏差

```
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
 
print("\n----------- Calculate Mean -----------\n")
print(df.mean())
 
print("\n----------- Calculate Median -----------\n")
print(df.median())
 
print("\n----------- Calculate Mode -----------\n")
print(df.mode())
```

Output:

```
----------- Measure Variance -----------
 
Apple     367.900000
Orange     52.666667
Banana    134.266667
Pear      211.866667
dtype: float64
 
----------- Standard Deviation -----------
 
Apple     19.180719
Orange     7.257180
Banana    11.587349
Pear      14.555640
dtype: float64
```

### 84计算 DataFrame 列之间的协方差

```
import pandas as pd

df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n----------- Calculating Covariance -----------\n")
print(df.cov())

print("\n----------- Between 2 columns -----------\n")
# Covariance of Apple vs Orange
print(df.Apple.cov(df.Orange))
```

Output:

```
----------- Calculating Covariance -----------
 
        Apple     Orange      Banana        Pear
Apple   367.9  47.600000  -40.200000  -35.000000
Orange   47.6  52.666667   54.333333   77.866667
Banana  -40.2  54.333333  134.266667  154.933333
Pear    -35.0  77.866667  154.933333  211.866667
 
----------- Between 2 columns -----------
 
47.60000000000001
```

### 85计算 Pandas 中两个 DataFrame 对象之间的相关性

```
import pandas as pd

df1 = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n------ Calculating Correlation of one DataFrame Columns -----\n")
print(df1.corr())

df2 = pd.DataFrame([[52, 54, 58, 41], [14, 24, 51, 78], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 17, 18, 98], [15, 34, 29, 52]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n----- Calculating correlation between two DataFrame -------\n")
print(df2.corrwith(other=df1))
```

Output:

```
------ Calculating Correlation of one DataFrame Columns -----
 
           Apple    Orange    Banana      Pear
Apple   1.000000  0.341959 -0.180874 -0.125364
Orange  0.341959  1.000000  0.646122  0.737144
Banana -0.180874  0.646122  1.000000  0.918606
Pear   -0.125364  0.737144  0.918606  1.000000
 
----- Calculating correlation between two DataFrame -------
 
Apple     0.678775
Orange    0.354993
Banana    0.920872
Pear      0.076919
dtype: float64
```

### 86计算 DataFrame 列的每个单元格的百分比变化

```
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
 
print("\n------ Percent change at each cell of a Column -----\n")
print(df[['Apple']].pct_change()[:3])
 
print("\n------ Percent change at each cell of a DataFrame -----\n")
print(df.pct_change()[:5])
```

Output:

```
------ Percent change at each cell of a Column -----
 
            Apple
Basket1       NaN
Basket2 -0.300000
Basket3  6.857143
 
------ Percent change at each cell of a DataFrame -----
 
            Apple    Orange    Banana      Pear
Basket1       NaN       NaN       NaN       NaN
Basket2 -0.300000 -0.300000 -0.300000 -0.300000
Basket3  6.857143  0.071429 -0.619048 -0.571429
Basket4 -0.727273 -0.066667 -0.875000 -0.333333
Basket5 -0.533333 -0.928571  0.000000  0.000000
```

### 87在 Pandas 中向前和向后填充 DataFrame 列的缺失值

```
import pandas as pd
 
df = pd.DataFrame([[10, 30, 40], [], [15, 8, 12],
                   [15, 14, 1, 8], [7, 8], [5, 4, 1]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
 
print("\n------ DataFrame with NaN -----\n")
print(df)
 
print("\n------ DataFrame with Forward Filling -----\n")
print(df.ffill())
 
print("\n------ DataFrame with Forward Filling -----\n")
print(df.bfill())
```

Output:

```
------ DataFrame with NaN -----
 
         Apple  Orange  Banana  Pear
Basket1   10.0    30.0    40.0   NaN
Basket2    NaN     NaN     NaN   NaN
Basket3   15.0     8.0    12.0   NaN
Basket4   15.0    14.0     1.0   8.0
Basket5    7.0     8.0     NaN   NaN
Basket6    5.0     4.0     1.0   NaN
 
------ DataFrame with Forward Filling -----
 
         Apple  Orange  Banana  Pear
Basket1   10.0    30.0    40.0   NaN
Basket2   10.0    30.0    40.0   NaN
Basket3   15.0     8.0    12.0   NaN
Basket4   15.0    14.0     1.0   8.0
Basket5    7.0     8.0     1.0   8.0
Basket6    5.0     4.0     1.0   8.0
 
------ DataFrame with Forward Filling -----
 
         Apple  Orange  Banana  Pear
Basket1   10.0    30.0    40.0   8.0
Basket2   15.0     8.0    12.0   8.0
Basket3   15.0     8.0    12.0   8.0
Basket4   15.0    14.0     1.0   8.0
Basket5    7.0     8.0     1.0   NaN
Basket6    5.0     4.0     1.0   NaN
```

### 88在 Pandas 中使用非分层索引使用 Stacking

```
import pandas as pd
 
df = pd.DataFrame([[10, 30, 40], [], [15, 8, 12],
                   [15, 14, 1, 8], [7, 8], [5, 4, 1]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
 
print("\n------ DataFrame-----\n")
print(df)
 
print("\n------ Stacking DataFrame -----\n")
print(df.stack(level=-1))
```

Output:

```
------ DataFrame-----
 
         Apple  Orange  Banana  Pear
Basket1   10.0    30.0    40.0   NaN
Basket2    NaN     NaN     NaN   NaN
Basket3   15.0     8.0    12.0   NaN
Basket4   15.0    14.0     1.0   8.0
Basket5    7.0     8.0     NaN   NaN
Basket6    5.0     4.0     1.0   NaN
 
------ Stacking DataFrame -----
 
Basket1  Apple     10.0
         Orange    30.0
         Banana    40.0
Basket3  Apple     15.0
         Orange     8.0
         Banana    12.0
Basket4  Apple     15.0
         Orange    14.0
         Banana     1.0
         Pear       8.0
Basket5  Apple      7.0
         Orange     8.0
Basket6  Apple      5.0
         Orange     4.0
         Banana     1.0
dtype: float64
```

### 89使用分层索引对 Pandas 进行拆分

```
import pandas as pd

df = pd.DataFrame([[10, 30, 40], [], [15, 8, 12],
                   [15, 14, 1, 8], [7, 8], [5, 4, 1]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n------ DataFrame-----\n")
print(df)

print("\n------ Unstacking DataFrame -----\n")
print(df.unstack(level=-1))
```

Output:

```
------ DataFrame-----
 
         Apple  Orange  Banana  Pear
Basket1   10.0    30.0    40.0   NaN
Basket2    NaN     NaN     NaN   NaN
Basket3   15.0     8.0    12.0   NaN
Basket4   15.0    14.0     1.0   8.0
Basket5    7.0     8.0     NaN   NaN
Basket6    5.0     4.0     1.0   NaN
 
------ Unstacking DataFrame -----
 
Apple   Basket1    10.0
        Basket2     NaN
        Basket3    15.0
        Basket4    15.0
        Basket5     7.0
        Basket6     5.0
Orange  Basket1    30.0
        Basket2     NaN
        Basket3     8.0
        Basket4    14.0
        Basket5     8.0
        Basket6     4.0
Banana  Basket1    40.0
        Basket2     NaN
        Basket3    12.0
        Basket4     1.0
        Basket5     NaN
        Basket6     1.0
Pear    Basket1     NaN
        Basket2     NaN
        Basket3     NaN
        Basket4     8.0
        Basket5     NaN
        Basket6     NaN
dtype: float64
```

### 90Pandas 获取 HTML 页面上 table 数据

```
import pandas as pd
df pd.read_html("url")
```

**<strong><img alt="27dce76462c45bb98549aa65f3af2b12.png" src="https://img-blog.csdnimg.cn/img_convert/27dce76462c45bb98549aa65f3af2b12.png"> **</strong>**<strong>阅读更多**</strong>
-   -   -   -   -   -   -   -   -   
<img alt="e67700e03f5051454e2ab0c09e211101.gif" src="https://img-blog.csdnimg.cn/img_convert/e67700e03f5051454e2ab0c09e211101.gif">
