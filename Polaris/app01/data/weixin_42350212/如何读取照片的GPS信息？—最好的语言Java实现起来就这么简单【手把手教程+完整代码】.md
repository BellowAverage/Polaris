
--- 
title:  如何读取照片的GPS信息？—最好的语言Java实现起来就这么简单【手把手教程+完整代码】 
tags: []
categories: [] 

---
>  
 大家好，我是Lex 喜欢欺负超人那个Lex 
 上次，我们用Python读取照片的GPS信息，可以获取拍摄时间、手机型号等信息，还可以对 
 拍摄地点进行精确定位。Java表示不服~~~ 
 今日重点：用Java读取照片的拍摄时间、GPS 以及手机型号等等信息 
 带你一步步实现功能，文末有完整源码哦【建议收藏】 


### 事情是这样的

上次用python对照片进行GPS读取，如下 ↓ ↓ ↓



【当然是选择原谅她啊】Python破解"通宵加班"女友的秘密

 今天决定，露出我的真面目

用世界上最好的语言—Java（可能会挨喷）

来实现一遍这个功能

<img alt="" height="203" src="https://img-blog.csdnimg.cn/20210704210337767.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="287">

功能大体介绍一下就是：

通过脚本分析照片，对照片的拍摄地点进行GPS读取

另外，还可以拿到拍摄时间、手机型号等等信息。

<img alt="" height="179" src="https://img-blog.csdnimg.cn/20210704215715643.png" width="196">

### 先上效果

从微信某个群里随便找了一位美女发的照片

<img alt="" height="485" src="https://img-blog.csdnimg.cn/20210705145428994.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="331">

**Java对照片进行分析，效果如下**

<img alt="" height="500" src="https://img-blog.csdnimg.cn/20210704213423824.gif" width="785">

**获得结果如下：**

```
{海拔=0 metres, 手机=Xiaomi, 纬度=24.41046111111111, 型号=MI MAX, 经度=103.41424722222223, 拍摄时间=2018:12:01 16:37:32, 
拍摄地点=中国  云南省 红河哈尼族彝族自治州 xx市 XXX路 XXX号 温泉XXXX}
经纬度：24.41046111111111,103.41424722222223
拍摄时间：2018:12:01 16:37:32
手机型号：Xiaomi MI MAX
拍摄地点：中国  云南省 红河哈尼族彝族自治州 弥勒市 XXX路 XXX号 温泉XXX酒店
{"status":0,"result":{"location":{"lng":103.42283328917563,"lat":24.413805252378915},
"formatted_address":"云南省红河哈尼族彝族自治州弥勒市XXX路","business":"","addressComponent":
{"country":"中国","country_code":0,"country_code_iso":"CHN","country_code_iso2":"CN",
"province":"云南省","city":"红河哈尼族彝族自治州","city_level":2,"district":"弥勒市","town":"","town_code":"","adcode":"532504","street":"温泉路","street_number":"","direction":"","distance":""},"cityCode":107}}
```

emmm，不好过多描述

### Java实现方法

#### 1、引入相关jar包

这里需要引入两个jar包，用于读取照片的exif信息，里面包含照片的完整信息。

资源下载，放在最后啦。

<img alt="" height="62" src="https://img-blog.csdnimg.cn/2021070421040648.png" width="288">

#### 2、读取Exif原始信息

首先利用jar包工具，

将照片里的Exif原始信息读取出来。

**完整代码如下：**

```
public static HashMap&lt;String, Object&gt; readPicInfo(String file_path) {
	HashMap&lt;String, Object&gt; map = new HashMap&lt;String,Object&gt;();
	Tag tag = null;
    File jpegFile = new File(file_path);
    Metadata metadata;
    try {
        metadata = JpegMetadataReader.readMetadata(jpegFile);
        Iterator&lt;Directory&gt; it = metadata.getDirectories().iterator();
        while (it.hasNext()) {
            Directory exif = it.next();
            Iterator&lt;Tag&gt; tags = exif.getTags().iterator();
            while (tags.hasNext()) {
                tag = (Tag) tags.next();
                System.out.println(tag.getTagName()+"--"+tag.getDescription());
            }
        }
    } catch (JpegProcessingException e) {
        e.printStackTrace();
    } catch (IOException e) {
        e.printStackTrace();
    }
	return map;
}
public static void main(String[] args) {
        //传入照片的绝对路径
	readPicInfo("C:\\Users\\pacer\\Desktop\\img\\others\\10.jpg");
}

```

