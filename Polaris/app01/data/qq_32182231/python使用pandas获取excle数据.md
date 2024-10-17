
--- 
title:  python使用pandas获取excle数据 
tags: []
categories: [] 

---
```
import pandas as pd

# 获取sheet页，sheet_name可以等于sheet名称，也可传入存sheet页名称的数组
excel_info = pd.read_excel(fileurl, sheet_name=sheet_name)  # excel_info 类型是 dataFrame
#根据列名获取整列数据
list1 = excel_info["列名"]
#获取前n行数据
list2 = excel_info.head(n)
#获取后n行数据
list3 = excel_info.tail(n)
#获取第n行数据
list4 = excel_info.loc(n)
#获取第4-9行，第3到4列的数据
list5 = excel_info.iloc[3:9, 2:4]


```


