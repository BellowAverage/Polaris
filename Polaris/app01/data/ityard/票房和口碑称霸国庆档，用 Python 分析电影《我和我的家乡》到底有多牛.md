
--- 
title:  票房和口碑称霸国庆档，用 Python 分析电影《我和我的家乡》到底有多牛 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20201005072819661.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt=""> 今年的国庆档电影市场的表现还是比较强势的，两名主力《我和我的家乡》和《姜子牙》起到了很好的带头作用。

《姜子牙》首日破 2 亿，一举刷新由《哪吒之魔童降世》保持的中国影市动画电影首日票房纪录，但因其后续口碑下滑，目前已被《我和我的家乡》在口碑和票房上实现了全面的超越，如不出意外，《我和我的家乡》将会是今年国庆档的最大赢家。

<img src="https://img-blog.csdnimg.cn/20201005072903193.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

从上图中我们可以看出《我和我的家乡》在猫眼上目前有 29.6 万人评分，总体评分 9.3，可以说是一个相当不错的成绩了，本文我们爬取该片的猫眼电影评论，一起分析下这部影片评论区的内容。

### 爬取

首先，我们来爬取猫眼电影评论数据，因 PC 端只能看到猫眼上的几条评论，所以我们要借助 APP 接口来爬取，接口格式为：`http://m.maoyan.com/mmdb/comments/movie/movieid.json?_v_=yes&amp;offset=15&amp;startTime=xxx`，两个参数说明如下：
- movieid：网站中每部影片的唯一 id- startTime：当前页面中第一条评论的时间，每页共有 15 条评论
爬取的主要实现代码如下：

```
# 获取页面内容
def get_page(url):
    headers = {<!-- -->
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'
                      '/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'accept': '*/*'
    }
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.text
    except requests.HTTPError as e:
        print(e)
    except requests.RequestException as e:
        print(e)
    except:
        print("出错了")

# 解析接口返回数据
def parse_data(html):
    json_data = json.loads(html)['cmts']
    comments = []
    # 解析数据并存入数组
    try:
        for item in json_data:
            comment = []
            comment.append(item['nickName']) # 昵称
            comment.append(item['cityName'] if 'cityName' in item else '') # 城市
            comment.append(item['content'].strip().replace('\n', '')) # 内容
            comment.append(item['score']) # 星级
            comment.append(item['startTime'])
            comment.append(item['time']) # 日期
            comment.append(item['approve']) # 赞数
            comment.append(item['reply']) # 回复数
            if 'gender' in item:
                comment.append(item['gender'])  # 性别
            comments.append(comment)
        return comments
    except Exception as e:
        print(comment)
        print(e)

# 保存数据，写入 csv
def save_data(comments):
    filename = 'comments.csv'
    dataObject = pd.DataFrame(comments)
    dataObject.to_csv(filename, mode='a', index=False, sep=',', header=False, encoding='utf_8_sig')

```

本文我们爬取了 2w 条左右评论数据，并将爬取的数据保存到了 csv 文件中。

### 数据分析

##### 评分星级

首先，我们看一下爬取数据中每个评分星级的比例情况，主要实现代码如下：

```
# 评分星级
rates = []
for s in df.iloc[:, 3]:
    rates.append(s)
sx = ["五星", "四星", "三星", "二星", "一星"]
sy = [
    str(rates.count(5.0) + rates.count(4.5)),
    str(rates.count(4.0) + rates.count(3.5)),
    str(rates.count(3.0) + rates.count(2.5)),
    str(rates.count(2.0) + rates.count(1.5)),
    str(rates.count(1.0) + rates.count(0.5))
]
(
    Pie(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width='700px', height='400px'))
    .add("", list(zip(sx, sy)), radius=["40%", "70%"])
    .set_global_opts(title_opts=opts.TitleOpts(title="评分星级比例", subtitle="数据来源：猫眼电影", pos_left = "left"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%", font_size=12))
).render_notebook()

```

效果如下：

<img src="https://img-blog.csdnimg.cn/20201005073005683.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

