
--- 
title:  超全的 100 个 Pandas 函数汇总，建议收藏 
tags: []
categories: [] 

---
来源：吊车尾学院

我整理了100个Pandas常用的函数，分别分为6类：统计汇总函数、数据清洗函数、数据筛选、绘图与元素级运算函数、时间序列函数和其他函数。

**统计汇总函数**


<td colspan="1" rowspan="1">**函数**</td><td colspan="1" rowspan="1">**含义**</td>
<td colspan="1" rowspan="1">min()</td><td colspan="1" rowspan="1">计算最小值</td>

计算最小值
<td colspan="1" rowspan="1">max()</td><td colspan="1" rowspan="1">计算最大值</td>

计算最大值
<td colspan="1" rowspan="1">sum()</td><td colspan="1" rowspan="1">求和</td>

求和
<td colspan="1" rowspan="1">mean()</td><td colspan="1" rowspan="1">计算平均值</td>

计算平均值
<td colspan="1" rowspan="1">count()</td><td colspan="1" rowspan="1">计数（统计非缺失元素的个数）</td>

计数（统计非缺失元素的个数）
<td colspan="1" rowspan="1">size()</td><td colspan="1" rowspan="1">计数（统计所有元素的个数）</td>

计数（统计所有元素的个数）
<td colspan="1" rowspan="1">median()</td><td colspan="1" rowspan="1">计算中位数</td>

计算中位数
<td colspan="1" rowspan="1">var()</td><td colspan="1" rowspan="1">计算方差</td>

计算方差
<td colspan="1" rowspan="1">std()</td><td colspan="1" rowspan="1">计算标准差</td>

计算标准差
<td colspan="1" rowspan="1">quantile()</td><td colspan="1" rowspan="1">计算任意分位数</td>

计算任意分位数
<td colspan="1" rowspan="1">cov()</td><td colspan="1" rowspan="1">计算协方差</td>

计算协方差
<td colspan="1" rowspan="1">corr()</td><td colspan="1" rowspan="1">计算相关系数</td>

计算相关系数
<td colspan="1" rowspan="1">skew()</td><td colspan="1" rowspan="1">计算偏度</td>

计算偏度
<td colspan="1" rowspan="1">kurt()</td><td colspan="1" rowspan="1">计算峰度</td>

计算峰度
<td colspan="1" rowspan="1">mode()</td><td colspan="1" rowspan="1">计算众数</td>

计算众数
<td colspan="1" rowspan="1">describe()</td><td colspan="1" rowspan="1">描述性统计（一次性返回多个统计结果）</td>

描述性统计（一次性返回多个统计结果）
<td colspan="1" rowspan="1">groupby()</td><td colspan="1" rowspan="1">分组</td>

分组
<td colspan="1" rowspan="1">aggregate()</td><td colspan="1" rowspan="1">聚合运算（可以自定义统计函数）</td>

聚合运算（可以自定义统计函数）
<td colspan="1" rowspan="1">argmin()</td><td colspan="1" rowspan="1">寻找最小值所在位置</td>

寻找最小值所在位置
<td colspan="1" rowspan="1">argmax()</td><td colspan="1" rowspan="1">寻找最大值所在位置</td>

寻找最大值所在位置
<td colspan="1" rowspan="1">any()</td><td colspan="1" rowspan="1">等价于逻辑“或”</td>

等价于逻辑“或”
<td colspan="1" rowspan="1">all()</td><td colspan="1" rowspan="1">等价于逻辑“与”</td>

等价于逻辑“与”
<td colspan="1" rowspan="1">value_counts()</td><td colspan="1" rowspan="1">频次统计</td>

频次统计
<td colspan="1" rowspan="1">cumsum()</td><td colspan="1" rowspan="1">运算累计和</td>

运算累计和
<td colspan="1" rowspan="1">cumprod()</td><td colspan="1" rowspan="1">运算累计积</td>

运算累计积
<td colspan="1" rowspan="1">pct­­_change()</td><td colspan="1" rowspan="1">运算比率（后一个元素与前一个元素的比率）</td>

运算比率（后一个元素与前一个元素的比率）



**数据清洗函数**


<td colspan="1" rowspan="1">**函数**</td><td colspan="1" rowspan="1">**含义**</td>
<td colspan="1" rowspan="1">duplicated()</td><td colspan="1" rowspan="1">判断序列元素是否重复</td>

判断序列元素是否重复
<td colspan="1" rowspan="1">drop_duplicates()</td><td colspan="1" rowspan="1">删除重复值</td>

删除重复值
<td colspan="1" rowspan="1">hasnans()</td><td colspan="1" rowspan="1">判断序列是否存在缺失（返回TRUE或FALSE）</td>

