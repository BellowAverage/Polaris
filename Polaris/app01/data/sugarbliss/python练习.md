
--- 
title:  python练习 
tags: []
categories: [] 

---
例题1：给你一个字符串，删除若干个后，如果匹配hello，输出YES，否则NO。

样例：ahhellllloou，输出：YES；hlelo，输出：NO。

利用python正则表达式，re.search方法扫描整个字符串并返回第一个成功的匹配。**.*** 代表匹配除换行符之外的所有字符。匹配不成功返回**None**。

```
import re ; 
print("YES" if re.search("h.*e.*l.*l.*o",input()) else "NO")
```

正则表达式分组匹配(?P&lt;type&gt;) 

例：身份证 **1102231990xxxxxxxx**

```
import re
s = '1102231990xxxxxxxx'
res = re.search('(?P&lt;province&gt;\d{3})(?P&lt;city&gt;\d{3})(?P&lt;born_year&gt;\d{4})',s)
print(res.groupdict())
#输出：{'province': '110', 'city': '223', 'born_year': '1990'}
```

 