我们来看一下，能获得那些信息：

拍摄的手机型号、GPS精确位置、拍摄时间、像素、修改日期

甚至包括，拍摄地点的海拔信息都是有的。

<img alt="" height="828" src="https://img-blog.csdnimg.cn/20210704211025641.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="965">

<img alt="" height="389" src="https://img-blog.csdnimg.cn/20210704211055341.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="477">

#### 3、GPS格式转换

我们通过exif读取的GPS信息，是类似于度、分、秒这种格式的。

我们需要将GPS信息通过计算转换成十进制的数字位数，

这样才可以调用百度地图API或者其他的地图API来将GPS信息转换为地理位置信息。

```
/***
 * 经纬度坐标格式转换
 * @param Gps
 */
public double latitude_and_longitude_convert_to_decimal_system(String Gps) {
	String a = Gps.split("°")[0].replace(" ", "");
	String b = Gps.split("°")[1].split("'")[0].replace(" ", "");
	String c = Gps.split("°")[1].split("'")[1].replace(" ", "").replace("\"", "");
	double gps_dou = Double.parseDouble(a)+Double.parseDouble(b)/60 + Double.parseDouble(c)/60/60;
	return gps_dou;
}
```

通过这个函数，我们将经纬度信息转换为10进制数字信息。

<img alt="" height="149" src="https://img-blog.csdnimg.cn/20210704211654890.png" width="511">

#### 4、调用地图API将GPS坐标转换为地理位置

我们通过exif原始信息，拿到的是一串地理坐标数字。

如果想要转换为具体的地址信息，那么就需要通过各大地图API来进行转换，

小伙伴们可以自己去免费注册一个百度地图API，然后通过调用它提供的接口，

就可以将传入的GPS坐标值，转换为地址信息。当然，这里也可以用我的。

**调用接口方法如下：**

```
//接口调用方法如下：
//api_key：是你注册的key值
//coords：是你的经纬度坐标

http://api.map.baidu.com/reverse_geocoding/v3/?ak="+api_key+"&amp;output=json&amp;coordtype=wgs84ll&amp;location="+coords
```

#### 5、完整代码

最后，将代码整理汇总一下。

做成了一个简单的java小项目

有java环境，即可运行~~

#### **【项目完整代码+完整jar包】 **

#### **下载地址：**

****

****

深藏功与名~~

<img alt="" height="187" src="https://img-blog.csdnimg.cn/20210704224035667.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="190">

### 推荐阅读

**【Java资源下载】**
- 【JDK5】jdk1.5x64位 windows版.zip- - 【JDK6】jdk-6u45-windows-x64 jdk1.6 64位 Windows版- - 【JDK7】jdk-7u72-windows-i586-32位- - 【JDK8】jdk-8u131-linux-x64.tar.gz- - 【JDK8】jdk-8u131-linux-x64.tar.gz- 
**【python实战】**
- ****- ****- **...**- ****- ****- ****
**【pygame开发实战开发30例 完整源码】**
- 
**【pygame游戏开发专栏，获取完整源码+教程】**
- ****- ****- ****- ****- ** **- ****
#### CSDN官方学习推荐 ↓ ↓ ↓

为了帮助更多小白从零进阶 Java 工程师，从CSDN官方那边搞来了一套 《Java 工程师学习成长知识图谱》

尺寸 `870mm x 560mm`，知识汇总非常齐全，还可以折叠成一本书大小。

<img alt="" height="828" src="https://img-blog.csdnimg.cn/20210704222452239.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="475">
