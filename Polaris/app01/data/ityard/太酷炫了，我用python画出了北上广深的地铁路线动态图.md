
--- 
title:  太酷炫了，我用python画出了北上广深的地铁路线动态图 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/0368050789b3ebff12002c96e1f5c96e.png">

今天教大家用python制作北上广深——地铁线路动态图，这可能是全网最全最详细的教程了。

### 坐标点的采集

小五之前做过类似的地理可视化，不过都是使用网络上收集到的json数据。但很多数据其实是过时的，甚至是错误/不全的。所以我们最好还是要自己动手，丰衣足食（爬虫大法好）。

打开高德地图的地铁网页，`http://map.amap.com/subway/index.html?&amp;1100`

可以轻松得到北京地铁数据的接口，同理也把其他三个城市的url复制出来。

有了api，解析json即可获得数据????

```
url = 'http://map.amap.com/service/subway?_1615466846985&amp;srhdata=1100_drw_beijing.json'
response = requests.get(url)
result = json.loads(response.text)
stations = []
for i in result['l']:
    station = []
    for a in i['st']:
        station.append([float(b) for b in a['sl'].split(',')])
    stations.append(station)
pprint.pprint(stations)

```

`pprint`格式化打印结果，方便预览

### 坐标系的转换

其实我之前有看到类似地理可视化文章，结果自己一试发现缩小看还行，一放大就会发现坐标点飘出二里地了????

正好拿上文获取的坐标点给大家演示一下，看看同样的经纬度在不同地图里的地理位置????

????可以看到该经纬度在高德地图里指的是`金安桥地铁站`，然而在百度地图里，地理位置则指向了几公里外的某大厦。

为什么会出现这个问题呢？

其实是不同地图产品的地理坐标系导致的。

下面说一下常见的地理坐标系：`地球坐标系`是国际通用坐标系，比较适合国际地图可视化。不过在我国范围内，一般不会直接使用它，而是使用由国家测绘局在其基础上加密的`火星坐标系`。另外还有公司会在`火星坐标系`上进行二次加密，比如百度坐标系、搜狗坐标系等。

我网上找到了一张图，来自知乎@师大Giser<sup>[1]</sup>????

上图可以作为参考，具体原因我们就不细究了。重点是什么，如何利用python转换坐标系？

例如在本文中，我们是在高德地图中获得的坐标点集合，那么也就是使用的是`GCJ-02`坐标系。而下文可视化中会调用百度地图的接口，也就是需要在`BD-09`坐标系中进行可视化。

幸好我在网上搜到了`GCJ-02`转`BD-09`的公式，并用python实现此公式：

```
#需要的两个常量先设置好
pi = 3.1415926535897932384 #π
r_pi = pi * 3000.0/180.0

def gcj02_bd09(lon_gcj02,lat_gcj02):
    b = math.sqrt(lon_gcj02 * lon_gcj02 + lat_gcj02 * lat_gcj02) + 0.00002 * math.sin(lat_gcj02 * r_pi)
    o = math.atan2(lat_gcj02 , lon_gcj02) + 0.000003 * math.cos(lon_gcj02 * r_pi)
    lon_bd09 = b * math.cos(o) + 0.0065
    lat_bd09 = b * math.sin(o) + 0.006
    return [lon_bd09,lat_bd09]

```

这样我们就写好了一个python将`GCJ-02`坐标系转成`BD-09`的函数，调用这个函数，就可以将高德地图获取的坐标点集合统统转换成百度坐标系。

```
result = []
for station in stations:
    result.append([gcj02_bd09(*point) for point in station])

```

以其中一个坐标点为例：

到此，我们的前期数据工作终于准备齐了。

当然，如果我们一开始获取的数据就是`BD_09(百度地图)`坐标系的，转换这步就可以直接省略喽~

### 地理可视化

接下来就要利用pyecharts中的`BMap`来可视化了，不过需要先获取百度开放平台的密钥。

百度地图开放平台????http://lbsyun.baidu.com/apiconsole/key#/home

登录百度账户，查看应用管理-我的应用。点击创建应用，全部默认随便创建。

复制????上图中的访问应用（AK），保存好，这在后续的可视化中将要用到。

我们使用pyecharts中的`BMap`，先导入模块

