
--- 
title:  Python数据可视化：分析瑞幸VS星巴克全国门店分布情况 
tags: []
categories: [] 

---
瑞幸和星巴克在我国市场上，是把咖啡领域的大部分业务都已经给占领的状态，今天小爱就给大家分享一下，使用Python数据可视化分析瑞幸与星巴克全国门店分布情况，一起来吧！

<img src="https://img-blog.csdnimg.cn/img_convert/68c5e44516d7aa499e5e57e147fca0c5.png" alt="">

### **瑞幸会撼动星巴克的行业地位吗？**

10月份瑞幸咖啡的酱香拿铁火出圈，让瑞幸再一次出现在聚光灯下，上一次还是财务造假的时候。

这几年国内咖啡市场火热，带动瑞幸在内的很多咖啡品牌飞速发展，从2013年到2023年，预计中国人均咖啡消费量上涨了238%，现在全国合计咖啡门店数量已超10万家，且以每年上万家的数量在增长。

瑞幸咖啡的崛起让我们想到咖啡界的标杆-星巴克，星巴克几乎是过去十几年咖啡的代名词，也是城市白领们的生活方式。

现在出现的现象是，但凡有星巴克门店的地方，几百米内几乎都有瑞幸门店的身影，有的甚至两三个形成包围之势。

下面通过可视化看板和Python数据分析来对比星巴克和瑞幸门店在数量、区域分布上的差异及关联关系。

主要有两点发现：

**1、星巴克更集中于长三角、珠三角、京津冀等沿海经济发达地区，特别是一二线城市；瑞幸相比星巴克较为分散，在很多三四线及以下城市也有门店。**

**2、瑞幸门店选址集中在星巴克周边，数据显示方圆500米范围内，全国平均每个星巴克门店周边有0.6个瑞幸门店。**

<img src="https://img-blog.csdnimg.cn/img_convert/6d1ce140f8b36e9da5c035fc3fb8cc80.jpeg" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/cd369eda2a342acff8dd1b095d028499.png" alt="">

### **数据集**

因为要对比分析星巴克和瑞幸门店数量和位置，所以数据集主要字段有门店名称、经度、纬度、城市。

>  
 ❝注：数据集时间为2022年，有20%左右的数量误差❞ 


全国星巴克咖啡门店数据集：<img src="https://img-blog.csdnimg.cn/img_convert/8e8fa65e735a817eeea74d0290ade54c.jpeg" alt="">全国瑞幸咖啡门店数据集：<img src="https://img-blog.csdnimg.cn/img_convert/1a591d0dff31fc50ac1048039d075c9d.jpeg" alt="">

两个数据集都存放在平台上，通过数据视图可以直接查看和使用数据集，后面我们用来搭建数据看板。

因为后面需要Python来处理数据，所以需要通过API数据接口来获取数据，操作起来非常方便，留着后面备用。

```
import requests
headers = {<!-- --> "x-token": "你的鉴权token" }
response = requests.get("http://app.chafer.nexadata.cn/openapi/v1/sheet/sht22nId5uouP2/records?size=1&amp;page=1", headers = headers)
print(response.json())

```

<img src="https://img-blog.csdnimg.cn/img_convert/6dd235aacee08334ca4890bb2e391260.jpeg" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/caab2013f30d5c7db5accc0a67acc813.png" alt="">

#### **星巴克、瑞幸全国门店数对比**

截至数据集时间（2022年），星巴克全国门店数量预计4442，瑞幸咖啡全国门店数量预计3904，星巴克门店数比瑞幸多14%。

<img src="https://img-blog.csdnimg.cn/img_convert/ce8572d99fc520e7306dbd1ca51e975b.jpeg" alt=""><img src="https://img-blog.csdnimg.cn/img_convert/9760ccdc0f8923d9bc6bfceea23685cc.jpeg" alt="">

从量级上来看两者已经很接近，而且瑞幸正以可怕的增长速度扩张门店，以我家附近的商圈为例，去年还只有一家瑞幸，今年已经有三家。

星巴克无论从选址位置、开店成本、门店面积、店员数量上来说都比瑞幸要苛刻一些，瑞幸主打外卖+外带，这也是除市场需求因素外，瑞幸能快速扩张的原因。

### **星巴克分布全国Top20城市**

星巴克门店数量前五的城市是：上海、北京、杭州、深圳、广州。在前二十城市中，长三角有6个，珠三角有5个，京津冀2个。

<img src="https://img-blog.csdnimg.cn/img_convert/f2ae4583f09e652f14d59aa1f1f123de.jpeg" alt="">

上海的星巴克门店数量668，是第二名北京2倍之多，同时上海也是全球星巴克门店数量最多的城市，看来魔都人民对咖啡的喜爱名不虚传。

杭州的星巴克数量仅次与上海、北京，高于深圳、广州，杭州的互联网和电商从业者们也比较喜欢星巴克。

### **瑞幸分布全国Top20城市**

