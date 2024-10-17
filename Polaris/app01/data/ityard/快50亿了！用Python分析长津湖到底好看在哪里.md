
--- 
title:  快50亿了！用Python分析长津湖到底好看在哪里 
tags: []
categories: [] 

---
来源：www.cnblogs.com/hahaa

十月份的黄金周，乃至整个十月份，妥妥的是《长津湖》的天下，才小半个月票房就已经突破44亿，都快追上战狼2了。猫眼评分9.5，口碑超高，2021年票房口碑双丰收大黑马！

<img src="https://img-blog.csdnimg.cn/img_convert/635aa9aaf0dc9833df9a010d80647e5a.png" alt="635aa9aaf0dc9833df9a010d80647e5a.png">

今天我们通过爬取猫眼的电影评论，进行可视化分析，康康长津湖为什么这么受欢迎，最后教大家进行票房预测，千万不要错过！

### 

### **数据获取**

猫眼评论爬取，还是那么老一套，直接构造 API 接口信息即可。

<img src="https://img-blog.csdnimg.cn/img_convert/0f4407a6bbd3d09139f8240bc062e5e8.png" alt="0f4407a6bbd3d09139f8240bc062e5e8.png">

这么几行代码，我们就可以得到如下结果

<img src="https://img-blog.csdnimg.cn/img_convert/9cf8af0a3fe94b032de9691262edf911.png" alt="9cf8af0a3fe94b032de9691262edf911.png">

获取到数据后，我们就可以解析返回的 json 数据，并保存到本地了。

先写一个保存数据的函数

<img src="https://img-blog.csdnimg.cn/img_convert/5a964d062e7bda824407a235f47225dd.png" alt="5a964d062e7bda824407a235f47225dd.png">

<img src="https://img-blog.csdnimg.cn/img_convert/9c869b3b0180ac0177dc79abf9259952.png" alt="9c869b3b0180ac0177dc79abf9259952.png">

<img src="https://img-blog.csdnimg.cn/img_convert/48bf82055b7220ea9f85c8ec47903433.png" alt="48bf82055b7220ea9f85c8ec47903433.png">

<img src="https://img-blog.csdnimg.cn/img_convert/38e65e7b3e6e686604349a05ce10bb94.png" alt="38e65e7b3e6e686604349a05ce10bb94.png">

<img src="https://img-blog.csdnimg.cn/img_convert/e0a198a44acfdf6326591cb6496fc52e.png" alt="e0a198a44acfdf6326591cb6496fc52e.png">

保存到本地的数据

<img src="https://img-blog.csdnimg.cn/img_convert/d4d83d03603c6703f4703822cacbb1ba.png" alt="d4d83d03603c6703f4703822cacbb1ba.png">

**可视化分析**

我们来进行相关的可视化分析

**1、数据清洗**

首先我们根据 comment_id 来去除重复数据

```
df_new = df.drop_duplicates(['comment_id'])
```

对于评论内容，我们进行去除非中文的操作。

<img src="https://img-blog.csdnimg.cn/img_convert/73769dbfb0b22990429928b585ed4b63.png" alt="73769dbfb0b22990429928b585ed4b63.png">

**2、评论点赞及回复榜**

来看看哪些评论是被点赞最多的

<img src="https://img-blog.csdnimg.cn/img_convert/09d1926f202e45b1c279e21919112419.png" alt="09d1926f202e45b1c279e21919112419.png">

<img src="https://img-blog.csdnimg.cn/img_convert/9ca03929100a1309d240c951330dccdd.png" alt="9ca03929100a1309d240c951330dccdd.png">

<img src="https://img-blog.csdnimg.cn/img_convert/fabe7b2ac8cb5a5b9c46ee5da5e0c0aa.png" alt="fabe7b2ac8cb5a5b9c46ee5da5e0c0aa.png">

<img src="https://img-blog.csdnimg.cn/img_convert/6fe0ef0a2726ed9b0af3dbd234990f18.png" alt="6fe0ef0a2726ed9b0af3dbd234990f18.png">