```
from pyecharts.charts import BMap 
from pyecharts import options as opts 
from pyecharts.globals import BMapType, ChartType 

```

在导入数据（也就是上文转换后的经纬度数据`result`）后，可以调整一下参数以及增添一些控件。

????关键参数都做了注释，方便大家查看（其中`百度appkey`记得替换成自己的）

```
map_b = (
    BMap(init_opts = opts.InitOpts(width = "800px", height = "600px"))
    .add_schema(
        baidu_ak = '****************', #百度地图开发应用appkey
        center = [116.403963, 39.915119], #当前视角的中心点
        zoom = 10, #当前视角的缩放比例
        is_roam = True, #开启鼠标缩放和平移漫游
    )
    .add(
        series_name = "",
        type_ = ChartType.LINES, #设置Geo图类型
        data_pair = result, #数据项
        is_polyline = True, #是否是多段线，在画lines图情况下#
        linestyle_opts = opts.LineStyleOpts(color = "blue", opacity = 0.5, width = 1), # 线样式配置项
    )
    .add_control_panel(
        maptype_control_opts = opts.BMapTypeControlOpts(type_ = BMapType.MAPTYPE_CONTROL_DROPDOWN), #切换地图类型的控件
        scale_control_opts = opts.BMapScaleControlOpts(), #比例尺控件
        overview_map_opts = opts.BMapOverviewMapControlOpts(is_open = True), #添加缩略地图
        navigation_control_opts = opts.BMapNavigationControlOpts() #地图的平移缩放控件
    )
)

map_b.render(path = 'subway_beijing.html')

```

>  
  注：因为是北京地图，所以设置天安门的经纬度[116.403963, 39.915119]为视角中心。 
 

让我们看一下可视化的结果吧：

????上图中的四个角都有控件，这是我们在代码中添加了控件参数，它们分别为：地图的平移缩放控件、切换地图类型的控件、缩略地图、以及比例尺控件。

是不是还阔以

<img src="https://img-blog.csdnimg.cn/img_convert/6fdb2281bdeefe4984b63d80e49d3c6c.png">

### 其他效果展示

上文已经基本实现了用python制作地铁线路动态图。不过大家都用同一种颜色背景制作动态图的话，就显得就太单调了。

正好我们还要绘制其他三个城市的地铁图，那就调整一些参数，看看能获得什么效果吧？

#### 上海-变色

上海的数据接口是：

```
http://map.amap.com/service/subway?_1615467204533&amp;srhdata=3100_drw_shanghai.json

```

上海市的地铁图我们改一下`line`的颜色，可在参数`linestyle_opts`中修改color。

????下图中的线条颜色是`lilac`——浅紫色

#### 广州-卫星图

广州的数据接口是：

```
http://map.amap.com/service/subway?_1615494419554&amp;srhdata=4401_drw_guangzhou.json

```

其实我们还可以调整可视化背景为卫星图。不过这一操作并不需要额外写代码，因为刚刚上文提到我在调整参数时添加了4个控件，其中右上角的就可以直接切换地图类型，具体操作见下图。

#### 深圳-个性化配色

深圳的数据接口是：

```
http://map.amap.com/service/subway?_1615494473615&amp;srhdata=4403_drw_shenzhen.json

```

如果不满意百度地图设置好的地图背景，我们还可以个性化设置`mapStyle`，调整自己的配色`styleJson`。

下图就是小五参考网上公开的配色方案制作的，大家也可以用来参考https://blog.csdn.net/weixin_41290949/article/details/106379134<sup>[2]</sup>

### 小结

今天带大家学习了如何利用python绘制一线城市的地铁线路动图。

主要分为四个部分：坐标点的采集、坐标系的转换、利用`pyecharts`地理可视化、其他效果展示。

如果你读完本文觉得有收获，希望可以给文章右下角点个赞????

#### 参考资料

[1]

地学大数据:知乎@师大Giser

百度地图开发mapStyle个性化地图styleJson的配色解决方案: **https://blog.csdn.net/weixin_41290949/article/details/106379134**

#### 本文代码下载

在公众号**Python小二**后台回复**地铁** ，即可获取全部代码！

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/871ebb610e498d9677ee841b15acc74b.gif">

微信扫码关注，了解更多内容
