
--- 
title:  python基于爬虫技术的海量电影数据分析源码,数据处理分析可视化，GUI界面展示 
tags: []
categories: [] 

---
## 基于爬虫技术的海量电影数据分析

##### 介绍

一个基于爬虫技术的海量电影数据分析系统

##### 系统架构

本系统主要分为四个部分，分别为后端爬虫抓取、数据处理分析可视化、GUI界面展示、启动运行，分别对应getData.py、pyec.py、GUI.py、main.py四个文件。 并且包含data文件夹用于存储系统所需或产生的数据文件。

##### 所需依赖包

numpy、pandas、requests、json、sklearn、webbrowser、tkinter、collections、pyecharts

##### 使用说明

在pycharm中打开项目，直接运行main.py文件即可。

##### 代码详解

###### 1.getData.py

该.py文件主要功能是抓取和读取电影数据，共包含8个函数，代码详解如下：

###### (1)recently()

这一函数主要是抓取最近上映票房排名前十名的电影信息。

```
url = "https://ys.endata.cn/enlib-api/api/movie/getMovie_BoxOffice_Day_Chart.do"

header = {
"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
"Cookie": 'JSESSIONID=b2685bfa-aa4f-4359-ae96-57befaf8d1ec; route=4e39643a15b7003e568cadd862137cf3; Hm_lvt_82932fc4fc199c08b9a83c4c9d02af11=1649834963,1649852471,1649859039,1649900037; Hm_lpvt_82932fc4fc199c08b9a83c4c9d02af11=1649917933'
}

post_BoxOffice_Day_data = {
    'r': 0.7572955414768414,
    'datetype': 'Day',
    'date': datetime.now().strftime('%Y-%m-%d'),
    'sdate': datetime.now().strftime('%Y-%m-%d'),
    'edate': datetime.now().strftime('%Y-%m-%d'),
    'bserviceprice': 1
} 
    ```

```

以上代码块是运行爬虫前的准备工作，包含抓取的网址url、爬虫所需的请求头、请求时需要附带的数据。

```
python
res = requests.post(url, headers=header, data=post_BoxOffice_Day_data).text
json_data = json.loads(res)
data0 = json_data['data']['table0']
data1 = json_data['data']['table1']

```

以上代码块是运行爬虫并将其解析为json形式，方便后面对数据进行取出。

```
movie_rank = []
movie_details_MovieName = []
movie_details_BoxOffice = []
movie_details_ShowCount = []
movie_details_AudienceCount = []
movie_details_Attendance = []

movie_percent_BoxOfficePercent = []
movie_percent_ShowCountPercent = []
movie_percent_AudienceCountPercent = []

```

以上代码是部分定义的所需的数据字段。

```
for i in range(10):
    movie_rank.append(data0[i]['Irank'])
    movie_details_MovieName.append(data0[i]['MovieName'])
    movie_details_BoxOffice.append(data0[i]['BoxOffice'])
    movie_details_ShowCount.append(data0[i]['ShowCount'])
    movie_details_AudienceCount.append(data0[i]['AudienceCount'])
    movie_details_Attendance.append(data0[i]['Attendance'])

```

以上是从json数据中取数据的过程。

```
top10_data = pd.DataFrame({
    "影片排名": movie_rank,
    "影片名称": movie_details_MovieName,
    "影片票房": movie_details_BoxOffice,
    "影片场次": movie_details_ShowCount,
    "影片人次": movie_details_AudienceCount,
    "上座率": movie_details_Attendance,
    "影片票房占比": movie_percent_BoxOfficePercent,
    "影片场次占比": movie_percent_ShowCountPercent,
    "影片人次占比": movie_percent_AudienceCountPercent,
    "一线城市票房": movie_city1_BoxOffice,
    "一线城市场次": movie_city1_ShowCount,
    "一线城市人次": movie_city1_AudienceCount,
    "二线城市票房": movie_city2_BoxOffice,
    "二线城市场次": movie_city2_ShowCount,
    "二线城市人次": movie_city2_AudienceCount,
    "三线城市票房": movie_city3_BoxOffice,
    "三线城市场次": movie_city3_ShowCount,
    "三线城市人次": movie_city3_AudienceCount,
    "四线城市票房": movie_city4_BoxOffice,
    "四线城市场次": movie_city4_ShowCount,
    "四线城市人次": movie_city4_AudienceCount,
    "其它票房": movie_others_BoxOffice,
    "其它场次": movie_others_ShowCount,
    "其它人次": movie_others_AudienceCount
})
print(top10_data)
top10_data.to_csv("data/top10_data.csv", encoding='gbk', index=False)