<img src="https://img-blog.csdnimg.cn/img_convert/b5eae5521fcdd022cfd42a440d4278d4.png" alt="b5eae5521fcdd022cfd42a440d4278d4.png">

<img src="https://img-blog.csdnimg.cn/img_convert/51f863a4b50119f69925b62925f0b66b.png" alt="51f863a4b50119f69925b62925f0b66b.png">

Output：

<img src="https://img-blog.csdnimg.cn/img_convert/675de24ba3ed9fb24376349cb78068d5.png" alt="675de24ba3ed9fb24376349cb78068d5.png">

<img src="https://img-blog.csdnimg.cn/img_convert/fe923683448f57167095aa5bea9d0bdc.png" alt="fe923683448f57167095aa5bea9d0bdc.png">

下面我们来看一下整体评论数据的情况

**3、各城市排行**

来看看哪些城市的评论最多呢

<img src="https://img-blog.csdnimg.cn/img_convert/81c7e68a4c9ffdcab1fba225bcaa7f52.png" alt="81c7e68a4c9ffdcab1fba225bcaa7f52.png">

<img src="https://img-blog.csdnimg.cn/img_convert/17c54395b77a9f562f68396d793977f3.png" alt="17c54395b77a9f562f68396d793977f3.png">

<img src="https://img-blog.csdnimg.cn/img_convert/43415ee5c3c7a74be2e310750ba95e25.png" alt="43415ee5c3c7a74be2e310750ba95e25.png">

<img src="https://img-blog.csdnimg.cn/img_convert/6c05775f8f6c6a74c8bca6054547c045.png" alt="6c05775f8f6c6a74c8bca6054547c045.png">

可以看到，这个评论城市的分布，也是与我国总体经济的发展情况相吻合的

**4、性别分布**

```
attr = [其他,男,女]

b = (Pie()
     .add(, [list(z) for z in zip(attr, df_new.groupby(gender).gender.count().values.tolist())])
     .set_global_opts(title_opts = opts.TitleOpts(title='性别分布'))
     .set_series_opts(label_opts=opts.LabelOpts(is_show=True,position='right'))
)
grid = Grid(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
grid.add(b, grid_opts=opts.GridOpts(pos_left=20%))
grid.render_notebook()
```

<img src="https://img-blog.csdnimg.cn/img_convert/d66ae08e77776310c59483a3fa38a7b9.png" alt="d66ae08e77776310c59483a3fa38a7b9.png">在填写了性别的数据当中，女性竟然多一些，这还是比较出乎意料的。

**5、是否观看**

<img src="https://img-blog.csdnimg.cn/img_convert/e599c7db62a4c7693c40ce14da3c4b2a.png" alt="e599c7db62a4c7693c40ce14da3c4b2a.png">

<img src="https://img-blog.csdnimg.cn/img_convert/30d969bf41110ef7fb6d53dcf67317bc.png" alt="30d969bf41110ef7fb6d53dcf67317bc.png">

大部分人都是在观看了之后才评论的，这要在一定程度上保证了评论和打分的可靠性。

**6、评分分布**

猫眼页面上是10分制，但是在接口当中是5分制。

<img src="https://img-blog.csdnimg.cn/img_convert/82c2470c09d0b52b5409136577838cf2.png" alt="82c2470c09d0b52b5409136577838cf2.png">

<img src="https://img-blog.csdnimg.cn/img_convert/c392b88af2f16bcedb9f8687503463fd.png" alt="c392b88af2f16bcedb9f8687503463fd.png">

<img src="https://img-blog.csdnimg.cn/img_convert/1e30d25043332c9308bc4c0ec6f4d690.png" alt="1e30d25043332c9308bc4c0ec6f4d690.png">

<img src="https://img-blog.csdnimg.cn/img_convert/33780ea1e59b8ec790605021d16c4375.gif" alt="33780ea1e59b8ec790605021d16c4375.gif">

<img src="https://img-blog.csdnimg.cn/img_convert/25d30a9dcb09a02855be998d0fa73701.png" alt="25d30a9dcb09a02855be998d0fa73701.png">

