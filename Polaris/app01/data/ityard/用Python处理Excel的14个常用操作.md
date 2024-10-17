
--- 
title:  用Python处理Excel的14个常用操作 
tags: []
categories: [] 

---
```
‍自从学了Python后就逼迫用Python来处理Excel，所有操作用Python实现。目的是巩固Python，与增强数据处理能力。
```

这也是我写这篇文章的初衷。废话不说了，直接进入正题。

数据是网上找到的销售数据，长这样：

<img src="https://img-blog.csdnimg.cn/img_convert/cbce2a0ec40d167a42845a62eaa6a22d.png" alt="cbce2a0ec40d167a42845a62eaa6a22d.png">

### **一、关联公式:Vlookup**

vlookup是excel几乎最常用的公式，一般用于两个表的关联查询等。所以我先把这张表分为两个表。

```
df1=sale[['订单明细号','单据日期','地区名称', '业务员名称','客户分类', '存货编码', '客户名称', '业务员编码', '存货名称', '订单号',
       '客户编码', '部门名称', '部门编码']]
df2=sale[['订单明细号','存货分类', '税费', '不含税金额', '订单金额', '利润', '单价','数量']]
```

需求：想知道df1的每一个订单对应的利润是多少。

利润一列存在于df2的表格中，所以想知道df1的每一个订单对应的利润是多少。用excel的话首先确认订单明细号是唯一值，然后在df1新增一列写：=vlookup(a2,df2!a:h,6,0) ，然后往下拉就ok了。（剩下13个我就不写excel啦）

那用python是如何实现的呢？

```
#查看订单明细号是否重复，结果是没。
df1["订单明细号"].duplicated().value_counts()
df2["订单明细号"].duplicated().value_counts()

df_c=pd.merge(df1,df2,on="订单明细号",how="left")
```

### **二、数据透视表**

**需求：想知道每个地区的业务员分别赚取的利润总和与利润平均数。**

```
pd.pivot_table(sale,index="地区名称",columns="业务员名称",values="利润",aggfunc=[np.sum,np.mean])
```

### **三、对比两列差异**

因为这表每列数据维度都不一样，比较起来没啥意义，所以我先做了个订单明细号的差异再进行比较。

需求：比较订单明细号与订单明细号2的差异并显示出来。

```
sale["订单明细号2"]=sale["订单明细号"]

#在订单明细号2里前10个都+1.
sale["订单明细号2"][1:10]=sale["订单明细号2"][1:10]+1

#差异输出
result=sale.loc[sale["订单明细号"].isin(sale["订单明细号2"])==False]
```

### **四、去除重复值**

**需求：去除业务员编码的重复值**

```
sale.drop_duplicates("业务员编码",inplace=True)
```

### **五、缺失值处理**

先查看销售数据哪几列有缺失值。

```
#列的行数小于index的行数的说明有缺失值，这里客户名称329&lt;335,说明有缺失值
sale.info()
```

<img width="637" src="https://img-blog.csdnimg.cn/img_convert/1fd0edc836307cf176d7b07cbec3e1b5.jpeg" alt="1fd0edc836307cf176d7b07cbec3e1b5.jpeg">

**需求：用0填充缺失值或则删除有客户编码缺失值的行。**实际上缺失值处理的办法是很复杂的，这里只介绍简单的处理方法，若是数值变量，最常用平均数或中位数或众数处理，比较复杂的可以用随机森林模型根据其他维度去预测结果填充。若是分类变量，根据业务逻辑去填充准确性比较高。**比如这里的需求填充客户名称缺失值：就可以根据存货分类出现频率最大的存货所对应的客户名称去填充。**

这里我们用简单的处理办法：用0填充缺失值或则删除有客户编码缺失值的行。

```
#用0填充缺失值
sale["客户名称"]=sale["客户名称"].fillna(0)
#删除有客户编码缺失值的行
sale.dropna(subset=["客户编码"])
```

### **六、多条件筛选**

**需求：想知道业务员张爱，在北京区域卖的商品订单金额大于6000的信息。**

```
sale.loc[(sale["地区名称"]=="北京")&amp;(sale["业务员名称"]=="张爱")&amp;(sale["订单金额"]&gt;5000)]
```

### **七、 模糊筛选数据**

**需求:筛选存货名称含有"三星"或则含有"索尼"的信息。**