```

以上是定义数据表并将数据表填满，打印数据表，保存数据表的过程。

###### (2)showing()

这一函数主要抓取最近正在上映的所有电影的基本信息。具体代码块功能参照recently函数。

###### (3)history()

这一函数主要是读取历史电影数据并返回列表格式

```
	def history():
	    data = pd.read_csv("data/moviesBoxOffice.csv", encoding='gbk')
	    data = np.array(data[:100]).tolist()
	    return data

```

以上为利用pandas库读取csv文件，numpy对DataFrame形式数据转换为list格式的过程。

###### (4)predict_data()

这一函数主要是读取历史电影数据进行建模，建模完成后，读取需要预测的在映电影数据，对其进行票房预测并返回。

```
	imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    data = pd.read_csv("data/moviesBoxOffice.csv", encoding='gbk')
    x = data[["总场次", "总人次(万)", "上映天数", "猫眼想看人数", "淘票票想看人数", "豆瓣想看人数"]]
    y = data["总票房(万)"]
    x = imp.fit_transform(np.array(x))

```

以上代码块主要是利用pandas读取历史电影数据，然后利用sklearn库中的SimpleImputer对数据中的空值进行填充。

```
	reg = LinearRegression().fit(x, y)

	predict_data = pd.read_csv("data/recentlyMovies.csv", encoding='gbk')
    name = predict_data['影片名称']
    current = predict_data['累计票房']
    predict_data['当前场次'] = (predict_data['当前场次'] / predict_data["累计上映天数"]) * 50 + predict_data["累计上映天数"]
    predict_data['当前人次'] = (predict_data['当前人次'] / predict_data["累计上映天数"]) * 50 + predict_data["累计上映天数"]
    predict_data['累计上映天数'] = predict_data["累计上映天数"] + 50
    predict_data = predict_data[["当前场次", "当前人次", "累计上映天数", "猫眼想看数", "淘票票想看数", "豆瓣想看数"]]
    predict_data = imp.fit_transform(predict_data)

```

以上代码主要是对历史电影数据进行建模并读取在映电影数据，对在映电影数据进行特征选择和处理

```
	result = reg.predict(predict_data)
    for i in range(len(result)):
        if result[i] &lt; 0:
            result[i] = (0 - result[i])
        result[i] = round((result[i] + current[i]) / 100000000, 2)
    predict_result = pd.DataFrame({
        "影片名称": name,
        "预测票房": result
    })
    predict_result.to_csv("data/predict_result.csv", encoding='gbk', index=False)
    return np.array(predict_result).tolist()

```

以上代码是对在映电影数据进行票房预测和制作输出数据表并返回的过程

###### (5)hotMovies()

这一函数主要是抓取当前在映票房前五的电影七天内的票房数据，具体代码块功能参照recently函数

###### (6)special()

这一函数主要抓取的是当前电影市场特效影厅种类及其票房占比的数据，具体代码块功能参照recently函数。

###### (7)champion_year()

这一函数主要抓取的是近十年来中国电影市场每年票房冠军影片的票房数据，还抓取了近十年国内电影市场的票房和上映影片数量等相关数据，具体代码块功能参照recently函数。

###### (8)Tablets()

这一函数主要是对近期在映电影的排片数据进行抓取并返回，具体代码块功能参照recently函数。

###### 2.pyec.py

该.py文件主要是对getData.py文件获取到的数据进行可视化操作，共有3个函数，代码功能详解如下：

###### (1)History()

该函数主要是对历史电影数据进行可视化，具体代码如下：

```
	csv_file = './moviesBoxOffice.csv'  # 导入csv数据'
    data = pd.read_csv(csv_file, encoding='gbk')
    data_type = data['影片主分类'].value_counts()
    data_BoxOffice = data['总票房(万)'][:10]

