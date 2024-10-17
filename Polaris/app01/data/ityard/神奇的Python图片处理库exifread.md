
--- 
title:  神奇的Python图片处理库exifread 
tags: []
categories: [] 

---
>  
  来源：挣扎的蓝藻 
  https://lanzao.blog.csdn.net/article/details/103080034 
 

【导语】：用 python 怎样获得图片的GPS信息？今天推荐一下 exifread 这个神奇的库，不仅仅是 GPS 信息，几乎能能获得图片的所有信息，快进来看看！！

要怎样获得拍摄图片的GPS呢？这里我们需要exifread 库，这个就是用来提取 GPS 信息的。直接 pip install exifread 来安装就好了。

其实不仅能获得GPS信息，图片的几乎所有信息都能获得。exifread的作用其实是代替了查看图片属性！如下图：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcllZZ2dqa0V3UnlFWmZOb1lVVXBKTm1vNmRHS1IwTjQzamtpYWljZDVTRHpNS2lhbTg4dDlkTUVHelFjb01zR1BqRlNNRkMwMkVrRnlpY2cvNjQw?x-oss-process=image/format,png">

这里用在三亚拍的骆驼照片来做个演示，看看能不能定位到三亚。

注：如果图片被压缩了的话会破坏里面的二进制信息，肯定就不能提取了哦！

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcllZZ2dqa0V3UnlFWmZOb1lVVXBKTlpzOWtJWXpBRldJSWN0ZkNFS2txdmZ2S3F0TzJlM3djang5WDRKRkx5czFnaWFyaWNESUV1cVZnLzY0MA?x-oss-process=image/format,png">

原理是： 先把图片以二进制的格式读取出来，然后通过 exifread 库把里面的 GPS 信息提取出来，再以特定的格式打印出来，最后直接复制里面的经纬度信息，在支持通过经纬度来查位置的地图里一查就能定位到了。

exifread库读取图片的二进制示例：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcllZZ2dqa0V3UnlFWmZOb1lVVXBKTlhiNVR2bHdTa0MxY1RXVTRpY1BNWVFIRU5FQ1pDVjhDYVhpYWxjaWJTUWlidjN5S2JpYVRTalFZWkR3LzY0MA?x-oss-process=image/format,png">

具体代码如下

```
import exifread
import re


# 读取图片为二进制格式
f = open("luotuo.JPG","rb")
tags = exifread.process_file(f)


# GPS信息
GPS = {}


# 拍摄时间
Data = ""


for tag,value in tags.items():
    # 获取纬度信息
    if re.match('GPS GPSLatitude', tag):
        try:
            match_result=re.match('\[(\w*), (\w*), (\w.*)/(\w.*)\]', str(value)).groups()
            GPS['纬度'] = str(int(match_result[0])) + " " + str(int(match_result[1])) + " " + str(int(match_result[2])/int(match_result[3]))
        except:
            GPS['纬度'] = str(value)
    # 获取纬度信息
    elif re.match('GPS GPSLongitude', tag):
        try:
            match_result=re.match('\[(\w*), (\w*), (\w.*)/(\w.*)\]',str(value)).groups()
            GPS['经度'] = str(int(match_result[0])) + " " + str(int(match_result[1])) + " " + str(int(match_result[2])/int(match_result[3]))
        except:
            GPS['经度'] = str(value)
    # 获取高度
    elif re.match('GPS GPSAltitude', tag):
        GPS['高度'] = str(value)
    # 获取拍摄时间
    elif re.match('Image DateTime', tag):
        Data = str(value)


# 打印信息
print("纬 经 度：" + GPS['纬度'] + "," + GPS['经度'])
print("拍摄时间：" + Data)

```

如图所示，读取后的纬经度信息直接就显示出来了

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcllZZ2dqa0V3UnlFWmZOb1lVVXBKTjNEZlc5dkxqcW5UWDFxc2N2TGxqaWFpYjg5d1BOM2lhMGF0a1FiaWJHSUc4YzBrRGVuZEtxTXNMRHcvNjQw?x-oss-process=image/format,png">

拓展1： 后期我们可以通过百度提供的 API 接口直接把经纬度转换为具体的地点。大家可以自己来尝试一下！

拓展2： 当然，你右键图片属性的详细信息里也有这些信息。

如果想保密的话，直接点击删除属性和个人信息就能能把信息删掉。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcllZZ2dqa0V3UnlFWmZOb1lVVXBKTnZGSlA5bkNaMVNvQ3RVanJqbVJxbU1DUUszNmxpYTBlWERjakFyNjBJaWNpYnZocEZ3amVWWUZ5QS82NDA?x-oss-process=image/format,png">

PS：如果觉得分享内容有一些帮助，欢迎大家随手分享、点赞、在看。

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcGFPWnF1SzE4eGM0V2JIT05pYmVoZU9HTXNJMUdIR0Z1UmpycUxpY2lhNld1aWNxaWNNWTZuY2t2Y21pYUZaWUcxWnM4Zjd5bnBwRTJaR2JFQS82NDA?x-oss-process=image/format,png">
