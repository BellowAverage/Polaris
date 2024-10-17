
--- 
title:  对于matplotlib的图像中汉字中文输出乱码问题的解决方法 
tags: []
categories: [] 

---
**示例代码如下：**

>  
 <pre>import csv
import matplotlib.pyplot as plt

filename = 'sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取最高温度。
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
    print(highs)

    # 根据最高温度绘制图形。
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(highs, c='red')

    # 设置图形的格式。
    ax.set_title("2008年7月每日最高温度", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    ax.set_ylabel("温度(F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()</pre> 


**运行结果：**

<img alt="" height="312" src="https://img-blog.csdnimg.cn/e71abf96e09b4dd181a616613b60c81f.png" width="434">

        图中出现汉字输出异常。

  **      解决办法：**

>  
 <pre>import csv
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"/System/Library/Fonts/STHeiti Medium.ttc", size=15)

filename = 'sitka_weather_07-2018_simple.csv'
   --snip--

    # 设置图形的格式。
    ax.set_title("2008年7月每日最高温度", fontsize=24, fontproperties=font_set)
    ax.set_xlabel('', fontsize=16)
    ax.set_ylabel("温度(F)", fontsize=16, fontproperties=font_set)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()</pre> 


加上红色部分的代码后，输出结果如下图：

<img alt="" height="307" src="https://img-blog.csdnimg.cn/59551acd67254e4588cac1679aaf18ed.png" width="421">



加上红色部分代码后，汉字无法正常输出的问题就完美解决了 ！！！



**特别声明：本文中的代码取自《Python编程-从入门到实践》第16章的sitka_highs.py**