判断序列是否存在缺失（返回TRUE或FALSE）
<td colspan="1" rowspan="1">isnull()</td><td colspan="1" rowspan="1">判断序列元素是否为缺失（返回与序列长度一样的bool值）</td>

判断序列元素是否为缺失（返回与序列长度一样的bool值）
<td colspan="1" rowspan="1">notnull()</td><td colspan="1" rowspan="1">判断序列元素是否不为缺失（返回与序列长度一样的bool值）</td>

判断序列元素是否不为缺失（返回与序列长度一样的bool值）
<td colspan="1" rowspan="1">dropna()</td><td colspan="1" rowspan="1">删除缺失值</td>

删除缺失值
<td colspan="1" rowspan="1">fillna()</td><td colspan="1" rowspan="1">缺失值填充</td>

缺失值填充
<td colspan="1" rowspan="1">ffill()</td><td colspan="1" rowspan="1">前向后填充缺失值（使用缺失值的前一个元素填充）</td>

前向后填充缺失值（使用缺失值的前一个元素填充）
<td colspan="1" rowspan="1">bfill()</td><td colspan="1" rowspan="1">后向填充缺失值（使用缺失值的后一个元素填充）</td>

后向填充缺失值（使用缺失值的后一个元素填充）
<td colspan="1" rowspan="1">dtypes()</td><td colspan="1" rowspan="1">检查数据类型</td>

检查数据类型
<td colspan="1" rowspan="1">astype()</td><td colspan="1" rowspan="1">类型强制转换</td>

类型强制转换
<td colspan="1" rowspan="1">pd.to_datetime</td><td colspan="1" rowspan="1">转日期时间型</td>

转日期时间型
<td colspan="1" rowspan="1">factorize()</td><td colspan="1" rowspan="1">因子化转换</td>

因子化转换
<td colspan="1" rowspan="1">sample()</td><td colspan="1" rowspan="1">抽样</td>

抽样
<td colspan="1" rowspan="1">where()</td><td colspan="1" rowspan="1">基于条件判断的值替换</td>

基于条件判断的值替换
<td colspan="1" rowspan="1">replace()</td><td colspan="1" rowspan="1">按值替换（不可使用正则）</td>

按值替换（不可使用正则）
<td colspan="1" rowspan="1">str.replace()</td><td colspan="1" rowspan="1">按值替换（可使用正则）</td>

按值替换（可使用正则）
<td colspan="1" rowspan="1">str.split.str()</td><td colspan="1" rowspan="1">字符分隔</td>

字符分隔



**数据筛选函数**


<td colspan="1" rowspan="1">**函数**</td><td colspan="1" rowspan="1">**含义**</td>
<td colspan="1" rowspan="1">isin()</td><td colspan="1" rowspan="1">成员关系判断</td>

成员关系判断
<td colspan="1" rowspan="1">between()</td><td colspan="1" rowspan="1">区间判断</td>

区间判断
<td colspan="1" rowspan="1">loc()</td><td colspan="1" rowspan="1">条件判断（可使用在数据框中）</td>

条件判断（可使用在数据框中）
<td colspan="1" rowspan="1">iloc()</td><td colspan="1" rowspan="1">索引判断（可使用在数据框中）</td>

索引判断（可使用在数据框中）
<td colspan="1" rowspan="1">compress()</td><td colspan="1" rowspan="1">条件判断</td>

条件判断
<td colspan="1" rowspan="1">nlargest()</td><td colspan="1" rowspan="1">搜寻最大的n个元素</td>

搜寻最大的n个元素
<td colspan="1" rowspan="1">nsmallest()</td><td colspan="1" rowspan="1">搜寻最小的n个元素</td>

搜寻最小的n个元素
<td colspan="1" rowspan="1">str.findall()</td><td colspan="1" rowspan="1">子串查询（可使用正则）</td>

子串查询（可使用正则）



**绘图与元素级运算函数**


<td colspan="1" rowspan="1">**函数**</td><td colspan="1" rowspan="1">**含义**</td>
<td colspan="1" rowspan="1">hist()</td><td colspan="1" rowspan="1">绘制直方图</td>

绘制直方图
<td colspan="1" rowspan="1">plot()</td><td colspan="1" rowspan="1">可基于kind参数绘制更多图形（饼图，折线图，箱线图等）</td>

可基于kind参数绘制更多图形（饼图，折线图，箱线图等）
<td colspan="1" rowspan="1">map()</td><td colspan="1" rowspan="1">元素映射</td>

元素映射
<td colspan="1" rowspan="1">apply()</td><td colspan="1" rowspan="1">基于自定义函数的元素级操作</td>

基于自定义函数的元素级操作



**时间序列函数**


