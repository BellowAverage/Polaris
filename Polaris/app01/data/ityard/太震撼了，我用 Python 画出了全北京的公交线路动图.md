
--- 
title:  太震撼了，我用 Python 画出了全北京的公交线路动图 
tags: []
categories: [] 

---
今天教大家用pyecharts制作北京市公交线路动态图，这应该是全网唯一一篇能正常运行的教程

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9JNGdZbktRZ1YxVmFEQkdNOFFUdmtsdWVXTUd0MWpGaWJkMnRGU1ppY1U2VWdiVjg3aEdTVVJpYVNBMWZManRRNmJ5SHQxaWJEaWFCa0U1N0ZtaHdoMlBJR1p3LzY0MA?x-oss-process=image/format,png">

## 一、获取百度秘钥

首先，本项目需要引用百度地图api，所以需要先注册获取百度开放平台秘钥，地址为：

```
http://lbsyun.baidu.com/apiconsole/key#

```

有账号的直接登录，没账号的先注册一下再登录，登录完成后，依次点击控制台-应用管理-我的应用-创建应用：

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9JNGdZbktRZ1YxVmFEQkdNOFFUdmtsdWVXTUd0MWpGaWJrQ0FjV2pXdm92U3E5bmZncFY0N1h3eFQ1MXhaYTRmU2VoZUY3VHM4NW1mQmRma3doWllDY3cvNjQw?x-oss-process=image/format,png">

访问应用（AK）下即是我们这次所需的秘钥

## 二、整理公交车地理数据

这个公交车地理数据着实有点坑，echarts官方给的数据长这样：

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9JNGdZbktRZ1YxVmFEQkdNOFFUdmtsdWVXTUd0MWpGaWJZRXJ5WnU0amM2ejdGdkRKUHMwbG1tbGVXS2p5UXNic1pMWlNZVEFjdmxmejRnUVB6Tk1iZ3cvNjQw?x-oss-process=image/format,png">

看起来好像密码，真让人头大

只好硬着头皮去研究一下官方代码：

```
$.getJSON(uploadedDataURL, function(data) {
    var hStep = 300 / (data.length - 1);
    var busLines = [].concat.apply([], data.map(function (busLine, idx) {
        var prevPt;
        var points = [];
        for (var i = 0; i &lt; busLine.length; i += 2) {
            var pt = [busLine[i], busLine[i + 1]];
            if (i &gt; 0) {
                pt = [
                    prevPt[0] + pt[0],
                    prevPt[1] + pt[1]
                ];
            }
            prevPt = pt;

            points.push([pt[0] / 1e4, pt[1] / 1e4]);
        }
        return {
            coords: points,
            lineStyle: {
                normal: {
                    color: echarts.color.modifyHSL('#5A94DF', Math.round(hStep * idx))
                }
            }
        }

```

这是一段java代码，如果看不懂就不要看了，大致意思是把数据都除以10000，然后列表奇数位依次相加、偶数位依次相加，两两一组即为各个公交站点地理坐标，每个列表代表1个线路。

用python实现以上过程，代码如下：

```
import json
with open('1.json','r') as f:
    datas=json.load(f)
result=[]
for data in datas:
    data = [float(i / 10000) for i in data]
    a=[]
    for i in range(2,len(data),2):
        data[i]=data[i-2]+data[i]
        data[i+1] = data[i - 1] + data[i+1]
        a.append([data[i],data[i+1]])
    result.append(a)

```

感觉还是python的代码要少一些

## 三、画图

这里给大家提供两种方式

### 1.带地图背景的

```
BAIDU_MAP_AK = "输入你自己的秘钥"

c = (
    BMap(init_opts=opts.InitOpts(width="1200px", height="800px"))
    .add_schema(
        baidu_ak=BAIDU_MAP_AK,
        center=[116.40, 40.04],
        zoom=10,
        is_roam=True,
    )
    .add(
        "",
        type_="lines",
        is_polyline=True,
        data_pair=result,
        linestyle_opts=opts.LineStyleOpts(opacity=0.2, width=0.5,color='red'),
        # 如果不是最新版本的话可以注释下面的参数（效果差距不大）
        progressive=200,
        progressive_threshold=500,
    )
)
c.render_notebook()


```

<img alt="" height="482" src="https://img-blog.csdnimg.cn/20201014204044748.gif" width="639">

### 2.不带地图背景的

```
BAIDU_MAP_AK = "输入你自己的秘钥"

c = (
    BMap(init_opts=opts.InitOpts(width="1200px", height="800px"))
    .add_schema(
        baidu_ak=BAIDU_MAP_AK,
        center=[116.40, 40.04],
        zoom=10,
        is_roam=True,
        map_style={
            "styleJson": [
                {
                    "featureType": "water",
                    "elementType": "all",
                    "stylers": {"color": "#031628"},
                },
               
           “省略部分修饰代码”
    )
    .add(
        "",
        type_="lines",
        is_polyline=True,
        data_pair=result,
        linestyle_opts=opts.LineStyleOpts(opacity=0.2, width=0.5,color='red'),
        # 如果不是最新版本的话可以注释下面的参数（效果差距不大）
        progressive=200,
        progressive_threshold=500,
    )
)
c.render_notebook()

```

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9JNGdZbktRZ1YxVmFEQkdNOFFUdmtsdWVXTUd0MWpGaWIxWDIzam1VQ1E5YlhXQWhBYUxnQjdaM3NFOHE5YVdSV0s5OEdCY3g5U3pyVXl5UzlURVlIeHcvNjQw?x-oss-process=image/format,png">

大家觉得哪一种更好看呢？欢迎在留言区留言

公交线路数据和完整代码在公众号后台回复**公交图**获取

&lt; END &gt;

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcGFPWnF1SzE4eGM0V2JIT05pYmVoZU9HTXNJMUdIR0Z1UmpycUxpY2lhNld1aWNxaWNNWTZuY2t2Y21pYUZaWUcxWnM4Zjd5bnBwRTJaR2JFQS82NDA?x-oss-process=image/format,png">

分享或在看是对我最大的支持
