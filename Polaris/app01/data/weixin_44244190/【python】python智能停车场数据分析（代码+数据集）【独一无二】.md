
--- 
title:  【python】python智能停车场数据分析（代码+数据集）【独一无二】 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>python智能停车场数据分析（代码+数据集）【独一无二】</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - - - <ul><li>- - - - - -  
   </li>- - <li><ul><li> 
   </li></ul> 
  </li></ul> 
  
  


## 一、题目要求

实现智能停车场数据分析，使用pygame实现对停车场的数据分析，pygame实现6个按钮，点击按钮，分别出发六功能图像的分析结果，要求如下：

>  
 数据来源（二选一）： 1） 爬取网页数据 2）数据文件 


>  
 数据分析： 1）停车时间的分布情况 2）停车高峰的时间统计 3）每周繁忙的比例 4）月收入分析 5）每日接待车辆的统计 6）车位利用率的统计 


>  
 绘制图表： 1）条形图 2）饼图 3）折线图 


## 二、数据来源

在实现智能停车场数据分析时，需要先观察停车场数据结构，找到数据中的固定规律，然后根提规律进行的分析。所以拿到数据文件后，先读取文件并将文件的头部信息打印，观察数据结构的规律性。

<img src="https://img-blog.csdnimg.cn/f28a643239ff4764986ab58ea981c7a6.png" alt="在这里插入图片描述">

>  
 其中：cn 为车牌号码; timein 为车辆进入停车场的时间; timeout 为车辆驶出停车场的时间; price 为停车所交费用; state 标记为1时说明车辆已经交费驶出，state标记为0时说明车辆还未驶出停车场; rps 为当前空余车位的数量。 


## 三、功能展示

### 1.pygame主界面实现

<img src="https://img-blog.csdnimg.cn/83d291d1861544cfbf9b4d9763885b38.png" alt="在这里插入图片描述">

### 2.停车时间分布数据分析

<img src="https://img-blog.csdnimg.cn/77311d81590a4e3aa48e9cae4bdd22bf.png" alt="在这里插入图片描述">

### 2.停车高峰时间数据分析

<img src="https://img-blog.csdnimg.cn/956a3175ba334d3eafaefcc7cf207abb.png" alt="在这里插入图片描述">

### 3. 每周繁忙比例

<img src="https://img-blog.csdnimg.cn/2e5a3098f2e446aea2678085e6cc4391.png" alt="在这里插入图片描述">

### 4. 月收入分析

<img src="https://img-blog.csdnimg.cn/a9b693a523ec4877a9af19582e9fcb2a.png" alt="在这里插入图片描述">

### 5. 每日接待车辆

<img src="https://img-blog.csdnimg.cn/5d6b14db539d4d64b9d15e1ba79de121.png" alt="在这里插入图片描述">

### 6. 车位利用率

<img src="https://img-blog.csdnimg.cn/f76a26371c0440e9906578cf6186d6d2.png" alt="在这里插入图片描述">

## 四、代码实现

**部分**代码展示如下：

```
import pygame
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']

# 初始化pygame
pygame.init()

# 设置窗口
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("停车场数据分析")

# 颜色和字体设置
button_color = (0, 128, 255)
text_color = (255, 255, 255)
font = pygame.font.SysFont('SimHei', 20)

# 按钮布局
buttons = {<!-- -->
    '停车时间分布': (100, 100),
    '停车高峰时间': (300, 100),
    '每周繁忙比例': (500, 100),
    '月收入分析': (100, 300),
    '每日接待车辆': (300, 300),
    '车位利用率': (500, 300)
}

# 读取Excel文件
df = pd.read_excel("停车场信息表.xlsx", engine='openpyxl')
df['timein'] = pd.to_datetime(df['timein'])
df['timeout'] = pd.to_datetime(df['timeout'])
df['parking_duration'] = (df['timeout'] - df['timein']).dt.total_seconds() / 3600

# 。。。。。。


```

#### 👇👇👇关注公众号，回复 “智能停车场数据分析” 获取源码+数据集👇👇👇
