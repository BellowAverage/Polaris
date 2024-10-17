
--- 
title:  Py之chinesecalendar：chinesecalendar的简介、安装、使用方法之详细攻略 
tags: []
categories: [] 

---
Py之chinesecalendar：chinesecalendar的简介、安装、使用方法之详细攻略





**目录**















## **<strong><strong>chinesecalendar**</strong>**<strong>的简介**</strong></strong>

       该库是判断某年某月某一天是不是工作日/节假日。 支持 2004年 至 2023年，包括 2020年 的春节延长。由于次年的节假日安排，取决于国务院发布的日程。 所以本项目一般会在国务院更新以后，发布新的版本。 按照以往的经验，一般是每年的 11月 前后发布新版本。





## **<strong><strong>chinesecalendar**</strong>**<strong>的安装**</strong></strong>

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple chinesecalendar
```



<img alt="" height="239" src="https://img-blog.csdnimg.cn/0b3937f48ca24fa3b0b808514c1b5ff5.png" width="1200">





## **<strong><strong>chinesecalendar**</strong>**<strong>的使用方法**</strong></strong>

### 1、基础用法

# 判断 2018年4月30号 是不是节假日 # 判断法定节假日是不是调休

```
import datetime

# 判断 2018年4月30号 是不是节假日
from chinese_calendar import is_holiday, is_workday
april_last = datetime.date(2022, 3, 23)
print('is_holiday: ',is_holiday(april_last))
print('is_workday: ',is_workday(april_last))



# 判断法定节假日是不是调休
from chinese_calendar import is_in_lieu
date01 = datetime.date(2022, 1, 29)
date02 = datetime.date(2022, 2, 1)
print('is_in_lieu: ',is_in_lieu(date02))

```










