
--- 
title:  Mysql之数据处理及数据汇总函数 
tags: []
categories: [] 

---
## 一、mysql函数简介

  MySQL是一种关系型数据库管理系统，它提供了一组内置函数，用于处理和操作数据库中的数据。这些函数可以用于查询、插入、更新和删除数据，以及执行各种数学、字符串和日期操作。函数一般是在数据上执行的，它给数据的转换和处理提供了方便。博文将在mysql5.7.26版下创建一个test数据库，一张goods表为例，介绍各函数的使用。

>  
 mysql &gt;CREATE TABLE goods ( ID INT AUTO_INCREMENT PRIMARY KEY, goods_name VARCHAR(255), goods_price DECIMAL(10, 2), goods_num INT, goods_description TEXT ); mysql&gt; INSERT INTO goods (goods_name, goods_price, goods_num, goods_description) VALUES -&gt; (‘desk’, 10.00, 5, ‘这是商品1的描述’), -&gt; (‘book’, 20.00, 3, ‘这是商品2的描述’), -&gt; (‘papper’, 30.00, 7, ‘这是商品3的描述’), -&gt; (‘cup’, 40.00, 2, ‘这是商品4的描述’), -&gt; (‘apple’, 50.00, 8, ‘这是商品5的描述’), -&gt; (‘bag’, 60.00, 4, ‘这是商品6的描述’), -&gt; (‘mouse’, 70.00, 6, ‘这是商品7的描述’), -&gt; (‘pen’, 80.00, 9, ‘这是商品8的描述’), -&gt; (‘lunch_box’, 90.00, 1, ‘这是商品9的描述’), -&gt; (‘bench’, 100.00, 10, ‘这是商品10的描述’); Query OK, 10 rows affected (0.07 sec) Records: 10 Duplicates: 0 Warnings: 0 <img src="https://img-blog.csdnimg.cn/8fb317b063ae45388ebed91138c2a841.png" alt="在这里插入图片描述"> 


## 二、数据处理函数使用示例

### 1、文本处理函数

  常用文本处理函数如下，有去掉字符串空格的函数，返回字符串长度的函数，有转换大小写的函数等等。

<th align="left">函数</th><th align="left">说明</th>
|------
<td align="left">Left()</td><td align="left">返回串左边的字符将串</td>
<td align="left">Length()</td><td align="left">返回串的长度</td>
<td align="left">Locate()</td><td align="left">找出串的一个子串</td>
<td align="left">Lower()</td><td align="left">转换为小写</td>
<td align="left">LTrim()</td><td align="left">去掉串左边的空格</td>
<td align="left">Right()</td><td align="left">返回串右边的字符</td>
<td align="left">RTrim()</td><td align="left">去掉串右边的空格</td>
<td align="left">Soundex()</td><td align="left">返回串的SOUNDEX值</td>
<td align="left">Substring()</td><td align="left">返回子串的字符</td>
<td align="left">Upper()</td><td align="left">将串转换为大写</td>
<td align="left">concat()</td><td align="left">字符串拼接函数，将多个字符串拼接为一个字符串</td>
- 将商品名转换为大写
>  
 mysql&gt; select Upper(goods_name) as good_name_up from goods; <img src="https://img-blog.csdnimg.cn/8c61edc427e44521874b7aaa33faae14.png" alt="在这里插入图片描述"> 

- 返回商品名字段值字符串长度
>  
 mysql&gt; select length(goods_name) as good_name_len from goods; <img src="https://img-blog.csdnimg.cn/35eb628b55e74470b362b474bc4f399d.png" alt="在这里插入图片描述"> 

- 拼接商品名和描述字段
>  
 mysql&gt; select concat(goods_name,goods_description) as good_name_and_des from goods; <img src="https://img-blog.csdnimg.cn/ddd5e97d081746a3bad65172d07caf29.png" alt="在这里插入图片描述"> 

