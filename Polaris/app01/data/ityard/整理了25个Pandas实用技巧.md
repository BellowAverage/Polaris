
--- 
title:  整理了25个Pandas实用技巧 
tags: []
categories: [] 

---
>  
  译者：山阴少年     
  原文链接：https://nbviewer.jupyter.org/github/justmarkham/pandas-videos/blob/master/top_25_pandas_tricks.ipynb 
 

**从剪贴板中创建DataFram**e

假设你将一些数据储存在Excel或者Google Sheet中，你又想要尽快地将他们读取至DataFrame中。

你需要选择这些数据并复制至剪贴板。然后，你可以使用**read_clipboard()函数**将他们读取至DataFrame中：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE12a0FVYnU4bjlyNGlhUEhrdDl0Qm10UU1nVnVXYmRDekpIQUFkUEV4cmxFWmdBZG4wSXZUSnhnLzY0MA?x-oss-process=image/format,png">

和read_csv()类似，read_clipboard()会自动检测每一列的正确的数据类型：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1QaExxT3JiV0ZzYkhPOFVlaWFoaENuUkQ4VnpGSFJWVGpDWkdVU2NUTThCQmVpY25RZEdTWTFpYncvNjQw?x-oss-process=image/format,png">

让我们再复制另外一个数据至剪贴板：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1pYVFCUUhIRmQxY2xpY1IwUE5MSFpVR25jaWF0UVl6cDdnTjJlZ2RXcm1pYnZHM1U3VkRNVWZhcXFnLzY0MA?x-oss-process=image/format,png">

神奇的是，pandas已经将第一列作为索引了：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE02dEJhbEYyZDhpY2NVMHJSNmliZUs5Tkhrb2gzWFdsdVdTR0FYZzN5SmUwUmliMnd0YmtKN09kZlEvNjQw?x-oss-process=image/format,png">

需要注意的是，**如果你想要你的工作在未来可复制，那么read_clipboard()并不值得推荐。**

**将DataFrame划分为两个随机的子集**

假设你想要将一个DataFrame划分为两部分，随机地将75%的行给一个DataFrame，剩下的25%的行给另一个DataFrame。

举例来说，我们的movie ratings这个DataFrame有979行：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE0yZ1A0SmljYVlEc2VqWU5pY2lhZ2gyMGU3OHRXaWF0blJvaWIzRWZEdllpYkp0Z1UxR00xTVRZVzdtckEvNjQw?x-oss-process=image/format,png">

我们可以使用**sample()函数**来随机选取75%的行，并将它们赋值给"movies_1"DataFrame：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1xamVvaWFyTWRWU0VtTGNyYjFEVzlBSFFubWplMHVveU9qRzlkUUE5TkN2WTBEOGlieUhqNWliSWcvNjQw?x-oss-process=image/format,png">

接着我们使用drop()函数来舍弃“moive_1”中出现过的行，将剩下的行赋值给"movies_2"DataFrame：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1sbzZCQkxiMEszNVNPYUpiZTI3NnNoSFdzUkNLNFF1bmliU2YwWFk4Y0lpYlFIT010bk9YMW1pY1EvNjQw?x-oss-process=image/format,png">

你可以发现总的行数是正确的：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1zQ0dybnVIbnRsR21qOW1vSHVpYVBFM2VLTzRHdEZYNGg5MjloQWljcHFqSG0xUnFGcG04dko3QS82NDA?x-oss-process=image/format,png">

你还可以检查每部电影的索引，或者"moives_1":

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1FUXczdFdqelZkMDFKM2lhSGZacXE5NWdaMTgzMFhGTHlYY0llMUtjZ3czQWlibHlOaWNFejRIVmcvNjQw?x-oss-process=image/format,png">

或者"moives_2":

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE13aWJJSjZneHljOFZBbDdsYUpFYjc5bU9ib3RDZ2JNS1hiZWliZ2lhYUhLWTUyWDZLaEhXRUdra2cvNjQw?x-oss-process=image/format,png">

需要注意的是，**这个方法在索引值不唯一的情况下不起作用。**

>  
  **注：**该方法在机器学习或者深度学习中很有用，因为在模型训练前，我们往往需要将全部数据集按某个比例划分成训练集和测试集。该方法既简单又高效，值得学习和尝试。 
 

**多种类型过滤DataFrame**

#### 

#### 让我们先看一眼movies这个DataFrame：

