
--- 
title:  python数据采集 url拼接format 用法详解 
tags: []
categories: [] 

---
## python数据采集 url拼接format 用法详解

### 1.通过位置来填充字符串

```
print('hello {0} i am {1}'.format('world','python'))    # 输入结果：hello world i am python
print('hello {} i am {}'.format('world','python') ) #输入结果：hello world i am python
print('hello {0} i am {1} . a now language-- {1}'.format('world','python')
# 输出结果：hello world i am python . a now language-- python

```

foramt会把参数按位置顺序来填充到字符串中，第一个参数是0，然后1 …… 也可以不输入数字，这样也会按顺序来填充 同一个参数可以填充多次，这个是format比%先进的地方

### 2.通过key来填充

```
obj = 'world'
name = 'python'
print('hello, {obj} ,i am {name}'.format(obj = obj,name = name))
# 输入结果：hello, world ,i am python

```

### 3.通过列表填充

```
list=['world','python']
print('hello {names[0]}  i am {names[1]}'.format(names=list))# 输出结果：hello world  i am python
print('hello {0[0]}  i am {0[1]}'.format(list)) #输出结果：hello world  i am python

```

### 4.通过字典填充

```
dict={<!-- -->‘obj’:’world’,’name’:’python’}
print(‘hello {<!-- -->names[obj]} i am {<!-- -->names[name]}’.format(names=dict)) # hello world i am python
注意访问字典的key，不用引号的

```

### 5.通过类的属性填充

```
class Names():
    obj='world'
    name='python'

print('hello {names.obj} i am {names.name}'.format(names=Names))#输入结果hello world i am python

```

### 6.使用魔法参数

```
args = [‘,’,’inx’]
kwargs = {<!-- -->‘obj’: ‘world’, ‘name’: ‘python’}
print(‘hello {<!-- -->obj} {<!-- -->} i am {<!-- -->name}’.format(*args, **kwargs))#输入结果：hello world , i am python

注意：魔法参数跟你函数中使用的性质是一样的：这里format(*args, **kwargs)) 等价于：format(‘,’,’inx’,obj = ‘world’,name = ‘python’)

```

### format 格式转换

```
数字    格式    输出    描述
3.1415926    {<!-- -->:.2f}    3.14    保留小数点后两位
3.1415926    {<!-- -->:+.2f}    3.14    带符号保留小数点后两位
-1    {<!-- -->:+.2f}    -1    带符号保留小数点后两位
2.71828    {<!-- -->:.0f}    3    不带小数
1000000    {<!-- -->:,}    1,000,000    以逗号分隔的数字格式
0.25    {<!-- -->:.2%}    25.00%    百分比格式
1000000000    {<!-- -->:.2e}    1.00E+09    指数记法
25    {<!-- -->0:b}    11001    转换成二进制
25    {<!-- -->0:d}    25    转换成十进制
25    {<!-- -->0:o}    31    转换成八进制
25    {<!-- -->0:x}    19    转换成十六进制
5    {<!-- -->:0&gt;2}    05    数字补零(填充左边, 宽度为2)
5    {<!-- -->:x&lt;4}    5xxx    数字补x (填充右边, 宽度为4)
10    {<!-- -->:x^4}    x10x    数字补x (填充两边,优先左边, 宽度为4)
13    {<!-- -->:10}    13    右对齐 (默认, 宽度为10)
13    {<!-- -->:&lt;10}    13    左对齐 (宽度为10)
13    {<!-- -->:^10}    13    中间对齐 (宽度为10)
b、d、o、x分别是二进制、十进制、八进制、十六进制。

```

### 其它用法

#### 1.转义“{}”

```
print('{<!-- -->{hello}} {<!-- -->{<!-- -->{0}}}'.format('world')) #输出结果：{hello} {world}
1
跟%中%%转义%一样，format中用 {<!-- --> 来转义{<!-- --> ，用 } 来转义 }

```

#### 2.format作为函数变量

```
name = 'InX'
hello = 'hello,{} welcome to python world!!!'.format #定义一个问候函数
hello(name) #输入结果：hello,inx welcome to python world!!!

```

#### 3.格式化datetime

```
from datetime import datetime
now=datetime.now()
print '{:%Y-%m-%d %X}'.format(now) # 输出结果：2017-07-24 16:51:42

```

#### 4.{}内嵌{}

```
print('hello {0:&gt;{1}} '.format('world',10))

##输出结果：hello      world 
1
从最内层的{<!-- -->}开始格式化

```

#### 5.叹号的用法

```
print(‘{<!-- -->!s}国’.format(‘中’)) #输出结果：中国
print(‘{<!-- -->!a}国’.format(‘中’)) #输出结果：’\u4e2d’国
print(‘{<!-- -->!s}国’.format(‘中’)) #输出结果:’中’国
！后面可以加s r a 分别对应str() repr() ascii() 作用是在填充前先用对应的函数来处理参数
差别就是repr带有引号，str()是面向用户的，目的是可读性，repr()是面向Python解析器的，返回值表示在python内部的含义,ascii (),返回ascii编码

```

url拼接format 用法详解

```
url_01 = ['https://www.qdfd.com.cn/qdweb/realweb/fh/FhProjectQueryNew.jsp?page={}&amp;rows=20&amp;okey=&amp;order='.format(str(i)) for i in range(1, 500)]

```
