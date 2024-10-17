
--- 
title:  这 10 个 Python 可视化工具，你都用过？ 
tags: []
categories: [] 

---
>  
  来源：Lty美丽人生 
  https://blog.csdn.net/weixin_44208569 
 

本文介绍 10 个适用于多个学科的 Python 数据可视化库，其中有名气很大的，也有鲜为人知的。

### **1、matplotlib**

matplotlib 是Python可视化程序库的泰斗。经过十几年它任然是Python使用者最常用的画图库。它的设计和在1980年代被设计的商业化程序语言MATLAB非常接近。

由于 matplotlib 是第一个 Python 可视化程序库，有许多别的程序库都是建立在它的基础上或者直接调用它。

比如pandas和Seaborn就是matplotlib的外包，它们让你能用更少的代码去调用 matplotlib的方法。

虽然用 matplotlib 可以很方便的得到数据的大致信息，但是如果要更快捷简单地制作可供发表的图表就不那么容易了。

就像Chris Moffitt 在“Python可视化工具简介”中提到的一样：“功能非常强大，也非常复杂。”

matplotlib 那有着强烈九十年代气息的默认作图风格也是被吐槽多年。即将发行的matplotlib 2.0 号称会包含许多更时尚的风格。

**开发者：John D. Hunter**

更多资料：

http://matplotlib.org/

### 

### **2、Seaborn**

Seaborn利用了matplotlib，用简洁的代码来制作好看的图表。

Seaborn跟matplotlib最大的区别就是它的默认绘图风格和色彩搭配都具有现代美感。

由于Seaborn是构建在matplotlib的基础上的，你需要了解matplotlib从而来调整Seaborn的默认参数。

**开发者: Michael Waskom**

更多资料：

http://seaborn.pydata.org/index.html

### 

### **3、ggplot**

ggplot 基于R的一个作图包 ggplot2, 同时利用了源于 《图像语法》（The Grammar of Graphics）中的概念。

ggplot 跟 matplotlib 的不同之处是它允许你叠加不同的图层来完成一幅图。比如你可以从轴开始，然后加上点，加上线，趋势线等等。

虽然《图像语法》得到了“接近思维过程”的作图方法的好评，但是习惯了matplotlib的用户可能需要一些时间来适应这个新思维方式。

ggplot的作者提到 ggplot 并不适用于制作非常个性化的图像。它为了操作的简洁而牺牲了图像复杂度。

ggplot跟pandas的整合度非常高，所以当你使用它的时候，最好将你的数据读成 DataFrame。

**开发者: ŷhat**

更多资料：

http://ggplot.yhathq.com/

### **4、Bokeh**

跟ggplot一样， Bokeh 也是基于《图形语法》的概念。

但是跟ggplot不一样的是，它完全基于Python而不是从R引用过来的。

它的长处在于它能用于制作可交互，可直接用于网络的图表。图表可以输出为JSON对象，HTML文档或者可交互的网络应用。

Boken也支持数据流和实时数据。Bokeh为不同的用户提供了三种控制水平。

最高的控制水平用于快速制图，主要用于制作常用图像， 例如柱状图，盒状图，直方图。

中等控制水平跟matplotlib一样允许你控制图像的基本元素（例如分布图中的点）。

最低的控制水平主要面向开发人员和软件工程师。

它没有默认值，你得定义图表的每一个元素。

**开发者: Continuum Analytics**

更多资料：

https://docs.bokeh.org/en/latest/

### **5、pygal**

pygal 跟 Bokeh 和 Plotly 一样，提供可直接嵌入网络浏览器的可交互图像。

跟其他两者的主要区别在于它可以将图表输出为SVG格式。

如果你的数据量相对小，SVG就够用了。但是如果你有成百上千的数据点，SVG的渲染过程会变得很慢。

由于所有的图表都被封装成了方法，而且默认的风格也很漂亮，用几行代码就可以很容易地制作出漂亮的图表。

**开发者: Florian Mounier**

更多资料：

http://www.pygal.org/en/latest/index.html

### 

### **6、Plotly**

你也许听说过在线制图工具Plotly，但是你知道你可以通过Python使用它么？

Plotly 跟 Bokeh 一样致力于交互图表的制作，但是它提供在别的库中很难找到的几种图表类型，比如等值线图，树形图和三维图表。

**开发者: Plotly**

更多资料：

https://plotly.com/python/

### **7、geoplotlib**

geoplotlib 是一个用于制作地图和地理相关数据的工具箱。

你可以用它来制作多种地图，比如等值区域图， 热度图，点密度图。

你必须安装 Pyglet （一个面向对象编程接口）来使用geoplotlib。不过因为大部分Python的可视化工具不提供地图，有一个专职画地图的工具也是挺方便的。

**开发者: Andrea Cuttone**

更多资料：

https://github.com/andrea-cuttone/geoplotlib

### **8、Gleam**

Gleam 借用了R中 Shiny 的灵感。它允许你只利用 Python 程序将你的分析变成可交互的网络应用，你不需要会用HTML CSS 或者 JaveScript。

Gleam 可以使用任何一种 Python 的可视化库。

当你创建一个图表的时候，你可以在上面加上一个域，这样用户可以用它来对数据排序和过滤了。

**开发者: David Robinson**

更多资料：

https://github.com/dgrtwo/gleam

### **9、missingno**

缺失数据是永远的痛。

missingno 用图像的方式让你能够快速评估数据缺失的情况，而不是在数据表里面步履维艰。

你可以根据数据的完整度对数据进行排序或过滤，或者根据热度图或树状图来考虑对数据进行修正。

**开发者: Aleksey Bilogur**

更多资料：

https://github.com/ResidentMario/missingno

### **10、Leather**

Leather的最佳定义来自它的作者 Christopher Groskopf。

Leather 适用于现在就需要一个图表并且对图表是不是完美并不在乎的人。

它可以用于所以的数据类型然后生成SVG图像，这样在你调整图像大小的时候就不会损失图像质量。

**开发者: Christopher Groskopf**

更多资料：

https://leather.readthedocs.io/en/latest/index.html

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcFh1ZmlibEhVcndWT0loNFg4WWhwYXBpYU1rQk9sSE16b0ZRQm1Qd3dUWEREOG1Dd3pQWEdydUxRbEVBR1VTT3c4aWNQV0FydnRRaWFMTVEvNjQw?x-oss-process=image/format,png">