瑞幸门店数量前五的城市是：上海、北京、广州、深圳、杭州，与星巴克前五城市一样，但排序略有差异。

在前二十城市中，长三角有6个，珠三角有2个，京津冀2个。<img src="https://img-blog.csdnimg.cn/img_convert/81b30a8b0e08a3111116c7c3a9a645a9.jpeg" alt="">

星巴克主要聚集在沿海一二线城市，而瑞幸在内陆城市快速占领市场，瑞幸前20的城市中已经有了合肥、昆明、郑州，而星巴克前20里并没有出现这三个省会城市。

因此瑞幸门店的分布更加分散，没有过度集中在一线城市。

### **星巴克全国分布热力图**

通过星巴克门店热力图也能看到，红色高密度区主要集中在沿海地区，内陆则呈现点状式分布，比较稀疏。<img src="https://img-blog.csdnimg.cn/img_convert/901b11bd999ad27c0e394b72ef9931cf.jpeg" alt="">

### **瑞幸全国分布热力图**

瑞幸门店分布则更加均匀，除沿海地区，华中地区湖南、安徽、湖北、湖南等也有比较多的门店。<img src="https://img-blog.csdnimg.cn/img_convert/63aab3c0cd31c88f5a1db35f9ae5e8a2.jpeg" alt="">

### **星巴克上海分布热力图**

上海是全国咖啡消费需求最大的城市，我们看看星巴克门店在上海的分布情况。

整体上星巴克门店集中在上海市区内环范围，往外以点线式分散，郊区五大新城、浦东机场、虹桥枢纽也是较为集中的区域。

<img src="https://img-blog.csdnimg.cn/img_convert/bf71aee21e825a6fa322ebc98292cc2c.jpeg" alt="">

### **瑞幸上海分布热力图**

瑞幸在上海市区内环的集中度没有星巴克那么明显，整体数量上也少很多。<img src="https://img-blog.csdnimg.cn/img_convert/a9757b7db160ab90f041f738aad598c9.jpeg" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/b17cb4b58356e069e3e3348f1689d809.png" alt="">

### **Python数据分析**

下面再深入分析星巴克和瑞幸门店的关联关系，我们知道瑞幸咖啡是后起之秀，据说很多门店的选址依据主要看周边是否有星巴克。

那全国范围每个星巴克门店周边平均有多少个瑞幸门店呢？这次从方圆500米范围看看瑞幸在星巴克周边的聚集情况。

我们使用Python和其第三方库shapely来进行处理数据，shapely主要用来处理地理坐标数据。

**第一步：导入所需要的库**

```
# 导入相关库
import pandas as pd
import requests
import time 
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

```

**第二步：从API中抽取数据**

```
# 抽取星巴克和瑞幸门店数据，通过下秒机器人API调用
# 抽取星巴克门店数据
headers = {<!-- --> "x-token": "tk7a2980431688455e8976e4bad4d13d6a" }
starbucks_list = []
for i in range(1,10):
    response_1 = requests.get("http://app.chafer.nexadata.cn/openapi/v1/sheet/sht22nId5uouP2/records?size=500&amp;page={0}".format(i), headers = headers)
    starbucks = response_1.json()['data']['list']
    starbucks = pd.DataFrame(starbucks)
    time.sleep(1)
    starbucks_list.append(starbucks)
starbucks = pd.concat(starbucks_list)
# 抽取瑞幸门店数据
luckin_list =[]
for j in range(1,9):
    response_2 = requests.get("http://app.chafer.nexadata.cn/openapi/v1/sheet/sht22nIeomVmYy/records?size=500&amp;page={0}".format(j), headers = headers)
    luckin = response_2.json()['data']['list']
    luckin = pd.DataFrame(luckin )
    luckin_list.append(luckin)
    time.sleep(1)

```

**第三步：判断星巴克门店方圆500米范围内的瑞幸门店数**

```
# 根据星巴克咖啡店坐标绘制半径为XX米的地理区域
def circle(data,radius):
    # radius 表示区域半径
    # 给定地理坐标
    center_latitude = float(data['维度'])
    center_longitude = float(data['经度'])
    # 创建圆形区域
    center_point = Point(center_longitude, center_latitude)
    circle = center_point.buffer(radius/111300)
    # 创建多边形区域
    polygon = Polygon(circle.exterior)
    return polygon

# 根据经纬度构建坐标点
def point(data):
    # 给定地理坐标
    center_latitude = float(data['维度'])
    center_longitude = float(data['经度'])
    # 创建坐标点
    center_point = Point(center_longitude, center_latitude)
    return center_point

# 判断瑞幸咖啡店是否在星巴克方圆500m范围内
def is_inside(data):
    polygon = data['Polygon']
    # 判断坐标是否在区域内
    n = 0
    luckin_city = luckin[luckin['城市']==data['城市']]
    for point in luckin_city['Point']:
        is_inside = polygon.contains(point)
        # 打印判断结果
        if is_inside:
            n = n + 1
    return n

# 根据星巴克门店坐标位置绘制方圆半径为500米的地理区域
starbucks['Polygon'] = starbucks.apply(circle,axis=1,args=(500,))

# 根据瑞幸门店经纬度构建坐标点
luckin['Point'] = luckin.apply(point, axis=1)

# 判断瑞幸门店是否在星巴克门店方圆500米范围内
starbucks['Luckin_numbers'] = starbucks.apply(is_inside, axis=1)

```

