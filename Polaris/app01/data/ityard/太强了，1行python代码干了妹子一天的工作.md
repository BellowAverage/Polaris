
--- 
title:  太强了，1行python代码干了妹子一天的工作 
tags: []
categories: [] 

---
事情是这样的，元旦前有朋友向我寻求帮助，吐槽老板在放假前给他安排一个苦逼的差事，想问问我能不能帮个忙，要不然假期都过不好了

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9JNGdZbktRZ1YxVkFEdlVqZGVMM1FtWFhSbXhjWVBIZzlUQlYxRk5xaWFpY2RldWhLQVVuOTlqalIzWW9ZaWNwNVNXRFFlSGdlcEE5cEphUDRsbWtCSDg4Zy82NDA?x-oss-process=image/format,png">

工作具体内容如下，主要是想把一个二维表格转成一维表格，如下图（表格为替代品）：

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9JNGdZbktRZ1YxVkFEdlVqZGVMM1FtWFhSbXhjWVBIZ1FIWnVTVFl2SHZlWjFQZU81SlVlcEZYVVhkYTVXZmJpYk1zS0wyemtwTEtOMkxFMjBLN09OdFEvNjQw?x-oss-process=image/format,png">

于是我马上想到了pandas，想着这么强大的函数肯定有这个功能，于是我开始翻阅资料，没想到还真找到了，而且仅用三行代码就搞定了，惊的朋友直呼python牛批

下面个大家详细介绍一下整个过程

### 1.正确读取表格

首先按照传统的方式读表格：

```
import pandas as pd
data1 = pd.read_excel('高中生数量.xlsx')
data1

```

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9JNGdZbktRZ1YxVkFEdlVqZGVMM1FtWFhSbXhjWVBIZzlQSHF2eXhDd2RCTnVuUlM3eWNnemJ1TjVxYjc5VEFBNWphY3RITm5VNVhDOGliZ2d2Szc3ancvNjQw?x-oss-process=image/format,png">

发现索引列没有被识别，产生了Unnamed: 0列，所以我们应该把第一列设置为索引列，代码如下：

```
import pandas as pd
data1 = pd.read_excel('高中生数量.xlsx',index_col=0)  #index_col用来设置索引列
data1

```

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9JNGdZbktRZ1YxVkFEdlVqZGVMM1FtWFhSbXhjWVBIZ2xpYWJyZVFtSEVNT3BGSWFaN3ZaRXpsdEVlRTR6MjgyWXBvRHlIUVEzdVlLOXlUVjJReHF0U2cvNjQw?x-oss-process=image/format,png">

这样就正常读取并识别表格了

### 2.重置索引

这一步主要是将索引列重置，变为普通列，便于下步，代码如下

```
data2=data1.reset_index()
data2

```

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9JNGdZbktRZ1YxVkFEdlVqZGVMM1FtWFhSbXhjWVBIZzJUVGZYZTRkUThvWTBvaWFsSFd1b3BHUmp0aDRleGIwSUk3RlJCUlV1eGtKOGFkS2dQRWFJb2cvNjQw?x-oss-process=image/format,png">

可以发现，之前的索引列编程‘index’列了

### 3.将列名转换为列数据

这一步主要用到pandas的melt函数，melt是逆转操作函数，可以将列名转换为列数据(columns name → column values)，重构DataFrame，用法如下：

```
pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None)

```

参数解释：

```
frame:要处理的数据集；
id_vars:不需要被转换的列名；
value_vars:需要转换的列名，如果剩下的列全部都要转换，就不用写了；
var_name和value_name是自定义设置对应的列名；
col_level :如果列是MultiIndex，则使用此级别。

```

我们把'index'列保留，并把转换后的列命名为'year',value命名为'stu_num':

```
data3=data2.melt(id_vars='index', var_name='year',value_name='stu_num')
data3

```

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9JNGdZbktRZ1YxVkFEdlVqZGVMM1FtWFhSbXhjWVBIZ1VLV2dWS1VzZXJEeWE1S2JMN3pPYmVxYVJjZkYyMGxXaWN2TlV1blM4OWp4dmRsSDJUY0s2R3cvNjQw?x-oss-process=image/format,png">

###  

### 4.把第一列设置为索引列

为了防止保存后的表格带有数字索引，需要把第一列设置为索引列：

```
data4=data3.set_index('index')
data4

```

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9JNGdZbktRZ1YxVkFEdlVqZGVMM1FtWFhSbXhjWVBIZ3VnSDZNeVZ2ckkxeGlhaWNoNVdraWJ6OE5lajFHdFMyNzZLU1l2U21tSDJVTjl0RWRjclAxVnU5US82NDA?x-oss-process=image/format,png">

###  

### 5.保存表格

```
data4.to_excel('转换后表格.xlsx')

```

大功告成，上述代码可以用1行代码搞定：

```
data=data.reset_index().melt('index', var_name='col').set_index('index')

```

是不是很强悍！

一起感受一下妹子的夸赞吧：

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9JNGdZbktRZ1YxVkFEdlVqZGVMM1FtWFhSbXhjWVBIZ2hJOGNpYjg3V1oyRTliZUpJVnFVMmliY1VkV2NRZm5RTUFUU2dKNlY3MHB2TWhsZEdpY25LUW1rUS82NDA?x-oss-process=image/format,png">

幸福就是这么简单，在这里哥想说一句，不是哥优秀，而是python太强大，哈哈！

 