```
sale.loc[sale["存货名称"].str.contains("三星|索尼")]
```

### **八、分类汇总**

需求:北京区域各业务员的利润总额。

```
sale.groupby(["地区名称","业务员名称"])["利润"].sum()
```

### **九、条件计算**

**需求：存货名称含“三星字眼”并且税费高于1000的订单有几个？这些订单的利润总和和平均利润是多少？（或者最小值，最大值，四分位数，标注差）**

```
sale.loc[sale["存货名称"].str.contains("三星")&amp;(sale["税费"]&gt;=1000)][["订单明细号","利润"]].describe()
```

<img width="422" src="https://img-blog.csdnimg.cn/img_convert/0e842176fc316e4ddcdf711e6f420e48.png" alt="0e842176fc316e4ddcdf711e6f420e48.png">

### **十、删除数据间的空格**

需求：删除存货名称两边的空格。

```
sale["存货名称"].map(lambda s :s.strip(""))
```

### **十一、数据分列**

<img width="764" src="https://img-blog.csdnimg.cn/img_convert/0a3532d8212b8fba5d16c25c3f8a3105.png" alt="0a3532d8212b8fba5d16c25c3f8a3105.png">

需求：将日期与时间分列。

```
sale=pd.merge(sale,pd.DataFrame(sale["单据日期"].str.split(" ",expand=True)),how="inner",left_index=True,right_index=True)
```

### **十二、异常值替换**

首先用describe()函数简单查看一下数据有无异常值。

```
#可看到销项税有负数，一般不会有这种情况，视它为异常值。
sale.describe()
```

<img width="1200" src="https://img-blog.csdnimg.cn/img_convert/76fe3881629f29fdca14848f6c4709db.jpeg" alt="76fe3881629f29fdca14848f6c4709db.jpeg">

**需求：用0代替异常值。**

```
sale["订单金额"]=sale["订单金额"].replace(min(sale["订单金额"]),0)
```

### **十三、分组**

**需求：根据利润数据分布把地区分组为："较差","中等","较好","非常好"**

首先，当然是查看利润的数据分布呀，这里我们采用四分位数去判断。

```
sale.groupby("地区名称")["利润"].sum().describe()
```

<img width="361" src="https://img-blog.csdnimg.cn/img_convert/f83bae50b6dc93c66fd0a917ce33f9c4.png" alt="f83bae50b6dc93c66fd0a917ce33f9c4.png">

根据四分位数把地区总利润为[-9,7091]区间的分组为“较差”，(7091,10952]区间的分组为"中等" (10952,17656]分组为较好，(17656,37556]分组为非常好。

```
#先建立一个Dataframe
sale_area=pd.DataFrame(sale.groupby("地区名称")["利润"].sum()).reset_index()

#设置bins,和分组名称
bins=[-10,7091,10952,17656,37556]
groups=["较差","中等","较好","非常好"]

#使用cut分组
#sale_area["分组"]=pd.cut(sale_area["利润"],bins,labels=groups)
```

### **十四、根据业务逻辑定义标签**

**需求：销售利润率（即利润/订单金额）大于30%的商品信息并标记它为优质商品，小于5%为一般商品。**

```
sale.loc[(sale["利润"]/sale["订单金额"])&gt;0.3,"label"]="优质商品"
sale.loc[(sale["利润"]/sale["订单金额"])&lt;0.05,"label"]="一般商品"
```

其实excel常用的操作还有很多，我就列举了14个自己比较常用的，若还想实现哪些操作可以评论一起交流讨论，另外我自身也知道我写python不够精简，惯性使用loc。（其实query会比较精简）。若大家对这几个操作有更好的写法请务必评论告知我，感谢！

最后想说说，我觉得最好不要拿excel和python做对比，去研究哪个好用，其实都是工具，excel作为最为广泛的数据处理工具，垄断这么多年必定在数据处理方便也是相当优秀的，有些操作确实python会比较简单，但也有不少excel操作起来比python简单的。

比如一个很简单的操作：对各列求和并在最下一行显示出来，excel就是对一列总一个sum()函数，然后往左一拉就解决，而python则要定义一个函数（因为python要判断格式，若非数值型数据直接报错。）

总结一下就是：**无论用哪个工具，能解决问题就是好数据分析师！**
- - - ****