```
In [60]:
movies.head()


Out[60]:

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1lcHlsSHRxS3o1RFQ0enFtVkxmajRteWdtVmQ1UHd4VEpCZGx2bmtZVFJaZGljRDQ4M2hNMnNBLzY0MA?x-oss-process=image/format,png">

其中有一列是genre（类型）:

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1tOTdvdVlERlpqMjNqdzltdGw3dU15d2lhQ3g4cmpaejhTbHI2ZU9WNXJHZU9odmpPcldHaWM3US82NDA?x-oss-process=image/format,png">

比如我们想要对该DataFrame进行过滤，我们只想显示genre为Action或者Drama或者Western的电影，我们可以使用多个条件，以"or"符号分隔：

```
In [62]:
movies[(movies.genre == 'Action') |
       (movies.genre == 'Drama') |
       (movies.genre == 'Western')].head()


Out[62]:

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1SeVJpYWljWkJPVUFtaks5bDI5ME1JM2lhTjhSNklqOExTTDFtUjFjdHBuNjJ2RmliWXFIY2dyRlZnLzY0MA?x-oss-process=image/format,png">

但是，你实际上可以使用isin()函数将代码写得更加清晰，将genres列表传递给该函数：

```
In [63]:
movies[movies.genre.isin(['Action', 'Drama', 'Western'])].head()


Out[63]:

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1Ma1Y1aWFnUDJvT2FoekVaUGRzc1haaE0zckpYYXhLWng0SWFQdGRjNkJ2bE5oWWdYVFVFc0pRLzY0MA?x-oss-process=image/format,png">

如果你想要进行相反的过滤，也就是你将吧刚才的三种类型的电影排除掉，那么你可以在过滤条件前加上破浪号：

```
In [64]:
movies[~movies.genre.isin(['Action', 'Drama', 'Western'])].head()


Out[64]:

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1lRUJpYnJHMkRGeEgxbTdmR2tHU0VOT2RleDJwR3pObVhSOFduZThLOHhTVVBmc2x3OEhyaWFGZy82NDA?x-oss-process=image/format,png">

这种方法能够起作用是**因为在Python中，波浪号表示“not”操作。**

**DataFrame筛选数量最多类别**

假设你想要对movies这个DataFrame通过genre进行过滤，但是只需要前3个数量最多的genre。

我们对genre使用**value_counts()函数**，并将它保存成counts（type为Series）:

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1KSzJsbU9aaGljWmlhamFnRW1OWmNia0JKSWVWb0hUaGxCSnZ1bjAya0FoVmliMENEc1NNSlZobXcvNjQw?x-oss-process=image/format,png" width="692" height="347">

该Series的nlargest()函数能够轻松地计算出Series中前3个最大值：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1vR3ZVV2hRMkpzUEdFQnlNZkxrb3pOTWFtZHZQc3E1S2ljNUZSQnJwVkJib2JaVG5hZE9OZ0Z3LzY0MA?x-oss-process=image/format,png">

事实上我们在该Series中需要的是索引：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1NMjVYbjNmR0VuN1JUWjhPRVRnSEwwTXVwbjJaemdzSzQwcFp0VzRJMUhNb3h6MDFZaWI4MEZ3LzY0MA?x-oss-process=image/format,png">

最后，我们将该索引传递给isin()函数，该函数会把它当成genre列表：