- 获取商品名字段字符串前3个字符子串
>  
 mysql&gt; select substring(goods_name,1,3) as su_goods_name from goods; <img src="https://img-blog.csdnimg.cn/4e24d68bf902491f88263ef907558334.png" alt="在这里插入图片描述"> #substring(str,start,length)格式，即需要输入字段名、开始位置，长度三个参数。 


### 2、日期和时间处理函数

  mysql自带有很多日期和时间处理函数，可以用于处理日期和时间字段。

<th align="left">函数</th><th align="left">说明</th>
|------
<td align="left">AddDate()</td><td align="left">增加一个日期(天、周等)</td>
<td align="left">AddTime()</td><td align="left">增加一个时间(时、分等)</td>
<td align="left">CurDate()</td><td align="left">返回当前日期</td>
<td align="left">CurTime()</td><td align="left">返回当前时间</td>
<td align="left">Date()</td><td align="left">返回日期时间的日期部分</td>
<td align="left">DateDiff()</td><td align="left">计算两个日期之差</td>
<td align="left">Date_Add()</td><td align="left">高度灵活的日期运算函数</td>
<td align="left">Date_Format()</td><td align="left">返回一个格式化的日期或时间串</td>
<td align="left">Day()</td><td align="left">返回一个日期的天数部分</td>
<td align="left">Dayofweek()</td><td align="left">对于一个日期，返回对应的星期几</td>
<td align="left">Hour()</td><td align="left">返回一个时间的小时部分</td>
<td align="left">Minute()</td><td align="left">返回一个时间的分钟部分</td>
<td align="left">Month()</td><td align="left">返回一个日期的月份部分</td>
<td align="left">Now()</td><td align="left">返回当前日期和时间</td>
<td align="left">Second()</td><td align="left">返回一个时间的秒部分</td>
<td align="left">Time()</td><td align="left">返回一个日期时间的时间部分</td>
<td align="left">Year()</td><td align="left">返回一个日期的年份部分</td>
- 获取当前日期和时间
>  
 mysql&gt; select now(); ±--------------------+ | now() | ±--------------------+ | 2023-07-27 11:17:58 | ±--------------------+ 1 row in set (0.00 sec) 

- 获取当前日期
>  
 mysql&gt; select curdate(); ±-----------+ | curdate() | ±-----------+ | 2023-07-27 | ±-----------+ 1 row in set (0.00 sec) 

- 获取当前时间
>  
 mysql&gt; select curtime(); ±----------+ | curtime() | ±----------+ | 11:20:26 | ±----------+ 1 row in set (0.00 sec) 

- 返回时间的日期部分
>  
 mysql&gt; select date(now()); ±------------+ | date(now()) | ±------------+ | 2023-07-27 | ±------------+ 1 row in set (0.00 sec) #date()函数常用于处理时间字段，时间字段包含日期和时间时，如果需要进行分组或者排序需要进行提取时间字段中的部分信息就可以使用，我们还可以提前其中的年份、月份、日期、时、分、秒等。 

- 某日期增加一个天数或者星期
>  
 mysql&gt; select adddate(‘2023-05-01’,interval 30 day); ±--------------------------------------+ | adddate(‘2023-05-01’,interval 30 day) | ±--------------------------------------+ | 2023-05-31 | ±--------------------------------------+ 1 row in set (0.00 sec) 

- 计算两个日期相差天数
>  
 mysql&gt; select datediff(‘1986-06-01’,‘2023-07-27’); ±------------------------------------+ | datediff(‘1986-06-01’,‘2023-07-27’) | ±------------------------------------+ | -13570 | ±------------------------------------+ 1 row in set (0.00 sec) 


### 3、数值处理函数

  数值处理函数仅处理数值数据。这些函数一般主要用于代数、三角或几何运算，因此没有串或日期—时间处理函数的使用那么频繁。在各类数据库管理系统中，数值函数基本是上一样的。