```

该代码块主要是读取历史电影票房数据为画图做前期准备工作

```
	a = (
        Bar(init_opts=opts.InitOpts(height="450px", width="900px", theme=ThemeType.MACARONS, bg_color='white'))
            .add_xaxis(list(data_type.index))
            .add_yaxis("类型", list(data_type))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="票房TOP1000类型统计"),
            # datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
    )
    b = (
        Bar(init_opts=opts.InitOpts(height="450px", width="900px", theme=ThemeType.LIGHT))
            .add_xaxis(list(data['影片名称'][:10]))
            .add_yaxis("票房", list(data_BoxOffice))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="票房TOP10总票房统计"),
            # datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
            xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 20}))
    )
    c = (
        Line(init_opts=opts.InitOpts(height="450px", width="900px", theme=ThemeType.LIGHT))
            .add_xaxis(list(data['影片名称'][:10]))
            .add_yaxis("总票房(万)", list(data['总票房(万)'][:10]), is_smooth=True)
            .add_yaxis("首日票房(万)", list(data['首日票房(万)'][:10]), is_smooth=True)
            .add_yaxis("首周票房(万)", list(data['首周票房(万)'][:10]), is_smooth=True)
            .add_yaxis("首周末票房(万)", list(data['首周末票房(万)'][:10]), is_smooth=True)
            .add_yaxis("点映票房(万)", list(data['点映票房(万)'][:10]), is_smooth=True)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             linestyle_opts=opts.LineStyleOpts(width=3))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="票房TOP10各类票房统计", pos_left='top'),
            # datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
            xaxis_opts=opts.AxisOpts(name="影片名称", axislabel_opts={"rotate": 20}),
            yaxis_opts=opts.AxisOpts(name="票房(万)")
        )
    )
    d = (
        Line(init_opts=opts.InitOpts(height="450px", width="900px", theme=ThemeType.MACARONS, bg_color='white'))
            .add_xaxis(list(data['影片名称'][:10]))
            .add_yaxis("总场次", list(data['总场次'][:10]), is_smooth=True)
            .add_yaxis("总人次(万)", list(data['总人次(万)'][:10]), is_smooth=True)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             linestyle_opts=opts.LineStyleOpts(width=3))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="票房TOP10场次人次统计", pos_left='top'),
            # datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
            xaxis_opts=opts.AxisOpts(name="影片名称", axislabel_opts={"rotate": 20}),
            yaxis_opts=opts.AxisOpts(name="次(万)")
        )
    )
    e = (
        Line(init_opts=opts.InitOpts(height="450px", width="900px", theme=ThemeType.LIGHT))
            .add_xaxis(list(data['影片名称'][:10]))
            .add_yaxis("平均票价", list(data['平均票价'][:10]), is_smooth=True)
            .add_yaxis("场均人次", list(data['场均人次'][:10]), is_smooth=True)
            .add_yaxis("上映天数", list(data['上映天数'][:10]), is_smooth=True)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             linestyle_opts=opts.LineStyleOpts(width=3))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="票房TOP10票价统计", pos_left='top'),
            xaxis_opts=opts.AxisOpts(name="影片名称", axislabel_opts={"rotate": 20})
        )
    )
    f = (
        Line(init_opts=opts.InitOpts(height="450px", width="900px", theme=ThemeType.MACARONS, bg_color='white'))
            .add_xaxis(list(data['影片名称'][:10]))
            .add_yaxis("猫眼想看人数", list(data['猫眼想看人数'][:10]), is_smooth=True)
            .add_yaxis("淘票票想看人数", list(data['淘票票想看人数'][:10]), is_smooth=True)
            .add_yaxis("豆瓣想看人数", list(data['豆瓣想看人数'][:10]), is_smooth=True)
            .add_yaxis("网页相关新闻数", list(data['网页相关新闻数'][:10]), is_smooth=True)
            .add_yaxis("微信公众号新闻数", list(data['微信公众号新闻数'][:10]), is_smooth=True)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             linestyle_opts=opts.LineStyleOpts(width=3))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="票房TOP10舆情统计", pos_left='top'),
            xaxis_opts=opts.AxisOpts(name="影片名称", axislabel_opts={"rotate": 20}),
            yaxis_opts=opts.AxisOpts(name="数量")
        )
    )
    g = (
        Line(init_opts=opts.InitOpts(height="450px", width="900px"))
            .add_xaxis(list(data['影片名称'][:10]))
            .add_yaxis("猫眼评分", list(data['猫眼评分'][:10]), is_smooth=True)
            .add_yaxis("淘票票评分", list(data['淘票票评分'][:10]), is_smooth=True)
            .add_yaxis("豆瓣评分", list(data['豆瓣评分'][:10]), is_smooth=True)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             linestyle_opts=opts.LineStyleOpts(width=3))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="票房TOP10口碑统计", pos_left='top'),
            xaxis_opts=opts.AxisOpts(name="影片名称", axislabel_opts={"rotate": 20})
        )
    )
    words_list = []
    for w in data['影片名称']:
        words_list.append(w)
    c1 = Counter(words_list)
    h = (
        WordCloud(init_opts=opts.InitOpts(height="450px", width="900px"))
            .add(series_name="影片词云", data_pair=c1.most_common(), word_size_range=[22, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="片名词云", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    i = (
        Pie(init_opts=opts.InitOpts(height="450px", width="600px"))
            .add(
            "",
            [list(z) for z in zip(data_type.index, list(data_type))],
            radius=["40%", "75%"],
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="电影分类"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    page = (
        Page(page_title="电影票房分析", layout=Page.SimplePageLayout)
            .add(a)
            .add(b)
            .add(h)
            .add(i)
            .add(c)
            .add(d)
            .add(e)
            .add(f)
            .add(g)
            .render("电影票房分析.html")
    )

```

以上代码主要是针对各种数据指标进行数据可视化，最后将其显示到网页供程序调用。a、b两个柱形图分别对票房Top1000的电影类型和票房Top10的总票房进行统计。c、d、e、f、g五个折线图分别是对票房Top10电影的各类票房、场次人次、票价、舆情、口碑五个方面的统计。h、i分别为电影名称词云图和电影分类饼图。

###### (2)Showing

该函数主要是对正在上映的电影进行数据分析，包含在映电影的票房、场次、人次、上座率五个柱形统计图，影片票房占比、场次占比、人次占比三个饼状统计图，影片地域分布票房、场次、人次三个层叠柱形图。具体代码功能与History函数相近。

###### (3)Industry

该函数主要是对近期电影行业及电影行业历史数据的可视化，主要包括热门电影票房趋势折线统计图，特效厅票房占比奋不饼状图，历年冠军影片票房趋势柱形折线图，影片年票房及新映影片趋势柱形折线图。具体代码功能与History函数相近。

###### 3.GUI.py

该.py文件主要是为系统构建GUI界面，共有15个函数，具体代码详解如下：

###### (1)create_tree_showing

该函数主要是为正在上映的电影数据创建数据表格。具体代码如下：

```
	# 表格
    columns = ("排名", "影片名称", '当前票房', '上映日期', '累计票房', '当前场次', '当前人次', '票房占比', '累计上映天数',
               '当前统计天数', '黄金场票房', '黄金场场次', '黄金场票房占比', '黄金场场次占比', '黄金场人次占比')
    treeview = ttk.Treeview(self.frame_l, height=30, show="headings", columns=columns)
    treeview.column("排名", width=50, anchor='center')
    treeview.column("影片名称", width=100, anchor='center')
    treeview.column("当前票房", width=75, anchor='center')
    treeview.column("上映日期", width=100, anchor='center')
    treeview.column("累计票房", width=75, anchor='center')
    treeview.column("当前场次", width=75, anchor='center')
    treeview.column("当前人次", width=75, anchor='center')
    treeview.column("票房占比", width=50, anchor='center')
    treeview.column("累计上映天数", width=50, anchor='center')
    treeview.column("当前统计天数", width=50, anchor='center')
    treeview.column("黄金场票房", width=75, anchor='center')
    treeview.column("黄金场场次", width=50, anchor='center')
    treeview.column("黄金场票房占比", width=50, anchor='center')
    treeview.column("黄金场场次占比", width=50, anchor='center')
    treeview.column("黄金场人次占比", width=50, anchor='center')

```

该代码块先是确定数据表头，然后创建表格并设置其父窗体，表格一次性显示数据行数，是否显示表头等参数，然后分别设置表格数据列及每列的宽度。

```
	treeview.heading("排名", text="排名")  # 显示表头
    treeview.heading("影片名称", text="影片名称")
    treeview.heading("当前票房", text="当前票房")
    treeview.heading("上映日期", text="上映日期")
    treeview.heading("累计票房", text="累计票房")
    treeview.heading("当前场次", text="当前场次")
    treeview.heading("当前人次", text="当前人次")
    treeview.heading("票房占比", text="票房占比")
    treeview.heading("累计上映天数", text="累计上映天数")
    treeview.heading("当前统计天数", text="当前统计天数")
    treeview.heading("黄金场票房", text="黄金场票房")
    treeview.heading("黄金场场次", text="黄金场场次")
    treeview.heading("黄金场票房占比", text="黄金场票房占比")
    treeview.heading("黄金场场次占比", text="黄金场场次占比")
    treeview.heading("黄金场人次占比", text="黄金场人次占比")

    # 垂直滚动条
    vbar = ttk.Scrollbar(self.frame_r, command=treeview.yview)
    treeview.configure(yscrollcommand=vbar.set)

    treeview.pack()
    self.treeview = treeview
    vbar.pack(side=RIGHT, fill=Y)
    self.vbar = vbar

```

该代码块设置表头文本信息，再设置该信息表的垂直滚动条。

###### (2)create_tree_tablets

该函数主要是为在映电影的排片数据创建数据表格。具体代码与create_tree_showing类似。

###### (3)create_tree_history

该函数主要是为历史电影数据创建数据表格。具体代码与create_tree_showing类似。

###### (4)create_tree_predict

该函数主要是为在映电影票房预测结果数据创建数据表格。具体代码与create_tree_showing类似。

###### (5)clear_tree

该函数主要功能是在切换展示数据表格时，对已展示表格数据进行清除。具体代码如下:

```
	def clear_tree(self, tree):
        '''
        清空表格
        '''
        tree.destroy()
        self.vbar.destroy()

```

该函数有一个tree参数，首先对tree进行销毁，再对该表格的垂直滚动条进行销毁。

###### (6)showing

该函数对应按钮’在映电影’，用于实现获取在映电影数据功能，具体代码如下：

```
	def showing(self):
        if self.treeview is not None:
            self.clear_tree(self.treeview)  # 清空表格

        self.create_tree_showing()
        self.B_0['text'] = '正在努力搜索'

        showing()
        list = np.array(pd.read_csv("data/recentlyMovies.csv", encoding='gbk')).tolist()
        self.add_tree(list, self.treeview)  # 将数据添加到tree中

        self.B_0['state'] = NORMAL
        self.B_0['text'] = '在映电影'

```

该代码块首先判断数据表格是否存在数据，如果存在即清空。然后创建在映电影数据表格，设置按钮文本变化，然后调用getData.py中的showing函数获取在映电影数据。再将数据添加到数据表格中进行展示，最后设置按钮文本为初始状态。

###### (7)history

该函数对应按钮’历史电影’，用于实现获取历史电影数据功能，具体代码与showing函数类似。

###### (8)predict

该函数对应按钮’在映电影票房预测’，用于实现对在映电影票房预测并展示，具体代码与showing函数类似。

###### (9)tablets

该函数对应按钮’拍片分析’，用于实现获取排片分析数据功能，具体代码与showing函数类似。

###### (10)center_window

该函数是创建整个GUI窗体的函数，具体代码如下：

```
	def center_window(self, root, w, h):
        """
        窗口居于屏幕中央
        :param root: root
        :param w: 窗口宽度
        :param h: 窗口高度
        :return:
        """
        # 获取屏幕 宽、高
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()

        # 计算 x, y 位置
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

```

###### (11)clicking

该函数对应’在映电影分析’按钮，用于跳转在映电影分析网页，具体代码如下：

```
	def clicking(self):
        recently()
        Showing()
        webbrowser.open("在映电影分析.html")

```

先调用getData.py下的recently函数获取在映电影数据，再调用pyec.py文件下的Showing函数进行统计图表制作，最后跳转到数据图表网页。

###### (12)clicked

该函数对应’历史数据分析’按钮，用于跳转电影票房分析网页，具体代码与clicking相似。

###### (13)industry

该函数对应’数据大盘’按钮，用于跳转数据大盘网页，具体代码与clicking相似。

###### (14)ui_process

该函数主要是对GUI窗体控件等进行布局，具体代码如下：

```
	def ui_process(self):
        root = Tk()
        self.root = root

```

该代码块主要是创建根窗体。

```
        root.title("电影数据分析")
        self.center_window(root, 1500, 750)
        root.resizable(0, 0)
        root['highlightcolor'] = 'yellow'

```

该代码块主要是设置GUI的名称，大小，整体高亮颜色。

```
        labelframe = LabelFrame(root, width=1500, height=750, background="white")
        labelframe.place(x=5, y=5)
        self.labelframe = labelframe
        # 图片
        photo = tk.PhotoImage(file="logo.png")
        Lab = tk.Label(root, image=photo, )
        Lab.place(x=10, y=10)

```

改代码块主要是对内部子窗体进行了初始化并且在子窗体的左上角添加了一张logo图片。

```
        # 查询按钮
        B_0 = Button(labelframe, text="在映电影", background="white")
        B_0.place(x=400, y=25, width=100, height=50)
        self.B_0 = B_0
        B_0.configure(command=lambda: thread_it(self.showing()))  # 按钮绑定单击事件

        B_1 = Button(labelframe, text="在映前十数据分析", background="white")
        B_1.place(x=550, y=25, width=100, height=50)
        self.B_1 = B_1
        B_1.configure(command=lambda: thread_it(self.clicking()))  # 按钮绑定单击事件

        B_4 = Button(labelframe, text="在映电影票房预测", background="white")
        B_4.place(x=700, y=25, width=100, height=50)
        self.B_4 = B_4
        B_4.configure(command=lambda: thread_it(self.predict()))

        B_2 = Button(labelframe, text="历史电影", background="white")
        B_2.place(x=850, y=25, width=100, height=50)
        self.B_2 = B_2
        B_2.configure(command=lambda: thread_it(self.history()))

        B_3 = Button(labelframe, text="历史数据分析", background="white")
        B_3.place(x=1000, y=25, width=100, height=50)
        self.B_3 = B_3
        B_3.configure(command=lambda: thread_it(self.clicked()))

        B_5 = Button(labelframe, text="数据大盘", background="white")
        B_5.place(x=1150, y=25, width=100, height=50)
        self.B_5 = B_5
        B_5.configure(command=lambda: thread_it(self.industry()))

        B_6 = Button(labelframe, text="排片分析", background="white")
        B_6.place(x=1300, y=25, width=100, height=50)
        self.B_6 = B_6
        B_6.configure(command=lambda: thread_it(self.tablets()))

```

以上代码块主要是在子窗体设置了各个功能对应的按钮。

```
        # 框架布局，承载多个控件
        frame_root = Frame(labelframe)
        frame_l = Frame(frame_root)
        frame_r = Frame(frame_root)
        frame_d = Frame(frame_root)
        self.frame_root = frame_root
        self.frame_l = frame_l
        self.frame_r = frame_r

```

该代码块设置了整体窗体的布局，以及各个子窗体控件的设置。

```
        # 框架的位置布局
        frame_l.grid(row=0, column=0, sticky=NSEW)
        frame_r.grid(row=0, column=1, sticky=NS)
        frame_root.place(x=10, y=100)

```

该代码块实现了整体窗体的位置布局

```
        root.columnconfigure(0, weight=1)
        root.mainloop()

```

改代码块设置了窗体列参数及运行了整个窗体

###### 4.main.py

该函数是整个系统的GUI入口，调用并运行了GUI。具体代码如下：

```
	from GUI import uiob
	
	if __name__ == '__main__':
	    ui = uiob()
	    ui.ui_process()

```

完整代码下载地址：
