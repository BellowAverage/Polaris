
--- 
title:  YYDS，用Python实现了个人手机定位 
tags: []
categories: [] 

---
来源：快学Python

本文作者依托《交通时空大数据分析、挖掘与可视化》一书中所介绍的相关技术开发了Python开源库TransBigData，进行一次对手机信令数据的处理、分析和挖掘。

### TransBigData简介

TransBigData是一个为交通时空大数据处理、分析和可视化而开发的Python包。TransBigData为处理常见的交通时空大数据（如出租车GPS数据、共享单车数据和公交车GPS数据等）提供了快速而简洁的方法。

目前，TransBigData主要提供以下方法：

(1)数据预处理：对数据集提供快速计算数据量、时间段、采样间隔等基本信息的方法，也针对多种数据噪声提供了相应的清洗方法。

(2)数据栅格化：提供在研究区域内生成、匹配多种类型的地理栅格快学Python（矩形、三角形、六边形及geohash栅格）的方法体系，能够以向量化的方式快速算法将空间点数据映射到地理栅格上。

(3)数据可视化：基于可视化包keplergl，用简单的代码即可在Jupyter Notebook上交互式地可视化展示数据。

(4)轨迹处理：从轨迹数据GPS点生成轨迹线型，轨迹点增密、稀疏化等。

(5)地图底图、坐标转换与计算：加载显示地图底图与各类特殊坐标系之间的坐标转换。

(6)特定处理方法：针对各类特定数据提供相应处理方法，如从出租车GPS数据中提取订单起讫点，从手机信令数据中识别居住地与工作地，从地铁网络GIS数据构建网络拓扑结构并计算最短路径等。

TransBigData可以通过pip或者conda安装，在命令提示符中运行下面代码即可安装：

```
pip install -U transbigdata
```

安装完成后，在Python中运行如下代码即可导入TransBigData包。

```
import transbigdata as tbd
```

### 手机信令数据读取

手机信令数据是指手机与通信基站之间交换的信息，包括位置、通信时长、通信频次等数据。这些数据可以用于分析用户的出行行为、生活习惯等，也可以用于城市交通管理、商业营销等领域。

使用Python开源库`TransBigData`可以快速高效地处理、分析、挖掘手机信令数据，识别出行和停留、居住地与工作地等信息，并绘制活动图以便于分析。

首先，我们将使用Python的pandas库来读取数据。Pandas是一款功能强大的数据处理库，它提供了灵活的数据结构和数据分析工具，可以轻松地对各种数据进行操作和分析。我们将使用Pandas读取包含手机信令数据的CSV文件，并将其存储在一个Pandas的数据框中。

我们需要将时间字段转换为正确的格式，以便进行后续的数据处理。我们使用Pandas的to_datetime函数将时间字段转换为datetime格式。然后后，我们按照时间顺序对数据进行排序，以便进行后续的数据处理：

```
import pandas as pd
import transbigdata as tbd
data = pd.read_csv(r'data/mobiledata_sample.csv')
#确保时间列准确识别（很重要）
data['stime'] = pd.to_datetime(data['stime'], format='%Y%m%d%H%M')
data = data.sort_values(by = ['user_id','stime'])
data.head()
```

结果如下图所示。

<img src="https://img-blog.csdnimg.cn/img_convert/83317b25796717e2dfca55dfab4b6cb9.png" alt="83317b25796717e2dfca55dfab4b6cb9.png">

### 识别出行和停留

在处理手机数据时，识别出行和停留是很重要的一步。基于手机识别出行和活动可以进一步进行路径分析、出行模式分析、人群分析等工作。

活动：手机数据通过连续地追踪个体的出行轨迹，可以构建出个体的出行链信息，一般来说，如果一个手机用户在某个位置停留了超过30分钟，我们可以认为用户在这里发生了活动。

出行：用户产生的连续两个活动如果产生的地理位置不同，则可以认为用户发生了出行行为。出行的起点为连续两个活动中前一个活动的地理位置，出行的开始时间为前一个活动结束的时间，出行的终点则为后一个活动的地理位置，出行的结束时间则为后一个活动开始的时间。简而言之，用户在活动点与活动点之间的移动，视为用户的出行。

使用TransBigData提供的手机信令数据处理方法，可以先将数据对应至栅格，将同一个栅格内的数据视为在同一个位置，以避免数据定位误差导致同一位置被识别为多个。然后，可以使用`tbd.mobile_stay_move`函数从手机数据中识别出行和停留:

```
#获取栅格参数
params = tbd.area_to_params([121.860, 29.295, 121.862, 29.301], accuracy=500)
#从手机数据中识别出行和停留
stay,move = tbd.mobile_stay_move(data,params,col = ['user_id','stime','longitude', 'latitude'])结果如下所示。
```

### 识别居住地与工作地

通过移动通信数据识别出用户的职住信息是研究的基础工作之一。TransBigData中，以停留活动点为依据，用`tbd.mobile_identify_home`方法可以识别居住地，用`tbd.mobile_identify_work`则可以识别工作地。具体规则为：
- 居住地识别规则为夜晚时段停留最长地点- 工作地识别规则为工作日白天时段停留最长地点（每日平均时长大于minhour）。
具体使用方法如下：

```
#识别居住地
home = tbd.mobile_identify_home(stay, col=['user_id','stime', 'etime','LONCOL', 'LATCOL','lon','lat'], start_hour=8, end_hour=20 )
home.head()
```

结果输出：

<img src="https://img-blog.csdnimg.cn/img_convert/b09a547a48ac94b0d8979ee3a7a88578.png" alt="b09a547a48ac94b0d8979ee3a7a88578.png">

```
#识别工作地
work = tbd.mobile_identify_work(stay, col=['user_id', 'stime', 'etime', 'LONCOL', 'LATCOL','lon','lat'], minhour=3, start_hour=8, end_hour=20,workdaystart=0, workdayend=4)
work.head()
```

<img src="https://img-blog.csdnimg.cn/img_convert/c8980d2a023829af38ac970266b056d1.png" alt="c8980d2a023829af38ac970266b056d1.png">

### 绘制活动图

为了加深对手机用户的具体活动情况的理解，我们可以用TransBigData提供的tbd.mobile_plot_activity方法将用户的每日活动情况绘制出来观察，具体代码如下：

```
#绘制某一用户的活动图，不同颜色代表不同活动
uid = 'fcc3a9e9df361667e00ee5c16cb08922'
tbd.mobile_plot_activity(stay[stay['user_id']==uid],figsize = (20, 5))
```

输出结果：

<img src="https://img-blog.csdnimg.cn/img_convert/85c1617f5556b5532fd4ce3e2e591876.png" alt="85c1617f5556b5532fd4ce3e2e591876.png">

上图中绘制的是一个手机用户在观测时间段内每一天的活动情况，横坐标为日期，纵坐标为时间，同一个位置的活动则以同样的颜色显示。从活动图中我们可以很清晰地看到这个用户每一个活动的开始与结束时间。

<img src="https://img-blog.csdnimg.cn/img_convert/b8dca16b4db56a2c20a7421b7cc1308e.jpeg" alt="b8dca16b4db56a2c20a7421b7cc1308e.jpeg">
- - - - - 