
--- 
title:  python猜数字游戏 
tags: []
categories: [] 

---
## python猜数字游戏

### python小甲鱼猜数字游戏：

#### 1、python中random随机数

**random模块提供生成伪随机数的函数，在使用时需要导入random模块**：

```
import random

```
- random.random() 最基本的随机函数，返回一个[0.0,1.0)之间的随机小数- random.uniform(a,b) 在指定范围内生成**随机小数**，两个参数其中一个是上限，一个是下限。如果a &gt; b，则生成的随机数n: b &lt;= n &lt;= a；如果 a &lt;b， 则 a &lt;= n &lt;= b- random.randint(m,n) 用于生成一个指定范围内的**整数**。其中参数a是下限，参数b是上限，生成的随机数n: a &lt;= n &lt;= b- random.choice(sequence) 从序列中获取一个随机元素；list，tuple 字符串都属于sequence。- random.sample(sequence,count) 从指定序列中获取指定个数的随机元素。sample函数不会修改原有序列。- random.randrange([start], stop[, step]) 从指定范围内，按指定基数递增的集合中获取一个随机数。- random.shuffle(list) 将一个列表内的元素顺序打乱，随机排列
```
import random
import string

# 随机整数：
print random.randint(1,50)

# 随机选取0到100间的偶数：
print random.randrange(0, 101, 2)

# 随机浮点数：
print random.random()
print random.uniform(1, 10)

# 随机字符：
print random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&amp;*()')

# 多个字符中生成指定数量的随机字符：
print random.sample('zyxwvutsrqponmlkjihgfedcba',5)

# 从a-zA-Z0-9生成指定数量的随机字符：
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print ran_str

# 多个字符中选取指定数量的字符组成新字符串：
print ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))

# 随机选取字符串：
print(random.choice(['剪刀', '石头', '布']))

# 打乱排序
lst=[10,20,30,40,50]
random.shuffle(lst)
print(lst)

```

#### 2、循环获取若干个随机数的写法：

```
lst=[]
for i in range(5):
    lst.append(random.randint(1,100))
print(lst)

#[97, 89, 76, 86, 60]

```

#### 3、开始游戏

游戏规则：

1、小甲鱼随机生成一个 1到100 的整数；

2、用户输入自己心中的数字；

3、用户输入的数字会与随机数匹配，若相等，则游戏成功；否者会告知猜大了还是猜小了；

4、用户有五次猜数字的机会；

```
'''
小甲鱼的游戏：
随便猜一个数，看你是不是小甲鱼肚里的蛔虫
'''

import random
x=random.randint(1,100)
# print(x)
print('小甲鱼随机数已生成（1-100），请开始游戏！')

i=7
while(i&gt;0):
    try:
        num=int(input('请输入你想要的猜的数字：'))
    except:
        print('输入错误，请重新输入！！！')
        continue
    if num==x:
        print('恭喜你，猜对啦！你真是小甲鱼肚子里的蛔虫呢。')
        break
    elif num&lt;x:
        print('猜小啦，再接再厉哦！')
    else:
        print('猜大了，再往小猜猜。')

    i=i-1
    if i&gt;0:
        print('你还有{0}次机会'.format(i))
        print()
    else:
        print('很遗憾，你的机会已用尽！！！')


```

<img src="https://img-blog.csdnimg.cn/b3aa3f7d375f4472b759c79ee05e9391.png#pic_center" alt="在这里插入图片描述"> 游戏结束，小甲鱼跟开心你陪他玩。
