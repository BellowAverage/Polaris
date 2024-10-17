
--- 
title:  【Python语法实例】-2 
tags: []
categories: [] 

---
##### 输入学生的成绩score，按分数输出其等级：score≥90为优，90&gt;score≥80为良，80&gt;score≥70为中等，70&gt;score≥60为及格，score&lt;60为不及格。

```
score=int(input("请输入成绩"))      #int()转换字符串为整型
if score &gt;= 90: 
    print("优")
elif  score &gt;= 80: 
    print("良") 
elif  score &gt;= 70:
    print("中")
elif  score &gt;= 60: 
    print("及格")
else :
    print("不及格")

```
