
--- 
title:  答应我！忘了他吧！不要再用print了，以后调试Python用冰淇淋 
tags: []
categories: [] 

---
>  
 大家好，我是Lex 喜欢欺负超人那个Lex 
 擅长领域：python开发、网络安全渗透、Windows域控Exchange架构 
 今日重点： 
 调试python不要再用print()了，甜甜的冰激凌调试工具来了 
 【建议收藏，然后下来一定操作一遍】 


### 事情是这样的

望着窗外，太阳在乌云背后努力想把阳光撒向人间

雨过天青云破处吹来的缕缕微风拂过你的脸颊

迎着微风贪婪的深吸一口，放下键盘，回想你这一生

<img alt="" height="194" src="https://img-blog.csdnimg.cn/2021070221175061.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="291">

最依赖的python的函数是什么

emmm，我猜一定是print()

从入坑案例 print('Hello World') 开始

你的代码越写越多，逻辑越来越复杂

但是在代码的寻常巷陌之间

却总是穿插着大量的print()调试语句

<img alt="" height="190" src="https://img-blog.csdnimg.cn/20210702203108786.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="268">

输出的结果，让人欢喜让人忧

答应我，从今天开始，忘了他

<img alt="" height="166" src="https://img-blog.csdnimg.cn/20210702203223403.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="294">

 以后用ice cream

### 

### icecream调试工具

**1、安装 pip install icecream**

```
pip install icecream

PS C:\Users\pacer&gt; pip install icecream
Collecting icecream
  Downloading icecream-2.1.1-py2.py3-none-any.whl (8.1 kB)
Collecting asttokens&gt;=2.0.1
  Downloading asttokens-2.0.5-py2.py3-none-any.whl (20 kB)
Collecting executing&gt;=0.3.1
  Downloading executing-0.6.0-py2.py3-none-any.whl (12 kB)
Requirement already satisfied: pygments&gt;=2.2.0 in d:\python36\lib\site-packages (from icecream) (2.9.0)
Requirement already satisfied: colorama&gt;=0.3.9 in d:\python36\lib\site-packages (from icecream) (0.4.3)
Requirement already satisfied: six in d:\python36\lib\site-packages (from asttokens&gt;=2.0.1-&gt;icecream) (1.11.0)
Installing collected packages: executing, asttokens, icecream
Successfully installed asttokens-2.0.5 executing-0.6.0 icecream-2.1.1
```

**2、调用方法**

```
from icecream import ic
ic('test')
```

### 案例解析

>  
   下面我们通过几个比对案例，来详细介绍一下 ice cream 到底比 print() 强在哪里。 


#### **案例1：访问函数**

```
#案例1：计算平方数
def pingfang(number):
    return number*number
```

>  
 如果我们需要调试函数，获取2,3,4的平方数。那么输出结果，需要这么写 


```
print(pingfang(2))
print(pingfang(3))
print(pingfang(4))
```

>  
 **输出结果如下：** 


```
4
9
16
```

>  
 **输出结果并不清晰，输入参数都看不见。****优化一下：** 


```
print('2的平方是：',pingfang(2))
print('3的平方是：',pingfang(3))
print('4的平方是：',pingfang(4))
```

>  
 **输出结果如下：** 


```
2的平方是：4
3的平方是：9
4的平方是：16
```
- 这样的输出，才是合理的，但是这样我们每个都要这么写，估计会疯掉。- 而且，当代码正式上线运行的时候，我们要注释大量的代码。
#### 不扯了，上icecream

```
#引入icecream模块 代替print
from icecream import ic

def pingfang(number):
    return number*number

#使用ic进行调试
ic(pingfang(2))
ic(pingfang(3))
ic(pingfang(4))
```

>  
 **输出结果如下：** 


```
ic| pingfang(2): 4
ic| pingfang(3): 9
ic| pingfang(4): 16
```

**输出结果被安排的明明白白。**

#### 案例2：访问字典

>  
 **建一个以老大命名的字典** 


```
#示例2:科比字典访问
kobe_dict = {
  'name': 'KobeBryant',
  'team': 'LALakers',
  'number': 24,
  'halloffame' : True
}
```

>  
 **print() 和 ic()访问方法进行对比：** 