从图中我们可以看出：有接近 9 成的人给了该片 5 星，1、2、3 星总共占比只有 5% 左右，说明该片的质量得到了大部分人的认可。

##### 性别比例

我们接着看评论人中的性别情况，主要实现代码如下：

```
# 性别比例
rates = []
for s in df.iloc[:, 8]:
    if s != 1 and s != 2:
        s = 3
    rates.append(s)
gx = ["男", "女", "未知"]
gy = [
    rates.count(1),
    rates.count(2),
    rates.count(3)
]
(
    Pie(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width="700px", height="400px"))
    .add("", list(zip(gx, gy)))
    .set_global_opts(title_opts=opts.TitleOpts(title="性别比例", subtitle="数据来源：猫眼电影", pos_left = "left"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%", font_size=12))
).render_notebook()

```

效果如下：

<img src="https://img-blog.csdnimg.cn/20201005073024802.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

通过上图我们可以发现：大部分人是比较注重自己的隐私的，没有显示自己的性别，通过性别可见的数据，我们可以发现男人和女人在评论区的活跃程度比较接近，女人略高一些。

##### 位置分布

我们再接着看评论人位置分布情况，先看下评论数量前 100 名的位置坐标情况，主要代码实现如下：

```
cities = []
for city in df.iloc[:, 1]:
    if city != "":
        cities.append(city)
data = Counter(cities).most_common(100)
gx1 = []
gy1 = []
for c in data:
    gx1.append(c[0])
    gy1.append(c[1])
geo = Geo(init_opts=opts.InitOpts(width="700px", height="400px", theme=ThemeType.DARK, bg_color="#404a59"))
(
    geo.add_schema(maptype="china", itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"))
    .add("评论数量", list(zip(gx1, gy1)))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
       toolbox_opts=opts.ToolboxOpts,
       title_opts=opts.TitleOpts(title="位置分布地理坐标", subtitle="数据来源：猫眼电影", pos_left = "left"),
       visualmap_opts=opts.VisualMapOpts(max_=500, is_piecewise=True)
    )
).render_notebook()

```

效果如下：

<img src="https://img-blog.csdnimg.cn/20201005073053924.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

下面再通过柱状图来展示一下评论数量前 15 名的城市，主要代码实现如下：

```
data_top15 = Counter(cities).most_common(15)
gx2 = []
gy2 = []
for c in data_top15:
    gx2.append(c[0])
    gy2.append(c[1])
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width="700px", height="400px"))
    .add_xaxis(gx2)
    .add_yaxis("", gy2)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="城市来源 TOP15", subtitle="数据来源：猫眼电影", pos_left = "center")
    )
).render_notebook()

```

效果如下：

<img src="https://img-blog.csdnimg.cn/20201005073701443.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

通过以上两图，我们可以直观的看出哪些城市的人在该片下的评论数量多少，进而可以相应的了解到其对该片的感兴趣程度。

##### 时评数量

我们接着看 24 小时中的评论数量，主要代码实现如下：

```
times = df.iloc[:, 5]
hours = []
for t in times:
    hours.append(str(t[11:13]))
hdata = sorted(Counter(hours).most_common())
hx = []
hy = []
for c in hdata:
    hx.append(c[0])
    hy.append(c[1])
(
    Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width="700px", height="400px"))
    .add_xaxis(hx)
    .add_yaxis("", hy, areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="24小时评论数量", subtitle="数据来源：猫眼电影", pos_left = "center")
    )
).render_notebook()

```

效果如下：

<img src="https://img-blog.csdnimg.cn/20201005073113290.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

从图中我们可以看出大家在下午 ~ 晚间活跃程度比较高，因 19 点左右是晚饭时间，这个时间段评论数量下降也合乎常理。

##### 主要演员

我们接着来看主要演员（包括其饰演的角色）在评论区中被提及的情况，主要代码实现如下：

