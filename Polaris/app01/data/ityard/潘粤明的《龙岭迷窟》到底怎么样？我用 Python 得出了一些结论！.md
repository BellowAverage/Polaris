
--- 
title:  潘粤明的《龙岭迷窟》到底怎么样？我用 Python 得出了一些结论！ 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20200404092614323.jpg" alt=""> 对于天下霸唱的鬼吹灯，相信很多小伙伴都知道，它可谓是国内盗墓寻宝系列小说的巅峰之作，最近得知该系列小说的《龙岭迷窟》部分被制作成了网剧，已经于 4 月 1 日开播了，主要演员潘粤明、姜超、张雨绮等都是一些大家比较熟悉的面孔，网剧质量、剧情还原度等到底怎么样呢？我们通过本文来简单了解一下。

我们都知道要了解一件事情是需要用数据说话的，本文数据来源我们还是选择豆瓣的评论区数据吧，先打开该剧豆瓣地址：`https://movie.douban.com/subject/30488569/` 看一下： <img src="https://img-blog.csdnimg.cn/20200404091940583.PNG" alt=""> 我们发现目前已经有两万七千多人参与了评分且打 4 星和 5 星的人数居多，总体评分 8.3，算是一个比较优秀的分数了。

接着我们将网页向下拉到短评位置，如下所示： <img src="https://img-blog.csdnimg.cn/20200404093227774.PNG#pic_center" alt=""> 目前有六千多人写了短评，但我们知道豆瓣最多只能查看 500 条短评数据，我们的数据来源就取 500 条短评数据。

### 获取数据

首先，我们通过 Python 爬取《龙岭迷窟》500 条豆瓣短评数据，爬取的具体细节这里就不说了，如果不了解的话，可以看一下：。

我们爬取的数据项包括：评论用户、评论时间、评论星级、评论内容，爬取的数据我们存储到 csv 文件中，实现代码如下：

```
def spider():
    url = 'https://accounts.douban.com/j/mobile/login/basic'
    headers = {<!-- -->"User-Agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}
    # 龙岭迷窟网址，为了动态翻页，start 后加了格式化数字，短评页面有 20 条数据，每页增加 20 条
    url_comment = 'https://movie.douban.com/subject/30488569/comments?start=%d&amp;limit=20&amp;sort=new_score&amp;status=P'
    data = {<!-- -->
        'ck': '',
        'name': '自己的用户名',
        'password': '自己的密码',
        'remember': 'false',
        'ticket': ''
    }
    session = requests.session()
    session.post(url=url, headers=headers, data=data)
    # 初始化 4 个 list 分别存用户名、评星、时间、评论文字
    users = []
    stars = []
    times = []
    content = []
    # 抓取 500 条，每页 20 条，这也是豆瓣给的上限
    for i in range(0, 500, 20):
        # 获取 HTML
        data = session.get(url_comment % i, headers=headers)
        # 状态码 200 表是成功
        print('第', i, '页', '状态码：',data.status_code)
        # 暂停 0-1 秒时间，防止IP被封
        time.sleep(random.random())
        # 解析 HTML
        selector = etree.HTML(data.text)
        # 用 xpath 获取单页所有评论
        comments = selector.xpath('//div[@class="comment"]')
        # 遍历所有评论，获取详细信息
        for comment in comments:
            # 获取用户名
            user = comment.xpath('.//h3/span[2]/a/text()')[0]
            # 获取评星
            star = comment.xpath('.//h3/span[2]/span[2]/@class')[0][7:8]
            # 获取时间
            date_time = comment.xpath('.//h3/span[2]/span[3]/@title')
            # 有的时间为空，需要判断下
            if len(date_time) != 0:
                date_time = date_time[0]
                date_time = date_time[:10]
            else:
                date_time = None
            # 获取评论文字
            comment_text = comment.xpath('.//p/span/text()')[0].strip()
            # 添加所有信息到列表
            users.append(user)
            stars.append(star)
            times.append(date_time)
            content.append(comment_text)
    # 用字典包装
    comment_dic = {<!-- -->'user': users, 'star': stars, 'time': times, 'comments': content}
    # 转换成 DataFrame 格式
    comment_df = pd.DataFrame(comment_dic)
    # 保存数据
    comment_df.to_csv('data.csv')
    # 将评论单独再保存下来
    comment_df['comments'].to_csv('comment.csv', index=False)

```

### 分析数据

数据我们已经取到了，接下来我们开始对所获取的数据进行分析。

##### 评论数量

首先，我们来看一下不同时间用户的评论数量，实现代码如下：

```
csv_data = pd.read_csv('data.csv')
df = pd.DataFrame(csv_data)
df_gp = df.groupby(['time']).size()
values = df_gp.values.tolist()
index = df_gp.index.tolist()
# 设置画布大小
plt.figure(figsize=(8, 5))
# 数据
plt.plot(index, values, label='评论数')
# 设置数字标签
for a, b in zip(index, values):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=13, color='black')
plt.title('评论数量随时间变化折线图')
plt.tick_params(labelsize=10)
plt.ylim(0, 300)
plt.legend(loc='upper right')
plt.show()

```