```
In [68]:
movies[movies.genre.isin(counts.nlargest(3).index)].head()


Out[68]:

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1WUDl1WVpmSTM4MGliS0ZES3N4MkJiNkZZWnhXd1BpYjZVbjJaVHgwNm52OFEyUFo1bFBuUU1zZy82NDA?x-oss-process=image/format,png">

这样，在DataFrame中只剩下Drame, Comdey, Action这三种类型的电影了。

**处理缺失值**

让我们来看一看UFO sightings这个DataFrame:

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE05U3g0aWNGZXN0RXlpY2Z1SWJQTGtNZGRhNExybEt0M3V1Q3NTWUpTWTVZN2NvcTRUTnBXMDZpY0EvNjQw?x-oss-process=image/format,png" width="671" height="224">

你将会注意到有些值是**缺失的**。

为了找出每一列中有多少值是缺失的，你可以使用**isna()函数**，然后再使用**sum()**:

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1MeTNZYkhpY1Q0OWV2cDN2NUZVc1VWaWF1T0VNeHRiME93WXdiakdtWGJ2UE9hQnJBSFJFbFpMUS82NDA?x-oss-process=image/format,png">

isna()会产生一个由True和False组成的DataFrame，sum()会将所有的True值转换为1，False转换为0并把它们加起来。

类似地，你可以通过mean()和isna()函数找出每一列中缺失值的百分比。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1pYVFRTzB2Vk95OTVGY1BiT0UyY2Y0RXJOTmFTTjBlTTc2RklvRHg3TEhFSGpUY05EcGtQM0t3LzY0MA?x-oss-process=image/format,png">

如果你想要舍弃那些包含了缺失值的列，你可以使用dropna()函数：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1sTmlic3N6TkhUcWhsQm9pYVhZbHBaR0xxcFJpYjVxQlZ4cUNQZ1RmSFFtOXNYVnl3MmVudlIyY1EvNjQw?x-oss-process=image/format,png" width="673" height="223">

或者你想要舍弃那么缺失值占比超过10%的列，你可以给dropna()设置一个阈值：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1McEFsRXNCaWJNZjRBMW5KQ3VvR2pLSXZGVFVTcWZuTHBzc3NaNzNyT0FYZGljSUt4MW9Xd2ljRHcvNjQw?x-oss-process=image/format,png" width="681" height="220">

len(ufo)返回总行数，我们将它乘以0.9，以告诉pandas保留那些至少90%的值不是缺失值的列。

**一个字符串划分成多列**

我们先创建另一个新的示例DataFrame:

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1QNWFKZlpYeWtaT0xhWTF6NXVpY3l1cUlpY1hqbEF3ZlVCZ1JieldMbDR3M252a0lwZzhOUUV0QS82NDA?x-oss-process=image/format,png">

如果我们需要将“name”这一列划分为三个独立的列，用来表示first, middle, last name呢？我们将会使用**str.split()函数**，告诉它**以空格进行分隔**，并将结果扩展成一个DataFrame:

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE13NjB3eDZTdTNpYnlpYjUzTDZwanBvS2ljNk9RUlQ4VVBaRHFqdHplQW40SWMyTE5FUVkwc25Rc1EvNjQw?x-oss-process=image/format,png">

这三列实际上可以通过一行代码保存至原来的DataFrame:

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE0ybmliUjl0TFBxY291Z2licVRSbmVQaWNLSkxFeGhOU0g2aWNHYngxNVJCWTJpYlI1QWhKb0tUZWYyZy82NDA?x-oss-process=image/format,png">

如果我们想要划分一个字符串，但是仅保留其中一个结果列呢？比如说，让我们以", "来划分location这一列：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1YeThGVXEyV2lhaGx5TFN1R0ltMFBYNFg3TnNtbnFHaWJZaWJaR1dnYmRaQkU2ZHN0bFlESW1CSncvNjQw?x-oss-process=image/format,png">

如果我们只想保留第0列作为city name，我们仅需要选择那一列并保存至DataFrame:

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE03dTBtY2ZQeUU3R2dpYzZpY0VQTTRiRHp5NGliVEgzVHZ2ajZTeEJJS1VqQ1NTSk9MSkc5ZGFncFEvNjQw?x-oss-process=image/format,png">

**Series扩展成DataFrame**

让我们创建一个新的示例DataFrame:

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1vcUFYcm5SSTY2TGljeklZMld1YzBFbnBOTVJqTXBlclpKbWdSd2JpYVdEdGpLaWFaNmM1dUxkeVEvNjQw?x-oss-process=image/format,png">

这里有两列，第二列包含了Python中的由整数元素组成的列表。

如果我们想要将第二列扩展成DataFrame，我们可以对那一列使用**apply()函数并传递给Series constructor**:

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1pY2dGT3J3OU11N0Zqa1ZkaWNMd0FCZFU5UzA4V2ljSU1sQlEwRVNWaWFrbmxYaFV0QkcwS3FQRkdRLzY0MA?x-oss-process=image/format,png">

通过使用concat()函数，我们可以将原来的DataFrame和新的DataFrame组合起来：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1vblFYMkx0dmg5bXhhYk9XdWNiWGZkWkoyblFUamJ4bXBwTnYzVjZoZ2hZOGhLUnpWaWJjSGN3LzY0MA?x-oss-process=image/format,png">

**对多个函数进行聚合**

让我们来看一眼从Chipotle restaurant chain得到的orders这个DataFrame:

```
In [82]:
orders.head(10)