<th align="left">函数</th><th align="left">说明</th>
|------
<td align="left">Abs()</td><td align="left">返回一个数的绝对值</td>
<td align="left">Cos()</td><td align="left">返回一个角度的余弦</td>
<td align="left">Exp()</td><td align="left">返回一个数的指数值</td>
<td align="left">Mod()</td><td align="left">返回除操作的余数</td>
<td align="left">Pi()</td><td align="left">返回圆周率</td>
<td align="left">Rand()</td><td align="left">返回一个随机数</td>
<td align="left">Sin()</td><td align="left">返回一个角度的正弦</td>
<td align="left">sqrt()</td><td align="left">返回一个数的平方根</td>
<td align="left">Tan()</td><td align="left">返回一个角度的正切</td>
<td align="left">RADIANS()</td><td align="left">将角度转换为弧度</td>
- 返回一个随机数
>  
 mysql&gt; select rand(); ±-------------------+ | rand() | ±-------------------+ | 0.7540961585511418 | ±-------------------+ 1 row in set (0.00 sec) 

- 获取圆周率
>  
 mysql&gt; select pi(); ±---------+ | pi() | ±---------+ | 3.141593 | ±---------+ 1 row in set (0.00 sec) 

- 计算90度的正弦值
>  
 mysql&gt; select sin(RADIANS(90)); ±-----------------+ | sin(RADIANS(90)) | ±-----------------+ | 1 | ±-----------------+ 1 row in set (0.00 sec) 

- 计算9的平方根
>  
 mysql&gt; select sqrt(9); ±--------+ | sqrt(9) | ±--------+ | 3 | ±--------+ 1 row in set (0.00 sec) 

- 查询商品表中剩余偶数件的商品
>  
 mysql&gt; select goods_name,goods_num from goods where mod(goods_num,2)=0; ±-----------±----------+ | goods_name | goods_num | ±-----------±----------+ | cup | 2 | | apple | 8 | | bag | 4 | | mouse | 6 | | bench | 10 | ±-----------±----------+ 5 rows in set (0.00 sec) 


## 三、数据汇总函数使用示例

  我们经常需要汇总数据而不用把它们实际检索出来，为此MySQL提供了专门的函数。使用这些函数，MySQL查询可用于检索数据，以便分析和报表生成。

<th align="left">函数</th><th align="left">说明</th>
|------
<td align="left">AVG()</td><td align="left">返回某列的平均值</td>
<td align="left">COUNT()</td><td align="left">返回某列的行数</td>
<td align="left">MAX()</td><td align="left">返回某列的最大值</td>
<td align="left">MIN()</td><td align="left">返回某列的最小值</td>
<td align="left">SUM()</td><td align="left">返回某列值之和</td>
- 求商品价格的平均值
>  
 mysql&gt; select avg(goods_price) from goods; ±-----------------+ | avg(goods_price) | ±-----------------+ | 55.000000 | ±-----------------+ 1 row in set (0.01 sec) 

- 统计商品的数量
>  
 mysql&gt; select count(**) from goods; ±---------+ | count(**) | ±---------+ | 10 | ±---------+ 1 row in set (0.00 sec) 

- 查找单价最高的商品
>  
 mysql&gt; select goods_name,goods_price from goods where goods_price in (select max(goods_price) from goods); ±-----------±------------+ | goods_name | goods_price | ±-----------±------------+ | bench | 100.00 | ±-----------±------------+ 1 row in set (0.00 sec) 

- 查找剩余数量最少的商品
>  
 mysql&gt; select goods_name,goods_num from goods where goods_num in (select min(goods_num) from goods); ±-----------±----------+ | goods_name | goods_num | ±-----------±----------+ | lunch_box | 1 | ±-----------±----------+ 1 row in set (0.00 sec) 

- 计算商品销售总计可以获得的金额
>  
 mysql&gt; select sum(goods_price*goods_num) as sum_sale from goods; ±---------+ | sum_sale | ±---------+ | 3270.00 | ±---------+ 1 row in set (0.00 sec) 