看一下效果图： <img src="https://img-blog.csdnimg.cn/20200404102048567.PNG#pic_center" alt=""> 尽管该剧截止目前只有 4 天的评论数据，我们从图中也不难发现一些规律：我们可以看出 4 月 1 日和 2 日两天的评论数量较多，其中 4 月 1 日为首播日，评论数量多合乎情理，而 4 月 2 日评论数量多于 4 月 1 日，我们可以推测是因为该剧播出之后迅速传播的结果，也就是让更多的人知道了该剧，之后随着时间的推移热度会有所下降，评论数量呈递减的趋势，评论数量变化的趋势也侧面反映了该剧热度变化的大致趋势。

##### 人物角色

接着，我们来看所获取的评论数据中，剧中主要角色被提及的次数，实现代码如下：

```
csv_data = pd.read_csv('data.csv')
roles = {<!-- -->'胡八一':0, '王胖子':0, '雪莉杨':0, '鹧鸪哨':0, '大金牙':0, '陈瞎子':0}
names = list(roles.keys())
for name in names:
    jieba.add_word(name)
for row in csv_data['comments']:
    row = str(row)
    for name in names:
        count = row.count(name)
        roles[name] += count
plt.figure(figsize=(8, 5))
# 数据
plt.bar(list(roles.keys()), list(roles.values()), width=0.5, label='提及次数', color=['r', 'dodgerblue', 'c', 'm', 'y', 'g'])
# 设置数字标签
for a, b in zip(list(roles.keys()), list(roles.values())):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=13, color='black')
plt.title('角色被提及次数柱状图')
plt.xticks(rotation=270)
plt.tick_params(labelsize=10)
plt.ylim(0, 200)
plt.legend(loc='upper right')
plt.show()

```

看一下效果图： <img src="https://img-blog.csdnimg.cn/20200404104025868.PNG#pic_center" alt=""> 从图中我们可以看出被提及角色数量的前三甲为：胡八一、王胖子、大金牙，通过角色被提及的次数，我们也可以大致推测出剧中角色的受欢迎程度，角色被提及的次数越多说明其受欢迎的程度应该越高。

##### 评论星级

再接着，我们看一下该剧每天用户的评论星级，星级最高为 5 星，一天中如果有多条评论星级数据，我们则取其平均值，代码实现如下：

```
csv_data = pd.read_csv('data.csv')
df_time = csv_data.groupby(['time']).size()
df_star = csv_data.groupby(['star']).size()
index = df_time.index.tolist()
value = [0] * len(index)
# 生成字典
dic = dict(zip(index, value))
for k, v in dic.items():
    stars = csv_data.loc[csv_data['time'] == str(k), 'star']
    # 平均值
    avg = np.mean(list(map(int, stars.values.tolist())))
    dic[k] = round(avg ,2)
# 设置画布大小
plt.figure(figsize=(8, 5))
# 数据
plt.plot(list(dic.keys()), list(dic.values()), label='星级', color='red', marker='o')
plt.title('评论星级随时间变化折线图')
plt.tick_params(labelsize=10)
plt.ylim(0, 5)
plt.legend(loc='upper right')
plt.show()

```

看一下效果图： <img src="https://img-blog.csdnimg.cn/20200404105156611.PNG#pic_center" alt=""> 我们从图中可以看出该剧评论星级大致维持在 4 星以上，说明大部分用户对于该剧的质量是比较认可的，评论星级也基本反映出了用户对于该剧的满意度。

##### 词云展示

最后，我们对评论内容进行词云展示，看一下哪些词汇才是评论区的热门词汇，代码实现如下：

```
def jieba_():
    # 打开评论数据文件
    content = open('comment.csv', 'rb').read()
    # jieba 分词
    word_list = jieba.cut(content)
    words = []
    # 过滤掉的词
    remove_words = ['以及', '不会', '一些', '那个', '只有',
                    '不过', '东西', '这个', '所有', '这么',
                    '但是', '全片', '一点', '一部', '一个',
                    '什么', '虽然', '一切', '样子', '一样',
                    '只能', '不是', '一种', '这个', '为了']
    for word in word_list:
        if word not in remove_words:
            words.append(word)
    global word_cloud
    # 用逗号隔开词语
    word_cloud = '，'.join(words)

def cloud():
    # 打开词云背景图
    cloud_mask = np.array(Image.open('bg.jpg'))
    # 定义词云的一些属性
    wc = WordCloud(
        # 背景图分割颜色为白色
        background_color='white',
        # 背景图样
        mask=cloud_mask,
        # 显示最大词数
        max_words=100,
        # 显示中文
        font_path='./fonts/simhei.ttf',
        # 最大尺寸
        max_font_size=80
    )
    global word_cloud
    # 词云函数
    x = wc.generate(word_cloud)
    # 生成词云图片
    image = x.to_image()
    # 展示词云图片
    image.show()
    # 保存词云图片
    wc.to_file('anjia.png')

```

看一下效果图： <img src="https://img-blog.csdnimg.cn/20200404110013775.PNG" alt=""> 如果需要完整代码，可以微信搜索公众号 **Python小二**，后台回复 **龙岭迷窟** 即可。