```
#print方法
print(kobe_dict['team'])

#ic方法
ic(kobe_dict['team'])
```

>  
 **输出结果对比：** 


```
#print输出
LALakers

#ic输出
ic| kobe_dict['team']: 'LALakers'
```

 **高下立判！！！**

#### 案例3：访问对象

```
#示例3:湖人类
class Lakers():
    city = 'los angles'
    player = 'kobe'
    NBA = True
```

>  
 **print() 和 ic()访问方法进行对比：** 


```
#print方法输出
lakers=Lakers()
print(lakers.city)
print(lakers.NBA)

#ic方法输出
ic(lakers.city)
ic(lakers.NBA)
```

>  
 **输出结果对比如下： ** 


```
los angles
True

ic| lakers.city: 'los angles'
ic| lakers.NBA: True
```

####  案例4：精准调试代码
- 我们在调试业务逻辑比较复杂的代码的时候- 为了验证业务在哪个逻辑或者哪一行输出有问题了。- 一般都在要监控的代码下面- 加上 print('aaa')、print('bbbb')或者print('-------')，别说你没这么干过- 搞的代码非常混乱，而且输出也不够精准。
```
#示例4：记录代码位置
def position(name):
    if name == 'kobe':
        #啪啪啪,业务代码一大堆
        ic()
    else:
        #啪啪啪,业务代码又一大堆
        ic()
if __name__ == '__main__':
    position('kobe')
    position('micheal')
```

>  
 **print() 和 ic()访问方法进行对比：** 

-  我们可以精确的输出业务代码的位置。  
<img alt="" height="352" src="https://img-blog.csdnimg.cn/20210702201831749.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="361">



####  案例5：始乱终弃很方便
- 当我们使用print()进行python调试的时候- 加了一大堆又臭又长的  print('aaa')、print('bbbb') 或者 print('-----')- 当项目正式上线的时候，肯定要去注释掉这些test输出- 这个时候，我们才发现：“他们都老了吗，他们在哪里呀~~~”- 找不着了，是吧？！这时候又要翻箱倒柜的去找来注释。- 如果我们用icecream进行调试- 只要开头加上一句
```
ic.disable() #关闭ic调试。[默认开启]
```
- 你所有的添加的ic输出- 相当于你的历史渣男记录- 全部洗白。
如下 ↓ ↓ ↓

```
from icecream import ic
#关闭所有ic调试输出
ic.disable()
#业务代码一大堆，啪啪啪...
#...
```
- 如果想要使用ic输出- 只要开头启用就好了。
```
ic.enable()  #启用ic调试
```

####   案例6：自定义ic输出很方便

```
icecream 的默认输出格式：

ic| testic.py:28 in position() at 14:28:51.172
ic| testic.py:31 in position() at 14:28:51.190
```


- 包括前缀：ic- 文件名：testic.py- 代码位置：28行- 函数：position()
**1、修改前缀：加上自定义内容**

```
ic.configureOutput(prefix='lex的爬虫 | ')
ic('运行到这里了...')
```

>  
 输出效果如下： 


<img alt="" height="242" src="https://img-blog.csdnimg.cn/20210702201917983.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="438">

**2、输出代码运行的时间**
- 有时候，进行代码输出调试的时候- 需要知道代码运行该位置时的精确时间- 我们可以自定义icecream来实现带时间的输出。
```
#定义一个返回当前时间的函数
from datetime import datetime
def now():
    return f'[{datetime.now()}]'

#将函数返回值,配置进ic里
ic.configureOutput(prefix=now)
ic('运行到这里了...')
```

>  
 **输出结果如下：** 


 <img alt="" height="332" src="https://img-blog.csdnimg.cn/20210702201956916.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="402">

**---------The End--------**

### 推荐阅读

**python实战**
- ****- ****- **...**- ****- ****- ****
**【pygame开发实战开发30例 完整源码】**
- 
**【pygame游戏开发专栏，获取完整源码+教程】**
- ****- ****- ****- ****- ** **- ****
#### CSDN官方学习推荐 ↓ ↓ ↓
- **CSDN出的Python全栈知识图谱，太强了，推荐给大家！**
<img alt="" height="574" src="https://img-blog.csdnimg.cn/20210607120133619.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="323">
