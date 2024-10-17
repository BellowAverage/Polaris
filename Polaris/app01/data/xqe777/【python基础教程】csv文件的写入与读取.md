
--- 
title:  【python基础教程】csv文件的写入与读取 
tags: []
categories: [] 

---
>  
 ✅作者简介：大家好我是hacker707,大家可以叫我hacker 📃个人主页： 🔥系列专栏： 💬推荐一款模拟面试、刷题神器👉 


<img src="https://img-blog.csdnimg.cn/d86586b389464d2aa9ba8ef688272334.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaGFja2VyNzA3,size_15,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">



#### csv文件读写
- - <ul><li>- - - <ul><li>- - 


## csv的简单介绍

CSV (Comma Separated Values)，即逗号分隔值（也称字符分隔值，因为分隔符可以不是逗号），是一种常用的文本格式，用以存储表格数据，包括数字或者字符。很多程序在处理数据时都会碰到csv这种格式的文件。python自带了csv模块，专门用于处理csv文件的读取

### csv的写入

<font color="#0099ff" size="4"> 1</font>通过创建writer对象，主要用到2个方法。一个是writerow，写入一行。另一个是writerows写入多行 <font color="#0099ff" size="4"> 2</font>使用DictWriter 可以使用字典的方式把数据写入进去

### 第一种写入方法(通过创建writer对象)

✅先来说一下第一种写入的方法：通过创建writer对象写入（每次写入一行） <font color="#0099ff" size="4"> 步骤</font>：1.创建数据和表头2.创建writer对象3.写表头4.遍历列表，将每一行数据写入csv 代码如下：

```
import csv

person = [('xxx', 18, 193), ('yyy', 18, 182), ('zzz', 19, 185)]
# 表头
header = ['name', 'age', 'height']

with open('person.csv', 'w', encoding='utf-8') as file_obj:
    # 1:创建writer对象
    writer = csv.writer(file_obj)
    # 2:写表头
    writer.writerow(header)
    # 3:遍历列表，将每一行的数据写入csv
    for p in person:
        writer.writerow(p)

```

写入完就会在当前目录下出现一个person.csv文件，鼠标右键点击show in Explorer打开person.csv查看

<img src="https://img-blog.csdnimg.cn/e33d3405a7c64a4388efda6a22238ef7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaGFja2VyNzA3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5caec63e9d7848deb36be80a90c01d6d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaGFja2VyNzA3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/355a106004534f45905b628f96796775.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaGFja2VyNzA3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 打开以后会发现写入的数据中间会换行 <font color="#0099ff" size="4"> 居然</font>：那么应该怎么解决这个问题呢 <font color="#0099ff" size="4"> hacker</font>：很简单啊 只需要在写入数据的时候加上一个参数<font color="#0099ff" size="4"> newline=‘’</font>为了防止换行写入 改正后的代码如下：

```
import csv

# 数据
person = [('xxx', 18, 193), ('yyy', 18, 182), ('zzz', 19, 185)]
# 表头
header = ['name', 'age', 'height']

with open('person.csv', 'w', encoding='utf-8', newline='') as file_obj:
    # 创建对象
    writer = csv.writer(file_obj)
    # 写表头
    writer.writerow(header)
    # 遍历，将每一行的数据写入csv
    for p in person:
        writer.writerow(p)

```

<img src="https://img-blog.csdnimg.cn/36a6b5ef050e426085f5ecb26762dca3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaGFja2VyNzA3,size_16,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> ✅通过创建writer对象（一次性写入多行） <font color="#0099ff" size="4"> 步骤</font>：1.创建数据和表头2.创建writer对象3.写表头4.在writerows里传入你要处理的数据

```
import csv

# 数据
person = [('xxx', 18, 193), ('yyy', 18, 182), ('zzz', 19, 185)]
# 表头
header = ['name', 'age', 'height']

with open('person.csv', 'w', encoding='utf-8', newline='') as file_obj:
    # 创建对象
    writer = csv.writer(file_obj)
    # 写表头
    writer.writerow(header)
    # 3.写入数据(一次性写入多行)
    writer.writerows(person)

```

写入结果如下：

<img src="https://img-blog.csdnimg.cn/45c982e004994ff79f7b2846775b6ac1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaGFja2VyNzA3,size_14,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 第二种写入方法(使用DictWriter可以使用字典的方式将数据写入)

<font color="#0099ff" size="4"> 注意事项</font>：使用字典的方式写入要注意传递的数据格式必须是字典 如果不是字典的话会报错

>  
 AttributeError: ‘tuple’ object has no attribute ‘keys’ 


<font color="#0099ff" size="4"> 步骤</font>1.创建数据和表头(<font color="#0099ff"> 数据必须是字典格式</font>)2.创建DictWriter对象3.写表头4.写入数据

```
import csv

# 数据
person = [
    {<!-- -->'name': 'xxx', 'age': 18, 'height': 193},
    {<!-- -->'name': 'yyy', 'age': 18, 'height': 182},
    {<!-- -->'name': 'zzz', 'age': 19, 'height': 185},
]
# 表头
header = ['name', 'age', 'height']

with open('person.csv', 'w', encoding='utf-8', newline='') as file_obj:
    # 1.创建DicetWriter对象
    dictWriter = csv.DictWriter(file_obj, header)
    # 2.写表头
    dictWriter.writeheader()
    # 3.写入数据(一次性写入多行)
    dictWriter.writerows(person)

```

<img src="https://img-blog.csdnimg.cn/4469b9ed2ed346229763cbf79d996582.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaGFja2VyNzA3,size_13,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

#### csv的读取

#### 通过reader()读取

```
import csv

with open('person.csv', 'r', encoding='utf-8') as file_obj:
    # 1.创建reader对象
    reader = csv.reader(file_obj)
    print(reader)

```

如果直接打印会返回csv.reader对象，这时需要遍历列表

>  
 &lt;_csv.reader object at 0x000001FB8CE655F8&gt; 


改正代码如下：

```
import csv

with open('person.csv', 'r', encoding='utf-8') as file_obj:
    # 1.创建reader对象
    reader = csv.reader(file_obj)
    # 2.遍历进行读取数据
    for r in reader:
        print(r)

```

读取结果如下：

```
['name', 'age', 'height']
['xxx', '18', '193']
['yyy', '18', '182']
['zzz', '19', '185']

```

如果想打印列表的某一个值，可以使用索引打印

```
print(r[0])

```

```
name
xxx
yyy
zzz

```

#### 通过dictreader()读取

```
import csv

with open('person.csv', 'r', encoding='utf-8') as file_obj:
    # 1.创建reader对象
    dictReader = csv.DictReader(file_obj)
    # 2.遍历进行读取数据
    for r in dictReader:
        print(r)

```

返回结果如下：

```
OrderedDict([('name', 'xxx'), ('age', '18'), ('height', '193')])
OrderedDict([('name', 'yyy'), ('age', '18'), ('height', '182')])
OrderedDict([('name', 'zzz'), ('age', '19'), ('height', '185')])

```

这时我们如果要取到某一个值就需要指定键去寻找值

```
print(r['name'])

```

```
xxx
yyy
zzz

```

以上就是python基础教程之csv文件的写入和读取，如果有改进的建议，欢迎在评论区留言奥~ 💖人生苦短，我用python💖 <img src="https://img-blog.csdnimg.cn/168e2200922f43f6ac5b0a80a394d170.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaGFja2VyNzA3,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">
