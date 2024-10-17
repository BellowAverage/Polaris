
--- 
title:  【hacker的错误集】ValueError: I/O operation on closed file 
tags: []
categories: [] 

---
>  
 ✅作者简介：大家好我是hacker707,大家可以叫我hacker，新星计划第三季python赛道Top1🏆🏆🏆 📃个人主页： 🔥系列专栏： 💬推荐一款模拟面试、刷题神器👉 


<img src="https://img-blog.csdnimg.cn/78c5e154928c4d0bb6a0cd1fcc5664ff.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaGFja2VyNzA3,size_15,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">



#### hacker错误集
- - <ul><li>- <ul><li>


## 报错内容

报错代码：

```
import csv

person = [('xxx', 18, 180), ('yyy', 18, 182), ('zzz', 19, 185)]
# 表头
header = ['name', 'age', 'height']

with open('person.csv', 'w', encoding='utf-8-sig') as file_obj:
    # 1:创建writer对象
    writer = csv.writer(file_obj)
    # 2:写表头
    writer.writerow(header)
    # 3:遍历列表，将每一行的数据写入csv
for p in person:
    writer.writerow(p)

```

<img src="https://img-blog.csdnimg.cn/7daf42dae7c244c69dfc55c3819e5f99.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaGFja2VyNzA3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 报错分析

ValueError: I/O operation on closed file.依旧是使用单词意思来分析报错原因 <mark>ValueError</mark>值错误 <mark>closed file</mark>关闭的文件 通过分析可以得出：with open处理了已经被关闭的数据。使用with open打开文件，如果语句在with open之外是无效的，因为文件已经被关闭了 <font color="#0099ff" size="4"> 居然</font>：那应该怎么解决呢 <font color="#0099ff" size="4">hacker</font>：👀👀👀

#### 解决方案

其实解决方法很简单，只需要将你要处理的数据都加到with open里，改一下代码缩进即可完美解决 <img src="https://img-blog.csdnimg.cn/6ff5dd7659ca40f28cb10c7f397e6130.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaGFja2VyNzA3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 改进后的代码：

```
import csv

person = [('xxx', 18, 180), ('yyy', 18, 182), ('zzz', 19, 185)]
# 表头
header = ['name', 'age', 'height']

with open('person.csv', 'w', encoding='utf-8-sig') as file_obj:
    # 1:创建writer对象
    writer = csv.writer(file_obj)
    # 2:写表头
    writer.writerow(header)
    # 3:遍历列表，将每一行的数据写入csv
    for p in person:
        writer.writerow(p)

```

完美解决🥳🥳🥳

## 结束语🏆🏆🏆

会持续更新专栏《hacker的错误集》相关知识，如果有改进的建议欢迎在评论区留言奥~ 感谢大家对hacker的支持💖💖💖