<td colspan="1" rowspan="1">**函数**</td><td colspan="1" rowspan="1">**含义**</td>
<td colspan="1" rowspan="1">dt.date()</td><td colspan="1" rowspan="1">抽取出日期值</td>

抽取出日期值
<td colspan="1" rowspan="1">dt.time()</td><td colspan="1" rowspan="1">抽取出时间（时分秒）</td>

抽取出时间（时分秒）
<td colspan="1" rowspan="1">dt.year()</td><td colspan="1" rowspan="1">抽取出年</td>

抽取出年
<td colspan="1" rowspan="1">dt.mouth()</td><td colspan="1" rowspan="1">抽取出月</td>

抽取出月
<td colspan="1" rowspan="1">dt.day()</td><td colspan="1" rowspan="1">抽取出日</td>

抽取出日
<td colspan="1" rowspan="1">dt.hour()</td><td colspan="1" rowspan="1">抽取出时</td>

抽取出时
<td colspan="1" rowspan="1">dt.minute()</td><td colspan="1" rowspan="1">抽取出分钟</td>

抽取出分钟
<td colspan="1" rowspan="1">dt.second()</td><td colspan="1" rowspan="1">抽取出秒</td>

抽取出秒
<td colspan="1" rowspan="1">dt.quarter()</td><td colspan="1" rowspan="1">抽取出季度</td>

抽取出季度
<td colspan="1" rowspan="1">dt.weekday()</td><td colspan="1" rowspan="1">抽取出星期几（返回数值型）</td>

抽取出星期几（返回数值型）
<td colspan="1" rowspan="1">dt.weekday_name()</td><td colspan="1" rowspan="1">抽取出星期几（返回字符型）</td>

抽取出星期几（返回字符型）
<td colspan="1" rowspan="1">dt.week()</td><td colspan="1" rowspan="1">抽取出年中的第几周</td>

抽取出年中的第几周
<td colspan="1" rowspan="1">dt.dayofyear()</td><td colspan="1" rowspan="1">抽取出年中的第几天</td>

抽取出年中的第几天
<td colspan="1" rowspan="1">dt.daysinmonth()</td><td colspan="1" rowspan="1">抽取出月对应的最大天数</td>

抽取出月对应的最大天数
<td colspan="1" rowspan="1">dt.is_month_start()</td><td colspan="1" rowspan="1">判断日期是否为当月的第一天</td>

判断日期是否为当月的第一天
<td colspan="1" rowspan="1">dt.is_month_end()</td><td colspan="1" rowspan="1">判断日期是否为当月的最后一天</td>

判断日期是否为当月的最后一天
<td colspan="1" rowspan="1">dt.is_quarter_start()</td><td colspan="1" rowspan="1">判断日期是否为当季度的第一天</td>

判断日期是否为当季度的第一天
<td colspan="1" rowspan="1">dt.is_quarter_end()</td><td colspan="1" rowspan="1">判断日期是否为当季度的最后一天</td>

判断日期是否为当季度的最后一天
<td colspan="1" rowspan="1">dt.is_year_start()</td><td colspan="1" rowspan="1">判断日期是否为当年的第一天</td>

判断日期是否为当年的第一天
<td colspan="1" rowspan="1">dt.is_year_end()</td><td colspan="1" rowspan="1">判断日期是否为当年的最后一天</td>

判断日期是否为当年的最后一天
<td colspan="1" rowspan="1">dt.is_leap_year()</td><td colspan="1" rowspan="1">判断日期是否为闰年</td>

判断日期是否为闰年



**其它函数**


<td colspan="1" rowspan="1">**函数**</td><td colspan="1" rowspan="1">**含义**</td>
<td colspan="1" rowspan="1">append()</td><td colspan="1" rowspan="1">序列元素的追加（需指定其他序列）</td>

序列元素的追加（需指定其他序列）
<td colspan="1" rowspan="1">diff()</td><td colspan="1" rowspan="1">一阶差分</td>

一阶差分
<td colspan="1" rowspan="1">round()</td><td colspan="1" rowspan="1">元素的四舍五入</td>

元素的四舍五入
<td colspan="1" rowspan="1">sort_values()</td><td colspan="1" rowspan="1">按值排序</td>

按值排序
<td colspan="1" rowspan="1">sort_index()</td><td colspan="1" rowspan="1">按索引排序</td>

按索引排序
<td colspan="1" rowspan="1">to_dict()</td><td colspan="1" rowspan="1">转为字典</td>

转为字典
<td colspan="1" rowspan="1">tolist()</td><td colspan="1" rowspan="1">转为列表</td>

转为列表
<td colspan="1" rowspan="1">unique()</td><td colspan="1" rowspan="1">元素排重</td>

元素排重



&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/b1030cbe2f8eb2bd5add3c19d2441962.gif">

微信扫码关注，了解更多内容
