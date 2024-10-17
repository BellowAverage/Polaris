
--- 
title:  最强Python Pandas学习神器来了 
tags: []
categories: [] 

---
来源：https://pandastutor.com/index.html

`Pandas`是数据挖掘常见的工具，掌握使用过程中的函数是非常重要的。本文将借助可视化的过程，讲解`Pandas`的各种操作。

### sort_values

```
(dogs[dogs['size'] == 'medium']
 .sort_values('type')
 .groupby('type').median()
)
```

执行步骤：
- size列筛选出部分行- 然后将行的类型进行转换- 按照type列进行分组，计算中位数
<img src="https://img-blog.csdnimg.cn/img_convert/0383fbec0d4fad650811155de1d35d83.png" alt="0383fbec0d4fad650811155de1d35d83.png">

<img src="https://img-blog.csdnimg.cn/img_convert/de9fbed49993956e09f705d7e38fe863.png" alt="de9fbed49993956e09f705d7e38fe863.png">

<img src="https://img-blog.csdnimg.cn/img_convert/021936a81066231b28625f9be9d11cf4.png" alt="021936a81066231b28625f9be9d11cf4.png">

<img src="https://img-blog.csdnimg.cn/img_convert/106ee18bc9e8838007100c9d8816f86c.png" alt="106ee18bc9e8838007100c9d8816f86c.png">

### selecting a column

```
dogs['longevity']
```

<img src="https://img-blog.csdnimg.cn/img_convert/88a3e22b76487239a649dab535624652.png" alt="88a3e22b76487239a649dab535624652.png">

### groupby + mean

```
dogs.groupby('size').mean()
```

执行步骤：
- 将数据按照size进行分组- 在分组内进行聚合操作
<img src="https://img-blog.csdnimg.cn/img_convert/36a542ce587f7ddd72f42de31decc691.png" alt="36a542ce587f7ddd72f42de31decc691.png">

<img src="https://img-blog.csdnimg.cn/img_convert/3c3b0b8a76c91ce40d2d9740f6668e00.png" alt="3c3b0b8a76c91ce40d2d9740f6668e00.png">

### grouping multiple columns

```
dogs.groupby(['type', 'size'])
```

<img src="https://img-blog.csdnimg.cn/img_convert/63c6cab27a24361c2d32cb06707ee793.png" alt="63c6cab27a24361c2d32cb06707ee793.png">

### groupby + multi aggregation

```
(dogs
  .sort_values('size')
  .groupby('size')['height']
  .agg(['sum', 'mean', 'std'])
)
```

执行步骤
- 按照size列对数据进行排序- 按照size进行分组- 对分组内的height进行计算
<img src="https://img-blog.csdnimg.cn/img_convert/800218ddcca1be22fe6418772f99721d.png" alt="800218ddcca1be22fe6418772f99721d.png">

<img src="https://img-blog.csdnimg.cn/img_convert/d4598a79bb5689f1ac4c6534799f6a3a.png" alt="d4598a79bb5689f1ac4c6534799f6a3a.png">

<img src="https://img-blog.csdnimg.cn/img_convert/3fa935e749fae21a598d1bc8f3e1db57.png" alt="3fa935e749fae21a598d1bc8f3e1db57.png">

<img src="https://img-blog.csdnimg.cn/img_convert/67d3557a47d9574b2936679491108d6c.png" alt="67d3557a47d9574b2936679491108d6c.png">

### filtering for columns

```
df.loc[:, df.loc['two'] &lt;= 20]
```

<img src="https://img-blog.csdnimg.cn/img_convert/82a3bed5051c43d1a009f420d0410a87.png" alt="82a3bed5051c43d1a009f420d0410a87.png">

### filtering for rows

```
dogs.loc[(dogs['size'] == 'medium') &amp; (dogs['longevity'] &gt; 12), 'breed']
```

<img src="https://img-blog.csdnimg.cn/img_convert/c259384727e36daf9880f7ab66a6f89f.png" alt="c259384727e36daf9880f7ab66a6f89f.png">

### dropping columns

```
dogs.drop(columns=['type'])
```

<img src="https://img-blog.csdnimg.cn/img_convert/bea19db9d448572f882ae7deb4154c51.png" alt="bea19db9d448572f882ae7deb4154c51.png">

### joining

```
ppl.join(dogs)
```

<img src="https://img-blog.csdnimg.cn/img_convert/0467fc17c94c8c7cfd51cd88dbca3395.png" alt="0467fc17c94c8c7cfd51cd88dbca3395.png">

### merging

```
ppl.merge(dogs, left_on='likes', right_on='breed', how='left')
```

<img src="https://img-blog.csdnimg.cn/img_convert/2f5be4c025c8cc70ae35c9fc1ffb2154.png" alt="2f5be4c025c8cc70ae35c9fc1ffb2154.png">

### pivot table

```
dogs.pivot_table(index='size', columns='kids', values='price')
```

<img src="https://img-blog.csdnimg.cn/img_convert/5ece847faf965803abcc6c022a36240d.png" alt="5ece847faf965803abcc6c022a36240d.png">

### melting

```
dogs.melt()
```

<img src="https://img-blog.csdnimg.cn/img_convert/efaab2c2277acdd4ccb1724710165839.png" alt="efaab2c2277acdd4ccb1724710165839.png">

### pivoting

```
dogs.pivot(index='size', columns='kids')
```

<img src="https://img-blog.csdnimg.cn/img_convert/fd67990235e84dfb805e099adee0099d.png" alt="fd67990235e84dfb805e099adee0099d.png">

### stacking column index

```
dogs.stack()
```

<img src="https://img-blog.csdnimg.cn/img_convert/0e9e1629d90d0b581a1333ca8d2affc4.png" alt="0e9e1629d90d0b581a1333ca8d2affc4.png">

### unstacking row index

```
dogs.unstack()
```

<img src="https://img-blog.csdnimg.cn/img_convert/fa79300730ea2bca008664c396d42386.png" alt="fa79300730ea2bca008664c396d42386.png">

### resetting index

```
dogs.reset_index()
```

<img src="https://img-blog.csdnimg.cn/img_convert/f5f1e115f69da340d3ffacbd2a31bdb6.png" alt="f5f1e115f69da340d3ffacbd2a31bdb6.png">

### setting index

```
dogs.set_index('breed')
```

<img src="https://img-blog.csdnimg.cn/img_convert/e52c1aa1b85bff7157540fb26d4bb61e.png" alt="e52c1aa1b85bff7157540fb26d4bb61e.png">

```
推荐阅读  点击标题可跳转
Python学习手册
Pandas学习大礼包
100+Python爬虫项目
Python数据分析入门手册
浙江大学内部Python教程

240个Python练习案例附源码

70个Python经典实用练手项目
整理了30款Python小游戏附源码
```