<img src="https://img-blog.csdnimg.cn/img_convert/f62632f360a2feb61d60f41dcaabc977.png" alt="f62632f360a2feb61d60f41dcaabc977.png">

<img src="https://img-blog.csdnimg.cn/img_convert/cd376bd5193b9610b251127e95e557a6.png" alt="cd376bd5193b9610b251127e95e557a6.png">

<img src="https://img-blog.csdnimg.cn/img_convert/d5d79b95e6c170a5243fc9ad30b7dcdd.png" alt="d5d79b95e6c170a5243fc9ad30b7dcdd.png">

**9、用户等级分布**

来看下猫眼评论用户的等级情况，虽然不知道这个等级有啥用

<img src="https://img-blog.csdnimg.cn/img_convert/c7a8d720db15ab72b867fa932ff268cc.png" alt="c7a8d720db15ab72b867fa932ff268cc.png">

<img src="https://img-blog.csdnimg.cn/img_convert/3a8f301b062bf83ef0ca569a46d74ce6.png" alt="3a8f301b062bf83ef0ca569a46d74ce6.png">

大家基本都是 level2，哈哈哈哈，普罗大众嘛!

**10、主创提及次数**

我们再来看看在评论中，各位主创被提及的次数情况.

<img src="https://img-blog.csdnimg.cn/img_convert/0745e1d0851bbdc647b67506dc37610d.png" alt="0745e1d0851bbdc647b67506dc37610d.png">

<img src="https://img-blog.csdnimg.cn/img_convert/18d073f4235812789ccac71017074607.png" alt="18d073f4235812789ccac71017074607.png">

毫无疑问，易烊千玺高居榜首，可能妈妈粉比较多吧，不过人家演技确实也在线.

<img src="https://img-blog.csdnimg.cn/img_convert/40efcba0f3936ed891283ff5e67d3fe3.png" alt="40efcba0f3936ed891283ff5e67d3fe3.png">

### 

### **明日票房预测**

<img src="https://img-blog.csdnimg.cn/img_convert/aef96ab8dec0eb6eb38d25705d9523cc.png" alt="aef96ab8dec0eb6eb38d25705d9523cc.png">

<img src="https://img-blog.csdnimg.cn/img_convert/eb7c257212cdf30146f991dfbc08949d.png" alt="eb7c257212cdf30146f991dfbc08949d.png">

<img src="https://img-blog.csdnimg.cn/img_convert/6df58475a92c4df1f0056225752bf6ea.png" alt="6df58475a92c4df1f0056225752bf6ea.png">

接下来画散点图，看下趋势情况。

<img src="https://img-blog.csdnimg.cn/img_convert/cfab58e4e3eb8db8ff4237651a8cfd76.png" alt="cfab58e4e3eb8db8ff4237651a8cfd76.png">

<img src="https://img-blog.csdnimg.cn/img_convert/d541583017e64b0999be4941d5ba7616.png" alt="d541583017e64b0999be4941d5ba7616.png">

可以看到，从一号开始，单日票房逐步增长，7号达到最高峰，8号开始回落。

下面我们来进行数据拟合，使用 sklearn 提供的 linear_model 来进行。

<img src="https://img-blog.csdnimg.cn/img_convert/68df3090f491629167b6d6a93309ca20.png" alt="68df3090f491629167b6d6a93309ca20.png">

<img src="https://img-blog.csdnimg.cn/img_convert/30d30e918723607a44d7117ce63dfaac.png" alt="30d30e918723607a44d7117ce63dfaac.png">

再根据拟合的结果，我们来预测下明天的票房情况。

<img src="https://img-blog.csdnimg.cn/img_convert/ce1506105f628eca46d129e4d30af0ff.png" alt="ce1506105f628eca46d129e4d30af0ff.png">

<img src="https://img-blog.csdnimg.cn/img_convert/119cc8e400ad615b672cec83177ef441.png" alt="119cc8e400ad615b672cec83177ef441.png">