**数据处理后如下：**

<img src="https://img-blog.csdnimg.cn/img_convert/5a3447f1290179058a15a07644d60454.jpeg" alt="">

**第四步：分析数据**
1. 方圆500米范围内，全国平均每个星巴克门店周边有0.6个瑞幸门店
```
# 方圆500米范围内，全国平均每个星巴克门店周边有0.6个瑞幸门店
starbucks['Luckin_numbers'].mean() 

```

输出：0.6
1. 方圆500米范围内，全国最多的星巴克门店周边有7个瑞幸门店
```
# 方圆500米范围内，最多的星巴克门店周边有7个瑞幸门店
starbucks['Luckin_numbers'].max()

```

输出：7
1. 方圆500米范围内，星巴克门店周边平均瑞幸门店数各城市排名，最多的是临沂市，平均每个星巴克门店周边有1.8个瑞幸门店
```
# 方圆500米范围内，星巴克门店周边平均瑞幸门店数各城市排名
# 最多的是临沂市平均每个星巴克门店周边有1.8个瑞幸门店
city_list = []
for city in pd.unique(starbucks['城市']):
    avg_luckin_numbers = starbucks[starbucks['城市']==city]['Luckin_numbers'].mean()
    starbucks_nums = starbucks[starbucks['城市']==city]['名称'].count()
    city_list.append([city,starbucks_nums,avg_luckin_numbers])

df = pd.DataFrame(city_list,columns=['city','starbucks_nums','avg_luckin_numbers'])
df.sort_values(by=['avg_luckin_numbers'],axis=0,ascending=False)

```

输出：

<img src="https://img-blog.csdnimg.cn/img_convert/798d6dab8ead781b92adf3d01251f578.jpeg" alt="">

看来瑞幸确实与星巴克有着不解的缘分，难怪我们会看到星巴克周边那么多的瑞幸门店。

星巴克门店养成了周边用户喝咖啡的习惯，或者说这里喝咖啡的用户比较多，星巴克才来这里开店，那么在星巴克周边再开瑞幸咖啡，就可以低成本获取一大波潜在用户，尽管有竞争，还是非常值得的。

<img src="https://img-blog.csdnimg.cn/img_convert/56ab8d16d4068a8e0febf2c09462f4fa.png" alt="">

### **总 结**

我们通过可视化看板和Python数据分析展示了星巴克和瑞幸咖啡门店的区域分布、关联关系，其实还有很多值得分析挖掘的地方。

比如说有些城市星巴克门店周边的瑞幸门店非常少，或者几乎没有，那原因是什么？是潜在的机会还是要规避的深坑？

如果大家有兴趣可以试一试。

## 关于Python学习指南

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后给大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、自动化办公等学习教程。带你从零基础系统性的学好Python！</mark>

#### 👉Python所有方向的学习路线👈

Python所有方向路线就是把Python常用的技术点做整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取）**</mark>

<img src="https://img-blog.csdnimg.cn/3c4ee87941694f3789398db3d52a2637.png#pic_center" alt="在这里插入图片描述">

#### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。

<img src="https://img-blog.csdnimg.cn/64c89bf6293d4699bf7ee8f34b9e69fd.png#pic_center" alt="在这里插入图片描述">

#### <mark>温馨提示：篇幅有限，已打包文件夹，获取方式在：文末</mark>

#### 👉Python70个实战练手案例&amp;源码👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/2017b67544f94e8898db755e2703224a.png#pic_center" alt="在这里插入图片描述">

#### 👉Python大厂面试资料👈

我们学习Python必然是为了找到高薪的工作，下面这些面试题是来自**阿里、腾讯、字节等一线互联网大厂**最新的面试资料，并且有阿里大佬给出了权威的解答，刷完这一套面试资料相信大家都能找到满意的工作。

<img src="https://img-blog.csdnimg.cn/3055c54d3224495987c589f150324d73.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/b0751719fe914aec8c8d09f62f772e44.png#pic_center" alt="在这里插入图片描述">

#### 👉Python副业兼职路线&amp;方法👈

学好 Python 不论是就业还是做副业赚钱都不错，但要学会兼职接单还是要有一个学习规划。

<img src="https://img-blog.csdnimg.cn/01bcd7cbfd6d43fb85ef410766735154.png#pic_center" alt="在这里插入图片描述">

**👉** **这份完整版的Python全套学习资料已经上传，朋友们如果需要可以扫描下方CSDN官方认证二维码或者点击链接免费领取**【**`保证100%免费`**】

<font color="red">**点击免费领取《CSDN大礼包》： 安全链接免费领取**</font>