Out[82]:

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE05dkI5aWNvMGdwb1o0cHcwck9RZklJRGFqQ1lTbmhzM1RJUFA0ZlZLS2tqOEtiYUNWZTZhR3F3LzY0MA?x-oss-process=image/format,png">

每个订单（order）都有订单号（order_id），包含一行或者多行。为了找出每个订单的总价格，你可以将那个订单号的价格（item_price）加起来。比如，这里是订单号为1的总价格：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1KeTJTM0t3dGd6eU40QTl5UXJ4d3ZCOGg0dGI5dFVneElrZk5ueGlhTnJ1NkJNVHFpYkt0Nm5Rdy82NDA?x-oss-process=image/format,png">

如果你想要计算每个订单的总价格，你可以对order_id使用groupby()，再对每个group的item_price进行求和。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE01a3ZFVVFLTUdsbXUwSkhHSGVscVllMjhnVngxcEFiMDNlU0pPVnNlTUxpYUxjVGlheHlMaWFpYWljZy82NDA?x-oss-process=image/format,png">

但是，事实上你不可能在聚合时仅使用一个函数，比如sum()。**为了对多个函数进行聚合，你可以使用agg()函数，**传给它一个函数列表，比如sum()和count():

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE04bThod0pES2dsWlRZRzBQS0l3M0pXaWEweEdwWWVFRjJpY0xWelJaZ2lhdEk5YW9VbDZacGpEWUEvNjQw?x-oss-process=image/format,png" width="661" height="252">

这将告诉我们没定订单的总价格和数量。

**聚合结果与DataFrame组合**

让我们再看一眼orders这个DataFrame:

```
In [86]:
orders.head(10)


Out[86]:

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE01MXRXdjVpYzJkYTJsREE4M3JwV0hLNGcwY2ljdUJkaWJhWW5zclRPanpvVVN2eGZweE1oVzJ6bWcvNjQw?x-oss-process=image/format,png">

如果我们想要增加新的一列，用于展示每个订单的总价格呢？回忆一下，我们通过使用sum()函数得到了总价格：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1ZM0NWNGJaZ2hvOTdobjFRaG5pY3diSU9sdHJLa0tlaGliaWFpYWhWTXdxbGRpYWh1akdLVHQxanpjUS82NDA?x-oss-process=image/format,png">

sum()是一个聚合函数，这表明它返回输入数据的精简版本（reduced version ）。

换句话说，sum()函数的输出：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE13MklnUHNpYmJsZEd5a1VmS3lzTldLdEJncVk0bVlMeEJjQnZseTdkemdCRW1OWTZOUnhqZ253LzY0MA?x-oss-process=image/format,png">

比这个函数的输入要小：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1GalQxTk9kUlcxSksySXo1ZFVtVURLQ1pEd2JYNWtpYmRDTGlhZGMwaWNxUlhES1FpYllnNnpPanh3LzY0MA?x-oss-process=image/format,png">

解决的办法是**使用transform()函数****，它会执行相同的操作但是返回与输入数据相同的形状**：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1oQXhGbHdpYk02MFJEZWpLZnFvSWhNanloaWFtTGliMTh0Umx3NVlWZGtZeEhETlFXc3A0aWFyaWJUUS82NDA?x-oss-process=image/format,png">

我们将这个结果存储至DataFrame中新的一列：

```
In [91]:
orders['total_price'] = total_price
orders.head(10)


Out[91]:

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE01cUNHVGhxQ2liY1ZZeUJKNm5RSEhYaEx6SHJKN3gzQ3hiMm10YnlZODhYZFdnZ1ZWWjY1TjJnLzY0MA?x-oss-process=image/format,png">

你可以看到，每个订单的总价格在每一行中显示出来了。

这样我们就能方便地甲酸每个订单的价格占该订单的总价格的百分比：

```
In [92]:
orders['percent_of_total'] = orders.item_price / orders.total_price
orders.head(10)


In [92]:

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1pY0d3OVZQVTNmdTJDdXVscFFNRnpxcDdOclJiNkE0TzhUVERxVUpNejBnc21GV2liRWRya3N4dy82NDA?x-oss-process=image/format,png">

**选取行和列的切片**

让我们看一眼另一个数据集：

```
In [93]:
titanic.head()


Out[93]:

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1yU1hSVktkRGxIQ1NSRXV2eVBsVUUyM1JuQzNpYVFwTmplM3RGWkdzVXRwYjN2Vjh2aGtIeVZnLzY0MA?x-oss-process=image/format,png">

