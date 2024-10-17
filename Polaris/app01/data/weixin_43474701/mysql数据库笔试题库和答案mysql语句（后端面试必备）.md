
--- 
title:  mysql数据库笔试题库和答案mysql语句（后端面试必备） 
tags: []
categories: [] 

---


#### 数据库笔试题库（入门基础篇）
- <ul><li>- - - - 


### 一、入门基础题

### `基础查询`

**1、现在运营想要查看用户信息表中所有的数据，请你取出相应结果(1-6题共用一个表）**

**2、现在运营同学想要用户的设备id对应的性别、年龄和学校的数据，请你取出相应数据**

**3、现在运营需要查看用户来自于哪些学校，请从用户信息表中取出学校的去重数据。**

**4、现在运营只需要查看前2个用户明细设备ID数据，请你从用户信息表 user_profile 中取出相应结果。**

**5、现在你需要查看前2个用户明细设备ID数据，并将列名改为 ‘user_infos_example’,请你从用户信息表取出相应结果。**

**6、现在运营想要筛选出所有北京大学的学生进行用户调研，请你从用户信息表中取出满足条件的数据，结果返回设备id和学校。** <img src="https://img-blog.csdnimg.cn/3ca941394a6a4b3f9a7d0a46d4c0b734.png" alt="在这里插入图片描述"> **建表语句：`（最好能根据上表自己写出来，对于初级的笔试很可能会有建表的题写语句）`**

```

drop table if exists user_profile;
CREATE TABLE `user_profile` (
`id` int NOT NULL,
`device_id` int NOT NULL,
`gender` varchar(14) NOT NULL,
`age` int ,
`university` varchar(32) NOT NULL,
`province` varchar(32)  NOT NULL);
INSERT INTO user_profile VALUES(1,2138,'male',21,'北京大学','BeiJing');
INSERT INTO user_profile VALUES(2,3214,'male',null,'复旦大学','Shanghai');
INSERT INTO user_profile VALUES(3,6543,'female',20,'北京大学','BeiJing');
INSERT INTO user_profile VALUES(4,2315,'female',23,'浙江大学','ZheJiang');
INSERT INTO user_profile VALUES(5,5432,'male',25,'山东大学','Shandong');

```

`第一题答案`

```
selectid,device_id,gender,age,university,provincefrom user_profile
或者
select*from user_profile
实际应用中一般写列名，很少用*号。select 表列名 from 表名

```

<img src="https://img-blog.csdnimg.cn/9ffd0da0fc294b0db000729e72c08fa4.png" alt="在这里插入图片描述">

`第二题答案`

```
SELECT device_id,gender,age,university from user_profile

```

<img src="https://img-blog.csdnimg.cn/fbead81fc69747398545a9b41295c1af.png" alt="在这里插入图片描述">

`第三题答案`

```
二种方式
1.distinct 关键字
select distinct university from user_profiledistinct去重，放在列的前面使用。
2.分组SELECT
universityfrom user_profilegroup by university以分组来筛选出去重的结果

```

<img src="https://img-blog.csdnimg.cn/74d85da2e4724e828ecd5ad1ae8baac1.png" alt="在这里插入图片描述">

`第四题答案`

```
select device_id from user_profile limit 0,2---运行效率更高

select device_id from user_profile limit 2 ---运行效率低

也可结合 limit offset： 一起使用时，limit表示要取的数量，offset表示跳过的数量

select device_id from user_profile limit 2 offset 0 // 跳过0条，从第一条数据开始取，取两条数据 ---运行效率中

```

<img src="https://img-blog.csdnimg.cn/ff6f9b0a2306457c9c36a29f9856d784.png" alt="在这里插入图片描述">

`第五题答案`

```
select device_id as user_infors_example from user_profile limit 0,2;
这里主要是用到了 起别名关键字 as 以及组合限制查询 limit 索引,个数
其中as可以省略,索引为0可以省略
select device_id user_infors_example from user_profile limit 2;

```

<img src="https://img-blog.csdnimg.cn/fcb69fc1bacf4d98b79b2b1bedb58f84.png" alt="在这里插入图片描述">

`第六题答案`

```
SELECT device_id,university from user_profile where university='北京大学';

```

<img src="https://img-blog.csdnimg.cn/c17c9cda9ec044be9662993e2f824da7.png" alt="在这里插入图片描述">

### `条件查询`

**7、现在运营想要取出用户信息表中的用户年龄，请取出相应数据，并按照年龄升序排序。**

**8、现在运营想要取出用户信息表中的年龄和gpa数据，并先按照gpa升序排序，再按照年龄升序排序输出，请取出相应数据。** <img src="https://img-blog.csdnimg.cn/445d9c8907cc45fca1bdd5e16707b291.png" alt="在这里插入图片描述"> `建表语句`

```
drop table if exists user_profile;
CREATE TABLE `user_profile` (
`id` int NOT NULL,
`device_id` int NOT NULL,
`gender` varchar(14) NOT NULL,
`age` int ,
`university` varchar(32) NOT NULL,
`gpa` float);
INSERT INTO user_profile VALUES(1,2138,'male',21,'北京大学',3.4);
INSERT INTO user_profile VALUES(2,3214,'male',23,'复旦大学',4.0);
INSERT INTO user_profile VALUES(3,6543,'female',20,'北京大学',3.2);
INSERT INTO user_profile VALUES(4,2315,'female',23,'浙江大学',3.6);
INSERT INTO user_profile VALUES(5,5432,'male',25,'山东大学',3.8);
INSERT INTO user_profile VALUES(6,2131,'male',28,'北京师范大学',3.3);

```

`第七题答案`

```
SELECT device_id,age FROM user_profile ORDER BY age ASC; 结尾加 ASC是升序，不写也行因为默认升序。 
#SELECT device_id,age FROM user_profile ORDER BY age desc; 结尾加 desc 是降序。

```

<img src="https://img-blog.csdnimg.cn/9e675131798543aea9a080b92741a963.png" alt="在这里插入图片描述"> `第八题答案`

```
SELECT device_id,gpa,age from user_profile order by gpa,age;默认以升序排列
SELECT device_id,gpa,age from user_profile order by gpa,age asc;
SELECT device_id,gpa,age from user_profile order by gpa asc,age asc;

```

<img src="https://img-blog.csdnimg.cn/eb8219f0525e485d9c089eb14caf09ce.png" alt="在这里插入图片描述"> `基础操作符` **9、现在运营想要筛选出所有北京大学的学生进行用户调研，请你从用户信息表中取出满足条件的数据，结果返回设备id和学校。**

**10、现在运营想要针对24岁以上的用户开展分析，请你取出满足条件的设备ID、性别、年龄、学校。 用户信息表：user_profile**

**11、现在运营想要针对20岁及以上且23岁及以下的用户开展分析，请你取出满足条件的设备ID、性别、年龄。**

**12、现在运营想要查看除复旦大学以外的所有用户明细，请你取出相应数据**

**13、现在运营想要对用户的年龄分布开展分析，在分析时想要剔除没有获取到年龄的用户，请你取出所有年龄值不为空的用户的设备ID，性别，年龄，学校的信息。** <img src="https://img-blog.csdnimg.cn/842bf4aacc784e8fbea2f50acda5970a.png" alt="在这里插入图片描述"> `建表语句`

```
drop table if exists user_profile;
CREATE TABLE `user_profile` (
`id` int NOT NULL,
`device_id` int NOT NULL,
`gender` varchar(14) NOT NULL,
`age` int ,
`university` varchar(32) NOT NULL,
`province` varchar(32)  NOT NULL);
INSERT INTO user_profile VALUES(1,2138,'male',21,'北京大学','BeiJing');
INSERT INTO user_profile VALUES(2,3214,'male',null,'复旦大学','Shanghai');
INSERT INTO user_profile VALUES(3,6543,'female',20,'北京大学','BeiJing');
INSERT INTO user_profile VALUES(4,2315,'female',23,'浙江大学','ZheJiang');
INSERT INTO user_profile VALUES(5,5432,'male',25,'山东大学','Shandong');

```

`第九题答案`

```
select device_id,university from user_profile where university='北京大学';
#更具需求,首先知道要北京大学的学生,所有用条件university='北京大学'
#然后结果返回设备id和学校, 查询的字段是device_id,university

```

<img src="https://img-blog.csdnimg.cn/4e3d70d7653b479599e18331174deea5.png" alt="在这里插入图片描述"> `第十题答案`

```
select device_id,gender,age ,university from user_profile where age &gt;= 24;

```

<img src="https://img-blog.csdnimg.cn/70e29ac820484dc883db82ea47aff84b.png" alt="在这里插入图片描述">

`第十一题答案`

```
SELECT device_id, gender, age
FROM user_profile
WHERE age&gt;=20&amp;&amp;age&lt;=23;
 
SELECT device_id, gender, age
FROM user_profile
WHERE age&gt;=20 AND age&lt;=23;
 
SELECT device_id, gender, age
FROM user_profile
WHERE age BETWEEN 20 AND 23;

```

<img src="https://img-blog.csdnimg.cn/6b4f4d7cb2784cab8529dbbe8fd85622.png" alt="在这里插入图片描述"> `第一十二题答案`

```
SELECT device_id, gender,age,university FROM user_profile WHERE university NOT IN ("复旦大学")

select device_id, gender, age, university from user_profile where university != '复旦大学'

```

<img src="https://img-blog.csdnimg.cn/fde5ad92bd8946f4aedcbdfeeb8fadb4.png" alt="在这里插入图片描述"> `第十三题答案`

```
SELECT device_id,gender,age,university FROM user_profile  WHERE age IS NOT NUL

```

`高级操作符` **14、现在运营想要找到男性且GPA在3.5以上(不包括3.5)的用户进行调研，请你取出相关数据。**

**15、现在运营想要找到学校为北大或GPA在3.7以上(不包括3.7)的用户进行调研，请你取出相关数据（使用OR实现）**

**16、现在运营想要找到学校为北大、复旦和山大的同学进行调研，请你取出相关数据。**

<img src="https://img-blog.csdnimg.cn/77fa800d6bc248ffaed863091fe72bdb.png" alt="在这里插入图片描述">

`第十四题答案`

```
SELECT device_id,gender,age,university,gpa FROM user_profile WHERE gender = 'male' AND gpa &gt; 3.5

```

<img src="https://img-blog.csdnimg.cn/a0461bf62aec4af59e1b5a7c21d4bb92.png" alt="在这里插入图片描述">

`第十五题答案`

```
SELECT device_id,gender,age,university,gpa FROM user_profile
WHERE university='北京大学' OR gpa &gt; 3.7

```

<img src="https://img-blog.csdnimg.cn/af3044d87fd548ef8e87f3cdb148ca2c.png" alt="在这里插入图片描述">

`第十六题答案`

```
select device_id,gender,age,university,gpa from user_profile
where university in('北京大学','复旦大学','山东大学');

```

<img src="https://img-blog.csdnimg.cn/a2a7e59677134abf8c0d9082e8e8b72c.png" alt="在这里插入图片描述"> **17、现在运营想要找到gpa在3.5以上(不包括3.5)的山东大学用户 或 gpa在3.8以上(不包括3.8)的复旦大学同学进行用户调研，请你取出相应数据** `第十七题答案` <img src="https://img-blog.csdnimg.cn/c241ea43b6554bec8afab2a481965e82.png" alt="在这里插入图片描述">

```
select device_id,gender,age,university,gpa from user_profile where university='山东大学' and gpa&gt;3.5 or university='复旦大学' and gpa&gt;3.8 
--虽然短，但是执行用时长 
select device_id, gender, age, university, gpa from user_profile where device_id in (select device_id from user_profile where gpa&gt;3.5 and university='山东大学') or device_id in (select device_id from user_profile where gpa&gt;3.8 and university='复旦大学') 
--复杂的写法，子查询的方式 
--运行时间短

```

<img src="https://img-blog.csdnimg.cn/a0ce7e16574b4d13bcd1f5aa8709d8b4.png" alt="在这里插入图片描述"> **18、现在运营想查看所有大学中带有北京的用户的信息，请你取出相应数据。** <img src="https://img-blog.csdnimg.cn/4989dda8f5aa48b886ad00045148759f.png" alt="在这里插入图片描述"> `第十八题答案`

```
SELECT device_id,age,university FROM user_profile
WHERE university LIKE '%北京%'

```

<img src="https://img-blog.csdnimg.cn/977c6257cccd459cb1ff7232e748277d.png" alt="在这里插入图片描述">

>  
 **字符匹配** 一般形式为： 列名 [NOT ] LIKE 匹配串中可包含如下四种通配符： **：匹配任意一个字符； %：匹配0个或多个字符； [ ]：匹配[ ]中的任意一个字符(若要比较的字符是连续的，则可以用连字符“-”表 达 )； [^ ]：不匹配[ ]中的任意一个字符。 例23．查询学生表中姓‘张’的学生的详细信息。 SELECT * FROM 学生表 WHERE 姓名 LIKE ‘张%’ 例24．查询姓“张”且名字是3个字的学生姓名。 SELECT * FROM 学生表 WHERE 姓名 LIKE '张**_’ 如果把姓名列的类型改为nchar(20)，在SQL Server 2012中执行没有结果。原因是姓名列的类型是char(20)，当姓名少于20个汉字时，系统在存储这些数据时自动在后边补空格，空格作为一个字符，也参加LIKE的比较。可以用rtrim()去掉右空格。 SELECT * FROM 学生表 WHERE rtrim(姓名) LIKE ‘张__’ 例25.查询学生表中姓‘张’、姓‘李’和姓‘刘’的学生的情况。 SELECT * FROM 学生表 WHERE 姓名 LIKE '[张李刘]%’ 例26.查询学生表表中名字的第2个字为“小”或“大”的学生的姓名和学号。 SELECT 姓名,学号 FROM 学生表 WHERE 姓名 LIKE ‘_[小大]%’ 例27.查询学生表中所有不姓“刘”的学生。 SELECT 姓名 FROM 学生 WHERE 姓名 NOT LIKE '刘%’ 例28.从学生表表中查询学号的最后一位不是2、3、5的学生信息。 SELECT * FROM 学生表 WHERE 学号 LIKE ‘%[^235]’ 


### `高级查询`

`计算函数` **19、运营想要知道复旦大学学生gpa最高值是多少，请你取出相应数据** <img src="https://img-blog.csdnimg.cn/5664915852ce473cad0c7465144ad27f.png" alt="在这里插入图片描述">

**第十九题答案**

```
方法1
# select max(gpa) as gpa
# from user_profile
# where university='复旦大学';
 
# 方法2
select gpa
from user_profile
where university='复旦大学'
order by gpa desc limit 1

```

<img src="https://img-blog.csdnimg.cn/9e49cce4a1ed41e9b30a09b2fa68ccd2.png" alt="在这里插入图片描述"> **20、现在运营想要看一下男性用户有多少人以及他们的平均gpa是多少，用以辅助设计相关活动，请你取出相应数据。**

<img src="https://img-blog.csdnimg.cn/e8862175428442e7913969fb719cce1b.png" alt="在这里插入图片描述">

`第二十题答案`

```
#问题分解：
      #限定条件为 男性用户；
      #有多少人，明显是计数，count函数；
      #平均gpa，求平均值用avg函数；
select
  count(gender) as male_num,
  round(avg(gpa), 1) as avg_gpa
from user_profile where gender="male";

```

<img src="https://img-blog.csdnimg.cn/8d923294533546168064f8ce81b88700.png" alt="在这里插入图片描述"> `分组查询` **21、现在运营想要对每个学校不同性别的用户活跃情况和发帖数量进行分析，请分别计算出每个学校每种性别的用户数、30天内平均活跃天数和平均发帖数量。**

**22、现在运营想查看每个学校用户的平均发贴和回帖情况，寻找低活跃度学校进行重点运营，请取出平均发贴数低于5的学校或平均回帖数小于20的学校。**

**23、现在运营想要查看不同大学的用户平均发帖情况，并期望结果按照平均发帖情况进行升序排列，请你取出相应数据。** <img src="https://img-blog.csdnimg.cn/b2191159336e4919bd8152254da75ed2.png" alt="在这里插入图片描述">

`第二十一题答案`

```
select 
    gender, university,
    count(device_id) as user_num,
    avg(active_days_within_30) as avg_active_days,
    avg(question_cnt) as avg_question_cnt
from user_profile
group by gender, university

```

<img src="https://img-blog.csdnimg.cn/02b3e71b87c740c8b49525253cdd5278.png" alt="在这里插入图片描述">

`第二十二题答案`

```
select
    university,
    avg(question_cnt) as avg_question_cnt,
    avg(answer_cnt) as avg_answer_cnt
from user_profile
group by university
having avg_question_cnt&lt;5 or avg_answer_cnt&lt;20

```

<img src="https://img-blog.csdnimg.cn/0ec1e78a67db4c55b11beecdbb257c54.png" alt="在这里插入图片描述"> `第二十三题答案`

```
select university,
    avg(question_cnt) as avg_question_cnt
from user_profile
group by university
order by avg_question_cnt

```

<img src="https://img-blog.csdnimg.cn/88200753a7484a088a940a50723864b1.png" alt="在这里插入图片描述">

### `多表查询`

**24、现在运营想要查看所有来自浙江大学的用户题目回答明细情况，请你取出相应数据**

<img src="https://img-blog.csdnimg.cn/de0e7471f42f41739ac89f37ef9ce87f.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/3622acc00d434c7db446013af7231eb0.png" alt="在这里插入图片描述">

`第二十四题答案`

```
select qpd.device_id, qpd.question_id, qpd.result
from question_practice_detail as qpd
inner join user_profile as up
on up.device_id=qpd.device_id and up.university='浙江大学'
order by question_id


```

或者

```
select device_id, question_id, result
from question_practice_detail
where device_id in (
    select device_id from user_profile
    where university='浙江大学'
)
order by question_id


```

<img src="https://img-blog.csdnimg.cn/1b71b0b0844942cfab107aab6a4331b1.png" alt="在这里插入图片描述"> **25、运营想要了解每个学校答过题的用户平均答题数量情况，请你取出数据。**

<img src="https://img-blog.csdnimg.cn/de9b6a6ea90149c2b18def91be73b01d.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ac61d060a8e24646b405e2584b6b38f7.png" alt="在这里插入图片描述">

`第二十五题答案`

```
select university,
    count(question_id) / count(distinct qpd.device_id) as avg_answer_cnt
from question_practice_detail as qpd
inner join user_profile as up
on qpd.device_id=up.device_id
group by university

```

<img src="https://img-blog.csdnimg.cn/ba61b63f202e4ac6b3d877f783e5d630.png" alt="在这里插入图片描述">

**26、运营想要计算一些参加了答题的不同学校、不同难度的用户平均答题量，请你写SQL取出相应数据**

<img src="https://img-blog.csdnimg.cn/5689f49628f6463cbdf30e31bafe2ce9.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/6180d9f2e61c464199f09f5647372f04.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b8e585133b124cc993822653c79ac14c.png" alt="在这里插入图片描述">

`第二十六题答案`

```
select 
    university,
    difficult_level,
    round(count(qpd.question_id) / count(distinct qpd.device_id), 4) as avg_answer_cnt
from question_practice_detail as qpd

left join user_profile as up
on up.device_id=qpd.device_id

left join question_detail as qd
on qd.question_id=qpd.question_id

group by university, difficult_level


```

<img src="https://img-blog.csdnimg.cn/0bab4f12551546d7bb6f0d4d0fdc424e.png" alt="在这里插入图片描述">