```
cts_list = df.iloc[:, 2]
cts_str ="".join([str(i) for i in cts_list])
px = ["黄渤", "王宝强", "刘昊然", "葛优", "刘敏涛", "范伟", "张译", "邓超", "闫妮", "沈腾", "马丽"]
py = [cts_str.count("黄渤") + cts_str.count("黄大宝"), cts_str.count("王宝强") + cts_str.count("老唐"),
      cts_str.count("刘昊然") + cts_str.count("小秦"), cts_str.count("葛优") + cts_str.count("张北京"),
      cts_str.count("刘敏涛") + cts_str.count("玲子"), cts_str.count("范伟") + cts_str.count("老范"),
      cts_str.count("张译") + cts_str.count("姜前方"), cts_str.count("邓超") + cts_str.count("乔树林"),
      cts_str.count("闫妮") + cts_str.count("闫飞燕"), cts_str.count("沈腾") + cts_str.count("马亮"),
      cts_str.count("马丽") + cts_str.count("秋霞")]
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width="700px", height="400px"))
    .add_xaxis(px)
    .add_yaxis("", py)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="主要演员及其饰演角色被提及次数", subtitle="数据来源：猫眼电影", pos_left = "center")
    )
).render_notebook()

```

效果如下：

<img src="https://img-blog.csdnimg.cn/2020100507312933.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

从图中我们可以看出主要演员在评论区出现次数的前三强为：沈腾、范伟和邓超，进而说明这几位演员的热度比较高，在评论区引起了大家广泛的热议。

##### 电影单元

我们接着看每个电影单元在评论区被提及的情况，主要代码实现如下：

```
mx = ["天上掉下个UFO", "北京好人", "最后一课", "回乡之路", "神笔马亮"]
my = [cts_str.count("天上掉下个UFO"), cts_str.count("北京好人"), cts_str.count("最后一课"), cts_str.count("回乡之路"), cts_str.count("神笔马亮")]
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width="700px", height="400px"))
    .add_xaxis(mx)
    .add_yaxis("", my)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="电影单元被提及次数", subtitle="", pos_left = "center")
    )
).render_notebook()

```

效果如下：

<img src="https://img-blog.csdnimg.cn/20201005073147818.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

从图中我们可以看出电影单元《最后一课》被提及的次数超过了其它几个单元被提及次数的总和，进而可以看出其热度比较高，引起了大家的共鸣，有点一枝独秀的感觉。

### 词云展示

##### 整体词云

首先我们来看一下整体评论的词云，代码实现如下：

```
cts_list = df.iloc[:, 2]
cts_str ="".join([str(i) for i in cts_list])
stylecloud.gen_stylecloud(text=cts_str, max_words=400,
                          collocations=False,
                          font_path="SIMLI.TTF",
                          icon_name="fas fa-home",
                          size=800,
                          output_name="total.png")
Image(filename="total.png")

```

效果如下：

<img src="https://img-blog.csdnimg.cn/20201005073213134.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="500">

从图中我们可以直观的看出：好看、很好看、值的一看、不错、最后一课等被提及的次数比较多，说明大多数人对影片是比较满意，电影单元最后一课热度比较高、引起了很多人的共鸣。

##### 热评词云

最后，我们看一下热门评论（点赞多、回复多的评论内容）的词云，代码实现如下：

```
hot_str = ""
for index, row in df.iterrows():
    content = row[2]
    support = row[6]
    reply = row[7]
    if(support &gt; 30):
        hot_str += content
    elif (reply &gt; 5):
        hot_str += content
stylecloud.gen_stylecloud(text=hot_str, max_words=200,
                          collocations=False,
                          font_path="SIMLI.TTF",
                          icon_name="fas fa-fire",
                          size=800,
                          output_name="hot.png")
Image(filename="hot.png")

```

效果如下：

<img src="https://img-blog.csdnimg.cn/20201005073238463.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="500">

这个热门评论的画风和之前有点不一样了，最醒目（最大）的词汇是：UFO、难看、电影倒是没看、和对象开演前十分钟分手了… 最后这个不多说了，大家自行体会吧~

因采集的评论数据有限，可能与实际情况存在一定的偏差，大家理性看待即可。