这就是著名的Titanic数据集，它保存了Titanic上乘客的信息以及他们是否存活。

如果你想要对这个数据集做一个数值方面的总结，你可以使用describe()函数：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE14SUFJdTNESUxtb3Z0U29zb2FBQllZbFpjQzQ5YmZ6Y0xVVTRwYnRkaGR6Q01La2FVYUJpYzVnLzY0MA?x-oss-process=image/format,png" width="678" height="302">

但是，这个DataFrame结果可能比你想要的信息显示得更多。

如果你想对这个结果进行过滤，只想显示“五数概括法”（five-number summary）的信息，你可以使用**loc函数并传递"min"到"max"的切片**:

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1rVkE3WlNUMXFiejgwTjNJdVE1Ulg1RERxSnptd0FmMFJaVnFOcnp0RXZjV2JzVU5sczc5ekEvNjQw?x-oss-process=image/format,png" width="681" height="222">

如果你不是对所有列都感兴趣，你也可以传递列名的切片：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1XYXJ2amtBckgya2o1bEdJNzhkRWczd2s1TklpYWYwTEQ1eVZvNjRCU2dPb3ozYmJqQUh5aWJXQS82NDA?x-oss-process=image/format,png" width="665" height="225">

**MultiIndexed Series重塑**

Titanic数据集的Survived列由1和0组成，因此你可以对这一列计算总的存活率：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1QcmdzaWJuWEE4a01MeGw5VTlydjd1eGpPRGdSZTN5THNSUDZ2a1A3d3J2N3BUN0lWSDRMZ05nLzY0MA?x-oss-process=image/format,png">

如果你想对某个类别，比如“Sex”，计算存活率，你可以使用groupby():

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1vRzd0a3NFbmljMG5laWFlQ3U3SXpVQ1JqZ3lMbFRpYjVRNU9BSTNRb3Bid1djczFmbk1FUDhiNlEvNjQw?x-oss-process=image/format,png">

如果你想一次性对两个类别变量计算存活率，你可以对这些类别变量使用groupby()：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1CMTQwWDJVbmZtS1ZFWm5wamliS3ZxN2NLVUlKNkpyTUNLdDA1Z0wzRFZ5bW1zaWNUQzRSMmpFdy82NDA?x-oss-process=image/format,png">

该结果展示了由Sex和Passenger Class联合起来的存活率。它存储为一个MultiIndexed Series，也就是说它对实际数据有多个索引层级。

这使得该数据难以读取和交互，因此更为方便的是**通过unstack()函数将MultiIndexed Series重塑成一个DataFrame**:

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1ZbEJXS0xuUmJUUzhvN2pGTGpoZkxubDd1WkNlV3pSR1BhdDZWTERHMXRZb1U1QnR1UkJPaHcvNjQw?x-oss-process=image/format,png">

该DataFrame包含了与MultiIndexed Series一样的数据，不同的是，现在你可以用熟悉的DataFrame的函数对它进行操作。

**创建数据透视表**

如果你经常使用上述的方法创建DataFrames，你也许会发现用**pivot_table()函数更为便捷**：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1melpCZDlPc1hxU3RxQmNpYVg5aDJWdWljY3dBQW82SWpualA3WTdsSHM0eG1UV2lhMmVGaEF0RmcvNjQw?x-oss-process=image/format,png">

想要使用数据透视表，你需要**指定索引**(index),** 列名**(columns), **值**(values)和**聚合函数**(aggregation function)。

数据透视表的另一个好处是，你可以**通过****设置margins=True轻松地将行和列都加起来**：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1GZlBvdGRsZ25qZG9SUTRzaWJkWW5pYjJtVEhaNTRNclRvWUY3VVkzaGtJeWZoMUtWSzZrZnJOQS82NDA?x-oss-process=image/format,png">

这个结果既显示了总的存活率，也显示了Sex和Passenger Class的存活率。

最后，你可以创建交叉表（cross-tabulation），只需要将聚合函数由"mean"改为"count":

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1pYWxCV0wxa25relFsRVJRaWJPTzFSR29UQnl1Z0hCM1FqNWZ2OVdhdENnazJ3d0JISUd0UW9MZy82NDA?x-oss-process=image/format,png">

这个结果展示了每一对类别变量组合后的记录总数。

**连续数据转类别数据**

让我们来看一下Titanic数据集中的Age那一列：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1pY2ZpYVEwU1lpYmliUGVDVldPTHUyaWJGRmZpYkNwMnBJSHlLQVJsUjRIZ002c2NpYmliRTloUVdqblFHQS82NDA?x-oss-process=image/format,png" width="681" height="232">

它现在是连续性数据，但是如果我们想要将它转变成类别数据呢？

一个解决办法是对年龄范围打标签，比如"adult", "young adult", "child"。实现该功能的最好方式是使用**cut()函数**：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1hN0I4c2JpY1dleXlvdjRLSXRXTGRlek42ZmliTlFROG5Pc2FOY2o3Wk1pYnM4eFBBdmliWHE5cThBLzY0MA?x-oss-process=image/format,png">

这会对每个值打上标签。0到18岁的打上标签"child"，18-25岁的打上标签"young adult"，25到99岁的打上标签“adult”。

注意到，该数据类型为**类别变量**，该类别变量**自动排好序**了（有序的类别变量）。

**Style a DataFrame**

上一个技巧在你想要修改整个jupyter notebook中的显示会很有用。但是，一个更灵活和有用的方法是定义特定DataFrame中的格式化（style）。

让我们回到stocks这个DataFrame:

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1VMDBjbUJvN2RFVVJVM2ljb01pYmVpY2tBenFWeHQ2eHVEUUxvZG5nM2dtdnYxQjhHRFFNV2ZnaWJnLzY0MA?x-oss-process=image/format,png" width="681" height="331">

我们可以**创建一个格式化字符串的字典，用于对每一列进行格式化**。然后将其传递给DataFrame的style.format()函数：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1ZT3Q2WDRwT3VCMnNDT25hYk5SQXlDbGRJdUU5c1J2VXRITjBxVmliOXZpYjdsVHplVVo5N1ZVUS82NDA?x-oss-process=image/format,png" width="694" height="349">

注意到，Date列是month-day-year的格式，Close列包含一个$符号，Volume列包含逗号。

我们可以通过**链式调用函数**来应用更多的格式化：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1KcWJuaWFGdjg1SXFFZjBIUnFCaklkYUkybEhRb3A5SzVJcVVXc25uVVhJNnRKSmpzZVJuaWNtdy82NDA?x-oss-process=image/format,png" width="686" height="391">

我们现在隐藏了索引，将Close列中的最小值高亮成红色，将Close列中的最大值高亮成浅绿色。

这里有另一个DataFrame格式化的例子：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE12aElFbTlrZnE0THg3anZ3WDhCUG51ZTUzRzJZNzJTYUIzczkwNW5pYXFWb0VBNW9pYm9MTTl3QS82NDA?x-oss-process=image/format,png" width="688" height="382">

Volume列现在有一个渐变的背景色，你可以轻松地识别出大的和小的数值。

最后一个例子：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1wQ0hBeVplb2xpYnZrUjd2UnJIN2FEbmtBaDNjQ1R0c3NhVGFWSXFQY0JwaWNRbXV6Qzg0TEdNdy82NDA?x-oss-process=image/format,png" width="682" height="424">

现在，Volumn列上有一个条形图，DataFrame上有一个标题。

请注意，还有许多其他的选项你可以用来格式化DataFrame。

**额外技巧**

#### ****

#### **Profile a DataFrame**

假设你拿到一个新的数据集，你不想要花费太多力气，只是想快速地探索下。那么你可以**使用****pandas-profiling这个模块**。

在你的系统上安装好该模块，然后**使用ProfileReport()函数**，传递的参数为任何一个DataFrame。它会返回一个互动的HTML报告：
- 第一部分为该数据集的总览，以及该数据集可能出现的问题列表- 第二部分为每一列的总结。你可以点击"toggle details"获取更多信息- 第三部分显示列之间的关联热力图- 第四部分为缺失值情况报告- 第五部分显示该数据及的前几行
**使用示例如下**（只显示第一部分的报告）：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95QXlRS3pDYkFIYU8xVTA5NWlienBCZHhsVE1URWQxaE1wYlVzakVjNmEzUGpqdTkxV0R3OGZHUjVKemcwWVF4YUNoVk1YbFpmVFRmaWJ1eE4xSnlTSVZ3LzY0MA?x-oss-process=image/format,png" width="902" height="735">

```
 PS：如果觉得分享内容有帮助，记得随手分享、点赞、在看~&lt; END &gt;

```
